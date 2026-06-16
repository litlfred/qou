import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:q-beta-q-eq-one-shadow-gate",
  title:
    "$\\mathfrak{Q}_\\beta$ precision-ladder $\\S 4(c)$ formalize-first gate — any candidate Habiro element $F(q)$ must reproduce the canonical integer shadows at $q = 1$: $c_2 \\to -1$ (the structural N=2 anchor) and $c_3 \\to J_{\\text{Hopf}}(1) = -2$ (registry anchor); a candidate failing either is structurally REFUTED",
  lean: {
    ref: "qou:QOU.QBeta.QOneShadowGate.qbeta_q_eq_one_shadow_anchors",
    validation: "not_checked",
  },
  uses: [
    "prop:q-beta-bar-even-kernel-invariant",
    "prop:q-beta-radius-of-convergence-gate",
    "prop:q-beta-c-2-eq-neg-one-structural",
    "prop:q-beta-c-k-recursion-from-habiro-q-difference",
  ],
  cites: ["jones1987", "wenzl1988", "habiro2004"],
  computation: {
    engine: "python+sympy+mpmath",
    script:
      "folio-assistant/computations/qbeta/qbeta_q_eq_one_shadow_gate_probe.py",
    witness:
      "folio-assistant/computations/qbeta/qbeta-q-eq-one-shadow-gate-probe.witness.json",
    status: "verified",
  },
  tags: [
    "q-beta",
    "precision-ladder",
    "structural",
    "formalize-first",
    "classical-limit-shadow",
    "kernel-invariant",
    "no-fit",
  ],
  authorNotes: [
    {
      kind: "status",
      body:
        "**Theorem (this proposition).** Sorry-free Lean proof " +
        "(`q-beta-q-eq-one-shadow-gate.lean`) — §3b-cond conditional class " +
        "`QOneShadowGateClass` with two field hypotheses (the $c_2$ and $c_3$ " +
        "classical-limit anchors) plus a rejection lemma. **Compute (sympy + " +
        "mpmath):** verified in `qbeta_q_eq_one_shadow_gate_probe.py` " +
        "(witness `qbeta-q-eq-one-shadow-gate-probe.witness.json`) — verifies " +
        "$c_2 \\to -1$, $c_3 \\to -2$ and the gate on passing / failing " +
        "rational candidates.",
    },
  ],
});
