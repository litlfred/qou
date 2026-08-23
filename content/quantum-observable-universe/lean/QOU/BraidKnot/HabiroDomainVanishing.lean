import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Algebra.BigOperators.Ring.Finset
import Mathlib.Order.Interval.Finset.Nat
import Mathlib.Algebra.Ring.Basic
import Mathlib.Algebra.Ring.Defs

/-!
# Why the Habiro ring's domain is the roots of unity — the vanishing mechanism

The keystone's open object is the **archimedean continuation** of a colored
`Σ(2,3,5)` WRT series to the substrate anchor `q₀ ≈ 1.10998` (real, `> 1`). The
2026-08-10 literature pass established, at read tier, that a unified-WRT /
Habiro-ring element does not reach that point. Beliakova–Le (arXiv:1106.6298 §1)
define the Habiro ring as the `(q;q)_k`-adic completion

    Ẑ[q] := lim←_k Z[q] / ((q;q)_k),      (q;q)_k = ∏_{j=1..k} (1 − q^j)

and state: *"Every element f(q) ∈ Ẑ[q] can be considered as a function whose
domain is the set of roots of unity."*

That domain statement is a **cited external theorem**, not formalized here. What
IS formalized here is the *mechanism underneath it*, which is short and entirely
algebraic: an element of the completion is an infinite sum `Σ_k f_k(q)·(q;q)_k`,
and at a root of unity that sum **terminates**, because the q-Pochhammer factor
is eventually zero. Termination is what makes evaluation well-defined there, and
its failure elsewhere is what makes the substrate anchor off-domain.

## What this file proves (sorry-free, generic `CommRing`)

* `qPochSelf q k = ∏_{j ∈ Icc 1 k} (1 - q^j)` — the q-Pochhammer symbol `(q;q)_k`.
* `qPochSelf_eq_zero_of_pow_eq_one` — if `q^n = 1` with `1 ≤ n ≤ k` then
  `(q;q)_k = 0`. **This is the vanishing mechanism.** The proof is one factor:
  the `j = n` term is `1 - q^n = 0`.
* `qPochSelf_eventually_zero` — the same statement as "eventually zero in `k`",
  the form the completion argument actually consumes.
* `qPochSelf_ne_zero_of_no_root_of_unity` — the converse direction that matters
  for the substrate: if **no** `1 ≤ j ≤ k` has `q^j = 1`, then over a domain
  `(q;q)_k ≠ 0`, so the sum does *not* terminate. A real `q₀ > 1` satisfies the
  hypothesis for every `k` (no positive power of a real `> 1` is `1`), so no
  truncation ever occurs there.

## §7c base ring

Deliberately generic `{R : Type*} [CommRing R]` — this is pure algebra about a
finite product, with no ordering, no `Real.sqrt`, and no archimedean content. The
non-vanishing direction needs `NoZeroDivisors` (an `IsDomain`-style hypothesis),
which is the weakest thing that makes "a product is nonzero iff every factor is"
true; it is *not* an archimedean assumption. The statement that the substrate
anchor `q₀ > 1` has no root-of-unity power is archimedean, and is therefore left
to the caller as the explicit hypothesis `hj` rather than baked in here.

## What is deliberately NOT claimed

This file does **not** formalize the Beliakova–Le domain theorem, the
convergence of state integrals (Garoufalidis–Kashaev arXiv:1411.6062 §1.1), or
the closed form `I_{1,2}(1) = (e^{iπ/6}/√3)·2·sinh(Vol(4₁)/2π)`. Those are cited
published results, verified numerically in
`computations/probes/habiro_domain_substrate_anchor_probe.py` and
`computations/probes/qbeta_5two_chirality_state_integral_probe.py` (the latter
reproduces the closed form to 1.1e-19 by independent quadrature). Formalizing
them is not a bean — they are literature, cited with `-- Ref:` where used.

-- Ref: [beliakova-le2011] https://arxiv.org/abs/1106.6298
-- Ref: [garoufalidis-kashaev2015] https://arxiv.org/abs/1411.6062
-/

namespace QOU.BraidKnot

open Finset

variable {R : Type*} [CommRing R]

/-- The q-Pochhammer symbol `(q;q)_k = ∏_{j=1}^{k} (1 - q^j)`, the factor whose
`k`-adic powers define the Habiro ring's completion. -/
def qPochSelf (q : R) (k : ℕ) : R :=
  ∏ j ∈ Finset.Icc 1 k, (1 - q ^ j)

@[simp] theorem qPochSelf_zero (q : R) : qPochSelf q 0 = 1 := by
  simp [qPochSelf]

/-- **The vanishing mechanism.** If `q` is an `n`-th root of unity with
`1 ≤ n ≤ k`, then `(q;q)_k = 0` — the `j = n` factor is `1 - q^n = 0`.

This is why the Habiro ring's elements evaluate at roots of unity: an element is
an infinite sum `Σ_k f_k(q)·(q;q)_k`, and here all but finitely many terms
vanish, so the sum terminates and evaluation is a finite computation. -/
theorem qPochSelf_eq_zero_of_pow_eq_one {q : R} {n k : ℕ}
    (hn : 1 ≤ n) (hq : q ^ n = 1) (hk : n ≤ k) :
    qPochSelf q k = 0 := by
  refine Finset.prod_eq_zero (i := n) ?_ ?_
  · exact Finset.mem_Icc.mpr ⟨hn, hk⟩
  · rw [hq, sub_self]

/-- The same fact in the "eventually zero" form the completion argument consumes:
past `k = n` the q-Pochhammer factor is identically zero. -/
theorem qPochSelf_eventually_zero {q : R} {n : ℕ} (hn : 1 ≤ n) (hq : q ^ n = 1) :
    ∀ k, n ≤ k → qPochSelf q k = 0 :=
  fun _ hk => qPochSelf_eq_zero_of_pow_eq_one hn hq hk

/-- **The converse, and the substrate side.** If no exponent `1 ≤ j ≤ k` makes
`q^j = 1`, then `(q;q)_k ≠ 0` over a ring without zero divisors — so the sum
never truncates and the finite-evaluation argument above is unavailable.

The substrate anchor is exactly this case: a real `q₀ > 1` has `q₀^j > 1` for
every `j ≥ 1`, so the hypothesis holds at every `k`. That archimedean fact is the
caller's to supply — it is not assumed here, keeping this file free of ordering. -/
theorem qPochSelf_ne_zero_of_no_root_of_unity [Nontrivial R] [NoZeroDivisors R]
    {q : R} {k : ℕ} (hj : ∀ j, 1 ≤ j → j ≤ k → q ^ j ≠ 1) :
    qPochSelf q k ≠ 0 := by
  rw [qPochSelf, Finset.prod_ne_zero_iff]
  intro j hjmem
  obtain ⟨h1, h2⟩ := Finset.mem_Icc.mp hjmem
  exact sub_ne_zero_of_ne (fun h => hj j h1 h2 h.symm)

end QOU.BraidKnot
