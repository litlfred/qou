import type { SkillDefinition } from "../framework/types.js";

export const editor: SkillDefinition = {
  id: "editor",
  name: "Editor",
  description:
    "Editorial coordination: session start protocol, triage routing, " +
    "environment checks, and skill dispatch.",
  roles: ["reader", "collaborator", "owner"],
  requiredCapabilities: [
    { capabilityId: "git-read", degradation: "fail" },
  ],
  routingPatterns: [
    "session\\s+start",
    "triage",
    "what.*should.*work\\s+on",
  ],
  tags: ["coordination", "session"],
};
