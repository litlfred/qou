import type { Requirement } from "../framework/types.js";

export const sorryCitation: Requirement = {
  id: "req-sorry-citation",
  title: "Sorry Citation Requirement",
  description:
    "Every `sorry` in a .lean file must have a bibliographic citation comment.",
  actors: ["collaborator", "owner"],
  statements: [
    {
      key: "REQ-SC-1",
      label: "Sorry has Ref comment",
      conformance: "SHALL",
      requirement:
        'Every `sorry` must be preceded by `-- Ref: [key] <url>` where ' +
        "the key matches an entry in references.bib.",
      satisfiedBy: [
        { kind: "skill", ref: "formalizer" },
        { kind: "skill", ref: "lean-proof-review" },
      ],
    },
  ],
  tags: ["lean", "formalization", "citation"],
};
