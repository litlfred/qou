import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:q-beta-radius-of-convergence-gate",
  title:
    "$\\mathfrak{Q}_\\beta$ precision-ladder $\\S 4(a)$ formalize-first gate — the log-correction generating function $g(u) = \\sum_{k \\ge 2} c_k u^k$ must have a simple pole at $u_{\\text{substrate}}$, and any candidate $F(q)$ whose nearest singularity lies elsewhere is structurally REFUTED",
  lean: {
    ref: "qou:QOU.QBeta.RadiusOfConvergenceGate.qbeta_g_simple_pole_at_u_substrate",
    validation: "not_checked",
  },
  uses: [
    "prop:q-beta-bar-even-kernel-invariant",
    "prop:q-beta-c-k-recursion-from-habiro-q-difference",
    "prop:q-beta-c-2-eq-neg-one-structural",
  ],
  cites: ["jones1987", "wenzl1988", "habiro2004"],
  computation: {
    engine: "python+sympy+mpmath",
    script:
      "folio-assistant/computations/qbeta/qbeta_radius_of_convergence_gate_probe.py",
    witness:
      "folio-assistant/computations/qbeta/qbeta-radius-of-convergence-gate-probe.witness.json",
    status: "verified",
  },
  tags: [
    "q-beta",
    "precision-ladder",
    "structural",
    "formalize-first",
    "radius-of-convergence",
    "simple-pole",
    "kernel-invariant",
    "no-fit",
  ],
  authorNotes: [
    {
      kind: "status",
      body:
        "**Theorem (this proposition, the gate direction).** Sorry-free " +
        "Lean proof (`q-beta-radius-of-convergence-gate.lean`) — conditional " +
        "theorem over `CommRing R` / the `RadiusOfConvergenceGateClass` " +
        "typeclass (§3b-cond); the forward direction (the cross-anchor " +
        "asymptotic-pole test) is a class hypothesis. **Compute (sympy + " +
        "mpmath):** verified in `qbeta_radius_of_convergence_gate_probe.py` " +
        "(witness `qbeta-radius-of-convergence-gate-probe.witness.json`) — " +
        "verifies the substrate anchors and demonstrates the gate on " +
        "candidate forms (passing: canonical SDP $c_k$ series; failing: a " +
        "mislocated pole at $u_0 = 2 u_{\\text{substrate}}$).",
    },
  ],
});
