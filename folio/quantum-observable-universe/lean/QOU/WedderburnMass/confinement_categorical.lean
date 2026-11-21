import Mathlib.LinearAlgebra.Matrix.Trace
import Mathlib.Data.Matrix.Basis
import QOU.SchurWeyl.HeckeWedderburnAnyChar
import QOU.BraidKnot.SytRowSuperstandard

/-!
# QOU.WedderburnMass.confinement_categorical

Canonical Lean for content block
[`prop:confinement-categorical`](../../../quantum-observable-universe/mass-theory/confinement-categorical.md).

The proposition says three things about `A = H_{n+1}(q)`:

1. **Survival**: the image of the centre projector is the centre `Z(A) = ⊕_λ K·e_λ`.
2. **Trace factorisation**: every trace on `A` factors through the centre projector,
   `τ = τ ∘ π_Z`, and equals the sum over Wedderburn blocks
   `τ(x) = Σ_λ τ(e_λ) · tr(ρ_λ x) / f^λ`.
3. **Observables are Wedderburn residues**: an element commuting with all of `A`
   is fixed by `π_Z`.

All three are proved here, sorry-free, from the Wedderburn isomorphism
`QOU.SchurWeyl.AnyChar.heckeWedderburnF` (any field, `q ≠ 0`, `q` not a root of
unity). The only extra hypothesis is that each block size `f^λ` (the number of
standard Young tableaux) is nonzero in `K`, which holds in characteristic zero.

## What this file does NOT prove

The `.md` also reads survival as the collapse of the GB-filtration spectral
sequence (`E_∞^{0,0} = Z(A)`, via `HH^k(A) = 0` for `k ≥ 1`). Hochschild
cohomology is not in Mathlib, so that reading is not formalised. What is proved
is the algebraic content it rests on: the centre projector and its three
properties. The earlier encoding (a context class `ConfinementCategoricalContext`
with unconstrained data and a `sorry`) is deleted; bean `qou-mtc9`.
-/

namespace QOU.WedderburnMass

open Matrix

section Generic

variable {K : Type*} [Field K]


theorem trace_unique {n : Type*} [Fintype n] [DecidableEq n]
    (τ : Matrix n n K →ₗ[K] K) (hτ : ∀ a b, τ (a * b) = τ (b * a)) (t : n) :
    ∀ x, τ x = τ (single t t 1) * trace x := by
  have hoff : ∀ i j, i ≠ j → τ (single i j 1) = 0 := by
    intro i j hij
    have := hτ (single i i 1) (single i j 1)
    rw [single_mul_single_same, single_mul_single_of_ne (1 : K) i j i (Ne.symm hij), one_mul,
      map_zero] at this
    exact this
  have hdiag : ∀ i, τ (single i i 1) = τ (single t t 1) := by
    intro i
    have := hτ (single i t 1) (single t i 1)
    simpa [single_mul_single_same] using this
  intro x
  conv_lhs => rw [matrix_eq_sum_single x]
  simp only [map_sum]
  rw [trace, Finset.mul_sum]
  refine Finset.sum_congr rfl fun i _ => ?_
  rw [Finset.sum_eq_single i]
  · have : single i i (x i i) = x i i • single i i (1 : K) := by simp [smul_single]
    rw [this, map_smul, hdiag, smul_eq_mul, mul_comm]; rfl
  · intro j _ hj
    have : single i j (x i j) = x i j • single i j (1 : K) := by simp [smul_single]
    rw [this, map_smul, hoff i j (Ne.symm hj), smul_zero]
  · simp

/-- A matrix commuting with every matrix unit is scalar. -/
theorem eq_scalar_of_commute {n : Type*} [Fintype n] [DecidableEq n] (t : n)
    (x : Matrix n n K) (hx : ∀ y : Matrix n n K, x * y = y * x) :
    x = x t t • (1 : Matrix n n K) := by
  ext i j
  by_cases hij : i = j
  · subst hij
    simp [smul_apply]
    by_cases hit : i = t
    · subst hit; rfl
    · have := congrFun (congrFun (hx (single t i 1)) t) i
      simp [mul_apply, single, Matrix.of_apply] at this
      exact this.symm
  · simp [smul_apply, hij]
    have := congrFun (congrFun (hx (single i i 1)) i) j
    simp [mul_apply, single, Matrix.of_apply, hij] at this
    exact this.symm

section Blocks
variable {ι : Type*} [Fintype ι] [DecidableEq ι] {d : ι → Type*}
  [∀ i, Fintype (d i)] [∀ i, DecidableEq (d i)] [∀ i, Nonempty (d i)]

/-- Projection onto the centre: block `i` goes to `(tr xᵢ / dᵢ) · 1`. -/
noncomputable def centreProj (x : ∀ i, Matrix (d i) (d i) K) : ∀ i, Matrix (d i) (d i) K :=
  fun i => (trace (x i) / (Fintype.card (d i) : K)) • (1 : Matrix (d i) (d i) K)

omit [Fintype ι] [DecidableEq ι] [∀ i, Nonempty (d i)] in
theorem centreProj_central (x y : ∀ i, Matrix (d i) (d i) K) :
    centreProj x * y = y * centreProj x := by
  funext i; simp [centreProj, Pi.mul_apply]

omit [Fintype ι] in
theorem centreProj_of_central (hd : ∀ i, (Fintype.card (d i) : K) ≠ 0)
    (x : ∀ i, Matrix (d i) (d i) K) (hx : ∀ y, x * y = y * x) : centreProj x = x := by
  funext i
  have hxi : ∀ z : Matrix (d i) (d i) K, x i * z = z * x i := by
    intro z
    have := congrFun (hx (Pi.single i z)) i
    simpa [Pi.mul_apply] using this
  set t : d i := Classical.arbitrary _
  have hs := eq_scalar_of_commute t (x i) hxi
  have htr : trace (x i) = x i t t * (Fintype.card (d i) : K) := by
    conv_lhs => rw [hs]
    rw [trace_smul, trace_one, smul_eq_mul]
  show (trace (x i) / (Fintype.card (d i) : K)) • (1 : Matrix (d i) (d i) K) = x i
  rw [htr, mul_div_assoc, div_self (hd i), mul_one]
  exact hs.symm

theorem trace_eq_residue_sum (hd : ∀ i, (Fintype.card (d i) : K) ≠ 0)
    (τ : (∀ i, Matrix (d i) (d i) K) →ₗ[K] K) (hτ : ∀ a b, τ (a * b) = τ (b * a))
    (x : ∀ i, Matrix (d i) (d i) K) :
    τ x = ∑ i, τ (Pi.single i 1) * (trace (x i) / (Fintype.card (d i) : K)) := by
  have hblock : ∀ i (y : Matrix (d i) (d i) K),
      τ (Pi.single i y) = τ (Pi.single i 1) * (trace y / (Fintype.card (d i) : K)) := by
    intro i y
    let τi : Matrix (d i) (d i) K →ₗ[K] K := τ ∘ₗ LinearMap.single K (fun i => Matrix (d i) (d i) K) i
    have hτi : ∀ a b, τi (a * b) = τi (b * a) := by
      intro a b
      simp only [τi, LinearMap.comp_apply, LinearMap.coe_single]
      rw [Pi.single_mul, Pi.single_mul, hτ]
    set t : d i := Classical.arbitrary _
    have hy := trace_unique τi hτi t y
    have h1 := trace_unique τi hτi t 1
    simp only [τi, LinearMap.comp_apply, LinearMap.coe_single, trace_one] at hy h1
    rw [hy, h1, mul_assoc, mul_div_assoc', mul_comm (Fintype.card (d i) : K) (trace y),
      mul_div_assoc, div_self (hd i), mul_one]
  have hx : x = ∑ i, Pi.single i (x i) := (Finset.univ_sum_single x).symm
  conv_lhs => rw [hx]
  rw [map_sum]
  exact Finset.sum_congr rfl fun i _ => hblock i (x i)

theorem trace_centreProj (hd : ∀ i, (Fintype.card (d i) : K) ≠ 0)
    (τ : (∀ i, Matrix (d i) (d i) K) →ₗ[K] K) (hτ : ∀ a b, τ (a * b) = τ (b * a))
    (x : ∀ i, Matrix (d i) (d i) K) : τ (centreProj x) = τ x := by
  rw [trace_eq_residue_sum hd τ hτ (centreProj x), trace_eq_residue_sum hd τ hτ x]
  refine Finset.sum_congr rfl fun i _ => ?_
  simp only [centreProj, trace_smul, trace_one, smul_eq_mul]
  rw [div_mul_cancel₀ _ (hd i)]
end Blocks

end Generic

/-! ## The Hecke algebra `H_{n+1}(q)` -/

section Hecke

open QOU.SchurWeyl QOU.SchurWeyl.AnyChar
open QOU.Mathlib (StandardYoungTableau)

variable {K : Type*} [Field K] (q : K) (hq0 : q ≠ 0)
  (hq2 : GenericParameter.NotRootOfUnity q) (n : ℕ)

/-- The centre projector of `H_{n+1}(q)`: transport `centreProj` through the
Wedderburn isomorphism. -/
noncomputable def heckeCentreProj (x : Hecke K q q⁻¹ n) : Hecke K q q⁻¹ n :=
  (heckeWedderburnF q hq0 hq2 n).symm (centreProj (heckeWedderburnF q hq0 hq2 n x))

/-- **Categorical confinement** ([`prop:confinement-categorical`]).

For `A = H_{n+1}(q)` over a field `K`, `q ≠ 0` not a root of unity, with every
block size `f^λ` nonzero in `K`, and any trace `τ : A → K`:

1. `π_Z x` is central;
2. `τ (π_Z x) = τ x`, and `τ x = Σ_λ τ(e_λ) · tr(ρ_λ x) / f^λ`
   with `e_λ = Φ⁻¹(Pi.single λ 1)` the block idempotent;
3. every central `x` satisfies `π_Z x = x`. -/
theorem confinement_categorical
    (hd : ∀ lam : Nat.Partition (n + 1),
      (Fintype.card (StandardYoungTableau (QOU.Mathlib.partitionShape lam)) : K) ≠ 0)
    (τ : Hecke K q q⁻¹ n →ₗ[K] K) (hτ : ∀ a b, τ (a * b) = τ (b * a)) :
    (∀ x y : Hecke K q q⁻¹ n, heckeCentreProj q hq0 hq2 n x * y
        = y * heckeCentreProj q hq0 hq2 n x) ∧
    (∀ x, τ (heckeCentreProj q hq0 hq2 n x) = τ x) ∧
    (∀ x, τ x = ∑ lam, τ ((heckeWedderburnF q hq0 hq2 n).symm (Pi.single lam 1)) *
        (trace (heckeWedderburnF q hq0 hq2 n x lam) /
          (Fintype.card (StandardYoungTableau (QOU.Mathlib.partitionShape lam)) : K))) ∧
    (∀ x : Hecke K q q⁻¹ n, (∀ y, x * y = y * x) → heckeCentreProj q hq0 hq2 n x = x) := by
  have hΦ : ∀ z, heckeWedderburnF q hq0 hq2 n ((heckeWedderburnF q hq0 hq2 n).symm z) = z :=
    fun z => AlgEquiv.apply_symm_apply _ z
  -- the trace transported to the block side
  let τ' := τ ∘ₗ (heckeWedderburnF q hq0 hq2 n).symm.toLinearMap
  have hτ' : ∀ a b, τ' (a * b) = τ' (b * a) := by
    intro a b; simp only [τ', LinearMap.comp_apply, AlgEquiv.toLinearMap_apply, map_mul, hτ]
  have hτx : ∀ x, τ x = τ' (heckeWedderburnF q hq0 hq2 n x) := by
    intro x; simp [τ']
  refine ⟨?_, ?_, ?_, ?_⟩
  · intro x y
    apply (heckeWedderburnF q hq0 hq2 n).injective
    rw [heckeCentreProj, map_mul, map_mul, hΦ]
    exact centreProj_central (K := K)
      (d := fun lam : Nat.Partition (n + 1) =>
        StandardYoungTableau (QOU.Mathlib.partitionShape lam)) _ _
  · intro x
    rw [hτx, hτx x, heckeCentreProj, hΦ]
    exact trace_centreProj hd τ' hτ' _
  · intro x
    rw [hτx, trace_eq_residue_sum hd τ' hτ' _]
    rfl
  · intro x hx
    apply (heckeWedderburnF q hq0 hq2 n).injective
    rw [heckeCentreProj, hΦ]
    refine centreProj_of_central hd _ fun y => ?_
    have := congrArg (heckeWedderburnF q hq0 hq2 n) (hx ((heckeWedderburnF q hq0 hq2 n).symm y))
    simpa only [map_mul, hΦ] using this

end Hecke

end QOU.WedderburnMass
