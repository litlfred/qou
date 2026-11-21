import QOU.AppendixSurreals.CasimirEpsilonVacuum
import QOU.AppendixSurreals.CasimirZetaPrefactor
import Mathlib.Tactic

/-!
# QOU.AppendixSurreals.CasimirModeCountFunctor — Stage C scaffolding for N_⊙

Stage C of the `N_⊙`-construction workplan
(`docs/workplans/2026-06-12-n-odot-construction-scoping.md`) for
[`conj:casimir-epsilon-vacuum`](../../../quantum-observable-universe/appendix-surreals/casimir-epsilon-vacuum.md).

The genuine blocker of the Casimir conjecture is the **categorical
object** `N_⊙(A, d)` — the plate-bounded, surreal-valued disjoint-unknot
density whose archimedean image is the standard mode count. The
selection principle (`CasimirNStability.lean`) and the prefactor
arithmetic (`CasimirZetaPrefactor.lean`) pin down *what `N_⊙` must reduce
to*; they do not *build* it. This file scaffolds the construction: it
gives `N_⊙` a **typed interface** (the §3b-cond class pattern) and proves
that any object meeting the interface discharges the downstream
`CasimirEpsilonVacuum` energy class. `N_⊙` thereby becomes a precise
upstream target rather than prose.

**What is new here, beyond `CasimirEpsilonVacuum`.** That class carries
the archimedean energy *density* `energyPerArea : ℝ → ℝ` directly. The
mode-count object is one level up: it depends on the plate **area** `A`
as well as the gap `d`, and the physically essential property is
**extensivity in area** (locality of the lift) — this is what makes
"energy per unit area" well-defined and area-independent. The interface
records that, plus the reduction (via `n`-stability) to the q-free
disjoint-count scaling `−π²/(720 d³)`.

**What remains open (no instance is provided).** Constructing an instance
is the Yekutieli-homotopy lift of the plate-bounded link-projection
functor — a functor from plate-bounded ambient-isotopy classes to
surreal-valued counts, functorial in `(A, d)`, whose `n`-stable
restriction is the bare disjoint-unknot count. The substrate-conformal
boundary data this lift needs is not yet formalised anywhere in the
corpus; see the workplan Stage C. This file is the *target type*, not the
construction.

Ref: [casimir1948] https://dwc.knaw.nl/DL/publications/PU00018547.pdf
Ref: [leitner2026] appendix-surreals/casimir-epsilon-vacuum.md
-/

namespace QOU.AppendixSurreals

open scoped Real

/-- **Stage-C interface for `N_⊙(A, d)`** (§3b-cond class). Carries the
archimedean image of `(N⊙^in − N⊙^out)·ε` as a function of plate area `A`
and gap `d` (units `ℏc = 1`), exactly as `CasimirEpsilonVacuum`
sidesteps the surreal layer by recording the standard-part. The two
axioms are the content the lift must deliver:

* `extensive_in_area` — the count difference is proportional to the plate
  area (locality / functoriality of the lift), so the per-area energy is
  well-defined and area-independent;
* `per_area_scaling` — the per-area count reduces to the q-free
  disjoint-unknot value `−π²/(720 d³)` selected by `n`-stability
  (`CasimirNStability`), with prefactor pinned by `CasimirZetaPrefactor`.

No instance is provided: the construction is the open Yekutieli lift. -/
class PlateModeCountFunctor where
  /-- archimedean image of `(N⊙^in − N⊙^out)·ε` for plates of area `A`,
  gap `d` (units `ℏc = 1`). -/
  modeCountDiff : ℝ → ℝ → ℝ
  /-- extensivity in plate area: the count difference is proportional to
  area, so energy per unit area is well-defined and area-independent. -/
  extensive_in_area : ∀ A d : ℝ, modeCountDiff A d = A * modeCountDiff 1 d
  /-- the per-area count reduces to the disjoint-unknot (bare-count,
  q-free) value selected by `n`-stability: the leading parallel-plate
  scaling `−π²/(720 d³)`. -/
  per_area_scaling :
    ∀ d : ℝ, 0 < d → modeCountDiff 1 d = -(Real.pi ^ 2) / (720 * d ^ 3)

/-- **`N_⊙ ⇒ CasimirEpsilonVacuum`.** The plate-mode-count functor's
per-area archimedean image is exactly the `CasimirEpsilonVacuum` energy
density. Hence constructing `N_⊙` (the open lift) discharges the
downstream conjecture class — and, via `energyPerArea_deriv`, the
textbook force law `−π²/(240 d⁴)`. This is the precise sense in which
`N_⊙` is the genuine *upstream* target. -/
instance casimirEpsilonVacuum_of_functor [PlateModeCountFunctor] :
    CasimirEpsilonVacuum where
  energyPerArea d := PlateModeCountFunctor.modeCountDiff 1 d
  energyPerArea_eq d hd := PlateModeCountFunctor.per_area_scaling d hd

/-- Area-extensivity of the total energy, as a standalone consequence:
the total Casimir energy between plates of area `A` is `A` times the
per-area density. This is the content that makes the *force per unit
area* a well-defined observable. -/
theorem modeCountDiff_extensive [PlateModeCountFunctor] (A d : ℝ) :
    PlateModeCountFunctor.modeCountDiff A d
      = A * PlateModeCountFunctor.modeCountDiff 1 d :=
  PlateModeCountFunctor.extensive_in_area A d

/-- The force per unit area follows from the functor interface alone, by
composing the derived `CasimirEpsilonVacuum` instance with
`energyPerArea_deriv`: `∂_d (energy/area) = π²/(240 d⁴)` for `d > 0`. -/
theorem force_per_area_of_functor [VacuumEpsilon] [PlateModeCountFunctor]
    (d : ℝ) (hd : 0 < d) :
    deriv CasimirEpsilonVacuum.energyPerArea d = Real.pi ^ 2 / (240 * d ^ 4) :=
  energyPerArea_deriv d hd

/-- **Stage-C reduction — the two external inputs, made explicit.** A
`PlateModeCountFunctor` is fully determined by (1) an area-extensive
count function and (2) the analytic fact that its per-area part has the
regularized cubic-tower scaling `−π²/(720 d³)`. Input (2) packages the
transported physics — the free-field `n³` mode degeneracy and the
ζ-regularization of the divergent tower (classical Casimir 1948) — which
is exactly what the open Yekutieli lift must supply. This constructor
exhibits the reduction: closing Stage C means producing `f` together
with these two proofs (no further data). -/
def PlateModeCountFunctor.ofData
    (f : ℝ → ℝ → ℝ)
    (hext : ∀ A d : ℝ, f A d = A * f 1 d)
    (hscale : ∀ d : ℝ, 0 < d → f 1 d = -(Real.pi ^ 2) / (720 * d ^ 3)) :
    PlateModeCountFunctor :=
  { modeCountDiff := f, extensive_in_area := hext, per_area_scaling := hscale }

/-- **Bridge to the Stage-B prefactor.** The `d⁻³` coefficient `π²/720`
of the per-area scaling is exactly the transverse geometric factor
`π²/6` times `ζ(−3) = 1/120` — i.e. the mode-count's leading coefficient
*is* the `CasimirZetaPrefactor` value. This ties the Stage-C interface to
the machine-checked Stage-B arithmetic (`riemannZeta_neg_three_re`), so
the one numerical constant the construction rests on is no longer free. -/
theorem casimir_coefficient_eq_zeta_prefactor :
    Real.pi ^ 2 / 720 = (Real.pi ^ 2 / 6) * (riemannZeta (-3 : ℂ)).re := by
  rw [riemannZeta_neg_three_re]; ring

/-- **Transported consistency witness — NOT a substrate derivation.**
This inhabits `PlateModeCountFunctor` with the *textbook* Casimir energy
density hardcoded, `f(A,d) = −A·π²/(720 d³)`. Its only purpose is to show
the interface is **consistent** (the two axioms are jointly satisfiable,
so the class is not vacuous) and that the downstream chain
(`CasimirEpsilonVacuum`, and via `energyPerArea_deriv` the force law)
runs end-to-end on a concrete object.

It is **transport, not derivation**: the `−π²/(720 d³)` scaling is
*postulated* here, copied from standard physics, **not** produced from
substrate data. Providing it as an instance would let `typeclass`
resolution silently discharge the conjecture, so it is deliberately a
plain `def` (not an `instance`). The open conjecture
(`conj:casimir-epsilon-vacuum`) is precisely that the categorical
Yekutieli lift yields *this* function from the plate-bounded mode count
— see `docs/workplans/2026-06-12-n-odot-construction-scoping.md` (Stage C).
-/
noncomputable def casimirTransportedFunctor : PlateModeCountFunctor :=
  PlateModeCountFunctor.ofData
    (fun A d => -A * Real.pi ^ 2 / (720 * d ^ 3))
    (fun _ _ => by ring)
    (fun _ _ => by ring)

end QOU.AppendixSurreals
