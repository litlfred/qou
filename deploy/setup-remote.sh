#!/usr/bin/env bash
# Setup script for the remote Lean MCP server.
#
# Reads lean-mcp.config.json from the repo root for all settings.
# Run this on your cloud VM / remote host.
#
# Prerequisites: git, curl, python3
#
# Usage:
#   git clone https://github.com/<owner>/<repo>.git
#   cd <repo>/deploy
#   ./setup-remote.sh

set -euo pipefail

DEPLOY_DIR="$(cd "$(dirname "$0")" && pwd)"
REPO_ROOT="$(cd "$DEPLOY_DIR/.." && pwd)"
CONFIG="$REPO_ROOT/lean-mcp.config.json"

if [ ! -f "$CONFIG" ]; then
    echo "✗ lean-mcp.config.json not found at repo root"
    exit 1
fi

# Parse config
DOMAIN=$(python3 -c "import json; print(json.load(open('$CONFIG')).get('domain',''))")
IMAGE=$(python3 -c "import json; print(json.load(open('$CONFIG')).get('image',''))")

echo "=== Lean MCP Remote Server Setup ==="
echo "  Domain: $DOMAIN"
echo "  Image:  $IMAGE"
echo ""

# ── 1. Docker ────────────────────────────────────────────────────
if command -v docker &>/dev/null; then
    echo "▸ Docker already installed: $(docker --version)"
else
    echo "▸ Installing Docker..."
    curl -fsSL https://get.docker.com | sh
    sudo usermod -aG docker "$USER"
    echo "  ✓ Docker installed. You may need to log out and back in."
fi

if docker compose version &>/dev/null; then
    echo "▸ Docker Compose available: $(docker compose version --short)"
else
    echo "✗ Docker Compose not available. Install docker-compose-plugin."
    exit 1
fi

# ── 2. GHCR auth ────────────────────────────────────────────────
echo ""
if [ -f "$HOME/.docker/config.json" ] && grep -q "ghcr.io" "$HOME/.docker/config.json" 2>/dev/null; then
    echo "▸ Already authenticated with GHCR"
else
    echo "▸ GHCR authentication needed."
    echo "  You need a GitHub PAT with 'read:packages' scope."
    echo "  Create at: https://github.com/settings/tokens/new"
    echo ""
    read -rp "  GitHub username: " GH_USER
    read -rsp "  GitHub PAT: " GH_TOKEN
    echo ""
    echo "$GH_TOKEN" | docker login ghcr.io -u "$GH_USER" --password-stdin
    echo "  ✓ Authenticated with GHCR"
fi

# ── 3. Generate config from lean-mcp.config.json ─────────────────
echo ""
if [ ! -f "$DEPLOY_DIR/.env" ]; then
    echo "▸ Generating deployment config..."
    "$DEPLOY_DIR/generate-config.sh"
else
    echo "▸ .env already exists (re-run generate-config.sh to regenerate)"
fi

# ── 4. Pull image ───────────────────────────────────────────────
echo ""
echo "▸ Pulling lean-mcp image..."
cd "$DEPLOY_DIR"
docker compose pull lean-mcp || echo "  ⚠ Pull failed (image may not be built yet)"

# ── 5. Start ─────────────────────────────────────────────────────
echo ""
echo "▸ Starting services..."
docker compose up -d

echo ""
echo "=== Setup complete ==="
echo ""
echo "Services:"
docker compose ps
echo ""
echo "Endpoints:"
echo "  OAuth (browser):  https://$DOMAIN/mcp"
echo "  Health check:     https://$DOMAIN/health"
echo ""
echo "To switch a Claude Code client to remote mode:"
echo "  Update .mcp.json → {\"mcpServers\":{\"lean-lsp\":{\"url\":\"https://$DOMAIN/mcp\"}}}"
echo ""
echo "Watchtower polls GHCR every $(python3 -c "import json; print(json.load(open('$CONFIG')).get('watchtower_poll_seconds',300))")s for new images."
echo "Logs: docker compose logs -f"
