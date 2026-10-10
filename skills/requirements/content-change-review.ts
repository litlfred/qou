import type { Requirement } from "../framework/types.js";

export const contentChangeReview: Requirement = {
  id: "req-content-change-review",
  title: "Content Change Review",
  description:
    "All content-object changes must pass schema validation and AST checks " +
    "before commit.",
  actors: ["collaborator", "owner"],
  statements: [
    {
      key: "REQ-CCR-1",
      label: "Schema validation",
      conformance: "SHALL",
      requirement:
        "Modified .ts manifests must pass Zod schema validation.",
      satisfiedBy: [{ kind: "skill", ref: "content-validation" }],
    },
    {
      key: "REQ-CCR-2",
      label: "LaTeX AST validation",
      conformance: "SHALL",
      requirement:
        "Rendered LaTeX output must parse without errors via unified-latex.",
      satisfiedBy: [{ kind: "skill", ref: "latex-validation" }],
    },
    {
      key: "REQ-CCR-3",
      label: "Cross-reference integrity",
      conformance: "SHOULD",
      requirement:
        "All \\hyperref and \\ref targets must resolve to existing labels.",
      satisfiedBy: [{ kind: "skill", ref: "content-validation" }],
    },
  ],
  tags: ["content", "validation", "review"],
};
