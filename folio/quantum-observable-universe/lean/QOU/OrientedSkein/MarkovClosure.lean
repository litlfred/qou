/-
Copyright (c) 2026 litlfred. All rights reserved.
-/
import QOU.OrientedSkein.HeckeCrossing
import QOU.SchurWeyl.MarkovTraceUnique

/-!
# `QOU.OrientedSkein.MarkovClosure` — a left partial trace makes the closure a Markov trace

Stage 4a of the oriented-skein formalisation (Step 3 of
`docs/audits/2026-10-11-drinfeld-kohno-sl2-via-emvz.md`).

Let `H` be a Hecke crossing on an object `X` of an `R`-linear monoidal category
(`QOU.OrientedSkein.HeckeCrossing`).  A **left trace** for `H` is a family of `R`-linear maps
`ptr_Y : End (X ⊗ Y) → End Y`, "close the leftmost strand", subject to

* naturality in `Y`: `ptr ((X ◁ g) ≫ f) = g ≫ ptr f` and `ptr (f ≫ (X ◁ g)) = ptr f ≫ g`;
* the loop value: `ptr (𝟙) = d • 𝟙`;
* the curl: closing the left strand of the crossing gives `ptr (S on strands 0,1) = w • 𝟙`;
* the double-closure conjugation rule: closing the two leftmost strands of
  `S ≫ f` and of `f ≫ S` gives the same endomorphism.

These are exactly the properties of the closure of the leftmost strand of a braid diagram (the
last one is Markov's first move, conjugation by `σ_1`, for the two strands involved).  Given such a
left trace, a functional `s : End 𝟙 → R` with `s 𝟙 = 1`, and an inverse `d⁻¹` of `d`, the
normalised full closure

`tr_n (x) = d^{-(n+1)} · s (close all strands of ρ_n (x))`

is a Markov trace family on the Hecke tower `H_{n+1}(q)` with Markov parameter `z = w d⁻¹`
(`QOU.SchurWeyl.HeckeCoset.MarkovTraceFamily`), where `ρ_n` is the Hecke action of `H` with the
generators numbered from the right (`σ_i ↦ S` on strands `n - 1 - i, n - i`), so that the tower
inclusion `H_n ↪ H_{n+1}` adds a strand on the left, where the next closure takes place.  By
`QOU.SchurWeyl.HeckeCoset.markovTrace_unique` it is then *the* Markov trace with parameter `z`.

The braided-rigid instance (closing a strand by `η_{F,E}`, the braiding and `ε_{F,E}`) is stage 4b.

## Main definitions

* `HeckeCrossing.revAction` — the Hecke action with generators numbered from the right.
* `LeftTrace H` — the left partial-trace datum.
* `LeftTrace.fullTr` — the closure of all strands.
* `LeftTrace.markovFamily` — the normalised closure as a `MarkovTraceFamily`.

## Main statements

* `HeckeCrossing.revAction_incl`, `HeckeCrossing.revAction_last` — compatibility with the tower.
* `LeftTrace.fullTr_gen_comm` — a crossing can be moved around the full closure.
* `LeftTrace.markovFamily_eq` — uniqueness: the normalised closure equals any Markov trace family
  with the same parameter.

Sorry-free; no axioms beyond Lean/Mathlib's.

## References

* [jones1987] V. F. R. Jones, *Hecke algebra representations of braid groups and link
  polynomials*, Ann. of Math. 126 (1987), §5.
* [turaev1988] V. Turaev, *The Yang–Baxter equation and invariants of links*, Invent. Math. 92
  (1988), §2.
-/

namespace QOU.OrientedSkein

open CategoryTheory MonoidalCategory QOU.SchurWeyl QOU.SchurWeyl.HeckeInclusion

universe v u

set_option linter.unusedSectionVars false

variable {R : Type*} [CommRing R]
variable {C : Type u} [Category.{v} C] [Preadditive C] [Linear R C]
  [MonoidalCategory C] [MonoidalPreadditive C] [MonoidalLinear R C]

namespace HeckeCrossing

variable {q qi : R} {X : C} (H : HeckeCrossing q qi X)

theorem gen_succ' (n : ℕ) (k : Fin n) : H.gen (n + 1) k.succ = X ◁ H.gen n k := by
  obtain ⟨k, hk⟩ := k
  rfl

/-- The Hecke action with generators numbered from the right: `σ_i ↦ gen (n - 1 - i)`. -/
noncomputable def revAction (n : ℕ) : Hecke R q qi n →ₐ[R] End (tpow X (n + 1)) :=
  Hecke.lift R q qi n (fun i => H.gen n i.rev)
    (fun i => by
      have := H.gen_quad n i.rev
      unfold IsHeckeQuad at this
      rw [End.mul_def, this, End.one_def])
    (fun i hi => by
      simp only [End.mul_def]
      set j : Fin n := (⟨(i : ℕ) + 1, hi⟩ : Fin n).rev with hj
      have hj1 : (j : ℕ) + 1 < n := by simp [hj, Fin.rev]; omega
      have hrev : i.rev = ⟨(j : ℕ) + 1, hj1⟩ := by
        ext; simp [hj, Fin.rev]; omega
      rw [hrev]
      exact (H.gen_braid n j hj1).symm)
    (fun i j h => by
      simp only [End.mul_def]
      exact (H.gen_comm n j.rev i.rev (by simp [Fin.rev]; omega)).symm)

@[simp] theorem revAction_σ (n : ℕ) (i : Fin n) :
    H.revAction n (Hecke.σ R q qi n i) = H.gen n i.rev := by
  simp [revAction]

/-- Left whiskering by `X`, as an `R`-algebra map `End Y →ₐ[R] End (X ⊗ Y)`. -/
def whiskerAlg (X Y : C) : End Y →ₐ[R] End (X ⊗ Y) where
  toFun g := X ◁ g
  map_one' := by rw [End.one_def, End.one_def, whiskerLeft_id]
  map_mul' a b := by rw [End.mul_def, End.mul_def, whiskerLeft_comp]
  map_zero' := MonoidalPreadditive.whiskerLeft_zero
  map_add' a b := MonoidalPreadditive.whiskerLeft_add a b
  commutes' r := by
    simp only [Algebra.algebraMap_eq_smul_one, End.one_def]
    rw [MonoidalLinear.whiskerLeft_smul, whiskerLeft_id]

@[simp] theorem whiskerAlg_apply (X Y : C) (g : End Y) :
    whiskerAlg (R := R) X Y g = X ◁ g := rfl

/-- **Tower compatibility.**  The inclusion `H_n ↪ H_{n+1}` adds a strand on the left. -/
theorem revAction_incl (n : ℕ) (x : Hecke R q qi n) :
    H.revAction (n + 1) (heckeIncl R q qi n x) = X ◁ H.revAction n x := by
  have key : (H.revAction (n + 1)).comp (heckeIncl R q qi n) =
      (whiskerAlg (R := R) X (tpow X (n + 1))).comp (H.revAction n) := by
    apply Hecke.hom_ext
    intro i
    rw [AlgHom.comp_apply, heckeIncl_σ, revAction_σ, Fin.rev_castSucc]
    change _ = X ◁ H.revAction n (Hecke.σ R q qi n i)
    rw [revAction_σ]
    exact H.gen_succ' n i.rev
  exact AlgHom.congr_fun key x

/-- **The new generator acts on the two leftmost strands.** -/
theorem revAction_last (n : ℕ) :
    H.revAction (n + 1) (Hecke.σ R q qi (n + 1) (Fin.last n)) = leftCross H.S (tpow X n) := by
  rw [revAction_σ, Fin.rev_last]
  rfl

end HeckeCrossing

/-- A **left trace** for a Hecke crossing `H` on `X`: `R`-linear maps closing the leftmost strand,
natural in the remaining strands, with loop value `d`, curl `w`, and invariance of the double
closure under conjugation by the crossing (Markov's first move on the two closed strands). -/
structure LeftTrace {q qi : R} {X : C} (H : HeckeCrossing q qi X) where
  /-- Close the leftmost strand. -/
  ptr : ∀ Y : C, (X ⊗ Y ⟶ X ⊗ Y) →ₗ[R] (Y ⟶ Y)
  /-- Naturality on the source side. -/
  ptr_whisker_comp : ∀ {Y : C} (g : Y ⟶ Y) (f : X ⊗ Y ⟶ X ⊗ Y),
    ptr Y ((X ◁ g) ≫ f) = g ≫ ptr Y f
  /-- Naturality on the target side. -/
  ptr_comp_whisker : ∀ {Y : C} (g : Y ⟶ Y) (f : X ⊗ Y ⟶ X ⊗ Y),
    ptr Y (f ≫ (X ◁ g)) = ptr Y f ≫ g
  /-- The loop value. -/
  d : R
  /-- The curl value. -/
  w : R
  /-- A closed loop is the scalar `d`. -/
  ptr_id : ∀ Y : C, ptr Y (𝟙 _) = d • 𝟙 Y
  /-- Closing the left strand of a crossing gives the scalar `w`. -/
  ptr_cross : ∀ Y : C, ptr (X ⊗ Y) (leftCross H.S Y) = w • 𝟙 (X ⊗ Y)
  /-- Closing the two leftmost strands is invariant under moving the crossing around. -/
  ptr2_conj : ∀ (Y : C) (f : X ⊗ (X ⊗ Y) ⟶ X ⊗ (X ⊗ Y)),
    ptr Y (ptr (X ⊗ Y) (leftCross H.S Y ≫ f)) = ptr Y (ptr (X ⊗ Y) (f ≫ leftCross H.S Y))

namespace LeftTrace

variable {q qi : R} {X : C} {H : HeckeCrossing q qi X} (P : LeftTrace H)

theorem ptr_whisker {Y : C} (g : Y ⟶ Y) : P.ptr Y (X ◁ g) = P.d • g := by
  have h := P.ptr_whisker_comp g (𝟙 _)
  rw [Category.comp_id, P.ptr_id, Linear.comp_smul, Category.comp_id] at h
  exact h

/-- The closure of all strands of `X^{⊗m}`. -/
noncomputable def fullTr : (m : ℕ) → (tpow X m ⟶ tpow X m) →ₗ[R] (𝟙_ C ⟶ 𝟙_ C)
  | 0 => LinearMap.id
  | m + 1 => (fullTr m).comp (P.ptr (tpow X m))

@[simp] theorem fullTr_zero (f : tpow X 0 ⟶ tpow X 0) : P.fullTr 0 f = f := rfl

theorem fullTr_succ (m : ℕ) (f : tpow X (m + 1) ⟶ tpow X (m + 1)) :
    P.fullTr (m + 1) f = P.fullTr m (P.ptr (tpow X m) f) := rfl

theorem fullTr_id : ∀ m : ℕ, P.fullTr m (𝟙 _) = P.d ^ m • 𝟙 (𝟙_ C)
  | 0 => by rw [fullTr_zero, pow_zero, one_smul]; rfl
  | m + 1 => by
      rw [fullTr_succ, show 𝟙 (tpow X (m + 1)) = 𝟙 (X ⊗ tpow X m) from rfl, P.ptr_id, map_smul, fullTr_id m, smul_smul, pow_succ, mul_comm]

theorem fullTr_whisker (m : ℕ) (g : tpow X m ⟶ tpow X m) :
    P.fullTr (m + 1) (X ◁ g) = P.d • P.fullTr m g := by
  rw [fullTr_succ, P.ptr_whisker, map_smul]

/-- **A crossing moves around the full closure** (for all endomorphisms `f`). -/
theorem fullTr_gen_comm : ∀ (m : ℕ) (i : Fin m) (f : tpow X (m + 1) ⟶ tpow X (m + 1)),
    P.fullTr (m + 1) (H.gen m i ≫ f) = P.fullTr (m + 1) (f ≫ H.gen m i)
  | 0, i, _ => i.elim0
  | m + 1, ⟨0, _⟩, f => by
      simp only [HeckeCrossing.gen_zero, fullTr_succ]
      exact congrArg (P.fullTr m) (P.ptr2_conj (tpow X m) f)
  | m + 1, ⟨i + 1, h⟩, f => by
      simp only [HeckeCrossing.gen_succ, fullTr_succ (m := m + 1)]
      rw [P.ptr_whisker_comp, P.ptr_comp_whisker]
      exact fullTr_gen_comm m ⟨i, Nat.lt_of_succ_lt_succ h⟩ _

/-- The unnormalised closure functional on `H_{n+1}`. -/
noncomputable def closure (s : (𝟙_ C ⟶ 𝟙_ C) →ₗ[R] R) (n : ℕ) : Hecke R q qi n →ₗ[R] R :=
  s.comp ((P.fullTr (n + 1)).comp (H.revAction n).toLinearMap)

theorem closure_apply (s : (𝟙_ C ⟶ 𝟙_ C) →ₗ[R] R) (n : ℕ) (x : Hecke R q qi n) :
    P.closure s n x = s (P.fullTr (n + 1) (H.revAction n x)) := rfl

theorem closure_comm (s : (𝟙_ C ⟶ 𝟙_ C) →ₗ[R] R) (n : ℕ) (x y : Hecke R q qi n) :
    P.closure s n (x * y) = P.closure s n (y * x) := by
  obtain ⟨a, rfl⟩ := RingQuot.mkAlgHom_surjective R (HeckeRel R q qi n) x
  induction a using FreeAlgebra.induction generalizing y with
  | grade0 r =>
      rw [AlgHom.commutes]
      exact congrArg (P.closure s n) (Algebra.commutes (A := Hecke R q qi n) r y)
  | grade1 i =>
      have hσ : RingQuot.mkAlgHom R (HeckeRel R q qi n) (FreeAlgebra.ι R i) =
          Hecke.σ R q qi n i := rfl
      rw [hσ, closure_apply, closure_apply, map_mul (H.revAction n), map_mul (H.revAction n),
        End.mul_def, End.mul_def,
        H.revAction_σ]
      exact congrArg s (P.fullTr_gen_comm n i.rev _).symm
  | mul a b ha hb =>
      rw [map_mul (RingQuot.mkAlgHom R (HeckeRel R q qi n)), mul_assoc, ha, mul_assoc, hb,
        mul_assoc]
  | add a b ha hb =>
      rw [map_add (RingQuot.mkAlgHom R (HeckeRel R q qi n)), add_mul, mul_add, map_add, map_add,
        ha, hb]

/-- **The normalised closure is a Markov trace family**, with Markov parameter `z = w d⁻¹`. -/
noncomputable def markovFamily (s : (𝟙_ C ⟶ 𝟙_ C) →ₗ[R] R) (hs : s (𝟙 _) = 1)
    (dinv : R) (hd : P.d * dinv = 1) : HeckeCoset.MarkovTraceFamily R q qi (P.w * dinv) where
  tr n := dinv ^ (n + 1) • P.closure s n
  tr_one n := by
    rw [LinearMap.smul_apply, closure_apply, map_one, End.one_def, fullTr_id, map_smul, hs,
      smul_eq_mul, smul_eq_mul, mul_one, ← mul_pow, mul_comm, hd, one_pow]
  tr_cyclic n x y := by
    rw [LinearMap.smul_apply, LinearMap.smul_apply, closure_comm]
  tr_incl n x := by
    rw [LinearMap.smul_apply, LinearMap.smul_apply, closure_apply, closure_apply,
      H.revAction_incl, fullTr_whisker, map_smul, smul_eq_mul, smul_eq_mul, smul_eq_mul,
      ← mul_assoc, pow_succ, mul_assoc (dinv ^ (n + 1)), mul_comm dinv, hd, mul_one]
  tr_markov n x := by
    have hc : P.ptr (tpow X (n + 1)) (leftCross H.S (tpow X n)) = P.w • 𝟙 _ :=
      P.ptr_cross (tpow X n)
    rw [LinearMap.smul_apply, LinearMap.smul_apply, closure_apply, closure_apply, map_mul,
      H.revAction_incl, H.revAction_last, End.mul_def, fullTr_succ, P.ptr_comp_whisker,
      hc, Linear.smul_comp, Category.id_comp, map_smul, map_smul, smul_eq_mul,
      smul_eq_mul, smul_eq_mul, pow_succ]
    ring

theorem markovFamily_tr (s : (𝟙_ C ⟶ 𝟙_ C) →ₗ[R] R) (hs : s (𝟙 _) = 1)
    (dinv : R) (hd : P.d * dinv = 1) (n : ℕ) (x : Hecke R q qi n) :
    (P.markovFamily s hs dinv hd).tr n x =
      dinv ^ (n + 1) * s (P.fullTr (n + 1) (H.revAction n x)) := rfl

/-- **Uniqueness.**  The normalised closure agrees with every Markov trace family with the same
parameter (`QOU.SchurWeyl.HeckeCoset.markovTrace_unique`). -/
theorem markovFamily_eq (s : (𝟙_ C ⟶ 𝟙_ C) →ₗ[R] R) (hs : s (𝟙 _) = 1)
    (dinv : R) (hd : P.d * dinv = 1) (T : HeckeCoset.MarkovTraceFamily R q qi (P.w * dinv))
    (n : ℕ) (x : Hecke R q qi n) :
    dinv ^ (n + 1) * s (P.fullTr (n + 1) (H.revAction n x)) = T.tr n x :=
  HeckeCoset.markovTrace_unique (P.markovFamily s hs dinv hd) T n x

end LeftTrace

end QOU.OrientedSkein
