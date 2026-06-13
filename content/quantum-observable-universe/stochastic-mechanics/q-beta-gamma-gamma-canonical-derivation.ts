import { remark } from "../../schema/builders";

export default remark({
  label: "rem:q-beta-gamma-gamma-canonical-derivation",
  title:
    "Story B selected as canonical $Q_\\beta$ interpretation by tracing the cat-action → Frobenius → Wedderburn → Wenzl bridge chain on canonical typed-$B_3$ braids; the $c_3 = -2$ Hopf-Jones identification is empirically observable at 112× residual reduction vs CODATA $Q_\\beta$ floor",
  interprets: "prop:q-beta-categorical-precision-ladder",
  uses: ["rem:kashiwara-jones-alternation-interpretation"],
  cites: [
    "wenzl1988",
    "jones1985",
    "hoefsmit1974",
  ],
  tags: [
    "gamma-gamma",
    "categorical-derivation",
    "story-A-vs-B",
    "wenzl-bridge",
    "story-B-canonical",
    "1ppb-roadmap",
  ],
  computation: {
    engine: "python+mpmath",
    script: "folio-assistant/computations/probe_q_beta_high_precision_ck.py",
    status: "experimental",
  },
  authorNotes: [
    {
      kind: "status",
      body: "This is a **derivation summary**, documenting the conclusion of the\nγγ chain trace. The chain itself is per-step formalised by:\n\n- [`prop:hoefsmit-V21-cos-symmetrization`](#prop:hoefsmit-V21-cos-symmetrization) (Step 1)\n- [`prop:markov-trace-frobenius-selection`](#prop:markov-trace-frobenius-selection) (Step 2)\n- [`prop:hecke-1d-irrep-closed-form-character`](#prop:hecke-1d-irrep-closed-form-character) (Steps 3-4)\n- [`prop:tau-M-asymptotic-rep-theory`](#prop:tau-M-asymptotic-rep-theory) (Steps 7-9)\n- [`prop:q-beta-categorical-precision-ladder`](#prop:q-beta-categorical-precision-ladder) (full ladder)",
    },
  ],
});
