from flask import Flask, jsonify
import pymysql
import os  # 确保已导入os

app = Flask(__name__)

# 修正：对齐docker-compose.yml的环境变量
MYSQL_CONFIG = {
    "host": os.getenv("DB_HOST", "mysql-db"),  # 对应docker-compose的DB_HOST
    "user": os.getenv("DB_USER", "task7_user"),  # 对应DB_USER（原root改为task7_user）
    "password": os.getenv("DB_PWD", "123456"),  # 对应DB_PWD
    "database": os.getenv("DB_NAME", "task7_db"),  # 对应DB_NAME
    "port": int(os.getenv("DB_PORT", 3306)),  # 对应DB_PORT（转成int类型）
    "charset": "utf8mb4",
    "ssl_disabled": True
}

# 新增：添加/api开头的查询接口（匹配Nginx代理的/api路径）
@app.route('/api/query_db', methods=['GET'])
def query_db():
    try:
        conn = pymysql.connect(**MYSQL_CONFIG)
        cursor = conn.cursor()
        # 确保表存在+查询数据
        cursor.execute("CREATE TABLE IF NOT EXISTS t1 (id INT);")
        cursor.execute("SELECT * FROM t1;")
        data = cursor.fetchall()
        cursor.close()
        conn.close()
        return jsonify({
            "code": 200,
            "msg": "查询成功",
            "data": data
        })
    except Exception as e:
        return jsonify({
            "code": 500,
            "msg": f"数据库操作失败: {str(e)}",
            "data": []
        })

# 保留原根路径接口（可选）
@app.route('/')
def index():
    return jsonify({"code": 200, "msg": "后端服务正常运行"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False, use_reloader=False)
