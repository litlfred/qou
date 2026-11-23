/-
Copyright (c) 2026 litlfred. All rights reserved.
Released under Apache 2.0 license.
-/
import Mathlib.RingTheory.Kaehler.Basic
import Mathlib.LinearAlgebra.SymmetricAlgebra.Basic

/-!
# The tangent algebra `Sym_S(Ω¹)` splits over `S` (owner ruling 2026-11-22, second card)

The brane tower's level object is the tangent algebra `T(S) = Sym_S(Ω[S⁄R])`, the coordinate
ring of the tangent bundle. It replaces `(S ⊗ S)/I²`, which carries no compatible bialgebra
in characteristic zero (`QOU.LiftingDescent.jet_polynomial_no_bialgebra`).

* `tangentSection : S →ₐ[R] T(S)` is the structure map (pull-back along `TX → X`).
* `tangentRetract : T(S) →ₐ[R] S` sends `Ω` to `0` (pull-back along the zero section).
* `tangentRetract_comp_tangentSection`: `r ∘ ℓ = id`, so `S` is a direct summand of `T(S)`.

Not formalised here: for a commutative Hopf algebra `S = 𝒪(G)`, `T(S) = 𝒪(TG)` is a Hopf
algebra (the tangent group `TG = G ⋉ 𝔤`) and both maps are Hopf maps. That is cited, not proved.

No `sorry`, no axiom beyond Lean's three.

## References
- [leitner2026] §3 Lifting and Descent
-/

namespace QOU.LiftingDescent

variable (R S : Type*) [CommRing R] [CommRing S] [Algebra R S]

/-- The tangent algebra `T(S) = Sym_S(Ω[S⁄R])`. -/
abbrev tangentAlgebra : Type _ := SymmetricAlgebra S (Ω[S⁄R])

/-- Section `ℓ : S → T(S)`, the structure map. -/
noncomputable def tangentSection : S →ₐ[R] tangentAlgebra R S :=
  (IsScalarTower.toAlgHom R S (tangentAlgebra R S))

/-- Retraction `r : T(S) → S`, killing `Ω`. -/
noncomputable def tangentRetract : tangentAlgebra R S →ₐ[R] S :=
  (SymmetricAlgebra.algebraMapInv (R := S) (M := Ω[S⁄R])).restrictScalars R

/-- **`S` is a direct summand of `T(S)`**: `r ∘ ℓ = id`. -/
theorem tangentRetract_comp_tangentSection :
    (tangentRetract R S).comp (tangentSection R S) = AlgHom.id R S := by
  ext a
  exact SymmetricAlgebra.algebraMap_leftInverse (R := S) (M := Ω[S⁄R]) a

/-- The retraction kills the generators `ι(ω)`. -/
theorem tangentRetract_ι (ω : Ω[S⁄R]) :
    tangentRetract R S (SymmetricAlgebra.ι S (Ω[S⁄R]) ω) = 0 := by
  simp [tangentRetract, SymmetricAlgebra.algebraMapInv]

end QOU.LiftingDescent
