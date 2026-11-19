import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:q-beta-c-2-eq-neg-one-structural",
  title:
    "$c_2 = -1$ in the $\\mathfrak{Q}_\\beta$ precision ladder is structural — the $(1 - b^2 \\cdot \\hbar_q^4)$ N=2 factor IS $(1 - u^2)$ with $u = b \\cdot \\hbar_q^2$, hence the $(1 + c_2 \\cdot u^2)$ coefficient is exactly $-1$ by ring identity",
  lean: {
    ref: "qou:QOU.QBeta.C2Structural.c_2_eq_neg_one_structural",
    validation: "not_checked",
  },
  uses: [
    "prop:q-beta-c-k-recursion-from-habiro-q-difference",
    "prop:q-beta-over-e0-classical-vanishing",
    "prop:t-beta-markov-frobenius-collapse",
  ],
  cites: ["jones1987", "wenzl1988"],
  computation: {
    engine: "sympy",
    script:
      "computations/qbeta/qbeta_symbolic_chain_alpha_b.py",
    witness: [
      "computations/qbeta/qbeta-symbolic-chain-alpha-b.witness.json",
      "computations/qbeta/qbeta-delta-element-fork-pricing.witness.json",
    ],
    status: "failed",
    // status was "verified" until 2026-08-23; the cited witness's own
    // `allPassed` is false (alpha_q0_matches_probe_n3_witness). Per ComputationStatus,
    // "failed" = script ran, witness does NOT match expected values.
    // Nothing compared the two until scripts/check-computation-status.py.,
  },
  tags: [
    "q-beta",
    "precision-ladder",
    "structural",
    "c-2",
    "categorical-derivation",
    "no-fit",
  ],
  authorNotes: [
    {
      kind: "caveat",
      date: "2026-11-16",
      body: "c_2 = -1 re-reads the N=2 factor 1 - b^2 hbar^4; N2_factor is a bare def with no derivation. The 5.6 ppm figure is on the retired z=1 base (convention C). On the ruled z_D base Q_base = 0.4447 MeV (-43.2%) and F_required = 1.759 exceeds the N=2 cap 1 - u^2 for every real phase (LadderFactorBound, EigenphaseQuantization; audit 2026-09-13 \u00a75.1). Mass-pipeline flag; no number changes.",
    },
    {
      kind: "status",
      body: "**Theorem (this proposition).** Sorry-free Lean proof\n([`q-beta-c-2-eq-neg-one-structural.lean`](q-beta-c-2-eq-neg-one-structural.lean))\n— one-line `ring` identity in `CommRing R`.\n\n**Compute (sympy).** Verified in\n[`qbeta_symbolic_chain_alpha_b.py`](https://github.com/litlfred/qou/blob/main/computations/qbeta/qbeta_symbolic_chain_alpha_b.py)\nwitness `qbeta-symbolic-chain-alpha-b.witness.json`, assertion\n`N2_factor_equals_one_minus_u_squared` (passing, tolerance $10^{-20}$).",
    },
  ],
});
