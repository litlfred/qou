import { remark } from "../../schema/builders";

export default remark({
  label: "rem:chi-per-irrep-cyclotomic-closed-forms",
  interprets: "rem:chi-v3-closed-form-proof",
  title:
    "All three $V_\\lambda$ per-irrep character difference closed forms with **cyclotomic factor pattern**: $V_{(3)}, V_{(1,1,1)}$ → $\\Phi_4^2$; $V_{(2,1)}$ → $\\Phi_8$; denominator powers $q, q^3, q^5$ track content sum",
  uses: [
    "rem:chi-v3-closed-form-proof",
    "rem:post-pr665-open-rd-inventory",
    "prop:hoefsmit-V21-cos-symmetrization",
    "rem:typed-b3-sub-braid-extraction",
  ],
  cites: [
    "jones1985",
    "wenzl1988",
    "hoefsmit1974",
    "kassel1995",
  ],
  tags: [
    "lean-infrastructure",
    "per-wedderburn-block",
    "closed-form",
    "cyclotomic",
    "v21-hoefsmit-matrix",
    "conjugate-partition-symmetry",
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
