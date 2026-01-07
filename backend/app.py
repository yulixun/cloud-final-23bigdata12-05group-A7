from flask import Flask, jsonify
import pymysql
import os

app = Flask(__name__)

# 从环境变量读取配置（适配Docker）
DB_CONFIG = {
    "host": os.getenv("DB_HOST", "mysql-db"),
    "user": os.getenv("DB_USER", "task7_user"),
    "password": os.getenv("DB_PWD", "123456"),
    "database": os.getenv("DB_NAME", "task7_db"),
    "port": int(os.getenv("DB_PORT", 3306)),
    "charset": "utf8mb4"
}

# 封装数据库操作函数
def query_db(sql, params=None):
    conn = None
    cursor = None
    try:
        conn = pymysql.connect(**DB_CONFIG)
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor = conn.cursor()
        cursor.execute(sql, params or ())

        if sql.strip().upper().startswith("SELECT"):
            return cursor.fetchall()
        else:
            conn.commit()
            return cursor.rowcount
    except Exception as e:
        if conn:
            conn.rollback()
        print(f"数据库错误：{e}")
        return None
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

# 核心修改1：去掉/api前缀，改成/db
@app.route('/api/db', methods=['GET'])
def get_db_data():
    # 确保表存在
    # query_db("CREATE TABLE IF NOT EXISTS t1 (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(50), value INT)")
    # 插入测试数据（避免空表）
    # query_db("INSERT IGNORE INTO t1 (name, value) VALUES (%s, %s), (%s, %s)", ("测试1", 100, "测试2", 200))
    # 查询所有数据
    data = query_db("SELECT * FROM demo_enrollments")

    if data is not None:
        return jsonify({"data": data})  # 前端extractRows能识别data字段
    else:
        return jsonify({"code": 500, "msg": "查询失败", "data": []}), 500

# 核心修改2：去掉/api前缀，改成/health
@app.route('/api/health', methods=['GET'])
def health():
    if query_db("SELECT 1") is not None:
        return jsonify({"status": "ok", "msg": "数据库连接正常"})
    else:
        return jsonify({"status": "error", "msg": "数据库连接失败"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
