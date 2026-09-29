import QOU.Mass.BindingQHermiteOscillator
import Mathlib.Data.Real.Basic
import Mathlib.Algebra.BigOperators.Group.Finset.Basic

/-!
# QOU.Mass.RogersSzegoInhabited — `FollowsRogersSzego` is non-vacuous

`QOU.Mass.BindingQHermiteOscillator.FollowsRogersSzego` (#2800) is the §3b conjecture class
encoding the standard Rogers–Szegő / continuous q-Hermite three-term recurrence. Its
downstream consequences (q→1 collapse, even/odd vanishing) were proved abstractly, but the
class had **no exhibited model** — so those theorems were conditional on inhabitation.

This file closes that: the sequence **defined by** the recurrence is a concrete
`FollowsRogersSzego` instance, so the class is **satisfiable** (the conjecture is not
vacuously unsatisfiable), and the abstract consequences now apply to a real witness.

Sibling PR #2822 independently identified `a_D^(n)=lw(n−1)` as the q-deformed involution
number — a q-Hermite **moment** — pointing the z2bn binding kernel `R(q,x)` at exactly this
family; the inhabited recurrence here is the Lean home of that kernel.

Ground ring `ℝ`. Self-contained (imports only `BindingQHermiteOscillator`).
-/

namespace QOU.Mass.BindingQHermiteOscillator

/-- The **Rogers–Szegő sequence defined by its three-term recurrence**
`H_0 = 1`, `H_1 = 1+t`, `H_{n+2} = (1+t)H_{n+1} − (1−q^{n+1})·t·H_n`. -/
noncomputable def rsSeq (q t : ℝ) : ℕ → ℝ
  | 0 => 1
  | 1 => 1 + t
  | (n + 2) => (1 + t) * rsSeq q t (n + 1) - (1 - q ^ (n + 1)) * t * rsSeq q t n

/-- **`FollowsRogersSzego` is inhabited.** `rsSeq` satisfies the recurrence by construction,
so the §3b conjecture class has a concrete model — it is non-vacuous, and all of its abstract
consequences (`rogers_szego_q_one_first_order`, `rogers_szego_odd_vanishes_at_neg_one`, …) now
hold of a real witness. -/
instance instFollowsRogersSzego (q t : ℝ) : FollowsRogersSzego (rsSeq q t) t q where
  recurrence _ := rfl

/-- **q→1: the Rogers–Szegő sequence is the binomial `(1+t)^n`.** At `q = 1` the coefficient
`1 − q^{m+1}` vanishes, collapsing the recurrence to `H_{n+1} = (1+t)·H_n`; with `H_0 = 1`
this gives `rsSeq 1 t n = (1+t)^n`, the classical (un-deformed) Rogers–Szegő. Marked `@[simp]`
so the simplifier reduces `rsSeq 1 t n` to its closed form downstream (per Gemini review, #2842). -/
@[simp]
theorem rsSeq_q_one (t : ℝ) : ∀ n, rsSeq 1 t n = (1 + t) ^ n
  | 0 => by simp [rsSeq]
  | 1 => by simp [rsSeq, pow_one]
  | (n + 2) => by
    rw [rsSeq, rsSeq_q_one t (n + 1), rsSeq_q_one t n]
    simp only [one_pow, sub_self, zero_mul, sub_zero]
    ring

/-- **`H_2(t;q) = 1 + (1+q)·t + t²`** for the standard Rogers–Szegő — the middle coefficient is
the **standard** quantum integer `[2]_q = 1+q` (contrast the *balanced* `q+q⁻¹` of
`QGaussianBinomialPascal.rogersSzego_two`; this is the normalization that obeys the
`FollowsRogersSzego` recurrence). -/
theorem rsSeq_two (q t : ℝ) : rsSeq q t 2 = 1 + (1 + q) * t + t ^ 2 := by
  show (1 + t) * rsSeq q t 1 - (1 - q ^ 1) * t * rsSeq q t 0 = _
  simp only [rsSeq, pow_one]
  ring

/-- **The odd terms of the inhabited model vanish at `t = −1`** — `rsSeq q (−1) (2j+1) = 0`.
The abstract even/odd-vanishing theorem (`rogers_szego_odd_vanishes_at_neg_one`, #2800) applied
to the concrete `FollowsRogersSzego` model `rsSeq`: its boundary value `rsSeq q (−1) 1 = 1+(−1) = 0`
discharges the hypothesis, so the q-deformed even/odd parity holds of a real witness. -/
theorem rsSeq_odd_vanishes_at_neg_one (q : ℝ) (j : ℕ) : rsSeq q (-1) (2 * j + 1) = 0 := by
  have hH1 : rsSeq q (-1) 1 = 0 := by simp [rsSeq]
  exact rogers_szego_odd_vanishes_at_neg_one (rsSeq q (-1)) q hH1 j

/-- **Two-step recurrence at `t = −1`.** Setting `t = −1` kills the `(1+t)` head of the
three-term recurrence, leaving the telescoping two-step `H_{n+2} = (1 − q^{n+1})·H_n`. -/
theorem rsSeq_neg_one_step (q : ℝ) (n : ℕ) :
    rsSeq q (-1) (n + 2) = (1 - q ^ (n + 1)) * rsSeq q (-1) n := by
  rw [rsSeq]; ring

/-- **The even terms of the inhabited model at `t = −1` are the `q`-shifted factorial
`(q; q²)_j`** — `rsSeq q (−1) (2j) = ∏_{i<j} (1 − q^{2i+1})`. Unrolling the two-step
recurrence `rsSeq_neg_one_step` on the even subsequence gives the explicit finite product
`(1−q)(1−q³)⋯(1−q^{2j−1})`, the q-Pochhammer `(q; q²)_j`, written self-contained as a
`Finset.prod` (no dependency on Mathlib's `QPochhammer`). Together with
`rsSeq_odd_vanishes_at_neg_one` this is the full closed form of the inhabited Rogers–Szegő
model at the binding anchor `t = −1`. -/
theorem rsSeq_even_at_neg_one (q : ℝ) (j : ℕ) :
    rsSeq q (-1) (2 * j) = ∏ i ∈ Finset.range j, (1 - q ^ (2 * i + 1)) := by
  induction j with
  | zero => simp [rsSeq]
  | succ j ih =>
    have h2 : 2 * (j + 1) = 2 * j + 2 := by ring
    rw [h2, rsSeq_neg_one_step q (2 * j), ih, Finset.prod_range_succ]
    ring

end QOU.Mass.BindingQHermiteOscillator
