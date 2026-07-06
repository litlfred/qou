import QOU.Braiding.HnMarkovTrace

/-!
# QOU.BraidKnot.JonesViaMarkovTrace — Jones value of the Hopf link via the Markov trace

**Tier-3 (bean `60iz`, epic `08a2`)** first real layer of the Jones-polynomial /
knot-invariant infrastructure behind
`jet_filtered_knot_factor.jonesQuotient`. Per the framework convention
(AGENTS.md §7a, `thm:jones-markov-trace`; Jones 1987, Wenzl 1988) the Jones
polynomial is the Markov trace of a braid's Hecke image,
`J_L(q) = tr_M(ρ(β_L))`.

This builds on the **real** q-deformed Markov-trace abstraction
`QOU.Braiding.MarkovTraceTower` — *complementary* to #2743's `q = 1` `k[S_n]`
Wedderburn build (this is the `H_n(q)` Markov trace, that is the symmetric-group
algebra). The `σ_1²`-closure is the **Hopf link**
(`QOU.BraidKnot.BraidLinkTypes.closure2 σ_sq = Link.hopfLink`), so the Markov
trace `trM_sigma1_sq` *is* the Jones value of the Hopf link.

The load-bearing content is `jonesHopf_invariant`: the Jones value is a **link
invariant** because the Markov trace is stabilisation-invariant
(strand-count-independent) — the proved reason the Markov trace descends to a
knot/link invariant. Sorry-free.
-/

namespace QOU.BraidKnot

open QOU.Braiding

variable (q : ℝ)

/-- **Jones value of the Hopf link**, via the Markov trace on the `H_n(q)`
    tower: `J(Hopf) = tr_M(σ_1²)`, evaluated at the base strand count `n = 2`
    (the `σ_1²`-closure is the Hopf link, `BraidLinkTypes.closure2`). -/
noncomputable def jonesHopf [T : MarkovTraceTower q] : ℝ :=
  T.trM_sigma1_sq 2

/-- **The Jones value is a link invariant.** The Markov trace of `σ_1²` computed
    in any `H_n(q)` with `n ≥ 2` agrees with the base `H_2` value `jonesHopf`,
    by Markov stabilisation (`σ_1²` uses only the first generator, so extra
    strands contribute `z · z⁻¹ = 1`). This is exactly the property that makes
    the Markov trace descend to a knot/link invariant (Jones 1987). Sorry-free. -/
theorem jonesHopf_invariant [T : MarkovTraceTower q]
    (n : ℕ) (hn : 2 ≤ n) :
    T.trM_sigma1_sq n = jonesHopf q := by
  unfold jonesHopf
  exact T.trM_sigma1_sq_stabilises n 2 hn (le_refl 2)

/-- **Closed form of the Hopf-link Jones value** in the canonical Wenzl-regime
    instance (`q > 1`):
    `J(Hopf) = (q^{5/2} − q^{1/2} + q² + q) / (q² + q)`. -/
theorem jonesHopf_canonical (hq : 1 < q) :
    jonesHopf q (T := markovTraceTower_canonical q hq) =
      (q ^ ((5 : ℝ) / 2) - q ^ ((1 : ℝ) / 2) + q ^ 2 + q) / (q ^ 2 + q) :=
  rfl

/-- **The Hopf-link Jones value is positive** in the Wenzl regime (`q > 1`):
    the canonical closed form is a ratio of positive reals (numerator
    `≥ (q² + q) > 0` since `q^{5/2} ≥ q^{1/2}` for `q ≥ 1`). In particular it is
    nonzero, so it is a valid normalization. Sorry-free. -/
theorem jonesHopf_pos (hq : 1 < q) :
    0 < jonesHopf q (T := markovTraceTower_canonical q hq) := by
  rw [jonesHopf_canonical q hq]
  have hq0 : (0 : ℝ) < q := lt_trans zero_lt_one hq
  have h52 : q ^ ((1 : ℝ) / 2) ≤ q ^ ((5 : ℝ) / 2) :=
    Real.rpow_le_rpow_of_exponent_le hq.le (by norm_num)
  have hden : 0 < q ^ 2 + q := by positivity
  apply div_pos _ hden
  nlinarith [h52, hq0, sq_nonneg q]

end QOU.BraidKnot
