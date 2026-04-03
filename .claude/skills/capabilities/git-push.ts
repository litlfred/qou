import type { CapabilityDefinition } from "../framework/types.js";

export const gitPush: CapabilityDefinition = {
  id: "git-push",
  name: "Git Push Access",
  description: "Can push commits to the remote repository.",
  detection: { method: "command", command: "git push --dry-run 2>&1" },
  requires: ["git-read"],
};
