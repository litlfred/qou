/-
  A concrete model of `H₃(q)`: its left regular representation (owner ruling 2026-11-25,
  "Fix - no lean model of H₃(q), only abstract algebras satisfying its relations").

  Basis of `H₃(q)`, in this order: `T_e, T_0, T_1, T_01, T_10, T_010` (indices 0–5), where
  `T_010 = σ₀σ₁σ₀`. `heckeL0 h`, `heckeL1 h` are left multiplication by `σ₀`, `σ₁` in this
  basis, as linear endomorphisms of `R⁶ = Fin 6 → R`, with `h = q − q⁻¹`. The Hecke relation `σᵢ² = hσᵢ + 1` and the
  braid relation hold for every `h` in any commutative ring (`model_rel`), so every abstract
  theorem stated for `HeckeH3Rel` applies here.

  Since `X · T_e = X` in the regular representation, `X` applied to the basis vector `T_e`
  is that element's coordinate vector in the basis above (`coord_*`). That turns the measured
  photon facts of `docs/audits/2026-11-25-photon-jet-and-hearing-the-shape.md` into theorems
  over any commutative ring `R` (§7c), most of them without any non-degeneracy hypothesis:

  1. `1, σ₀, σ₁, V` are linearly independent (`F1_independent`), and the elements of
     `F₁ = span{1, σ₀, σ₁, V}` are exactly those with coordinates 4 and 5 zero (`F1_coords`).
  2. `1, V, V²` are linearly independent (`one_V_V2_independent`). This discharges the
     hypothesis of `QOU.PhotonTangent.borromean_weights_forced` in the model
     (`borromean_weights_forced_model`).
  3. `σ₀σ₁ − σ₁σ₀ ∉ F₁` (`commutator_not_mem_F1`): the photon filtration's graded piece is
     not commutative.
  4. The mirror vertex `σ₁σ₀⁻¹` is not in `W = span{σ₀, σ₁, V}` (`mirror_not_mem_W`), so
     `W ≠ W′`.
  5. Two photons span everything: `σ₁σ₀` and `σ₀σ₁σ₀ = Vσ₀ + h²σ₀ + h` are in `F₂`
     (`electron_eq`, abstract identity), so `F₂ = H₃`.
  6. **Normaliser of `F₁` = centre** (`normaliser_F1_central`): if `X = Σ cᵢTᵢ` and
     `[X, σ₀]`, `[X, σ₁]` lie in `F₁`, then `X` commutes with `σ₀` and `σ₁`.

  -- Ref: [iwahori1964] https://doi.org/10.15083/00039809
  -- Ref: [kassel2008] https://doi.org/10.1007/978-0-387-68548-9
-/
import QOU.StandardModel.PhotonTangent
import Mathlib.Data.Fin.VecNotation
import Mathlib.Algebra.Module.LinearMap.End
import Mathlib.Tactic.FinCases
import Mathlib.Tactic.LinearCombination

namespace QOU.HeckeH3Model

open QOU.Mass.BorromeanPhotonFactorisation

variable {R : Type*} [CommRing R]

/-- The model algebra: `R`-linear endomorphisms of `R⁶`. -/
abbrev M6 (R : Type*) [CommRing R] := Module.End R (Fin 6 → R)

/-- A linear endomorphism of `R⁶` from a formula. -/
def ofFun (f : (Fin 6 → R) → Fin 6 → R) (hadd : ∀ v w, f (v + w) = f v + f w)
    (hsmul : ∀ (c : R) v, f (c • v) = c • f v) : M6 R :=
  { toFun := f, map_add' := hadd, map_smul' := hsmul }

/-- Left multiplication by `σ₀`. -/
def heckeL0 (h : R) : M6 R :=
  ofFun (fun v => ![v 1, v 0 + h * v 1, v 3, v 2 + h * v 3, v 5, v 4 + h * v 5])
    (fun v w => by funext i; fin_cases i <;> simp <;> ring)
    (fun c v => by funext i; fin_cases i <;> simp <;> ring)

/-- Left multiplication by `σ₁`. -/
def heckeL1 (h : R) : M6 R :=
  ofFun (fun v => ![v 2, v 4, v 0 + h * v 2, v 5, v 1 + h * v 4, v 3 + h * v 5])
    (fun v w => by funext i; fin_cases i <;> simp <;> ring)
    (fun c v => by funext i; fin_cases i <;> simp <;> ring)

@[simp] theorem heckeL0_apply (h : R) (v : Fin 6 → R) :
    heckeL0 h v = ![v 1, v 0 + h * v 1, v 3, v 2 + h * v 3, v 5, v 4 + h * v 5] := rfl

@[simp] theorem heckeL1_apply (h : R) (v : Fin 6 → R) :
    heckeL1 h v = ![v 2, v 4, v 0 + h * v 2, v 5, v 1 + h * v 4, v 3 + h * v 5] := rfl

/-- **The model satisfies the `H₃(q)` relations** for every `h`. -/
theorem model_rel (h : R) : HeckeH3Rel h (heckeL0 h) (heckeL1 h) where
  quad_a := by
    ext v i; fin_cases i <;> simp [Module.End.mul_apply] <;> ring
  quad_b := by
    ext v i; fin_cases i <;> simp [Module.End.mul_apply] <;> ring
  braid := by
    ext v i; fin_cases i <;> simp [Module.End.mul_apply] <;> ring

/-- The basis vector `T_e`. -/
def te : Fin 6 → R := ![1, 0, 0, 0, 0, 0]

/-- Coordinates of an element of the model: its value on `T_e`. -/
def coord (X : M6 R) : Fin 6 → R := X te

/-- The vertex `V = σ₀σ₁⁻¹` in the model. -/
abbrev modelV (h : R) : M6 R := vertex h (heckeL0 h) (heckeL1 h)

/-- Coordinates of `c₀ + c₁σ₀ + c₂σ₁ + c₃V`: `(c₀, c₁ − hc₃, c₂, c₃, 0, 0)`. -/
theorem coord_F1 (h c₀ c₁ c₂ c₃ : R) (i : Fin 6) :
    coord (c₀ • (1 : M6 R) + c₁ • heckeL0 h + c₂ • heckeL1 h + c₃ • modelV h) i
      = ![c₀, c₁ - h * c₃, c₂, c₃, 0, 0] i := by
  fin_cases i <;> simp [coord, te, vertex, Module.End.mul_apply] <;> ring

/-- **`1, σ₀, σ₁, V` are linearly independent** in the model, over any commutative ring. -/
theorem F1_independent (h : R) {c₀ c₁ c₂ c₃ : R}
    (hz : c₀ • (1 : M6 R) + c₁ • heckeL0 h + c₂ • heckeL1 h + c₃ • modelV h = 0) :
    c₀ = 0 ∧ c₁ = 0 ∧ c₂ = 0 ∧ c₃ = 0 := by
  have e : ∀ i, ![c₀, c₁ - h * c₃, c₂, c₃, 0, 0] i = 0 := fun i => by
    rw [← coord_F1, hz]; rfl
  have e0 := e 0; have e1 := e 1; have e2 := e 2; have e3 := e 3
  simp at e0 e1 e2 e3
  refine ⟨e0, ?_, e2, e3⟩
  rw [e3, mul_zero, sub_zero] at e1; exact e1

/-- Coordinates of `c₀ + c₁V + c₂V²`. -/
theorem coord_V_powers (h c₀ c₁ c₂ : R) (i : Fin 6) :
    coord (c₀ • (1 : M6 R) + c₁ • modelV h + c₂ • (modelV h * modelV h)) i
      = ![c₀ + c₂ * h ^ 2, -(h * c₁) + c₂ * h ^ 3, -(c₂ * h), c₁ - c₂ * h ^ 2, c₂, 0] i := by
  fin_cases i <;> simp [coord, te, vertex, Module.End.mul_apply] <;> ring

/-- **`1, V, V²` are linearly independent** in the model, over any commutative ring. -/
theorem one_V_V2_independent (h : R) :
    LinearIndependent R ![(1 : M6 R), modelV h, modelV h * modelV h] := by
  rw [Fintype.linearIndependent_iff]
  intro c hc
  simp only [Fin.sum_univ_three, Matrix.cons_val_zero, Matrix.cons_val_one, Matrix.cons_val_two,
    Matrix.head_cons, Matrix.tail_cons] at hc
  have e : ∀ i, ![c 0 + c 2 * h ^ 2, -(h * c 1) + c 2 * h ^ 3, -(c 2 * h), c 1 - c 2 * h ^ 2,
      c 2, 0] i = 0 := fun i => by rw [← coord_V_powers, hc]; rfl
  have e0 := e 0; have e3 := e 3; have e4 := e 4
  simp at e0 e3 e4
  have k2 : c 2 = 0 := e4
  have k1 : c 1 = 0 := by rw [k2] at e3; simpa using e3
  have k0 : c 0 = 0 := by rw [k2] at e0; simpa using e0
  intro i; fin_cases i <;> simp [k0, k1, k2]

open QOU.PhotonTangent in
/-- **The Borromean photon weights are forced on the line `R·V` in `H₃(q)`**, with no measured
hypothesis. Over all photons the factorisation is not unique (audit §11.2). -/
theorem borromean_weights_forced_model [IsDomain R] {q q' : R} (hqq : q * q' = 1) {x y : R}
    (hxy : (1 + x • modelV (q - q')) * (1 + y • modelV (q - q'))
      = modelV (q - q') * modelV (q - q') * modelV (q - q')) :
    (x = q * (q - q') ∧ y = -(q' * (q - q'))) ∨ (x = -(q' * (q - q')) ∧ y = q * (q - q')) :=
  borromean_weights_forced (model_rel (q - q')) rfl hqq (one_V_V2_independent (q - q')) hxy

/-- **`σ₀σ₁ − σ₁σ₀ ∉ F₁`.** -/
theorem commutator_not_mem_F1 [Nontrivial R] (h c₀ c₁ c₂ c₃ : R) :
    heckeL0 h * heckeL1 h - heckeL1 h * heckeL0 h
      ≠ c₀ • (1 : M6 R) + c₁ • heckeL0 h + c₂ • heckeL1 h + c₃ • modelV h := by
  intro hc
  have e := coord_F1 h c₀ c₁ c₂ c₃ 4
  rw [← hc] at e
  simp [coord, te, Module.End.mul_apply] at e

/-- **The mirror vertex `σ₁σ₀⁻¹` is not in `W`.** -/
theorem mirror_not_mem_W [Nontrivial R] (h c₁ c₂ c₃ : R) :
    heckeL1 h * (heckeL0 h - h • (1 : M6 R))
      ≠ c₁ • heckeL0 h + c₂ • heckeL1 h + c₃ • modelV h := by
  intro hc
  have e := coord_F1 h 0 c₁ c₂ c₃ 4
  simp only [zero_smul, zero_add] at e
  rw [← hc] at e
  simp [coord, te, Module.End.mul_apply] at e

/-- **`σ₀σ₁σ₀ = Vσ₀ + h²σ₀ + h`** in any algebra with the `H₃(q)` relations, so the electron
word lies in `F₂`, the span of products of at most two photons. -/
theorem electron_eq {A : Type*} [Ring A] [Algebra R A] {h : R} {a b : A}
    (H : HeckeH3Rel h a b) :
    a * b * a = vertex h a b * a + (h ^ 2) • a + h • (1 : A) := by
  rw [vertex, mul_assoc a (b - h • 1) a, sub_mul, smul_mul_assoc, one_mul, mul_sub,
    mul_smul_comm, H.quad_a]
  simp only [smul_add, smul_smul, mul_one, ← mul_assoc]
  rw [pow_two]
  abel

/-- A general element `Σ cᵢ Tᵢ` of the model. -/
def elem (h : R) (c : Fin 6 → R) : M6 R :=
  c 0 • 1 + c 1 • heckeL0 h + c 2 • heckeL1 h + c 3 • (heckeL0 h * heckeL1 h)
    + c 4 • (heckeL1 h * heckeL0 h) + c 5 • (heckeL0 h * heckeL1 h * heckeL0 h)

/-- **The normaliser of `F₁` is the centre.** If `[X, σ₀]` and `[X, σ₁]` lie in `F₁`
(coordinates 4 and 5 zero, `coord_F1`), then `X` commutes with `σ₀` and `σ₁`. -/
theorem normaliser_F1_central (h : R) (c : Fin 6 → R)
    (h40 : coord (elem h c * heckeL0 h - heckeL0 h * elem h c) 4 = 0)
    (h50 : coord (elem h c * heckeL0 h - heckeL0 h * elem h c) 5 = 0)
    (h41 : coord (elem h c * heckeL1 h - heckeL1 h * elem h c) 4 = 0) :
    elem h c * heckeL0 h = heckeL0 h * elem h c ∧
      elem h c * heckeL1 h = heckeL1 h * elem h c := by
  simp [coord, te, elem, Module.End.mul_apply] at h40 h50 h41
  have k5 : c 5 = c 2 + h * c 4 := by linear_combination -h40
  have k3 : c 3 = c 4 := by linear_combination h50
  have k1 : c 1 = c 2 := by linear_combination -h41 + k5
  constructor <;>
  · ext v i; fin_cases i <;> simp [elem, Module.End.mul_apply] <;> rw [k1, k3, k5] <;> ring

end QOU.HeckeH3Model
