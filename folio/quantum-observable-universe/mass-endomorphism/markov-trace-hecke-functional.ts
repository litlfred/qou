import { proposition } from "../../schema/builders";

/**
 * The Markov trace as a linear functional on the Hecke algebra, and the
 * connected-sum rule. Lifts the word evaluator `trWord` of
 * `prop:markov-trace-recursive-reducer` from positive braid words to the
 * presented Hecke tower, then to `QOU.Hecke.IwahoriHecke K q n`.
 */
export default proposition({
  label: "prop:markov-trace-hecke-functional",
  title:
    "The Markov trace is a linear functional on $H_n(q)$, and the connected-sum rule",
  authorNotes: [
    {
      kind: "status",
      date: "2026-11-22",
      body: "Proved in Lean, sorry-free (axioms propext, Classical.choice, Quot.sound): `towerTr`, `towerTr_mul_comm`, `towerTr_markov`, `towerTr_disjoint`, `towerTr_shift` (shift invariance), `towerTr_split` (tr(X·Y↑ᵐ⁺¹) = tr X·tr Y for X ∈ H_m), `towerTr_connectedSum`, `towerTr_interface`, `heckeMarkovTrace`, `heckeMarkovTrace_mul_comm`, `heckeMarkovTrace_σ`, `markovKnotFactor`, `markov_trace_eq_tau_mul_knotFactor`. Also proved: `heckeIncl`, `heckeShift`, `heckeMarkovTrace_heckeIncl` (coherence along inclusions), `heckeMarkovTrace_disjoint` and `heckeMarkovTrace_connectedSum` on the finite algebras (factor s z). Bond words: `towerTr_interfaceWord` (a block bond B gives the factor tr B), `towerTr_vertexCube_block`, `towerTr_overlapBond` and `towerTr_gammaGammaBond` (the overlapping γγ bond gives tr X · tr(V³ Y↑¹), independent of the first nucleon). This is the mechanism for the measured fact in `gamma-gamma-bond-is-pair-independent.witness.json` that μ depends only on the second nucleon. Checked 2026-11-22: the probe's trace (Σ_λ y_λ χ_λ over λ ⊢ 6, `y_lambda_su_n`, zero on three-row shapes) equals an independent exact Markov trace at z_D, proton pin, to ~3e-60 relative on W_free and W_atom for all four pairs, and μ = tr(V³·Y↑¹)/tr Y holds exactly. The probe's layout (bond appended after both nucleons) is `towerTr_overlapBond_appended` with m = 2. The independent trace was not ported line by line from `trWord`; both satisfy the Markov axioms, so they agree by `markovTrace_unique`.  Added 2026-11-22: `towerTr_gapBond` and `towerTr_singleGapBond` (a bond entering both nucleons through at most one interface letter a + bσ_m gives (a+bz)·tr(xA₁A₂)·tr(YC₁C₂)), the cross-ratio identities `towerTr_gapBond_crossRatio`, `towerTr_singleGapBond_crossRatio`, `towerTr_free_crossRatio` (μ_pp μ_nn = μ_pn μ_np), and `not_both_lt_one_of_crossRatio` (with all μ > 0, pn and np cannot both bind while pp and nn do not). The γγ chain: `ggChain`, `towerTr_ggChain` (tr = tr N₀ · ∏ tr(V³·N_j↑¹)), `he4_ggChain_word_eq`, `towerTr_he4_ggChain_word`, `he4_ggChain_trace_difference`. Binding-half readings (namespace `QOU.BraidKnot.BindingHalf`): `binding_eq_pair_wordDifference`, `pair_isTrace_iff_central`, `convolve_eq_pair`, `convolve_isTrace_iff`, `hecke_convolve_isTrace_iff`, `markov_free_pairing`, `markov_binding_eq_free_minus_atom_pair`. Probes: computations/probes/he4_bond_both_nucleons/, he4_closed_form/, knot_factor_binding_half/. Two interface letters: `towerTr_twoGapBond_reduce`, `towerTr_twoLetter_expand`, `towerTr_twoGap` (three product terms plus one cable term), `towerTr_twoGap_outerLeft`/`_outerRight` and their cross-ratio forms, `not_pattern_of_affine_rankOne`. Two bonds into one nucleon: `towerTr_rho2_all` (independent of bond order and of over/under transport), `towerTr_rho2_vertexCube`. Probes: he4_multi_gap_bond/, he4_crossing_remainder/. Strand reflection: `towerTr_reflect` (for a word in σ_0..σ_{n-1}, the trace is unchanged under σ_a ↦ σ_{n-1-a}), via the half-twist `garsideWord` and `garsideWord_mul_twGen` (Δ_n σ_a = σ_{n-1-a} Δ_n), `twWord_isUnit`, and cyclicity. Issue #8960.",
    },
  ],
  uses: ["prop:markov-trace-recursive-reducer"],
  cites: ["jones1987"],
  lean: {
    ref: "qou:QOU.BraidsAndKnots.BraidKnot.HeckeFunctional.towerTr_connectedSum",
    validation: "not_checked",
  },
  tags: ["markov-trace", "connected-sum", "linear-functional", "knot-factor"],
});
