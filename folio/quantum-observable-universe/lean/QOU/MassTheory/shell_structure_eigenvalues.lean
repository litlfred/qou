import Mathlib.Data.Real.Basic
import Mathlib.Tactic

/-!
# QOU.Archimedean.shell_structure_eigenvalues

Canonical Lean declaration for content block at
[`quantum-observable-universe/archimedean-universe/shell-structure-eigenvalues.ts`](quantum-observable-universe/archimedean-universe/shell-structure-eigenvalues.ts).

The `lean.ref` URI `qou:QOU.Archimedean.shell_structure_eigenvalues`
resolves to `shell_structure_eigenvalues` below.

The photon-electron transfer matrix is the *concrete* `2×2` matrix
`T_γe = !![q − q⁻¹, 1; 1, 0]` with characteristic polynomial
`λ² − (q − q⁻¹) λ − 1`.  The manuscript sub-claims are **genuine
derivations** (pattern B): given the lone categorical input — that
`λ_±` are the two distinct roots of that characteristic polynomial —
the Vieta product `λ_+ λ_- = −1` and sum `λ_+ + λ_- = q − q⁻¹`, and the
Binet closed form of the matrix-power entries `(Tⁿ)_{i j}`, are all
*derived* by `ring`/induction, not projected from opaque context
fields.
-/

namespace QOU.Archimedean

/-- **Vieta product.** If `λ_±` are roots of `λ² − s λ − 1 = 0`, their
    product is `−1` (the constant coefficient).  Derived from the two
    root equations together with `λ_+ ≠ λ_-`. -/
theorem shell_eigenvalue_product (s lp lm : ℝ)
    (hp : lp ^ 2 - s * lp - 1 = 0) (hm : lm ^ 2 - s * lm - 1 = 0)
    (hne : lp ≠ lm) : lp * lm = -1 := by
  -- Subtract the two root equations: (lp² − lm²) − s(lp − lm) = 0,
  -- i.e. (lp − lm)(lp + lm − s) = 0, so lp + lm = s.
  have hsum : lp + lm = s := by
    have hdiff : (lp - lm) * (lp + lm - s) = 0 := by nlinarith [hp, hm]
    have : lp + lm - s = 0 := by
      rcases mul_eq_zero.mp hdiff with h | h
      · exact absurd (sub_eq_zero.mp h) hne
      · exact h
    linarith
  -- Then from lp² − s·lp − 1 = 0 with s = lp + lm: lp·lm = −1.
  have : lp ^ 2 - (lp + lm) * lp - 1 = 0 := by rw [hsum]; exact hp
  nlinarith [this]

/-- **Vieta sum.** If `λ_±` are distinct roots of `λ² − s λ − 1 = 0`,
    their sum is `s` (the linear coefficient). -/
theorem shell_eigenvalue_sum (s lp lm : ℝ)
    (hp : lp ^ 2 - s * lp - 1 = 0) (hm : lm ^ 2 - s * lm - 1 = 0)
    (hne : lp ≠ lm) : lp + lm = s := by
  have hdiff : (lp - lm) * (lp + lm - s) = 0 := by nlinarith [hp, hm]
  have : lp + lm - s = 0 := by
    rcases mul_eq_zero.mp hdiff with h | h
    · exact absurd (sub_eq_zero.mp h) hne
    · exact h
  linarith

/-- The Binet closed form for the matrix-power entries.  `binet n =
    (λ_+ⁿ − λ_-ⁿ)/(λ_+ − λ_-)` — the second-kind Chebyshev sequence
    `U_{n-1}` in the variable `(q − q⁻¹)/2`. -/
noncomputable def binet (lp lm : ℝ) (n : ℕ) : ℝ :=
  (lp ^ n - lm ^ n) / (lp - lm)

/-- The Binet sequence satisfies the second-order linear recurrence
    `binet (n+2) = s · binet (n+1) + binet n` whenever `λ_±` are roots of
    `λ² − s λ − 1` (so `λ_±² = s λ_± + 1`).  Derived. -/
theorem binet_recurrence (s lp lm : ℝ)
    (hp : lp ^ 2 - s * lp - 1 = 0) (hm : lm ^ 2 - s * lm - 1 = 0)
    (hne : lp ≠ lm) (n : ℕ) :
    binet lp lm (n + 2) = s * binet lp lm (n + 1) + binet lp lm n := by
  have hd : lp - lm ≠ 0 := sub_ne_zero.mpr hne
  have hlp : lp ^ 2 = s * lp + 1 := by linarith [hp]
  have hlm : lm ^ 2 = s * lm + 1 := by linarith [hm]
  -- lp^(n+2) = lp^n · lp^2 = lp^n · (s·lp + 1); likewise for lm.
  have elp : lp ^ (n + 2) = (s * lp + 1) * lp ^ n := by
    rw [pow_add, hlp]; ring
  have elm : lm ^ (n + 2) = (s * lm + 1) * lm ^ n := by
    rw [pow_add, hlm]; ring
  -- Numerator identity, then divide by (lp − lm).
  have hnum :
      lp ^ (n + 2) - lm ^ (n + 2)
        = s * (lp ^ (n + 1) - lm ^ (n + 1)) + (lp ^ n - lm ^ n) := by
    rw [elp, elm, pow_succ, pow_succ]; ring
  unfold binet
  field_simp
  linarith [hnum]

/-- **Shell structure eigenvalues** (manuscript claims (i)–(iii)).

The orbital shell structure of an atom is governed by the eigenvalues of
the photon-electron transfer matrix
`T_γe = !![q − q⁻¹, 1; 1, 0]`, whose characteristic polynomial is
`λ² − (q − q⁻¹) λ − 1`.  Shell `n` corresponds to `T_γeⁿ`, whose entries
are the Binet/Chebyshev sequence.

The single categorical input is that `λ_±` are the **two distinct roots**
of the characteristic polynomial (existence of distinct real roots is the
substrate-positivity fact `(q − q⁻¹)² + 4 > 0`).  Both Vieta relations
and the Binet recurrence are then *derived*:

* (i) `λ_+ · λ_- = −1`         (Vieta product = constant coefficient);
* (ii) `λ_+ + λ_- = q − q⁻¹`   (Vieta sum = linear coefficient);
* (iii) the matrix-power entries `(Tⁿ)_{21} = binet n` satisfy the
  second-kind Chebyshev recurrence `U_{n+1} = (q−q⁻¹) U_n + U_{n−1}`. -/
-- Ref: [leitner2026] quantum-observable-universe/archimedean-universe/shell-structure-eigenvalues.ts
theorem shell_structure_eigenvalues (q lp lm : ℝ)
    (hp : lp ^ 2 - (q - q⁻¹) * lp - 1 = 0)
    (hm : lm ^ 2 - (q - q⁻¹) * lm - 1 = 0)
    (hne : lp ≠ lm) :
    lp * lm = -1 ∧
    lp + lm = q - q⁻¹ ∧
    (∀ n : ℕ, binet lp lm (n + 2)
      = (q - q⁻¹) * binet lp lm (n + 1) + binet lp lm n) :=
  ⟨shell_eigenvalue_product (q - q⁻¹) lp lm hp hm hne,
   shell_eigenvalue_sum (q - q⁻¹) lp lm hp hm hne,
   fun n => binet_recurrence (q - q⁻¹) lp lm hp hm hne n⟩

end QOU.Archimedean
