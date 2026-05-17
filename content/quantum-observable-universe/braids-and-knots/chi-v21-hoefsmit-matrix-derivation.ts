import { remark } from "../../schema/builders";

export default remark({
  label: "rem:chi-v21-hoefsmit-matrix-derivation",
  lean: {
    ref: "qou:QOU.BraidKnot.chi_v21_hoefsmit_matrix_derivation",
    validation: "not_checked",
  },
  interprets: "rem:chi-per-irrep-cyclotomic-closed-forms",
  title:
    "V_(2,1) Hoefsmit 2×2 matrix derivation scaffolding: scalar trace + Hecke-quadratic identities + Laurent decomposition of the closed form $-(q^4+1)(q^2-1)/(4q^3)$",
  uses: [
    "rem:chi-per-irrep-cyclotomic-closed-forms",
    "prop:hoefsmit-V21-cos-symmetrization",
    "rem:post-pr665-open-rd-inventory",
  ],
  cites: ["hoefsmit1974", "jones1985", "wenzl1988"],
  tags: [
    "lean-infrastructure",
    "v21-hoefsmit",
    "matrix-derivation",
    "laurent-decomposition",
    "scaffolding",
  ],
  computation: {
    engine: "sympy",
    script: "folio-assistant/computations/probe_per_wedderburn_block_ck.py",
    witness: [
      "folio-assistant/computations/per-wedderburn-block-ck.witness.json",
    ],
    status: "experimental",
  },
});
