import QOU.KnotTheory.Vassiliev.ChordDiagram
import QOU.KnotTheory.Vassiliev.FourTermRelation
import QOU.KnotTheory.Vassiliev.WeightSystem
import QOU.KnotTheory.Vassiliev.FiniteTypeInvariant
import QOU.KnotTheory.Vassiliev.MilnorVassilievBridge

/-!
# QOU.KnotTheory.Vassiliev — finite-type (Vassiliev) invariant scaffold

Foundational finite-type invariant infrastructure, aimed at eventually
formalizing the Milnor = leading-Vassiliev bridge that the general exact-order
Milnor conjecture (#4471, `QOU.MassTheory.MilnorParitySignLaw`) requires.

* `ChordDiagram` — chord diagrams (fixed-point-free involutions) + the
  symmetric-group relabelling action. **sorry-free.**
* `FourTermRelation` — the free module on chord diagrams with the 1T (framing)
  and 4T (four-term) relations. **sorry-free.**
* `WeightSystem` — linear functionals on the 4T-quotient `𝒜`. **sorry-free.**
* `FiniteTypeInvariant` — the Vassiliev order filtration and symbol map.
  **sorry-free.**
* `MilnorVassilievBridge` — the deep theorems (Kontsevich universality; the
  Milnor = leading-Vassiliev bridge) as **honest content-bearing conjecture
  classes** (§3b-tax, no instance, NOT axiomatized), with the conditional
  exact-order result hooking to #4471.
-/
