import { proposition } from "../../schema/builders";

export default proposition({
  authorNotes: [
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data." },
  ],
  label: "prop:lagrange-resolvent-transform",
  title:
    "Discrete Fourier transform diagonalises $C_5$ on the Bring's surface",
  tags: ["lagrange", "resolvent", "fourier", "c5", "brings-surface"],
  lean: { ref: "qou:QOU.BringsSurface.lagrange_resolvent_transform",
    validation: "not_checked",
  },
  uses: [
    "def:brings-surface",
  ],
  examples: ["rem:lagrange-resolvents"],
});
