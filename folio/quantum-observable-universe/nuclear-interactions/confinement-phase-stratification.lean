import Mathlib.Topology.Connected.Clopen
import Mathlib.Topology.Instances.Real.Lemmas
import Mathlib.Data.Fintype.Card

/-!
# QOU.BraidKnot.ConfinementPhaseStratification

**Proposition** (`prop:confinement-phase-stratification`): openness of the
confinement locus, and constancy of the active support and the binding
multiplicity on a connected phase.

## Model

The confinement predicate is *strict* feasibility of the confinement SDP.
Strict feasibility is written as finitely many strict inequalities
`0 < g i (q, X)` in the parameter `q` and the decision variable `X`
(positive definiteness of a Gram matrix is such a system, by Sylvester's
criterion on its leading principal minors). The `g i` are assumed
continuous. The locus is then `strictLocus g = {q | ∃ X, ∀ i, 0 < g i (q, X)}`.

The active support at `q` is the set of dual variables that are strictly
positive. The dual `y` and the primal slacks `s` are assumed continuous in
`q`, complementary (`y i q * s i q = 0`) and strictly complementary
(`0 < y i q ∨ 0 < s i q`) on the phase. These are hypotheses about the SDP
data, not about the conclusion.

## What is proved (2026-11-21)

* `isOpen_strictLocus` — claim (1): the locus is open. It is the projection
  of an open set, and `Prod.fst` is an open map.
* `activeSupport_eq_of_isPreconnected` and `mu_eq_of_isPreconnected` —
  claim (3), first two bullets: on a preconnected set where the
  hypotheses hold, the active support and its size are constant.

Not proved here: claim (2) (the complement is a real-algebraic
stratification), the real-analyticity of `σ_F` in claim (3), and claims (4)
and (5). Until 2026-11-21 this file carried claims (1) and (3) as fields of
a class with opaque `confined` and `mu`, and the theorems returned those
fields.

LaTeX: `\label{prop:confinement-phase-stratification}`
-/

namespace QOU.BraidKnot

open Set

variable {E : Type*} [TopologicalSpace E] {ι : Type*}

/-- The confinement locus: parameters `q` at which the strict system
    `0 < g i (q, X)` has a solution `X`. -/
def strictLocus (g : ι → ℝ × E → ℝ) : Set ℝ :=
  {q | ∃ X, ∀ i, 0 < g i (q, X)}

/-- **Claim (1): the confinement locus is open.** -/
-- Ref: [leitner2026] prop:confinement-phase-stratification
theorem isOpen_strictLocus [Finite ι] (g : ι → ℝ × E → ℝ)
    (hg : ∀ i, Continuous (g i)) : IsOpen (strictLocus g) := by
  have hS : IsOpen (⋂ i, {p : ℝ × E | 0 < g i p}) :=
    isOpen_iInter_of_finite fun i => isOpen_lt continuous_const (hg i)
  have hEq : strictLocus g = Prod.fst '' (⋂ i, {p : ℝ × E | 0 < g i p}) := by
    ext q
    simp only [strictLocus, mem_setOf_eq, mem_image, mem_iInter, Prod.exists]
    constructor
    · rintro ⟨X, hX⟩
      exact ⟨q, X, hX, rfl⟩
    · rintro ⟨q', X, hX, rfl⟩
      exact ⟨X, hX⟩
  rw [hEq]
  exact isOpenMap_fst _ hS

/-- The active support at `q`: dual variables that are strictly positive. -/
noncomputable def activeSupport {κ : Type*} [Fintype κ] (y : κ → ℝ → ℝ) (q : ℝ) :
    Finset κ := by
  classical
  exact Finset.univ.filter (fun i => 0 < y i q)

theorem mem_activeSupport {κ : Type*} [Fintype κ] (y : κ → ℝ → ℝ) (q : ℝ) (i : κ) :
    i ∈ activeSupport y q ↔ 0 < y i q := by
  classical
  simp [activeSupport]

/-- On a preconnected set, a strictly complementary pair of continuous
    functions keeps the same sign pattern: either `y` is positive
    throughout, or it is not positive anywhere. -/
theorem pos_dichotomy_of_isPreconnected {y s : ℝ → ℝ} (hy : Continuous y)
    (hs : Continuous s) {C : Set ℝ} (hC : IsPreconnected C)
    (hstrict : ∀ q ∈ C, 0 < y q ∨ 0 < s q)
    (hcomp : ∀ q ∈ C, y q * s q = 0) :
    (∀ q ∈ C, 0 < y q) ∨ (∀ q ∈ C, ¬ 0 < y q) := by
  by_contra h
  push_neg at h
  obtain ⟨⟨a, ha, hya⟩, ⟨b, hb, hyb⟩⟩ := h
  have hsa : 0 < s a := (hstrict a ha).resolve_left (not_lt.mpr hya)
  obtain ⟨c, hcC, hyc, hsc⟩ :=
    hC {q | 0 < y q} {q | 0 < s q} (isOpen_lt continuous_const hy)
      (isOpen_lt continuous_const hs) (fun q hq => hstrict q hq)
      ⟨b, hb, hyb⟩ ⟨a, ha, hsa⟩
  have h0 := hcomp c hcC
  have : 0 < y c * s c := mul_pos hyc hsc
  linarith

/-- **Claim (3), active support.** On a preconnected set where the dual `y`
    and the slacks `s` are continuous, complementary and strictly
    complementary, the active support is constant. -/
-- Ref: [leitner2026] prop:confinement-phase-stratification
theorem activeSupport_eq_of_isPreconnected {κ : Type*} [Fintype κ]
    (y s : κ → ℝ → ℝ) (hy : ∀ i, Continuous (y i)) (hs : ∀ i, Continuous (s i))
    {C : Set ℝ} (hC : IsPreconnected C)
    (hstrict : ∀ i, ∀ q ∈ C, 0 < y i q ∨ 0 < s i q)
    (hcomp : ∀ i, ∀ q ∈ C, y i q * s i q = 0)
    {q₁ q₂ : ℝ} (h₁ : q₁ ∈ C) (h₂ : q₂ ∈ C) :
    activeSupport y q₁ = activeSupport y q₂ := by
  ext i
  rw [mem_activeSupport, mem_activeSupport]
  rcases pos_dichotomy_of_isPreconnected (hy i) (hs i) hC (hstrict i) (hcomp i) with h | h
  · exact ⟨fun _ => h q₂ h₂, fun _ => h q₁ h₁⟩
  · exact ⟨fun h' => absurd h' (h q₁ h₁), fun h' => absurd h' (h q₂ h₂)⟩

/-- **Claim (3), binding multiplicity** `μ = |S*|`. -/
-- Ref: [leitner2026] prop:confinement-phase-stratification
theorem mu_eq_of_isPreconnected {κ : Type*} [Fintype κ]
    (y s : κ → ℝ → ℝ) (hy : ∀ i, Continuous (y i)) (hs : ∀ i, Continuous (s i))
    {C : Set ℝ} (hC : IsPreconnected C)
    (hstrict : ∀ i, ∀ q ∈ C, 0 < y i q ∨ 0 < s i q)
    (hcomp : ∀ i, ∀ q ∈ C, y i q * s i q = 0)
    {q₁ q₂ : ℝ} (h₁ : q₁ ∈ C) (h₂ : q₂ ∈ C) :
    (activeSupport y q₁).card = (activeSupport y q₂).card := by
  rw [activeSupport_eq_of_isPreconnected y s hy hs hC hstrict hcomp h₁ h₂]

/-- **Confinement phase stratification, claims (1) and (3a–b).** The locus
    is open, and on any preconnected subset of it where the dual pair is
    continuous and strictly complementary, the active support and the
    binding multiplicity are constant. -/
-- Ref: [leitner2026] prop:confinement-phase-stratification
theorem ConfinementPhaseStratification [Finite ι] {κ : Type*} [Fintype κ]
    (g : ι → ℝ × E → ℝ) (hg : ∀ i, Continuous (g i))
    (y s : κ → ℝ → ℝ) (hy : ∀ i, Continuous (y i)) (hs : ∀ i, Continuous (s i)) :
    IsOpen (strictLocus g) ∧
    ∀ C ⊆ strictLocus g, IsPreconnected C →
      (∀ i, ∀ q ∈ C, 0 < y i q ∨ 0 < s i q) →
      (∀ i, ∀ q ∈ C, y i q * s i q = 0) →
      ∀ q₁ ∈ C, ∀ q₂ ∈ C,
        activeSupport y q₁ = activeSupport y q₂ ∧
        (activeSupport y q₁).card = (activeSupport y q₂).card :=
  ⟨isOpen_strictLocus g hg, fun _ _ hC hstrict hcomp _ h₁ _ h₂ =>
    ⟨activeSupport_eq_of_isPreconnected y s hy hs hC hstrict hcomp h₁ h₂,
     mu_eq_of_isPreconnected y s hy hs hC hstrict hcomp h₁ h₂⟩⟩

end QOU.BraidKnot
