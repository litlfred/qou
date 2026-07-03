import { theorem } from "../../schema/builders";

export default theorem({
  label: "thm:six-term-mass-formula-complete",
  title:
    "Six-term mass formula: derivation + computation index",
  lean: {
    ref: "qou:QOU.BraidKnot.six_term_mass_formula_complete",
    validation: "not_checked",
  },
  uses: [
    "prop:terms-2-6-higher-operations",
    "prop:chirality-writhe-ribbon-derivation",
  ],
  computation: {
    engine: "sympy",
    script: "computations/term6_residues_at_roots.py",
    witness: "computations/term6-residues-at-roots.witness.json",
    consumers: [
      "computations/term6_habiro_residue_mpfr_50dps_bridge.py",
    ],
    status: "verified",
  },
  tags: [
    "mass-formula",
    "six-term",
    "master-index",
    "completeness",
    "derivation-status",
  ],
});
