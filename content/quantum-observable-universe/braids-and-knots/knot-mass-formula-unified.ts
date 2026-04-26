import { theorem } from "../../schema/builders";

export default theorem({
  label: "thm:knot-mass-formula-unified",
  title:
    "Unified mass formula: tower + Frobenius co-Casimir correction",
  lean: {
    ref: "qou:QOU.BraidKnot.knot_mass_unified",
    validation: "not_checked",
  },
  uses: [
    "prop:mass-endomorphism-tower",
    "thm:frobenius-codim-universal",
    "prop:partition-sum-proton-residual",
    "prop:categorical-mass-markov",
    "def:hecke-mass-element",
    "thm:jones-markov-trace",
    "cor:quantum-dilogarithm",
    "prop:figure-eight-bw-coefficients",
    "conj:knot-factor-frobenius-pairing",
  ],
  cites: ["kassel1995"],
  tags: [
    "mass",
    "knot",
    "vortex",
    "frobenius",
    "co-casimir",
    "tower",
    "unified-formula",
    "universal",
  ],
});
