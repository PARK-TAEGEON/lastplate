# 학습 모델 보관 위치

학습 완료 모델은 이 폴더에 로컬 저장합니다. 모델 파일은 Git에서 제외합니다.
원본 데이터 이용 조건을 먼저 확인하고, 날짜 기준 학습/검증 분리로 MAE를 평가하세요.
demo/demand_history.csv의 5행은 형식 확인용 합성 데이터이며 성능 평가에 사용할 수 없습니다.
향후 scripts/train.py에서 XGBoost 또는 LightGBM 중 하나를 학습하고 tools/demand.py에 연결하세요.
