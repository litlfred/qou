import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:q-beta-radius-of-convergence-gate",
  title:
    "$\\mathfrak{Q}_\\beta$ precision-ladder $\\S 4(a)$ gate — the log-correction generating function $g(u) = \\sum_{k \\ge 2} c_k u^k$ has a unique dominant simple pole at $u_{\\text{substrate}}$ (convention-C frame)",
  lean: {
    ref: "qou:QOU.QBeta.RadiusOfConvergenceGate.qbeta_g_simple_pole_at_u_substrate",
    validation: "not_checked",
  },
  uses: [
    "prop:q-beta-bar-even-kernel-invariant",
    "prop:q-beta-c-k-recursion-from-habiro-q-difference",
    "prop:q-beta-c-2-eq-neg-one-structural",
    "conj:qbeta-c-k-closed-forms",
  ],
  cites: ["jones1987", "wenzl1988", "habiro2004"],
  computation: {
    engine: "python+mpmath",
    script:
      "computations/qbeta/qbeta_radius_of_convergence_gate_probe.py",
    witness:
      "computations/qbeta/qbeta-radius-of-convergence-gate-probe.witness.json",
    status: "verified",
  },
  tags: [
    "q-beta",
    "precision-ladder",
    "formalize-first",
    "radius-of-convergence",
    "simple-pole",
    "kernel-invariant",
    "convention-c-frame",
    "open-rd",
  ],
  authorNotes: [
    {
      kind: "note",
      date: "2026-08-08",
      body: `**Base ring (§7c) — \`ℝ\` is load-bearing.** The subject is a *radius of convergence* and a pole location on the real line, and \`u_substrate\` is a hard-coded decimal (\`0.008517234550156142\`). A radius of convergence is a metric notion and a decimal literal is an archimedean evaluation; neither survives passage to a generic commutative ring.`,
    },
    {
      kind: "status",
      date: "2026-11-15",
      body:
        "**Conjecture (demoted from proposition 2026-11-15, owner choice " +
        "\"Conjecture + re-scope\").** The former statement asserted an exact " +
        "pole location and called every other candidate \"structurally " +
        "REFUTED\". That cannot follow from the evidence: the only input is the " +
        "finite window $c_2, \\ldots, c_{10}$, and finitely many Taylor " +
        "coefficients do not determine where a generating function's poles are " +
        "(adding $u^{11} h(u)$ with $h$ rational moves the pole anywhere and " +
        "leaves the window unchanged). The window is *consistent* with a simple " +
        "dominant pole at $u_{\\text{substrate}}$, which is what is now claimed, " +
        "as a conjecture. The $c_k$ themselves are the convention-C frame " +
        "(`conj:qbeta-c-k-closed-forms`; $c_k$ for $k \\ge 4$ are calibrated " +
        "against the CODATA residual), and no ladder exists yet under " +
        "convention D (bean `qou-cds1`). **Lean:** the sibling file's " +
        "`qbeta_g_simple_pole_at_u_substrate` projects the class field " +
        "`pole_location_is_u_substrate`, i.e. it assumes its conclusion; it is " +
        "a statement of the conjecture, not a proof of it. **Compute:** " +
        "`qbeta_radius_of_convergence_gate_probe.py` measures the window " +
        "signature (flat $c_k u_0^k$, ratio test) and demonstrates the test on " +
        "a mislocated candidate pole; it is evidence, not a proof.",
    },
  ],
});
