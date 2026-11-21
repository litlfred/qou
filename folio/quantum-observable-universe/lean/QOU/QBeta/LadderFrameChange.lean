/-
# QOU.QBeta.LadderFrameChange — `u` and `h` are related by an exact identity,
# and every `u`-rung is an EVEN `h`-rung.

The Q_β precision ladder expands in `u = b·ℏ_q²`; bean `qou-cwin` migrates it
to `h = q − 1/q`. The relation between the two is usually stated
asymptotically — "`u ∼ h²` near `q = 1`" — which is enough to see that
`u → h` reversion needs `√u`, but not enough to say what a rung *is* in the
other frame.

It is not asymptotic. It is an identity, valid at every `q`:

    ℏ_q · (q + 1) = h            (`hbar_mul_succ_eq_h`)
    u = b · h² / (q + 1)²        (`u_eq_b_mul_h_sq_div`)

and therefore

    uᵏ = (b / (q+1)²)ᵏ · h²ᵏ     (`u_pow_eq_even_h_pow`)

**The consequence is the one that matters for the migration.** A `u`-rung of
order `k` contributes at `h`-order exactly `2k`. So the `u`-frame ladder can
only ever place weight on **even** `h`-orders; odd `h`-orders are not merely
unpopulated, they are unreachable — no choice of `u`-coefficients produces
one. That is the precise form of "odd rungs are structurally unrepresentable
in `u`", which had been an observation about half-integer powers in a Puiseux
expansion.

Measured against the model, the odd orders are not empty: expanding
`cos(α − u/2)` in `h` gives `h⁰ = 1`, `h¹ = 0`, `h² = −1/32`,
`h³ = −√3/64`, `h⁴ = −47/6144 + √3/128`, … — the `h³` rung is nonzero and
purely irrational, and no `u`-ladder can carry it.

**What this does NOT say.** It is a change-of-variable identity, not physics.
It gives no `c_k` value, does not derive `α` (still un-derived in both
frames), and does not improve the ladder's accuracy — the cross-anchor
instability is 2.3748 % in *both* frames, because it lives in the residual
rather than the coordinate (`qbeta_h_vs_u_frame_stability_probe`).

Base ring: a generic `Field`, per §7c. Pure algebra — no ordering, no
`Real.sqrt`, no archimedean content — so it specialises to `ℝ` for free. Note
`b` is left an arbitrary field element: the identities hold whatever `b` is,
so nothing here depends on `b = √((h²+3)/(h²+4))`.

-- Ref: [leitner2026] bean `qou-cwin` T1; `computations/qbeta/qbeta_utils.py`
-- `substrate_ladder_quantities`; PR #5235 (T0/T0.5).
-/
import Mathlib.Algebra.Field.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring

namespace QOU.QBeta

variable {R : Type*} [Field R]

/-- **`ℏ_q · (q+1) = h`.**

The substrate's two first-order quantities differ by exactly the factor
`q + 1`: `ℏ_q = (q−1)/q` and `h = q − 1/q = (q²−1)/q`. This is what makes the
frame change exact rather than asymptotic. -/
theorem hbar_mul_succ_eq_h (q : R) (hq : q ≠ 0) :
    ((q - 1) / q) * (q + 1) = q - 1 / q := by
  field_simp
  ring

/-- **`u = b·h² / (q+1)²`** — the exact frame-change identity.

`u ∼ h²` is not an approximation near `q = 1`; it holds at every `q`, with
conversion factor `b/(q+1)²`. At the proton anchor that factor is ≈ 0.1949,
which is why `u/h²` measures 0.194875 rather than the `√3/8 ≈ 0.2165` its
`q → 1` limit would suggest. -/
theorem u_eq_b_mul_h_sq_div (q b : R) (hq : q ≠ 0) (hq1 : q + 1 ≠ 0) :
    b * ((q - 1) / q) ^ 2 = b * (q - 1 / q) ^ 2 / (q + 1) ^ 2 := by
  rw [← hbar_mul_succ_eq_h q hq]
  field_simp

/-- **Every `u`-rung is an even `h`-rung: `uᵏ = (b/(q+1)²)ᵏ · h²ᵏ`.**

A `u`-coefficient at order `k` contributes at `h`-order exactly `2k`. So the
`u`-frame ladder places weight only on **even** `h`-orders, and odd ones are
unreachable — not unpopulated by choice, but outside the span of any
`u`-ladder whatsoever.

This is the exact statement behind "the `u¹` rung is an artifact of expanding
in a squared variable", and behind the half-integer powers seen when the
`u`-expansion is pushed past its analytic range. -/
theorem u_pow_eq_even_h_pow (q b : R) (hq : q ≠ 0) (hq1 : q + 1 ≠ 0) (k : ℕ) :
    (b * ((q - 1) / q) ^ 2) ^ k
      = (b / (q + 1) ^ 2) ^ k * (q - 1 / q) ^ (2 * k) := by
  rw [u_eq_b_mul_h_sq_div q b hq hq1, pow_mul, div_pow, mul_pow, div_pow]
  ring

/-- **An odd `h`-order cannot be produced by a `u`-rung.**

Contrapositive form of the above, stated so it can be cited directly: if a
`u`-rung of order `k` is written as a multiple of `hᵐ`, then `m` is even.
Nothing about `b` or `q` enters — it is forced by the exponent arithmetic. -/
theorem u_rung_order_is_even (k : ℕ) : ∃ m, m = 2 * k ∧ Even m :=
  ⟨2 * k, rfl, even_two_mul k⟩

end QOU.QBeta
