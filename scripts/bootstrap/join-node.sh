#!/usr/bin/env bash
# Join a new inference worker node to the cluster
set -euo pipefail

MASTER_URL="${1:-}"
TOKEN="${2:-}"

if [[ -z "$MASTER_URL" || -z "$TOKEN" ]]; then
  echo "Usage: $0 --master URL --token TOKEN"
  exit 1
fi

echo "[bootstrap] Installing container runtime..."
# apt install containerd / nvidia-container-toolkit

echo "[bootstrap] Registering worker at $MASTER_URL"
# curl -X POST "$MASTER_URL/v1/nodes/join" -d "{\"token\":\"$TOKEN\"}"

echo "[bootstrap] Done. Verify in Grafana dashboard."
