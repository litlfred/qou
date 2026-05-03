import QOU.BraidKnot.ConfinementLevel
import Mathlib.Algebra.Field.Basic

/-!
# QOU.BraidKnot.GradedTraceResidueSplit — graded-trace residue split

The Markov trace on the filtered Hecke algebra `H_n(q)` decomposes
canonically as

    tr_M(T_w) = tr_gr(σ(T_w)) + Res_GB(T_w)

where `σ` is the symbol map to the associated graded algebra and
`Res_GB` is the sum of rewriting-defect residues at root-of-unity
poles.  Filtered-algebra analogue of Strutinsky's smooth-plus-
oscillating nuclear-energy decomposition.

**Pre-Archimedean.** Polymorphic in the ground field `R`; the
opaque trace declarations carry `q : R` and return values in `R`,
not `ℝ`.  Per `QOU.GroundRingAnnotations`, this stub is in the
formal pre-Arch chain.

**Formal-chain version.**  Lives under `lean/QOU/` and is compiled
by `lake build`.  The co-located documentation stub at
`braids-and-knots/graded-trace-residue-split.lean` mirrors this.

LaTeX label: `prop:graded-trace-residue-split`
-/

namespace QOU.BraidKnot

universe u

/-- The symbol map `σ: J^ℓ → J^ℓ/J^{ℓ+1}` on the confinement
    filtration.  Polymorphic in the ground field `R`.  Axiomatised. -/
noncomputable opaque GradedTraceResidueSplit.symbolMap
    {R : Type u} [Field R] (ℓ : ℕ) (q : R) : Unit → Unit

/-- The Markov trace on the associated graded algebra `gr H_n(q)`.
    Smooth / Strutinsky-macroscopic piece. Valued in `R`. -/
noncomputable opaque GradedTraceResidueSplit.gradedTrace
    {R : Type u} [Field R] (q : R) (x : Unit) : R

/-- The total residue contribution from GB rewriting defects at
    root-of-unity poles. Oscillating / Strutinsky-shell piece.
    Valued in `R`. -/
noncomputable opaque GradedTraceResidueSplit.gbResidue
    {R : Type u} [Field R] (q : R) (x : Unit) : R

/-- The full Markov trace on `H_n(q)`, valued in `R`. -/
noncomputable opaque GradedTraceResidueSplit.markovTrace
    {R : Type u} [Field R] (q : R) (x : Unit) : R

/-- **Graded-trace residue split.**  Polymorphic in the ground field `R`.

    The Markov trace decomposes as smooth (graded) + oscillating
    (residue), the categorical analogue of Strutinsky's
    macroscopic + shell-correction split. -/
class GradedTraceResidueSplit (R : Type u) [Field R] where
  q : R
  element : Unit
  smooth : R       -- tr_gr(σ(element), q)
  oscillating : R  -- Res_GB(element, q)
  total : R        -- tr_M(element, q)
  split_identity :
    total = smooth + oscillating
  smooth_is_graded :
    smooth = GradedTraceResidueSplit.gradedTrace q element
  oscillating_is_residue :
    oscillating = GradedTraceResidueSplit.gbResidue q element

/-- Level-0 case: when oscillating residue vanishes, total = smooth.
    This recovers the pure-descended regime.

    Ref: [manuscript] `prop:categorical-mass-markov`. -/
theorem GradedTraceResidueSplit.level_zero_pure_descended
    {R : Type u} [Field R] (S : GradedTraceResidueSplit R)
    (h : S.oscillating = 0) :
    S.total = S.smooth := by
  rw [S.split_identity, h, add_zero]

/-- The graded-trace residue split is the algebraic shadow of
    Strutinsky's `E = Ẽ + δE_shell`.

    Ref: [manuscript] §Nuclear Binding and Beta Stability. -/
theorem GradedTraceResidueSplit.strutinsky_analogue
    {R : Type u} [Field R] (S : GradedTraceResidueSplit R) :
    S.total = S.smooth + S.oscillating :=
  S.split_identity

/-- **Graded trace residue split proposition.**  Conditional on a
    `[GradedTraceResidueSplit R]` instance, the split identity
    holds. -/
-- Ref: [manuscript] `prop:graded-trace-residue-split`
theorem graded_trace_residue_split
    {R : Type u} [Field R] [s : GradedTraceResidueSplit R] :
    s.total = s.smooth + s.oscillating :=
  s.split_identity

end QOU.BraidKnot
