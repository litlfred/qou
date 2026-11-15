import type { ActorDefinition } from "../framework/types.js";

export const reader: ActorDefinition = {
  id: "reader",
  name: "Reader",
  type: "person",
  description: `Default role for unauthenticated Folio Assist users. Can view content, validate LaTeX, review scientific accuracy, and track proof status.`,
  inherits: [],
  capabilities: ["git-read"],
};
