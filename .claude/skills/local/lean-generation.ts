import type { SkillDefinition } from "../framework/types.js";

export const leanGeneration: SkillDefinition = {
  id: "lean-generation",
  name: "Lean Generation",
  description: "Stub extraction from LaTeX, cross-reference sync between content objects and Lean files.",
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
    { path: ".github/scripts/generate_lean_stubs.py", runtime: "python", phase: "execute" },
  ],
  schemas: [
    { module: "schemas/types", types: ["Block", "LeanRef", "DefinitionBlock"], access: "read" },
    { module: "schemas/qou-types", types: ["ProofObject"], access: "read-write" },
  ],
  tags: ["lean", "generation", "stub"],
};
