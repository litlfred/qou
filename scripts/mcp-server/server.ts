/**
 * QOU Paper Writing Assistant — MCP Server
 *
 * A unified MCP server providing:
 *   - PDF/HTML rendering (full paper, chapter, section, or single theorem)
 *   - Content-object validation and build pipeline
 *   - Formula/diagram quick preview (LaTeX → PNG)
 *   - User preference storage (render format, scope)
 *   - Lean LSP proxy (delegates to lean-lsp-mcp subprocess)
 *
 * Transports:
 *   --stdio   Stdio transport (default, for Claude Code .mcp.json)
 *   --http    Streamable HTTP transport (for remote/Docker deployment)
 *
 * @module scripts/mcp-server/server
 */

import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { registerRenderTools } from "./tools/render.js";
import { registerValidateTools } from "./tools/validate.js";
import { registerPreviewTools } from "./tools/preview.js";
import { registerPreferenceTools } from "./tools/preferences.js";
import { registerLeanTools } from "./tools/lean.js";
import { registerDepsTools } from "./tools/check-deps.js";
import { REPO_ROOT } from "./paths.js";

// ── Server setup ─────────────────────────────────────────────────

const server = new McpServer({
  name: "qou-paper-assistant",
  version: "0.1.0",
}, {
  capabilities: {
    tools: {},
  },
});

// ── Register all tool groups ─────────────────────────────────────

registerRenderTools(server);
registerValidateTools(server);
registerPreviewTools(server);
registerPreferenceTools(server);
registerLeanTools(server);
registerDepsTools(server);

// ── Transport selection ──────────────────────────────────────────

const args = process.argv.slice(2);
const mode = args.includes("--http") ? "http" : "stdio";

if (mode === "stdio") {
  const transport = new StdioServerTransport();
  await server.connect(transport);
  console.error(`[qou-mcp] Paper writing assistant started (stdio, repo: ${REPO_ROOT})`);
} else {
  // HTTP mode — for Docker/remote deployment
  // Uses Streamable HTTP transport on port from env or 8080
  const port = parseInt(process.env.MCP_PORT || "8080", 10);
  const { StreamableHTTPServerTransport } = await import(
    "@modelcontextprotocol/sdk/server/streamableHttp.js"
  );

  const httpTransport = new StreamableHTTPServerTransport({ sessionIdGenerator: undefined });
  await server.connect(httpTransport);

  Bun.serve({
    port,
    async fetch(req) {
      const url = new URL(req.url);
      if (url.pathname === "/mcp") {
        return httpTransport.handleRequest(req);
      }
      if (url.pathname === "/health") {
        return new Response(JSON.stringify({ status: "ok", version: "0.1.0" }), {
          headers: { "content-type": "application/json" },
        });
      }
      return new Response("Not Found", { status: 404 });
    },
  });

  console.error(`[qou-mcp] Paper writing assistant started (HTTP :${port}, repo: ${REPO_ROOT})`);
}
