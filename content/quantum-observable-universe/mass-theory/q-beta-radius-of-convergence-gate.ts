import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:q-beta-radius-of-convergence-gate",
  title:
    "$Q_\\beta$ precision-ladder $\\S 4(a)$ formalize-first gate — the log-correction generating function $g(u) = \\sum_{k \\ge 2} c_k u^k$ must have a simple pole at $u_{\\text{substrate}}$, and any candidate $F(q)$ whose nearest singularity lies elsewhere is structurally REFUTED",
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
    engine: "sympy+mpmath",
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
});
