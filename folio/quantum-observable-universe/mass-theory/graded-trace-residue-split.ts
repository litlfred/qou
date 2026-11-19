import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:graded-trace-residue-split",
  title:
    "Graded-trace residue split on the confinement filtration",
  lean: {
    ref: "qou:QOU.BraidKnot.graded_trace_residue_split",
    validation: "leanok",
  },
  uses: ["prop:schur-weyl-mass-decomposition"],
  tags: [
    "filtration",
    "graded-trace",
    "residue",
    "strutinsky",
    "associated-graded",
    "mass",
    "spectral-sequence",
  ],
});
