import { proof } from "../../schema/builders";

export default proof({
  label: "prf:operator-selection-lp",
  title: "Proof of operator selection lp",
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): LP formulation is dual to the spectral decomposition of\n[knot operator selection](#prop:knot-operator-selection), part (i).\nThe" },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): ## Confinement as the special case $n = 3$, $d = 6$\n\nSetting $n = 3$ and $d = 6$ recovers the\n[confinement LP](#prop:confinement-lp) exactly:\n\n| General LP | Confinement LP ($n = 3$) |\n|:---|:---|\n| Basis $\\{b_1, \\ldots, b_d\\}$ | $\\{\\gamma, \\sigma_0, \\sigma_1, L_+, L_-, e^-\\}$ |\n| Gram matrix $G \\in \\mathbb{R}^{d \\times d}$ | $6 \\times 6$ Gram matrix of $H_3(q)$ |\n| Target $n_{\\mathrm{target}}$ | $\\approx 1.000$ (proton), $\\approx 0.811$ (neutron) |\n| Optimal $x^*$ | not determined by the program — the minimisers form a face at objective $0$. $\\mathrm{NF}(\\mathcal{B}_3) \\approx (+0.998, -0.010, +0.009, +0.046, -0.044, 0)$ is **feasible but not optimal** ($\\mathrm{tr}_M \\approx 0.9986$). |\n| Active set $\\mathcal{A}$ | $\\{\\sigma_0, L_-\\}$ (two active demand channels) |\n\nThe confinement LP is the $n = 3$ instantiation: three strands\nencoding three quark colors, six NF basis elements spanning the\noperator space, and the Borromean link $\\mathcal{B}_3$ as the unique\nLP vertex." },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): directions the trace cannot see. Proved in [`MarkovGramDegenerate.lean`](../lean/QOU/QBeta/MarkovGramDegenerate.lean)." },
    {
      kind: "caveat",
      date: "2026-08-24",
      body:
        "**The program is degenerate and does not select an operator.** Because " +
        "the NF basis begins with the identity, `G[1][j] = tr_M(1 . b_j) = t_j`: " +
        "the first row of the Gram matrix IS the objective vector, so the " +
        "Frobenius positivity constraint at i = 1 is `t.x >= 0` — the objective " +
        "bounded below by its own constraint. The optimal value is therefore " +
        "identically 0 for every n, every q and every trace convention, and " +
        "`y_0* = 0` follows by strong duality. The minimisers form a " +
        "positive-dimensional face (>= 6 vertices at n = 3, in mirror pairs), so " +
        "no distinguished `Phi*` exists. And NF(B_3) — tabulated in the proof " +
        "block as the n = 3 optimum — is feasible but NOT optimal, with " +
        "objective tr_M(B_3) ~ 0.9986 against an optimum of 0. Measured in " +
        "`computations/meson/operator_selection_lp_objective_audit.py`; full " +
        "analysis in `docs/audits/2026-08-24-operator-selection-lp-objective-defect.md`. " +
        "No replacement objective is proposed here — that needs the author's " +
        "intent (bean `qou-v7qj`).",
    },
  ],
  uses: ["prop:operator-selection-lp"],
});
