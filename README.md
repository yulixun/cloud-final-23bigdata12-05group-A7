# cloud-final-23bigdata12-05group-A7
2025,cloud tech submit

宿主机 OS	Windows 11（WSL2 后端 Ubuntu-22.04）	宿主机为 Windows 11 操作系统，Docker 运行在 WSL2 虚拟化的 Ubuntu 22.04 发行版上
虚拟化软件（如 KVM/VirtualBox/VMware）	WSL2（Windows Subsystem for Linux 2）	未使用传统虚拟化软件，通过 WSL2 为 Docker 提供 Linux 内核环境
Docker 版本	28.5.2（Docker Desktop 桌面版）	从 docker info 输出的 Client Version 确认，为 Docker Desktop 最新稳定版
其他依赖（数据库 / 语言运行时 / 镜像仓库等）	1. Docker Compose：v2.40.3-desktop.12. 数据库：MySQL 8.0（实验选用）3. 后端运行时：Python 3.9（Flask 框架）4. 前端服务器：Nginx 1.25-alpine	1. Compose 版本从 docker compose version 确认，满足 ≥v2.20.0 要求；2. 列出实验中三层应用编排涉及的核心依赖，贴合「前端 + 后端 + 数据库」场景
Cmd确认版本号和docker compose 的version
