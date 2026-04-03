import type { CapabilityDefinition } from "../framework/types.js";

export const gitPush: CapabilityDefinition = {
  id: "git-push",
  name: "Git Push Access",
  description: "Can push commits to the remote repository.",
  detection: { method: "command", command: "git remote get-url origin >/dev/null 2>&1 && GIT_TERMINAL_PROMPT=0 git ls-remote --exit-code origin >/dev/null 2>&1" },
  requires: ["git-read"],
};
