import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:upstream-mathlib-additions",
  title:
    "Upstream Mathlib additions: complex dilogarithm via tsum + BW formula + Cl_2 oddness",
  // rem:three-substantive-mathlib-fillers dropped from uses[] 2026-11-20 (owner choice, bean qou-tm3c):
  // not cited in the statement or proof. A remark carries no premise; the edge only put this block
  // downstream of a conjecture.
  uses: [],
  cites: ["zagier1986", "bloch2000"],
  tags: [
    "mathlib-filler",
    "complex-dilogarithm",
    "bloch-wigner-dilogarithm",
    "clausen-oddness",
    "lean-construction",
    "upstream-contribution",
  ],
  lean: {
    ref: "qou:QOU.Archimedean.UpstreamAdditions.complexLiTwo",
    validation: "not_checked",
  },
  authorNotes: [
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data." },
    {
      kind: "status",
      body: "See [Table 2](#tbl:upstream-mathlib-additions-table2-data).\n\nThe first three are tractable Mathlib PRs; the fourth requires\nsubstantial Tauberian-theorem infrastructure.",
    },
  ],
});
