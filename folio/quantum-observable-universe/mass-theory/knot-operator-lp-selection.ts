import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:knot-operator-lp-selection",
  title:
    "Knot operators are selected per confinement by the LP/SDP dual basis of the Frobenius Gram pseudo-inverse",
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
      body: "**Gram pseudo-inverse (owner ruling 2026-11-20, option A of `docs/audits/2026-11-20-qa-fails-proposals.md` P2).** The constraint is $G^{+}Sx \\ge n_T$, with $G^{+}$ the Moore–Penrose pseudo-inverse of the Frobenius Gram matrix, i.e. the inverse on $H_n(q)/\\mathrm{rad}$; this is the matrix the code uses (`pyhecke.gram.G_PINV`, `gram_quotient_inverse`), since under convention D the Gram matrix on $H_3(q)$ has a radical and `gram_inverse()` raises. The Lean carries $G^{+}$ as a field of the LP data with the four Penrose conditions (`IsMoorePenrose`) and sets $M = G^{+}S$; it proves `gramPinv_eq_inv_of_isUnit_det` ($G^{+} = G^{-1}$ when $\\det G$ is a unit), and, sorry-free over any ordered commutative ring: weak duality, that a primal/dual pair with equal objectives is optimal on both sides, and complementary slackness, bundled as `knot_operator_lp_selection`. Strong duality (existence of such a pair) is NOT proved; the theorem takes the equal-objective certificate as a hypothesis. The earlier Lean (maximisation, no Gram factor) carried a class with no instance, proved empty as `KnotOperatorLPSelectionLegacy.isEmpty`. No compute number moves; whether `wedderburn_pair_volumes.py` passes $G$ or $G^{+}$ to its solver has not been checked against this statement.",
    },
    {
      kind: "status",
      body: "**Open** as a fully-formalized proposition. The LP/SDP\ninfrastructure is already first-class\n([AGENTS.md §LP/SDP duals](https://github.com/litlfred/qou/blob/main/AGENTS.md))\nand witnesses for individual confinements are in place. To\npromote to `proposition`:\n\n1. **Discharge** the LP-feasibility $\\leftrightarrow$ confinement-realisability\n   equivalence (currently asserted as part of [`prop:operator-selection-lp`](#prop:operator-selection-lp); requires\n   a categorical-physics statement linking the Frobenius-positive\n   cone to physical confinement).\n2. **Verify** that for every authored confinement (proton,\n   neutron, deuteron, ...) the LP/SDP solver returns an active\n   set matching the existing categorical-physics identification.\n3. **Lean formalization**: encode the LP duality statement as a\n   class hypothesis with the witness data as an instance proof.",
    },
  ],
});
