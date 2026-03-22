#!/usr/bin/env bash
# Background lake build with exponential backoff on failure.
#
# Runs lake build in lean-archive/. On failure, retries with
# decaying intervals: 10s, 30s, 90s, 270s (max 4 retries).
# Writes status to /tmp/qou-lean-build-status.json for other
# scripts to consume.
#
# Usage: ./scripts/lean-build-bg.sh &
#   (launched by session-start hook, runs in background)

set -uo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
LEAN_DIR="$REPO_ROOT/lean-archive"
STATUS_FILE="/tmp/qou-lean-build-status.json"

export PATH="$HOME/.elan/bin:$HOME/.local/bin:$PATH"

# ── Pre-check: is lean even available? ────────────────────────────
if ! command -v lean &>/dev/null; then
    cat > "$STATUS_FILE" <<EOF
{"status": "unavailable", "message": "Lean not installed", "timestamp": "$(date -Iseconds)", "attempts": 0}
EOF
    exit 0
fi

if [ ! -d "$LEAN_DIR" ]; then
    cat > "$STATUS_FILE" <<EOF
{"status": "unavailable", "message": "lean-archive/ not found", "timestamp": "$(date -Iseconds)", "attempts": 0}
EOF
    exit 0
fi

# ── Build with retry ──────────────────────────────────────────────
MAX_RETRIES=4
DELAYS=(10 30 90 270)
ATTEMPT=0

write_status() {
    local status="$1" msg="$2" attempt="$3"
    cat > "$STATUS_FILE" <<EOF
{"status": "$status", "message": "$msg", "timestamp": "$(date -Iseconds)", "attempts": $attempt}
EOF
}

cd "$LEAN_DIR"

# First ensure deps are fetched
if [ ! -f "lake-manifest.json" ]; then
    write_status "building" "Fetching dependencies..." 0
    lake update 2>&1 > /tmp/qou-lake-update.log || true
fi

# Fetch Mathlib cache if missing
if [ ! -d ".lake/packages/mathlib/.lake/build/lib" ] 2>/dev/null; then
    write_status "building" "Fetching Mathlib cache..." 0
    lake exe cache get 2>&1 > /tmp/qou-lake-cache.log || true
fi

while [ $ATTEMPT -le $MAX_RETRIES ]; do
    ATTEMPT=$((ATTEMPT + 1))
    write_status "building" "Build attempt $ATTEMPT..." $ATTEMPT

    if lake build 2>&1 > /tmp/qou-lake-build.log; then
        write_status "ready" "Build succeeded" $ATTEMPT
        exit 0
    fi

    if [ $ATTEMPT -le $MAX_RETRIES ]; then
        DELAY=${DELAYS[$((ATTEMPT - 1))]}
        write_status "retrying" "Build failed, retrying in ${DELAY}s (attempt $ATTEMPT/$MAX_RETRIES)" $ATTEMPT
        sleep "$DELAY"
    fi
done

# All retries exhausted
write_status "failed" "Build failed after $MAX_RETRIES attempts. See /tmp/qou-lake-build.log" $ATTEMPT
exit 1
