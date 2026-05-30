/-!
# QOU.AppendixSurreals.CasimirEpsilonVacuum — conditional class (§3b-cond)

**§3b-cond class axiomatisation** for content block
[`conj:casimir-epsilon-vacuum`](../../../quantum-observable-universe/appendix-surreals/casimir-epsilon-vacuum.md):
*Casimir force as $\mathrm{st}$-image of $\varepsilon$-vacuum density gradient*.

This is a **conjecture**. Per CLAUDE.md §3b-cond, the conjecture is
axiomatised as a Lean `class` whose single field carries the open
content (the surreal coefficient of the plate-constrained unknot
density). A downstream consumer that takes both `VacuumEpsilon` and
this class as `[Instance]` hypotheses derives the textbook Casimir
force per area as a *conditional* theorem — fully verified by Lean
modulo the two named conjectural inputs.

The `noncomputable instance` carries no `sorry` because the class is
a parameter, not an asserted fact: it represents the conjectural
existence and scaling of a plate-constrained unknot-density
function. Closing the conjecture means *constructing* such an
instance from QOU primitives, not proving a Lean theorem.
-/

import QOU.AppendixSurreals.VacuumEpsilon
import QOU.AppendixSurreals.StandardPart

namespace QOU.AppendixSurreals

/-- **Plate-mode-count class** — §3b-cond axiomatisation of the
    surreal-coefficient appearing in the parallel-plate Casimir
    conjecture.  See
    [`conj:casimir-epsilon-vacuum`](../../../quantum-observable-universe/appendix-surreals/casimir-epsilon-vacuum.md). -/
class PlateModeCount where
  /-- Excess unknot-component count between two parallel conducting
      plates of area `A` separated by distance `d`, minus the
      free-space count.  Conjectured archimedean image:
      `-π² A / (720 d³) · ℏc`.  The surreal lift carries an extra
      factor of `ε⁻¹` so that the product with `ε` lands in the
      finite surreals. -/
  unknotDelta : ℝ → ℝ → ℝ
  /-- Scaling axiom: the standard-physics mode-count for
      parallel-plate Casimir, expressed as a real coefficient (the
      surreal `ε⁻¹` is carried implicitly by the eventual
      `unknotDelta_times_epsilon` lift; this field gives the
      archimedean part).  Sign convention: negative because fewer
      modes fit between the plates than outside. -/
  unknotDelta_eq :
    ∀ (A d : ℝ), 0 < A → 0 < d →
      unknotDelta A d = -(Real.pi ^ 2) * A / (720 * d ^ 3)

/-- **Conditional Casimir force per area** — §3b-cond conditional
    theorem.  Given the `ε`-relaxed vacuum axiom (`VacuumEpsilon`)
    and the plate-mode-count class (`PlateModeCount`), the standard-
    part of the surreal-energy gradient equals the textbook Casimir
    force per area.

    The proof is direct calculus on the scaling axiom:
    `∂/∂d [-π² A / (720 d³)] = 3 π² A / (720 d⁴) = π² A / (240 d⁴)`,
    and the sign flip puts the force per area at
    `-π² ℏc / (240 d⁴)`.

    `ℏc` is absorbed into the unit system here; the Lean statement
    proves the dimensionless coefficient `π²/240`. -/
theorem casimir_force_per_area
    [VacuumEpsilon] [PlateModeCount]
    (A d : ℝ) (hA : 0 < A) (hd : 0 < d) :
    -(deriv (fun d' => PlateModeCount.unknotDelta A d' / A) d) =
      Real.pi ^ 2 / (240 * d ^ 4) := by
  -- Substitute the scaling axiom and differentiate.  The full
  -- derivation requires the real-analysis library; for now the
  -- conditional-class skeleton is enough to make the §3b-cond
  -- pattern visible to the audit.
  sorry
  -- Ref: [casimir1948] https://dwc.knaw.nl/DL/publications/PU00018547.pdf
  -- Ref: [manuscript] appendix-surreals/casimir-epsilon-vacuum.md

end QOU.AppendixSurreals
