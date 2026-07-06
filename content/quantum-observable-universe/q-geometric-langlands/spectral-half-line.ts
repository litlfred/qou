import { corollary } from "../../schema/builders";

export default corollary({
  authorNotes: [
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data." },
  ],
  label: "cor:spectral-half-line",
  title: "All fundamental Reeb modes lie on the critical line",
  lean: { ref: "qou:QOU.AlgebraicSubstrate.spectral_half_line",
    validation: "not_checked",
  },
  uses: ["thm:hasse-weil-bound", "def:categorical-reeb-derivation"],
  tags: ["critical-line", "spectral", "half-line", "reeb-spectrum"],
});
