import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:magic-requires-higher-cohomology",
  title:
    "Proposition 8. Magic shell SDP optimum requires non-trivial $E_\\infty^{p, q \\geq 1}$ contribution",
  lean: {
    ref: "qou:QOU.LiftingDescent.HigherCohomology.MagicRequiresHigherCohomology",
    validation: "not_checked",
  },
  uses: [
    "conj:homological-shell-condensation",
    "conj:sdp-rank-collapse-magic-shell",
    "conj:magic-from-iterative-brane-tower",
    "conj:mass-endomorphism",
    "prop:torus-knot-shell-binding",
    "prop:torus-knot-generators",
    "def:brings-surface",
  ],
  cites: [
    "yekutieli2010",
    "kassel1995",
    "mathas1999",
  ],
  tags: [
    "spectral-sequence",
    "cohomology",
    "hopf-link",
    "torus-knot",
    "brings-surface",
    "magic-numbers",
    "open-problem",
    "axiom-class",
  ],
});
