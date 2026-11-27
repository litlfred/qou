/-
Copyright (c) 2026 QOU contributors. All rights reserved.
Released under Apache 2.0 license.
-/
import Mathlib.Algebra.Colimit.DirectLimit
import Mathlib.Algebra.Algebra.Hom
import Mathlib.Algebra.Algebra.Subalgebra.Basic

/-!
# The colimit of an `ℕ`-indexed tower of algebras

Given `K`-algebras `G 0, G 1, …` and one-step algebra maps `f n : G n →ₐ[K] G (n+1)`,
this file builds the iterated maps `inclLE i j : G i →ₐ G j` (`i ≤ j`), the
`DirectedSystem`, the colimit `Lim G f` as a `K`-algebra, the level maps
`ofₐ n : G n →ₐ[K] Lim G f`, and the range filtration `H n := (ofₐ n).range` with
`H_mono`.

It is the generic form of `QOU.SchurWeyl.HeckeDirectedSystem` + `QOU.SchurWeyl.HeckeColimit`,
which do the same thing for one specific tower. It is used for the Coxeter-presentation
Hecke tower in `QOU.IwahoriHecke.CoxeterTower` (bean `qou-0fmb`).

**Mathlib supplies no `Algebra K (DirectLimit …)` instance.** As in `HeckeColimit`, the
algebra structure is built with `Algebra.ofModule` over the existing
`DirectLimit.instModule`, so there is one `SMul K (Lim G f)` and no diamond.

No injectivity of the `f n` is assumed or used: `H n` is the *image* of level `n`.

Sorry-free; axioms `propext`, `Classical.choice`, `Quot.sound`.
-/

namespace QOU.MathlibExt.AlgebraTowerColimit

variable {K : Type*} [CommRing K] (G : ℕ → Type*) [∀ n, Ring (G n)] [∀ n, Algebra K (G n)]
  (f : ∀ n, G n →ₐ[K] G (n + 1))

/-- The iterated tower map `G i →ₐ G j` for `i ≤ j`. -/
noncomputable def inclLE : ∀ (i j : ℕ), i ≤ j → (G i →ₐ[K] G j) :=
  fun i _j h =>
    Nat.leRec (motive := fun n (_ : i ≤ n) => G i →ₐ[K] G n)
      (AlgHom.id K _) (fun n _ prev => (f n).comp prev) h

@[simp] theorem inclLE_self (i : ℕ) : inclLE G f i i le_rfl = AlgHom.id K (G i) :=
  Nat.leRec_self _ _

theorem inclLE_succ (i j : ℕ) (h : i ≤ j) :
    inclLE G f i (j + 1) (h.trans (Nat.le_succ j)) = (f j).comp (inclLE G f i j h) :=
  Nat.leRec_succ _ _ h

theorem inclLE_trans (i j k : ℕ) (hij : i ≤ j) (hjk : j ≤ k) (x : G i) :
    inclLE G f j k hjk (inclLE G f i j hij x) = inclLE G f i k (hij.trans hjk) x := by
  induction k, hjk using Nat.le_induction with
  | base => simp
  | succ n hn ih =>
      rw [inclLE_succ G f j n hn, inclLE_succ G f i n (hij.trans hn)]
      simp only [AlgHom.comp_apply]
      rw [ih]

instance directedSystem :
    DirectedSystem G (fun i j h => (inclLE G f i j h : G i → G j)) where
  map_self := by
    intro i x
    rw [inclLE_self]; rfl
  map_map := by
    intro k j i hij hjk x
    exact inclLE_trans G f i j k hij hjk x

/-- The colimit of the tower. -/
noncomputable abbrev Lim : Type _ := DirectLimit G (inclLE G f)

/-- Level `n` as a ring map into the colimit. -/
noncomputable abbrev ofLim (n : ℕ) : G n →+* Lim G f :=
  DirectLimit.Ring.of G (inclLE G f) n

/-- Level `n` as a linear map into the colimit (the same function as `ofLim n`). -/
noncomputable abbrev ofLimₗ (n : ℕ) : G n →ₗ[K] Lim G f :=
  DirectLimit.Module.of K ℕ G (inclLE G f) n

theorem smul_mul_assoc' (r : K) (x y : Lim G f) : r • x * y = r • (x * y) := by
  induction x, y using DirectLimit.induction₂ (f := inclLE G f) with
  | _ i x y =>
    show r • ofLim G f i x * ofLim G f i y = r • (ofLim G f i x * ofLim G f i y)
    have hm : ∀ a b : G i, ofLim G f i (a * b) = ofLim G f i a * ofLim G f i b := map_mul _
    have hs : ∀ (c : K) (a : G i), ofLim G f i (c • a) = c • ofLim G f i a :=
      fun c a => (ofLimₗ G f i).map_smul c a
    calc r • ofLim G f i x * ofLim G f i y
        = ofLim G f i (r • x) * ofLim G f i y := by rw [hs]
      _ = ofLim G f i (r • x * y) := (hm _ _).symm
      _ = ofLim G f i (r • (x * y)) := by rw [smul_mul_assoc]
      _ = r • ofLim G f i (x * y) := hs _ _
      _ = r • (ofLim G f i x * ofLim G f i y) := by rw [hm]

theorem mul_smul_comm' (r : K) (x y : Lim G f) : x * r • y = r • (x * y) := by
  induction x, y using DirectLimit.induction₂ (f := inclLE G f) with
  | _ i x y =>
    show ofLim G f i x * r • ofLim G f i y = r • (ofLim G f i x * ofLim G f i y)
    have hm : ∀ a b : G i, ofLim G f i (a * b) = ofLim G f i a * ofLim G f i b := map_mul _
    have hs : ∀ (c : K) (a : G i), ofLim G f i (c • a) = c • ofLim G f i a :=
      fun c a => (ofLimₗ G f i).map_smul c a
    calc ofLim G f i x * r • ofLim G f i y
        = ofLim G f i x * ofLim G f i (r • y) := by rw [hs]
      _ = ofLim G f i (x * r • y) := (hm _ _).symm
      _ = ofLim G f i (r • (x * y)) := by rw [mul_smul_comm]
      _ = r • ofLim G f i (x * y) := hs _ _
      _ = r • (ofLim G f i x * ofLim G f i y) := by rw [hm]

/-- The colimit is a `K`-algebra, over the colimit's own module structure. -/
noncomputable instance instAlgebraLim : Algebra K (Lim G f) :=
  Algebra.ofModule (smul_mul_assoc' G f) (mul_smul_comm' G f)

/-- Level `n` as a `K`-algebra map into the colimit. -/
noncomputable def ofₐ (n : ℕ) : G n →ₐ[K] Lim G f :=
  AlgHom.mk' (ofLim G f n) (fun c x => (ofLimₗ G f n).map_smul c x)

@[simp] theorem ofₐ_apply (n : ℕ) (x : G n) : ofₐ G f n x = ofLim G f n x := rfl

theorem ofₐ_comp {i j : ℕ} (hij : i ≤ j) (x : G i) :
    ofₐ G f j (inclLE G f i j hij x) = ofₐ G f i x :=
  DirectLimit.Ring.of_f (f := inclLE G f) hij x

/-- One step up the tower, then into the colimit. -/
theorem ofₐ_step (n : ℕ) (x : G n) : ofₐ G f (n + 1) (f n x) = ofₐ G f n x := by
  have h := ofₐ_comp G f (Nat.le_succ n) x
  rw [inclLE_succ G f n n le_rfl, AlgHom.comp_apply, inclLE_self] at h
  exact h

/-- The range filtration: `H n` is the image of level `n`. -/
noncomputable def H (n : ℕ) : Subalgebra K (Lim G f) := (ofₐ G f n).range

theorem H_mono : Monotone (H G f) := by
  intro i j hij y hy
  obtain ⟨x, rfl⟩ := hy
  exact ⟨inclLE G f i j hij x, ofₐ_comp G f hij x⟩

/-- Every element of the colimit comes from some level. -/
theorem exists_ofₐ (y : Lim G f) : ∃ n x, ofₐ G f n x = y := by
  induction y using DirectLimit.induction (f := inclLE G f) with
  | ih i x => exact ⟨i, x, rfl⟩

end QOU.MathlibExt.AlgebraTowerColimit
