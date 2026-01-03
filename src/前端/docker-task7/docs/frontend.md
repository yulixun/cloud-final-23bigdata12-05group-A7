# 角色3：前端服务（Frontend）说明

## 1. 交付内容
- src/frontend：HTML/CSS/JS 静态页面
- src/frontend/nginx.conf：Nginx 配置，包含 /api 反向代理
- compose.frontend.yml：前端 compose 片段（供角色4合并）
- docs/frontend.md：本文档

## 2. 设计说明（可解释）
1) 为什么用 Nginx 反向代理 /api？
- 浏览器始终访问同源（localhost:80），避免 CORS 跨域配置；
- Compose 网络内可直接用服务名访问（backend:5000），不写死 IP；
- 真实数据库连接只发生在后端（安全、可控），前端只拿到 API 返回结果。

2) 路由映射规则
- 浏览器访问：http://localhost:80
- 前端请求后端：/api/*
- Nginx 转发：/api/xxx -> http://backend:5000/xxx

## 3. 数据库数据展示功能（本角色核心功能）
- 点击“查询数据库数据（表格展示）”按钮：
  - 前端调用：GET /api/db
  - 页面同时显示：
    1) 表格：把返回中的数组数据渲染成表格（更直观）
    2) 原始返回：保留 JSON/文本，便于截图与排错

说明：后端返回可以是数组，或对象中包含 rows/data/latest/items/records 等数组字段，前端会自动识别并表格化。

## 4. 与后端对接约定（供角色2/4对齐）
- 后端服务名：backend
- 后端端口：5000（容器内 5000）
- 建议后端提供接口：
  - GET /health
  - GET /db  （返回数据库查询结果，建议 JSON 数组或含 rows/data/latest 字段）

## 5. 验证步骤（可验证）
1) 启动服务（由角色4整合后执行）：
   docker compose up -d --build

2) 前端页面访问验证：
- 打开浏览器：http://localhost:80
- 能看到页面即成功

3) 前端调用后端 + 数据库验证（截图点）：
- 点击“调用后端健康检查”：页面显示后端返回
- 点击“查询数据库数据（表格展示）”：页面出现表格，并显示数据库返回的记录

4) 排错命令：
- curl -i http://localhost:80/api/health
- curl -i http://localhost:80/api/db
- docker compose logs frontend
- docker compose logs backend

## 6.角色三实验环境
- Ubuntu 24.04.2
- Docker version 29.1.2
- ocker Compose version v2.40.3