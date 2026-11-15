/-
Copyright (c) 2026 litlfred. All rights reserved.
-/
import Mathlib.Algebra.Category.ModuleCat.Monoidal.Basic
import Mathlib.LinearAlgebra.TensorProduct.Basis
import Mathlib.LinearAlgebra.StdBasis
import Mathlib.Tactic.Module
import QOU.OrientedSkein.HeckeCrossing

/-!
# `QOU.OrientedSkein.Model.GLnRMatrix` — the `GL_n` Hecke R-matrix on `R^n`, for every `n`

Dispatch B of PR #7705 (bean `qou-slck`): the vector representation of `U_q(gl_n)` as a
**nondegenerate** model of the oriented skein relations, built in `ModuleCat R`.  This file is the
crossing half: the object `X = R^n` and Jimbo's `GL_n` R-matrix `Ř` on `X ⊗ X`,

* `Ř (e_i ⊗ e_i) = q · e_i ⊗ e_i`,
* `Ř (e_i ⊗ e_j) = e_j ⊗ e_i + (q - qi) · e_i ⊗ e_j` for `i < j`,
* `Ř (e_i ⊗ e_j) = e_j ⊗ e_i` for `i > j`,

with the convention of `QOU.IwahoriHecke.RMatrix.rCheck` (the `n = 2` matrix already in the tree:
the `z = q - qi` term sits on the increasing pair).  We prove, for **every** `n` and over any
commutative ring `R` with `q * qi = 1`:

* `quad` — the Hecke quadratic relation `Ř² = (q - qi) Ř + (q qi) 1` (Brundan's relation (1));
* `braid` — the braid (Yang–Baxter) relation on `X ⊗ (X ⊗ X)` (Brundan's relation (2)), by a case
  analysis on the relative order of the three indices;
* `crossing` — so `Ř` is a `HeckeCrossing q qi X`, and `crossing.heckeAction` is an `R`-algebra map
  `H_{m+1}(q) →ₐ End (X^{⊗(m+1)})` for every `m`;
* `S_ne_smul_id` — for `n ≥ 2` the crossing is **not** a scalar, so this model is not the
  one-dimensional `unitDatum` of `QOU.OrientedSkein.OS.NonVacuity`.

`q * qi = 1` is genuinely needed: the quadratic relation on `e_i ⊗ e_j` (`i ≠ j`) and two of the
thirteen braid cases reduce to it.

## Engineering note

All computations are done on pure tensors of the standard basis.  The elements are typed with the
*raw* tensor products `XX R n = X ⊗[R] X` and `XXX R n = X ⊗[R] (X ⊗[R] X)` (not the `ModuleCat`
carriers `↑(X ⊗ X)`), and the whiskerings of `S` are rewritten to `LinearMap.rTensor`/`lTensor` of
the raw linear map `rLin`; otherwise the `ModuleCat` and `TensorProduct` module instances on the
same type do not match syntactically and `simp` cannot apply `TensorProduct.assoc_tmul`.

Sorry-free; no axioms beyond Lean/Mathlib's.

## References

* [jimbo1986] M. Jimbo, *A q-analogue of U(gl(N+1)), Hecke algebra, and the Yang–Baxter
  equation*, Lett. Math. Phys. 11 (1986).
* [brundan2017] J. Brundan, *Representations of the oriented skein category*, arXiv 1712.08953,
  Theorem 1.1 and §1.4.
-/

namespace QOU.OrientedSkein.GLn

open CategoryTheory MonoidalCategory Module

universe u

variable (R : Type u) [CommRing R] (n : ℕ)

/-- The vector representation `X = R^n` as an object of `ModuleCat R`. -/
noncomputable def X : ModuleCat.{u} R := ModuleCat.of R (Fin n → R)

/-- The raw tensor square `X ⊗[R] X`. -/
abbrev XX : Type u := TensorProduct R (X R n) (X R n)

/-- The raw right-nested tensor cube `X ⊗[R] (X ⊗[R] X)`. -/
abbrev XXX : Type u := TensorProduct R (X R n) (XX R n)

variable {R n}

/-- The standard basis vector `e_i`. -/
noncomputable def e (i : Fin n) : X R n := (Pi.single i 1 : Fin n → R)

variable (q qi : R)

/-- `Ř (e_i ⊗ e_j)`. -/
noncomputable def rv (i j : Fin n) : XX R n :=
  if i = j then q • (e i ⊗ₜ e i) else if i < j then e j ⊗ₜ e i + (q - qi) • (e i ⊗ₜ e j)
  else e j ⊗ₜ e i

theorem rv_self (i : Fin n) : rv q qi i i = q • (e i ⊗ₜ e i) := by simp [rv]

theorem rv_lt {i j : Fin n} (h : i < j) :
    rv q qi i j = e j ⊗ₜ e i + (q - qi) • (e i ⊗ₜ e j) := by
  simp [rv, h, h.ne]

theorem rv_gt {i j : Fin n} (h : j < i) : rv q qi i j = e j ⊗ₜ e i := by
  simp [rv, h.ne', not_lt.mpr h.le]

variable (R n) in
/-- The standard basis of `X`. -/
noncomputable def basX : Basis (Fin n) R (X R n) := Pi.basisFun R (Fin n)

theorem basX_apply (i : Fin n) : basX R n i = e i := Pi.basisFun_apply R (Fin n) i

variable (R n) in
/-- The basis `e_i ⊗ e_j` of `X ⊗ X`. -/
noncomputable def bas : Basis (Fin n × Fin n) R (XX R n) :=
  (basX R n).tensorProduct (basX R n)

theorem bas_apply (i j : Fin n) : bas R n (i, j) = e i ⊗ₜ e j := by
  rw [bas, Basis.tensorProduct_apply, basX_apply, basX_apply]

/-- `Ř` as a linear endomorphism of the raw tensor square. -/
noncomputable def rLin : XX R n →ₗ[R] XX R n := (bas R n).constr R (fun p => rv q qi p.1 p.2)

theorem rLin_ee (i j : Fin n) : rLin q qi (e i ⊗ₜ e j) = rv q qi i j := by
  rw [← bas_apply, rLin]
  exact Basis.constr_basis _ _ _ _

/-- `Ř` as a morphism `X ⊗ X ⟶ X ⊗ X` of `ModuleCat R`. -/
noncomputable def S : X R n ⊗ X R n ⟶ X R n ⊗ X R n := ModuleCat.ofHom (rLin q qi)

theorem S_ee (i j : Fin n) : (S q qi).hom (e i ⊗ₜ e j : XX R n) = rv q qi i j :=
  rLin_ee q qi i j

/-- Two morphisms out of `X ⊗ X` agree if they agree on the basis `e_i ⊗ e_j`. -/
theorem hom_ext2 {Y : ModuleCat.{u} R} {f g : X R n ⊗ X R n ⟶ Y}
    (h : ∀ i j, f.hom (e i ⊗ₜ e j : XX R n) = g.hom (e i ⊗ₜ e j : XX R n)) : f = g := by
  ext1
  apply (bas R n).ext
  rintro ⟨i, j⟩
  rw [bas_apply]
  exact h i j

variable (R n) in
/-- The basis `e_a ⊗ (e_b ⊗ e_c)` of `X ⊗ (X ⊗ X)`. -/
noncomputable def bas3 : Basis (Fin n × (Fin n × Fin n)) R (XXX R n) :=
  (basX R n).tensorProduct (bas R n)

/-- Two morphisms out of `X ⊗ (X ⊗ X)` agree if they agree on the basis `e_a ⊗ (e_b ⊗ e_c)`. -/
theorem hom_ext3 {Y : ModuleCat.{u} R} {f g : X R n ⊗ (X R n ⊗ X R n) ⟶ Y}
    (h : ∀ a b c, f.hom (e a ⊗ₜ (e b ⊗ₜ e c : XX R n) : XXX R n) =
      g.hom (e a ⊗ₜ (e b ⊗ₜ e c : XX R n) : XXX R n)) : f = g := by
  ext1
  apply (bas3 R n).ext
  rintro ⟨a, b, c⟩
  have : bas3 R n (a, b, c) = e a ⊗ₜ (e b ⊗ₜ e c : XX R n) := by
    rw [bas3, Basis.tensorProduct_apply, basX_apply, bas_apply]
  rw [this]
  exact h a b c

section homs

variable {A B C : ModuleCat.{u} R}

theorem hom_assoc_apply (x) : (α_ A B C).hom.hom x = TensorProduct.assoc R A B C x := rfl

theorem hom_assoc_inv_apply (x) :
    (α_ A B C).inv.hom x = (TensorProduct.assoc R A B C).symm x := rfl

end homs

theorem S_whiskerRight_apply (x : TensorProduct R (XX R n) (X R n)) :
    (S q qi ▷ X R n).hom x = (rLin (n := n) q qi).rTensor (X R n) x := rfl

theorem S_whiskerLeft_apply (x : XXX R n) :
    (X R n ◁ S q qi).hom x = (rLin (n := n) q qi).lTensor (X R n) x := rfl

/-- Decide an order (in)equality between elements of `Fin n` from the hypotheses. -/
macro "fin_omega" : tactic =>
  `(tactic| (simp only [Fin.lt_iff_val_lt_val, Fin.ext_iff] at *; omega))

/-- **Relation (1): the Hecke quadratic relation** `Ř² = (q - qi) Ř + (q qi) 1`. -/
theorem quad (h : q * qi = 1) : IsHeckeQuad q qi (S (n := n) q qi) := by
  unfold IsHeckeQuad
  apply hom_ext2
  intro i j
  simp only [ModuleCat.hom_comp, LinearMap.comp_apply, ModuleCat.hom_add, ModuleCat.hom_smul,
    LinearMap.add_apply, LinearMap.smul_apply, S_ee, ModuleCat.hom_id, LinearMap.id_apply]
  rcases lt_trichotomy i j with h1 | rfl | h1
  · simp only [rv_lt q qi h1, map_add, map_smul, S_ee, rv_gt q qi h1]
    match_scalars <;> first | ring1 | linear_combination h | linear_combination -h
  · simp only [rv_self, map_smul, S_ee]
    match_scalars <;> first | ring1 | linear_combination h | linear_combination -h
  · simp only [rv_gt q qi h1, S_ee, rv_lt q qi h1]
    match_scalars <;> first | ring1 | linear_combination h | linear_combination -h

set_option maxHeartbeats 1000000 in
/-- **Relation (2): the braid (Yang–Baxter) relation** for `Ř` on `X ⊗ (X ⊗ X)`, for every `n`.
The proof evaluates both sides on `e_a ⊗ (e_b ⊗ e_c)` and splits on the relative order of
`a, b, c`; only the two cases `a = b < c` and `a < b = c` use `q * qi = 1`. -/
theorem braid (h : q * qi = 1) :
    leftCross (S q qi) (X R n) ≫ (X R n ◁ S q qi) ≫ leftCross (S q qi) (X R n) =
      (X R n ◁ S q qi) ≫ leftCross (S q qi) (X R n) ≫ (X R n ◁ S q qi) := by
  apply hom_ext3
  intro a b c
  simp only [leftCross, ModuleCat.hom_comp, LinearMap.comp_apply, S_whiskerRight_apply,
    S_whiskerLeft_apply, hom_assoc_apply, hom_assoc_inv_apply, TensorProduct.assoc_symm_tmul,
    LinearMap.rTensor_tmul, LinearMap.lTensor_tmul, rLin_ee]
  rcases lt_trichotomy a b with h1 | h1 | h1 <;> rcases lt_trichotomy b c with h2 | h2 | h2 <;>
    rcases lt_trichotomy a c with h3 | h3 | h3 <;> (try subst_vars) <;>
    (try (exfalso; fin_omega)) <;>
    simp (disch := fin_omega) only [rv_self, rv_lt, rv_gt, map_add, map_smul,
      TensorProduct.tmul_add, TensorProduct.add_tmul, ← TensorProduct.smul_tmul',
      TensorProduct.tmul_smul, TensorProduct.assoc_tmul, TensorProduct.assoc_symm_tmul,
      LinearMap.rTensor_tmul, LinearMap.lTensor_tmul, rLin_ee] <;>
    match_scalars <;>
    first | ring1 | linear_combination (q - qi) * h | linear_combination (qi - q) * h

/-- **The `GL_n` R-matrix is a Hecke crossing** on `X = R^n`, for every `n`. -/
noncomputable def crossing (h : q * qi = 1) : HeckeCrossing q qi (X R n) where
  S := S q qi
  quad := quad q qi h
  braid := braid q qi h

@[simp] theorem crossing_S (h : q * qi = 1) : (crossing (n := n) q qi h).S = S q qi := rfl

/-- **Nondegeneracy of the crossing.**  For `n ≥ 2` (and `R` nontrivial) the crossing is not a
scalar multiple of the identity: `Ř (e_0 ⊗ e_1)` has a nonzero `e_1 ⊗ e_0` component.  So the
`H_m(q)`-action on `X^{⊗ m}` does not factor through the trivial character, unlike the
one-dimensional `unitDatum`. -/
theorem S_ne_smul_id [Nontrivial R] (hn : 2 ≤ n) (c : R) :
    S (n := n) q qi ≠ c • 𝟙 _ := by
  intro hS
  set i0 : Fin n := ⟨0, by omega⟩
  set i1 : Fin n := ⟨1, by omega⟩
  have h01 : i0 < i1 := by simp [i0, i1, Fin.lt_iff_val_lt_val]
  have hne : (i1, i0) ≠ (i0, i1) := by simp [i0, i1]
  have := congrArg (fun f => (bas R n).repr (f.hom (e i0 ⊗ₜ e i1 : XX R n)) (i1, i0)) hS
  simp only [ModuleCat.hom_smul, ModuleCat.hom_id, LinearMap.smul_apply, LinearMap.id_apply] at this
  rw [S_ee, rv_lt q qi h01, ← bas_apply, ← bas_apply, map_smul, map_add, map_smul,
    Basis.repr_self, Basis.repr_self] at this
  simp [Finsupp.single_apply, hne] at this

end QOU.OrientedSkein.GLn
