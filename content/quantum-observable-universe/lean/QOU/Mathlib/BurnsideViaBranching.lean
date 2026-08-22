import Mathlib.Algebra.BigOperators.Ring.Finset
import Mathlib.Algebra.Order.BigOperators.Ring.Finset
import Mathlib.Tactic

/-!
# `Σ_λ (f^λ)² = n!` without RSK — the branching induction

`QOU/Mathlib/RSKBurnsideTarget.lean` states the Burnside identity
`∑_{λ ⊢ n} dim(λ)² = n!` and records its proof as

> "the RSK correspondence `S_n ≃ Σ_λ SYT(λ)²` (absent from pinned Mathlib; the
> multi-session next step)"

with the general-`n` case open (the `decide`-verified range reaches `n ≤ 12`).

**RSK is not needed.** The identity follows by induction from the two branching
rules on the Young lattice, and this file supplies the inductive step in the form
that consumes them:

* **down** — `f^λ = Σ_{μ ↗ λ} f^μ`: an SYT of `λ` puts its largest entry in some
  corner, so removing that corner is a bijection onto `⨆_μ SYT(μ)`. This is
  essentially the defining recursion of the SYT count, not a theorem about
  representations.
* **up** — `Σ_{λ ⊐ μ} f^λ = n · f^μ` for `μ ⊢ n−1`. The one with content; it is
  the `DU − UD = I` relation of Stanley's differential-poset formulation.

Given both, `Σ_{λ ⊢ n} (f^λ)² = n · Σ_{μ ⊢ n−1} (f^μ)²`, and induction from
`Σ_{λ ⊢ 0} = 1` gives `n!`.

Verified numerically for `n ≤ 10` (both branching rules at every `μ`, and the
resulting recursion) before formalising.

## What this file proves

`sum_sq_step`, stated for an abstract bipartite incidence so it depends on **no**
Young-diagram infrastructure: two finite levels `A`, `B`, an incidence
`I ⊆ A ×ˢ B`, a weight `f`, and the two branching hypotheses give

    ∑_{l ∈ B} (f l)² = c · ∑_{m ∈ A} (f m)².

The proof is a Fubini exchange over `I`. `sum_sq_factorial_of_step` then iterates
it to `n!`.

## What is hypothesis, and what is left

`hdown` and `hup` are hypotheses. Instantiating them for the Young lattice —
`A = shapes (n−1)`, `B = shapes n`, `I` the covering relation, `f = #SYT` — is the
remaining work, and **`hup` is the only mathematically substantial part**. That
is a much smaller target than constructing the RSK bijection: it is one identity
about corner-addition counts, where RSK is a bijection between `S_n` and pairs of
tableaux.

Per AGENTS.md §"Axiomatization is NOT a Proof", carrying `hup` as a hypothesis
does not establish it; the contribution here is that the *route* avoids RSK.

## A second route is further along — read this before investing here

Bean `qou-3c2j` (sibling, landing through PRs #5139 / #5151 / #5156) is building
the same identity by the **representation-theoretic** route, and is closer: the
regular module decomposes into isotypic components, each of type `S^μ`, with
multiplicity `m_μ = dim Hom_G(k[G], S^μ) = dim S^μ` — the first equality from
Schur orthonormality (`SpechtSchurDiagonal.finrank_homG_specht`, landed
sorry-free), the second from `MathlibExt.RegularHom.homGRegularEquiv` (landed
sorry-free). Then `n! = dim_k k[S_n] = Σ_μ m_μ · dim S^μ = Σ_μ (dim S^μ)²`. As
that bean records, the identity comes out as a **conclusion**, so it would retire
the `sorryAx` in `OVTopAssembly.sum_numSYT_sq_eq_factorial` rather than route
around it. One brick remains there: turning `sSup_isotypicComponents` into a
`finrank` sum indexed by `PartitionIndex n`.

This file is therefore kept as an **independent second route**, not as the
primary attack, and its remaining obligation (`hup`) is the larger of the two.
Its standing value is that it is representation-theory-free: the branching
induction needs no Specht module, no semisimplicity, and no character theory —
only two counting rules on the Young lattice. If the isotypic route closes first,
the honest use of this file is to *verify* that result from the combinatorial
side, per AGENTS.md §"converge on landing".

## Base ring

`ℕ` throughout — the identity is about counts, and no subtraction or ordering
beyond `Finset` sums is used.

-- Ref: [stanley1999] https://doi.org/10.1017/CBO9780511609589
-- Ref: [manuscript] QOU/Mathlib/RSKBurnsideTarget.lean
-/

namespace QOU.Mathlib

open Finset

/-- **The inductive step, abstractly.** Two finite levels `A` and `B` joined by an
incidence `I`, with

* `hdown` — each `l ∈ B` has weight equal to the total weight of its
  `I`-predecessors in `A`;
* `hup` — each `m ∈ A` has `I`-successors in `B` of total weight `c · f m`;

then the weighted square-sums are related by the same factor `c`.

Instantiated on the Young lattice with `f = #SYT` and `c = n`, this is
`Σ_{λ ⊢ n} (f^λ)² = n · Σ_{μ ⊢ n−1} (f^μ)²`. -/
theorem sum_sq_step {σ : Type*} [DecidableEq σ]
    (A B : Finset σ) (I : Finset (σ × σ)) (f : σ → ℕ) (c : ℕ)
    (hdown : ∀ l ∈ B, ∑ m ∈ A.filter (fun m => (m, l) ∈ I), f m = f l)
    (hup : ∀ m ∈ A, ∑ l ∈ B.filter (fun l => (m, l) ∈ I), f l = c * f m) :
    ∑ l ∈ B, (f l) ^ 2 = c * ∑ m ∈ A, (f m) ^ 2 := by
  have key : ∑ l ∈ B, f l * (∑ m ∈ A.filter (fun m => (m, l) ∈ I), f m)
      = ∑ m ∈ A, f m * (∑ l ∈ B.filter (fun l => (m, l) ∈ I), f l) := by
    simp only [Finset.mul_sum, Finset.sum_filter]
    rw [Finset.sum_comm]
    refine Finset.sum_congr rfl (fun m _ => Finset.sum_congr rfl (fun l _ => ?_))
    by_cases h : (m, l) ∈ I <;> simp [h, mul_comm]
  calc ∑ l ∈ B, (f l) ^ 2
      = ∑ l ∈ B, f l * (∑ m ∈ A.filter (fun m => (m, l) ∈ I), f m) := by
        refine Finset.sum_congr rfl (fun l hl => ?_)
        rw [hdown l hl, sq]
    _ = ∑ m ∈ A, f m * (∑ l ∈ B.filter (fun l => (m, l) ∈ I), f l) := key
    _ = ∑ m ∈ A, c * (f m) ^ 2 := by
        refine Finset.sum_congr rfl (fun m hm => ?_)
        rw [hup m hm, sq]; ring
    _ = c * ∑ m ∈ A, (f m) ^ 2 := by rw [Finset.mul_sum]

/-- **Iterating the step gives the factorial.** A level-indexed family whose
square-sums satisfy `S (n+1) = (n+1) · S n` with `S 0 = 1` is `n!`. Combined with
`sum_sq_step` at each level, this is the Burnside identity. -/
theorem sum_sq_factorial_of_step (S : ℕ → ℕ) (h0 : S 0 = 1)
    (hstep : ∀ n, S (n + 1) = (n + 1) * S n) : ∀ n, S n = Nat.factorial n := by
  intro n
  induction n with
  | zero => simpa using h0
  | succ n ih => rw [hstep n, ih, Nat.factorial_succ]

/-- **Non-vacuity of the step.** The hypotheses are satisfiable: a single-element
level on each side with the unique incidence, weight `1`, and `c = 1`. -/
example : ∑ l ∈ ({0} : Finset ℕ), (fun _ : ℕ => 1) l ^ 2
    = 1 * ∑ m ∈ ({0} : Finset ℕ), (fun _ : ℕ => 1) m ^ 2 := by simp

end QOU.Mathlib
