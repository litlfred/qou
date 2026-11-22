import Mathlib.Tactic
import QOU.Mass.QDifferenceConfluentObstruction

/-!
# QOU.Mass.FibreMonodromyOrderTwo — the fibre root of unity is `-1`, and C1 dies there

Wall W1 (`qou-d8de`) asks for a q-difference prolongation `D_q` built from the colour
spectral curve `Σ : P(X,z) = 0`. Its **route 2** reads, verbatim:

> *Root-of-unity fibre monodromy. The fibre singularity is a root of unity; a
> q-difference connection may arise naturally from its local monodromy.*

Route 1 (a q-shift on the base, `z ↦ q²z`) is closed in all three charts it could
have lived in — the base coordinate (`QOU.Mass.ColorCubicIrreducible`, PR #6695), the
ramified local coordinate (`QOU.Mass.IrreducibleCubicNoQuadraticRoot`, PR #6738), and
`Σ` itself (`QOU.Mass.DilationBranchLocusRigidity`, PR #6769). So route 2 is the live
one, and this file asks the question that comes *before* any construction: **which
root of unity can that datum actually supply?**

## The two halves

**(1) No total branch point** — `colorCubic_no_triple_root`. Over any field of
characteristic zero the colour cubic `X³ + (z+1)X² + (z²+z+1)X + (z³+z²+z+1)` has no
triple root, for **any** `z`. Matching against `(X − r)³` gives three coefficient
equations; eliminating `r` from the first two forces `2z² + z + 2 = 0`, and from the
first and third `26z³ + 24z² + 24z + 26 = 0`, and those two have no common solution
(they reduce to `15z = 30` and then `12 = 0`).

Geometrically: a branch point of the 3-sheeted cover is where sheets collide, and
"three sheets collide" is exactly "the fibre cubic has a triple root". Since that never
happens, **every branch point is simple** — precisely two sheets meet — so the local
monodromy is a *transposition*, of order exactly `2`. The only root of unity the fibre
datum supplies is therefore `-1`: never a primitive cube root, never anything higher.

**The covering-space step is stated here in prose and is NOT formalised** — Mathlib has
no monodromy of a branched cover of Riemann surfaces in usable form. What is formalised
is the algebraic fact it rests on (no triple root), exactly as
`DilationBranchLocusRigidity` formalises the coefficient identity under its own
unformalised "σ permutes the branch locus" step.

**(2) C1 is unavailable at `q = -1`** — `c1_hypothesis_fails_at_neg_one`. The quantum
integers collapse: `qint (-1) (2k) = 0` and `qint (-1) (2k+1) = 1`. The C1 carrier
`QDifferenceConfluentObstruction.qlift_normalized_kernel_exists` carries the standing
hypothesis `∀ k, 1 ≤ k → qint q k ≠ 0`, and `qint (-1) 2 = 0` **falsifies it**. So the
carrier theorem is not merely degenerate at `q = -1`; it does not apply at all.

`c1_undetermined_of_qint_eq_zero` says what goes wrong independently of that
hypothesis: when the leading coefficient vanishes, `[m+2]_q · b_{m+2} = b_{m+1} + b_m`
holds for one value of `b_{m+2}` iff it holds for every value, so it is a constraint on
`b_{m+1}, b_m` rather than a recurrence determining `b_{m+2}`.

## Scope (fixed before the argument was run)

**Scope (b)**, with the invariants cited above, applies to exactly one identification:
*`q` = the eigenvalue of the local fibre monodromy*. Every looser reading of route 2
stays **open at scope (a) at most** — in particular a q-difference structure that uses
the monodromy *representation* without setting `q` to an eigenvalue, one built at
`z = ∞`, or one from the global `S₃` rather than a local generator. Route 3
(Ramis–Sauloy–Zhang / Sauloy) is untouched.

Nothing here constructs `D_q`; this removes a reading of a route. No fit, nothing wired.

Ground ring: `[Field K] [CharZero K]` (§7c). Characteristic zero is used only to know
`15 ≠ 0` and `12 ≠ 0`; nothing archimedean appears.

-- Ref: [leitner2026] docs/audits/2026-09-05-w1-dilation-does-not-lift-to-sigma.md (W1 route 1, all three charts)
-/

namespace QOU.Mass.FibreMonodromyOrderTwo

open Finset QOU.Mass.QDifferenceConfluentObstruction

variable {K : Type*} [Field K]

/-! ### Part 1 — the colour cubic never has a triple root -/

section NoTripleRoot

variable [CharZero K]

/-- **No total branch point.** If the colour cubic `X³ + (z+1)X² + (z²+z+1)X +
(z³+z²+z+1)` equalled `(X − r)³` — i.e. if all three sheets collided over `z` — its
coefficients would satisfy the three hypotheses below. They are inconsistent, for every
`z` and every `r`.

Consequently every branch point of the 3-sheeted cover is **simple**: exactly two
sheets meet, so the local monodromy is a transposition of order `2`. -/
theorem colorCubic_no_triple_root (z r : K)
    (hc2 : z + 1 = -3 * r)
    (hc1 : z ^ 2 + z + 1 = 3 * r ^ 2)
    (hc0 : z ^ 3 + z ^ 2 + z + 1 = -r ^ 3) : False := by
  -- Eliminating `r` between the quadratic and linear coefficients.
  have hA : 2 * z ^ 2 + z + 2 = 0 := by
    linear_combination 3 * hc1 - (z + 1 - 3 * r) * hc2
  -- Eliminating `r` between the constant and linear coefficients.
  have hB : 26 * z ^ 3 + 24 * z ^ 2 + 24 * z + 26 = 0 := by
    linear_combination 27 * hc0 - ((z + 1) ^ 2 - 3 * r * (z + 1) + 9 * r ^ 2) * hc2
  -- The two are simultaneously solvable only at `z = 2` …
  have hz : (15 : K) * z = 30 := by
    linear_combination (26 * z + 11) * hA - 2 * hB
  have hz2 : z = 2 := by
    have h15 : (15 : K) ≠ 0 := by norm_num
    apply mul_left_cancel₀ h15
    rw [hz]; norm_num
  -- … where the quadratic elimination reads `12 = 0`.
  rw [hz2] at hA
  norm_num at hA

end NoTripleRoot

/-! ### Part 2 — the quantum integers at `q = -1`, and what that does to C1 -/

/-- At `q = -1` the **even** quantum integers vanish: `[2k]_{-1} = 0`. -/
theorem qint_neg_one_two_mul (k : ℕ) : qint (-1 : K) (2 * k) = 0 := by
  induction k with
  | zero => simp [qint]
  | succ n ih =>
      have h : 2 * (n + 1) = (2 * n) + 1 + 1 := by ring
      rw [h, qint, Finset.sum_range_succ, Finset.sum_range_succ]
      rw [qint] at ih
      rw [ih]
      have : ((-1 : K)) ^ (2 * n) = 1 := by
        rw [pow_mul]; norm_num
      rw [this]
      have h2 : ((-1 : K)) ^ (2 * n + 1) = -1 := by
        rw [pow_succ, pow_mul]; norm_num
      rw [h2]; ring

/-- At `q = -1` the **odd** quantum integers are `1`: `[2k+1]_{-1} = 1`. -/
theorem qint_neg_one_two_mul_succ (k : ℕ) : qint (-1 : K) (2 * k + 1) = 1 := by
  rw [qint, Finset.sum_range_succ]
  have ih := qint_neg_one_two_mul (K := K) k
  rw [qint] at ih
  rw [ih]
  have : ((-1 : K)) ^ (2 * k) = 1 := by rw [pow_mul]; norm_num
  rw [this]; ring

/-- The instance that matters: `[2]_{-1} = 0`. -/
theorem qint_neg_one_two : qint (-1 : K) 2 = 0 := by
  have := qint_neg_one_two_mul (K := K) 1
  simpa using this

/-- **The C1 carrier's standing hypothesis is FALSE at `q = -1`.**

`QDifferenceConfluentObstruction.qlift_normalized_kernel_exists` — the proved binding
q-difference carrier `[n+2]_q·b_{n+2} = b_{n+1} + b_n` — assumes
`∀ k, 1 ≤ k → qint q k ≠ 0`. At the value route 2's fibre monodromy supplies, that
assumption does not hold, so the carrier theorem does not apply. -/
theorem c1_hypothesis_fails_at_neg_one :
    ¬ (∀ k : ℕ, 1 ≤ k → qint (-1 : K) k ≠ 0) := by
  intro h
  exact h 2 (by norm_num) qint_neg_one_two

/-- **A vanishing leading coefficient makes C1 a constraint, not a recurrence.**

If `[n+2]_q = 0` then the C1 equation holds for one candidate value of `b_{n+2}` iff it
holds for every candidate value — so it carries no information about `b_{n+2}`. This is
independent of the carrier theorem's hypothesis; it is what that hypothesis exists to
prevent. -/
theorem c1_undetermined_of_qint_eq_zero (q : K) (n : ℕ)
    (hz : qint q (n + 2) = 0) (rhs c c' : K) :
    (qint q (n + 2) * c = rhs) ↔ (qint q (n + 2) * c' = rhs) := by
  rw [hz]; simp

/-- The two halves joined: at the fibre-monodromy value `q = -1`, C1's leading
coefficient vanishes for every **even** index, so on that whole subsequence the carrier
determines nothing. -/
theorem c1_undetermined_at_neg_one (k : ℕ) (rhs c c' : K) :
    (qint (-1 : K) (2 * k + 2) * c = rhs) ↔ (qint (-1 : K) (2 * k + 2) * c' = rhs) := by
  refine c1_undetermined_of_qint_eq_zero (-1 : K) (2 * k) ?_ rhs c c'
  have h : 2 * k + 2 = 2 * (k + 1) := by ring
  rw [h]
  exact qint_neg_one_two_mul (K := K) (k + 1)

end QOU.Mass.FibreMonodromyOrderTwo
