# 워크시트 6: 작성표 ② (README 여섯 칸 설계)

> **작성 기준:** 처음 보는 사람(짝)이 코드를 열어보지 않고 `README.md`만 읽고 3분 안에 실행 및 테스트할 수 있도록 작성합니다.

| 칸 번호 | 항목 | 내가 적는 내용 (`README.md`에 반영) |
| :--- | :--- | :--- |
| **① What** | 프로그램 소개 (한 문장) | 학생들의 성적 CSV 파일을 읽어 유효한 점수(0~100점 정수)만 선별하고 잘못된 행은 사유와 함께 건너뛰는 프로그램입니다. |
| **② Why ★** | 만든 이유 (AI가 대신 쓸 수 없는 맥락) | 실제 성적 데이터에는 빈 줄, 100점 초과나 음수 점수, 빈 칸, 열 개수 오류 등이 섞여 있어 단순 파일 읽기로는 프로그램이 중단되거나 잘못된 성적이 집계되기 때문입니다. |
| **③ How** | 설치 및 실행 명령 | ```bash
pip install pytest pytest-cov
python3 load_scores.py scores.csv
``` |
| **④ 테스트** | `pytest` 실행 방법 및 통과 화면 | ```bash
pytest
pytest --cov=load_scores --cov-report=term-missing
```
*(통과 화면: `12 passed in 0.04s`)* |
| **⑤ 파일 구성** | 저장소 내 주요 파일 설명 | - `load_scores.py`: 성적 CSV 파싱 및 유효성 검증 핵심 모듈<br>- `test_load_scores.py`: 명세 기반 직접 작성 `pytest` 단위 테스트<br>- `test_ai_A.py`: AI에게 코드를 주고 생성한 테스트<br>- `test_ai_B.py`: AI에게 명세를 주고 생성한 테스트<br>- `scores.csv`, `empty.csv`, `weird.csv`: 실행 및 테스트용 CSV 데이터<br>- `LICENSE`: MIT 라이선스 |
| **⑥ 만든 사람** | 작성자 · AI 활용 · 직접 판단 | - 만든 사람 : 한국기술교육대학교 학번 이름 *(본인 학번/이름 기입)*<br>- AI를 쓴 곳 : `prompts.txt` 조건에 따른 AI 테스트(`test_ai_A.py`, `test_ai_B.py`) 생성 및 `README.md` 초안 정리<br>- 내가 직접 판단한 것 : 코드를 보지 않고 명세서 6칸 기반 8개 테스트 케이스 설계, 경계값(`0·100·101`) 검증, AI 코드 기반 테스트의 버그 고착(`== 85`) 여부 판별 |

### 완료 확인
- [x] 여섯 칸 모두 작성
- [x] 명령을 직접 실행해 봄
- [x] 테스트 화면 캡처 (README ④번에 터미널 결과 붙여넣기)
- [x] 커밋하고 `push` 완료
