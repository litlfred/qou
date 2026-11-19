import QOU.Nuclear.BraneTowerExponentialDecayAndCPTClosure

/-!
# `prop:archimedean-remainder-exponential-decay` — Exponential Decay of Brane-Tower & Spectral Remainders

Companion Lean module for `prop:archimedean-remainder-exponential-decay`, re-exporting the
exponential-decay predicate `ArchimedeanRemainderExponentialDecay` and proving its unconditional
satisfaction for both the scaled quadratic Hecke brane-tower remainder and any geometrically
majorized spectral/ladder series via `QOU.Nuclear.BraneTowerExponentialDecayAndCPTClosure`.
-/

namespace QOU.Interactions

open QOU.Nuclear.BraneTowerExponentialDecayAndCPTClosure

-- Ref: [jones1985] doi:10.2307/1971403
-- Ref: [leitner2026] prop:archimedean-remainder-exponential-decay
/-- Exponential-decay control predicate on a truncation remainder sequence `remainder : ℕ → ℝ`:
there exist strictly positive constants `C, c > 0` such that
`|remainder N| ≤ C · exp(-c · N)` for every truncation depth `N : ℕ`. -/
class ArchimedeanRemainderExponentialDecay (remainder : ℕ → ℝ) : Prop where
  exp_decay_bound :
    ∃ C c : ℝ, 0 < C ∧ 0 < c ∧
      ∀ N : ℕ, |remainder N| ≤ C * Real.exp (-c * (N : ℝ))

/-- Unconditional discharge of `ArchimedeanRemainderExponentialDecay` for the scaled quadratic
Hecke brane-tower truncation remainder at any real deformation parameter `1 < q` and positive
energy scale `0 < scale`. -/
theorem archimedeanRemainderExponentialDecay_braneTower {q scale : ℝ}
    (hq : 1 < q) (hscale : 0 < scale) :
    ArchimedeanRemainderExponentialDecay
      (fun N => scale * (braneTowerPartialSum q N - braneTowerExactLimit q)) :=
  ⟨braneTower_exists_exp_decay_bound hq hscale⟩

/-- Unconditional discharge of `ArchimedeanRemainderExponentialDecay` for the tail remainder
`seriesTailRemainder a` of any geometrically majorized spectral or Habiro–Bürmann series
(`|a k| ≤ M · r^k`, `0 < M`, `0 < r < 1`). -/
theorem archimedeanRemainderExponentialDecay_geom_majorant {a : ℕ → ℝ} {M r : ℝ}
    (hM : 0 < M) (hr0 : 0 < r) (hr1 : r < 1) (ha : ∀ k : ℕ, |a k| ≤ M * r ^ k) :
    ArchimedeanRemainderExponentialDecay (seriesTailRemainder a) :=
  ⟨exists_exp_decay_of_geom_majorant hM hr0 hr1 ha⟩

end QOU.Interactions
