import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:gb-residue-spectral-sum",
  title:
    "Gröbner–Shirshov residue spectral sum for the mass trace",
  lean: {
    ref: "qou:QOU.BraidKnot.gb_residue_spectral_sum",
    validation: "not_checked",
  },
  uses: [
    "prop:confinement-level-unique",
    "prop:graded-markov-trace-from-gs-filtration",
    "prop:residue-at-root",
  ],
  tags: [
    "mass",
    "filtration",
    "groebner-shirshov",
    "residue",
    "spectral-sequence",
    "quantum-dilogarithm",
    "cohomology",
  ],
});
