"""Run: python -m streamlit run app.py"""
import csv
from pathlib import Path
from datetime import date
import streamlit as st
from dotenv import load_dotenv
from graph import build_graph

ROOT = Path(__file__).resolve().parent
load_dotenv(ROOT / ".env")


def read_demo(name):
    with (ROOT / "data" / "demo" / name).open(encoding="utf-8", newline="") as file:
        return list(csv.DictReader(file))


st.set_page_config(page_title="LastPlate", page_icon="🍽️")
st.title("🍽️ LastPlate")
st.caption("식수 예측 → 안전 조리량 → 발주 추천 → 재고 우선소진")
st.info("합성 데이터와 규칙 기반 예측을 사용하는 초기 데모입니다. 학습 모델·LLM·RAG는 아직 연결되지 않았습니다.")
with st.form("meal"):
    day = st.date_input("급식 예정일", value=date(2026, 9, 17))
    employees = st.number_input("기본 인원", min_value=0, value=600, step=1)
    attendance = st.slider("예상 참석률 (%)", 0, 100, 80)
    extra = st.number_input("외부 추가 인원 (예: 35)", min_value=0, value=0, step=1)
    safety = st.slider("안전여유 (%)", 0, 30, 5)
    submitted = st.form_submit_button("계산하기")
if submitted:
    try:
        result = build_graph().invoke({"employees": employees, "attendance_rate": attendance / 100,
            "extra_people": extra, "safety_rate": safety / 100, "service_date": day.isoformat(),
            "recipes": read_demo("recipes.csv"), "lots": read_demo("inventory.csv")})
        left, right = st.columns(2)
        left.metric("예상 식수", result["demand"]["prediction"])
        right.metric("안전 조리량", result["cooking_quantity"])
        st.subheader("발주 추천 (kg)")
        st.dataframe([{k: v for k, v in order.items() if k != "allocations"} for order in result["orders"]], hide_index=True)
        st.subheader("사용 가능한 재고: 소비기한이 빠른 순서")
        st.dataframe(result["eligible_lots"], hide_index=True)
        with st.expander("재고별 사용량 보기"):
            st.json(result["orders"])
        st.caption("발주는 추천값입니다. 실제 발주 전 담당자가 재고 상태와 레시피를 검수해야 합니다.")
    except (ValueError, OSError, KeyError) as error:
        st.error(f"입력값 또는 데모 데이터를 확인하세요: {error}")
