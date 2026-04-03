import type { ActorDefinition } from "../framework/types.js";

export const owner: ActorDefinition = {
  id: "owner",
  name: "Owner",
  type: "person",
  description: `Repository owner. Full access including deployment, auth whitelist management, and commits to main.`,
  inherits: ["collaborator"],
  capabilities: ["deploy-access"],
};
