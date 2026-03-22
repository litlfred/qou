#!/usr/bin/env bash
# Generate deploy/.env, authorized-emails.txt, and Caddyfile
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
parse_json_array() {
    python3 -c "import json,sys; d=json.load(open('$CONFIG')); [print(e) for e in d.get('$1',[])]"
}

IMAGE=$(parse_json image "ghcr.io/litlfred/qou/lean-mcp")
MCP_PORT=$(parse_json mcp_internal_port "8080")
OAUTH_PROVIDER=$(parse_json oauth_provider "google")

if [ "$MODE" = "folio" ]; then
    DOMAIN=$(parse_json_nested folio domain "folio.example.org")
    VIEWER_DIR=$(parse_json_nested folio viewer_dir "viewer")
    TEMPLATE="$DEPLOY_DIR/Caddyfile.folio.template"
    COMPOSE_FILE="docker-compose.folio.yml"
else
    DOMAIN=$(parse_json domain "lean.example.org")
    TEMPLATE="$DEPLOY_DIR/Caddyfile.template"
    COMPOSE_FILE="docker-compose.yml"
fi

echo "=== Generating deploy config ($MODE mode) ==="
echo "  Domain:    $DOMAIN"
echo "  Image:     $IMAGE"
echo "  OAuth:     $OAUTH_PROVIDER"
[ "$MODE" = "folio" ] && echo "  Viewer:    $VIEWER_DIR/"
echo ""

# ── Generate .env ────────────────────────────────────────────────
LEAN_TOKEN=$(openssl rand -hex 32)
COOKIE=$(openssl rand -base64 32 | head -c 32)

if [ "$CI" = true ]; then
    GOOGLE_CLIENT_ID="FILL_ME_IN"
    GOOGLE_CLIENT_SECRET="FILL_ME_IN"
else
    echo "Google OAuth credentials (create at https://console.cloud.google.com/apis/credentials):"
    echo "  Authorized redirect URI: https://$DOMAIN/oauth2/callback"
    echo ""
    read -rp "  Google Client ID: " GOOGLE_CLIENT_ID
    read -rsp "  Google Client Secret: " GOOGLE_CLIENT_SECRET
    echo ""
fi

cat > "$DEPLOY_DIR/.env" <<ENVEOF
# Auto-generated from lean-mcp.config.json ($MODE mode) — do not commit
# Regenerate with: ./deploy/generate-config.sh $([ "$MODE" = "folio" ] && echo "--folio")

# ── Deployment mode ──────────────────────────────────────────────
DEPLOY_MODE=$MODE
COMPOSE_FILE=$COMPOSE_FILE

# ── Domain & Image ───────────────────────────────────────────────
LEAN_MCP_DOMAIN=$DOMAIN
FOLIO_DOMAIN=$DOMAIN
LEAN_MCP_IMAGE=$IMAGE
LEAN_MCP_INTERNAL_PORT=$MCP_PORT

# ── Lean MCP Server ──────────────────────────────────────────────
LEAN_LSP_MCP_TOKEN=$LEAN_TOKEN

# ── Google OAuth ─────────────────────────────────────────────────
OAUTH2_PROXY_PROVIDER=$OAUTH_PROVIDER
GOOGLE_CLIENT_ID=$GOOGLE_CLIENT_ID
GOOGLE_CLIENT_SECRET=$GOOGLE_CLIENT_SECRET
COOKIE_SECRET=$COOKIE
ENVEOF

echo "  ✓ .env generated"

# ── Generate authorized-emails.txt ───────────────────────────────
parse_json_array authorized_emails > "$DEPLOY_DIR/authorized-emails.txt"
echo "  ✓ authorized-emails.txt generated ($(wc -l < "$DEPLOY_DIR/authorized-emails.txt") emails)"

# ── Generate Caddyfile from template ──────────────────────────────
if [ -f "$TEMPLATE" ]; then
    LEAN_MCP_DOMAIN="$DOMAIN" LEAN_MCP_INTERNAL_PORT="$MCP_PORT" \
    FOLIO_DOMAIN="$DOMAIN" \
        envsubst '${LEAN_MCP_DOMAIN} ${LEAN_MCP_INTERNAL_PORT} ${FOLIO_DOMAIN}' \
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
fi

echo ""
echo "Done. Review $DEPLOY_DIR/.env, then run:"
echo "  cd $DEPLOY_DIR && docker compose -f $COMPOSE_FILE up -d"
