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
    "def:hecke-normal-form",
    "prop:frobenius-gram-matrix",
    "def:demand-profile",
  ],
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
      date: "2026-11-21",
      body: "**$S$ and $n_T$ defined from the corpus; the operator family and the cost $t$ are data, and no producer is attached (owner-authorised task \"Define S, n_T + producer\").** Fixed by the corpus: $G$ and $G^{+}$ (`pyhecke.gram.gram_matrix_mp` / `G_PINV`, convention D, owner ruling P2); the supply matrix, column $o = \\mathrm{NF}(\\beta(o))$ (Lean field `KnotOperatorLP.supply`; the $(\\mathbf{1},\\mathbf{1})$ entry of `computations/knot-operator-table.py`); the demand vector $n_T^{i} = \\max(0, -c_i)$ for $\\mathrm{NF}(T) = \\sum c_i b_i$ (`def:demand-profile` magnitudes; the demand vector $\\sum_{c_i<0} |c_i|\\, b_i^{\\vee}$ of `prf:knot-operator-selection`), now `demandVector` in the Lean. NOT fixed, so stated as data rather than chosen: (1) the operator family and braid words $\\beta(T_{m,m'})$. `knot-operator-table.py` lists $T_{1,0}, T_{2,1} = \\sigma_0, T_{2,2} = \\sigma_0^2, T_{2,3} = \\sigma_0\\sigma_1\\sigma_0, T_{2,5} = (\\sigma_0\\sigma_1)^2\\sigma_0$ in $H_3$; `prop:knot-operator-selection` and `torus-embeddable-complete` name the generator set $T_{1,0}$ and $T_{2,3}, T_{2,5}, T_{2,7}, T_{2,9}, T_{3,4}, T_{3,5}$. The two lists differ, and the closure of $\\sigma_0\\sigma_1\\sigma_0 \\in B_3$ is the Hopf link (conjugate to $\\sigma_0^2\\sigma_1$, then Markov destabilisation), not the trefoil. (2) the cost $t$, read as crossing energy: the corpus carries per-crossing weights $q$ / $-q^{-1}$ (`def:crossing-energy`), $\\tfrac12(q-q^{-1})$ (`binding-knots-visual-inventory`) and $q+q^{-1}$ (`chapter-overview`), and `confinement-operator-selection.py` uses $\\sum_i |c_i|\\,\\deg(b_i)\\,E_\\times$ on an NF vector. An LP producer needs both choices plus a target set, so none is written; the `computation` pointer stays absent. The block's theorem holds for every choice of these data.",
    },
    {
      kind: "status",
      date: "2026-11-21",
      body: "**No producer solves the stated LP; the `computation` pointer is removed.** The block declared `computations/wedderburn_pair_volumes.py` / `wedderburn-pair-volumes.witness.json` with status `verified`. That producer calls `solve_operator_selection_lp(t, G, n_target)` with $t_i = \\mathrm{tr}_M(b_i)$, the Gram matrix $G$ itself and a scalar net target $n_{\\mathrm{target}} = \\mathrm{net}(\\mathrm{NF}(B_3))$; the solver's program is $\\min t^{\\top}x$ subject to $\\mathbf{1}^{\\top}x = n_{\\mathrm{target}}$, $Gx \\ge 0$ and $x_i \\ge -M$ (a large box bound, not $x \\ge 0$). That is a different LP from $\\min t^{\\top}x$ subject to $G^{+}Sx \\ge n_T$, $x \\ge 0$. A search of `computations/` (`solve_operator_selection_lp`, `solve_frobenius_dual_lp`, `G_PINV`, `gram_quotient_inverse`, `pinv`) found no producer that solves the stated program: `solve_frobenius_dual_lp` imposes $Gx = u$ as an equality, and `confinement-operator-selection.py` / `gram-matrix-dual.py` apply $G^{+}$ to a demand profile without an LP. The block has no computational witness until such a producer exists. The witness file also records a stale `scriptHash` (`25431e10193a`, against `b093882f8ec9` for the current script); it is not refreshed here. The producer still names this block as the `source` of its assertions.",
    },
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
