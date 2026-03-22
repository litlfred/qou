#!/usr/bin/env bash
# Self-updater for the Folio deployment.
#
# Polls git for new commits on main. When found:
#   1. Pulls latest code
#   2. Regenerates Caddyfile, authorized-emails.txt, viewer files
#   3. Checks for new Docker image
#   4. Clears lean-mcp cached data and bounces all services
#
# The key difference from self-update.sh: this always refreshes the viewer
# and clears the lean-mcp container's cached state on any code change.
#
# Usage:
#   ./deploy/self-update-folio.sh
#   crontab: */1 * * * * /opt/qou/deploy/self-update-folio.sh >> /var/log/folio-update.log 2>&1

set -uo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
DEPLOY_DIR="$REPO_ROOT/deploy"
LOCKFILE="/tmp/folio-update.lock"

# ── Prevent concurrent runs ──────────────────────────────────────
if [ -f "$LOCKFILE" ]; then
    LOCK_AGE=$(( $(date +%s) - $(stat -c %Y "$LOCKFILE" 2>/dev/null || echo 0) ))
    if [ "$LOCK_AGE" -lt 300 ]; then
        exit 0  # another run is active
    fi
    rm -f "$LOCKFILE"  # stale lock
fi
trap 'rm -f "$LOCKFILE"' EXIT
touch "$LOCKFILE"

CHANGED=false
COMPOSE_FILE="docker-compose.folio.yml"

# ── 1. Check git for new commits ─────────────────────────────────
cd "$REPO_ROOT"
git fetch origin main --quiet 2>/dev/null

LOCAL_SHA=$(git rev-parse HEAD 2>/dev/null)
REMOTE_SHA=$(git rev-parse origin/main 2>/dev/null)

if [ "$LOCAL_SHA" != "$REMOTE_SHA" ]; then
    echo "[$(date -Is)] Git: new commits on main ($LOCAL_SHA → $REMOTE_SHA)"

    # Clean pull: nuke everything except deploy/.env (the only secret on disk).
    git clean -xdf --exclude='deploy/.env'
    git checkout -- .
    git pull origin main --quiet

    # Regenerate non-secret files from committed config
    CONFIG="$REPO_ROOT/lean-mcp.config.json"
    if [ -f "$DEPLOY_DIR/.env" ] && [ -f "$CONFIG" ]; then
        source "$DEPLOY_DIR/.env"

        # Caddyfile from folio template
        if [ -f "$DEPLOY_DIR/Caddyfile.folio.template" ]; then
            FOLIO_DOMAIN="${FOLIO_DOMAIN:-${LEAN_MCP_DOMAIN}}" \
            LEAN_MCP_INTERNAL_PORT="${LEAN_MCP_INTERNAL_PORT}" \
                envsubst '${LEAN_MCP_DOMAIN} ${LEAN_MCP_INTERNAL_PORT} ${FOLIO_DOMAIN}' \
                < "$DEPLOY_DIR/Caddyfile.folio.template" \
                > "$DEPLOY_DIR/Caddyfile"
        fi

        # authorized-emails.txt from config
        python3 -c "
import json
[print(e) for e in json.load(open('$CONFIG')).get('authorized_emails', [])]
" > "$DEPLOY_DIR/authorized-emails.txt"

        # Refresh viewer files from repo
        VIEWER_DIR=$(python3 -c "import json; print(json.load(open('$CONFIG')).get('folio',{}).get('viewer_dir','viewer'))")
        VIEWER_SRC="$REPO_ROOT/$VIEWER_DIR"
        VIEWER_DST="$DEPLOY_DIR/viewer"
        if [ -d "$VIEWER_SRC" ]; then
            rm -rf "$VIEWER_DST"
            cp -r "$VIEWER_SRC" "$VIEWER_DST"
            echo "[$(date -Is)] Viewer files refreshed from $VIEWER_DIR/"
        fi
    fi

    CHANGED=true
fi

# ── 2. Check Docker image for new digest ─────────────────────────
cd "$DEPLOY_DIR"

RUNNING_DIGEST=$(docker inspect --format='{{index .RepoDigests 0}}' lean-mcp 2>/dev/null | cut -d@ -f2 || echo "none")

if docker compose -f "$COMPOSE_FILE" pull lean-mcp --quiet 2>/dev/null; then
    source "$DEPLOY_DIR/.env" 2>/dev/null || true
    IMAGE="${LEAN_MCP_IMAGE:-ghcr.io/litlfred/qou/lean-mcp}:latest"
    NEW_DIGEST=$(docker inspect --format='{{index .RepoDigests 0}}' "$IMAGE" 2>/dev/null | cut -d@ -f2 || echo "unknown")

    if [ "$RUNNING_DIGEST" != "$NEW_DIGEST" ] && [ "$NEW_DIGEST" != "unknown" ]; then
        echo "[$(date -Is)] Docker: new image digest ($RUNNING_DIGEST → $NEW_DIGEST)"
        CHANGED=true
    fi
fi

# ── 3. Restart if anything changed (clear cache + bounce) ────────
if [ "$CHANGED" = true ]; then
    echo "[$(date -Is)] Clearing cached data and restarting services..."

    # Stop lean-mcp to clear any in-memory/on-disk cache
    docker compose -f "$COMPOSE_FILE" stop lean-mcp 2>/dev/null || true

    # Remove the container so it starts fresh (no stale oleans/lake cache)
    docker compose -f "$COMPOSE_FILE" rm -f lean-mcp 2>/dev/null || true

    # Bring everything back up
    docker compose -f "$COMPOSE_FILE" up -d --remove-orphans
    echo "[$(date -Is)] Services restarted with fresh state."
else
    # Silent — nothing to do
    :
fi
