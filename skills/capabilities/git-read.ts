import type { CapabilityDefinition } from "../framework/types.js";

export const gitRead: CapabilityDefinition = {
  id: "git-read",
  name: "Git Read Access",
  description: "Can read from the local git repository.",
  detection: { method: "command", command: "git rev-parse --is-inside-work-tree" },
};
