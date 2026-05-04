import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:six-term-per-derivation-weights",
  title: "Per-derivation weights for the six-term mass formula",
  lean: {
    ref: "qou:QOU.BraidKnot.SixTermPerDerivationWeights.binding_assembly",
    validation: "not_checked",
  },
  uses: [
    "thm:six-term-mass-formula-complete",
    "prop:categorical-mass-markov",
    "prop:binding-scale-catalan",
    "thm:frobenius-codim-universal",
    "prop:chirality-dual-space-derivation",
    "prop:full-pole-structure-mass-trace",
    "prop:mass-endomorphism-tower",
  ],
  cites: [],
});
