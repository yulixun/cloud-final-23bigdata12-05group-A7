from flask import Flask, jsonify
import pymysql
import os

app = Flask(__name__)

# MySQL配置（适配pymysql 1.1.0，移除无效参数）
MYSQL_CONFIG = {
    "host": os.getenv("MYSQL_HOST", "mysql-db"),
    "user": os.getenv("MYSQL_USER", "root"),
    "password": os.getenv("MYSQL_PASSWORD", "123456"),
    "database": os.getenv("MYSQL_DB", "test"),
    "port": 3306,
    "charset": "utf8mb4",
    "ssl_disabled": True  # 仅保留ssl_disabled，兼容低版本
}

@app.route('/')
def index():
    try:
        conn = pymysql.connect(**MYSQL_CONFIG)
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS t1 (id INT);")
        cursor.execute("SELECT * FROM t1;")
        data = cursor.fetchall()
        cursor.close()
        conn.close()
        
        success_msg = "连接MySQL成功（Windows WSL2环境）"
        print(success_msg)
        return jsonify({
            "code": 200,
            "msg": success_msg,
            "data": data
        })
    except Exception as e:
        error_msg = f"连接MySQL失败：{str(e)}"
        print(error_msg)
        return jsonify({
            "code": 500,
            "msg": error_msg,
            "data": []
        })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False, use_reloader=False)
