FROM nginx:alpine

# Nginx 站点配置（含反向代理）
COPY nginx.conf /etc/nginx/conf.d/default.conf

# 静态页面
COPY html/ /usr/share/nginx/html/
