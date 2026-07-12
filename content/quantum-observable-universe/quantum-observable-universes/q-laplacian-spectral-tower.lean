import Mathlib.Analysis.SpecialFunctions.Complex.Circle
import Mathlib.Analysis.SpecialFunctions.Complex.Log

/-!
# The q-Laplacian spectral tower and its root-of-unity truncation

The q-Laplacian `Δ_q = d_q δ_q + δ_q d_q`
([`def:q-harmonic-form`](q-harmonic-form.md)) has eigenvalues given by
the **q-integer tower** `[k]_q²`, where
`[k]_q = (q^k − q^{−k})/(q − q^{−1})`. This single tower is the shared
spectral engine of the q-heat equation (`∂_t u = −Δ_q u`, mode decay
`e^{−[k]_q² t}`), the q-Navier–Stokes system, and the Wenzl / Gram-
matrix block dimensions.

This file formalises the **root-of-unity truncation**: at the primitive
root of unity `q = exp(iπ/r)`, the q-integer `[r]_q` vanishes. By the
Verlinde / Reshetikhin–Turaev mechanism this truncates the
representation category — and hence the q-Laplacian spectrum — to the
finite set `{[1]_q², …, [r−1]_q²}`, exact in the cyclotomic field.

This is a **fibre-level** statement: `q` is a formal/complex variable
with `Im(q)` unconstrained (the operative structure is the root of
unity / bar involution, not a reality assumption — cf. AGENTS.md
"Im(q) at fibre vs observable level"). It is stated over `ℂ` because
the root of unity `exp(iπ/r)` is genuinely complex.

The vanishing `[r]_q = 0` is the numerator identity
`q^r − q^{−r} = 0`, i.e. `q^{2r} = 1`: at `q = exp(iπ/r)` we have
`q^r = exp(iπ) = −1`, so `q^{2r} = 1` and the numerator
`q^r − q^{−r} = (−1) − (−1) = 0`.

-- Ref: [verlinde1988] https://doi.org/10.1016/0550-3213(88)90603-7
-- Ref: [reshetikhin1991] https://doi.org/10.1007/BF01239527
-/


namespace QOU.QuantumObservableUniverses

open Complex

/-- The primitive root of unity `ζ_r = exp(iπ/r)` at which the
representation category truncates at level `r`. -/
noncomputable def truncRoot (r : ℕ) : ℂ := Complex.exp (Real.pi * I / r)

/-- `ζ_r ^ r = −1` (so `ζ_r ^ (2r) = 1`): the r-th power of the
truncation root is `exp(iπ) = −1`. -/
theorem truncRoot_pow (r : ℕ) (hr : r ≠ 0) :
    (truncRoot r) ^ r = -1 := by
  unfold truncRoot
  rw [← Complex.exp_nat_mul]
  have hr_ne : (r : ℂ) ≠ 0 := Nat.cast_ne_zero.mpr hr
  have : (r : ℂ) * (Real.pi * I / r) = Real.pi * I := by
    field_simp
  rw [this, Complex.exp_pi_mul_I]

/-- **Root-of-unity truncation.** The unnormalised q-integer numerator
`q^r − q^{−r}` vanishes at `q = ζ_r = exp(iπ/r)`. Since
`ζ_r ^ r = −1` and `ζ_r ^ {−r} = (−1)^{−1} = −1`, the numerator is
`(−1) − (−1) = 0`. This is the level-`r` Verlinde / WRT truncation that
collapses the infinite q-Laplacian spectrum to a finite, exact set. -/
theorem qIntegerNumerator_vanishes_at_truncRoot (r : ℕ) (hr : r ≠ 0) :
    (truncRoot r) ^ r - (truncRoot r)⁻¹ ^ r = 0 := by
  have hpow : (truncRoot r) ^ r = -1 := truncRoot_pow r hr
  have hinv : (truncRoot r)⁻¹ ^ r = -1 := by
    rw [inv_pow, hpow]; norm_num
  rw [hpow, hinv]; ring

end QOU.QuantumObservableUniverses
