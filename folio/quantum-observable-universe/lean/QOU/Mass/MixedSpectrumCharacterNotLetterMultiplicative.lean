/-
# A character with mixed σ-spectrum is not letter-multiplicative — so a
# two-row block's log-weight is not a bond functional by any general argument

## Why this file exists

`QOU/Mass/OneRowBlockLetterProduct.lean` (PR #7200, bean `qou-m8f3`) records
why the dominant summand of the partition sum carries no connected many-body
term at `A ≤ 4`: the dominant block is one-row, its character is a ring
homomorphism `H_n(q) → R` with `σ_g ↦ q`, so the character of a word of letters
`c·σ_g + d·1` is the product `∏ (c q + d)` and its logarithm is a sum over
letters — chain-edge additive, exactly.

At ⁶Li the dominant block is the two-row `(15,3)` (bean `qou-vn6h`,
`computations/brng_two_row_dominant_block_a6_probe.py`). A two-row character is
the trace of a representation of dimension `> 1`; on the generator `σ` it has
**both** Hecke eigenvalues, `q` and `−q⁻¹`, each with positive multiplicity
(for `λ = (n−k, k)` with `k ≥ 1` and `n − k ≥ 2`, the standard tableaux with
`1, 2` in the same row and those with `2` in row two are both non-empty). This
file records the structural reason the one-row argument cannot be extended to
it — not merely that it happens not to be, but that **no** scalar `q'` can make
`χ(x·σ) = q'·χ(x)` hold for all `x`:

> If a linear functional `χ` on a ring carrying a Hecke generator
> `σ² = (q − q⁻¹)σ + 1` is right-multiplicative for the letter `σ` with scalar
> `q'`, then `q'` is a root of the Hecke quadratic, i.e. `q' ∈ {q, −q⁻¹}`
> (`quadratic_of_rightLetterMultiplicative`, `root_of_rightLetterMultiplicative`);
> and a functional whose values `χ(1) = d₊ + d₋`, `χ(σ) = d₊ q − d₋ q⁻¹` carry
> both eigenvalues with `d₊ ≠ 0 ≠ d₋` is compatible with neither root
> (`mixedSpectrum_not_rightLetterMultiplicative`). The same holds for any affine
> letter `c·σ + d·1` with `c ≠ 0` (`letter_multiplicative_iff_sigma`).

So for a two-row block the interface contribution to `log|χ^λ|` is not a
per-letter constant **by any general argument**, and whether the block's
log-weight has a connected many-edge term is a question about the specific
word, to be measured — which the probe does, with the one-row block and the
full trace as zero controls. This file does **not** say the connected term is
non-zero; it says the one-row proof does not reach the two-row block, and it
does not touch the bond-rule theorems on the full trace
(`QOU/Mass/MarkovBondRuleForcesPairwise.lean`), which concern `tr_M` and not one
block.

## Base ring (§7c)

`[Field R]`, because `q⁻¹` appears in the Hecke relation and the argument divides
by `c` for a general letter. No ordering, no `ℝ`, no logarithm. The multiplicity
hypotheses are stated as `χ(1) ≠ 0` and `d₊ ≠ 0 ≠ d₋` in `R`; the specialisation
to natural multiplicities needs `CharZero R` and is given as a corollary.
`q + q⁻¹ ≠ 0` (i.e. `q² ≠ −1`) is the one genuine hypothesis and holds for every
real `q`.

-- Ref: [leitner2026] §"Frobenius pairing", per-block characters of `H_n(q)`
-/

import Mathlib.Algebra.Algebra.Defs
import Mathlib.Algebra.Module.LinearMap.Defs
import Mathlib.Tactic.Ring
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.LinearCombination

namespace QOU.Mass.MixedSpectrumCharacterNotLetterMultiplicative

variable {R H : Type*} [Field R] [Ring H] [Algebra R H]

/-- The Hecke relation for a generator `σ` with parameter `q`:
`σ² = (q − q⁻¹) σ + 1` (the convention `(σ − q)(σ + q⁻¹) = 0` of §7a). -/
def HeckeRel (σ : H) (q : R) : Prop := σ * σ = (q - q⁻¹) • σ + 1

/-- `χ` is right-multiplicative for the letter `σ` with scalar `q'`:
`χ(x σ) = q' χ(x)` for every `x`. This is what makes a letter contribute a
fixed factor to the character of any word it is appended to. -/
def RightLetterMultiplicative (χ : H →ₗ[R] R) (σ : H) (q' : R) : Prop :=
  ∀ x : H, χ (x * σ) = q' * χ x

/-- Right-multiplicativity forces the scalar onto the Hecke quadratic:
`(q'² − (q − q⁻¹) q' − 1) · χ(1) = 0`. -/
theorem quadratic_of_rightLetterMultiplicative (χ : H →ₗ[R] R) (σ : H) (q q' : R)
    (hrel : HeckeRel σ q) (hmul : RightLetterMultiplicative χ σ q') :
    (q' * q' - (q - q⁻¹) * q' - 1) * χ 1 = 0 := by
  have hσ : χ σ = q' * χ 1 := by simpa using hmul 1
  have h1 : χ (σ * σ) = q' * (q' * χ 1) := by rw [hmul σ, hσ]
  have h2 : χ (σ * σ) = (q - q⁻¹) * (q' * χ 1) + χ 1 := by
    rw [hrel, map_add, map_smul, smul_eq_mul, hσ]
  have : q' * (q' * χ 1) = (q - q⁻¹) * (q' * χ 1) + χ 1 := h1.symm.trans h2
  linear_combination this

/-- With `χ(1) ≠ 0` the scalar is one of the two Hecke eigenvalues. -/
theorem root_of_rightLetterMultiplicative (χ : H →ₗ[R] R) (σ : H) (q q' : R)
    (hq : q ≠ 0) (h1 : χ 1 ≠ 0)
    (hrel : HeckeRel σ q) (hmul : RightLetterMultiplicative χ σ q') :
    q' = q ∨ q' = -q⁻¹ := by
  have hquad := quadratic_of_rightLetterMultiplicative χ σ q q' hrel hmul
  have hfac : (q' - q) * (q' + q⁻¹) = 0 := by
    have h0 : q' * q' - (q - q⁻¹) * q' - 1 = 0 :=
      (mul_eq_zero.mp hquad).resolve_right h1
    have : (q' - q) * (q' + q⁻¹) = q' * q' - (q - q⁻¹) * q' - 1 := by
      field_simp
      ring
    rw [this, h0]
  rcases mul_eq_zero.mp hfac with h | h
  · left; exact sub_eq_zero.mp h
  · right; exact eq_neg_of_add_eq_zero_left h

/-- **Mixed spectrum excludes letter-multiplicativity.** If `χ(1) = d₊ + d₋`
and `χ(σ) = d₊ q − d₋ q⁻¹` with both multiplicities non-zero (the trace of a
representation in which `σ` has both eigenvalues `q` and `−q⁻¹`), then no
scalar `q'` makes `χ(x σ) = q' χ(x)` for all `x`. -/
theorem mixedSpectrum_not_rightLetterMultiplicative (χ : H →ₗ[R] R) (σ : H)
    (q dp dm : R) (hq : q ≠ 0) (hqq : q + q⁻¹ ≠ 0)
    (hdp : dp ≠ 0) (hdm : dm ≠ 0)
    (hrel : HeckeRel σ q)
    (h1 : χ 1 = dp + dm) (hσ : χ σ = dp * q - dm * q⁻¹) (h1ne : χ 1 ≠ 0) :
    ¬ ∃ q' : R, RightLetterMultiplicative χ σ q' := by
  rintro ⟨q', hmul⟩
  have hσ' : χ σ = q' * χ 1 := by simpa using hmul 1
  rw [h1, hσ] at hσ'
  rcases root_of_rightLetterMultiplicative χ σ q q' hq h1ne hrel hmul with h | h
  · -- q' = q: forces dm (q + q⁻¹) = 0
    rw [h] at hσ'
    have : dm * (q + q⁻¹) = 0 := by linear_combination -hσ'
    rcases mul_eq_zero.mp this with h' | h'
    · exact hdm h'
    · exact hqq h'
  · -- q' = −q⁻¹: forces dp (q + q⁻¹) = 0
    rw [h] at hσ'
    have : dp * (q + q⁻¹) = 0 := by linear_combination hσ'
    rcases mul_eq_zero.mp this with h' | h'
    · exact hdp h'
    · exact hqq h'

/-- Natural multiplicities, characteristic zero: a block in which `σ` has the
eigenvalue `q` with multiplicity `d₊ ≥ 1` and `−q⁻¹` with multiplicity `d₋ ≥ 1`
is not letter-multiplicative. For `λ = (n−k, k)` two-row with `k ≥ 1`,
`n − k ≥ 2`, both multiplicities are positive. -/
theorem twoRow_not_rightLetterMultiplicative [CharZero R] (χ : H →ₗ[R] R) (σ : H)
    (q : R) (dp dm : ℕ) (hq : q ≠ 0) (hqq : q + q⁻¹ ≠ 0)
    (hdp : 0 < dp) (hdm : 0 < dm) (hrel : HeckeRel σ q)
    (h1 : χ 1 = (dp : R) + (dm : R)) (hσ : χ σ = (dp : R) * q - (dm : R) * q⁻¹) :
    ¬ ∃ q' : R, RightLetterMultiplicative χ σ q' := by
  have hdp' : (dp : R) ≠ 0 := Nat.cast_ne_zero.mpr (Nat.pos_iff_ne_zero.mp hdp)
  have hdm' : (dm : R) ≠ 0 := Nat.cast_ne_zero.mpr (Nat.pos_iff_ne_zero.mp hdm)
  have h1ne : χ 1 ≠ 0 := by
    rw [h1]
    exact_mod_cast Nat.pos_iff_ne_zero.mp (Nat.add_pos_left hdp dm)
  exact mixedSpectrum_not_rightLetterMultiplicative χ σ q (dp : R) (dm : R)
    hq hqq hdp' hdm' hrel h1 hσ h1ne

/-- An affine letter `c·σ + d·1` with `c ≠ 0` is right-multiplicative with
scalar `φ` iff `σ` is, with scalar `(φ − d)/c`. So the interface letters of the
atom word (`pp`: `σ`, `nn`: `σ − h`, `pn`: `σ − h(½ − δ/4)`) inherit the
obstruction above verbatim. -/
theorem letter_multiplicative_iff_sigma (χ : H →ₗ[R] R) (σ : H) (c d φ : R) (hc : c ≠ 0) :
    (∀ x : H, χ (x * (c • σ + d • (1 : H))) = φ * χ x) ↔
      RightLetterMultiplicative χ σ ((φ - d) / c) := by
  have key : ∀ x : H, χ (x * (c • σ + d • (1 : H))) = c * χ (x * σ) + d * χ x := by
    intro x
    rw [mul_add, Algebra.mul_smul_comm, Algebra.mul_smul_comm, mul_one, map_add, map_smul,
      map_smul, smul_eq_mul, smul_eq_mul]
  constructor
  · intro h x
    have := (key x).symm.trans (h x)
    field_simp
    linear_combination this
  · intro h x
    rw [key x, h x]
    field_simp
    ring

end QOU.Mass.MixedSpectrumCharacterNotLetterMultiplicative
