from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('myDB.db')
    conn.row_factory = sqlite3.Row  # 컬럼명으로 데이터에 접근 가능하게 설정
    return conn

@app.route('/customer_list')
def customer_list():
    # URL 파라미터 읽기
    sort_column = request.args.get('sort', 'id') 
    search_type = request.args.get('search_type')
    search_query = request.args.get('search_query')

    conn = get_db_connection()
    
    # 기본 쿼리
    query = "SELECT id, name, age, grade, job, point FROM TBL_CUST"
    params = []

    # [수정 1] 검색 조건 처리
    if search_type and search_query:
        # WHERE를 사용하여 조건을 시작합니다. 
        # 보안을 위해 ?(플레이스홀더)를 사용합니다.
        query += f" WHERE {search_type} LIKE ?"
        params.append(f"%{search_query}%")

    # [수정 2] 정렬 처리
    # 정렬 컬럼은 파라미터 바인딩(?)이 되지 않으므로 화이트리스트 체크가 권장되나, 
    # 일단 문법적으로 WHERE 뒤에 오도록 구성합니다.
    if sort_column:
        query += f" ORDER BY {sort_column} ASC"

    # 최종 쿼리 실행
    try:
        data = conn.execute(query, params).fetchall()
    except Exception as e:
        print(f"쿼리 실행 에러: {e}")
        data = []
    finally:
        conn.close()
    
    return render_template('customer_list.html', data=data)

@app.route('/product_list')
def product_list():
    # URL 파라미터 읽기
    sort_column = request.args.get('sort', 'pno') 
    search_type = request.args.get('search_type')
    search_query = request.args.get('search_query')

    conn = get_db_connection()
    
    # 기본 쿼리
    query = "SELECT pno, pname, stock, price, brand FROM TBL_PROD"
    params = []

    # [수정 1] 검색 조건 처리
    if search_type and search_query:
        # WHERE를 사용하여 조건을 시작합니다. 
        # 보안을 위해 ?(플레이스홀더)를 사용합니다.
        query += f" WHERE {search_type} LIKE ?"
        params.append(f"%{search_query}%")

    # [수정 2] 정렬 처리
    # 정렬 컬럼은 파라미터 바인딩(?)이 되지 않으므로 화이트리스트 체크가 권장되나, 
    # 일단 문법적으로 WHERE 뒤에 오도록 구성합니다.
    if sort_column:
        query += f" ORDER BY {sort_column} ASC"

    # 최종 쿼리 실행
    try:
        data = conn.execute(query, params).fetchall()
    except Exception as e:
        print(f"쿼리 실행 에러: {e}")
        data = []
    finally:
        conn.close()
    
    return render_template('product_list.html', data=data)

# 나머지 페이지들도 미리 라우트만 만들어둡니다.
@app.route('/order_list')
def order_list():
    return "주문조회 페이지 (준비 중)"

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
