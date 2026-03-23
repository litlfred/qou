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
  tags: ["ontology", "glossary", "naming"],
};
