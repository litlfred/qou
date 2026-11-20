import { remark } from "../../schema/builders";

export default remark({
  label: "rem:beta-decay-skein-properties",
  interprets: "def:beta-decay-skein",
  title:
    "Weak vertex, $10$-crossing budget, and $Q$-value of the $\\beta$-decay Skein operation",
  tags: [
    "beta-decay",
    "skein-relation",
    "groebner-basis",
    "hecke-algebra",
    "weak-force",
    "crossing-change",
    "lepton",
    "normal-form",
  ],
  uses: [
    "def:beta-decay-skein",
    "def:stable-nucleus",
    "prop:nuclear-groebner-reduction",
    "def:categorical-proton",
    "def:categorical-neutron",
    "rem:force-knot-identification",
    "def:Q-value-transition",
  ],
  authorNotes: [
    {
      kind: "caveat",
      date: "2026-11-20",
      body:
        "**Scope note (R3, bean `qou-99qc`): the T(3,5) claims machine-checked, exact arithmetic.** " +
        "Probe `computations/probes/qbeta_r253/r3_t35_crossing_budget_probe.py` (pre-registered). " +
        "HOLD: $(\\sigma_1\\sigma_2)^5$ has $10$ letters and closes to a knot; $\\sigma_1^3$ left-divides it in $B_3^+$ " +
        "(six positive length-$7$ cofactors, e.g. $\\sigma_2\\sigma_1^3\\sigma_2\\sigma_1^2$; Burau, faithful on $B_3$). " +
        "DO NOT HOLD as stated: (i) the $3+0+7$ split is not produced by Gröbner–Shirshov reduction and is not unique " +
        "($40$ placements of a $\\sigma_i^3$ block with positive complement); (ii) the $7$ residual crossings cannot be " +
        "absorbed by R2 moves, since a positive word has no $\\sigma\\sigma^{-1}$ pair (the text's 'R2' is the Hecke quadratic " +
        "relation); (iii) the number of quadratic-relation steps is order-dependent ($25$ leftmost-first, $30$ rightmost-first, " +
        "same normal form), so 'the net R2 step count' is not defined; (iv) under convention D, " +
        "$\\mathrm{tr}_{z_D}((\\sigma_1\\sigma_2)^5) = q^2(q^{12}+q^8-1)/(q^2+1)^2 \\notin \\mathbb{Z}[q^{\\pm1/2}]$; " +
        "(v) $\\mathcal{B}_n(\\sigma_1\\sigma_2)^5$ is not a scalar multiple of $\\mathcal{B}_p$ in $H_3(q)$. " +
        "The $Q$ formula uses the excised convention-C pair-Skein scale and the undefined step count, so no convention-D " +
        "$Q_\\beta$ follows from this block. Lean `crossing_budget_correct` is true by the structure's own field and checks nothing.",
    },
  ],
});
