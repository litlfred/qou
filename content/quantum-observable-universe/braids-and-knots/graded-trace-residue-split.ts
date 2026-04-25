import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:graded-trace-residue-split",
  title:
    "Graded-trace residue split on the confinement filtration",
  lean: {
    ref: "qou:QOU.BraidKnot.graded_trace_residue_split",
    validation: "not_checked",
  },
  uses: [
    "def:confinement-level",
    "def:hecke-normal-form",
    "prop:hecke-mass-trace",
    "prop:categorical-mass-markov",
    "prop:gb-residue-spectral-sum",
    "prop:schur-weyl-mass-decomposition",
    "conj:mass-endomorphism",
  ],
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
