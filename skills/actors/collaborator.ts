import type { ActorDefinition } from "../framework/types.js";

export const collaborator: ActorDefinition = {
  id: "collaborator",
  name: "Collaborator",
  type: "person",
  description: `Authenticated via GitHub OAuth. Can edit content, formalize proofs, manage Lean files, and push to feature branches.`,
  inherits: ["reader"],
  capabilities: ["git-push", "lean-toolchain", "lean-mcp"],
};
