import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:term6-binding-density",
  title:
    "Term 6 binding density: $B(Z,N)/A \\approx \\alpha \\cdot T_6(Z,N)/A^3 + \\beta + \\delta_M(Z,N)$",
  tags: [
    "binding-energy",
    "gs-filtration",
    "spectral-sequence",
    "term-6",
    "level-3-stratum",
    "calibrated-fit",
    "magic-shell-correction",
  ],
  uses: [
    "prop:gb-spectral-sequence",
    "rem:mass-endomorphism-jet-tower",
    "thm:markov-trace-factorization",
    "prop:wigner-np-pairing",
    "conj:categorical-neutrality-saturated-shells",
  ],
  cites: ["bethe1936", "weizsacker1935", "geckpfeiffer2000"],
  lean: {
    ref: "qou:QOU.BraidKnot.Term6BindingDensity",
    validation: "not_checked",
  },
});
