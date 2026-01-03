# MySQL 服务配置说明（docker-task7）
## 1. 环境说明
- 运行环境：Windows 11 Docker Desktop + WSL2 Ubuntu
- MySQL 版本：8.0
- 核心配置：volume 持久化 + 健康检查

## 2. 目录结构
docker-task7/
├── src/db/my.cnf # MySQL 自定义配置
├── volumes/mysql/ # 数据持久化目录
├── docker-compose.yml # 编排配置
└── docs/db.md # 说明文档

## 3. 核心配置说明
### 3.1 Volume 持久化
- 挂载宿主机 `./volumes/mysql` 到容器 `/var/lib/mysql`，实现数据持久化；
- 容器重启/删除后，数据仍保存在宿主机目录中。

### 3.2 健康检查
- 检查命令：`mysqladmin ping` 验证数据库存活；
- 检查间隔：10s，超时时间：5s，重试3次，启动延迟30s；
- 优化点：调整超时时间从默认10s改为5s，提升检查效率。

## 4. 验证步骤
1. 启动容器：`docker compose up -d mysql-db`；
2. 验证健康状态：`docker compose ps` 显示 Up (healthy)；
3. 插入测试数据→重启容器→数据不丢失，验证持久化。
