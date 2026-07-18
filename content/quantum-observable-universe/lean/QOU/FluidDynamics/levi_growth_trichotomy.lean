import Mathlib.Data.Real.Basic
import Mathlib.Order.Basic

/-!
# QOU.FluidDynamics.levi_growth_trichotomy — Levi condition-number trichotomy

Refines the `conj:levi-degeneracy` **dichotomy** into an exhaustive **trichotomy**
on the growth exponent of the Levi condition number, per the q-NS gap audit
Finding 3
([`docs/audits/2026-07-18-q-ns-classical-gap-decomposition.md`](../../../../../../docs/audits/2026-07-18-q-ns-classical-gap-decomposition.md)).

## The problem with the dichotomy

`conj:levi-degeneracy` states "*exactly one* of (A) `C_L(κ) = O(1)` / (B)
`C_L(κ) ~ κ`". These are **not complementary**: an intermediate rate
`C_L(κ) ~ κ^β` with `0 < β < 1` satisfies neither, so as written the conjecture
could be vacuously false. The existing `LeviDegeneracy` class encodes only the
degeneracy *set*, not the growth *rate*, so it does not capture the dichotomy at
all.

## The fix

Introduce the growth exponent `β = limsup_κ (log C_L(κ) / log κ) ∈ [0, 1]` and
state the exhaustive trichotomy:

* **β = 0** — `C_L = O(1)`, Levi non-degenerate ⇒ (categorically) NS-singular
  (branch A);
* **β = 1** — `C_L ~ κ`, Levi degenerates / core → sheet ⇒ NS-regular (branch B);
* **0 < β < 1** — marginal `C_L ~ κ^β`, **undetermined** (the window the
  dichotomy silently dropped).

`levi_trichotomy_exhaustive` proves these three cover `[0, 1]`; the branch
implications tie β = 0 / β = 1 to the Levi non-degeneracy predicate that
`yekutieli_levi_unification.lean` connects to the NS obstruction.

## Honest scope

This formalises the **classification structure** — that the correct statement is
a trichotomy and that the marginal window is a genuine third case. It does
**not** compute the actual `β` (which branch the real `C_L(κ)` growth falls
into): that value is the open content of `conj:levi-degeneracy` and, via
Bridge B, the Clay problem.

## Base ring (§7c)
Archimedean: `β` and `C_L` are real (a `limsup` of real log-ratios, an order
comparison). `ℝ` is correct — this block is on the archimedean side of the wall.

## References
- [manuscript] fluid-dynamics/levi-degeneracy-conjecture (`conj:levi-degeneracy`),
  core-levi-form, ns-obstruction-tower
-/

namespace QOU.FluidDynamics

/-- Growth-rate data for the Levi condition number `C_L(κ)` along the
    root-of-unity ladder `q_κ = e^{iπ/κ}`, refining `conj:levi-degeneracy`.

    `beta = limsup_κ log C_L(κ) / log κ` is the growth exponent, assumed in
    `[0, 1]` (the bounded-rate regime: `C_L` grows no faster than linearly). The
    two branch fields carry the manuscript's dichotomy *implications*; the
    marginal window `0 < β < 1` is left open (no field forces it either way). -/
structure LeviGrowthTrichotomy where
  /-- The Levi condition number `C_L(κ)` at ladder step `κ`. -/
  condNumber : ℕ → ℝ
  /-- Growth exponent `β = limsup_κ log C_L(κ) / log κ`. -/
  beta : ℝ
  /-- **Bounded-rate regime:** `0 ≤ β ≤ 1` (`C_L` grows no faster than `κ`). -/
  beta_mem : 0 ≤ beta ∧ beta ≤ 1
  /-- "Levi form non-degenerate along the ladder" (both eigenvalues positive). -/
  leviNonDegenerate : Prop
  /-- **Branch A:** `β = 0` (`C_L = O(1)`) ⇒ Levi non-degenerate (NS-singular). -/
  branchA : beta = 0 → leviNonDegenerate
  /-- **Branch B:** `β = 1` (`C_L ~ κ`) ⇒ Levi degenerates (NS-regular). -/
  branchB : beta = 1 → ¬ leviNonDegenerate

/-- **The trichotomy is exhaustive on `[0, 1]`.** Every bounded-rate exponent
    falls into exactly one of `β = 0`, `0 < β < 1`, `β = 1` — so the original
    two-branch dichotomy (`β = 0` xor `β = 1`) is *not* a valid partition; the
    marginal window `0 < β < 1` is the missing third case. -/
-- Ref: [manuscript] fluid-dynamics/levi-degeneracy-conjecture (Finding 3)
theorem levi_trichotomy_exhaustive (T : LeviGrowthTrichotomy) :
    T.beta = 0 ∨ (0 < T.beta ∧ T.beta < 1) ∨ T.beta = 1 := by
  obtain ⟨h0, h1⟩ := T.beta_mem
  rcases eq_or_lt_of_le h0 with h | h
  · exact Or.inl h.symm
  · rcases eq_or_lt_of_le h1 with h' | h'
    · exact Or.inr (Or.inr h')
    · exact Or.inr (Or.inl ⟨h, h'⟩)

/-- **The marginal window is a genuine third case.** When `0 < β < 1`, neither
    `β = 0` nor `β = 1` holds — so neither branch A nor branch B is triggered and
    the regularity verdict is undetermined. This is exactly why the dichotomy
    must be a trichotomy. -/
-- Ref: [manuscript] fluid-dynamics/levi-degeneracy-conjecture (Finding 3)
theorem levi_marginal_undetermined (T : LeviGrowthTrichotomy)
    (h : 0 < T.beta ∧ T.beta < 1) : T.beta ≠ 0 ∧ T.beta ≠ 1 :=
  ⟨ne_of_gt h.1, ne_of_lt h.2⟩

/-- **Branches A and B are mutually exclusive.** No bounded-rate exponent can
    make the flow both NS-singular (β = 0) and NS-regular (β = 1); `0 = 1` is
    false. A sanity check that the two dichotomy branches never overlap. -/
-- Ref: [manuscript] fluid-dynamics/levi-degeneracy-conjecture
theorem levi_branches_exclusive (T : LeviGrowthTrichotomy)
    (hA : T.beta = 0) (hB : T.beta = 1) : False := by
  rw [hA] at hB; exact zero_ne_one hB

end QOU.FluidDynamics
