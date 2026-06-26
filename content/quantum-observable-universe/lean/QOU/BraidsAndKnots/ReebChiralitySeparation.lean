/-
  Reeb-Casimir level ⊕ chirality separates the five A₅ irreps.

  Formalises the step-3 finding of the keystone "look-to-Reeb" probe
  (`computations/keystone_reeb_casimir_chirality_step3.py`, merged in PR #2531):

    * the Reeb-spin eigenvalue, pulled back to the A₅ irreps via the SO(3)
      tower as the Casimir `ℓ(ℓ+1)` at first appearance (`icosBranchingMult`,
      `S5SO3FiberAction.lean`), takes values A:0, T₁:2, H:6, T₂:12, G:12 —
      so it is NOT injective (T₂, G collide at ℓ = 3, Casimir 12);
    * the chirality (the self-conjugate (3,1,1) = T₁ ⊕ T₂ split, the only
      chirality-bearing pair) separates that collision;
    * hence the COMPOSITE `(Reeb-Casimir level, chirality)` IS injective —
      it separates all five A₅ irreps.

  This is the on-main-grounded structure of `BringFiberAction.five_distinct_classes`
  (the substantive field of the conjectural fibre map): the five distinct
  rotation "classes" are realised by the (level, chirality) composite, with the
  level canonical from `icosBranchingMult` and the chirality from the
  conjugation/parity structure already in `S5SO3FiberAction.lean`.  It does NOT
  supply the geometric `irrepToRotation` ANGLES — those remain owner-gated
  (Seifert-S¹ Reeb weights; `conj:s5-so3-fiber-action`) — only the separation
  the substantive field asserts.

  Unconditional, sorry-free; does not depend on `BringFiberAction`.

  -- Ref: [klein1884vorlesungen] Klein, Lectures on the Icosahedron
-/
import QOU.BraidsAndKnots.S5SO3FiberAction

namespace QOU.BraidsAndKnots

/-- First angular-momentum level at which each A₅ irrep appears in the SO(3)
    tower, read off `icosBranchingMult` (A@0, T₁@1, H@2, T₂@3, G@3). -/
def A5Irrep.firstEll : A5Irrep → ℕ
  | .A => 0 | .T₁ => 1 | .H => 2 | .T₂ => 3 | .G => 3

/-- The `firstEll` value is grounded in `icosBranchingMult`: each irrep's
    multiplicity entry is nonzero at its `firstEll` (and the table is the
    derived I-character branching).  Entry order is [A, T₁, T₂, G, H]. -/
theorem A5Irrep.firstEll_appears :
    (icosBranchingMult (A5Irrep.A.firstEll)).get! 0 = 1 ∧
    (icosBranchingMult (A5Irrep.T₁.firstEll)).get! 1 = 1 ∧
    (icosBranchingMult (A5Irrep.H.firstEll)).get! 4 = 1 ∧
    (icosBranchingMult (A5Irrep.T₂.firstEll)).get! 2 = 1 ∧
    (icosBranchingMult (A5Irrep.G.firstEll)).get! 3 = 1 := by
  decide

/-- Reeb-spin Casimir at first appearance: `ℓ(ℓ+1)` (classical limit of the
    content-Casimir `μ_λ`). -/
def A5Irrep.reebCasimir (r : A5Irrep) : ℕ := r.firstEll * (r.firstEll + 1)

/-- Chirality of each A₅ irrep: the T₁/T₂ pair (the self-conjugate (3,1,1)
    split) carries `±1`; the others are chirality-neutral. -/
def A5Irrep.chirality : A5Irrep → ℤ
  | .T₁ => 1 | .T₂ => -1 | _ => 0

/-- **The Reeb level alone does NOT separate the five irreps.**  T₂ and G both
    first appear at ℓ = 3, so both have Casimir 12. -/
theorem A5Irrep.reebCasimir_not_injective :
    ¬ Function.Injective A5Irrep.reebCasimir := by
  intro h
  have : A5Irrep.T₂ = A5Irrep.G := h (by decide)
  exact absurd this (by decide)

/-- The composite key: (Reeb-Casimir level, chirality). -/
def A5Irrep.reebChiralityKey (r : A5Irrep) : ℕ × ℤ := (r.reebCasimir, r.chirality)

/-- **Reeb level ⊕ chirality SEPARATES the five A₅ irreps** (the composite key
    is injective).  The chirality `±1` breaks the T₂/G Casimir-12 degeneracy
    that the level alone leaves; all other pairs are already separated by the
    level.  This realises the `five_distinct_classes` separation from on-main
    canonical data, with no geometric angle input. -/
theorem A5Irrep.reebChiralityKey_injective :
    Function.Injective A5Irrep.reebChiralityKey := by
  intro a b h
  cases a <;> cases b <;> simp_all [A5Irrep.reebChiralityKey, A5Irrep.reebCasimir,
    A5Irrep.firstEll, A5Irrep.chirality]

/-- The five keys are pairwise distinct (the explicit witness list). -/
theorem A5Irrep.reebChiralityKey_values :
    A5Irrep.A.reebChiralityKey = (0, 0) ∧
    A5Irrep.T₁.reebChiralityKey = (2, 1) ∧
    A5Irrep.H.reebChiralityKey = (6, 0) ∧
    A5Irrep.T₂.reebChiralityKey = (12, -1) ∧
    A5Irrep.G.reebChiralityKey = (12, 0) := by
  decide

end QOU.BraidsAndKnots
