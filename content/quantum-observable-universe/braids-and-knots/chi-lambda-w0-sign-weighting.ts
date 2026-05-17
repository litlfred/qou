import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:chi-lambda-w0-sign-weighting",
  title:
    "Long-element $\\chi_\\lambda(w_0)$ sign-character weighting of the $c_k$ chain at $H_3$",
  lean: {
    ref: "qou:QOU.BraidKnot.ChiLambdaW0SignWeighting",
    validation: "not_checked",
  },
  uses: [
    "rem:chi-per-irrep-cyclotomic-closed-forms",
    "rem:chi-v3-closed-form-proof",
    "rem:chi-v21-hoefsmit-matrix-derivation",
    "rem:chi-v111-via-sign-substitution",
    "prop:alpha-k-derivation-procedure",
  ],
  cites: [
    "kassel1995",
    "wenzl1988",
    "hoefsmit1974",
  ],
  tags: [
    "c-k",
    "wedderburn",
    "sign-character",
    "long-element",
    "s3-representation-theory",
    "markov-trace",
    "per-block",
    "open-rd-item-3",
  ],
  computation: {
    engine: "python+mpmath",
    script: "folio-assistant/computations/probe_per_wedderburn_block_ck.py",
    witness: [
      "folio-assistant/computations/per-wedderburn-block-ck.witness.json",
    ],
    status: "experimental",
  },
});
