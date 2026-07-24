import Mathlib.Algebra.Module.Basic
import Mathlib.Algebra.NoZeroSMulDivisors.Basic

/-!
# QOU.FluidDynamics.yekutieli_levi_unification — obstruction ⟺ Levi non-degeneracy

The categorical face of the **Levi dichotomy** (`conj:levi-degeneracy`), assembled
from the Yekutieli obstruction tower
([`ns-obstruction-tower`](../../../quantum-observable-universe/fluid-dynamics/ns-obstruction-tower.md),
steps (c)–(e)) and part of the q-NS classical-gap program
([`docs/audits/2026-07-18-q-ns-classical-gap-decomposition.md`](../../../../../../docs/audits/2026-07-18-q-ns-classical-gap-decomposition.md)).

**Scope discipline (owner directive 2026-07-24).** Every statement is *given a
QOU*: `κ_n|_Σ`, `leviNonDegenerate`, and the local cohomology are the QOU's own
categorical data. This is a statement *about QOUs*, not about the classical `ℝ³`
Navier–Stokes problem.

## The unification

`ns-obstruction-tower` establishes, at a collision point `p ∈ Σ` of an
anti-parallel vortex pair:

* **(e)** the leading NS obstruction on the collision locus is
  `κ_n|_Σ = lk(ϱ₁, ϱ₂) · e(ξ)|_Σ` (plus a subleading jet correction `δ_n`);
* **(c)** the local cohomology `H¹_{𝔪_p}(A) = V_{1/2} ⊕ V_{1/2}` is nonzero iff
  both filament cores still carry nontrivial local sections — i.e. have **not**
  dissolved into a sheet — and the Euler residue `e(ξ)|_Σ` is nonzero exactly on
  that support;
* **(d)** `H¹_{𝔪_p}(A) ≠ 0 ⟺ λ∥(p) > 0 ∧ λ⊥(p) > 0` (Levi non-degeneracy).

Chaining these, with nontrivial linking, gives the clean equivalence

`κ_n|_Σ ≠ 0  ⟺  Levi form non-degenerate at p`.

This is exactly the **branch structure** of `conj:levi-degeneracy`:

* **branch A** — non-degenerate core ⇒ obstruction survives ⇒ (categorically)
  NS-singular (`ns_obstruction_iff_levi` + `levi_nondegenerate_of_obstruction`);
* **branch B** — Levi degenerates / core flattens to a sheet ⇒ obstruction
  vanishes ⇒ (categorically) NS-regular (`ns_regular_of_sheet`).

## Honest scope (anti-laundering)

This is a **categorical** equivalence between the obstruction class and the Levi
geometry. It does **not** decide which branch the *actual* growth rate `C_L(κ)`
falls into (that is the open computation, `conj:levi-degeneracy`, and — via
Bridge B — the Clay content). What it does: replace the opaque
`obstruction_is_regularity_criterion` hypothesis of
`CategoricalClassicalNSBridge` (`q_ns_classical_bridge.lean`) with the *derived*
Yekutieli/local-cohomology mechanism, modulo the two named geometric inputs
(local-cohomology ⟺ Levi; Euler-residue ⟺ local-cohomology) which are the
content of `ns-obstruction-tower` (c)/(d).

## Base ring (§7c)

Generic: the obstruction class lives in an abelian group `M` (`H²(Σ, 𝓑)`), the
linking number is an integer, and non-vanishing of `n • x` needs only that `M`
is torsion-free (`[NoZeroSMulDivisors ℤ M]`) — the **leading-order** / generic
situation. The Kummer *divisibility/torsion* refinement (which `χ(A) = -6`
survives) is handled separately by `prop:ns-kummer-specialisation`. No `ℝ`.

## References
- [manuscript] fluid-dynamics/ns-obstruction-tower (`prop:ns-obstruction-tower`),
  core-levi-form (`prop:core-levi-form`), levi-degeneracy-conjecture
  (`conj:levi-degeneracy`), ns-kummer-specialisation
-/

namespace QOU.FluidDynamics

/-- Local-cohomology / Levi / Euler-residue data at a collision point `p ∈ Σ`,
    from `ns-obstruction-tower` steps (c)–(e).

    `M` is the coefficient group `H²(Σ, 𝓑)` (torsion-free at leading order);
    `linking : ℤ` is `lk(ϱ₁, ϱ₂)`; the leading obstruction is the integer
    multiple `kappaLeading = linking • eulerResidue`. The two `Prop` fields are
    the geometric equivalences the manuscript proves (c)/(d): they carry the
    real content, so the class is non-degenerate. -/
class NSObstructionLeviData (M : Type*) [AddCommGroup M]
    [NoZeroSMulDivisors ℤ M] where
  /-- The Euler residue `e(ξ)|_Σ ∈ H²(Σ, 𝓑)`. -/
  eulerResidue : M
  /-- The linking number `lk(ϱ₁, ϱ₂)` of the anti-parallel pair. -/
  linking : ℤ
  /-- The leading NS obstruction `κ_n|_Σ = lk · e(ξ)|_Σ`. -/
  kappaLeading : M
  /-- **Step (e):** the leading obstruction is the linking multiple of the
      Euler residue. -/
  kappa_def : kappaLeading = linking • eulerResidue
  /-- "`H¹_{𝔪_p}(A) ≠ 0`": the local cohomology at `p` is nonzero (both cores
      carry local sections; no sheet). -/
  localCohomNonzero : Prop
  /-- "`λ∥(p) > 0 ∧ λ⊥(p) > 0`": the Levi form is non-degenerate at `p`. -/
  leviNonDegenerate : Prop
  /-- **Step (d):** local cohomology nonvanishing ⟺ Levi non-degeneracy. -/
  localCohom_iff_levi : localCohomNonzero ↔ leviNonDegenerate
  /-- **Steps (c)/(e):** the Euler residue is nonzero ⟺ the local cohomology at
      `p` is nonzero. -/
  eulerResidue_iff_localCohom : eulerResidue ≠ 0 ↔ localCohomNonzero

variable {M : Type*} [AddCommGroup M] [NoZeroSMulDivisors ℤ M]

/-- **The Yekutieli–Levi unification.** With nontrivial linking, the leading NS
    obstruction on `Σ` is nonzero **iff** the Levi form is non-degenerate at `p`
    — the categorical face of the Levi dichotomy. Derived from `kappa_def`,
    `smul_ne_zero_iff`, and the two geometric equivalences (c)/(d). -/
-- Ref: [manuscript] fluid-dynamics/ns-obstruction-tower, core-levi-form
theorem ns_obstruction_iff_levi [ctx : NSObstructionLeviData M]
    (hlk : ctx.linking ≠ 0) :
    ctx.kappaLeading ≠ 0 ↔ ctx.leviNonDegenerate := by
  rw [ctx.kappa_def, smul_ne_zero_iff, ctx.eulerResidue_iff_localCohom,
    ctx.localCohom_iff_levi]
  exact and_iff_right hlk

/-- **Branch A (blow-up side).** A surviving obstruction forces the Levi form to
    be non-degenerate at `p` (discrete cores, no sheet). -/
-- Ref: [manuscript] fluid-dynamics/levi-degeneracy-conjecture (branch A)
theorem levi_nondegenerate_of_obstruction [ctx : NSObstructionLeviData M]
    (hlk : ctx.linking ≠ 0) (hobs : ctx.kappaLeading ≠ 0) :
    ctx.leviNonDegenerate :=
  (ns_obstruction_iff_levi hlk).mp hobs

/-- **Branch B (regular side).** If the Levi form degenerates (the core flattens
    into a sheet), the leading NS obstruction on `Σ` vanishes — categorically
    NS-regular. -/
-- Ref: [manuscript] fluid-dynamics/levi-degeneracy-conjecture (branch B)
theorem ns_regular_of_sheet [ctx : NSObstructionLeviData M]
    (hlk : ctx.linking ≠ 0) (hsheet : ¬ ctx.leviNonDegenerate) :
    ctx.kappaLeading = 0 := by
  by_contra h
  exact hsheet ((ns_obstruction_iff_levi hlk).mp h)

end QOU.FluidDynamics
