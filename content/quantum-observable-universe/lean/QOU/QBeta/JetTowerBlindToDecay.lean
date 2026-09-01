/-
# The jet tower is blind to the decay channel

Beans `qou-cds1` / `qou-pdix`. Owner asked whether the ladder's phase might be
hidden in the Gröbner–Shirshov jet tower (`H_k → H_3` branching with q-Plancherel
weights). It cannot be, and the reason is an exact symmetry rather than a
measurement.

## The mechanism

The tower's channel weights are

    w_μ(k) = Σ_{λ ⊢ k} W_λ · mult_μ(λ ↓ H₃),      W_λ = d_q(λ)² / [k]_q!

and `d_q(λ) = [k]_q! / Π_cells [h(c)]_q`, so `W_λ = [k]_q! / (Π_cells [h(c)]_q)²`
depends on λ **only through its multiset of hook lengths**. Transposing a Young
diagram permutes that multiset, so

    W_{λ'} = W_λ    for every λ and every q,

while transposition swaps the trivial and sign branchings,
`mult_{(3)}(λ' ↓ H₃) = mult_{(1³)}(λ ↓ H₃)`. Since `λ ↦ λ'` is an involution of
the partitions of `k`, reindexing gives

    w_sym(k) = w_alt(k)    exactly, for every k and every q.

Verified numerically at 40 dps for `k = 3…9` (residuals ≤ 7.3e-40, and exactly
zero for `k = 3,4,5`), and the hook-multiset invariance checked with **zero
counterexamples** over every partition of every `k ≤ 9`.

## Why that answers the question

The two channels enter the two physical sectors with opposite signs: mass sees
`y₃ + y₍₁³₎`, decay sees `y₃ − y₍₁³₎` (this bean, Step 9 and the Borromean
character computation). So the tower's contribution to the **decay** combination
is `w_sym − w_alt = 0` — identically, at every level. **No phase can hide in the
tower, because the tower contributes nothing at all to the channel that needs
one.**

Note this is a statement about the tower, not about the ladder: it does not touch
the mass sector, where `w_sym + w_alt = 2w_sym` is exactly what the tower's
unbounded growth feeds.

## What is formalised here

`sum_eq_of_involution` — the reindexing step, stated abstractly so it carries the
argument without formalising Young diagrams: if a finite index set carries an
involution under which the weight is invariant and the two multiplicities swap,
the two weighted sums are equal. The two hypotheses it needs are exactly the two
facts checked numerically above.

Scope-(b): a structural exclusion citing a proved identity. Nothing derived,
proposed, wired or readmitted.
-/
import Mathlib.Algebra.BigOperators.Group.Finset.Defs
import Mathlib.Data.Real.Basic

namespace QOU.QBeta

open Finset

/-- **The reindexing that makes the tower blind to decay.** On a finite index set
closed under an involution `t`, if the weight `W` is `t`-invariant and the two
multiplicities swap under `t`, the two weighted sums coincide — so their
*difference*, which is what the decay channel sees, vanishes identically.

Instantiated at `ι =` partitions of `k`, `t =` transpose, `W =` the q-Plancherel
weight (a function of the hook multiset, which transpose permutes) and
`m₁, m₂ =` the trivial and sign branching multiplicities. -/
theorem sum_eq_of_involution {ι : Type*} [DecidableEq ι] (s : Finset ι)
    (t : ι → ι) (ht : ∀ i ∈ s, t i ∈ s) (htt : ∀ i ∈ s, t (t i) = i)
    (W m₁ m₂ : ι → ℝ)
    (hW : ∀ i ∈ s, W (t i) = W i)
    (hm : ∀ i ∈ s, m₁ (t i) = m₂ i) :
    ∑ i ∈ s, W i * m₁ i = ∑ i ∈ s, W i * m₂ i := by
  refine Finset.sum_bij' (fun a _ => t a) (fun a _ => t a) ht ht htt htt ?_
  intro a ha
  have h1 : W (t a) = W a := hW a ha
  have h2 : m₁ (t (t a)) = m₂ (t a) := hm (t a) (ht a ha)
  rw [htt a ha] at h2
  rw [h1, ← h2]

/-- The decay combination therefore vanishes identically at every level. -/
theorem decay_combination_zero {ι : Type*} [DecidableEq ι] (s : Finset ι)
    (t : ι → ι) (ht : ∀ i ∈ s, t i ∈ s) (htt : ∀ i ∈ s, t (t i) = i)
    (W m₁ m₂ : ι → ℝ)
    (hW : ∀ i ∈ s, W (t i) = W i)
    (hm : ∀ i ∈ s, m₁ (t i) = m₂ i) :
    (∑ i ∈ s, W i * m₁ i) - (∑ i ∈ s, W i * m₂ i) = 0 := by
  rw [sum_eq_of_involution s t ht htt W m₁ m₂ hW hm, sub_self]

end QOU.QBeta
