import Mathlib.RingTheory.RootsOfUnity.Basic
import Mathlib.RingTheory.Polynomial.Cyclotomic.Basic
import QOU.MathlibExt.QIntegerCanonical

/-!
# Level-2 SU(2) Verlinde witness at a primitive 8th root of unity

Three algebraic facts that together identify the categorical witness
of the universal `Φ_8(u) = u^4 + 1` factor in atomic-step Habiro
elements:

1. The q-Pochhammer `(ζ; ζ)_7 = 8` evaluates to an integer at a
   primitive 8th root of unity.
2. The Hecke generator `σ_i` has order 8 in `H_n(q)` at `q = ζ`,
   matching `M_first_Φ_8 = 7 = ord(σ_i) − 1` observed empirically.
3. The quantum integer `[4]_q = 0` at `q = ζ` — first vanishing
   quantum integer; Wenzl projector kernel kicks in at partition
   first-column length ≥ `k + 2 = 4` for level `k = 2` SU(2).

These three identities, together with the WZW correspondence
`q = e^(iπ/(k+2)) ⇒ k = 2`, witness the level-2 SU(2) Verlinde
truncation that produces the universal `Φ_8²` factor via
Wenzl-annihilator-forced Δa_m interference.

**Base ring (§7c).** None of the three facts is analytic: each is a
purely algebraic property of a *primitive 8th root of unity*. The
witness is therefore stated over a generic field `R` with a parameter
`ζ : R` and the hypothesis `IsPrimitiveRoot ζ 8`, rather than pinning
the analytic model `ζ_8 = e^(iπ/4) ∈ ℂ`. Any field carrying a
primitive 8th root (in particular the cyclotomic/Hecke settings where
the witness is consumed) instantiates it.

## References

-- Ref: [wenzl1987] Hans Wenzl, "On the structure of Brauer's centralizer
--      algebras", Annals of Math. 128 (1988), 173-193.
-- Ref: [washington1997] Lawrence Washington, "Introduction to
--      Cyclotomic Fields", Springer GTM 83, 1997. Chapter 2.
-- Ref: [jones1987] Vaughan Jones, "Hecke algebra representations of
--      braid groups and link polynomials", Annals of Math. 126 (1987),
--      335-388.
-- Ref: [witten1989] Edward Witten, "Quantum field theory and the Jones
--      polynomial", Comm. Math. Phys. 121 (1989), 351-399.
-/

namespace QOU.BraidKnot.Zeta8Witness

open scoped Classical

variable {R : Type*} [Field R] {ζ : R}

/-- The q-Pochhammer symbol `(q; q)_m = Π_{k=1..m} (1 − q^k)`. -/
def qPoch (q : R) : ℕ → R
  | 0 => 1
  | (m + 1) => qPoch q m * (1 - q ^ (m + 1))

/-- **Identity (1): `(ζ; ζ)_7 = 8`**.

    The q-Pochhammer at a primitive 8th root of unity, truncated at
    `m = 7 = ord(ζ) − 1`, evaluates to the integer `8 = ord(ζ)`.

    Algebraic derivation: from `X^8 − 1 = ∏_{k=0}^{7}(X − ζ^k)`,
    dividing by `(X − 1)` gives `X^7 + ⋯ + 1 = ∏_{k=1}^{7}(X − ζ^k)`.
    Evaluating at `X = 1`: LHS = `8`, RHS = `∏_{k=1}^{7}(1 − ζ^k) = (ζ; ζ)_7`. -/
theorem qPoch_seven_eq_eight (hζ : IsPrimitiveRoot ζ 8) : qPoch ζ 7 = (8 : R) := by
  -- Ref: [washington1997] §2.1, Theorem 2.1 (cyclotomic evaluations at
  -- roots of unity): ∏_{k=1}^{n−1}(1 − ζ^k) = n for ζ a primitive
  -- n-th root. The hypothesis `hζ` pins `n = 8`.
  -- Concrete n = 8 route: `ζ^4 = -1` (primitive 2nd root) collapses the
  -- seven-factor product to `8`. The `linear_combination` coefficient is
  -- the exact quotient `(∏_{k=1}^{7}(1 - X^k) - 8) / (X^4 + 1)`.
  have h8 : ζ ^ 8 = 1 := hζ.pow_eq_one
  have hne : ζ ^ 4 ≠ 1 := hζ.pow_ne_one_of_pos_of_lt (by norm_num) (by norm_num)
  have h4 : ζ ^ 4 = -1 := by
    have hsq : (ζ ^ 4 - 1) * (ζ ^ 4 + 1) = 0 := by
      have h2 : (ζ ^ 4) ^ 2 = 1 := by rw [← pow_mul]; norm_num; exact h8
      linear_combination h2
    rcases mul_eq_zero.mp hsq with h | h
    · exact absurd (by linear_combination h) hne
    · linear_combination h
  have expand : qPoch ζ 7
      = (1-ζ^1)*(1-ζ^2)*(1-ζ^3)*(1-ζ^4)*(1-ζ^5)*(1-ζ^6)*(1-ζ^7) := by
    simp only [qPoch]; ring
  rw [expand]
  linear_combination (-ζ^24 + ζ^23 + ζ^22 + ζ^20 - 2*ζ^19 - ζ^18 - ζ^17 - 2*ζ^16
    + 2*ζ^15 + 2*ζ^14 + 2*ζ^13 + 4*ζ^12 - 2*ζ^11 - 2*ζ^10 - 2*ζ^9 - 6*ζ^8
    + ζ^7 + ζ^6 + 2*ζ^5 + 7*ζ^4 - ζ^2 - ζ - 7) * h4

/-- **Identity (2): `σ_i` has order 8 at `q = ζ`**.

    Direct consequence of primitivity: `ζ^k ≠ 1` for `0 < k < 8`. The
    Hecke eigenvalues `ζ` and `−ζ⁻¹ = ζ³` both have order 8, so
    `ord(σ_i) = lcm(8, 8) = 8`, matching the empirical
    `M_first_Φ_8 = 7 = ord − 1` boundary. -/
theorem zeta_pow_ne_one (hζ : IsPrimitiveRoot ζ 8) (k : ℕ) (hk_pos : 0 < k)
    (hk_lt : k < 8) : ζ ^ k ≠ 1 :=
  hζ.pow_ne_one_of_pos_of_lt hk_pos.ne' hk_lt

/-- The Hecke quadratic relation eigenvalue split over a field (an
    integral domain): if `(σ − ζ)(σ + ζ⁻¹) = 0` then `σ = ζ` or
    `σ = −ζ⁻¹`. -/
theorem hecke_eigenvalues (σ : R) (h : (σ - ζ) * (σ + ζ⁻¹) = 0) :
    σ = ζ ∨ σ = -ζ⁻¹ := by
  rcases mul_eq_zero.mp h with h1 | h2
  · left; linear_combination h1
  · right; linear_combination h2

/-- The quantum integer `[n]_q = (q^n − q^(−n)) / (q − q^(−1))`. -/
noncomputable def qInt (q : R) (n : ℕ) : R :=
  if q = q⁻¹ then (n : R) else (q ^ n - q ^ (-(n : ℤ))) / (q - q⁻¹)

/-- **Bridge to the canonical singular-locus-guarded bracket.**

The guard here is written `q = q⁻¹`, which is the same locus as
`q − q⁻¹ = 0` (`sub_eq_zero`) — so this is the two-sided `qIntBalClSing`, not
the one-sided `qIntBalCl`.  That matters in this file specifically: the roots of
unity it works with sit exactly where the balanced denominator degenerates, so
which guard is in force is not a formality here. -/
theorem qInt_eq_canonical (q : R) (n : ℕ) :
    qInt q n = QOU.QInteger.qIntBalClSing q n := by
  unfold qInt QOU.QInteger.qIntBalClSing
  rw [← sub_eq_zero (a := q) (b := q⁻¹)]
  split_ifs with h
  · rfl
  · simp [QOU.QInteger.qIntBal, QOU.Mass.QHookDimensionBalanced.qIntBal, zpow_neg,
      zpow_natCast, inv_pow]

/-- **Identity (3): `[4]_q = 0` at `q = ζ`** (first vanishing quantum
    integer).

    Since `ζ^4` is a primitive 2nd root of unity, `ζ^4 = −1 = ζ^(−4)`,
    consequently the numerator `q^4 - q^(-4)` vanishes while the denominator is
    nonzero. The vanishing `[4]_q = 0` is the Wenzl projector boundary
    for the level-`k = 2` SU(2) Verlinde truncation. -/
theorem qInt_four_eq_zero (hζ : IsPrimitiveRoot ζ 8) : qInt ζ 4 = 0 := by
  -- Ref: [wenzl1987] §3 (Wenzl projectors and quantum dimensions).
  -- Ref: [witten1989] §4 (level-k SU(2) Verlinde truncation).
  -- Key algebraic step: ζ^4 = -1 (primitive 2nd root), numerator vanishes.
  have h8 : ζ ^ 8 = 1 := hζ.pow_eq_one
  have hne4 : ζ ^ 4 ≠ 1 := hζ.pow_ne_one_of_pos_of_lt (by norm_num) (by norm_num)
  have h4 : ζ ^ 4 = -1 := by
    have hsq : (ζ ^ 4 - 1) * (ζ ^ 4 + 1) = 0 := by
      have h2 : (ζ ^ 4) ^ 2 = 1 := by rw [← pow_mul]; norm_num [h8]
      linear_combination h2
    rcases mul_eq_zero.mp hsq with h | h
    · exact absurd (by linear_combination h) hne4
    · linear_combination h
  -- ζ ≠ ζ⁻¹ (else ζ² = 1, contradicting order 8)
  have hne2 : ζ ^ 2 ≠ 1 := hζ.pow_ne_one_of_pos_of_lt (by norm_num) (by norm_num)
  have hζ0 : ζ ≠ 0 := hζ.ne_zero (by norm_num)
  have hnei : ζ ≠ ζ⁻¹ := by
    intro he
    apply hne2
    field_simp [hζ0] at he
    linear_combination he
  unfold qInt
  -- `ζ ≠ ζ⁻¹` so we take the else-branch; numerator `ζ⁴ − ζ⁻⁴ = -1 − (-1) = 0`.
  rw [if_neg hnei, zpow_neg, zpow_natCast, h4]
  norm_num

/-- **The Wenzl truncation boundary is reached at first-column length
    `≥ 4`**: some quantum integer at or below that length vanishes at
    `q = ζ`.

    This is the part of the level-2 SU(2) Verlinde statement this file
    can actually support, and it follows from its own
    `qInt_four_eq_zero`.

    **Still open, and deliberately not claimed here.** The full
    statement — that for any partition `λ` with first-column length
    `≥ 4` the Hecke character `χ^λ` has zero quantum trace at `q = ζ`,
    the categorical content of the universal `Φ_8` cancellation at
    `M = 7` — needs the Wenzl projector machinery, which is not in
    Mathlib and not in this corpus. There is no `χ^λ` in scope to state
    it about.

    **2026-08-21 (bean `qou/q407`).** The previous version was

    ```lean
    theorem wenzl_annihilator (_n : ℕ) (firstCol : ℕ) (_h : 4 ≤ firstCol) :
        ∃ chi_lambda_at_zeta : R, chi_lambda_at_zeta = 0 := ⟨0, rfl⟩
    ```

    which says a field has a zero. `firstCol` and `_h` were unused, so it
    held at first-column length 1 exactly as at 4, and it carried the
    three citations below while proving nothing any of them says. The
    docstring's "stated as a structural target" was accurate about the
    intent and did not stop the declaration from reading as proved to
    every consumer and every gate. -/
-- Ref: [wenzl1987] §3 Theorem 3.1; [jones1987] §5; [witten1989] §4.
theorem wenzl_annihilator (hζ : IsPrimitiveRoot ζ 8)
    (firstCol : ℕ) (h : 4 ≤ firstCol) :
    ∃ j ≤ firstCol, qInt ζ j = 0 :=
  ⟨4, h, qInt_four_eq_zero hζ⟩

end QOU.BraidKnot.Zeta8Witness
