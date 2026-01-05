# Docker Compose 配置说明文档
## 文档概述
本文档详细描述了单机一体化项目的`docker-compose.yml`配置细节，包含网络设计、环境变量、服务启动命令等内容，适用于团队成员查阅和环境部署。

## 一、全局网络设计说明
### 1. 网络类型选择
本次配置使用**自定义bridge网络（app-network）**，而非Docker默认bridge网络，原因如下：
- 隔离性更强：自定义网络仅用于本项目的3个服务（mysql-db、backend、frontend），避免与其他Docker服务的网络冲突；
- 域名解析友好：同一自定义网络内，容器可通过`container_name`直接相互访问（如后端服务可通过`mysql-db`直接连接数据库），无需手动配置IP地址；
- 灵活性更高：可按需配置网络子网、网关等参数（本次默认配置满足单机需求，无需额外自定义）。

### 2. 网络关联方式
所有服务均通过`networks: - app-network`配置加入自定义网络，确保服务间网络互通，对外仅暴露必要端口（后端端口、前端端口），提升安全性。

## 二、环境变量配置说明
### 1. 配置文件位置
环境变量统一配置在项目根目录（`~/docker-task7`）的`.env`文件中，不直接写入`docker-compose.yml`，避免硬编码泄露敏感信息（如数据库密码）。

### 2. 核心环境变量含义
| 变量名          | 含义                  | 示例值       |
|-----------------|-----------------------|--------------|
| MYSQL_ROOT_PWD  | MySQL根用户密码       | 123456       |
| MYSQL_DB        | 项目默认数据库名称    | app_db       |
| MYSQL_USER      | 项目专用数据库用户    | app_user     |
| MYSQL_USER_PWD  | 项目数据库用户密码    | app123456    |
| BACKEND_PORT    | 后端服务端口          | 5000         |
| FRONTEND_PORT   | 前端服务端口          | 80           |

### 3. 环境变量引用方式
在`docker-compose.yml`中，通过`${变量名}`格式引用`.env`文件中的变量，示例：
```yaml
# 数据库密码引用
MYSQL_ROOT_PASSWORD=${MYSQL_ROOT_PWD}
# 后端端口引用
ports:
  - "${BACKEND_PORT}:${BACKEND_PORT}"
