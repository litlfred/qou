import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:qbeta-c8-c10-silver-rationals",
  title:
    "$\\mathfrak{Q}_\\beta$ c_8, c_9, c_10 closed-form values at the silver ratio q = 1 + √2",
  tags: [
    "qbeta",
    "c-k",
    "habiro",
    "silver-ratio",
    "pell-lucas",
    "closed-form",
    "lean",
  ],
  lean: {
    ref: "qou:QOU.QBeta.qbeta_c10_at_silver",
    validation: "not_checked",
  },
  computation: {
    engine: "sympy",
    script: "computations/qbeta/qbeta_silver_rationals.py",
    witness: "computations/qbeta/qbeta-silver-rationals.witness.json",
    status: "verified",
  },
  uses: [],
  authorNotes: [
    {
      kind: "status",
      body: "Wires the sorry-free norm_num Lean theorems qbeta_c{8,9,10}_at_silver to a computation: the rationals c_8=49/16, c_9=−7, c_10=343/128 are verified exact (sympy.Rational) with c_3=−2 and the Hoefsmit b²=7/8, the latter itself verified exact at q=1+√2. SUBDOMINANT-but-REAL: the silver/Q_A pole is a genuine subdominant kernel root (char ≈3.12, not the dominant ≈117.4); no fit, no c_k≥3 made canonical.",
    },
  ],
});
