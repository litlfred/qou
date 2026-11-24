import type { SkillDefinition } from "../framework/types.js";

export const leanBuildHygiene: SkillDefinition = {
  id: "lean-build-hygiene",
  name: "Lean Build Hygiene & Community Packaging",
  description:
    "CPU-throttled Lean 4 build discipline (LEAN_NUM_THREADS=1, nice -n 15, overlay olean cache, " +
    "direct-cone compilation) plus Mathlib4 and Lean Reservoir community lean_lib hygiene gates.",
  roles: ["collaborator", "owner"],
  requiredCapabilities: [
    { capabilityId: "git-read", degradation: "fail" },
    { capabilityId: "lean-toolchain", degradation: "fallback", fallbackCapabilityId: "lean-mcp" },
  ],
  mcpServices: ["lean-lsp"],
  routingPatterns: [
    "lean.*build",
    "lean.*hygiene",
    "lean.*lint",
    "reservoir",
    "lean_lib",
    "olean.*cache",
  ],
  scripts: [
    { path: "scripts/lean-best-practices-lint.py", runtime: "python3", phase: "execute", args: ["--diff"] },
    { path: "scripts/lean-kg-detangler.py", runtime: "python3", phase: "execute", args: ["--summary-only"] },
  ],
  tags: ["lean", "build", "hygiene", "lint", "reservoir"],
};
