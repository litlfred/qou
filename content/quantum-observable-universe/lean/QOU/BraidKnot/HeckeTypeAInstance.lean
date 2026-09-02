import QOU.MathlibExt.IwahoriHeckeAlgebra
import QOU.BraidKnot.HeckeIwahoriConventionBridge
import Mathlib.GroupTheory.Coxeter.Matrix

/-!
# The arc's theorems, instantiated on the actual Hecke algebra

`HeckeGenerators` and `HeckeGeneratorsBelow` **axiomatise** the Hecke, braid and far
relations on an ambient ring; they do not construct `H_n(q)`. Every theorem in the
Jucys–Murphy / full-twist / seminormal arc is therefore of the form *"in any ring
carrying such elements, …"* — conditional on being handed one.

This file hands it one. `QOU.MathlibExt.IwahoriHecke.HeckeAlgebra` imposes both
defining families, and the type-A Coxeter matrix on `ℕ` gives the braid graph of the
infinite strand family, so **every** index satisfies the relations and the unbounded
`HeckeGenerators` class — not merely `HeckeGeneratorsBelow n` for one `n` — is
inhabited.

The parameter bookkeeping is the convention bridge: the corpus writes
`σ² = (q − q⁻¹)σ + 1`, the Iwahori normalisation writes `(T − Q)(T + 1) = 0`, and the
two agree at `Q = q²` with `σ = q⁻¹T`. So the algebra instantiated here is
`HeckeAlgebra R (q * q) typeAMatrix` and the generators are its `T` rescaled. No square
root is adjoined anywhere; the parameter moves, not the generator.
-/

namespace QOU.BraidKnot.Hecke

open QOU.MathlibExt.IwahoriHecke

universe u

variable {R : Type u} [Field R]

/-! ## The type-A Coxeter matrix -/

/-- The Coxeter matrix of type `A_∞`, on the index set `ℕ` of strand positions:
adjacent generators braid (`m = 3`), non-adjacent ones commute (`m = 2`), and the
diagonal is `1`.

Indexing by `ℕ` rather than `Fin (n-1)` is deliberate. The relations then hold at every
index, so this single object serves every `n` at once: `HeckeGenerators` (unbounded) is
inhabited, and each `HeckeGeneratorsBelow n` follows by restriction. -/
def typeAMatrix : ℕ → ℕ → ℕ := fun i j =>
  if i = j then 1 else if j = i + 1 ∨ i = j + 1 then 3 else 2

@[simp] theorem typeAMatrix_succ_right (i : ℕ) : typeAMatrix i (i + 1) = 3 := by
  simp [typeAMatrix]

@[simp] theorem typeAMatrix_succ_left (i : ℕ) : typeAMatrix (i + 1) i = 3 := by
  simp [typeAMatrix]

theorem typeAMatrix_of_lt {i j : ℕ} (h : i + 1 < j) : typeAMatrix i j = 2 := by
  have h1 : i ≠ j := by omega
  have h2 : ¬(j = i + 1 ∨ i = j + 1) := by omega
  simp [typeAMatrix, h1, h2]

theorem typeAMatrix_of_gt {i j : ℕ} (h : i + 1 < j) : typeAMatrix j i = 2 := by
  have h1 : j ≠ i := by omega
  have h2 : ¬(i = j + 1 ∨ j = i + 1) := by omega
  simp [typeAMatrix, h1, h2]

/-- **Agreement with Mathlib's `CoxeterMatrix.Aₙ`.** On the common range the ℕ-indexed
matrix above *is* Mathlib's type-A Coxeter matrix.

Mathlib does have `Aₙ : (n : ℕ) → CoxeterMatrix (Fin n)`; the reason this file does not
simply use it is the indexing. `Aₙ N` is `Fin N`-indexed, which pins one `n`, whereas
the `HeckeGenerators` class is ℕ-indexed and unbounded. Stating the agreement keeps the
two from being merely parallel: anything proved about `Aₙ` transfers here on the nose. -/
theorem typeAMatrix_eq_An (N : ℕ) (i j : Fin N) :
    typeAMatrix i j = CoxeterMatrix.Aₙ N i j := by
  have hiff : ((j : ℕ) = (i : ℕ) + 1 ∨ (i : ℕ) = (j : ℕ) + 1)
      ↔ ((j : ℕ) + 1 = (i : ℕ) ∨ (i : ℕ) + 1 = (j : ℕ)) := by omega
  simp only [typeAMatrix, CoxeterMatrix.Aₙ, Matrix.of_apply, Fin.ext_iff, hiff]

/-- The type-A matrix is symmetric — needed for the non-vacuity witness below. -/
theorem typeAMatrix_symm (i j : ℕ) : typeAMatrix i j = typeAMatrix j i := by
  have h1 : (i = j) ↔ (j = i) := by omega
  have h2 : (j = i + 1 ∨ i = j + 1) ↔ (i = j + 1 ∨ j = i + 1) := by omega
  simp only [typeAMatrix, h1, h2]

/-! ## The type-A Hecke algebra -/

/-- **The type-A Iwahori–Hecke algebra** at corpus parameter `q`, built at the Iwahori
parameter `Q = q²` so that the rescaled generators land in the corpus convention. -/
abbrev TypeAHecke (R : Type u) [Field R] (q : R) : Type u :=
  HeckeAlgebra R (q * q) typeAMatrix

/-- The Iwahori-normalised generators of the type-A Hecke algebra. -/
noncomputable def typeAT (q : R) (i : ℕ) : TypeAHecke R q := T R (q * q) typeAMatrix i

theorem typeAT_quadratic (q : R) (i : ℕ) :
    (typeAT q i - (q * q) • (1 : TypeAHecke R q)) * (typeAT q i + 1) = 0 := by
  simpa [typeAT, Algebra.smul_def] using T_quadratic (R := R) (q := q * q) (M := typeAMatrix) i

theorem typeAT_braid (q : R) (i : ℕ) :
    typeAT q i * typeAT q (i + 1) * typeAT q i
      = typeAT q (i + 1) * typeAT q i * typeAT q (i + 1) := by
  have h := T_braid (R := R) (q := q * q) (M := typeAMatrix) i (i + 1)
  rw [typeAMatrix_succ_right, typeAMatrix_succ_left] at h
  simpa [typeAT, altProd, mul_assoc] using h

theorem typeAT_far (q : R) {i j : ℕ} (hij : i + 1 < j) :
    typeAT q i * typeAT q j = typeAT q j * typeAT q i := by
  have h := T_braid (R := R) (q := q * q) (M := typeAMatrix) i j
  rw [typeAMatrix_of_lt hij, typeAMatrix_of_gt hij] at h
  simpa [typeAT, altProd] using h

/-! ## The instance

This is what promotes the arc. -/

/-- **The unbounded `HeckeGenerators` instance on the actual type-A Hecke algebra.**

`σ i = q⁻¹ · T i` is the convention bridge; the inverse is read straight off the Hecke
relation, since `σ² = (q − q⁻¹)σ + 1` says exactly that `σ − (q − q⁻¹)` is a two-sided
inverse of `σ`. -/
noncomputable def typeAHeckeGenerators (q : R) (hq : q ≠ 0) :
    HeckeGenerators R (TypeAHecke R q) q where
  σ := fun i => q⁻¹ • typeAT q i
  σinv := fun i => q⁻¹ • typeAT q i - algebraMap R (TypeAHecke R q) (q - q⁻¹)
  hecke := fun i => by
    have := hecke_of_iwahori q hq (typeAT q i) (typeAT_quadratic q i)
    simpa only [Algebra.smul_def, mul_one] using this
  mul_σinv := fun i => by
    have h : (q⁻¹ • typeAT q i) * (q⁻¹ • typeAT q i)
        = algebraMap R (TypeAHecke R q) (q - q⁻¹) * (q⁻¹ • typeAT q i) + 1 := by
      have := hecke_of_iwahori q hq (typeAT q i) (typeAT_quadratic q i)
      simpa only [Algebra.smul_def, mul_one] using this
    rw [mul_sub, h, Algebra.commutes]
    abel
  σinv_mul := fun i => by
    have h : (q⁻¹ • typeAT q i) * (q⁻¹ • typeAT q i)
        = algebraMap R (TypeAHecke R q) (q - q⁻¹) * (q⁻¹ • typeAT q i) + 1 := by
      have := hecke_of_iwahori q hq (typeAT q i) (typeAT_quadratic q i)
      simpa only [Algebra.smul_def, mul_one] using this
    rw [sub_mul, h]
    abel
  braid := fun i => braid_of_scaled q⁻¹ (typeAT q i) (typeAT q (i + 1)) (typeAT_braid q i)
  far := fun i j hij => far_of_scaled q⁻¹ (typeAT q i) (typeAT q j) (typeAT_far q hij)

/-- **The type-A Hecke algebra does not collapse.**

Without this the `HeckeGenerators` instance below would be inhabited but vacuous — every
theorem the arc transports would hold of the zero ring. The witness is the index
representation `T_i ↦ q²`, which exists because `typeAMatrix` is symmetric. -/
instance instNontrivialTypeAHecke (q : R) : Nontrivial (TypeAHecke R q) :=
  nontrivial_of_symm R (q * q) typeAMatrix typeAMatrix_symm

/-! ## What this closes

The arc's results now hold **of the Hecke algebra**, not merely of any ring that
happens to carry the relations. Two representative consequences; the rest of the arc
composes the same way. -/

/-- Jucys–Murphy elements commute **in the type-A Hecke algebra**. -/
theorem typeA_jmRaw_comm (q : R) (hq : q ≠ 0) (i k : ℕ) :
    jmRaw (typeAHeckeGenerators q hq) i * jmRaw (typeAHeckeGenerators q hq) k
      = jmRaw (typeAHeckeGenerators q hq) k * jmRaw (typeAHeckeGenerators q hq) i :=
  jmRaw_comm _ i k

/-- The multiplicative Jucys–Murphy recursion `L_{i+1} = σᵢ Lᵢ σᵢ` in the type-A Hecke
algebra, with `σ` the genuine rescaled generator. -/
theorem typeA_jmRaw_succ (q : R) (hq : q ≠ 0) (i : ℕ) :
    jmRaw (typeAHeckeGenerators q hq) (i + 1)
      = (q⁻¹ • typeAT q i) * jmRaw (typeAHeckeGenerators q hq) i * (q⁻¹ • typeAT q i) :=
  rfl

end QOU.BraidKnot.Hecke
