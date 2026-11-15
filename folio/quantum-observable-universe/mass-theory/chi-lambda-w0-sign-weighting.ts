import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:chi-lambda-w0-sign-weighting",
  title:
    "Long-element $\\chi_\\lambda(w_0)$ sign-character weighting of the $c_k$ chain at $H_3$",
  lean: {
    ref: "qou:QOU.BraidKnot.chi_lambda_w0_sign_weighting",
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
    engine: "python",
    // Live H_3 Wedderburn per-block probe (Hoefsmit seminormal blocks,
    // y_lambda solve, chi_lambda(w_0) per block). The original
    // probe_per_wedderburn_block_ck.py producer was deleted; its k=5,6
    // sign-agreement witness survives only at
    // fsh-guts/deprecated/computations/chi-lambda-w0-sign-weighting.witness.json.
    script: "computations/option_e_phase1_h3_cross_check.py",
    witness: "computations/option-e-phase1-h3-cross-check.witness.json",
    status: "experimental",
  },
  authorNotes: [
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data." },
    {
      kind: "status",
      body: "**Sign-character weighting formalized as a proposition** (this\nblock) — the qualitative pattern (1, 0, −1) is now a theorem\nbacked by the per-irrep closed forms from  and the\nexplicit $S_3$ character values. **Magnitude closure remains\nopen** and is the natural next research question.",
    },
  ],
});
