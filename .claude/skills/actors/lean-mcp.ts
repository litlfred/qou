import type { ActorDefinition } from "../framework/types.js";

export const leanMcp: ActorDefinition = {
  id: "lean-mcp",
  name: "Lean MCP Server",
  type: "system",
  description: `The lean-lsp-mcp server process. Provides diagnostics, goal states, hover docs, completions, and search tools.`,
  inherits: [],
  capabilities: ["lean-toolchain"],
  meta: {
    endpoint: "lean-lsp",
    configPath: "lean-mcp.config.json",
  },
};
