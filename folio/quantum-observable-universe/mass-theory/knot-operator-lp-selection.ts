import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:knot-operator-lp-selection",
  title:
    "Knot operators are selected per confinement by the Frobenius Gram-inverse LP/SDP dual basis",
  lean: {
    ref: "qou:QOU.BraidsAndKnots.knot_operator_lp_selection",
    validation: "not_checked",
  },
  uses: [
    "rem:gram-matrix-spectral-connection",
    "prop:weak-spectral-completeness",
  ],
  computation: {
    engine: "python",
    script: "computations/wedderburn_pair_volumes.py",
    witness:
      "computations/wedderburn-pair-volumes.witness.json",
    status: "verified",
  },
  tags: [
    "lp-dual",
    "sdp",
    "gram-inverse",
    "knot-operator",
    "operator-selection",
    "active-set",
    "confinement",
    "shadow-price",
  ],
  authorNotes: [
    {
      kind: "status",
      date: "2026-11-20",
      body: "**Lean restated to match this block (QA re-adjudication 2026-11-20).** The previous Lean `Optimal` maximised the objective and used the supply matrix without $G^{-1}$, and its class `KnotOperatorLPSelection` had no instance: at $n_T = 0$ strong duality forces the zero selection to be optimal, and complementary slackness then asks its empty support to be a singleton. That is now proved (`KnotOperatorLPSelectionLegacy.isEmpty`), so the old theorem was vacuous. The new Lean states the minimisation LP with constraint $G^{-1}Sx \\ge n_T$ and proves, sorry-free over any ordered commutative ring: weak duality, that a primal/dual pair with equal objectives is optimal on both sides, and complementary slackness ($y_i\\cdot\\text{slack}_i = 0$, $x_o\\cdot\\text{reduced cost}_o = 0$), bundled as `knot_operator_lp_selection`. Strong duality (existence of such a pair) is NOT proved; the theorem takes the equal-objective certificate as a hypothesis. Caveat: `⁻¹` is Mathlib's matrix inverse, which is $0$ when $\\det G$ is not a unit, and under convention D the Frobenius Gram matrix on $H_3(q)$ has a radical (see `prop:knot-operator-selection`); the theorems hold for any $G$ but are uninformative there. Producer `wedderburn_pair_volumes.py` made mpmath end to end the same day.",
    },
    {
      kind: "status",
      body: "**Open** as a fully-formalized proposition. The LP/SDP\ninfrastructure is already first-class\n([AGENTS.md §LP/SDP duals](https://github.com/litlfred/qou/blob/main/AGENTS.md))\nand witnesses for individual confinements are in place. To\npromote to `proposition`:\n\n1. **Discharge** the LP-feasibility $\\leftrightarrow$ confinement-realisability\n   equivalence (currently asserted as part of [`prop:operator-selection-lp`](#prop:operator-selection-lp); requires\n   a categorical-physics statement linking the Frobenius-positive\n   cone to physical confinement).\n2. **Verify** that for every authored confinement (proton,\n   neutron, deuteron, ...) the LP/SDP solver returns an active\n   set matching the existing categorical-physics identification.\n3. **Lean formalization**: encode the LP duality statement as a\n   class hypothesis with the witness data as an instance proof.",
    },
  ],
});
