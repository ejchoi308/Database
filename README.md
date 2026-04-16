## 1단계: VS Code 준비<br>
VS Code 설치 및 Python Extension 설치 (필수)<br>
<br>
<br>
## 2단계: 프로젝트 폴더 및 파일 준비my_db_project 폴더 생성<br>
그 안에 templates 폴더 생성<br>
파일 배치:<br>
app.py (프로젝트 루트)<br>
myDB.db (프로젝트 루트 - 이름 확인!)<br>
templates/index.html (홈 - HTML 파일)<br>
templates/layout.html (메뉴 및 스타일 - HTML 파일)<br>
templates/customer_list.html (고객목록 - HTML 파일)<br>
templates/product_list.html (제품목록 - HTML 파일)<br>
코드 수정:<br>
app.py 파일안에서 <br>
DB 이름 변경 : conn = sqlite3.connect('myDB.db')<br>
테이블 이름 변경 : conn.execute('SELECT * FROM TBL_CUST').fetchall()<br>
<br>
<br>
## 3단계: uv 설치 및 초기화 (터미널)<br>
터미널에서<br>
%> cd my_db_project<br>
<br>
### 1. uv 설치 <br>
uv는 Rust로 구현된 초고속 Python 패키지 및 프로젝트 관리 도구<br>
기존의 pip, pip-tools, pipx, poetry, pyenv, virtualenv 등을 하나로 통합하여 대체할 수 있는 강력한 도구<br>
<br>
%> powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"<br>
<br>
### 2.  프로젝트  초기화<br>
%> uv init<br>
(pyproject.toml과 .python-version 파일이 자동으로 생깁니다.)<br>
<br>
<br>
## 4단계: Flask 라이브러리 추가<br>
%> uv add flask<br>
(.venv(가상환경) 폴더가 자동으로 만들어지므로 아주 편합니다.)<br>
(uv add flask를 마친 후, VS Code 오른쪽 하단에서 <br>
파이썬 인터프리터를 **./.venv/Scripts/python.exe**로 선택해 주면 코드의 노란 줄도 사라집니다.)<br>
<br>
<br>
## 5단계: 서버 실행 및 확인<br>
%> uv run app.py<br>
<br>
<br>
## 6단계: 확인<br>
브라우저 주소창: http://127.0.0.1:5000<br>
