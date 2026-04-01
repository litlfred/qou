#!/usr/bin/env bash
# Session-start hook: check local Lean, fall back to remote MCP.
#
# Priority: local lean installed locally
#
# Reads lean-mcp.config.json for the remote server domain.
# Prints JSON status for Claude Code and the editor skill to consume.

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
LEAN_DIR="$REPO_ROOT/content/quantum-observable-universe/lean"
LAKEFILE="$LEAN_DIR/lakefile.toml"
MANIFEST="$LEAN_DIR/lake-manifest.json"
CONFIG="$REPO_ROOT/lean-mcp.config.json"

export PATH="$HOME/.elan/bin:$HOME/.local/bin:$PATH"

# ── Parse remote domain from config ──────────────────────────────
REMOTE_DOMAIN=""
if [ -f "$CONFIG" ]; then
    REMOTE_DOMAIN=$(python3 -c "import json; print(json.load(open('$CONFIG')).get('domain',''))" 2>/dev/null || true)
fi
REMOTE_URL=""
if [ -n "$REMOTE_DOMAIN" ]; then
    REMOTE_URL="https://$REMOTE_DOMAIN/mcp"
fi

# ── Check uv (needed for local stdio MCP) ────────────────────────
UV_OK=false
if command -v uv &>/dev/null; then
    UV_OK=true
fi

# ── Check local lean ─────────────────────────────────────────────
LOCAL_OK=false
LOCAL_MSG=""
LEAN_VERSION=""

if command -v lean &>/dev/null; then
    LEAN_VERSION=$(lean --version 2>&1 | head -1)
    if [ $? -eq 0 ]; then
        LOCAL_OK=true
    fi
fi

# ── Check deps + cache (only if local lean exists) ────────────────
DEPS_READY=true
CACHE_OK=true

if [ "$LOCAL_OK" = true ]; then
    # Check lakefile deps
    if [ -f "$LAKEFILE" ] && [ -f "$MANIFEST" ]; then
        REQUIRED_DEPS=$(grep -A1 '^\[\[require\]\]' "$LAKEFILE" | grep 'name' | sed 's/.*= *"\(.*\)"/\1/' | tr -d '"' | tr -d ' ')
        for dep in $REQUIRED_DEPS; do
            if ! grep -q "\"name\": *\"$dep\"" "$MANIFEST" 2>/dev/null && \
               ! grep -q "\"name\":\"$dep\"" "$MANIFEST" 2>/dev/null; then
                DEPS_READY=false
            fi
        done
    elif [ ! -f "$MANIFEST" ]; then
        DEPS_READY=false
    fi

    # Check Mathlib cache
    if [ ! -d "$LEAN_DIR/.lake/packages/mathlib/.lake/build/lib" ] 2>/dev/null; then
        CACHE_OK=false
    fi

    # Auto-fetch missing deps/cache in background
    if [ "$DEPS_READY" = false ] || [ "$CACHE_OK" = false ]; then
        LOCK="$LEAN_DIR/.lake/.cache-fetch.lock"
        if ! [ -f "$LOCK" ]; then
            touch "$LOCK"
            (
                cd "$LEAN_DIR"
                if [ "$DEPS_READY" = false ]; then
                    lake update >> /tmp/lake-cache-fetch.log 2>&1 || true
                fi
                if [ "$CACHE_OK" = false ]; then
                    lake exe cache get >> /tmp/lake-cache-fetch.log 2>&1 || true
                fi
                rm -f "$LOCK"
            ) &
        fi
    fi
fi

# ── Determine local readiness ────────────────────────────────────
LOCAL_READY=false
if [ "$LOCAL_OK" = true ] && [ "$UV_OK" = true ] && [ "$DEPS_READY" = true ] && [ "$CACHE_OK" = true ]; then
    LOCAL_READY=true
fi

# ── Check remote MCP availability ────────────────────────────────
REMOTE_OK=false
if [ -n "$REMOTE_URL" ]; then
    # Quick HTTP probe — 3s timeout, just check if it responds
    if curl -sf --max-time 3 -o /dev/null "$REMOTE_URL" 2>/dev/null; then
        REMOTE_OK=true
    fi
fi

# ── Determine mode ───────────────────────────────────────────────
# Priority: local > remote
MODE="none"
if [ "$LOCAL_READY" = true ]; then
    MODE="local"
elif [ "$REMOTE_OK" = true ]; then
    MODE="remote"
elif [ "$LOCAL_OK" = true ]; then
    # Local lean exists but not fully ready — still usable with caveats
    MODE="local-degraded"
fi

# ── Build message ────────────────────────────────────────────────
MSG=""
case "$MODE" in
    local)
        MSG="Local Lean MCP ready ($LEAN_VERSION)"
        ;;
    remote)
        MSG="Local Lean not available. Using remote MCP at $REMOTE_URL"
        ;;
    local-degraded)
        if [ "$UV_OK" = false ]; then
            MSG="uv not installed. Run: curl -LsSf https://astral.sh/uv/install.sh | sh"
        elif [ "$DEPS_READY" = false ]; then
            MSG="Dependencies missing — fetching in background (log: /tmp/lake-cache-fetch.log)"
        elif [ "$CACHE_OK" = false ]; then
            MSG="Mathlib cache missing — fetching in background (log: /tmp/lake-cache-fetch.log)"
        fi
        ;;
    none)
        if [ -n "$REMOTE_URL" ]; then
            MSG="No Lean available locally or remotely ($REMOTE_URL unreachable). Run: ./scripts/setup-lean-mcp.sh"
        else
            MSG="Lean not installed. Run: ./scripts/setup-lean-mcp.sh"
        fi
        ;;
esac

# ── Ripgrep ──────────────────────────────────────────────────────
RG_OK=false
command -v rg &>/dev/null && RG_OK=true

# ── LaTeX (latexmk + pdflatex) ──────────────────────────────────
LATEXMK_OK=false
command -v latexmk &>/dev/null && LATEXMK_OK=true
PDFLATEX_OK=false
command -v pdflatex &>/dev/null && PDFLATEX_OK=true

# ── Output ───────────────────────────────────────────────────────
cat <<EOF
{"mode": "$MODE", "local_ready": $LOCAL_READY, "remote_ok": $REMOTE_OK, "remote_url": "$REMOTE_URL", "lean_available": $LOCAL_OK, "uv_available": $UV_OK, "deps_ready": $DEPS_READY, "cache_ok": $CACHE_OK, "ripgrep": $RG_OK, "latexmk": $LATEXMK_OK, "pdflatex": $PDFLATEX_OK, "version": "$LEAN_VERSION", "message": "$MSG"}
EOF
exit 0
