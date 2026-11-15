import Mathlib.Tactic

/-!
# QOU.BraidKnot.InterfaceComposition

**Canonical declaration** for content block at
[`quantum-observable-universe/mass-theory/canonical-braid-interface-composition.ts`](quantum-observable-universe/mass-theory/canonical-braid-interface-composition.ts).

Formalises the manuscript interface-composition table: the `pp`/`pn`/`nn`
adjacent-interface counts for the three nucleon orderings — canonical
(`pppnnn`), alternating (`pnpn`), paired (`ppnn`). The canonical and paired
orderings share the profile `(1,1,1)`; the alternating ordering is the
outlier `(0,3,0)`.
-/

namespace QOU.BraidKnot

/-- The three nucleon orderings tabulated in the manuscript. -/
inductive NucleonOrdering
  | canonical   -- pppnnn
  | alternating -- pnpn
  | paired      -- ppnn
deriving DecidableEq

namespace InterfaceComposition

/-- Proton–proton interface count `n_pp`. -/
def n_pp : NucleonOrdering → ℕ
  | .canonical => 1
  | .alternating => 0
  | .paired => 1

/-- Proton–neutron interface count `n_pn`. -/
def n_pn : NucleonOrdering → ℕ
  | .canonical => 1
  | .alternating => 3
  | .paired => 1

/-- Neutron–neutron interface count `n_nn`. -/
def n_nn : NucleonOrdering → ℕ
  | .canonical => 1
  | .alternating => 0
  | .paired => 1

/-- The interface profile `(n_pp, n_pn, n_nn)`. -/
def profile (o : NucleonOrdering) : ℕ × ℕ × ℕ := (n_pp o, n_pn o, n_nn o)

/-- The canonical and paired orderings have the identical interface
    profile `(1,1,1)`. -/
theorem canonical_profile_eq_paired :
    profile NucleonOrdering.canonical = profile NucleonOrdering.paired := rfl

/-- The alternating ordering is the outlier: its profile differs from the
    canonical one. -/
theorem alternating_profile_ne_canonical :
    profile NucleonOrdering.alternating ≠ profile NucleonOrdering.canonical := by
  decide

end InterfaceComposition

-- Ref: [leitner2026] quantum-observable-universe/mass-theory/canonical-braid-interface-composition.ts

/-- Placeholder carrier retained so the `lean.ref` URI
    `qou:QOU.BraidKnot.InterfaceComposition` resolves; the tabulated content
    lives in the `InterfaceComposition` namespace above. -/
structure InterfaceComposition where
  /-- The nucleon ordering this interface record describes. -/
  ordering : NucleonOrdering

end QOU.BraidKnot
