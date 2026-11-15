import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:pn-averaging-uniqueness",
  title: "Canonical p-n interface averaging uniqueness",
  cites: ["jones1987", "wenzl1988"],
  uses: [],
  defines: [],
  tags: ["normalization", "frobenius", "no-fitting", "uniqueness"],
  lean: { ref: "qou:QOU.BraidKnot.pn_averaging_unique" },
  authorNotes: [
    {
      kind: "caveat",
      body: "An earlier version of the scope paragraph stated that both candidates satisfy bar-invariance — a conditional hypothesis reported as a settled fact. Only the uniform form does; verified exactly in computations/probes/pn_interface_bar_structure_probe.py.",
    },
    {
      kind: "note",
      date: "2026-05-30",
      body: "The closed-form-weight derivation chain was established 2026-05-30.",
    },
  ],
});
