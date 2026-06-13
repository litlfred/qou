import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:borel-partial-resolution",
  title:
    "Borel's theorem partially discharges the keystone's sharpness target — explicit dimensions",
  lean: {
    ref: "qou:QOU.AppendixSurreals.BorelPartialResolution.borel_partial",
    validation: "not_checked",
  },
  uses: ["rem:k-theory-period-rosetta"],
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
