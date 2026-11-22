import QOU.SchurWeyl.HeckeInclusion
import Mathlib.Algebra.Colimit.DirectLimit

/-!
# The Hecke tower as a directed system over `ℕ`

Bean `qou-0fmb`, step 1 of the colimit bridge
`HeckeCoset.MarkovTraceFamily → OcneanuTrace.MarkovTrace`.

`SchurWeyl.heckeIncl` gives one step, `H_n → H_{n+1}`. A direct limit needs the
whole family `f i j : i ≤ j → (H_i →ₐ H_j)` together with the two
`DirectedSystem` laws. This file builds it by `Nat.leRec` and nothing else.

## What is here

* `heckeInclLE i j h` — the iterated inclusion, `AlgHom.id` at `h : i ≤ i` and
  `heckeIncl ∘ …` one step up.
* `heckeInclLE_self`, `heckeInclLE_succ` — the two computation rules.
* `heckeInclLE_trans` — composition, by induction on the upper bound.
* the `DirectedSystem` instance.

## What is NOT here

No colimit, no trace, no `MarkovTrace`. In particular **nothing in this file
needs `heckeIncl` to be injective** — that is `qou-ejde`, and it gates strict
growth of the filtration (`qou-p8yg`), not the existence of the limit.

-- Ref: [leitner2026] beans qou-0fmb / qou-ejde / qou-301d.
-/

namespace QOU.SchurWeyl.HeckeDirectedSystem

open QOU.SchurWeyl QOU.SchurWeyl.Hecke QOU.SchurWeyl.HeckeInclusion

variable (K : Type*) [CommRing K] (q qi : K)

/-- The iterated Hecke inclusion `H_i →ₐ H_j` for `i ≤ j`. -/
noncomputable def heckeInclLE : ∀ (i j : ℕ), i ≤ j → (Hecke K q qi i →ₐ[K] Hecke K q qi j) :=
  fun i _j h =>
    Nat.leRec (motive := fun n (_ : i ≤ n) => Hecke K q qi i →ₐ[K] Hecke K q qi n)
      (AlgHom.id K _) (fun n _ prev => (heckeIncl K q qi n).comp prev) h

@[simp] theorem heckeInclLE_self (i : ℕ) :
    heckeInclLE K q qi i i le_rfl = AlgHom.id K (Hecke K q qi i) :=
  Nat.leRec_self _ _

theorem heckeInclLE_succ (i j : ℕ) (h : i ≤ j) :
    heckeInclLE K q qi i (j + 1) (h.trans (Nat.le_succ j))
      = (heckeIncl K q qi j).comp (heckeInclLE K q qi i j h) :=
  Nat.leRec_succ _ _ h

/-- **Composition.** Induction on the upper index, via `Nat.le_induction`. -/
theorem heckeInclLE_trans (i j k : ℕ) (hij : i ≤ j) (hjk : j ≤ k) (x : Hecke K q qi i) :
    heckeInclLE K q qi j k hjk (heckeInclLE K q qi i j hij x)
      = heckeInclLE K q qi i k (hij.trans hjk) x := by
  induction k, hjk using Nat.le_induction with
  | base => simp
  | succ n hn ih =>
      rw [heckeInclLE_succ K q qi j n hn, heckeInclLE_succ K q qi i n (hij.trans hn)]
      simp only [AlgHom.comp_apply]
      rw [ih]

/-- The iterated inclusion is the identity on generator *indices*: `σ_m` at level
`i` goes to `σ_m` at level `j`.  One step is `heckeIncl_σ` (`σ_i ↦ σ_{i.castSucc}`);
this is the `Nat.le_induction` iterate, and it is what lets a generator be read at
any level of the tower above the one it first appears in. -/
theorem heckeInclLE_σ (i j : ℕ) (hij : i ≤ j) (m : ℕ) (hmi : m < i) :
    heckeInclLE K q qi i j hij (σ K q qi i ⟨m, hmi⟩)
      = σ K q qi j ⟨m, lt_of_lt_of_le hmi hij⟩ := by
  induction j, hij using Nat.le_induction with
  | base => rw [heckeInclLE_self]; rfl
  | succ n hn ih =>
      rw [heckeInclLE_succ K q qi i n hn, AlgHom.comp_apply, ih, heckeIncl_σ]
      rfl

/-- The Hecke tower is a directed system over `ℕ`. -/
instance directedSystem :
    DirectedSystem (Hecke K q qi) (fun i j h => (heckeInclLE K q qi i j h : Hecke K q qi i → Hecke K q qi j)) where
  map_self := by
    intro i x
    rw [heckeInclLE_self]; rfl
  map_map := by
    intro k j i hij hjk x
    exact heckeInclLE_trans K q qi i j k hij hjk x

end QOU.SchurWeyl.HeckeDirectedSystem
