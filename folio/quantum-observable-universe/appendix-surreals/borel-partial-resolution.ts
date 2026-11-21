import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:borel-partial-resolution",
  title:
    "Borel's theorem partially discharges the depth correspondence's sharpness target — explicit dimensions",
  lean: {
    ref: "qou:QOU.AppendixSurreals.BorelPartialResolution.borel_partial",
    validation: "not_checked",
  },
  // rem:k-theory-period-rosetta dropped from uses[] 2026-11-20 (owner choice, bean qou-tm3c):
  // linked in the .md only as background for why Borel's theorem matters; the proposition records Borel ranks, which do not depend on it. A remark carries no premise; the edge only put this block
  // downstream of a conjecture.
  uses: [],
  cites: ["bloch2000", "suslin1991"],
  tags: [
    "borel-theorem",
    "k-theory",
    "keystone-discharge",
    "bring-natural-fields",
    "beilinson-conjecture",
    "graded-mikusinski",
    "explicit-dimensions",
  ],
  authorNotes: [
    {
      kind: "status",
      body: "See [Table 2](#tbl:borel-partial-resolution-table2-data).",
    },
  ],
});
