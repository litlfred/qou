#!/usr/bin/env bash
# Generate deploy/.env and deploy/authorized-emails.txt from lean-mcp.config.json.
#
# Reads the repo-root config file and produces deployment artifacts.
# Secrets (tokens, OAuth creds) are generated or prompted — never stored in config.
#
# Usage:
#   ./deploy/generate-config.sh          # interactive, prompts for secrets
#   ./deploy/generate-config.sh --ci     # non-interactive, generates tokens only

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
CONFIG="$REPO_ROOT/lean-mcp.config.json"
DEPLOY_DIR="$REPO_ROOT/deploy"

if [ ! -f "$CONFIG" ]; then
    echo "✗ Config not found: $CONFIG"
    exit 1
fi

# ── Parse config (portable — no jq dependency) ───────────────────
parse_json() {
    python3 -c "import json,sys; d=json.load(open('$CONFIG')); print(d.get('$1','$2'))"
}
parse_json_array() {
    python3 -c "import json,sys; d=json.load(open('$CONFIG')); [print(e) for e in d.get('$1',[])]"
}

DOMAIN=$(parse_json domain "lean.example.org")
PORT=$(parse_json port "443")
IMAGE=$(parse_json image "ghcr.io/litlfred/qou/lean-mcp")
MCP_PORT=$(parse_json mcp_internal_port "8080")
WATCHTOWER_POLL=$(parse_json watchtower_poll_seconds "300")
OAUTH_PROVIDER=$(parse_json oauth_provider "google")

echo "=== Generating deploy config from lean-mcp.config.json ==="
echo "  Domain:    $DOMAIN"
echo "  Image:     $IMAGE"
echo "  OAuth:     $OAUTH_PROVIDER"
echo ""

# ── Generate .env ────────────────────────────────────────────────
LEAN_TOKEN=$(openssl rand -hex 32)
COOKIE=$(openssl rand -base64 32 | head -c 32)

if [ "${1:-}" = "--ci" ]; then
    # Non-interactive: leave OAuth creds as placeholders
    GOOGLE_CLIENT_ID="FILL_ME_IN"
    GOOGLE_CLIENT_SECRET="FILL_ME_IN"
else
    # Interactive: prompt for OAuth creds
    echo "Google OAuth credentials (create at https://console.cloud.google.com/apis/credentials):"
    echo "  Authorized redirect URI: https://$DOMAIN/oauth2/callback"
    echo ""
    read -rp "  Google Client ID: " GOOGLE_CLIENT_ID
    read -rsp "  Google Client Secret: " GOOGLE_CLIENT_SECRET
    echo ""
fi

cat > "$DEPLOY_DIR/.env" <<ENVEOF
# Auto-generated from lean-mcp.config.json — do not commit
# Regenerate with: ./deploy/generate-config.sh

# ── Domain & Image ───────────────────────────────────────────────
LEAN_MCP_DOMAIN=$DOMAIN
LEAN_MCP_IMAGE=$IMAGE
LEAN_MCP_INTERNAL_PORT=$MCP_PORT
PROXY_PORT=$PORT
WATCHTOWER_POLL_INTERVAL=$WATCHTOWER_POLL

# ── Lean MCP Server ──────────────────────────────────────────────
LEAN_LSP_MCP_TOKEN=$LEAN_TOKEN

# ── Google OAuth ─────────────────────────────────────────────────
OAUTH2_PROXY_PROVIDER=$OAUTH_PROVIDER
GOOGLE_CLIENT_ID=$GOOGLE_CLIENT_ID
GOOGLE_CLIENT_SECRET=$GOOGLE_CLIENT_SECRET
COOKIE_SECRET=$COOKIE

# ── Watchtower ───────────────────────────────────────────────────
WATCHTOWER_TOKEN=$(openssl rand -hex 16)
ENVEOF

echo "  ✓ .env generated"

# ── Generate authorized-emails.txt ───────────────────────────────
parse_json_array authorized_emails > "$DEPLOY_DIR/authorized-emails.txt"
echo "  ✓ authorized-emails.txt generated ($(wc -l < "$DEPLOY_DIR/authorized-emails.txt") emails)"

echo ""
echo "Done. Review $DEPLOY_DIR/.env, then run:"
echo "  cd $DEPLOY_DIR && docker compose up -d"
