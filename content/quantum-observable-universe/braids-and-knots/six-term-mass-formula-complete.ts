import { theorem } from "../../schema/builders";

export default theorem({
  label: "thm:six-term-mass-formula-complete",
  title:
    "Six-term mass formula: derivation + computation index",
  lean: {
    decl: "QOU.BraidKnot.six_term_mass_formula_complete",
    validation: "not_checked",
  },
  uses: [
    "thm:knot-mass-formula-unified",
    "prop:categorical-mass-markov",
    "prop:mass-endomorphism-tower",
    "thm:frobenius-codim-universal",
    "prop:partition-sum-proton-residual",
    "prop:three-parameters-wedderburn",
    "prop:figure-eight-bw-coefficients",
    "prop:gb-residue-spectral-sum",
    "prop:gb-spectral-sequence",
    "prop:e-infinity-page-identifications",
    "prop:terms-2-6-higher-operations",
    "prop:chirality-writhe-ribbon-derivation",
    "def:habiro-ring",
    "rem:kashaev-volume-density",
  ],
  tags: [
    "mass-formula",
    "six-term",
    "master-index",
    "completeness",
    "derivation-status",
  ],
});
