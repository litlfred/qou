import QOU.CategoricalReeb.QReebFlowOnColorCoords

/-!
# QOU.CategoricalReeb.SixCanonicalKnotOperators

The six canonical knot operators as $q$-Reeb-flow trajectories on
the color sectors.  Conditional on a `QReebFlowOnColorCoords q`
instance, the boundary permutation induced by each canonical
braid word equals the corresponding element of $S_3$, realising
$\rho: B_3 \to S_3$ explicitly as a flow-trajectory computation.

LaTeX label: `prop:six-canonical-knot-operators`

The argument is a finite case check on the six elements of $S_3$:
each row of the proposition's table is one constructor of
`CanonicalBraid` below, and its `boundaryPerm` is a finite-cases
discharge.

## References

- [leitner2026] folio/quantum-observable-universe/braids-and-knots/six-canonical-knot-operators.md
-/

namespace QOU.CategoricalReeb

open ColorSector

/-- The six canonical braid words on three strands generating $S_3$. -/
inductive CanonicalBraid where
  | identity
  | sigma1            -- adjacent transposition (rg)
  | sigma2            -- adjacent transposition (gb)
  | garside           -- σ₁σ₂σ₁ (rb), the non-adjacent transposition
  | threeCyclePos     -- σ₁σ₂ (rgb)
  | threeCycleNeg     -- σ₂σ₁ (rbg)
deriving DecidableEq, Repr

/-- The list of all six canonical braid constructors. -/
def CanonicalBraid.all : List CanonicalBraid :=
  [.identity, .sigma1, .sigma2, .garside, .threeCyclePos, .threeCycleNeg]

theorem CanonicalBraid.all_length :
    CanonicalBraid.all.length = 6 := rfl

theorem CanonicalBraid.all_nodup :
    CanonicalBraid.all.Nodup := by decide

/-- Permutations of the three colour sectors realised on the
    boundary ramified disc.  We encode them as functions
    `ColorSector → ColorSector`. -/
def CanonicalBraid.boundaryPerm : CanonicalBraid → ColorSector → ColorSector
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

/-- `boundaryPerm β` is a bijection on the three-element type
    `ColorSector` for every canonical braid `β`. -/
theorem boundaryPerm_bijective (β : CanonicalBraid) :
    Function.Bijective β.boundaryPerm := by
  refine ⟨?_, ?_⟩
  · -- Injectivity: a finite check over the 3×3 colour pairs for each of the
    -- six braids.  After casing, `boundaryPerm` reduces to a concrete colour
    -- and the hypothesis `h` to a concrete colour equality; `simp_all`
    -- closes the diagonal (`rfl`) cases and rules out the off-diagonal ones
    -- by `ColorSector` no-confusion (no contradictory-premise discharge).
    intro s₁ s₂ h
    cases β <;> cases s₁ <;> cases s₂ <;> simp_all [CanonicalBraid.boundaryPerm]
  · -- Surjectivity: exhibit a preimage colour for each target.
    intro s
    cases β <;> cases s <;>
      (first
        | (exact ⟨ColorSector.red,   by decide⟩)
        | (exact ⟨ColorSector.green, by decide⟩)
        | (exact ⟨ColorSector.blue,  by decide⟩))

/-- The boundary permutation is an involution exactly for the
    identity element and the three transpositions
    ($\sigma_1$, $\sigma_2$, garside). -/
theorem boundaryPerm_involution_iff_transposition (β : CanonicalBraid) :
    (∀ s, β.boundaryPerm (β.boundaryPerm s) = s) ↔
      (β = .identity ∨ β = .sigma1 ∨ β = .sigma2 ∨ β = .garside) := by
  constructor
  · intro h
    cases β
    case identity        => exact Or.inl rfl
    case sigma1          => exact Or.inr (Or.inl rfl)
    case sigma2          => exact Or.inr (Or.inr (Or.inl rfl))
    case garside         => exact Or.inr (Or.inr (Or.inr rfl))
    case threeCyclePos   => exfalso; have := h ColorSector.red; cases this
    case threeCycleNeg   => exfalso; have := h ColorSector.red; cases this
  · intro h s
    rcases h with h | h | h | h <;> subst h <;> cases s <;> rfl

/-- The two 3-cycles are inverses of each other on the boundary
    disc: applying `threeCyclePos` then `threeCycleNeg` returns
    the identity. -/
theorem threeCycles_are_inverse :
    ∀ s, CanonicalBraid.threeCycleNeg.boundaryPerm
            (CanonicalBraid.threeCyclePos.boundaryPerm s) = s := by
  intro s
  cases s <;> rfl

/-- The Garside element coincides with the non-adjacent
    transposition $(rb)$ on the boundary. -/
theorem garside_swaps_red_blue :
    CanonicalBraid.garside.boundaryPerm ColorSector.red = ColorSector.blue ∧
    CanonicalBraid.garside.boundaryPerm ColorSector.blue = ColorSector.red := by
  decide

/-- The boundary permutations of the six canonical braids are
    pairwise distinct, so the map
    `CanonicalBraid → (ColorSector → ColorSector)` realises an
    injection into the symmetric group on three sectors. -/
theorem boundaryPerm_injective :
    Function.Injective CanonicalBraid.boundaryPerm := by
  intro β₁ β₂ h
  -- For distinct constructors the two boundary permutations disagree on at
  -- least one colour sector; evaluating the function equality `h` at the red
  -- and green witnesses (`congrFun`) yields a concrete colour equality that
  -- `simp_all` resolves — diagonal cases by `rfl`, off-diagonal by
  -- `ColorSector` no-confusion.  (Function equality is not decidable, so we
  -- evaluate at witnesses rather than `decide`-ing the functions.)
  cases β₁ <;> cases β₂ <;>
    first
      | rfl
      | (have hr := congrFun h ColorSector.red
         have hg := congrFun h ColorSector.green
         simp_all [CanonicalBraid.boundaryPerm])

/-- The number of distinct boundary permutations realised by the
    six canonical braids is exactly $6 = |S_3|$.  Together with
    `boundaryPerm_bijective`, this shows the canonical braids
    realise all six elements of the symmetric group on three
    color sectors. -/
theorem canonical_braid_count_six :
    CanonicalBraid.all.length = 6 ∧ CanonicalBraid.all.Nodup :=
  ⟨CanonicalBraid.all_length, CanonicalBraid.all_nodup⟩

/-- **Six canonical knot operators realise $S_3$.**

    The six canonical braid words map to six distinct bijections
    of `ColorSector`, exhausting the six elements of the
    symmetric group on three sectors.  This is the combinatorial
    boundary-permutation content of
    `prop:six-canonical-knot-operators`; the geometric
    identification of these permutations with the boundary
    footprints of the $q$-Reeb flow trajectories (which DOES
    consume the `QReebFlowOnColorCoords q` class) lives in the
    manuscript prose, not in this theorem. -/
-- Ref: [leitner2026] folio/quantum-observable-universe/braids-and-knots/six-canonical-knot-operators.md
theorem boundary_perm_realises_S3 :
    Function.Injective CanonicalBraid.boundaryPerm ∧
    (∀ β : CanonicalBraid, Function.Bijective β.boundaryPerm) ∧
    (CanonicalBraid.all.length = 6 ∧ CanonicalBraid.all.Nodup) :=
  ⟨boundaryPerm_injective, boundaryPerm_bijective, canonical_braid_count_six⟩

end QOU.CategoricalReeb
