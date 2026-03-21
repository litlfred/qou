# QOU Paper Writing Assistant — Docker Image
#
# Includes: Bun, TeX Live, Pandoc, Lean 4, lean-lsp-mcp, ripgrep, poppler-utils
#
# Build:
#   docker build -t qou-paper-assistant -f scripts/mcp-server/Dockerfile .
#
# Run (stdio mode — pipe MCP messages):
#   docker run -i --rm qou-paper-assistant --stdio
#
# Run (HTTP mode — expose port 8080):
#   docker run -d -p 8080:8080 qou-paper-assistant --http
#
# The image expects the repo to be mounted at /workspace or baked in at build time.

FROM ubuntu:24.04 AS base

ENV DEBIAN_FRONTEND=noninteractive
ENV HOME=/root
ENV PATH="/root/.bun/bin:/root/.elan/bin:/root/.local/bin:${PATH}"

# ── System dependencies ──────────────────────────────────────────

RUN apt-get update && apt-get install -y --no-install-recommends \
    ca-certificates \
    curl \
    git \
    unzip \
    # TeX Live (scheme-full for maximum compatibility)
    texlive-full \
    latexmk \
    # Pandoc
    pandoc \
    # PDF → PNG conversion
    poppler-utils \
    # ripgrep (for lean-lsp-mcp local search)
    ripgrep \
    # Python (for uv/lean-lsp-mcp)
    python3 \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

# ── Bun ──────────────────────────────────────────────────────────

RUN curl -fsSL https://bun.sh/install | bash

# ── uv (Python package manager, for lean-lsp-mcp) ───────────────

RUN curl -LsSf https://astral.sh/uv/install.sh | sh

# ── Lean 4 (via elan) ───────────────────────────────────────────

FROM base AS lean-setup

WORKDIR /workspace

# Copy toolchain file first to cache the Lean download
COPY lean/lean-toolchain lean/lean-toolchain

RUN curl -sSf https://raw.githubusercontent.com/leanprover/elan/master/elan-init.sh | \
    sh -s -- -y --default-toolchain none && \
    elan toolchain install $(cat lean/lean-toolchain)

# ── Project setup ────────────────────────────────────────────────

FROM lean-setup AS project

WORKDIR /workspace

# Copy dependency files first (better caching)
COPY lean/lakefile.toml lean/lake-manifest.json lean/
COPY scripts/mcp-server/package.json scripts/mcp-server/
COPY content/package.json content/

# Install Lean deps and Bun deps
RUN cd lean && lake update && lake exe cache get || true
RUN cd scripts/mcp-server && bun install
RUN cd content && bun install

# Copy full repo
COPY . .

# Build Lean (may take a while)
RUN cd lean && lake build || true

# Verify lean-lsp-mcp works
RUN uvx lean-lsp-mcp --help > /dev/null 2>&1 || echo "lean-lsp-mcp not yet cached"

# ── Runtime ──────────────────────────────────────────────────────

WORKDIR /workspace/scripts/mcp-server

EXPOSE 8080

ENTRYPOINT ["bun", "run", "server.ts"]
CMD ["--http"]
