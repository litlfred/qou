import Mathlib.Algebra.Field.Basic
import Mathlib.Algebra.GroupWithZero.Basic
import Mathlib.Data.Int.Basic
import Mathlib.Tactic.Ring


/-!
# QOU.dq_squared — Non-vanishing of dq² (archimedean form)

The q-deformed exterior derivative satisfies:

  dq²(α) = q⁻¹(1 - q⁻¹) dθ ∧ ℒ_ξ α

Thus dq² = 0 iff q = 1 or α is Reeb-invariant.

LaTeX label: `prop:dq-squared`

## References

- [manuscript] §1-quantum-observable-universe/dq-squared

**Base ring** (AGENTS.md §7c): the archimedean realisation of the
categorical `prop:categorical-dq-squared` obstruction. The formula
`q⁻¹(1 - q⁻¹) · dθ · ℒ_ξ α` needs an inverse `q⁻¹`, so the carrier is a
generic `{R : Type*} [Field R]` with `q : R`, `q ≠ 0`. The "archimedean"
qualifier names the *geometric interpretation* (`ω_V ↦ dθ` the symplectic
form, `[ξ, α] ↦ ℒ_ξ α` the Lie derivative) of the same algebraic identity;
the `q = 1` disjunct is an algebraic fact, not the archimedean `0 < q`.
Specialise via `ι : R → ℝ, q ↦ q₀` for numerical evaluation.

**Design note.** The obstruction `dqSquared` is a `def` of the data,
*not* a free structure field (a free field would be logically
independent of the inputs, making the vanishing iff vacuous).
-/

namespace QOU

/-- **Archimedean dq² data**: substrate `q` (with invertibility witness),
    the Lie-derivative value `ℒ_ξ α`, and the Levi form `dθ`. -/
-- Ref: [manuscript] §1
structure ArchimedeanDqSquared (R : Type*) [Field R] where
  /-- The substrate parameter q. -/
  q : R
  /-- q ≠ 0 (algebraic invertibility — not the archimedean `0 < q`). -/
  q_ne_zero : q ≠ 0
  /-- The Lie derivative value ℒ_ξ α (scalar representative). -/
  lie_deriv : R
  /-- The Levi form value dθ(·, ·) (scalar representative). -/
  levi_form : R

variable {R : Type*} [Field R]

/-- The archimedean dq² value: `dq²(α) = q⁻¹(1 - q⁻¹) · dθ · ℒ_ξ α`.
    Defined as a function of the data so the vanishing theorem is
    non-vacuous. -/
-- Ref: [manuscript] §1
def ArchimedeanDqSquared.dqSquared (d : ArchimedeanDqSquared R) : R :=
  d.q⁻¹ * (1 - d.q⁻¹) * d.levi_form * d.lie_deriv

/-- **Non-vanishing of dq²** (archimedean statement of `prop:dq-squared`).

    For a nondegenerate Levi form (`dθ ≠ 0`), `dq²(α) = 0 ⟺ q = 1 ∨ ℒ_ξ α = 0`:
    the q-deformed de Rham operator fails to be a cochain differential away
    from the classical limit `q = 1`, except on Reeb-invariant forms. This
    is the decl named by the content block's `lean.ref`. -/
-- Ref: [manuscript] §1
theorem dq_squared (d : ArchimedeanDqSquared R) (h_levi : d.levi_form ≠ 0) :
    d.dqSquared = 0 ↔ (d.q = 1 ∨ d.lie_deriv = 0) := by
  unfold ArchimedeanDqSquared.dqSquared
  constructor
  · intro h
    rcases mul_eq_zero.mp h with h1 | hlie
    · rcases mul_eq_zero.mp h1 with h2 | hlevi
      · rcases mul_eq_zero.mp h2 with hinv0 | hsub
        · exact absurd (inv_eq_zero.mp hinv0) d.q_ne_zero
        · left
          have hinv : d.q⁻¹ = 1 := (sub_eq_zero.mp hsub).symm
          exact inv_eq_one.mp hinv
      · exact absurd hlevi h_levi
    · right; exact hlie
  · intro h
    rcases h with hq1 | hlie
    · rw [hq1]; simp
    · rw [hlie]; ring

/-- dq² vanishes on Reeb-invariant forms. -/
-- Ref: [manuscript] §1
theorem dq_squared_zero_reeb_invariant (d : ArchimedeanDqSquared R)
    (h : d.lie_deriv = 0) : d.dqSquared = 0 := by
  unfold ArchimedeanDqSquared.dqSquared
  rw [h]; ring

/-- dq² vanishes at q = 1 (classical limit). -/
-- Ref: [manuscript] §1
theorem dq_squared_zero_classical (d : ArchimedeanDqSquared R)
    (hq : d.q = 1) : d.dqSquared = 0 := by
  unfold ArchimedeanDqSquared.dqSquared
  rw [hq]; simp

/-- On horizontal ℒ_ξ-invariant forms, dq defines a cochain complex. -/
-- Ref: [manuscript] §1
theorem dq_cochain_on_invariant (d : ArchimedeanDqSquared R)
    (h : d.lie_deriv = 0) : d.dqSquared = 0 :=
  dq_squared_zero_reeb_invariant d h

end QOU
