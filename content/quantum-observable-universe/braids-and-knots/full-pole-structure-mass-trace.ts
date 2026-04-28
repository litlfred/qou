import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:full-pole-structure-mass-trace",
  title:
    "Habiro completion of the mass trace",
  lean: {
    ref: "qou:QOU.BraidKnot.HabiroCompletion",
    validation: "not_checked",
  },
  uses: [
    "def:habiro-ring",
    "prop:gb-residue-spectral-sum",
    "prop:schur-weyl-mass-decomposition",
  ],
  cites: ["habiro2004", "jones1987"],
  tags: [
    "habiro-ring",
    "cyclotomic-completion",
    "markov-trace",
    "root-of-unity",
    "mass",
  ],
});
