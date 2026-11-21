import Mathlib.Algebra.Ring.Defs
import Mathlib.Tactic.Ring

/-!
# QOU.Mass.sl2_period_conserved_quantity — first integral of the depth-2 recurrence

The depth-`2` (`det B = 1`) prolongation recurrence
`a (n+2) = τ · a (n+1) − a n`
([`prop:sl2-prolongation-recurrence`](#prop:sl2-prolongation-recurrence)) admits a
**conserved first integral**

  `H_n(a, τ) := a (n+1)² − τ · a (n+1) · a n + a n²`,    `H_{n+1} = H_n`,

the discrete "energy" of the Lucas/Chebyshev recurrence (the cup-product
symplectic form evaluated on consecutive periods). Its existence is the
structural obstruction that **forks** the depth-`2` hypothesis from the true
prolonged period: a sequence whose ratio `a (n+1) / a n` grows without bound has
`H_n → ∞`, so it conserves no first integral and therefore satisfies *no* depth-`2`
(`det = 1`) recurrence. The residue-sum period
`a_D^(n) = Σ_λ dim_q` ([`prop:sw-period-residue-sum`](#prop:sw-period-residue-sum))
grows factorially, so the depth-`2` `τ` is only the `n ≤ 4` germ — not the period.

The first integral itself is a **ring identity** (proved here, generic and
sorry-free); the growth obstruction is its archimedean reading.

LaTeX label: `prop:sl2-period-conserved-quantity`.

## References

- [leitner2026] §mass-theory/sl2-period-conserved-quantity

**Ground ring**: generic `[CommRing R]` (the conserved quantity is a polynomial
identity in the sequence and `τ`). See `GroundRingAnnotations.lean`.
-/

namespace QOU.Mass

variable {R : Type*} [CommRing R]

/-- The depth-`2` first integral `H_n = a (n+1)² − τ · a (n+1) · a n + a n²`,
the discrete energy of the Lucas/Chebyshev recurrence. -/
def sl2Invariant (a : ℕ → R) (τ : R) (n : ℕ) : R :=
  a (n + 1) ^ 2 - τ * a (n + 1) * a n + a n ^ 2

/-- **First integral, single step.** If `a` satisfies the depth-`2` recurrence
`a (n+2) = τ · a (n+1) − a n`, the invariant is unchanged: `H_{n+1} = H_n`.
Pure consequence of substituting the recurrence and expanding (`ring`). -/
-- Ref: [leitner2026] §mass-theory/sl2-period-conserved-quantity
theorem sl2Invariant_succ (a : ℕ → R) (τ : R)
    (hrec : ∀ n, a (n + 2) = τ * a (n + 1) - a n) (n : ℕ) :
    sl2Invariant a τ (n + 1) = sl2Invariant a τ n := by
  have h : a (n + 1 + 1) = τ * a (n + 1) - a n := hrec n
  unfold sl2Invariant
  rw [h]
  ring

/-- **Conserved first integral.** The invariant is constant along the whole
orbit of the depth-`2` recurrence: `H_n = H_0` for every `n`. (Induction on `n`,
each step discharged by `sl2Invariant_succ`.) -/
-- Ref: [leitner2026] §mass-theory/sl2-period-conserved-quantity
theorem sl2Invariant_eq_zeroth (a : ℕ → R) (τ : R)
    (hrec : ∀ n, a (n + 2) = τ * a (n + 1) - a n) (n : ℕ) :
    sl2Invariant a τ n = sl2Invariant a τ 0 := by
  induction n with
  | zero => rfl
  | succ k ih => rw [sl2Invariant_succ a τ hrec k, ih]

end QOU.Mass
