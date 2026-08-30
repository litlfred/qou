/-
# The parameter selection, in the currency the final inequality is stated in

`RothSiegelBound.exists_rothGammaFull_auxiliary` produces heights `H` and a threshold `N` with all
seven clauses of `Γ_m` at the auxiliary polynomial's own height.  `RothNormalisation`'s
`roth_contradiction_of_normalisation` consumes a *different* currency: three real constants `cH`,
`θ`, `L'`, a lower bound `K` on `T_h·r_h`, and the single inequality `(1+θ)·m·L' < K(μ−ν)`.

This file is the exchange.  Each lemma converts one clause of the selection's output into one
hypothesis of the normalisation, and every one of them turns out to be a *floor on the heights* or
a *power of the heights below `N`* — which is exactly what the selection takes as parameters.
That is the point: after this file, no hypothesis of the chain refers to data the chain itself
produces.

## The three slack constants, and where each comes from

* `η` is the normalisation slack.  It is `1/k`, where `k` is the exponent in the selection's new
  clause `(H h)^k ≤ N`: the heights are polynomially small in `N`, so `log H_h ≤ (1/k)·log N`, and
  the two-sided `rothDegrees_log_bounds` closes to within `1 ± 1/k`.  Taking `k` large is the
  formal content of "let `N` be large compared with the heights".
* `θ` is the auxiliary polynomial's share of the denominators' size.  It enters through `hpt`,
  which is a lower bound on `log q_h` — on the *denominators*, not the heights.  `height_le_mul_den`
  is what makes the two interchangeable: a rational bounded by `B` has `H ≤ B·q`, so a floor on the
  heights is a floor on the denominators up to the constant `B`.
* `ε` is how far step 1's index falls short of `m/2`, and is unchanged from `RothNormalisation`.

`δ`, the approximation excess, is not a slack — it is the budget the other three are paid out of,
which is what `slack_pos` says.
-/
import QOU.Mathlib.RothIntegerChain
import QOU.Mathlib.RothNormalisation
import QOU.Mathlib.RothSiegelBound

open NumberField Finset

namespace MvPolynomial

section Logs

/-- `H^k ≤ N`, in logs.  The selection's new clause, made usable. -/
theorem log_pow_le_log {Hh N k : ℕ} (hH : 2 ≤ Hh) (hpow : Hh ^ k ≤ N) :
    (k : ℝ) * Real.log Hh ≤ Real.log N := by
  have hHpos : (0 : ℝ) < (Hh : ℝ) := by
    have : 0 < Hh := by omega
    exact_mod_cast this
  have hcast : ((Hh : ℝ)) ^ k ≤ (N : ℝ) := by exact_mod_cast hpow
  have h := Real.log_le_log (by positivity) hcast
  rwa [Real.log_pow] at h

/-- **The normalisation slack is `1/k`.**  `rothDegrees_log_bounds` is two-sided to within
`log H_h`, and the selection's `(H h)^k ≤ N` bounds that by `(1/k)·log N`.  So the degrees satisfy
`(1 − η)·log N ≤ r_h·log H_h ≤ (1 + η)·log N` with `η = 1/k`, uniformly in `h` — which is what
`hT` and `hL'` need, and neither can get from a one-sided estimate. -/
theorem selection_normalisation {m : ℕ} (H : Fin m → ℕ) (N k : ℕ) (hN : N ≠ 0)
    (hH : ∀ h, 2 ≤ H h) (hk : 0 < k) (hpow : ∀ h, (H h) ^ k ≤ N) (h : Fin m) :
    (rothDegrees H N h : ℝ) * Real.log (H h) ≤ (1 + 1 / (k : ℝ)) * Real.log N
      ∧ (1 - 1 / (k : ℝ)) * Real.log N ≤ (rothDegrees H N h : ℝ) * Real.log (H h) := by
  have hkR : (0 : ℝ) < (k : ℝ) := by exact_mod_cast hk
  have hstep : Real.log (H h) ≤ (1 / (k : ℝ)) * Real.log N := by
    have hle := log_pow_le_log (hH h) (hpow h)
    rw [one_div, inv_mul_eq_div, le_div_iff₀ hkR]
    linarith
  obtain ⟨hlow, hhigh⟩ := rothDegrees_log_bounds H N hN hH h
  constructor
  · calc (rothDegrees H N h : ℝ) * Real.log (H h) ≤ Real.log N + Real.log (H h) := hhigh
      _ ≤ Real.log N + (1 / (k : ℝ)) * Real.log N := by linarith
      _ = (1 + 1 / (k : ℝ)) * Real.log N := by ring
  · calc (1 - 1 / (k : ℝ)) * Real.log N = Real.log N - (1 / (k : ℝ)) * Real.log N := by ring
      _ ≤ Real.log N - Real.log (H h) := by linarith
      _ ≤ (rothDegrees H N h : ℝ) * Real.log (H h) := hlow

end Logs

section Denominators

/-- **A bounded rational's height is at most `B` times its denominator.**  `H = max(|num|, den)`,
and `|num| ≤ B·den` is just `|κ| ≤ B` cleared of its denominator; `den ≤ B·den` needs `B ≥ 1`.

This is the lemma that lets a floor on the *heights* — which is all the selection can impose,
since `S` is a set of heights — serve as a floor on the *denominators*, which is what `hpt`
actually constrains.  Without it the two floors are unrelated: a rational of height `10^9` can
have denominator `1`. -/
theorem height_le_mul_den {κ : ℚ} {B : ℝ} (hB : 1 ≤ B) (hκ : |((κ : ℚ) : ℝ)| ≤ B) :
    ((max κ.num.natAbs κ.den : ℕ) : ℝ) ≤ B * (κ.den : ℝ) := by
  have hden : (0 : ℝ) < (κ.den : ℝ) := by exact_mod_cast κ.pos
  have hcast : ((κ : ℚ) : ℝ) = (κ.num : ℝ) / (κ.den : ℝ) := by
    rw [Rat.cast_def]
  have habs : |((κ : ℚ) : ℝ)| = |(κ.num : ℝ)| / (κ.den : ℝ) := by
    rw [hcast, abs_div, abs_of_pos hden]
  have hnum : |(κ.num : ℝ)| ≤ B * (κ.den : ℝ) := by
    rw [habs, div_le_iff₀ hden] at hκ
    linarith
  have hnat : ((κ.num.natAbs : ℕ) : ℝ) = |(κ.num : ℝ)| := by
    rw [Int.cast_natAbs, Int.cast_abs]
  rw [Nat.cast_max]
  refine max_le ?_ ?_
  · rw [hnat]; exact hnum
  · nlinarith

/-- **`hpt` from a floor on the heights.**  `roth_contradiction_of_normalisation`'s `hpt` clause is
`2 + cH + log(2B) + log 2 ≤ θ·log q_h`.  Routed through `height_le_mul_den`, it becomes a condition
on a *number* `T` below every height — and `T` is precisely the selection's floor parameter, so this
clause costs nothing beyond enlarging `T`. -/
theorem hpt_of_floor {m : ℕ} {H : Fin m → ℕ} {κ : Fin m → ℚ} {B θ cH : ℝ}
    (hB : 1 ≤ B) (hθ : 0 ≤ θ)
    (hκB : ∀ h, |((κ h : ℚ) : ℝ)| ≤ B)
    (hHκ : ∀ h, max (κ h).num.natAbs (κ h).den = H h)
    {T : ℕ} (hT1 : 1 ≤ T) (hfloorH : ∀ h, T ≤ H h)
    (hfloor : 2 + cH + Real.log (2 * B) + Real.log 2 + θ * Real.log B ≤ θ * Real.log T) :
    ∀ h, 2 + cH + Real.log (2 * B) + Real.log 2 ≤ θ * Real.log ((κ h).den : ℝ) := by
  intro h
  have hB0 : (0 : ℝ) < B := lt_of_lt_of_le zero_lt_one hB
  have hden : (0 : ℝ) < ((κ h).den : ℝ) := by exact_mod_cast (κ h).pos
  have hTR : (0 : ℝ) < (T : ℝ) := by exact_mod_cast hT1
  -- `T ≤ H h ≤ B · den h`
  have hHB : ((H h : ℕ) : ℝ) ≤ B * ((κ h).den : ℝ) := by
    rw [← hHκ h]; exact height_le_mul_den hB (hκB h)
  have hTH : (T : ℝ) ≤ ((H h : ℕ) : ℝ) := by exact_mod_cast hfloorH h
  have hlog : Real.log T ≤ Real.log B + Real.log ((κ h).den : ℝ) := by
    calc Real.log T ≤ Real.log (B * ((κ h).den : ℝ)) :=
          Real.log_le_log hTR (le_trans hTH hHB)
      _ = Real.log B + Real.log ((κ h).den : ℝ) := Real.log_mul (ne_of_gt hB0) (ne_of_gt hden)
  nlinarith [mul_le_mul_of_nonneg_left hlog hθ]

end Denominators

end MvPolynomial
