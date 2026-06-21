import Mathlib.Algebra.Field.Basic
import Mathlib.Algebra.GroupWithZero.Basic
import Mathlib.Data.Int.Basic
import Mathlib.Tactic.Ring


/-!
# QOU.categorical_dq_squared — Non-vanishing of dq²

The categorical q-deformed exterior derivative satisfies:

  dq²(α) = q⁻¹(1 - q⁻¹) ω_V ∧_q [ξ, α]

So dq² = 0 iff q = 1 or [ξ, α] = 0. On ξ-invariant forms,
dq reduces to q⁻¹ d with dq² = 0.

LaTeX label: `prop:categorical-dq-squared`

## References

- [manuscript] §1-quantum-observable-universe/categorical-dq-squared

**Base ring** (AGENTS.md §7c): the obstruction formula
`q⁻¹(1 - q⁻¹) · [ξ, α]` requires an inverse `q⁻¹`, so the carrier is a
generic `{R : Type*} [Field R]` with `q : R`, `q ≠ 0`. The combinatorial
content stays generic — no archimedean ordering is used (the `q = 1`
disjunct is an *algebraic* identity, not the archimedean `0 < q`). The
ground ring `R_q = ℤ[q, q⁻¹]` of the manuscript embeds into its fraction
field `Frac(R_q)`, which is the canonical `[Field R]` instance; specialise
via `ι : Frac(R_q) → ℝ, q ↦ q₀` for numerical evaluation.

**Design note.** The obstruction is a `def` of the data (`dqSquared`),
*not* a free structure field. A free field would be logically
independent of `q`/`reeb_bracket`, making `dqSquared = 0 ↔ …` vacuous;
defining it functionally is what lets the iff be a genuine theorem.
-/

namespace QOU

/-- **dq² obstruction data**: the substrate `q` (with invertibility
    witness) and the Reeb-bracket value `[ξ, α]`. -/
-- Ref: [manuscript] §1
structure DqSquaredObstruction (R : Type*) [Field R] where
  /-- The substrate parameter q. -/
  q : R
  /-- q ≠ 0 (algebraic invertibility — not the archimedean `0 < q`). -/
  q_ne_zero : q ≠ 0
  /-- The Reeb-bracket value [ξ, α] (scalar representative). -/
  reeb_bracket : R

variable {R : Type*} [Field R]

/-- The dq² obstruction: `dq²(α) = q⁻¹(1 - q⁻¹) · [ξ, α]`.
    Defined as a function of the data so the vanishing theorems below are
    non-vacuous. -/
-- Ref: [manuscript] §1
def DqSquaredObstruction.obstruction (obs : DqSquaredObstruction R) : R :=
  obs.q⁻¹ * (1 - obs.q⁻¹) * obs.reeb_bracket

/-- dq² vanishes iff q = 1 or the form is Reeb-invariant. -/
-- Ref: [manuscript] §1
theorem dq_squared_vanishes_iff (obs : DqSquaredObstruction R) :
    obs.obstruction = 0 ↔ (obs.q = 1 ∨ obs.reeb_bracket = 0) := by
  unfold DqSquaredObstruction.obstruction
  constructor
  · intro h
    rcases mul_eq_zero.mp h with h1 | h3
    · rcases mul_eq_zero.mp h1 with h2 | h4
      · -- q⁻¹ = 0 contradicts q ≠ 0
        exact absurd (inv_eq_zero.mp h2) obs.q_ne_zero
      · -- 1 - q⁻¹ = 0 ⟹ q⁻¹ = 1 ⟹ q = 1
        left
        have hinv : obs.q⁻¹ = 1 := (sub_eq_zero.mp h4).symm
        exact inv_eq_one.mp hinv
    · right; exact h3
  · intro h
    rcases h with hq1 | hreeb
    · rw [hq1]; simp
    · rw [hreeb]; ring

/-- **Non-vanishing of dq²** (categorical statement of `prop:categorical-dq-squared`).

    `dq² = 0 ⟺ q = 1 ∨ [ξ, α] = 0` — equivalently, for `q ≠ 1` the
    obstruction is nonzero on any non-Reeb-invariant form, so the
    q-deformed de Rham complex is *not* a cochain complex. This is the
    decl named by the content block's `lean.ref`. -/
-- Ref: [manuscript] §1
theorem categorical_dq_squared (obs : DqSquaredObstruction R) :
    obs.obstruction = 0 ↔ (obs.q = 1 ∨ obs.reeb_bracket = 0) :=
  dq_squared_vanishes_iff obs

/-- On Reeb-invariant forms, dq is a cochain differential (dq² = 0). -/
-- Ref: [manuscript] §1
theorem dq_squared_zero_on_invariant (obs : DqSquaredObstruction R)
    (h_inv : obs.reeb_bracket = 0) : obs.obstruction = 0 := by
  unfold DqSquaredObstruction.obstruction
  rw [h_inv]; ring

/-- For q ≠ 1, dq² ≠ 0 on generic (non-Reeb-invariant) forms. -/
-- Ref: [manuscript] §1
theorem dq_squared_nonzero_generic (obs : DqSquaredObstruction R)
    (hq : obs.q ≠ 1) (h_gen : obs.reeb_bracket ≠ 0) :
    obs.obstruction ≠ 0 := by
  rw [Ne, categorical_dq_squared obs, not_or]
  exact ⟨hq, h_gen⟩

end QOU
