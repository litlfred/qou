import Mathlib.Algebra.Ring.Defs
import Mathlib.Algebra.Group.Basic
import Mathlib.Algebra.GroupWithZero.Units.Basic
import Mathlib.Tactic.Ring


/-!
# QOU.categorical_dq_squared — Non-vanishing of dq²

The categorical q-deformed exterior derivative satisfies:

  dq²(α) = q⁻¹(1 - q⁻¹) ω_V ∧_q [ξ, α]

So dq² = 0 iff q = 1 or [ξ, α] = 0. On ξ-invariant forms,
dq reduces to q⁻¹ d with dq² = 0.

LaTeX label: `prop:categorical-dq-squared`

## References

- [leitner2026] §1-quantum-observable-universe/categorical-dq-squared

**Base ring** (AGENTS.md §7c): the obstruction formula
`q⁻¹(1 - q⁻¹) · [ξ, α]` needs `q` invertible, so `q` is carried as a
**unit** `q : Rˣ` — the exact algebraic content of the former `q ≠ 0` —
over a generic `[CommRing R]`.  No field, no division: the manuscript's
own ground ring `R_q = ℤ[q, q⁻¹]` (`LaurentPolynomial ℤ`, in which
`q = T 1` *is* a unit) is now a direct instance, with no passage to
`Frac(R_q)`.  Specialise via `ι : R_q → ℝ, q ↦ q₀` for numerical
evaluation.

`[IsDomain R]` is the one genuinely load-bearing extra hypothesis, and it
is *essential*, not decorative: the `←` direction of the iff needs
`mul_eq_zero`.  Over a `CommRing` with zero divisors the statement is
false — in `R = ZMod 6` take `q = 5` (a unit, `q⁻¹ = 5`, `q ≠ 1`) and
`reeb_bracket = 3 ≠ 0`; then `q⁻¹(1 - q⁻¹)·3 = 5·2·3 = 30 = 0`, so the
obstruction vanishes with neither disjunct holding.  `ℤ[q, q⁻¹]` and
every field are domains, so nothing downstream is lost.

**Design note.** The obstruction is a `def` of the data (`obstruction`),
*not* a free structure field. A free field would be logically
independent of `q`/`reeb_bracket`, making `obstruction = 0 ↔ …` vacuous;
defining it functionally is what lets the iff be a genuine theorem.
-/

namespace QOU

/-- **dq² obstruction data**: the substrate `q` (as a unit of the ground
    ring) and the Reeb-bracket value `[ξ, α]`. -/
-- Ref: [leitner2026] §1
structure DqSquaredObstruction (R : Type*) [CommRing R] where
  /-- The substrate parameter q, carried as a unit — algebraic
      invertibility (the old `q ≠ 0`), not the archimedean `0 < q`. -/
  q : Rˣ
  /-- The Reeb-bracket value [ξ, α] (scalar representative). -/
  reeb_bracket : R

variable {R : Type*} [CommRing R]

/-- The dq² obstruction: `dq²(α) = q⁻¹(1 - q⁻¹) · [ξ, α]`.
    Defined as a function of the data so the vanishing theorems below are
    non-vacuous. -/
-- Ref: [leitner2026] §1
def DqSquaredObstruction.obstruction (obs : DqSquaredObstruction R) : R :=
  ((obs.q⁻¹ : Rˣ) : R) * (1 - ((obs.q⁻¹ : Rˣ) : R)) * obs.reeb_bracket

/-- dq² vanishes iff q = 1 or the form is Reeb-invariant. -/
-- Ref: [leitner2026] §1
theorem dq_squared_vanishes_iff [IsDomain R] (obs : DqSquaredObstruction R) :
    obs.obstruction = 0 ↔ (obs.q = 1 ∨ obs.reeb_bracket = 0) := by
  unfold DqSquaredObstruction.obstruction
  constructor
  · intro h
    rcases mul_eq_zero.mp h with h1 | h3
    · rcases mul_eq_zero.mp h1 with h2 | h4
      · -- a unit is never 0 in a nontrivial ring
        exact absurd h2 (Units.ne_zero _)
      · -- 1 - q⁻¹ = 0 ⟹ q⁻¹ = 1 ⟹ q = 1
        left
        have hinv : ((obs.q⁻¹ : Rˣ) : R) = 1 := (sub_eq_zero.mp h4).symm
        exact inv_eq_one.mp (Units.val_eq_one.mp hinv)
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
-- Ref: [leitner2026] §1
theorem categorical_dq_squared [IsDomain R] (obs : DqSquaredObstruction R) :
    obs.obstruction = 0 ↔ (obs.q = 1 ∨ obs.reeb_bracket = 0) :=
  dq_squared_vanishes_iff obs

/-- On Reeb-invariant forms, dq is a cochain differential (dq² = 0). -/
-- Ref: [leitner2026] §1
theorem dq_squared_zero_on_invariant (obs : DqSquaredObstruction R)
    (h_inv : obs.reeb_bracket = 0) : obs.obstruction = 0 := by
  unfold DqSquaredObstruction.obstruction
  rw [h_inv]; ring

/-- For q ≠ 1, dq² ≠ 0 on generic (non-Reeb-invariant) forms. -/
-- Ref: [leitner2026] §1
theorem dq_squared_nonzero_generic [IsDomain R] (obs : DqSquaredObstruction R)
    (hq : obs.q ≠ 1) (h_gen : obs.reeb_bracket ≠ 0) :
    obs.obstruction ≠ 0 := by
  rw [Ne, categorical_dq_squared obs, not_or]
  exact ⟨hq, h_gen⟩

end QOU
