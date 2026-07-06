import Mathlib.Algebra.Field.Basic
import Mathlib.Tactic.Ring
import Mathlib.Tactic.LinearCombination

/-!
# QOU.Mass.BindingQHermiteOscillator — the Rogers–Szegő / continuous q-Hermite family

The third natural recurrence family around the binding keystone (answering "what q-difference
structures come out naturally — **not limited to q-Bessel**"). Where `BindingHyperbolicRecurrence`
gives the hyperbolic cosh/sinh tower (Layer 1) and `BindingQBesselKernel` the super-exponential
q-Bessel tower (Layer 2), the **Rogers–Szegő polynomials** `H_n(t;q) = Σ_{k=0}^n [n;k]_q t^k`
(equivalently the continuous q-Hermite, the q-oscillator bound-state basis) sit between them: a
**q-deformation of the harmonic-oscillator / Hermite** basis whose `q → 1` limit is the binomial
`(1+t)^n` and, after the standard rescaling, the Hermite functions — whose own classical tower is
the cosh/sinh of Layer 1.

This file records the family as a §3b recurrence *class* (the standard three-term recurrence is
the hypothesis) and proves two structural consequences:

* **`q → 1` collapse** to the first-order binomial recurrence — the classical (un-q-deformed) limit;
* **even/odd decoupling at `t = −1`** — the recurrence becomes two-step `H_{n+2} = (1−q^{n+1})H_n`,
  so with the boundary value `H_1(−1;q) = 0` *all odd terms vanish*. This is the **q-deformed
  even/odd parity**: the q-oscillator analogue of the cosh (even) / sinh (odd) split of
  `NaStokesKeystone` and `BindingHyperbolicRecurrence`, now at the level of the q-Hermite basis.

Standard reference recurrence (Rogers–Szegő):
`H_{n+1}(t;q) = (1+t)·H_n(t;q) − (1−q^n)·t·H_{n−1}(t;q)`.

Ground ring: a generic field (the family is **fibre-level / q-formal**, §7c — no archimedean
evaluation). The recurrence is the conjectural/definitional input; the consequences are derived. -/

namespace QOU.Mass.BindingQHermiteOscillator

variable {K : Type*} [Field K]

/-- **The Rogers–Szegő / continuous q-Hermite three-term recurrence, as a class.** `H n` is the
`n`-th polynomial value `H_n(t;q)`; the field is the standard recurrence (shifted to avoid `n−1`):
`H_{m+2} = (1+t)·H_{m+1} − (1−q^{m+1})·t·H_m`. The q-oscillator bound-state basis recurrence. -/
class FollowsRogersSzego (H : ℕ → K) (t q : K) : Prop where
  /-- The Rogers–Szegő three-term recurrence (with `n = m+1`). -/
  recurrence : ∀ m, H (m + 2) = (1 + t) * H (m + 1) - (1 - q ^ (m + 1)) * t * H m

/-- **`q → 1` collapse to the binomial first-order recurrence.** At `q = 1` the coefficient
`1 − q^{m+1}` vanishes, so the three-term recurrence degenerates to `H_{m+2} = (1+t)·H_{m+1}` —
the recurrence of the ordinary binomial `H_n = (1+t)^n·H_0`, the classical (un-deformed) limit of
Rogers–Szegő. -/
theorem rogers_szego_q_one_first_order (H : ℕ → K) (t : K)
    [inst : FollowsRogersSzego H t 1] (m : ℕ) :
    H (m + 2) = (1 + t) * H (m + 1) := by
  have h := inst.recurrence m
  simpa using h

/-- **Even/odd decoupling at `t = −1`.** Setting `t = −1` annihilates the `(1+t)` term, so the
recurrence becomes the **two-step** relation `H_{m+2} = (1 − q^{m+1})·H_m` linking same-parity
indices only. This is the algebraic source of the q-Hermite even/odd parity. -/
theorem rogers_szego_t_neg_one_two_step (H : ℕ → K) (q : K)
    [inst : FollowsRogersSzego H (-1) q] (m : ℕ) :
    H (m + 2) = (1 - q ^ (m + 1)) * H m := by
  have h := inst.recurrence m
  rw [h]; ring

/-- **The odd Rogers–Szegő terms vanish at `t = −1`** (`H_{2j+1}(−1;q) = 0`), given the boundary
value `H_1(−1;q) = 0` (which holds since `H_1(t;q) = 1 + t`). By the two-step decoupling above,
the odd-index subsequence is `0` for all `j`. This is the **q-deformed even/odd parity**: the
q-oscillator analogue of "`sinh` is the odd channel" — the odd sector collapses, leaving the even
(cosh-like) Rogers–Szegő tower, exactly mirroring the bar-even/bar-odd split of `NaStokesKeystone`. -/
theorem rogers_szego_odd_vanishes_at_neg_one (H : ℕ → K) (q : K)
    [inst : FollowsRogersSzego H (-1) q] (hH1 : H 1 = 0) (j : ℕ) :
    H (2 * j + 1) = 0 := by
  induction j with
  | zero => simpa using hH1
  | succ j ih =>
    rw [show 2 * (j + 1) + 1 = (2 * j + 1) + 2 from by ring,
      rogers_szego_t_neg_one_two_step H q (2 * j + 1), ih, mul_zero]

end QOU.Mass.BindingQHermiteOscillator
