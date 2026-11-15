#!/usr/bin/env bash
# Provision a new Hetzner server for QOU Folio.
#
# Required env vars:
#   SERVER_NAME, REPO_URL, DOMAIN, IMAGE, MCP_PORT, OWNER_USERNAME,
#   SESSION_MAX_AGE, SERVER_TYPE, SERVER_LOC, SERVER_IMG,
#   GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET,
#   GH_CLIENT_ID, GH_CLIENT_SECRET,
#   HCLOUD_TOKEN (used by hcloud CLI)
#
# Generates: FOLIO_API_TOKEN, COOKIE_SECRET (random)

set -euo pipefail

# ── Validate required env vars ────────────────────────────────────
for var in SERVER_NAME REPO_URL DOMAIN IMAGE MCP_PORT OWNER_USERNAME \
           SESSION_MAX_AGE SERVER_TYPE SERVER_LOC SERVER_IMG \
           GOOGLE_CLIENT_ID GOOGLE_CLIENT_SECRET \
           GH_CLIENT_ID GH_CLIENT_SECRET; do
  if [ -z "${!var:-}" ]; then
    echo "::error::Missing required env var: $var"
    exit 1
  fi
done

# ── Check server doesn't already exist ────────────────────────────
if hcloud server describe "$SERVER_NAME" &>/dev/null; then
  echo "::error::Server '$SERVER_NAME' already exists. Use 'update' or 'destroy' first."
  hcloud server ip "$SERVER_NAME"
  exit 1
fi

# ── Generate one-time secrets ─────────────────────────────────────
FOLIO_API_TOKEN=$(openssl rand -hex 32)
COOKIE_SECRET=$(openssl rand -base64 32 | tr -d '\n')

# ── Build cloud-init script ──────────────────────────────────────
# Uses a quoted heredoc ('CLOUD_INIT_EOF') so no shell expansion occurs.
# Variables are injected via sed replacements on safe, non-secret values.
# Secrets are written to .env via printf (no heredoc injection risk).

cat > /tmp/cloud-init.sh <<'CLOUD_INIT_EOF'
#!/bin/bash
set -euxo pipefail

curl -fsSL https://get.docker.com | sh
apt-get install -y gettext-base python3

git clone __REPO_URL__ /opt/qou
cd /opt/qou

# .env is written by the base64-encoded script below
base64 -d <<< "__ENV_B64__" > deploy/.env

export FOLIO_DOMAIN="__DOMAIN__"
export MCP_INTERNAL_PORT="__MCP_PORT__"
envsubst '${FOLIO_DOMAIN} ${MCP_INTERNAL_PORT}' \
  < deploy/Caddyfile.folio.template \
  > deploy/Caddyfile

cp -r folio-assistant/cat-harness-tools/viewer deploy/viewer 2>/dev/null || true
cp -r folio-assistant/cat-harness-tools/ui deploy/assistant 2>/dev/null || true

cd deploy
docker compose -f docker-compose.folio.yml pull
docker compose -f docker-compose.folio.yml up -d

# ── Set up self-update cron (every minute) ────────────────────────
CRON_LINE="* * * * * /opt/qou/deploy/self-update-folio.sh >> /var/log/folio-update.log 2>&1"
(crontab -l 2>/dev/null || true; echo "$CRON_LINE") | crontab -

# ── Log rotation for update log ──────────────────────────────────
cat > /etc/logrotate.d/folio-update <<'LOGROTATE'
/var/log/folio-update.log {
    daily
    rotate 7
    compress
    missingok
    notifempty
}
LOGROTATE

echo "=== Folio provisioning complete ==="
CLOUD_INIT_EOF

# ── Generate .env content safely and base64-encode ────────────────
export FOLIO_DOMAIN="$DOMAIN"
export PAPER_ASSISTANT_IMAGE="$IMAGE"
export MCP_INTERNAL_PORT="$MCP_PORT"
export FOLIO_API_TOKEN
export COOKIE_SECRET
export OWNER_USERNAME
export SESSION_MAX_AGE
export GOOGLE_CLIENT_ID GOOGLE_CLIENT_SECRET
export GH_CLIENT_ID GH_CLIENT_SECRET

ENV_CONTENT=$(bash "$(dirname "$0")/write-env.sh" /dev/stdout)
ENV_B64=$(printf '%s' "$ENV_CONTENT" | base64 -w0)

# ── Substitute safe placeholders in cloud-init ────────────────────
sed -i "s|__REPO_URL__|${REPO_URL}|g" /tmp/cloud-init.sh
sed -i "s|__DOMAIN__|${DOMAIN}|g" /tmp/cloud-init.sh
sed -i "s|__MCP_PORT__|${MCP_PORT}|g" /tmp/cloud-init.sh
sed -i "s|__ENV_B64__|${ENV_B64}|g" /tmp/cloud-init.sh

# ── Create server ─────────────────────────────────────────────────
echo "▸ Creating server..."
# Redirect stdout to /dev/null — hcloud prints root password there.
# Errors still go to stderr. We don't need the password (cloud-init
# handles setup, hcloud ssh uses the API for access).
hcloud server create \
  --name "$SERVER_NAME" \
  --type "$SERVER_TYPE" \
  --image "$SERVER_IMG" \
  --location "$SERVER_LOC" \
  --user-data-from-file /tmp/cloud-init.sh \
  > /dev/null

rm -f /tmp/cloud-init.sh

IP=$(hcloud server ip "$SERVER_NAME")
echo ""
echo "============================================"
echo "  Server created!"
echo "  IP: $IP"
echo "  Domain: $DOMAIN"
echo "============================================"
echo ""
echo "Next: Point DNS  $DOMAIN → A → $IP"
echo "Caddy auto-provisions TLS once DNS propagates."
