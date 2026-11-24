import type { SkillDefinition } from "../framework/types.js";

export const proofStatusTracking: SkillDefinition = {
  id: "proof-status-tracking",
  name: "Proof Status Tracking",
  description: "Per-block .qa.json sidecar tracking, Lean static census, and KG/Reservoir readiness reporting.",
  roles: ["reader", "collaborator", "owner"],
  requiredCapabilities: [
    { capabilityId: "git-read", degradation: "fail" },
  ],
  routingPatterns: ["status", "tracking", "manifest", "proof.*object"],
  scripts: [
    { path: "scripts/lean-static-census.py", runtime: "python3", phase: "execute" },
    { path: "scripts/lean-kg-detangler.py", runtime: "python3", phase: "execute", args: ["--summary-only"] },
    { path: "folio/pipeline/qa-evidence-audit.ts", runtime: "bun", phase: "execute" },
  ],
  schemas: [
    { module: "schemas/qou-types", types: ["ProofObject", "ProofObjectsManifest", "ReviewRecord", "CoverageEntry"], access: "read-write" },
  ],
  tags: ["tracking", "manifest", "status"],
};
