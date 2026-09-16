# 비개발자 팀 협업 안내

## 시작 전 10분

통합 담당자 1명을 정하고 README 역할 표에 실제 이름을 적습니다. 모두 저장소 초대를 수락하고, 같은 Python 3.11 환경에서 앱을 실행해 봅니다. 브랜치를 하나씩 만들고 자신의 파일만 수정하여 작은 PR을 올리는 연습을 합니다.

## GitHub Desktop으로 작업하기

1. File → Clone repository에서 lastplate를 받습니다.
2. Current Branch가 main인지 확인하고 Fetch origin → Pull origin으로 최신 파일을 받습니다.
3. Branch → New branch에서 `feat/ui-demo`처럼 작업 브랜치를 만듭니다.
4. 맡은 파일을 수정하고 앱을 실행합니다.
5. Changes에서 필요한 파일만 선택하고 Summary에 변경 내용을 적어 Commit합니다.
6. Publish branch 또는 Push origin 후 Create Pull Request를 누릅니다.
7. 통합 담당자가 합친 뒤 main으로 돌아와 Fetch/Pull합니다.

화면에 .env나 원본 데이터가 변경 목록으로 보이면 업로드하지 말고 통합 담당자에게 알립니다.

## 문제가 생기면

- `Author identity unknown`: `git config --local user.name "본인 이름"` 및 `git config --local user.email "본인의 GitHub 등록 이메일 또는 GitHub 제공 noreply 이메일"`을 설정합니다. 다른 팀원의 신원을 사용하지 않습니다.
- 브랜치 전환이 거절됨: 변경 사항이 남아 있는 상태입니다. 현재 브랜치와 변경 파일을 확인하고 저장 방법을 통합 담당자와 정합니다.
- 충돌 표시: 통합 담당자가 함께 수정합니다. GitHub Desktop에서는 충돌을 해결하기 어렵다면 Abort merge로 병합 시도를 취소할 수 있습니다. 강제로 파일을 버리지 않습니다.
- push 거절 또는 저장소 없음: 계정, 초대 수락, 저장소 주소를 확인합니다. 비밀번호 대신 GitHub 인증 화면을 사용합니다.
- ModuleNotFoundError: README에 있는 가상환경 Python으로 requirements 설치와 앱 실행을 모두 수행했는지 확인합니다.

## AI에게 코드 작업을 요청할 때

"LastPlate의 tools/demand.py만 수정해 주세요. README의 함수 반환 규격을 유지하고 합성 데이터로 검증하세요. API 키와 원본 데이터를 커밋하지 말고, main에 직접 push하지 마세요."

AI가 바꾼 파일도 사람이 PR에서 확인합니다. 다른 담당 영역을 바꿔야 하면 먼저 상의합니다.
