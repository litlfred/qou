import type { Requirement } from "../framework/types.js";

export const commitHygiene: Requirement = {
  id: "req-commit-hygiene",
  title: "Commit Hygiene",
  description: "Commits must not include build artifacts or Lean cache files.",
  actors: ["collaborator", "owner"],
  statements: [
    {
      key: "REQ-CH-1",
      label: "No Lean artifacts",
      conformance: "SHALL",
      requirement:
        "Commits must not contain .lake/, lake-packages/, or build/ paths.",
      satisfiedBy: [{ kind: "skill", ref: "content-validation" }],
    },
    {
      key: "REQ-CH-2",
      label: "Status field accuracy",
      conformance: "SHALL",
      requirement:
        "When a .lean file changes, the sibling .ts manifest status field " +
        "must be updated to reflect the new proof state.",
      satisfiedBy: [{ kind: "skill", ref: "formalizer" }],
    },
  ],
  tags: ["git", "hygiene"],
};
