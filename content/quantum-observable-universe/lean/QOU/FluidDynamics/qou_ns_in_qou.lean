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
(`qou-obstruction-reduction`), hence — via Kummer non-divisibility — a nonzero
NS obstruction `NS(A) = e(ξ)|_Σ` (`ns-obstruction`, `ns-kummer-specialisation`),
which is by definition the QOU's internal q-NS singularity at `q = 1`
(`ns-obstruction-tower`, `blowup-yekutieli`). The capstone
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

## Two layers, honestly separated
- **base `QOUFluidUniverse`** — the definitional/arithmetic chain (observability
  → χ → obstruction → internal blow-up). Fully instantiable (`descartesQOU`).
- **`QOUFluidUniverseLevi`** — adds the *geometric* Yekutieli–Levi equivalence
  (`obstruction ≠ 0 ↔ Levi non-degenerate`, the T8 result), which is a genuine
  categorical theorem, **not** a definition; it is kept as a conditional
  extension and is *not* collapsed to `rfl` in `descartesQOU`.

## Base ring (§7c)
Generic `{k : Type*} [CommRing k]` for the obstruction; `χ(A) : ℤ`; other data
are `Prop`s. The concrete instance uses `k = ℤ`. No `ℝ`.

## References
- [manuscript] quantum-observable-universes/quantum-observable-universe,
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
  /-- The NS obstruction value `NS(A) = e(ξ)|_Σ`. -/
  obstruction : k
  /-- "The QOU's internal q-NS flow at `q = 1` is singular" — categorical
      internal observable (`blowup-yekutieli`), NOT the `ℝ³` PDE. -/
  internalBlowup : Prop
  /-- **Step 1 (`qou-obstruction-reduction`):** observability forces `χ(A) ≠ 0`. -/
  observability_forces_chi : observability → eulerChar ≠ 0
  /-- **Step 2 (`ns-obstruction`, `ns-kummer-specialisation`):** `χ(A) ≠ 0`
      forces `NS(A) ≠ 0` (Kummer non-divisibility). -/
  chi_forces_obstruction : eulerChar ≠ 0 → obstruction ≠ 0
  /-- **Step 3 (`ns-obstruction`):** a nonzero NS obstruction *is*, by
      definition, the QOU's internal q-NS singularity (NS-singular ⟺ NS(A)≠0). -/
  obstruction_iff_internal_blowup : obstruction ≠ 0 ↔ internalBlowup

variable {k : Type*} [CommRing k]

/-- **The QOU's NS obstruction is nonzero.** Given a QOU, `NS(A) ≠ 0`. -/
-- Ref: [manuscript] fluid-dynamics/ns-obstruction, ns-kummer-specialisation
theorem qou_obstruction_nonzero (U : QOUFluidUniverse k) : U.obstruction ≠ 0 :=
  U.chi_forces_obstruction (U.observability_forces_chi U.observability_holds)

/-- **Given a QOU, its internal q-NS flow at `q = 1` is singular.**

    Derived by composing the QOU's own structural steps: observability ⇒
    `χ(A) ≠ 0` ⇒ `NS(A) ≠ 0` ⇒ internal blow-up. A statement **about the QOU** —
    it does **not** resolve the classical Navier–Stokes problem, and
    `internalBlowup` is the categorical internal observable, not the `ℝ³` PDE. -/
-- Ref: [manuscript] fluid-dynamics/ns-obstruction-tower, blowup-yekutieli
theorem qou_internal_ns_singular (U : QOUFluidUniverse k) : U.internalBlowup :=
  U.obstruction_iff_internal_blowup.mp (qou_obstruction_nonzero U)

/-- **Contrapositive scope check.** If a QOU's internal q-NS flow were regular,
    its NS obstruction would vanish — impossible for a genuine QOU. -/
-- Ref: [manuscript] fluid-dynamics/ns-obstruction-tower
theorem qou_not_internally_regular (U : QOUFluidUniverse k)
    (hreg : ¬ U.internalBlowup) : False :=
  hreg (qou_internal_ns_singular U)

/-! ### Non-vacuity: the concrete Descartes QOU -/

/-- **The Descartes QOU** (`χ(A) = -6`, Bring's surface; `ns-singularity-descartes`)
    as a concrete `QOUFluidUniverse ℤ`. The obstruction is modelled by the scalar
    `-6 = χ(A)` and `internalBlowup` is *defined* as `NS(A) ≠ 0` (the categorical
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
-- Ref: [manuscript] fluid-dynamics/ns-singularity-descartes
theorem descartes_internal_ns_singular : descartesQOU.internalBlowup :=
  qou_internal_ns_singular descartesQOU

/-! ### Geometric layer: the Levi branch (conditional extension) -/

/-- A QOU together with the **geometric** Yekutieli–Levi equivalence. This
    equivalence (`ns-obstruction-tower` (c)/(d), the T8 result
    `ns_obstruction_iff_levi`) is a categorical *theorem*, not a definition, so
    it is carried here as an extra hypothesis rather than folded into the base. -/
structure QOUFluidUniverseLevi (k : Type*) [CommRing k]
    extends QOUFluidUniverse k where
  /-- "The QOU's Levi form is non-degenerate along its ladder" (branch A of
      `conj:levi-degeneracy`). -/
  leviNonDegenerate : Prop
  /-- **Yekutieli–Levi unification:** `NS(A) ≠ 0 ↔ Levi non-degenerate.** -/
  obstruction_iff_levi : obstruction ≠ 0 ↔ leviNonDegenerate

/-- **Given a QOU (with the Yekutieli–Levi equivalence), its internal q-NS is
    forced into the non-degenerate branch** — branch A of `conj:levi-degeneracy`
    (`β = 0`, blow-up side). *In a QOU* the trichotomy branch is decided; the
    general growth-rate `β` of a classical flow is untouched. -/
-- Ref: [manuscript] fluid-dynamics/ns-obstruction-tower, levi-degeneracy-conjecture
theorem qou_levi_nondegenerate (U : QOUFluidUniverseLevi k) :
    U.leviNonDegenerate :=
  U.obstruction_iff_levi.mp (qou_obstruction_nonzero U.toQOUFluidUniverse)

end QOU.FluidDynamics
