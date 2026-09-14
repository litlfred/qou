/-
Copyright (c) 2026 QOU contributors. All rights reserved.
Released under Apache 2.0 license.
-/
import Mathlib.Algebra.Algebra.Basic
import QOU.SchurWeyl.HeckeDirectedSystem

/-!
# The colimit of the Iwahori–Hecke tower, and its range filtration

Step 2 of the bridge from `QOU.SchurWeyl`'s level-indexed Hecke algebras to the
single-algebra `OcneanuTrace.MarkovTrace` interface, which wants **one** ring `A`
carrying a monotone family of subalgebras `H : ℕ → Subalgebra R A`.  Step 1
(`QOU.SchurWeyl.HeckeDirectedSystem`) supplied the `DirectedSystem` instance;
this file takes the colimit and builds the filtration.

## What is proved here

* `HeckeLim` — the colimit `lim_n Hecke K q qi n`, via Mathlib's unified
  `DirectLimit`.  No injectivity of `heckeIncl` is needed: measured against the
  live Mathlib, `DirectLimit` carries **no** injectivity hypothesis, so the
  carrier exists unconditionally and the bridge is *not* gated on bean
  `qou-ejde` (whether `heckeIncl` is injective).  That question governs whether
  the `ofLim n` are embeddings, which is a separate statement.
* `instAlgebraHeckeLim` — the `K`-algebra structure.  **Mathlib supplies no
  `Algebra R (DirectLimit …)` instance** (measured: the `DirectLimit` namespace
  has `instModule` and `instRing`-family instances and nothing algebra-valued),
  so it is built here with `Algebra.ofModule` over the *existing* `Module K`
  instance — deliberately not with `RingHom.toAlgebra'`, which would mint a
  second `SMul K (HeckeLim …)` and put a diamond against `DirectLimit.instModule`.
* `ofLimₐ` — level `n` as an `AlgHom` into the colimit, and `ofLimₐ_comp`, the
  statement that it is compatible with the tower maps.
* `H` and `H_mono` — the range filtration and its monotonicity.  This is the
  `MarkovTrace.H` / `MarkovTrace.H_mono` pair.

## What is NOT proved here

Nothing about a trace.  `H n` is the *image* of level `n`, which coincides with
level `n` itself only when `ofLim n` is injective; that is exactly the open
question of `qou-ejde` and is **not** used anywhere below.  The Markov
stabilisation axiom, the generators `g`/`ginv`, and the trace itself are steps
3–6 and are not in this file.
-/

namespace QOU.SchurWeyl.HeckeColimit

open QOU.SchurWeyl QOU.SchurWeyl.HeckeInclusion QOU.SchurWeyl.HeckeDirectedSystem

variable (K : Type*) [CommRing K] (q qi : K)

/-- The transition family of the Hecke tower, packaged for `DirectLimit`. -/
noncomputable abbrev heckeF : ∀ i j : ℕ, i ≤ j → (Hecke K q qi i →ₐ[K] Hecke K q qi j) :=
  heckeInclLE K q qi

/-- The colimit of the Iwahori–Hecke tower `Hecke K q qi 0 → Hecke K q qi 1 → ⋯`. -/
noncomputable abbrev HeckeLim : Type _ :=
  DirectLimit (Hecke K q qi) (heckeF K q qi)

/-- Level `n` of the tower, as a ring map into the colimit. -/
noncomputable abbrev ofLim (n : ℕ) : Hecke K q qi n →+* HeckeLim K q qi :=
  DirectLimit.Ring.of (Hecke K q qi) (heckeF K q qi) n

/-- Level `n` of the tower, as a `K`-linear map into the colimit. -/
noncomputable abbrev ofLimₗ (n : ℕ) : Hecke K q qi n →ₗ[K] HeckeLim K q qi :=
  DirectLimit.Module.of K ℕ (Hecke K q qi) (heckeF K q qi) n

/-- The ring map and the linear map into the colimit are the *same* function.
Both are `x ↦ ⟦⟨n, x⟩⟧`; this is what lets the algebra axioms below be checked
by transporting the corresponding identity one level down the tower. -/
@[simp] theorem ofLimₗ_eq_ofLim (n : ℕ) (x : Hecke K q qi n) :
    ofLimₗ K q qi n x = ofLim K q qi n x := rfl

/-- Scalars pull out of the colimit's multiplication on the left. -/
theorem smul_mul_assoc' (r : K) (x y : HeckeLim K q qi) :
    r • x * y = r • (x * y) := by
  induction x, y using DirectLimit.induction₂ (f := heckeF K q qi) with
  | _ i x y =>
    show r • ofLim K q qi i x * ofLim K q qi i y = r • (ofLim K q qi i x * ofLim K q qi i y)
    have hm : ∀ a b : Hecke K q qi i,
        ofLim K q qi i (a * b) = ofLim K q qi i a * ofLim K q qi i b := map_mul _
    have hs : ∀ (c : K) (a : Hecke K q qi i),
        ofLim K q qi i (c • a) = c • ofLim K q qi i a :=
      fun c a => (ofLimₗ K q qi i).map_smul c a
    calc r • ofLim K q qi i x * ofLim K q qi i y
        = ofLim K q qi i (r • x) * ofLim K q qi i y := by rw [hs]
      _ = ofLim K q qi i (r • x * y) := (hm _ _).symm
      _ = ofLim K q qi i (r • (x * y)) := by rw [smul_mul_assoc]
      _ = r • ofLim K q qi i (x * y) := hs _ _
      _ = r • (ofLim K q qi i x * ofLim K q qi i y) := by rw [hm]

/-- Scalars pull out of the colimit's multiplication on the right. -/
theorem mul_smul_comm' (r : K) (x y : HeckeLim K q qi) :
    x * r • y = r • (x * y) := by
  induction x, y using DirectLimit.induction₂ (f := heckeF K q qi) with
  | _ i x y =>
    show ofLim K q qi i x * r • ofLim K q qi i y = r • (ofLim K q qi i x * ofLim K q qi i y)
    have hm : ∀ a b : Hecke K q qi i,
        ofLim K q qi i (a * b) = ofLim K q qi i a * ofLim K q qi i b := map_mul _
    have hs : ∀ (c : K) (a : Hecke K q qi i),
        ofLim K q qi i (c • a) = c • ofLim K q qi i a :=
      fun c a => (ofLimₗ K q qi i).map_smul c a
    calc ofLim K q qi i x * r • ofLim K q qi i y
        = ofLim K q qi i x * ofLim K q qi i (r • y) := by rw [hs]
      _ = ofLim K q qi i (x * r • y) := (hm _ _).symm
      _ = ofLim K q qi i (r • (x * y)) := by rw [mul_smul_comm]
      _ = r • ofLim K q qi i (x * y) := hs _ _
      _ = r • (ofLim K q qi i x * ofLim K q qi i y) := by rw [hm]

/-- The colimit is a `K`-algebra.

Built from the **existing** `DirectLimit.instModule`, so `•` on `HeckeLim` is the
colimit's own scalar action and no diamond is created.  `RingHom.toAlgebra'`
applied to `ofLim 0 ∘ algebraMap` would also typecheck and is deliberately not
used: it would introduce a second, propositionally-but-not-definitionally equal
`SMul K (HeckeLim K q qi)`. -/
noncomputable instance instAlgebraHeckeLim : Algebra K (HeckeLim K q qi) :=
  Algebra.ofModule (smul_mul_assoc' K q qi) (mul_smul_comm' K q qi)

/-- Level `n` of the tower, as a `K`-algebra map into the colimit. -/
noncomputable def ofLimₐ (n : ℕ) : Hecke K q qi n →ₐ[K] HeckeLim K q qi :=
  AlgHom.mk' (ofLim K q qi n) (fun c x => (ofLimₗ K q qi n).map_smul c x)

@[simp] theorem ofLimₐ_apply (n : ℕ) (x : Hecke K q qi n) :
    ofLimₐ K q qi n x = ofLim K q qi n x := rfl

/-- The algebra maps into the colimit are compatible with the tower maps: going
up the tower first and then into the colimit is the same as going straight in. -/
theorem ofLimₐ_comp {i j : ℕ} (hij : i ≤ j) (x : Hecke K q qi i) :
    ofLimₐ K q qi j (heckeInclLE K q qi i j hij x) = ofLimₐ K q qi i x :=
  DirectLimit.Ring.of_f (f := heckeF K q qi) hij x

/-- The **range filtration** of the colimit: `H n` is the image of level `n`.

This is the `MarkovTrace.H` field.  It is the image, not an isomorphic copy of
`Hecke K q qi n` — those coincide exactly when `ofLim n` is injective, which is
the open question of bean `qou-ejde` and is not assumed anywhere here. -/
noncomputable def H (n : ℕ) : Subalgebra K (HeckeLim K q qi) :=
  (ofLimₐ K q qi n).range

theorem mem_H (n : ℕ) (y : HeckeLim K q qi) :
    y ∈ H K q qi n ↔ ∃ x : Hecke K q qi n, ofLim K q qi n x = y :=
  Iff.rfl

theorem ofLim_mem_H (n : ℕ) (x : Hecke K q qi n) :
    ofLim K q qi n x ∈ H K q qi n :=
  ⟨x, rfl⟩

/-- The range filtration is increasing.  This is the `MarkovTrace.H_mono` field. -/
theorem H_mono : Monotone (H K q qi) := by
  intro i j hij y hy
  obtain ⟨x, rfl⟩ := hy
  exact ⟨heckeInclLE K q qi i j hij x, ofLimₐ_comp K q qi hij x⟩

end QOU.SchurWeyl.HeckeColimit
