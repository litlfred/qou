-- The library used to discharge its own §3b-cond hypotheses GLOBALLY.
--
-- No instance is declared here, so nothing below can be blamed on the probe's
-- own construction. This file records the BEFORE state as comments (measured,
-- not recalled) and ASSERTS the after state, so it fails if the demotion is
-- ever reverted.

import QOU.Mathlib.HeckeAlgebra

namespace TrivialGlobalInstanceProbe

open QOU.Mathlib.HeckeAlgebra

/-! ## Before (2026-08-23, measured)

`HeckeAlgebra.lean` declared

    instance triv_hecke (R : Type u) [CommRing R] (n : N) (q : R) :
        IwahoriHeckeAlgebra R n q where
      carrier := PUnit
      hecke_relation := True ; braid_relation := True ; far_commute := True

so resolution supplied it for EVERY `R`, `n`, `q`:

    #synth IwahoriHeckeAlgebra Z 3 1                    -->  triv_hecke Z 3 1
    #synth WedderburnDecomposition Z 3 1                -->  triv_wedderburn Z 3 1
    (inferInstance : IwahoriHeckeAlgebra Z 3 1).carrier = PUnit   -- closed by rfl

Two steps of the canonical derivation chain therefore had inert Lean
hypotheses: every `[IwahoriHeckeAlgebra ...]` was discharged behind the
caller's back, with the carrier pinned to `PUnit`.

`triv_hecke`'s own docstring said why it existed -- "Discharges the §3b-cond
hypothesis at the audit level" -- which is what §3b-tax forbids: an unproved
primary is honestly represented by a content-bearing class with NO instance.
The defect was not the placeholder but its globality. -/

/-! ## A second defect, in the same lines, closed later

The `hecke_relation := True ; braid_relation := True ; far_commute := True` in
the BEFORE block above records more than the globality this probe was about:
those three were `Prop` FIELDS, so `triv_hecke` was choosing what the relations
meant, not satisfying them. This probe did not claim otherwise -- it was
scoped to globality -- but a reader can easily take the quoted lines as
incidental syntax rather than as a second finding sitting in plain sight.

Closed 2026-09-07: the three are now equations in the class's own `mul`,
`smul`, `one` and `sigma`. `triv_hecke` survives the change and discharges them
by `Subsingleton.elim`, which is honest -- `PUnit` is the zero algebra, where
every equation between elements holds. What changed is that this is now a
*consequence* of the model rather than a choice the model made.

Everything below is unaffected: it tests resolution, not the relations, and
`triv_hecke` is still the trivial model, still a `def`. -/

/-! ## After: both are `def`s, so nothing is supplied silently -/

-- Neither of these type-checks any more, which is the point. Uncommenting
-- either should fail with "failed to synthesize"; that is the regression test.
--
--   example : IwahoriHeckeAlgebra ℤ 3 (1 : ℤ) := inferInstance
--   example : WedderburnDecomposition ℤ 3 (1 : ℤ) := inferInstance

-- The trivial model remains available -- deliberately, by name.
example : IwahoriHeckeAlgebra ℤ 3 (1 : ℤ) := triv_hecke ℤ 3 1

-- And a conditional theorem is now genuinely conditional: this states nothing
-- until a caller supplies a Hecke model, rather than resolving to `PUnit`.
theorem conditional_needs_a_model {R : Type} [CommRing R] {n : ℕ} {q : R}
    [IwahoriHeckeAlgebra R n q] (P : Prop) (hP : P) : P := hP

-- Supplying it explicitly is what a caller must now do.
example (P : Prop) (hP : P) : P :=
  @conditional_needs_a_model ℤ _ 3 1 (triv_hecke ℤ 3 1) P hP

end TrivialGlobalInstanceProbe
