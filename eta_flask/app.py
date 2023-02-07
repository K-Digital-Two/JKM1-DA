import os
from flask import Flask, jsonify, request, Response
from flask_cors import CORS
from flask_mysqldb import MySQL
# .env 환경변수 사용
from dotenv import load_dotenv

# json한글깨짐 해결
import json
from functools import wraps


#Flask 객체 인스턴스 생성
app = Flask(__name__)
CORS(app)


# MySQL 계정정보 등록
load_dotenv()

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
CORS(app)
mysql = MySQL(app)

app.config['MYSQL_USER'] = os.getenv("MYSQL_USER")
app.config['MYSQL_PASSWORD'] = os.getenv("MYSQL_PASSWORD")
app.config['MYSQL_HOST'] = os.getenv("MYSQL_HOST")
app.config['MYSQL_DB'] = os.getenv("MYSQL_DB")

# API 생성(GET, POST): react와 통신하기 위해 GET과 POST데이터를 조회하고 생성하는 API
@app.route('/', methods=['GET', 'POST'])
def shiplog():
    if request.method == 'GET':
        # MySQL 서버에 접속하기
        cur = mysql.connection.cursor()
        # MySQL 명령어 실행하기
        cur.execute("SELECT * FROM ship")
        # 전체 row 가져오기
        res = cur.fetchall()
        # Flask에서 제공하는 json변환 함수
        return jsonify(res)

    if request.method == 'POST':
        ship_shipId = request.json['ship_shipId']
        # mysql 접속 후 cursor 생성하기
        cur = mysql.connection.cursor()
        # DB 데이터 삽입하기
        cur.executemany("INSERT INTO shiplog VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", [ship_shipId])
        # DB에 수정사항 반영하기
        mysql.connection.commit()
        # mysql cursor 종료하기
        cur.close()
        return


if __name__ == '__main__':
    # 코드 수정시 자동 반영
    app.run(debug=True)