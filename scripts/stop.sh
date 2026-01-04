#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."

if docker compose version >/dev/null 2>&1; then
  DC="docker compose"
elif command -v docker-compose >/dev/null 2>&1; then
  DC="docker-compose"
else
  echo "❌ 没找到 docker compose / docker-compose"; exit 1
fi

COMPOSE_FILE=""
for f in docker-compose.yml docker-compose.yaml compose.yml compose.yaml; do
  if [[ -f "$f" ]]; then COMPOSE_FILE="$f"; break; fi
done
[[ -n "$COMPOSE_FILE" ]] || { echo "❌ 没找到 compose 文件"; exit 1; }

echo "🛑 Stopping (keep volumes)..."
$DC -f "$COMPOSE_FILE" down
echo "✅ Stopped."
