#!/usr/bin/env bash
# Destroy a Hetzner server for QOU Folio.
#
# Required env vars:
#   SERVER_NAME, DOMAIN
#   HCLOUD_TOKEN (used by hcloud CLI)

set -euo pipefail

if ! hcloud server describe "$SERVER_NAME" &>/dev/null; then
  echo "Server '$SERVER_NAME' not found — nothing to destroy."
  exit 0
fi

IP=$(hcloud server ip "$SERVER_NAME")
echo "▸ Destroying server $SERVER_NAME ($IP)..."
hcloud server delete "$SERVER_NAME"
echo "✓ Server destroyed."
echo "Remember to remove DNS record for $DOMAIN"
