import type { SkillDefinition } from "../framework/types.js";

export const leanGeneration: SkillDefinition = {
  id: "lean-generation",
  name: "Lean Generation",
  description: "Lean module authoring from Folio content object triples and cross-reference sync between .ts/.md/.lean siblings.",
  roles: ["collaborator", "owner"],
  requiredCapabilities: [
    { capabilityId: "lean-toolchain", degradation: "fallback", fallbackCapabilityId: "lean-mcp" },
  ],
  dependsOn: [
    { ref: "content-validation", kind: "skill", conformance: "SHALL" },
  ],
  mcpServices: ["lean-lsp"],
  routingPatterns: ["extract.*stub", "from\\s+latex", "generate.*lean"],
  scripts: [
    { path: "scripts/lean-best-practices-lint.py", runtime: "python3", phase: "execute", args: ["--diff"] },
  ],
  schemas: [
    { module: "schemas/types", types: ["Block", "LeanRef", "DefinitionBlock"], access: "read" },
    { module: "schemas/qou-types", types: ["ProofObject"], access: "read-write" },
  ],
  tags: ["lean", "generation", "stub"],
};
