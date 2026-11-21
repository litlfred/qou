/-
# A one-dimensional block's character is a product over letters — so its
# log-weight is a bond functional

## Why this file exists

Bean `qou-brng`'s live remainder after `QOU/Mass/MultiplicityNotExtensive.lean`
(#7181) was the **dominant summand's own log-weight**
`L(A) = log|y_{λ*} χ^{λ*}(β_A)|` of the partition sum
`tr_M(β_A) = Σ_λ y_λ χ^λ(β_A)`: the multiplicity channel being `O(√A)`, an
extensive term could only live in the largest term itself, and the `tr_M` bond
rule (`QOU/Mass/MarkovBondRuleForcesPairwise.lean`) says nothing about a single
block's character.

Measured on the live atom word (`computations/brng_dominant_summand_ursell_probe.py`,
2026-09-12, proton pin, convention D): for **every** typed cluster with `A ≤ 4`
the dominant summand is the **one-row block `λ* = (3A)`**, with the runner-up at
most 75.4 % of it. That block is one-dimensional, so its character is a ring
homomorphism `H_n(q) → R` sending every generator `σ_g` to `q`. This file records
the consequence that makes the measurement a structural fact rather than a
coincidence of numbers:

> the character of any word of letters `c·σ_g + d·1` under a one-dimensional
> block is the **product over the letters** of `c·q + d`.

Hence the word-dependent part of the dominant summand's log-weight is a **sum
over letters** — and the atom word's interface letters are one per bond of a
chain, so the sum is exactly chain-edge additive, with no connected many-body
term of any order. (Measured: chain-edge residual `7.4e-51` in the atom's own
block; the complete-graph Ursell cumulants are the chain's missing-edge
accounting, `b₃ = −b₂` to the working precision.) What is left of `L(A)` after
the letters is `log y_{(3A)}`, which contains no word at all.

## What is and is not proved here

* Proved (generic, §7c): the product formula for an algebra homomorphism to the
  base ring evaluated on a list of affine letters, and its factorisation over a
  concatenation. Nothing about which block dominates.
* NOT proved: that the dominant block *is* one-row. That is a measurement, made
  per word and per `A`, and it **fails at ⁶Li** (dominant `(15,3)`), where a
  two-row character is not letter-multiplicative and this file says nothing.
  So the exclusion this file supports is scope-(b) at `A ≤ 4` and stops there.

## Base ring

Generic `[CommRing R]`, an `R`-algebra `H` (the Hecke algebra is one), and an
`R`-algebra homomorphism `χ : H →ₐ[R] R` (the one-row character). The Markov
parameter `q : R` is the common image of the generators. No `ℝ`, no ordering,
no logarithm: the additive statement is the multiplicative one read through
`log`, which lives on the archimedean side and is not needed for the algebra.

-- Ref: [leitner2026] §"Frobenius pairing", per-block characters of `H_n(q)`
-/

import Mathlib.Algebra.Algebra.Hom
import Mathlib.Algebra.BigOperators.Group.List.Basic

namespace QOU.Mass.OneRowBlockLetterProduct

variable {R H : Type*} [CommRing R] [Ring H] [Algebra R H]

/-- An affine letter `c·σ_g + d·1` of the atom word: `mass_at_3A_proper.
atom_braid_word_3A` returns triples `(c, d, g)` denoting the Hecke element
`c*sigma_g + d*1`. -/
def letter (σ : ℕ → H) (l : R × R × ℕ) : H :=
  algebraMap R H l.1 * σ l.2.2 + algebraMap R H l.2.1

/-- The scalar a one-dimensional block assigns to a letter when every generator
is sent to `q`: `c·q + d`. -/
def letterValue (q : R) (l : R × R × ℕ) : R :=
  l.1 * q + l.2.1

/-- A one-dimensional block sends a letter to its scalar. -/
theorem map_letter (χ : H →ₐ[R] R) (σ : ℕ → H) (q : R) (hσ : ∀ g, χ (σ g) = q)
    (l : R × R × ℕ) : χ (letter σ l) = letterValue q l := by
  simp [letter, letterValue, map_add, map_mul, hσ]

/-- **The product formula.** Under a one-dimensional block, the character of a
word is the product over its letters of `c·q + d`. This is the whole reason the
dominant summand's log-weight cannot carry a connected many-body term at
`A ≤ 4`: the word enters only through a product of per-letter scalars. -/
theorem map_word_eq_prod (χ : H →ₐ[R] R) (σ : ℕ → H) (q : R)
    (hσ : ∀ g, χ (σ g) = q) (w : List (R × R × ℕ)) :
    χ (w.map (letter σ)).prod = (w.map (letterValue q)).prod := by
  induction w with
  | nil => simp
  | cons l w ih =>
    simp only [List.map_cons, List.prod_cons, map_mul, map_letter χ σ q hσ, ih]

/-- **Factorisation over a concatenation.** The atom word is the free word with
interface letters inserted; under a one-dimensional block the character
factorises over any split of the letter list, so the interface letters
contribute a separate factor — one per bond, which is exactly "bond additive"
once a logarithm is taken on the archimedean side. -/
theorem map_word_append (χ : H →ₐ[R] R) (σ : ℕ → H) (q : R)
    (hσ : ∀ g, χ (σ g) = q) (a b : List (R × R × ℕ)) :
    χ ((a ++ b).map (letter σ)).prod
      = (a.map (letterValue q)).prod * (b.map (letterValue q)).prod := by
  rw [map_word_eq_prod χ σ q hσ, List.map_append, List.prod_append]

end QOU.Mass.OneRowBlockLetterProduct
