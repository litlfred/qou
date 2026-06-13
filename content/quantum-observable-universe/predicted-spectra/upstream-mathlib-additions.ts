import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:upstream-mathlib-additions",
  title:
    "Upstream Mathlib additions: complex dilogarithm via tsum + BW formula + Cl_2 oddness",
  uses: ["rem:three-substantive-mathlib-fillers"],
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
    {
      kind: "status",
      body: "See [Table 2](#tbl:upstream-mathlib-additions-table2-data).\n\nThe first three are tractable Mathlib PRs; the fourth requires\nsubstantial Tauberian-theorem infrastructure.",
    },
  ],
});
