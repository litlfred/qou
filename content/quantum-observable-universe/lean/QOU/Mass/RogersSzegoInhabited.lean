import QOU.Mass.BindingQHermiteOscillator
import Mathlib.Data.Real.Basic

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
this gives `rsSeq 1 t n = (1+t)^n`, the classical (un-deformed) Rogers–Szegő. -/
theorem rsSeq_q_one (t : ℝ) : ∀ n, rsSeq 1 t n = (1 + t) ^ n
  | 0 => by simp [rsSeq]
  | 1 => by simp [rsSeq, pow_one]
  | (n + 2) => by
    rw [rsSeq, rsSeq_q_one t (n + 1), rsSeq_q_one t n]
    simp only [one_pow, sub_self, zero_mul, sub_zero]
    ring

end QOU.Mass.BindingQHermiteOscillator
