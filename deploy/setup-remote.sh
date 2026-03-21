#!/usr/bin/env bash
# Setup script for the remote Lean MCP server.
#
# Run this on your cloud VM / remote host to:
#   1. Install Docker + Compose (if missing)
#   2. Authenticate with GHCR
#   3. Create .env and authorized-emails.txt from examples
#   4. Pull the lean-mcp image
#   5. Start all services
#
# Prerequisites: git, curl
#
# Usage:
#   git clone https://github.com/litlfred/qou.git
#   cd qou/deploy
#   ./setup-remote.sh

set -euo pipefail

DEPLOY_DIR="$(cd "$(dirname "$0")" && pwd)"

echo "=== Lean MCP Remote Server Setup ==="
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
echo "▸ Authenticating with GHCR..."
echo "  You need a GitHub Personal Access Token with 'read:packages' scope."
echo "  Create one at: https://github.com/settings/tokens/new"
echo ""
if [ ! -f "$HOME/.docker/config.json" ] || ! grep -q "ghcr.io" "$HOME/.docker/config.json" 2>/dev/null; then
    echo "  Run: echo YOUR_TOKEN | docker login ghcr.io -u YOUR_USERNAME --password-stdin"
    echo "  Then re-run this script."
    echo ""
fi

# ── 3. Config files ──────────────────────────────────────────────
cd "$DEPLOY_DIR"

if [ ! -f .env ]; then
    echo "▸ Creating .env from example..."
    cp .env.example .env
    # Generate secrets
    LEAN_TOKEN=$(openssl rand -hex 32)
    COOKIE=$(openssl rand -base64 32 | head -c 32)
    sed -i "s/changeme-generate-with-openssl-rand-hex-32/$LEAN_TOKEN/" .env
    sed -i "s/changeme-generate-with-openssl/$COOKIE/" .env
    echo "  ✓ .env created with generated secrets"
    echo "  ⚠ You still need to fill in GOOGLE_CLIENT_ID and GOOGLE_CLIENT_SECRET"
    echo "    Create at: https://console.cloud.google.com/apis/credentials"
else
    echo "▸ .env already exists"
fi

if [ ! -f authorized-emails.txt ]; then
    echo "▸ Creating authorized-emails.txt from example..."
    cp authorized-emails.example authorized-emails.txt
    echo "  ✓ Created. Edit to add authorized email addresses."
else
    echo "▸ authorized-emails.txt already exists"
fi

# ── 4. Pull image ───────────────────────────────────────────────
echo ""
echo "▸ Pulling lean-mcp image..."
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
echo "  OAuth (browser):  http://$(hostname -I | awk '{print $1}'):${PROXY_PORT:-4180}/mcp"
echo "  Token (API/CLI):  Set LEAN_LSP_MCP_TOKEN in .env, expose port 8080"
echo ""
echo "To switch clients to remote mode, update .mcp.json:"
echo '  {"mcpServers":{"lean-lsp":{"url":"https://YOUR_HOST:4180/mcp"}}}'
echo ""
echo "Watchtower will auto-update lean-mcp when new images are pushed to GHCR."
echo "Check logs: docker compose logs -f"
