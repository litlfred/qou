import type { SkillDefinition } from "../framework/types.js";

export const criticalPathAnalysis: SkillDefinition = {
  id: "critical-path-analysis",
  name: "Critical Path Analysis",
  description:
    "Dependency DAG tracing, assumption audits, upstream/downstream impact analysis, " +
    "and categorical vs archimedean context separation.",
  roles: ["collaborator", "owner"],
  requiredCapabilities: [
    { capabilityId: "git-read", degradation: "fail" },
  ],
  routingPatterns: [
    "critical\\s+path",
    "trace.*dependenc",
    "assumption.*need",
    "archimedean.*categorical",
  ],
  schemas: [
    { module: "schemas/types", types: ["Block", "Chapter"], access: "read" },
    { module: "schemas/qou-types", types: ["DependencyEdge", "ProofObjectsManifest"], access: "read" },
  ],
  tags: ["analysis", "dependencies", "critical-path"],
};
