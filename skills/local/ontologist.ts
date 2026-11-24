import type { SkillDefinition } from "../framework/types.js";

export const ontologist: SkillDefinition = {
  id: "ontologist",
  name: "Ontologist",
  description: "Term disambiguation, glossary generation, and Mathlib naming alignment.",
  roles: ["collaborator", "owner"],
  requiredCapabilities: [
    { capabilityId: "git-read", degradation: "fail" },
  ],
  dependsOn: [
    { ref: "content-validation", kind: "skill", conformance: "SHOULD" },
  ],
  routingPatterns: ["glossary", "terminology", "naming", "disambiguat"],
  scripts: [
    { path: "scripts/lean-best-practices-lint.py", runtime: "python3", phase: "execute", args: ["--diff"] },
    { path: "folio/pipeline/block-manifest-audit.ts", runtime: "bun", phase: "execute" },
  ],
  schemas: [
    { module: "schemas/qou-types", types: ["GlossaryEntry", "GlossaryManifest", "NarrativeMapping", "MappingManifest"], access: "read-write" },
  ],
  tags: ["ontology", "glossary", "naming"],
};
