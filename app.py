from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('myDB.db')
    conn.row_factory = sqlite3.Row  # 컬럼명으로 데이터에 접근 가능하게 설정
    return conn

@app.route('/')
def index():
    # URL 파라미터 읽기 (예: /?sort=name&search_type=id&search_query=admin)
    sort_column = request.args.get('sort', 'id')  # 기본값 id
    search_type = request.args.get('search_type')
    search_query = request.args.get('search_query')

    conn = get_db_connection()
    
    # 기본 쿼리
    query = "SELECT id, name, age, grade, job, point FROM TBL_CUST"
    params = []

    # [작성 포인트 1] 검색 조건 처리 (WHERE 절)
    if search_type and search_query:
        query += f" AND {search_type} LIKE '%{search_query}%'"
        #params.append(f"%{search_query}%")
        pass 

    # [작성 포인트 2] 정렬 처리 (ORDER BY 절)
    if sort_column:
        query += f" ORDER BY {sort_column} ASC"
        pass

    data = conn.execute(query, params).fetchall()
    conn.close()
    
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)