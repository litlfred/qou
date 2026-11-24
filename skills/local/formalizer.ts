import type { SkillDefinition } from "../framework/types.js";

export const formalizer: SkillDefinition = {
  id: "formalizer",
  name: "Formalizer",
  description:
    "Lean proof generation, library synthesis, tactic translation, " +
    "and sorry-removal workflows.",
  roles: ["collaborator", "owner"],
  requiredCapabilities: [
    { capabilityId: "lean-toolchain", degradation: "fallback", fallbackCapabilityId: "lean-mcp" },
    { capabilityId: "lean-mcp", degradation: "warn" },
  ],
  dependsOn: [
    { ref: "content-validation", kind: "skill", conformance: "SHALL" },
  ],
  mcpServices: ["lean-lsp"],
  routingPatterns: [
    "fill\\s+in.*proof",
    "prove",
    "remove\\s+sorry",
    "formalize",
  ],
  scripts: [
    { path: "scripts/lean-best-practices-lint.py", runtime: "python3", phase: "execute", args: ["--diff"] },
    { path: "scripts/lean-static-census.py", runtime: "python3", phase: "execute" },
  ],
  schemas: [
    { module: "schemas/types", types: ["Block", "LeanRef", "FormalizationStatus", "DefinitionBlock"], access: "read-write" },
    { module: "schemas/qou-types", types: ["ProofObject", "TacticMapping"], access: "read-write" },
  ],
  tags: ["lean", "formalization", "proof"],
};
