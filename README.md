# 🍽️ LastPlate

급식 수요를 예측하고 안전 조리량·발주량·재고 우선소진을 추천하는 ESG 해커톤 MVP입니다.

**현재 구현:** Streamlit 입력 화면 → LangGraph 3개 노드 → 규칙 기반 예상 식수 → 안전 조리량 → kg 단위 발주 추천 → 소비기한 순 재고 배분.
**아직 미구현:** XGBoost/LightGBM 학습, 자연어 입력, LLM 설명, RAG 검색. 데모를 실제 예측 성능이나 폐기 감소 실적으로 소개하지 마세요.

## 처음 실행하기 (Windows)

Python 3.11과 Git을 설치합니다. PowerShell을 열어 저장소를 받은 뒤 실행하세요.

```powershell
git clone https://github.com/PARK-TAEGEON/lastplate.git
cd lastplate
py -3.11 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
Copy-Item .env.example .env
.\.venv\Scripts\python.exe -m streamlit run app.py
```

비공개 저장소는 초대를 수락한 GitHub 계정으로 인증해야 합니다. `.env`가 이미 있으면 복사 단계를 건너뛰세요. 초기 데모에는 API 키가 필요하지 않습니다. 가상환경 활성화를 생략하므로 PowerShell 실행 정책을 바꿀 필요도 없습니다.

macOS/Linux에서는 `python3.11 -m venv .venv` 후 `.venv/bin/python -m pip install -r requirements.txt`, `cp .env.example .env`, `.venv/bin/python -m streamlit run app.py`를 사용하세요.

패키지 버전 범위는 초기 설치용이며 고정 환경은 아닙니다. 팀 실행 환경을 확인한 후 통합 담당자가 같은 Python 버전에서 `python -m pip freeze` 결과를 검토하여 별도 lock 파일로 공유하세요.

## 팀원 5명 역할

| 역할 | 맡는 파일 | 완료 기준 |
|---|---|---|
| 1. 통합 담당 | graph.py, requirements.txt, 저장소 설정 | 전체 실행, PR 검토, 최종 시연 |
| 2. 수요예측 | tools/demand.py, models/, scripts/ | 날짜 분리 평가와 predict_demand 반환 규격 유지 |
| 3. 발주·재고 | tools/order.py, tools/inventory.py | kg 단위 계산, 소비기한과 재고 배분 확인 |
| 4. Agent·RAG | rag/, 향후 자연어 처리 모듈 | 추가 인원 입력과 근거 문서 연결 |
| 5. UI·데모·발표 | app.py, data/demo/, docs/ | 입력/결과 화면, 시연 시나리오 |

Agent 담당이 graph.py를 바꾸려면 통합 담당과 먼저 합의합니다. 같은 파일은 두 사람이 동시에 수정하지 않는 것을 기본으로 합니다.

## Git을 쉽게 이해하기

- GitHub 저장소: 공용 프로젝트 보관함
- `main`: 제출·시연에 쓰는 최종본
- 브랜치: 각자 작업하는 사본
- commit: 내 컴퓨터에 변경 묶음 저장
- push: GitHub에 내 저장 내용을 올림
- PR (Pull Request): 최종본에 합쳐 달라는 검토 요청
- pull: 합쳐진 최신 최종본을 내 컴퓨터로 받음

해커톤에서는 **main + 짧은 작업 브랜치**만 사용합니다. develop 브랜치는 만들지 않습니다. 통합 담당자가 PR을 확인하고 합칩니다. 브랜치는 로컬 폴더 복사가 아니므로, 전환하기 전 저장 상태를 확인하세요.

## 매일 작업 순서

작업 시작 전에 `git status`를 확인하세요. 변경 파일이 남아 있다면 먼저 자신의 작업 브랜치에서 저장하거나 통합 담당자에게 도움을 요청하세요.

```powershell
git switch main
git pull --ff-only origin main
git switch -c feat/demand-baseline
# 맡은 파일만 수정하고 앱 실행 확인
git status
git add tools/demand.py
git diff --cached
git commit -m "feat: add demand baseline"
git push -u origin feat/demand-baseline
```

GitHub의 **Compare & pull request**를 눌러 main 대상으로 PR을 만들고, 바꾼 내용과 확인 방법을 씁니다. 통합 담당자는 변경 내용·실행 결과·비밀정보 포함 여부를 확인하고 **Squash and merge**로 합칩니다. 합쳐진 뒤 main으로 돌아가 최신 파일을 받습니다. 새 작업은 새 브랜치에서 시작하세요.

브랜치 예시: `feat/order-inventory`, `feat/rag-search`, `feat/ui-demo`, `fix/demo-error`. 동일 이름이 이미 있으면 `feat/ui-demo-2`처럼 새 이름을 쓰세요. 저장할 파일을 명시하며, 잘 모를 때 `git add .`를 사용하지 않습니다.

충돌이나 pull 오류가 나오면 멈추고 통합 담당자에게 알려주세요. `git reset --hard`, `git clean`, 강제 push로 해결하지 마세요. 자세한 복구 안내는 [협업 가이드](docs/team-guide.md)를 참고하세요.

## 프로젝트 구조

```text
lastplate/
├── app.py                 # Streamlit 화면
├── graph.py               # LangGraph 조립
├── tools/                 # 수요·조리·발주·재고 계산
├── rag/documents/         # 합성 운영 지침, 향후 RAG 자료
├── data/demo/             # 공개 가능한 합성 CSV
├── data/raw/              # 로컬 원본, Git 제외
├── data/processed/        # 로컬 전처리 데이터, Git 제외
├── models/                # 로컬 학습 모델, Git 제외
├── scripts/               # 향후 전처리·학습 스크립트
├── tests/                 # 핵심 계산 검증
├── docs/                  # 팀원 안내와 데모 시나리오
├── .github/               # PR 양식과 자동 계산 검증
├── requirements.txt
├── .env.example           # 빈 설정 양식
└── .gitignore
```

## 데이터와 함수 규격

`demand_history.csv`: date, employees, attendance_rate(0~1), actual_meals. 5행은 형식 확인용입니다.
`recipes.csv`: ingredient, kg_per_person. 현재 하나의 메뉴이며 ingredient는 한 번씩만 적습니다.
`inventory.csv`: lot_id, ingredient, stock_kg, expiry_date(YYYY-MM-DD). 재료 이름이 레시피와 정확히 같아야 합니다.

`predict_demand()`는 prediction, method, is_trained_model을 반환합니다. 안전 조리량은 예상 식수에 안전여유를 적용한 올림값입니다. **안전여유는 예측구간이 아닙니다.** 발주는 사용 가능한 재고를 차감한 부족량이며 결과 표시 단위는 kg, 소수점 3자리입니다. 실제 포장 단위·최소 발주량은 추후 추가합니다.

## 시연과 검증

기본 데모는 2026-09-17, 기본 600명, 참석률 80%, 안전여유 5%로 고정합니다. 예상 식수 480명, 안전 조리량 504명입니다. 추가 35명 입력 시 각각 515명, 541명으로 증가합니다. 자세한 발주값은 [데모 시나리오](docs/demo-scenario.md)에 있습니다.

```powershell
.\.venv\Scripts\python.exe -m unittest discover -s tests -v
```

## 저장소 소유자가 할 설정

1. Settings → Collaborators에서 팀원 4명을 초대하고 각자 수락합니다.
2. 계정/요금제에서 지원하면 main 보호 규칙 또는 ruleset에 PR 필수, 승인 1명, 강제 push·삭제 금지를 설정합니다.
3. 자동 검증이 성공한 뒤 `core-calculations`를 필수 검사로 선택합니다.

이 안내 자체가 GitHub 보호 설정을 적용하지는 않습니다. 보호 기능을 사용할 수 없는 비공개 저장소에서는 통합 담당자만 main을 변경하는 팀 규칙을 지키세요. 공개 전환과 라이선스 선택은 팀 및 데이터 이용 조건을 확인한 뒤 결정합니다.

API 키·개인정보·실제 급식 원본은 올리지 않습니다. 키가 노출되면 파일 삭제만으로 해결되지 않으므로 즉시 키를 폐기/재발급하고 통합 담당자에게 알려주세요.

공식 참고: [Streamlit 설치](https://docs.streamlit.io/get-started/installation), [LangGraph 설치](https://docs.langchain.com/oss/python/langgraph/install), [GitHub 저장소 생성](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-new-repository).
