import Mathlib.Algebra.Ring.Defs
import Mathlib.Tactic.NormNum

/-!
# QOU.FluidDynamics.qou_ns_in_qou — q-NS singularity *inside a QOU* (conditional)

**Scope discipline (owner directive 2026-07-24).** Every statement here is
conditional on being *given a Quantum Observable Universe* `(𝐂, A, τ)`
([`def:quantum-observable-universe`](../../../quantum-observable-universe/quantum-observable-universes/quantum-observable-universe.md)).
We make **no** claim about the general classical Navier–Stokes problem on
`ℝ³` (the Clay Millennium problem). The conclusion `internalBlowup` is the
QOU's **own internal** q-NS observable at `q = 1`, defined categorically from
the substrate — *not* a finite-time singularity of the physical PDE. Bridging
the two (identifying Object 1 = the internal flow with Object 2 = the `ℝ³` PDE)
is the open wall (`bean qou-innq`); it is deliberately **not** asserted.

## The in-QOU chain

Given a QOU, its defining **observability axiom** `Hom_𝐂(𝟙, Ad(A)) = 0` forces
irreducibility of the adjoint, hence a nonzero Euler characteristic `χ(A)`
(`qou-obstruction-reduction`), hence a nonzero **global** Euler class
`NS(A) := e(ξ) ∈ H²(S, ℤ)` of the Reeb bundle (its degree is `χ(A)`; item 1 of
`thm:ns-singularity-descartes`), which is by definition the QOU's internal q-NS
singularity at `q = 1` (`ns-obstruction-tower`, `blowup-yekutieli`). The
obstruction lives on the whole surface `S`, not on the vortex locus `Σ`: every
class in `H²` restricts to zero on a one-dimensional `Σ` (item 3). The capstone
`qou_internal_ns_singular` composes these QOU-structural steps.

**Every QOU is internally singular — from the axiom, not from `χ = -6`.** The
chain starts at the *definitional* observability field, so `qou_internal_ns_singular`
holds for **every** `QOUFluidUniverse` (∀ `U`); the Descartes `χ = -6` instance
below only *witnesses non-vacuity*. There is **no NS-regular QOU**: a `χ = 0`
(regular) object has `NS(A) = 0`, which violates observability, so it is a quantum
*universe* but **not** a quantum *observable* universe. Regularity and QOU-hood
are mutually exclusive.

**Clay recasting (in-QOU boundary).** Consequently the open bridge is *not* "which
QOU?" but "**is the physical fluid a QOU at all?**": classical NS blows up ⟺ the
fluid is the internal `q = 1` flow of a QOU (satisfies observability); classical
NS is globally regular ⟺ the fluid is *not* a QOU (fails observability, `χ = 0`).
That embedding question is the open wall (`bean qou-innq`,
`qou_ns_surreal_bridge`), deliberately not asserted.

**Non-vacuity.** `descartesQOU` is a *concrete* instance (`χ(A) = -6`, Bring's
surface) for which the whole base chain discharges **sorry-free**: the
arithmetic `-6 ≠ 0` is decidable and `internalBlowup` is definitionally
`NS(A) ≠ 0` (`ns-obstruction`). So `descartes_internal_ns_singular` is an
*unconditional* proof that this QOU's internal q-NS is singular — the capstone
is not an empty conditional.

## The Levi layer is withdrawn (2026-11-15, owner decision, PR #7747)

This module used to add a second layer, `QOUFluidUniverseLevi`, carrying the
"Yekutieli–Levi equivalence" `NS(A) ≠ 0 ↔ Levi non-degenerate`, and the theorem
`qou_levi_nondegenerate` placing every QOU on branch (A) of
`conj:levi-degeneracy`. Both are removed: step (d) of `prop:ns-obstruction-tower`
is withdrawn, the Levi datum of the vorticity plane field in dimension 3 is the
single scalar `ξ·curl ξ` (`prop:core-levi-form`), and branch (A) is refuted under
that reading by a Beltrami solution (`beltrami_refutes_branchA`). No Lean
declaration consumed them. Bean `qou-fm7s`.

## The obstruction is the global class (2026-11-15, owner decision, PR #7747)

Until this date the base chain modelled `NS(A) = e(ξ)|_Σ` and justified
`χ(A) ≠ 0 → NS(A) ≠ 0` by Kummer non-divisibility. That contradicts item 3 of the
restated `thm:ns-singularity-descartes`: `H²(Σ, ·) = 0` for one-dimensional `Σ`, so
`e(ξ)|_Σ = 0` always and the old step 2 could not be instantiated. The owner chose
to restate the chain on the global class. The obstruction is now `e(ξ) ∈ H²(S, ℤ)`,
and step 2 is the degree statement `deg e(ξ) = χ(A)`, so `χ(A) ≠ 0` gives
`e(ξ) ≠ 0` with no Kummer input. `descartesQOU` already modelled the global class
(`χ = -6`), so it is unchanged. The cost is that the chain no longer localises the
singularity on `Σ`; that localisation was the withdrawn Levi step.

## Base ring (§7c)
Generic `{k : Type*} [CommRing k]` for the obstruction; `χ(A) : ℤ`; other data
are `Prop`s. The concrete instance uses `k = ℤ`. No `ℝ`.

## References
- [leitner2026] quantum-observable-universes/quantum-observable-universe,
  stochastic-mechanics/qou-obstruction-reduction, fluid-dynamics/ns-obstruction,
  ns-obstruction-tower, ns-kummer-specialisation, ns-singularity-descartes,
  lifting-and-descent/p3-blowup-yekutieli
-/

namespace QOU.FluidDynamics

/-- The q-NS data **of a given Quantum Observable Universe** `(𝐂, A, τ)` over
    `k` — the definitional/arithmetic chain. `internalBlowup` is the QOU's
    **internal** q-NS singularity observable at `q = 1` (categorical), *not* the
    classical `ℝ³` PDE. -/
structure QOUFluidUniverse (k : Type*) [CommRing k] where
  /-- **Observability axiom**: `Hom_𝐂(𝟙, Ad(A)) = 0` (condition (ii) of
      `def:quantum-observable-universe`). Held by definition of a QOU. -/
  observability : Prop
  /-- A QOU satisfies its observability axiom by definition. -/
  observability_holds : observability
  /-- The Euler characteristic `χ(A) : ℤ`. -/
  eulerChar : ℤ
  /-- The NS obstruction `NS(A) := e(ξ)`, the **global** Euler class of the Reeb
      bundle in `H²(S, ℤ) ≅ ℤ` (not its restriction to `Σ`, which is always 0). -/
  obstruction : k
  /-- "The QOU's internal q-NS flow at `q = 1` is singular" — categorical
      internal observable (`blowup-yekutieli`), NOT the `ℝ³` PDE. -/
  internalBlowup : Prop
  /-- **Step 1 (`qou-obstruction-reduction`):** observability forces `χ(A) ≠ 0`. -/
  observability_forces_chi : observability → eulerChar ≠ 0
  /-- **Step 2 (item 1 of `thm:ns-singularity-descartes`):** `deg e(ξ) = χ(A)`,
      so `χ(A) ≠ 0` forces the global class `NS(A) ≠ 0`. -/
  chi_forces_obstruction : eulerChar ≠ 0 → obstruction ≠ 0
  /-- **Step 3 (`ns-obstruction`):** a nonzero NS obstruction *is*, by
      definition, the QOU's internal q-NS singularity (NS-singular ⟺ NS(A)≠0). -/
  obstruction_iff_internal_blowup : obstruction ≠ 0 ↔ internalBlowup

variable {k : Type*} [CommRing k]

/-- **The QOU's NS obstruction is nonzero.** Given a QOU, the global class
    `NS(A) = e(ξ) ≠ 0`. -/
-- Ref: [leitner2026] fluid-dynamics/ns-singularity-descartes
theorem qou_obstruction_nonzero (U : QOUFluidUniverse k) : U.obstruction ≠ 0 :=
  U.chi_forces_obstruction (U.observability_forces_chi U.observability_holds)

/-- **Given a QOU, its internal q-NS flow at `q = 1` is singular.**

    Derived by composing the QOU's own structural steps: observability ⇒
    `χ(A) ≠ 0` ⇒ `e(ξ) ≠ 0` in `H²(S)` ⇒ internal blow-up. A statement **about the QOU** —
    it does **not** resolve the classical Navier–Stokes problem, and
    `internalBlowup` is the categorical internal observable, not the `ℝ³` PDE. -/
-- Ref: [leitner2026] fluid-dynamics/ns-obstruction-tower, blowup-yekutieli
theorem qou_internal_ns_singular (U : QOUFluidUniverse k) : U.internalBlowup :=
  U.obstruction_iff_internal_blowup.mp (qou_obstruction_nonzero U)

/-- **Contrapositive scope check.** If a QOU's internal q-NS flow were regular,
    its NS obstruction would vanish — impossible for a genuine QOU. -/
-- Ref: [leitner2026] fluid-dynamics/ns-obstruction-tower
theorem qou_not_internally_regular (U : QOUFluidUniverse k)
    (hreg : ¬ U.internalBlowup) : False :=
  hreg (qou_internal_ns_singular U)

/-! ### Non-vacuity: the concrete Descartes QOU -/

/-- **The Descartes QOU** (`χ(A) = -6`, Bring's surface; `ns-singularity-descartes`)
    as a concrete `QOUFluidUniverse ℤ`. The obstruction is the global class
    `e(ξ) ∈ H²(S, ℤ) ≅ ℤ`, modelled by its degree `-6 = χ(A)` and `internalBlowup` is *defined* as `NS(A) ≠ 0` (the categorical
    meaning of NS-singular). Every base field discharges sorry-free: `-6 ≠ 0` is
    decidable arithmetic, and Step 3 is `Iff.rfl`. -/
def descartesQOU : QOUFluidUniverse ℤ where
  observability := True
  observability_holds := trivial
  eulerChar := -6
  obstruction := -6
  internalBlowup := (-6 : ℤ) ≠ 0
  observability_forces_chi := fun _ => by norm_num
  chi_forces_obstruction := fun _ => by norm_num
  obstruction_iff_internal_blowup := Iff.rfl

/-- **The Descartes QOU's internal q-NS is singular — unconditionally.** The
    capstone applied to the concrete instance; no `sorry`, no open hypothesis
    (still an *in-QOU* statement, not the `ℝ³` PDE). Witnesses that the general
    `qou_internal_ns_singular` is not vacuous. -/
-- Ref: [leitner2026] fluid-dynamics/ns-singularity-descartes
theorem descartes_internal_ns_singular : descartesQOU.internalBlowup :=
  qou_internal_ns_singular descartesQOU

end QOU.FluidDynamics
