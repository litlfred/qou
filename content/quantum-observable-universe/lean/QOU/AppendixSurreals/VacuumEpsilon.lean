import Mathlib.Data.Real.Basic

/-!
# QOU.AppendixSurreals.VacuumEpsilon — conjectural class (placeholder)

**§3b-cond class axiomatisation** for content block
[`conj:vacuum-epsilon`](../../../quantum-observable-universe/appendix-surreals/vacuum-epsilon.md): *Infinitesimal vacuum: $\\mathrm{Geom}(\\bigcirc) = \\varepsilon$*.

This is a **conjecture**: the class `VacuumEpsilon` is a primary conjecture
carrier with **no instance** — the honest open state per AGENTS.md §3b-tax.
(The field schema is still a structural placeholder; see the note at the
bottom of the file and bean `qou-ffwk`.)  Downstream theorems may take
`[VacuumEpsilon]` as an explicit `[Instance]` hypothesis to derive
conditional Lean theorems against this named input (per §3b-cond).

The field schema below is a structural placeholder; refine the
fields to match the conjecture's actual content as the
formalisation matures.
-/

namespace QOU.AppendixSurreals

/-- Infinitesimal vacuum: $\\mathrm{Geom}(\\bigcirc) = \\varepsilon$

    Conjectural class — see [`conj:vacuum-epsilon`](../../../quantum-observable-universe/appendix-surreals/vacuum-epsilon.md). -/
class VacuumEpsilon where
  -- Witness: computations/none
  /-- **Content statement** (from manuscript):

      The Hoefsmit scattering pipeline assigns to each link $L$ a
*geometric energy* $\mathrm{Geom}(L) \in \mathbb{R}$
([Hoefsmit scattering pipeline](#prop:hoefsmit-scattering-pipeline)).
The vacuum normalisation requires $\mathrm{Geom}(\bigcirc) = 0$
on the unknot, so that the empty link contributes nothing to
particle masses.

      Field schema below is a structural placeholder; refine per §3b
      to match the conjecture's actual content. The placeholder is
      trivially inhabited; the conjectural content is carried by the
      narrative block, not by this field. -/
  residual : ℝ
  /-- The residual vanishes (the conjecture is the assertion that
      this holds). -/
  residual_eq_zero : residual = 0


-- **No instance is provided — the honest open state** (AGENTS.md §3b-tax).
-- Previously: `axiom conj_vacuum_epsilon` plus
-- `noncomputable instance : VacuumEpsilon := conj_vacuum_epsilon`, i.e. the
-- conjecture was asserted by `axiom` and installed globally, so every
-- downstream `[VacuumEpsilon]` resolved for free.  Consumers
-- (`CasimirModeCountFunctor`, `CasimirEpsilonVacuum`, `Conjectures`) already
-- declare `[VacuumEpsilon]`, so the global instance was silently satisfying a
-- hypothesis they had correctly written down.  Removed, not completed.
--
-- SEPARATE OPEN DEFECT (bean `qou-ffwk`): the field schema above is still a
-- placeholder — `residual : ℝ` with `residual_eq_zero : residual = 0` is
-- inhabited by `⟨0, rfl⟩`, so the class carries no content yet.  De-laundering
-- the axiom does not fix that; the fields must be refined to the actual claim
-- (`geom : Link → ℝ` with `geom unknot = 0`) before `[VacuumEpsilon]` means
-- anything downstream.

end QOU.AppendixSurreals
