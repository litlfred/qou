import QOU.QBeta.AomegaM2BPSCohomology

set_option autoImplicit false

/-!
# QOU.QBeta.RouteCM3CategoryIdentification — M3 as a content-bearing conjecture class

Route C's M3 rung (`qou-rtec`, D2 of the 2026-08-15 attack-options ledger):
the **identification** of a genuine closed-sector 3-CY categorical datum for
`T[K]` whose chirality-graded DT/BPS output reproduces the certified M2
spectrum. Post-`d999b21d7` this is exactly what is NOT yet established: M2
(`AomegaM2BPSCohomology`) is a *conditional structural characterization* —
taking the eq-(98) constants as DT invariants, the putative BPS spectrum
would be abelian — it does **not** construct a `(Q,W)`, compute a cohomology
from a category, or derive `A_ω`.

## Conjecture taxonomy (AGENTS.md §3b)

**Primary conjecture** (no other conjecture-class binder in the signature —
the classification is derived from the type). The class is content-bearing:
its fields pin the categorical datum's chirality-graded output to the
certified M2 integers, which is falsifiable — a candidate category whose
output misses `{3,4}` refutes its instance. **No instance is provided**: an
instance IS the conjecture's resolution, and constructing one from
Hecke/Bring data is the M1 rung (`qou-q9ih`). Per the anti-laundering rule a
quiver *fitted* to the integers may inhabit a `Candidate` wrapper in its own
file, never this class, whose docstring contract is "constructed from
Hecke/Bring data, not fitted".

LaTeX context: `docs/audits/2026-08-11-route-c-bps-cohomology-scoping.md`.

## References

- [kontsevich-soibelman2008] Kontsevich & Soibelman, "Stability structures,
  motivic Donaldson–Thomas invariants and cluster transformations."
  https://arxiv.org/abs/0811.2435
- [davison-meinhardt2020] Davison & Meinhardt, "Cohomological Donaldson–Thomas
  theory of a quiver with potential and quantum enveloping algebras."
  https://doi.org/10.1007/s00222-020-00961-y
- [leitner2026] docs/audits/2026-08-14-aomega-to-S-bridge-refuted-O2-negative.md (M2 scope).
-/

namespace QOU.QBeta.RouteCM3CategoryIdentification

open QOU.QBeta.AomegaM2BPSCohomology

universe u

/-- **M3 (primary conjecture).** The closed-sector categorical datum `C`
carries a chirality-graded DT output (`true` = the `S⁺` sector, `false` =
`S⁻`) that reproduces the certified M2 spectrum. Content-bearing: the two
equations are the conjecture's falsifiable claims about `C`; an instance
exists iff the identification holds for `C`. (Carries the `dtOutput` data
field, so it is a data-class, not a `Prop` marker — deliberately: an
instance must SUPPLY the output, not merely assert one exists.) -/
class IdentifiesClosedSector (C : Type u) where
  /-- `C` has a well-defined chirality-graded integer DT output (Int — the ℤ notation is outside this import cone). -/
  dtOutput : Bool → Int
  /-- The `S⁺`-sector output equals the certified `dimBPSplus`. -/
  dt_plus_eq : dtOutput true = dimBPSplus
  /-- The `S⁻`-sector output equals the certified `dimBPSminus`. -/
  dt_minus_eq : dtOutput false = dimBPSminus

/-- Conditional consequence: any category satisfying M3 outputs the concrete
chirality pair `(4, 3)` — composed from the class fields and M2's decidable
anchors, so the identification inherits every certified M2 number. -/
theorem dt_output_four_three (C : Type u) [h : IdentifiesClosedSector C] :
    h.dtOutput true = 4 ∧ h.dtOutput false = 3 :=
  ⟨h.dt_plus_eq.trans (show dimBPSplus = 4 by decide),
   h.dt_minus_eq.trans (show dimBPSminus = 3 by decide)⟩

/-- Conditional consequence: the bar split of any M3-identified category is
the certified `(7, 1)` — even part `7`, odd part `1`. -/
theorem dt_output_bar_split (C : Type u) [h : IdentifiesClosedSector C] :
    h.dtOutput true + h.dtOutput false = 7 ∧
    h.dtOutput true - h.dtOutput false = 1 := by
  obtain ⟨hp, hm⟩ := dt_output_four_three C
  rw [hp, hm]
  exact ⟨by decide, by decide⟩

end QOU.QBeta.RouteCM3CategoryIdentification
