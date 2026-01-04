#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/.."

# 选 compose 命令：docker compose(优先) -> docker-compose
if docker compose version >/dev/null 2>&1; then
  DC="docker compose"
elif command -v docker-compose >/dev/null 2>&1; then
  DC="docker-compose"
else
  echo "❌ 没找到 docker compose / docker-compose"
  echo "   先安装 Docker + Compose 插件/或 docker-compose"
  exit 1
fi

# 自动找 compose 文件
COMPOSE_FILE=""
for f in docker-compose.yml docker-compose.yaml compose.yml compose.yaml; do
  if [[ -f "$f" ]]; then COMPOSE_FILE="$f"; break; fi
done
if [[ -z "$COMPOSE_FILE" ]]; then
  echo "❌ 没找到 compose 文件（docker-compose.yml / compose.yml 等）"
  exit 1
fi

echo "✅ Using: $DC -f $COMPOSE_FILE"
echo "🚀 Building & starting..."
# 尽量使用 --wait（新版本 compose 支持）
if $DC up --help 2>/dev/null | grep -q -- '--wait'; then
  $DC -f "$COMPOSE_FILE" up -d --build --wait --wait-timeout 120
else
  $DC -f "$COMPOSE_FILE" up -d --build
fi

echo "📌 Status:"
$DC -f "$COMPOSE_FILE" ps
echo "✅ Done. Open your app via the published port (e.g., http://localhost:xxxx)"
