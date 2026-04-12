#!/usr/bin/env bash
# Shared Docker-based TeX helpers for hooks and scripts.
#
# Uses the paper-assistant image (same image as the folio MCP server)
# as a fallback when pdflatex/dvisvgm aren't installed locally.
#
# Source this file to get:
#   - PAPER_IMAGE    — the Docker image name
#   - tex_available()— check if TeX is available (local or Docker)
#   - tex_exec()     — run a command with TeX available (local or Docker)
#   - docker_tex_run() — run a command inside the paper-assistant container
#
# Usage:
#   source "$(dirname "$0")/lib/docker-tex.sh"
#   if tex_available; then
#     tex_exec bun run scripts/render-tex/render-tex-blocks.ts
#   fi

# ── Image name (matches lean-mcp.config.json and build-lean-mcp.yml) ─
PAPER_IMAGE="ghcr.io/litlfred/qou/paper-assistant:latest"

# ── Repo root ──────────────────────────────────────────────────────
REPO_ROOT="${REPO_ROOT:-$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)}"

# ── Helpers ────────────────────────────────────────────────────────
_has() { command -v "$1" &>/dev/null; }

# Check if TeX tools are available locally.
tex_local() {
  _has pdflatex && _has dvisvgm
}

# Check if Docker is available and the paper-assistant image is pulled.
tex_docker_ready() {
  _has docker && docker image inspect "$PAPER_IMAGE" &>/dev/null
}

# Check if Docker is available (image may need pulling).
tex_docker_available() {
  _has docker
}

# Check if TeX is available via any method.
tex_available() {
  tex_local || tex_docker_ready
}

# Pull the paper-assistant image (if Docker is available).
# Returns 0 on success, 1 on failure.
tex_docker_pull() {
  if ! _has docker; then
    echo "[docker-tex] Docker not available" >&2
    return 1
  fi
  echo "[docker-tex] Pulling $PAPER_IMAGE ..." >&2
  docker pull "$PAPER_IMAGE" 2>&1 | tail -3 >&2
}

# Run a command inside the paper-assistant container with the repo mounted.
# The working directory inside the container matches the caller's relative
# position within the repo.
#
# Usage: docker_tex_run <command> [args...]
docker_tex_run() {
  if ! tex_docker_ready; then
    echo "[docker-tex] Image not available. Run: docker pull $PAPER_IMAGE" >&2
    return 1
  fi

  # Compute working directory relative to repo root
  local rel_cwd
  rel_cwd=$(realpath --relative-to="$REPO_ROOT" "$(pwd)" 2>/dev/null || echo ".")

  docker run --rm \
    --entrypoint "" \
    -v "$REPO_ROOT:/work" \
    -w "/work/$rel_cwd" \
    -e HOME=/root \
    "$PAPER_IMAGE" \
    "$@"
}

# Run a command with TeX available — uses local tools if present,
# falls back to Docker container.
#
# Usage: tex_exec <command> [args...]
tex_exec() {
  if tex_local; then
    "$@"
  elif tex_docker_ready; then
    docker_tex_run "$@"
  else
    echo "[docker-tex] No TeX available (local or Docker)" >&2
    return 1
  fi
}
