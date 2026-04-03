import type { Requirement } from "../framework/types.js";

export const sessionStart: Requirement = {
  id: "req-session-start",
  title: "Session Start Protocol",
  description:
    "Every new session must detect the user's identity, assign a role, " +
    "check Lean availability, and present a triage summary.",
  actors: ["reader", "collaborator", "owner"],
  statements: [
    {
      key: "REQ-SS-1",
      label: "Identity detection",
      conformance: "SHALL",
      requirement:
        "The session hook must determine the user identity via git config, " +
        "OAuth token, environment variable, or default to reader.",
      satisfiedBy: [{ kind: "capability", ref: "git-read" }],
    },
    {
      key: "REQ-SS-2",
      label: "Role assignment",
      conformance: "SHALL",
      requirement:
        "The detected identity must be mapped to an actor via role-assignments.",
      satisfiedBy: [{ kind: "skill", ref: "editor" }],
    },
    {
      key: "REQ-SS-3",
      label: "Lean availability check",
      conformance: "SHOULD",
      requirement:
        "Check local Lean toolchain; fall back to remote MCP if unavailable.",
      satisfiedBy: [
        { kind: "capability", ref: "lean-toolchain" },
        { kind: "capability", ref: "lean-mcp" },
      ],
    },
  ],
  tags: ["session", "initialization"],
};
