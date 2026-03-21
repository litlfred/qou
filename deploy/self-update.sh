#!/usr/bin/env bash
# Self-updater: polls the git repo and GHCR for changes, bounces services.
#
# Runs as a cron job or systemd timer on the remote host.
# No SSH keys needed in CI — the host pulls, not pushed to.
#
# What it checks (every run):
#   1. Git repo: new commits on main? → git pull, regenerate Caddyfile
#   2. Docker image: new digest on GHCR? → docker compose pull + restart
#
# Usage:
#   ./deploy/self-update.sh              # run once
#   crontab: */1 * * * * /opt/qou/deploy/self-update.sh >> /var/log/lean-mcp-update.log 2>&1

set -uo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
DEPLOY_DIR="$REPO_ROOT/deploy"
LOCKFILE="/tmp/lean-mcp-update.lock"

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

# ── 1. Check git for new commits ─────────────────────────────────
cd "$REPO_ROOT"
git fetch origin main --quiet 2>/dev/null

LOCAL_SHA=$(git rev-parse HEAD 2>/dev/null)
REMOTE_SHA=$(git rev-parse origin/main 2>/dev/null)

if [ "$LOCAL_SHA" != "$REMOTE_SHA" ]; then
    echo "[$(date -Is)] Git: new commits on main ($LOCAL_SHA → $REMOTE_SHA)"

    # Clean pull: remove everything not in the repo, but preserve secrets.
    # -x: remove untracked files including ignored ones
    # -d: remove untracked directories
    # -f: force
    # --exclude: keep deploy secrets that aren't in the repo
    git clean -xdf \
        --exclude='deploy/.env' \
        --exclude='deploy/authorized-emails.txt' \
        --exclude='deploy/Caddyfile'
    git checkout -- .
    git pull origin main --quiet

    # Regenerate Caddyfile if config changed (no secrets involved)
    if [ -f "$DEPLOY_DIR/.env" ] && [ -f "$DEPLOY_DIR/Caddyfile.template" ]; then
        source "$DEPLOY_DIR/.env"
        LEAN_MCP_DOMAIN="${LEAN_MCP_DOMAIN}" \
        LEAN_MCP_INTERNAL_PORT="${LEAN_MCP_INTERNAL_PORT}" \
            envsubst '${LEAN_MCP_DOMAIN} ${LEAN_MCP_INTERNAL_PORT}' \
            < "$DEPLOY_DIR/Caddyfile.template" \
            > "$DEPLOY_DIR/Caddyfile"
    fi

    # Regenerate authorized-emails.txt from config
    CONFIG="$REPO_ROOT/lean-mcp.config.json"
    if [ -f "$CONFIG" ]; then
        python3 -c "
import json
d = json.load(open('$CONFIG'))
for e in d.get('authorized_emails', []):
    print(e)
" > "$DEPLOY_DIR/authorized-emails.txt"
    fi

    CHANGED=true
fi

# ── 2. Check Docker image for new digest ─────────────────────────
cd "$DEPLOY_DIR"

# Get the currently running image digest
RUNNING_DIGEST=$(docker inspect --format='{{index .RepoDigests 0}}' lean-mcp 2>/dev/null | cut -d@ -f2 || echo "none")

# Pull latest and check if digest changed
if docker compose pull lean-mcp --quiet 2>/dev/null; then
    # Get the newly pulled digest
    source "$DEPLOY_DIR/.env" 2>/dev/null || true
    IMAGE="${LEAN_MCP_IMAGE:-ghcr.io/litlfred/qou/lean-mcp}:latest"
    NEW_DIGEST=$(docker inspect --format='{{index .RepoDigests 0}}' "$IMAGE" 2>/dev/null | cut -d@ -f2 || echo "unknown")

    if [ "$RUNNING_DIGEST" != "$NEW_DIGEST" ] && [ "$NEW_DIGEST" != "unknown" ]; then
        echo "[$(date -Is)] Docker: new image digest ($RUNNING_DIGEST → $NEW_DIGEST)"
        CHANGED=true
    fi
fi

# ── 3. Restart if anything changed ───────────────────────────────
if [ "$CHANGED" = true ]; then
    echo "[$(date -Is)] Restarting services..."
    docker compose up -d --remove-orphans
    echo "[$(date -Is)] Services restarted."
else
    # Silent — nothing to do
    :
fi
