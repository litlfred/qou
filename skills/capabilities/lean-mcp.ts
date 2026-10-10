import type { CapabilityDefinition } from "../framework/types.js";

export const leanMcp: CapabilityDefinition = {
  id: "lean-mcp",
  name: "Lean MCP Server",
  description: "The lean-lsp-mcp server is reachable (local or remote).",
  detection: {
    method: "mcp-probe",
    endpoint: "lean-lsp",
    healthPath: "/health",
  },
  requires: [],
};
