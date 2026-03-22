#!/usr/bin/env bash
# Background Lean service: update deps, fetch cache, build.
#
# Full lifecycle for getting Lean MCP operational:
#   1. Check lean/lake availability
#   2. lake update (fetch/update all deps from lakefile.toml)
#   3. lake exe cache get (fetch Mathlib oleans)
#   4. lake build (compile QOU project)
#   5. On failure: retry with exponential backoff (10s, 30s, 90s, 270s)
#
# Writes status to /tmp/qou-lean-build-status.json for session-status.sh
# and the editor skill to consume. Status values:
#   unavailable  — lean not installed or lean-archive/ missing
#   updating     — running lake update
#   caching      — running lake exe cache get
#   building     — running lake build
#   retrying     — build failed, waiting to retry
#   ready        — build succeeded, MCP fully operational
#   failed       — all retries exhausted
#
# Usage: ./scripts/lean-build-bg.sh &
#   (launched by SessionStart hook, runs in background)

set -uo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
LEAN_DIR="$REPO_ROOT/lean-archive"
STATUS_FILE="/tmp/qou-lean-build-status.json"
LOG_DIR="/tmp"

export PATH="$HOME/.elan/bin:$HOME/.local/bin:$PATH"

write_status() {
    local status="$1" msg="$2" step="$3" attempt="${4:-0}"
    cat > "$STATUS_FILE" <<EOF
{"status": "$status", "message": "$msg", "step": "$step", "timestamp": "$(date -Iseconds)", "attempts": $attempt}
EOF
}

# ── Pre-check: is lean even available? ────────────────────────────
if ! command -v lean &>/dev/null; then
    write_status "unavailable" "Lean not installed. Run: ./scripts/setup-lean-mcp.sh" "check" 0
    exit 0
fi

if ! command -v lake &>/dev/null; then
    write_status "unavailable" "Lake not installed. Run: ./scripts/setup-lean-mcp.sh" "check" 0
    exit 0
fi

if [ ! -d "$LEAN_DIR" ]; then
    write_status "unavailable" "lean-archive/ not found" "check" 0
    exit 0
fi

cd "$LEAN_DIR"

# ── Step 1: lake update (always run to ensure deps match lakefile) ─
write_status "updating" "Running lake update..." "update" 0
if lake update > "$LOG_DIR/qou-lake-update.log" 2>&1; then
    write_status "updating" "Dependencies updated" "update" 0
else
    # lake update can fail on optional deps (doc-gen4, etc.) — continue
    write_status "updating" "lake update had warnings (continuing)" "update" 0
fi

# ── Step 2: lake exe cache get (fetch Mathlib oleans) ──────────────
write_status "caching" "Fetching Mathlib cache..." "cache" 0
if lake exe cache get > "$LOG_DIR/qou-lake-cache.log" 2>&1; then
    write_status "caching" "Cache fetched" "cache" 0
else
    write_status "caching" "Cache fetch had issues (continuing)" "cache" 0
fi

# ── Step 3: lake build with retry ──────────────────────────────────
MAX_RETRIES=4
DELAYS=(10 30 90 270)
ATTEMPT=0

while [ $ATTEMPT -le $MAX_RETRIES ]; do
    ATTEMPT=$((ATTEMPT + 1))
    write_status "building" "Build attempt $ATTEMPT..." "build" $ATTEMPT

    if lake build > "$LOG_DIR/qou-lake-build.log" 2>&1; then
        write_status "ready" "Lean MCP ready (build succeeded)" "done" $ATTEMPT
        exit 0
    fi

    if [ $ATTEMPT -le $MAX_RETRIES ]; then
        DELAY=${DELAYS[$((ATTEMPT - 1))]}
        LAST_ERR=$(tail -1 "$LOG_DIR/qou-lake-build.log" 2>/dev/null | head -c 200)
        write_status "retrying" "Build failed: ${LAST_ERR}. Retrying in ${DELAY}s ($ATTEMPT/$MAX_RETRIES)" "build" $ATTEMPT
        sleep "$DELAY"
    fi
done

# All retries exhausted — report last error
LAST_ERR=$(grep "^error:" "$LOG_DIR/qou-lake-build.log" 2>/dev/null | tail -1 | head -c 200)
write_status "failed" "Build failed: ${LAST_ERR:-see /tmp/qou-lake-build.log}" "build" $ATTEMPT
exit 1
