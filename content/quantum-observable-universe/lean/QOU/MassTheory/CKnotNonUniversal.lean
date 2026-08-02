/-
# `C_knot` is non-universal — no level-only rescale closes binding (T/³He mirror invariant)

The master binding formula is `B(K) = m_e · |Σ_λ y_λ χ^λ(β_K) sgn(w_0) f^λ| = m_e · S(K)` with the
weight `y_λ` now PINNED to the derived Wenzl Markov weight (`BindingWeightMarkovPinning`, PR #4543),
`Σ_λ y_λ f^λ = tr_M(1) = 1`. The residual `C_knot(K) = B_AME(K)/(m_e · S(K))` is the FITTED deficit —
the open Δ_λ gate (bean `qou-3q7t`).

The companion probe `c_knot_nonuniversal_pinned_weight_probe.py` measures, with this ONE derived weight
(all 0-fit, exact mpmath):

  `C_knot(D) = 5.85`, `C_knot(T) = 4.44`, `C_knot(³He) = 3.29`, `C_knot(⁴He) = 9.31`  → spread 2.83×.

**The formalize-first invariant (this file):** the triton `T` and helion `³He` sit at the SAME strand
count `H₉`, so any *level-only* closure `B(K) = g(n_K, q₀) · m_e · S(K)` would force the SAME rescale
`g(9, q₀)` to reproduce both `B_AME(T)` from `S(T)` and `B_AME(³He)` from `S(³He)`. But the measured
`(B, S)` pairs make that impossible: `B_T · S_He ≠ B_He · S_T` (the cross-multiplied form of
`B_T/S_T ≠ B_He/S_He`). Hence **no level-only rescale `g(n, q₀)` closes binding** — `C_knot` carries
genuine per-knot (isospin / mirror) content, not captured by `(n, q₀)`.

This is a **scope-(b) structural exclusion of the level-only-rescale closure class** (cited invariant:
`mirror_cross_ne`). It does NOT exclude a per-knot Δ_λ derivation — that stays OPEN (`qou-3q7t`). The
numerical values are experimental `B_AME` (diagnostic only, never inverted into a weight) and the
substrate-derived `S(K)` from the pinned Markov weight; `free_parameters = 0`, nothing wired.
-/
import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring
import Mathlib.Data.Real.Basic

namespace QOU.MassTheory.CKnotNonUniversal

/-- Master-formula magnitude `S(K) = |Σ_λ y_λ χ^λ(β_K) sgn f^λ|` for the triton, at `H₉`, with the
pinned Wenzl weight (probe `c-knot-nonuniversal-pinned-weight.witness.json`). -/
def S_T : ℝ := 3.7349054

/-- Master-formula magnitude `S(K)` for the helion `³He`, at the SAME `H₉`, pinned weight. -/
def S_He : ℝ := 4.5882788

/-- AME 2020 binding of the triton (MeV) — experimental diagnostic target, never inverted. -/
def B_T : ℝ := 8.4817962

/-- AME 2020 binding of the helion `³He` (MeV) — experimental diagnostic target, never inverted. -/
def B_He : ℝ := 7.7180413

/-- **The mirror-pair cross-inequality** `B_T · S_He ≠ B_He · S_T` — the cross-multiplied form of
`C_knot(T) = B_T/S_T ≠ B_He/S_He = C_knot(³He)`. This is the structural obstruction to any level-only
closure: `T` and `³He` share the strand count `H₉`, so a rescale depending only on the level cannot
reproduce both bindings. Falsifiable (a genuine numerical claim about the measured `(B, S)` pairs),
sorry-free. -/
theorem mirror_cross_ne : B_T * S_He ≠ B_He * S_T := by
  unfold B_T S_He B_He S_T; norm_num

/-- **No level-only rescale closes binding.** If a single scale `g` (`= g(9, q₀) · m_e`, the level-`H₉`
value of any closure `B(K) = g(n_K, q₀) · m_e · S(K)`) reproduced BOTH the triton and the helion
binding from their `S` values, then `B_T · S_He = B_He · S_T`, contradicting `mirror_cross_ne`. Hence
`C_knot` is not a function of `(n, q₀)` — it carries per-knot content. scope-(b) exclusion of the
level-only-rescale closure class. -/
theorem no_level_only_closure : ¬ ∃ g : ℝ, B_T = g * S_T ∧ B_He = g * S_He := by
  rintro ⟨g, hT, hHe⟩
  apply mirror_cross_ne
  rw [hT, hHe]; ring

/-- **The required rescales differ by more than the isospin band.** `C_knot(T)/C_knot(³He) > 1.1`
(measured 1.35), i.e. `B_T · S_He > 1.1 · (B_He · S_T)` — the mismatch a level-only closure would have
to absorb exceeds the ~8% isospin tolerance (ROUTE 5), so the exclusion is not a marginal-precision
artifact. -/
theorem mirror_gap_exceeds_isospin_band : B_T * S_He > 1.1 * (B_He * S_T) := by
  unfold B_T S_He B_He S_T; norm_num

end QOU.MassTheory.CKnotNonUniversal
