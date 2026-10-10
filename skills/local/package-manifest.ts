import type { PackageManifest } from "../framework/package-manifest.js";

/**
 * Package manifest for the qou local skills ("authoring-math").
 *
 * Declares all system dependencies needed by the formal mathematics
 * authoring assistant when running inside a Docker container on
 * Ubuntu LTS.
 */
export const authoringMathManifest: PackageManifest = {
  packageId: "local",
  name: "authoring-math",
  description: `Formal mathematics authoring assistant for the Quantum Observable Universe paper — Lean 4 formalization, LaTeX rendering, content validation, and MCP server.`,
  baseImage: "ubuntu:24.04",
  architectures: ["amd64", "arm64"],

  ociAnnotations: {
    "org.opencontainers.image.title": "QOU Paper Writing Assistant",
    "org.opencontainers.image.description":
      "Lean 4 + LaTeX + content-object authoring environment",
    "org.opencontainers.image.source": "https://github.com/litlfred/qou",
    "org.opencontainers.image.licenses": "MIT",
  },

  apt: [
    { package: "ca-certificates", reason: "TLS for downloads" },
    { package: "curl", reason: "Installer downloads" },
    { package: "git", reason: "Repository operations" },
    { package: "unzip", reason: "Archive extraction" },
    { package: "build-essential", reason: "Lean native compilation" },
    { package: "cmake", reason: "Lean native compilation" },
    { package: "libgmp-dev", reason: "Lean GMP arithmetic" },
    { package: "texlive-full", reason: "LaTeX rendering (scheme-full)" },
    { package: "latexmk", reason: "LaTeX build automation" },
    { package: "pandoc", reason: "Markdown/LaTeX/HTML conversion" },
    { package: "poppler-utils", reason: "PDF to PNG preview (pdftoppm)" },
    { package: "ripgrep", reason: "Lean MCP local project search" },
    { package: "python3", reason: "lean-lsp-mcp runtime" },
    { package: "python3-pip", reason: "Python package management fallback" },
    { package: "python3-venv", reason: "Python virtual environments" },
    { package: "graphviz", reason: "Dependency graph rendering" },
  ],

  installers: [
    {
      name: "bun",
      installCommand: "curl -fsSL https://bun.sh/install | bash",
      binary: "bun",
      reason: "MCP server runtime, content pipeline execution",
    },
    {
      name: "uv",
      installCommand: "curl -LsSf https://astral.sh/uv/install.sh | sh",
      binary: "uv",
      reason: "Python package manager for lean-lsp-mcp",
    },
    {
      name: "elan",
      installCommand:
        "curl -sSf https://raw.githubusercontent.com/leanprover/elan/master/elan-init.sh | sh -s -- -y --default-toolchain none",
      binary: "elan",
      reason: "Lean 4 toolchain manager",
    },
  ],

  python: [
    {
      package: "lean-lsp-mcp",
      reason: "Lean LSP MCP bridge (installed via uvx)",
    },
  ],

  node: [
    {
      package: "@anthropic-ai/sdk",
      version: "^0.80.0",
      reason: "Claude API for programmatic agent use",
    },
    {
      package: "@modelcontextprotocol/sdk",
      version: "^1.12.0",
      reason: "MCP protocol implementation",
    },
    {
      package: "zod",
      version: "^3.0.0",
      reason: "Schema validation for content objects",
    },
  ],

  envVars: [
    {
      name: "FOLIO_API_TOKEN",
      description: "Bearer token for programmatic MCP access",
      required: false,
    },
    {
      name: "ANTHROPIC_API_KEY",
      description: "Anthropic API key for Claude-powered skills",
      required: false,
    },
  ],

  exposedPorts: [
    { port: 8080, protocol: "tcp", service: "MCP server (HTTP mode)" },
  ],

  healthcheck: {
    test: ["CMD", "curl", "-f", "http://localhost:8080/mcp"],
    interval: "30s",
    timeout: "5s",
    retries: 3,
  },
};
