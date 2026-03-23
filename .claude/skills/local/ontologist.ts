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
    { path: ".github/scripts/ontologist.py", runtime: "python", phase: "execute", args: ["scan"] },
    { path: ".github/scripts/ontologist.py", runtime: "python", phase: "execute", args: ["generate-lean"] },
    { path: ".github/scripts/ontologist.py", runtime: "python", phase: "execute", args: ["generate-mapping"] },
  ],
  schemas: [
    { module: "schemas/qou-types", types: ["GlossaryEntry", "GlossaryManifest", "NarrativeMapping", "MappingManifest"], access: "read-write" },
  ],
  tags: ["ontology", "glossary", "naming"],
};
