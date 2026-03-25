#!/usr/bin/env bash
# Generate deploy/.env, whitelist files, and Caddyfile
# from lean-mcp.config.json.
#
# Reads the repo-root config file and produces deployment artifacts.
# Secrets (tokens, OAuth creds) are generated or prompted — never stored in config.
#
# Usage:
#   ./deploy/generate-config.sh              # interactive MCP-only deployment
#   ./deploy/generate-config.sh --ci         # non-interactive, generates tokens only
#   ./deploy/generate-config.sh --folio      # interactive folio deployment (viewer + MCP)
#   ./deploy/generate-config.sh --folio --ci # non-interactive folio deployment

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
CONFIG="$REPO_ROOT/lean-mcp.config.json"
DEPLOY_DIR="$REPO_ROOT/deploy"

if [ ! -f "$CONFIG" ]; then
    echo "✗ Config not found: $CONFIG"
    exit 1
fi

# ── Parse flags ─────────────────────────────────────────────────
MODE="mcp"
CI=false
for arg in "$@"; do
    case "$arg" in
        --folio) MODE="folio" ;;
        --ci)    CI=true ;;
    esac
done

# ── Parse config (portable — no jq dependency) ───────────────────
parse_json() {
    python3 -c "import json,sys; d=json.load(open('$CONFIG')); print(d.get('$1','$2'))"
}
parse_json_nested() {
    python3 -c "import json,sys; d=json.load(open('$CONFIG')); print(d.get('$1',{}).get('$2','$3'))"
}

IMAGE=$(parse_json image "ghcr.io/litlfred/qou/paper-assistant")
MCP_PORT=$(parse_json mcp_internal_port "8080")
OWNER_USERNAME=$(parse_json_nested auth owner "litlfred")
SESSION_MAX_AGE_HRS=$(parse_json_nested auth session_max_age_hours "24")
SESSION_MAX_AGE=$(( SESSION_MAX_AGE_HRS * 3600 ))

DOMAIN=$(parse_json_nested folio domain "folio.example.org")
if [ "$MODE" = "folio" ]; then
    VIEWER_DIR=$(parse_json_nested folio viewer_dir "viewer")
    TEMPLATE="$DEPLOY_DIR/Caddyfile.folio.template"
    COMPOSE_FILE="docker-compose.folio.yml"
else
    TEMPLATE="$DEPLOY_DIR/Caddyfile.template"
    COMPOSE_FILE="docker-compose.yml"
fi

echo "=== Generating deploy config ($MODE mode) ==="
echo "  Domain:    $DOMAIN"
echo "  Image:     $IMAGE"
echo "  Owner:     $OWNER_USERNAME"
[ "$MODE" = "folio" ] && echo "  Viewer:    $VIEWER_DIR/"
echo ""

# ── Generate .env ────────────────────────────────────────────────
LEAN_TOKEN=$(openssl rand -hex 32)
COOKIE=$(openssl rand -base64 32 | tr -d '\n')

if [ "$CI" = true ]; then
    GOOGLE_CLIENT_ID="FILL_ME_IN"
    GOOGLE_CLIENT_SECRET="FILL_ME_IN"
    GH_CLIENT_ID="FILL_ME_IN"
    GH_CLIENT_SECRET="FILL_ME_IN"
else
    echo "── Google OAuth (for viewers) ──"
    echo "  Create at: https://console.cloud.google.com/apis/credentials"
    echo "  Redirect URI: https://$DOMAIN/auth/google/callback"
    echo ""
    read -rp "  Google Client ID: " GOOGLE_CLIENT_ID
    read -rsp "  Google Client Secret: " GOOGLE_CLIENT_SECRET
    echo ""
    echo ""
    echo "── GitHub OAuth (for collaborators) ──"
    echo "  Create at: https://github.com/settings/developers"
    echo "  Callback URL: https://$DOMAIN/auth/github/callback"
    echo ""
    read -rp "  GitHub Client ID: " GH_CLIENT_ID
    read -rsp "  GitHub Client Secret: " GH_CLIENT_SECRET
    echo ""
fi

# Write .env safely using printf — no heredoc injection risk from secrets
# containing $, backticks, or backslashes.
{
  printf '# Auto-generated from lean-mcp.config.json (%s mode) — do not commit\n' "$MODE"
  printf '# Regenerate with: ./deploy/generate-config.sh%s\n' "$([ "$MODE" = "folio" ] && echo " --folio")"
  printf '\n# ── Deployment mode ──────────────────────────────────────────────\n'
  printf 'DEPLOY_MODE=%s\n' "$MODE"
  printf 'COMPOSE_FILE=%s\n' "$COMPOSE_FILE"
  printf '\n# ── Domain & Image ───────────────────────────────────────────────\n'
  printf 'FOLIO_DOMAIN=%s\n' "$DOMAIN"
  printf 'PAPER_ASSISTANT_IMAGE=%s\n' "$IMAGE"
  printf 'MCP_INTERNAL_PORT=%s\n' "$MCP_PORT"
  printf '\n# ── Lean MCP Server ──────────────────────────────────────────────\n'
  printf 'FOLIO_API_TOKEN=%s\n' "$LEAN_TOKEN"
  printf '\n# ── Auth Gateway ─────────────────────────────────────────────────\n'
  printf 'COOKIE_SECRET=%s\n' "$COOKIE"
  printf 'OWNER_USERNAME=%s\n' "$OWNER_USERNAME"
  printf 'SESSION_MAX_AGE=%s\n' "$SESSION_MAX_AGE"
  printf '\n# ── Google OAuth (viewers) ───────────────────────────────────────\n'
  printf 'GOOGLE_CLIENT_ID=%s\n' "$GOOGLE_CLIENT_ID"
  printf 'GOOGLE_CLIENT_SECRET=%s\n' "$GOOGLE_CLIENT_SECRET"
  printf '\n# ── GitHub OAuth (collaborators) ─────────────────────────────────\n'
  printf 'GH_CLIENT_ID=%s\n' "$GH_CLIENT_ID"
  printf 'GH_CLIENT_SECRET=%s\n' "$GH_CLIENT_SECRET"
} > "$DEPLOY_DIR/.env"

echo "  ✓ .env generated"

# ── Copy whitelist files ─────────────────────────────────────────
# These are the source-of-truth whitelists from the repo
for wl in google-viewers.txt github-collaborators.txt; do
    if [ -f "$DEPLOY_DIR/$wl" ]; then
        echo "  ✓ $wl present"
    else
        echo "  ⚠ $wl not found — creating empty"
        echo "# Whitelist — add one entry per line" > "$DEPLOY_DIR/$wl"
    fi
done

# ── Generate Caddyfile from template ──────────────────────────────
if [ -f "$TEMPLATE" ]; then
    FOLIO_DOMAIN="$DOMAIN" MCP_INTERNAL_PORT="$MCP_PORT" \
        envsubst '${FOLIO_DOMAIN} ${MCP_INTERNAL_PORT}' \
        < "$TEMPLATE" \
        > "$DEPLOY_DIR/Caddyfile"
    echo "  ✓ Caddyfile generated for $DOMAIN"
fi

# ── Copy viewer files for folio mode ──────────────────────────────
if [ "$MODE" = "folio" ]; then
    VIEWER_SRC="$REPO_ROOT/$VIEWER_DIR"
    VIEWER_DST="$DEPLOY_DIR/viewer"
    if [ -d "$VIEWER_SRC" ]; then
        rm -rf "$VIEWER_DST"
        cp -r "$VIEWER_SRC" "$VIEWER_DST"
        echo "  ✓ Viewer files copied to deploy/viewer/"
    else
        echo "  ⚠ Viewer dir not found: $VIEWER_SRC"
    fi

    # Copy assistant files
    ASSISTANT_SRC="$REPO_ROOT/assistant"
    ASSISTANT_DST="$DEPLOY_DIR/assistant"
    if [ -d "$ASSISTANT_SRC" ]; then
        rm -rf "$ASSISTANT_DST"
        cp -r "$ASSISTANT_SRC" "$ASSISTANT_DST"
        echo "  ✓ Assistant files copied to deploy/assistant/"
    fi
fi

echo ""
echo "Done. Review $DEPLOY_DIR/.env, then run:"
echo "  cd $DEPLOY_DIR && docker compose -f $COMPOSE_FILE up -d"
