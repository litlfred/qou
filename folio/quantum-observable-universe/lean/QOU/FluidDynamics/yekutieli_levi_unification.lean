import Mathlib.Algebra.Module.Basic
import Mathlib.Algebra.NoZeroSMulDivisors.Basic

/-!
# QOU.FluidDynamics.yekutieli_levi_unification — obstruction ⟺ local cohomology

**Re-scoped 2026-11-15 (owner decision, PR #7747, bean `qou-fm7s`).** This module
used to state the "Yekutieli–Levi unification" `κ_n|_Σ ≠ 0 ⟺ Levi form
non-degenerate at p`, with branch (A) "non-degenerate ⇒ obstruction survives ⇒
NS-singular" and branch (B) "sheet ⇒ obstruction vanishes ⇒ NS-regular". Both
rested on step (d) of `prop:ns-obstruction-tower`,
`H¹_{𝔪_p}(A) ≠ 0 ⟺ λ∥(p) > 0 ∧ λ⊥(p) > 0`, which is **withdrawn**:

* with `Θ = f·ξ♭` (owner decision Q1, `prop:core-levi-form`) the Levi datum of
  the vorticity plane field in dimension 3 is the single scalar `ξ·curl ξ`, so the
  two eigenvalues `λ∥, λ⊥` are undefined;
* branch (A) of `conj:levi-degeneracy` is refuted under that reading by the
  Beltrami solution `u = e^{−νt}(sin z, cos z, 0)` on `T³`
  (`beltrami_refutes_branchA`).

Removed: the fields `leviNonDegenerate` and `localCohom_iff_levi` (step (d)), and
the theorems `ns_obstruction_iff_levi`, `levi_nondegenerate_of_obstruction`
(branch A) and `ns_regular_of_sheet` (branch B). No Lean declaration in the
corpus consumed them. What remains is steps (c)/(e) only, and the conclusion is
the local-cohomology statement, not a Levi or regularity statement.

**Further scope note.** By `thm:ns-singularity-descartes` item 3, `Σ` is
one-dimensional, so `H²(Σ, ·) = 0` and every class `e(ξ)|_Σ` vanishes. The class
below is therefore an abstract carrier of the (c)/(e) bookkeeping; no instance is
supplied, and none is claimed for the Descartes universe.

## Base ring (§7c)

Generic: the obstruction class lives in an abelian group `M`, the linking number
is an integer, and non-vanishing of `n • x` needs only that `M` is torsion-free
(`[NoZeroSMulDivisors ℤ M]`). No `ℝ`.

## References
- [leitner2026] fluid-dynamics/ns-obstruction-tower (`prop:ns-obstruction-tower`),
  core-levi-form (`prop:core-levi-form`), levi-degeneracy-conjecture
  (`conj:levi-degeneracy`), ns-singularity-descartes
-/

namespace QOU.FluidDynamics

/-- Local-cohomology / Euler-residue data at a collision point `p ∈ Σ`, from
    `ns-obstruction-tower` steps (c) and (e). Step (d), the Levi equivalence, is
    withdrawn (see the module docstring).

    `M` is the coefficient group (torsion-free); `linking : ℤ` is
    `lk(ϱ₁, ϱ₂)`; the leading obstruction is `kappaLeading = linking • eulerResidue`. -/
class NSObstructionLeviData (M : Type*) [AddCommGroup M]
    [NoZeroSMulDivisors ℤ M] where
  /-- The Euler residue `e(ξ)|_Σ`. -/
  eulerResidue : M
  /-- The linking number `lk(ϱ₁, ϱ₂)` of the anti-parallel pair. -/
  linking : ℤ
  /-- The leading obstruction `κ_n|_Σ = lk · e(ξ)|_Σ`. -/
  kappaLeading : M
  /-- **Step (e):** the leading obstruction is the linking multiple of the
      Euler residue. -/
  kappa_def : kappaLeading = linking • eulerResidue
  /-- "`H¹_{𝔪_p}(A) ≠ 0`": the local cohomology at `p` is nonzero. -/
  localCohomNonzero : Prop
  /-- **Steps (c)/(e):** the Euler residue is nonzero ⟺ the local cohomology at
      `p` is nonzero. -/
  eulerResidue_iff_localCohom : eulerResidue ≠ 0 ↔ localCohomNonzero

variable {M : Type*} [AddCommGroup M] [NoZeroSMulDivisors ℤ M]

/-- With nontrivial linking, the leading obstruction is nonzero **iff** the local
    cohomology at `p` is nonzero. Derived from `kappa_def`, `smul_ne_zero_iff` and
    step (c)/(e). Says nothing about the Levi form or about regularity. -/
-- Ref: [leitner2026] fluid-dynamics/ns-obstruction-tower
theorem ns_obstruction_iff_localCohom [ctx : NSObstructionLeviData M]
    (hlk : ctx.linking ≠ 0) :
    ctx.kappaLeading ≠ 0 ↔ ctx.localCohomNonzero := by
  rw [ctx.kappa_def, smul_ne_zero_iff, ctx.eulerResidue_iff_localCohom]
  exact and_iff_right hlk

end QOU.FluidDynamics
