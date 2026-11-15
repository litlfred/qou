#!/usr/bin/env bash
# Update an existing Hetzner server with new secrets/config and restart.
#
# Required env vars:
#   SERVER_NAME, DOMAIN, IMAGE, MCP_PORT, OWNER_USERNAME, SESSION_MAX_AGE,
#   GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET,
#   GH_CLIENT_ID, GH_CLIENT_SECRET,
#   HCLOUD_TOKEN (used by hcloud CLI)
#
# Optional:
#   AUTO=true — skip gracefully if server doesn't exist (for push triggers)

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

# ── Check server exists ───────────────────────────────────────────
if ! hcloud server describe "$SERVER_NAME" &>/dev/null; then
  if [ "${AUTO:-false}" = "true" ]; then
    echo "Server '$SERVER_NAME' not provisioned yet — skipping auto-update."
    exit 0
  fi
  echo "::error::Server '$SERVER_NAME' not found. Run 'provision' first."
  exit 1
fi

IP=$(hcloud server ip "$SERVER_NAME")

# ── Accept the server's SSH host key ─────────────────────────────
# On fresh CI runners ~/.ssh/known_hosts is empty, so hcloud server ssh
# would fail with "Host key verification failed".
mkdir -p ~/.ssh && chmod 700 ~/.ssh
ssh-keyscan -H "$IP" >> ~/.ssh/known_hosts

# ── Preserve existing secrets ─────────────────────────────────────
# Regenerating would invalidate all sessions and API tokens.
if ! EXISTING_ENV=$(hcloud server ssh "$SERVER_NAME" -- cat /opt/qou/deploy/.env 2>/dev/null); then
  echo "::warning::Could not read existing .env from server — generating new secrets"
  echo "::warning::This will invalidate all existing sessions and API tokens"
  EXISTING_ENV=""
fi

FOLIO_API_TOKEN=$(echo "$EXISTING_ENV" | grep '^FOLIO_API_TOKEN=' | cut -d= -f2- || true)
COOKIE_SECRET=$(echo "$EXISTING_ENV" | grep '^COOKIE_SECRET=' | cut -d= -f2- || true)
[ -z "$FOLIO_API_TOKEN" ] && FOLIO_API_TOKEN=$(openssl rand -hex 32)
[ -z "$COOKIE_SECRET" ] && COOKIE_SECRET=$(openssl rand -base64 32 | tr -d '\n')

# ── Write .env safely (no heredoc, no injection) ──────────────────
export FOLIO_DOMAIN="$DOMAIN"
export FOLIO_DOMAIN="$DOMAIN"
export PAPER_ASSISTANT_IMAGE="$IMAGE"
export MCP_INTERNAL_PORT="$MCP_PORT"
export FOLIO_API_TOKEN
export COOKIE_SECRET
export OWNER_USERNAME
export SESSION_MAX_AGE
export GOOGLE_CLIENT_ID GOOGLE_CLIENT_SECRET
export GH_CLIENT_ID GH_CLIENT_SECRET

ENV_CONTENT=$("$SCRIPT_DIR/write-env.sh" /dev/stdout)
printf '%s' "$ENV_CONTENT" | hcloud server ssh "$SERVER_NAME" -- tee /opt/qou/deploy/.env > /dev/null

# ── Pull latest code + images, regenerate config, restart ─────────
echo "▸ Pulling latest code and images, restarting..."
hcloud server ssh "$SERVER_NAME" -- bash -c '
  cd /opt/qou
  git fetch origin main --quiet
  git reset --hard origin/main

  cd deploy
  source .env
  FOLIO_DOMAIN="${FOLIO_DOMAIN}" \
  MCP_INTERNAL_PORT="${MCP_INTERNAL_PORT}" \
  FOLIO_DOMAIN="${FOLIO_DOMAIN}" \
    envsubst '"'"'${FOLIO_DOMAIN} ${MCP_INTERNAL_PORT} ${FOLIO_DOMAIN}'"'"' \
    < Caddyfile.folio.template > Caddyfile

  rm -rf viewer assistant
  cp -r ../folio-assistant/cat-harness-tools/viewer viewer 2>/dev/null || true
  cp -r ../folio-assistant/cat-harness-tools/ui assistant 2>/dev/null || true

  docker compose -f docker-compose.folio.yml pull
  docker compose -f docker-compose.folio.yml up -d --remove-orphans
'

echo "✓ Updated on $IP ($DOMAIN)"
