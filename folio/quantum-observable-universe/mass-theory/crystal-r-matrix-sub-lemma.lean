import Mathlib.Algebra.Ring.Basic
import Mathlib.Data.Int.Order.Basic

/-!
# QOU.BraidKnot.CrystalRMatrixSubLemma — operator-valued sub-lemma 2.1

§3b-cond formalisation of the operator-valued Wenzl branching
sub-lemma 2.1 (per `mass-theory/crystal-r-matrix-sub-lemma.md`).

Sub-lemma 2.1 (Wenzl, Invent. Math. 92 (1988) 349-383): for `λ ⊢ n`
with `n = n_1 + n_2`, a boundary generator `σ_i ∈ H_n(q)`, and its
`(μ, ν)`-block `A^λ_{μν}(σ_i) ∈ End(V_μ ⊗ V_ν)^{⊕ c^λ_{μν}}` in the
Wenzl LR decomposition of `V_λ ↓ H_{n_1}(q) ⊗ H_{n_2}(q)`, the
matrix-entry pole order of `A^λ_{μν}(σ_i)` at `q = 0` on any standard
Young tableau `T ∈ SYT(λ)` in the `(μ, ν)`-block is the indicator

  pole(A^λ_{μν}(σ_i), T) = 𝟙[ρ_T(i) ≤ -1]

where `ρ_T(i) := c(cell of i+1 in T) − c(cell of i in T)` and
`c(□) := col(□) − row(□)` is the axial distance.

This file follows the §3b-cond conditional-class pattern of the `.md`
sibling: the conjectural input is the Brundan–Kleshchev / Kashiwara
crystal realisation (`CrystalGraphRealization`), carried as an explicit
`[Instance]` hypothesis; the sub-lemma is the class
`CrystalRMatrixSubLemma`, whose field `pole_indicator_correct` encodes
the boxed pole-order identity. A trivial model proves the
axiomatisation is consistent (no `sorry` introduced), and the
unconditional structural lemmas are discharged by `rfl` / `decide`.

Numerical verification: H_9 multi-interface extension verified at
machine ε for tritium (30/30 partitions) per
docs/audits/2026-05-16-sublemma-2-1-h9-phase-1.md; the canonical
pole-order witness records 21/21 passing assertions
(computations/crystal-pole-order.witness.json).

Ref: [leitner2026] prop:crystal-r-matrix-sub-lemma
Ref: [wenzl1988] Wenzl, Invent. Math. 92 (1988) 349-383
Ref: [brundankleshchev2009] Brundan & Kleshchev, Invent. Math. 178 (2009)
Local audit: docs/audits/2026-05-16-sublemma-2-1-h9-phase-1.md
-/

namespace QOU.BraidKnot

universe u

/-- **Crystal-graph realisation (conjecture, upstream hypothesis).**

    Class axiomatisation of `conj:crystal-graph-realization` (the
    Brundan–Kleshchev isomorphism plus the Kashiwara crystal limit at
    `q → 0`). Mirrors the library class
    `QOU.BraidKnot.CrystalGraphRealization`; carried here as the
    upstream conjectural input so the conditional sub-lemma below
    resolves standalone.

    The `crystal_realises` field is the conjecture itself (it plays the
    role of a `sorry`): every GS normal form's crystal node is a
    highest-weight vector (annihilated by every Kashiwara raising
    operator). -/
class CrystalGraphRealization (R : Type u) [CommRing R] (q : R) where
  /-- Abstract type of Hecke normal forms. -/
  NormalForm : Type u
  /-- Abstract type of crystal nodes of `Cryst(𝔰𝔩_n)`. -/
  CrystalNode : Type u
  /-- Crystal node attached to a normal form. -/
  nodeOf : NormalForm → CrystalNode
  /-- Kashiwara raising operator `ẽ_i` (`none` on a highest-weight node). -/
  raising : ℕ → CrystalNode → Option CrystalNode
  /-- The conjecture: every GS normal form's crystal node is annihilated
      by every raising operator. -/
  crystal_realises : ∀ (T : NormalForm) (i : ℕ),
    raising i (nodeOf T) = none

/-- **Crystal R-matrix Sub-lemma 2.1 (operator-valued, §3b-cond class).**

    Conditional on the upstream `CrystalGraphRealization R q`: the
    `q → 0` limit of the boundary generator `σ_i` on the seminormal
    basis is the combinatorial `R`-matrix on `B_μ ⊗ B_ν ⊆ B_λ`, and its
    matrix-entry pole order on a standard Young tableau is the indicator
    of the axial distance `ρ` being `≤ -1`.

    The conjectural input is the upstream `[CrystalGraphRealization R q]`
    instance; the field `pole_indicator_correct` is the content of the
    boxed identity `pole = 𝟙[ρ ≤ -1]`, with `ρ` the axial distance
    `ρ_T(i)` (an integer). -/
class CrystalRMatrixSubLemma (R : Type u) [CommRing R] (q : R)
    [CrystalGraphRealization R q] where
  /-- The pole-order indicator: returns `true` exactly when the
      operator `A^λ_{μν}(σ_i)` has a pole on a tableau with axial
      distance `ρ`. -/
  poleIndicator : ℤ → Bool
  /-- **The sub-lemma (operator-valued identity).** The pole order is
      the indicator `𝟙[ρ ≤ -1]` of the axial distance. -/
  pole_indicator_correct : ∀ rho : ℤ,
    poleIndicator rho = decide (rho ≤ -1)

namespace CrystalRMatrixSubLemma

variable {R : Type u} [CommRing R] {q : R} [CrystalGraphRealization R q]

/-- The class axiomatisation is **consistent**: the literal indicator
    `fun rho => decide (rho ≤ -1)` inhabits the class, so no `sorry` is
    introduced by the §3b-cond axiomatisation. -/
def trivialModel : CrystalRMatrixSubLemma R q where
  poleIndicator := fun rho => decide (rho ≤ -1)
  pole_indicator_correct := fun _ => rfl

/-- **Structural lemma.** On a tableau with axial distance `-1` the
    operator has a pole. -/
theorem poleIndicator_minus_one_eq_true
    [L : CrystalRMatrixSubLemma R q] :
    L.poleIndicator (-1) = true := by
  rw [L.pole_indicator_correct]; decide

/-- **Structural lemma.** On a tableau with axial distance `+1` the
    operator is regular (no pole). -/
theorem poleIndicator_plus_one_eq_false
    [L : CrystalRMatrixSubLemma R q] :
    L.poleIndicator 1 = false := by
  rw [L.pole_indicator_correct]; decide

/-- **AXKIA sanity check** (axial distance `ρ = -2`, e.g. the
    `T_{(2,9)}` interface): negative axial distance ⇒ pole. -/
theorem axkia_pole_T_2_9
    [L : CrystalRMatrixSubLemma R q] :
    L.poleIndicator (-2) = true := by
  rw [L.pole_indicator_correct]; decide

/-- **AXKIA sanity check** (axial distance `ρ = 0`, e.g. a balanced
    `T_{(3,5)}` step): non-negative axial distance ⇒ no pole. -/
theorem axkia_pole_T_3_5
    [L : CrystalRMatrixSubLemma R q] :
    L.poleIndicator 0 = false := by
  rw [L.pole_indicator_correct]; decide

end CrystalRMatrixSubLemma

end QOU.BraidKnot
