/-
Copyright (c) 2026 The QOU authors. Released under CC BY 4.0.

# The standard polynomial `S₄` vanishes on the concrete `H₃` model

`S₄(x₁,x₂,x₃,x₄) = Σ_{π ∈ S₄} sgn(π) x_{π1} x_{π2} x_{π3} x_{π4}` is the
Amitsur–Levitzki standard polynomial. Over a field in which `[2]_q [3]_q ≠ 0`,
`H₃(q)` is split semisimple, `≅ k ⊕ k ⊕ M₂(k)`, and `S₄` vanishes on each
factor, so it vanishes on `H₃(q)`. This file proves the vanishing with no
hypothesis on the ring and no hypothesis on `h = q − q⁻¹`: for every
commutative ring `R` and every `h : R`, `S₄` vanishes identically on the
subalgebra of `End_R(R⁶)` spanned by the six elements
`1, σ₀, σ₁, σ₀σ₁, σ₁σ₀, σ₀σ₁σ₀` of the left-regular model
`QOU.HeckeH3Model` (main theorem `S4_elem_eq_zero`).

## Method

1. `S4` is packaged as an `AlternatingMap` (`S4Alt`), so after composing with
   the linear map `c ↦ Σ cᵢ Tᵢ` it is determined by its values on strictly
   increasing basis quadruples (`Basis.ext_alternating` + `Tuple.sort`):
   `C(6,4) = 15` cases.
2. Right multiplications `ρ(σ₀)`, `ρ(σ₁)` commute with the model's left
   multiplications. An element `X` of their centraliser is zero as soon as
   `X(T_e) = 0`, because `T_e, T_e σ₀, T_e σ₁, …` are the six coordinate
   vectors. So each of the 15 cases is a check on one vector.

No numerical value enters. This settles claim 1 of
`docs/audits/2026-11-27-knot-volume-conjecture.md` and marks the line between
`n = 3` (where `S₄ ≡ 0`) and `n ≥ 4` (where `TL₄` has an `M₃` block and
`S₄ ≠ 0`).
-/
import QOU.StandardModel.HeckeH3Model
import Mathlib.LinearAlgebra.Alternating.Basic
import Mathlib.LinearAlgebra.StdBasis
import Mathlib.Data.Fin.Tuple.Sort
import Mathlib.Algebra.Algebra.Subalgebra.Basic

namespace QOU.HeckeH3StandardPolynomial

open QOU.HeckeH3Model

section General

variable {A : Type*} [Ring A]

/-- The standard polynomial of degree 4 (Amitsur–Levitzki), written out over
the 24 permutations with their signs. -/
def S4 (a b c d : A) : A :=
  a * b * c * d - a * b * d * c - a * c * b * d + a * c * d * b + a * d * b * c - a * d * c * b
  - b * a * c * d + b * a * d * c + b * c * a * d - b * c * d * a - b * d * a * c
    + b * d * c * a
  + c * a * b * d - c * a * d * b - c * b * a * d + c * b * d * a + c * d * a * b
    - c * d * b * a
  - d * a * b * c + d * a * c * b + d * b * a * c - d * b * c * a - d * c * a * b
    + d * c * b * a

theorem S4_add₁ (a a' b c d : A) : S4 (a + a') b c d = S4 a b c d + S4 a' b c d := by
  simp only [S4, add_mul, mul_add]; abel
theorem S4_add₂ (a b b' c d : A) : S4 a (b + b') c d = S4 a b c d + S4 a b' c d := by
  simp only [S4, add_mul, mul_add]; abel
theorem S4_add₃ (a b c c' d : A) : S4 a b (c + c') d = S4 a b c d + S4 a b c' d := by
  simp only [S4, add_mul, mul_add]; abel
theorem S4_add₄ (a b c d d' : A) : S4 a b c (d + d') = S4 a b c d + S4 a b c d' := by
  simp only [S4, add_mul, mul_add]; abel

section Smul
variable {R : Type*} [CommRing R] [Algebra R A]

theorem S4_smul₁ (r : R) (a b c d : A) : S4 (r • a) b c d = r • S4 a b c d := by
  simp only [S4, smul_mul_assoc, mul_smul_comm, smul_sub, smul_add]
theorem S4_smul₂ (r : R) (a b c d : A) : S4 a (r • b) c d = r • S4 a b c d := by
  simp only [S4, smul_mul_assoc, mul_smul_comm, smul_sub, smul_add]
theorem S4_smul₃ (r : R) (a b c d : A) : S4 a b (r • c) d = r • S4 a b c d := by
  simp only [S4, smul_mul_assoc, mul_smul_comm, smul_sub, smul_add]
theorem S4_smul₄ (r : R) (a b c d : A) : S4 a b c (r • d) = r • S4 a b c d := by
  simp only [S4, smul_mul_assoc, mul_smul_comm, smul_sub, smul_add]

variable (R A) in
/-- `S₄` as an alternating `R`-multilinear map `A⁴ → A`. -/
def S4Alt : A [⋀^Fin 4]→ₗ[R] A where
  toFun v := S4 (v 0) (v 1) (v 2) (v 3)
  map_update_add' v i x y := by
    rcases i with ⟨_ | _ | _ | _ | n, hi⟩
    all_goals first
      | (exfalso; omega)
      | (simp only [Function.update_apply, Fin.ext_iff, Fin.val_zero, Fin.val_one, Fin.val_two]
         norm_num
         simp [S4_add₁, S4_add₂, S4_add₃, S4_add₄])
  map_update_smul' v i r x := by
    rcases i with ⟨_ | _ | _ | _ | n, hi⟩
    all_goals first
      | (exfalso; omega)
      | (simp only [Function.update_apply, Fin.ext_iff, Fin.val_zero, Fin.val_one, Fin.val_two]
         norm_num
         simp [S4_smul₁, S4_smul₂, S4_smul₃, S4_smul₄])
  map_eq_zero_of_eq' v i j hv hij := by
    change S4 (v 0) (v 1) (v 2) (v 3) = 0
    fin_cases i <;> fin_cases j <;> (try exact absurd rfl hij) <;>
      (first
        | (have e : v 0 = v 1 := hv; rw [e])
        | (have e : v 0 = v 2 := hv; rw [e])
        | (have e : v 0 = v 3 := hv; rw [e])
        | (have e : v 1 = v 0 := hv; rw [e])
        | (have e : v 1 = v 2 := hv; rw [e])
        | (have e : v 1 = v 3 := hv; rw [e])
        | (have e : v 2 = v 0 := hv; rw [e])
        | (have e : v 2 = v 1 := hv; rw [e])
        | (have e : v 2 = v 3 := hv; rw [e])
        | (have e : v 3 = v 0 := hv; rw [e])
        | (have e : v 3 = v 1 := hv; rw [e])
        | (have e : v 3 = v 2 := hv; rw [e])) <;>
      (simp only [S4]; abel)

@[simp] theorem S4Alt_apply (v : Fin 4 → A) :
    S4Alt A R v = S4 (v 0) (v 1) (v 2) (v 3) := rfl

end Smul

/-- `S₄` vanishes when an argument is `1` (here the first). -/
theorem S4_one_left (b c d : A) : S4 1 b c d = 0 := by
  simp only [S4, one_mul, mul_one]; abel

/-- A subring is closed under `S₄`. -/
theorem S4_mem {S : Type*} [SetLike S A] [SubringClass S A] {s : S} {a b c d : A}
    (ha : a ∈ s) (hb : b ∈ s) (hc : c ∈ s) (hd : d ∈ s) : S4 a b c d ∈ s := by
  unfold S4
  repeat' first
    | apply add_mem | apply sub_mem | apply mul_mem | assumption

end General

variable {R : Type*} [CommRing R]

/-- Right multiplication by `σ₀` in the basis `1, σ₀, σ₁, σ₀σ₁, σ₁σ₀, σ₀σ₁σ₀`. -/
def heckeR0 (h : R) : M6 R :=
  ofFun (fun v => ![v 1, v 0 + h * v 1, v 4, v 5, v 2 + h * v 4, v 3 + h * v 5])
    (fun v w => by funext i; fin_cases i <;> simp <;> ring)
    (fun c v => by funext i; fin_cases i <;> simp <;> ring)

/-- Right multiplication by `σ₁` in the same basis. -/
def heckeR1 (h : R) : M6 R :=
  ofFun (fun v => ![v 2, v 3, v 0 + h * v 2, v 1 + h * v 3, v 5, v 4 + h * v 5])
    (fun v w => by funext i; fin_cases i <;> simp <;> ring)
    (fun c v => by funext i; fin_cases i <;> simp <;> ring)

@[simp] theorem heckeR0_apply (h : R) (v : Fin 6 → R) :
    heckeR0 h v = ![v 1, v 0 + h * v 1, v 4, v 5, v 2 + h * v 4, v 3 + h * v 5] := rfl

@[simp] theorem heckeR1_apply (h : R) (v : Fin 6 → R) :
    heckeR1 h v = ![v 2, v 3, v 0 + h * v 2, v 1 + h * v 3, v 5, v 4 + h * v 5] := rfl

/-- The centraliser of the right multiplications. -/
abbrev rightCentralizer (h : R) : Subalgebra R (M6 R) :=
  Subalgebra.centralizer R ({heckeR0 h, heckeR1 h} : Set (M6 R))

theorem heckeL0_mem (h : R) : heckeL0 h ∈ rightCentralizer h := by
  rw [Subalgebra.mem_centralizer_iff]
  rintro g (rfl | rfl) <;> ext v i <;> fin_cases i <;> simp [Module.End.mul_apply] <;> ring

theorem heckeL1_mem (h : R) : heckeL1 h ∈ rightCentralizer h := by
  rw [Subalgebra.mem_centralizer_iff]
  rintro g (rfl | rfl) <;> ext v i <;> fin_cases i <;> simp [Module.End.mul_apply] <;> ring

/-- An element of the right centraliser vanishes once it kills `T_e`. -/
theorem eq_zero_of_apply_te (h : R) {X : M6 R} (hX : X ∈ rightCentralizer h)
    (hte : X te = 0) : X = 0 := by
  rw [Subalgebra.mem_centralizer_iff] at hX
  have r0 : ∀ v, X (heckeR0 h v) = heckeR0 h (X v) := fun v => by
    have := congrArg (fun Y : M6 R => Y v) (hX (heckeR0 h) (by simp))
    simpa [Module.End.mul_apply] using this.symm
  have r1 : ∀ v, X (heckeR1 h v) = heckeR1 h (X v) := fun v => by
    have := congrArg (fun Y : M6 R => Y v) (hX (heckeR1 h) (by simp))
    simpa [Module.End.mul_apply] using this.symm
  have hv : ∀ v : Fin 6 → R, v = v 0 • te + v 1 • heckeR0 h te + v 2 • heckeR1 h te
      + v 3 • heckeR1 h (heckeR0 h te) + v 4 • heckeR0 h (heckeR1 h te)
      + v 5 • heckeR0 h (heckeR1 h (heckeR0 h te)) := by
    intro v; funext i; fin_cases i <;> simp [te]
  apply LinearMap.ext; intro v
  rw [hv v]
  simp only [map_add, map_smul, r0, r1, hte, map_zero, smul_zero, add_zero, LinearMap.zero_apply]

/-- The six basis elements `1, σ₀, σ₁, σ₀σ₁, σ₁σ₀, σ₀σ₁σ₀` of the model. -/
def T (h : R) : Fin 6 → M6 R :=
  ![1, heckeL0 h, heckeL1 h, heckeL0 h * heckeL1 h, heckeL1 h * heckeL0 h,
    heckeL0 h * heckeL1 h * heckeL0 h]

theorem T_mem (h : R) (i : Fin 6) : T h i ∈ rightCentralizer h := by
  have h0 := heckeL0_mem h
  have h1 := heckeL1_mem h
  fin_cases i <;> simp only [T] <;>
    first
    | exact one_mem _
    | simpa using h0
    | simpa using h1
    | simpa using mul_mem h0 h1
    | simpa using mul_mem h1 h0
    | simpa using mul_mem (mul_mem h0 h1) h0

/-! ### The fifteen sorted quadruples -/

set_option maxHeartbeats 1000000 in
theorem S4_T_1234 (h : R) : S4 (T h 1) (T h 2) (T h 3) (T h 4) = 0 := by
  apply eq_zero_of_apply_te h (S4_mem (T_mem h _) (T_mem h _) (T_mem h _) (T_mem h _))
  simp only [S4, T, LinearMap.sub_apply, LinearMap.add_apply, Module.End.mul_apply,
    Matrix.cons_val, heckeL0_apply, heckeL1_apply, te]
  funext i; fin_cases i <;> simp <;> ring

set_option maxHeartbeats 1000000 in
theorem S4_T_1235 (h : R) : S4 (T h 1) (T h 2) (T h 3) (T h 5) = 0 := by
  apply eq_zero_of_apply_te h (S4_mem (T_mem h _) (T_mem h _) (T_mem h _) (T_mem h _))
  simp only [S4, T, LinearMap.sub_apply, LinearMap.add_apply, Module.End.mul_apply,
    Matrix.cons_val, heckeL0_apply, heckeL1_apply, te]
  funext i; fin_cases i <;> simp <;> ring

set_option maxHeartbeats 1000000 in
theorem S4_T_1245 (h : R) : S4 (T h 1) (T h 2) (T h 4) (T h 5) = 0 := by
  apply eq_zero_of_apply_te h (S4_mem (T_mem h _) (T_mem h _) (T_mem h _) (T_mem h _))
  simp only [S4, T, LinearMap.sub_apply, LinearMap.add_apply, Module.End.mul_apply,
    Matrix.cons_val, heckeL0_apply, heckeL1_apply, te]
  funext i; fin_cases i <;> simp <;> ring

set_option maxHeartbeats 1000000 in
theorem S4_T_1345 (h : R) : S4 (T h 1) (T h 3) (T h 4) (T h 5) = 0 := by
  apply eq_zero_of_apply_te h (S4_mem (T_mem h _) (T_mem h _) (T_mem h _) (T_mem h _))
  simp only [S4, T, LinearMap.sub_apply, LinearMap.add_apply, Module.End.mul_apply,
    Matrix.cons_val, heckeL0_apply, heckeL1_apply, te]
  funext i; fin_cases i <;> simp <;> ring

set_option maxHeartbeats 1000000 in
theorem S4_T_2345 (h : R) : S4 (T h 2) (T h 3) (T h 4) (T h 5) = 0 := by
  apply eq_zero_of_apply_te h (S4_mem (T_mem h _) (T_mem h _) (T_mem h _) (T_mem h _))
  simp only [S4, T, LinearMap.sub_apply, LinearMap.add_apply, Module.End.mul_apply,
    Matrix.cons_val, heckeL0_apply, heckeL1_apply, te]
  funext i; fin_cases i <;> simp <;> ring

theorem S4_T_0123 (h : R) : S4 (T h 0) (T h 1) (T h 2) (T h 3) = 0 :=
  S4_one_left _ _ _

theorem S4_T_0124 (h : R) : S4 (T h 0) (T h 1) (T h 2) (T h 4) = 0 :=
  S4_one_left _ _ _

theorem S4_T_0125 (h : R) : S4 (T h 0) (T h 1) (T h 2) (T h 5) = 0 :=
  S4_one_left _ _ _

theorem S4_T_0134 (h : R) : S4 (T h 0) (T h 1) (T h 3) (T h 4) = 0 :=
  S4_one_left _ _ _

theorem S4_T_0135 (h : R) : S4 (T h 0) (T h 1) (T h 3) (T h 5) = 0 :=
  S4_one_left _ _ _

theorem S4_T_0145 (h : R) : S4 (T h 0) (T h 1) (T h 4) (T h 5) = 0 :=
  S4_one_left _ _ _

theorem S4_T_0234 (h : R) : S4 (T h 0) (T h 2) (T h 3) (T h 4) = 0 :=
  S4_one_left _ _ _

theorem S4_T_0235 (h : R) : S4 (T h 0) (T h 2) (T h 3) (T h 5) = 0 :=
  S4_one_left _ _ _

theorem S4_T_0245 (h : R) : S4 (T h 0) (T h 2) (T h 4) (T h 5) = 0 :=
  S4_one_left _ _ _

theorem S4_T_0345 (h : R) : S4 (T h 0) (T h 3) (T h 4) (T h 5) = 0 :=
  S4_one_left _ _ _

/-- The 15 strictly increasing basis quadruples: the five avoiding `T_e = 1`
are checked on `T_e`, the ten containing it vanish by `S4_one_left`. -/
theorem S4_T_strictMono (h : R) (a b c d : Fin 6) (hab : a < b) (hbc : b < c) (hcd : c < d) :
    S4 (T h a) (T h b) (T h c) (T h d) = 0 := by
  rcases a with ⟨_ | _ | _ | _ | _ | _ | a, ha⟩ <;> (try (exfalso; omega)) <;>
  rcases b with ⟨_ | _ | _ | _ | _ | _ | b, hb⟩ <;> (try (exfalso; omega)) <;>
  (try (exfalso; simp only [Fin.mk_lt_mk] at hab; omega)) <;>
  rcases c with ⟨_ | _ | _ | _ | _ | _ | c, hc⟩ <;> (try (exfalso; omega)) <;>
  (try (exfalso; simp only [Fin.mk_lt_mk] at hbc; omega)) <;>
  rcases d with ⟨_ | _ | _ | _ | _ | _ | d, hd⟩ <;> (try (exfalso; omega)) <;>
  (try (exfalso; simp only [Fin.mk_lt_mk] at hcd; omega)) <;>
  simp only [Nat.zero_add, Nat.reduceAdd, Fin.zero_eta, Fin.reduceFinMk, S4_T_1234, S4_T_1235, S4_T_1245, S4_T_1345, S4_T_2345, S4_T_0123, S4_T_0124, S4_T_0125, S4_T_0134, S4_T_0135, S4_T_0145, S4_T_0234, S4_T_0235, S4_T_0245, S4_T_0345]

/-- `c ↦ Σ cᵢ Tᵢ` as a linear map. -/
noncomputable def elemₗ (h : R) : (Fin 6 → R) →ₗ[R] M6 R :=
  (Pi.basisFun R (Fin 6)).constr R (T h)

theorem elemₗ_apply (h : R) (c : Fin 6 → R) : elemₗ h c = elem h c := by
  simp [elemₗ, Module.Basis.constr_apply, Fin.sum_univ_six, elem, T]

/-- **`S₄ ≡ 0` on the concrete `H₃` model**, over every commutative ring and
for every `h`. -/
theorem S4_elem_eq_zero (h : R) (c₁ c₂ c₃ c₄ : Fin 6 → R) :
    S4 (elem h c₁) (elem h c₂) (elem h c₃) (elem h c₄) = 0 := by
  have key : (S4Alt (M6 R) R).compLinearMap (elemₗ h) = 0 := by
    apply (Pi.basisFun R (Fin 6)).ext_alternating
    intro v hv
    simp only [AlternatingMap.zero_apply, AlternatingMap.compLinearMap_apply]
    set g := S4Alt (M6 R) R
    have hb : (fun i => elemₗ h (Pi.basisFun R (Fin 6) (v i))) = T h ∘ v := by
      funext i; simp [elemₗ]
    rw [hb]
    set σ := Tuple.sort v
    have hmono : StrictMono (v ∘ σ) :=
      (Tuple.monotone_sort v).strictMono_of_injective (hv.comp σ.injective)
    have hsorted : g (T h ∘ (v ∘ σ)) = 0 := by
      simp only [g, S4Alt_apply, Function.comp_apply]
      exact S4_T_strictMono h _ _ _ _ (hmono (by decide)) (hmono (by decide))
        (hmono (by decide))
    have := g.map_perm (T h ∘ v) σ
    rw [Function.comp_assoc] at this
    rw [hsorted] at this
    have h1 := congrArg (fun x => Equiv.Perm.sign σ • x) this
    simp only [smul_zero, smul_smul, Int.units_mul_self, one_smul] at h1
    exact h1.symm
  have := congrArg (fun f : (Fin 6 → R) [⋀^Fin 4]→ₗ[R] M6 R => f ![c₁, c₂, c₃, c₄]) key
  simpa [elemₗ_apply] using this

end QOU.HeckeH3StandardPolynomial
