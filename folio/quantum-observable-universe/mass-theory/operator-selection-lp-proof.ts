import { proof } from "../../schema/builders";

export default proof({
  label: "prf:operator-selection-lp",
  title: "Proof of operator selection lp",
  authorNotes: [
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
  computation: {
    engine: "mpmath",
    script: "computations/m_p_substrate_identity_50dps.py",
    witness: "computations/m-p-substrate-identity-50dps.witness.json",
    status: "verified",
  },
});
