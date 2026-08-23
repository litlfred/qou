-- The library discharges its own §3b-cond hypotheses GLOBALLY.
--
-- No instance of mine is declared here. Everything below is answered by the
-- corpus as it stands, so nothing can be blamed on the probe's construction.

import QOU.Mathlib.HeckeAlgebra

namespace TrivialGlobalInstanceProbe

open QOU.Mathlib.HeckeAlgebra

/-! ## 1. The Hecke algebra hypothesis is discharged by the library -/

-- Typeclass resolution supplies the instance, for arbitrary `R`, `n`, `q`.
example : IwahoriHeckeAlgebra ℤ 3 (1 : ℤ) := inferInstance

-- It finds `triv_hecke ℤ 3 1` (declared `instance` in HeckeAlgebra.lean,
-- with `carrier := PUnit` and all three relations `:= True`).
#synth IwahoriHeckeAlgebra ℤ 3 (1 : ℤ)

-- And the carrier really is `PUnit` -- `rfl`, not inspection.
example : (inferInstance : IwahoriHeckeAlgebra ℤ 3 (1 : ℤ)).carrier = PUnit := rfl

/-! ## 2. So is the Wedderburn decomposition -/

example : WedderburnDecomposition ℤ 3 (1 : ℤ) := inferInstance
#synth WedderburnDecomposition ℤ 3 (1 : ℤ)

/-! ## 3. Consequence: every such hypothesis is inert

A theorem conditioned on "being a Hecke algebra" is unconditional -- the
instance argument is supplied by the library at every call site, so it
contributes nothing to the proof term. -/

theorem conditional_is_unconditional {R : Type} [CommRing R] {n : ℕ} {q : R}
    [IwahoriHeckeAlgebra R n q] (P : Prop) (hP : P) : P := hP

example (P : Prop) (hP : P) : P :=
  conditional_is_unconditional (R := ℤ) (n := 3) (q := 1) P hP

end TrivialGlobalInstanceProbe
