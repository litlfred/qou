/-!
# QOU.BraidKnot.LightNucleus

The light-nucleus enumeration `{²H, ³H, ³He}` and associated
mass-number / strand-count utility functions.  Mirrors the type
defined in the content-block file
`content/quantum-observable-universe/braids-and-knots/conj-canonical-knot-id-sdp.lean`
so it can be referenced from Lake-tracked modules.

(The content-block file is read but not Lake-built; this module
exposes the same API for use by Lake-tracked downstream
modules.)
-/

import Mathlib.Tactic

namespace QOU.BraidKnot

/-- **Light-nucleus enumeration** for the canonical knot
    identification: deuteron (²H = 6_2), tritium (³H = 8_11),
    helium-3 (³He = L_6a4). -/
inductive LightNucleus : Type where
  | deuterium
  | tritium
  | helium3
deriving DecidableEq, Repr

/-- The atomic mass number `A` of a `LightNucleus`. -/
def LightNucleus.A : LightNucleus → ℕ
  | .deuterium => 2
  | .tritium   => 3
  | .helium3   => 3

/-- The atomic strand count `n_0 = 3 · A`. -/
def LightNucleus.n₀ (n : LightNucleus) : ℕ := 3 * n.A

/-- The number of constituents (nucleons). -/
def LightNucleus.numConstituents (n : LightNucleus) : ℕ := n.A

/-- Strand count is positive (A ≥ 2 ⟹ n_0 ≥ 6). -/
theorem LightNucleus.n₀_pos (n : LightNucleus) : 0 < n.n₀ := by
  cases n <;> decide

/-- The mass-number `A` is at least 2 for every light nucleus. -/
theorem LightNucleus.A_ge_two (n : LightNucleus) : 2 ≤ n.A := by
  cases n <;> decide

/-- The strand count `n_0` is at least 6 (the minimum for a binding
    operation between two trefoils, each on 3 strands). -/
theorem LightNucleus.n₀_ge_six (n : LightNucleus) : 6 ≤ n.n₀ := by
  cases n <;> decide

end QOU.BraidKnot
