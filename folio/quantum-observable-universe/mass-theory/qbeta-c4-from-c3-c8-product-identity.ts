import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:qbeta-c4-from-c3-c8-product-identity",
  title:
    "c_4 = c_8 / c_3 via the structural product identity c_3 · c_4 = c_8",
  tags: [
    "qbeta",
    "c-4",
    "c-k",
    "product-identity",
    "j-hopf",
    "silver-ratio",
    "lean",
  ],
  lean: {
    ref: "qou:QOU.QBeta.c4_eq_c8_div_c3_at_silver",
    validation: "not_checked",
  },
  computation: {
    engine: "sympy",
    script: "computations/qbeta/qbeta_silver_rationals.py",
    witness: "computations/qbeta/qbeta-silver-rationals.witness.json",
    status: "verified",
  },
  uses: ["prop:qbeta-c8-c10-silver-rationals"],
  authorNotes: [
    {
      kind: "status",
      body: "Wires the sorry-free norm_num Lean theorem c4_eq_c8_div_c3_at_silver: the product identities c_3·c_4=c_8 (c_4=−49/32) and c_3·c_6=c_9 (c_6=7/2) are verified exact at the silver ratio b²=7/8. Shares the silver-rationals verification script.",
    },
  ],
});
