import Mathlib.Algebra.Ring.Units
import Mathlib.Algebra.GroupWithZero.Units.Basic
import Mathlib.Tactic.Ring


/-!
# QOU.dq_squared — Non-vanishing of dq² (archimedean form)

The q-deformed exterior derivative satisfies:

  dq²(α) = q⁻¹(1 - q⁻¹) dθ ∧ ℒ_ξ α

Thus dq² = 0 iff q = 1 or α is Reeb-invariant.

LaTeX label: `prop:dq-squared`

## References

- [leitner2026] §1-quantum-observable-universe/dq-squared

**Base ring** (AGENTS.md §7c): the archimedean realisation of the
categorical `prop:categorical-dq-squared` obstruction. The formula
`q⁻¹(1 - q⁻¹) · dθ · ℒ_ξ α` needs the modulus to be invertible, so `q` is
carried as a **unit** `q : Rˣ` over a generic `{R : Type*} [CommRing R]`
and `↑q⁻¹` is a `Units` coercion — no field, no ring inverse. (Carrying the
unit *replaces* the old `q : R` plus `q_ne_zero` field: over a domain the
two are the same datum.)

The vanishing **iff** additionally needs `[IsDomain R]`, and that hypothesis
is genuine rather than technical: the forward direction reads off a factor
from a vanishing product. Over `ℤ/6` the statement is FALSE — take
`q = 5` (a unit, `q⁻¹ = 5`), `dθ = 3 ≠ 0`, `ℒ_ξ α = 3 ≠ 0`; then
`q⁻¹(1 − q⁻¹) = 5·(−4) = 4` and `4·3·3 = 36 = 0`, yet `q ≠ 1` and
`ℒ_ξ α ≠ 0`. `ℤ[q, q⁻¹]` *is* a domain, so the substrate ring qualifies;
a field is not needed.

The "archimedean" qualifier names the *geometric interpretation*
(`ω_V ↦ dθ` the symplectic form, `[ξ, α] ↦ ℒ_ξ α` the Lie derivative) of
the same algebraic identity; the `q = 1` disjunct is an algebraic fact, not
the archimedean `0 < q`. Specialise via `ι : R → ℝ, q ↦ q₀` for numerical
evaluation.

**Design note.** The obstruction `dqSquared` is a `def` of the data,
*not* a free structure field (a free field would be logically
independent of the inputs, making the vanishing iff vacuous).
-/

namespace QOU

/-- **Archimedean dq² data**: substrate `q` (as a unit — the invertibility
    witness is the unit structure itself), the Lie-derivative value `ℒ_ξ α`,
    and the Levi form `dθ`. -/
-- Ref: [leitner2026] §1
structure ArchimedeanDqSquared (R : Type*) [CommRing R] where
  /-- The substrate parameter q, carried as a unit (algebraic
      invertibility — not the archimedean `0 < q`). -/
  q : Rˣ
  /-- The Lie derivative value ℒ_ξ α (scalar representative). -/
  lie_deriv : R
  /-- The Levi form value dθ(·, ·) (scalar representative). -/
  levi_form : R

variable {R : Type*} [CommRing R]

/-- The archimedean dq² value: `dq²(α) = q⁻¹(1 - q⁻¹) · dθ · ℒ_ξ α`.
    Defined as a function of the data so the vanishing theorem is
    non-vacuous. -/
-- Ref: [leitner2026] §1
def ArchimedeanDqSquared.dqSquared (d : ArchimedeanDqSquared R) : R :=
  (↑d.q⁻¹ : R) * (1 - (↑d.q⁻¹ : R)) * d.levi_form * d.lie_deriv

/-- **Non-vanishing of dq²** (archimedean statement of `prop:dq-squared`).

    For a nondegenerate Levi form (`dθ ≠ 0`), `dq²(α) = 0 ⟺ q = 1 ∨ ℒ_ξ α = 0`:
    the q-deformed de Rham operator fails to be a cochain differential away
    from the classical limit `q = 1`, except on Reeb-invariant forms. This
    is the decl named by the content block's `lean.ref`.

    `[IsDomain R]` is essential, not cosmetic — see the module docstring for
    the `ℤ/6` counterexample without it. -/
-- Ref: [leitner2026] §1
theorem dq_squared [IsDomain R] (d : ArchimedeanDqSquared R)
    (h_levi : d.levi_form ≠ 0) :
    d.dqSquared = 0 ↔ (d.q = 1 ∨ d.lie_deriv = 0) := by
  unfold ArchimedeanDqSquared.dqSquared
  constructor
  · intro h
    rcases mul_eq_zero.mp h with h1 | hlie
    · rcases mul_eq_zero.mp h1 with h2 | hlevi
      · rcases mul_eq_zero.mp h2 with hinv0 | hsub
        · exact absurd hinv0 (Units.ne_zero _)
        · left
          have hinv : (↑d.q⁻¹ : R) = 1 := (sub_eq_zero.mp hsub).symm
          exact inv_eq_one.mp (Units.val_eq_one.mp hinv)
      · exact absurd hlevi h_levi
    · right; exact hlie
  · intro h
    rcases h with hq1 | hlie
    · rw [hq1]; simp
    · rw [hlie]; ring

/-- dq² vanishes on Reeb-invariant forms. -/
-- Ref: [leitner2026] §1
theorem dq_squared_zero_reeb_invariant (d : ArchimedeanDqSquared R)
    (h : d.lie_deriv = 0) : d.dqSquared = 0 := by
  unfold ArchimedeanDqSquared.dqSquared
  rw [h]; ring

/-- dq² vanishes at q = 1 (classical limit). -/
-- Ref: [leitner2026] §1
theorem dq_squared_zero_classical (d : ArchimedeanDqSquared R)
    (hq : d.q = 1) : d.dqSquared = 0 := by
  unfold ArchimedeanDqSquared.dqSquared
  rw [hq]; simp

/-- On horizontal ℒ_ξ-invariant forms, dq defines a cochain complex. -/
-- Ref: [leitner2026] §1
theorem dq_cochain_on_invariant (d : ArchimedeanDqSquared R)
    (h : d.lie_deriv = 0) : d.dqSquared = 0 :=
  dq_squared_zero_reeb_invariant d h

end QOU
