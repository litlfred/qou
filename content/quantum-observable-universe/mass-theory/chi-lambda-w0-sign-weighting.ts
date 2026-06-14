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
    "rem:chi-v21-hoefsmit-matrix-derivation",
    "rem:chi-v111-via-sign-substitution",
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
    status: "experimental",
  },
  authorNotes: [
    {
      kind: "status",
      body: "**Sign-character weighting formalized as a proposition** (this\nblock) — the qualitative pattern (1, 0, −1) is now a theorem\nbacked by the per-irrep closed forms from  and the\nexplicit $S_3$ character values. **Magnitude closure remains\nopen** and is the natural next research question.",
    },
  ],
});
