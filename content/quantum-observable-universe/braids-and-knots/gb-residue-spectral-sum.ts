import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:gb-residue-spectral-sum",
  title:
    "Gröbner–Shirshov residue spectral sum for the mass trace",
  lean: {
    decl: "QOU.BraidKnot.gb_residue_spectral_sum",
    validation: "not_checked",
  },
  uses: [
    "def:confinement-level",
    "def:hecke-normal-form",
    "prop:confinement-level-unique",
    "prop:hecke-mass-trace",
    "prop:categorical-mass-markov",
    "thm:jones-markov-trace",
    "cor:quantum-dilogarithm",
    "prop:mass-endomorphism-tower",
    "conj:mass-endomorphism",
    "def:habiro-ring",
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
