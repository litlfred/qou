#!/usr/bin/env bash
# Write deploy/.env safely using printf (no heredoc injection risk).
#
# Usage: deploy/write-env.sh /path/to/.env
#
# All values come from environment variables. Uses printf '%s' to
# prevent shell metacharacters in secrets from being interpreted.

set -euo pipefail

OUTPUT="${1:?Usage: write-env.sh /path/to/.env}"

{
  printf 'DEPLOY_MODE=folio\n'
  printf 'COMPOSE_FILE=docker-compose.folio.yml\n'
  printf 'FOLIO_DOMAIN=%s\n' "$FOLIO_DOMAIN"
  printf 'PAPER_ASSISTANT_IMAGE=%s\n' "$PAPER_ASSISTANT_IMAGE"
  printf 'MCP_INTERNAL_PORT=%s\n' "$MCP_INTERNAL_PORT"
  printf 'FOLIO_API_TOKEN=%s\n' "$FOLIO_API_TOKEN"
  printf 'COOKIE_SECRET=%s\n' "$COOKIE_SECRET"
  printf 'OWNER_USERNAME=%s\n' "$OWNER_USERNAME"
  printf 'SESSION_MAX_AGE=%s\n' "$SESSION_MAX_AGE"
  printf 'GOOGLE_CLIENT_ID=%s\n' "$GOOGLE_CLIENT_ID"
  printf 'GOOGLE_CLIENT_SECRET=%s\n' "$GOOGLE_CLIENT_SECRET"
  printf 'GH_CLIENT_ID=%s\n' "$GH_CLIENT_ID"
  printf 'GH_CLIENT_SECRET=%s\n' "$GH_CLIENT_SECRET"
} > "$OUTPUT"
