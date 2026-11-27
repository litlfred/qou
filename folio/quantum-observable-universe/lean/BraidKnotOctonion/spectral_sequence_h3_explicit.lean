import Mathlib.GroupTheory.Perm.Fin
import Mathlib.Data.Fintype.Perm
import Mathlib.Algebra.Algebra.Basic
import Mathlib.LinearAlgebra.Matrix.Trace
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Abel
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.FinCases

/-!
# QOU.BraidKnot.spectral_sequence_h3_explicit — conjecture carrier

Content block
[`conj:spectral-sequence-h3-explicit`](../../../quantum-observable-universe/mass-theory/spectral-sequence-h3-explicit.md).

**Conjecture, not a proposition (owner, 2026-11-20, bean `qou-6qbv`).** The
block claims explicit formulas for the differentials `d₁`, `d₂` of the
GB-filtered Hochschild spectral sequence on `H₃(R, q)` and the resulting
`E_∞` page identifications.

## What changed

Until 2026-11-20 a `def` projected the three claims out of a context class that
also carried free fields `Z`, `N`, `n_strands` and the bare equation
`n_strands = 3`. The projection is gone. The three claims stay as `Prop`
parameters of the carrier `SpectralSequenceH3Explicit`, because their encoding
is an author decision this file deliberately does not make (a `d₁ ∘ d₁ = 0`
encoding is true of every differential and is not the claim). No instance is
supplied: that is the open state.

## What is proved

`e1_ranks_h3`: the `E₁` page the block describes has ranks `1, 2, 2, 1`. The
filtration is by Coxeter length on the standard basis `{T_w : w ∈ S₃}` of
`H₃(q)`, and `ℓ(w)` is the inversion count of `w`; the ranks are the numbers
of permutations of three letters with `0, 1, 2, 3` inversions. This is the one
numerical claim in the block that does not depend on the open differentials.

**Caveat (2026-11-20, bean `qou-6qbv`).** These are the ranks of `gr H₃(q)` under the
length filtration, which is what the block describes. They are **not** the `E₁` page of
the Hochschild spectral sequence that `prop:gb-spectral-sequence`'s proof actually
builds: that sequence lives on `Hom(H₃^{⊗k}, H₃)` and abuts to `HH*(H₃)`, which at
generic `q` is the centre `Z(H₃)`, of dimension 3 (one per partition of 3), not 6.
The block's statement (`E_∞ ⇒ gr H_n`) and its proof (`E_∞ ≅ gr HH*`) name different
abutments, and the confinement filtration `J^•` is defined as increasing while the
proof uses it as decreasing. See `QOU.BraidKnot.GBRewriteDifferential`.
-/

namespace QOU.BraidKnot

open Equiv

/-- **Conjecture (explicit spectral sequence on `H₃`).** `d1Explicit`,
`d2Explicit`, `pagesConcretised` are the block's three sub-claims; the carrier
holds exactly when all three do. -/
-- Ref: [leitner2026] quantum-observable-universe/mass-theory/spectral-sequence-h3-explicit
class SpectralSequenceH3Explicit
    (d1Explicit d2Explicit pagesConcretised : Prop) : Prop where
  /-- (i) the explicit `d₁`-differential. -/
  d1 : d1Explicit
  /-- (ii) the explicit `d₂`-differential. -/
  d2 : d2Explicit
  /-- (iii) the `E_∞` page identifications on `H₃(R, q)`. -/
  pages : pagesConcretised

/-- Inversion count of a permutation, which is its Coxeter length in `Sₙ`. -/
def inversionCount {n : ℕ} (σ : Perm (Fin n)) : ℕ :=
  (Finset.univ.filter fun p : Fin n × Fin n => p.1 < p.2 ∧ σ p.2 < σ p.1).card

/-- **The `E₁` ranks.** The standard basis of `H₃(q)` graded by Coxeter length
has ranks `1, 2, 2, 1` in lengths `0, 1, 2, 3`. -/
-- Ref: [leitner2026] quantum-observable-universe/mass-theory/spectral-sequence-h3-explicit
theorem e1_ranks_h3 :
    (List.range 4).map (fun k =>
      (Finset.univ.filter fun σ : Perm (Fin 3) => inversionCount σ = k).card)
      = [1, 2, 2, 1] := by
  decide

/-! ## The explicit pages, on the cocentre (2026-11-27, group B of the mass-conjecture survey)

The block's own sentence `E_∞ ⇒ gr H_n` and its proof's `E_∞ ≅ gr HH*` name two
different abutments (caveat above). A trace — and the `α_k` are traces — factors
through the **cocentre** `HH₀(H₃) = H₃ / [H₃, H₃]`, not through `HH⁰ = Z(H₃)`. Filter
`H₃` by Coxeter length and pass to the cocentre. That gives a precise version of the
block, and it is proved here over a generic ring:

* `E₁` is `gr H₃`, ranks `1, 2, 2, 1` (`e1_ranks_h3`).
* **`d` in degree 1** kills `[σ₁] − [σ₂]`, which is a sum of commutators
  (`h3_diff_eq_commutators`). So the class `[σ₁ − σ₂]` of the proof sketch is
  **zero** in `HH₀`: `α₁ = 0` holds for **every** trace, Markov or not
  (`h3_trace_sigma_diff`), not only by `z − z = 0`.
* **`d` in degree 2** kills `[σ₁σ₂] − [σ₂σ₁]`, itself a commutator.
* **`d` in degree 3** sends the top class `[σ₁σ₂σ₁]` down to filtration 2:
  `σ₁σ₂σ₁ ≡ a·σ₁σ₂ + b·σ₁` modulo commutators (`h3_trace_longest`).
* `E_∞` therefore has ranks `1, 1, 1, 0` (`einf_ranks_h3`), spanned by the
  minimal-length class representatives `1, σ₁, σ₁σ₂` (`h3_trace_standard_basis`).
  These three classes are **independent** at generic `q`: the trivial, sign and
  reflection characters separate them with determinant `(Q+1)(Q²+Q+1)`
  (`h3_cocentre_independent`), so `rank HH₀(H₃) = 3 = #{λ ⊢ 3}`.

This settles the two consistency questions recorded in
`mass-theory/explicit-alpha-k-h3.lean`: the sketch's "four surviving classes" are
three, because `[σ₁σ₂σ₁]` is not a new class; and `σ₁ − σ₂` need not be central,
because the trace pairing lives on `HH₀`, where `σ₁ − σ₂` is `0`. The value
`α₃ = tr(σ₁σ₂σ₁) = h z² + z` is unchanged, and is now *forced* by `α₁`, `α₂`:
`α₃ = h·α₂ + tr σ₁`.

The quadratic relation is taken in the general form `s² = a·s + b`, which covers
both normalisations: `σ² = hσ + 1` (`a = h`, `b = 1`) and `T² = (Q−1)T + Q`.
No value of `q` and no numerics are used.

-- Ref: [geckpfeiffer2000] §8.2 (cocentre of Iwahori–Hecke algebras; minimal-length
--      class representatives)
-/

section Cocentre

variable {R : Type*} [CommRing R] {A : Type*} [Ring A] [Algebra R A]

/-- **`σ₁ − σ₂` is a sum of commutators** (times `b`). For `s² = a s + b` and the
braid relation: `b (s₁ − s₂) = [s₁, s₂s₁] − [s₂, s₁s₂] − a [s₁, s₂]`. -/
theorem h3_diff_eq_commutators (a b : R) (s₁ s₂ : A)
    (hq₁ : s₁ * s₁ = a • s₁ + b • 1) (hq₂ : s₂ * s₂ = a • s₂ + b • 1)
    (braid : s₁ * s₂ * s₁ = s₂ * s₁ * s₂) :
    b • (s₁ - s₂) = (s₁ * (s₂ * s₁) - s₂ * s₁ * s₁) - (s₂ * (s₁ * s₂) - s₁ * s₂ * s₂)
      - a • (s₁ * s₂ - s₂ * s₁) := by
  have e1 : s₂ * s₁ * s₁ = a • (s₂ * s₁) + b • s₂ := by
    rw [mul_assoc, hq₁, mul_add, mul_smul_comm, mul_smul_comm, mul_one]
  have e2 : s₁ * s₂ * s₂ = a • (s₁ * s₂) + b • s₁ := by
    rw [mul_assoc, hq₂, mul_add, mul_smul_comm, mul_smul_comm, mul_one]
  rw [e1, e2, ← mul_assoc, ← mul_assoc, ← braid, smul_sub, smul_sub]
  abel

/-- **`α₁ = 0` for every trace.** Any `R`-linear `τ` with `τ(xy) = τ(yx)` gives
`b·τ(σ₁ − σ₂) = 0`; with `b` a unit (here `b = 1` or `b = Q = q²`), `τ σ₁ = τ σ₂`. -/
theorem h3_trace_sigma_diff (a b : R) (s₁ s₂ : A) (τ : A →ₗ[R] R)
    (hτ : ∀ x y : A, τ (x * y) = τ (y * x))
    (hq₁ : s₁ * s₁ = a • s₁ + b • 1) (hq₂ : s₂ * s₂ = a • s₂ + b • 1)
    (braid : s₁ * s₂ * s₁ = s₂ * s₁ * s₂) :
    b * τ (s₁ - s₂) = 0 := by
  rw [← smul_eq_mul, ← map_smul, h3_diff_eq_commutators a b s₁ s₂ hq₁ hq₂ braid]
  simp only [map_sub, map_smul, hτ s₁ (s₂ * s₁), hτ s₂ (s₁ * s₂), hτ s₁ s₂, mul_assoc,
    sub_self, smul_zero]

/-- **The top class drops filtration.** For any trace,
`τ(σ₁σ₂σ₁) = a·τ(σ₁σ₂) + b·τ(σ₂)`: the length-3 class is a combination of
length-2 and length-1 classes. -/
theorem h3_trace_longest (a b : R) (s₁ s₂ : A) (τ : A →ₗ[R] R)
    (hτ : ∀ x y : A, τ (x * y) = τ (y * x))
    (hq₁ : s₁ * s₁ = a • s₁ + b • 1) :
    τ (s₁ * s₂ * s₁) = a * τ (s₁ * s₂) + b * τ s₂ := by
  rw [hτ (s₁ * s₂) s₁, ← mul_assoc, hq₁, add_mul, smul_mul_assoc, smul_mul_assoc, one_mul,
    map_add, map_smul, map_smul, smul_eq_mul, smul_eq_mul]

/-- **Every trace on the standard basis of `H₃`** is fixed by its three values on the
minimal-length class representatives `1, σ₁, σ₁σ₂` (`b = 1` normalisation):
on `1, σ₁, σ₂, σ₁σ₂, σ₂σ₁, σ₁σ₂σ₁` it reads `t₀, t₁, t₁, t₂, t₂, a t₂ + t₁`. -/
theorem h3_trace_standard_basis (a : R) (s₁ s₂ : A) (τ : A →ₗ[R] R)
    (hτ : ∀ x y : A, τ (x * y) = τ (y * x))
    (hq₁ : s₁ * s₁ = a • s₁ + (1 : R) • 1) (hq₂ : s₂ * s₂ = a • s₂ + (1 : R) • 1)
    (braid : s₁ * s₂ * s₁ = s₂ * s₁ * s₂) :
    τ s₂ = τ s₁ ∧ τ (s₂ * s₁) = τ (s₁ * s₂) ∧
      τ (s₁ * s₂ * s₁) = a * τ (s₁ * s₂) + τ s₁ := by
  have hd := h3_trace_sigma_diff a 1 s₁ s₂ τ hτ hq₁ hq₂ braid
  rw [one_mul, map_sub, sub_eq_zero] at hd
  refine ⟨hd.symm, hτ s₂ s₁, ?_⟩
  rw [h3_trace_longest a 1 s₁ s₂ τ hτ hq₁, one_mul, hd]

/-! ### Independence of the three classes

Three representations of `H₃` in the `T`-normalisation `T² = (Q−1)T + Q`, all with
entries polynomial in `Q` (so over any commutative ring): trivial `T ↦ Q`, sign
`T ↦ −1`, and the 2-dimensional reflection representation. -/

/-- Reflection representation of `H₃`, generator `T₁`. -/
def h3Refl₁ (Q : R) : Matrix (Fin 2) (Fin 2) R := !![Q, 1; 0, -1]
/-- Reflection representation of `H₃`, generator `T₂`. -/
def h3Refl₂ (Q : R) : Matrix (Fin 2) (Fin 2) R := !![-1, 0; Q, Q]

/-- The reflection matrices satisfy the Hecke and braid relations. -/
theorem h3Refl_relations (Q : R) :
    h3Refl₁ Q * h3Refl₁ Q = (Q - 1) • h3Refl₁ Q + Q • (1 : Matrix (Fin 2) (Fin 2) R) ∧
    h3Refl₂ Q * h3Refl₂ Q = (Q - 1) • h3Refl₂ Q + Q • (1 : Matrix (Fin 2) (Fin 2) R) ∧
    h3Refl₁ Q * h3Refl₂ Q * h3Refl₁ Q = h3Refl₂ Q * h3Refl₁ Q * h3Refl₂ Q := by
  refine ⟨?_, ?_, ?_⟩ <;> ext i j <;> fin_cases i <;> fin_cases j <;>
    simp [h3Refl₁, h3Refl₂, Matrix.mul_apply, Fin.sum_univ_two] <;> ring

/-- The reflection character on `1, T₁, T₁T₂` is `2, Q − 1, −Q`. -/
theorem h3Refl_character (Q : R) :
    Matrix.trace (1 : Matrix (Fin 2) (Fin 2) R) = 2 ∧
    Matrix.trace (h3Refl₁ Q) = Q - 1 ∧
    Matrix.trace (h3Refl₁ Q * h3Refl₂ Q) = -Q := by
  refine ⟨?_, ?_, ?_⟩ <;>
    simp [h3Refl₁, h3Refl₂, Matrix.trace, Fin.sum_univ_two, sub_eq_add_neg]

/-- **The three classes are independent at generic `q`.** If `x₀[1] + x₁[T₁] + x₂[T₁T₂]`
is killed by the trivial (`1, Q, Q²`), sign (`1, −1, 1`) and reflection
(`2, Q−1, −Q`) characters, then `(Q+1)(Q²+Q+1)` annihilates each coefficient. Over
`ℚ(q)` (or any ring where `[2]_Q [3]_Q` is a non-zero-divisor) the coefficients vanish,
so `rank HH₀(H₃) = 3`. -/
theorem h3_cocentre_independent (Q x₀ x₁ x₂ : R)
    (htriv : x₀ + x₁ * Q + x₂ * Q ^ 2 = 0)
    (hsign : x₀ - x₁ + x₂ = 0)
    (hrefl : 2 * x₀ + x₁ * (Q - 1) - x₂ * Q = 0) :
    (Q + 1) * (Q ^ 2 + Q + 1) * x₀ = 0 ∧
    (Q + 1) * (Q ^ 2 + Q + 1) * x₁ = 0 ∧
    (Q + 1) * (Q ^ 2 + Q + 1) * x₂ = 0 := by
  refine ⟨?_, ?_, ?_⟩
  · linear_combination (1) * htriv + (Q^3) * hsign + (Q*(Q+1)) * hrefl
  · linear_combination (Q+2) * htriv + (-Q*(2*Q+1)) * hsign + ((Q-1)*(Q+1)) * hrefl
  · linear_combination (Q+1) * htriv + (Q+1) * hsign + (-(Q+1)) * hrefl

/-- **The `E_∞` ranks on the cocentre.** Filtration degrees `0, 1, 2, 3` carry
`1, 1, 1, 0` classes (`1, σ₁, σ₁σ₂`, nothing), against the `E₁` ranks `1, 2, 2, 1`.
The total, 3, is the number of partitions of 3. The kills are
`h3_diff_eq_commutators` (degree 1), the commutator `σ₁σ₂ − σ₂σ₁` (degree 2) and
`h3_trace_longest` (degree 3). -/
theorem einf_ranks_h3 :
    (List.range 4).map (fun k =>
      (Finset.univ.filter fun σ : Perm (Fin 3) => inversionCount σ = k).card - [0, 1, 1, 1][k]!)
      = [1, 1, 1, 0] := by
  decide

end Cocentre

end QOU.BraidKnot
