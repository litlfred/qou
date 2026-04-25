import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:mass-formula-regime-switching",
  title:
    "Mass formula regime switch: SW+Frob for $A \\leq 2$, BW+$\\chi$ for $A \\geq 3$ (non-additive)",
  lean: {
    ref: "qou:QOU.BraidKnot.mass_formula_regime_switching",
    validation: "not_checked",
  },
  uses: [
    "thm:knot-mass-formula-unified",
    "thm:frobenius-codim-universal",
    "prop:figure-eight-bw-coefficients",
    "prop:partition-sum-proton-residual",
    "prop:categorical-mass-markov",
    "prop:schur-weyl-mass-decomposition",
    "rem:deuteron-first-principles",
    "rem:np-discrepancy-resolution",
  ],
  tags: [
    "mass-formula",
    "unification",
    "regime-switching",
    "bethe-weizsacker",
    "schur-weyl",
    "chirality",
  ],
});
