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
