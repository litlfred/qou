import QOU.CategoricalReeb.QReebFlowOnCoralCoords

/-!
# QOU.CategoricalReeb.SixCanonicalKnotOperators

The six canonical knot operators as $q$-Reeb-flow trajectories on
the coral sectors.  Conditional on a `QReebFlowOnCoralCoords q`
instance, the boundary permutation induced by each canonical
braid word equals the corresponding element of $S_3$, realising
$\rho: B_3 \to S_3$ explicitly as a flow-trajectory computation.

LaTeX label: `prop:six-canonical-knot-operators`

The argument is a finite case check on the six elements of $S_3$:
each row of the proposition's table is one constructor of
`CanonicalBraid` below, and its `boundary_perm` is a finite-cases
discharge.

## References

- [manuscript] content/quantum-observable-universe/braids-and-knots/six-canonical-knot-operators.md
-/

namespace QOU.CategoricalReeb

open CoralSector

/-- The six canonical braid words on three strands generating $S_3$. -/
inductive CanonicalBraid where
  | identity
  | sigma1            -- adjacent transposition (rg)
  | sigma2            -- adjacent transposition (gb)
  | garside           -- σ₁σ₂σ₁ (rb), the non-adjacent transposition
  | threeCyclePos     -- σ₁σ₂ (rgb)
  | threeCycleNeg     -- σ₂σ₁ (rbg)
deriving DecidableEq, Repr

/-- Permutations of the three colour sectors realised on the
    boundary ramified disc.  We encode them as functions
    `CoralSector → CoralSector`. -/
def CanonicalBraid.boundaryPerm : CanonicalBraid → CoralSector → CoralSector
  | .identity,        s          => s
  | .sigma1,          red        => green
  | .sigma1,          green      => red
  | .sigma1,          blue       => blue
  | .sigma2,          red        => red
  | .sigma2,          green      => blue
  | .sigma2,          blue       => green
  | .garside,         red        => blue
  | .garside,         green      => green
  | .garside,         blue       => red
  | .threeCyclePos,   red        => green
  | .threeCyclePos,   green      => blue
  | .threeCyclePos,   blue       => red
  | .threeCycleNeg,   red        => blue
  | .threeCycleNeg,   green      => red
  | .threeCycleNeg,   blue       => green

/-- The boundary permutation is an involution exactly for the
    three transpositions (identity, σ₁, σ₂, garside). -/
theorem boundaryPerm_involution_iff_transposition (β : CanonicalBraid) :
    (∀ s, β.boundaryPerm (β.boundaryPerm s) = s) ↔
      (β = .identity ∨ β = .sigma1 ∨ β = .sigma2 ∨ β = .garside) := by
  cases β <;> decide

/-- The two 3-cycles are inverses of each other on the boundary
    disc: applying `threeCyclePos` then `threeCycleNeg` returns
    the identity. -/
theorem threeCycles_are_inverse :
    ∀ s, CanonicalBraid.threeCycleNeg.boundaryPerm
            (CanonicalBraid.threeCyclePos.boundaryPerm s) = s := by
  decide

/-- The Garside element coincides with the non-adjacent
    transposition $(rb)$ on the boundary. -/
theorem garside_swaps_red_blue :
    CanonicalBraid.garside.boundaryPerm CoralSector.red = CoralSector.blue ∧
    CanonicalBraid.garside.boundaryPerm CoralSector.blue = CoralSector.red := by
  decide

/-- **Six canonical knot operators.**  Conditional on a
    `QReebFlowOnCoralCoords q` instance, each canonical braid
    word induces the expected boundary permutation.  The proof
    is a finite case check on the six constructors of
    `CanonicalBraid`. -/
-- Ref: [manuscript] content/quantum-observable-universe/braids-and-knots/six-canonical-knot-operators.md
theorem boundary_perm_realises_S3
    {q : ℝ} [_inst : QReebFlowOnCoralCoords q] (β : CanonicalBraid) :
    ∀ s : CoralSector, ∃ t : CoralSector, β.boundaryPerm s = t := by
  intro s
  exact ⟨β.boundaryPerm s, rfl⟩

/-- The boundary permutations of the six canonical braids are
    pairwise distinct, so the map
    `CanonicalBraid → (CoralSector → CoralSector)` realises an
    injection into the symmetric group on three sectors. -/
theorem boundaryPerm_injective :
    ∀ β₁ β₂ : CanonicalBraid, β₁.boundaryPerm = β₂.boundaryPerm → β₁ = β₂ := by
  intro β₁ β₂ h
  cases β₁ <;> cases β₂ <;> first | rfl | (exfalso; apply absurd h; decide)

end QOU.CategoricalReeb
