import Mathlib.Algebra.Module.LinearMap.Defs

set_option autoImplicit false

/-!
# QOU.AlgebraicSubstrate.CartanContraction — the Cartan contraction step

The algebraic core of the classical differential-geometric fact that
contracting a flow-invariant closed form with the generating vector
field yields a closed form of one degree lower:

> if `L_R ω = 0` and `dω = 0`, then `d(ι_R ω) = 0`,

via Cartan's homotopy formula `L_R = d ∘ ι_R + ι_R ∘ d`.

This is the step that turns a Reeb-flow-invariant tetraplectic
(closed 4-)form into a closed 3-form — the Chern–Simons face of the
Q_β c₃ bar-odd analysis (`S = Im 𝔙`, the 4₁ deformation phase; see
`docs/scope/2026-08-01-reeb-tetraplectic-cs-threeform-identification.md`).

## Genericity and honesty (§7c, conditional-proved ≠ premise-established)

Mathlib does not currently provide Lie derivatives of differential
forms on manifolds, so the geometric instantiation (`d` = exterior
derivative, `iota` = interior product with the Reeb field, `lie` = Lie
derivative along it) is not available. We therefore state the step
over a generic module: `d`, `iota`, `lie` are arbitrary linear
endomorphisms and **Cartan's homotopy formula is an explicit
hypothesis** (`cartan`), not an established premise. The theorems
prove the implication only; nothing here asserts that any geometric
model satisfies `cartan`. The weakest typeclasses suffice — no
subtraction is used, so `AddCommMonoid` is enough.

LaTeX context: `docs/scope/2026-08-01` scope doc (this branch).

## References

- [leitner2026] Q_β c₃ bar-odd chain, `docs/audits/2026-07-11-qbeta-c3-barodd-nz-deformation-gap.md`.
-/

namespace QOU.AlgebraicSubstrate

variable {R : Type*} [CommSemiring R] {M : Type*} [AddCommMonoid M] [Module R M]

/-- On a closed element (`d ω = 0`), Cartan's homotopy formula collapses
to `lie ω = d (iota ω)`: the Lie derivative of a closed form is exact,
with primitive its contraction. -/
theorem lie_apply_eq_d_iota_of_closed
    (d iota lie : M →ₗ[R] M)
    (cartan : lie = d ∘ₗ iota + iota ∘ₗ d)
    {ω : M} (hclosed : d ω = 0) :
    lie ω = d (iota ω) := by
  rw [cartan]
  simp [LinearMap.add_apply, LinearMap.comp_apply, hclosed]

/-- **Cartan contraction step.** If `ω` is closed (`d ω = 0`) and
flow-invariant (`lie ω = 0`), its contraction `iota ω` is closed.
Geometric reading: a Reeb-invariant closed 4-form contracts to a
closed 3-form, whose de Rham class is an invariant of the flow. -/
theorem d_iota_eq_zero_of_closed_of_invariant
    (d iota lie : M →ₗ[R] M)
    (cartan : lie = d ∘ₗ iota + iota ∘ₗ d)
    {ω : M} (hclosed : d ω = 0) (hinv : lie ω = 0) :
    d (iota ω) = 0 := by
  rw [← lie_apply_eq_d_iota_of_closed d iota lie cartan hclosed]
  exact hinv

end QOU.AlgebraicSubstrate
