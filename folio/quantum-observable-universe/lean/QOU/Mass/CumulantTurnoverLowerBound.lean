/-
# The measured cumulant signs alone put the coordination-weight turnover at `A ≥ 4`

`QOU.Mass.CoordinationWeightDifferences` rewrites the body-order cumulants as forward
differences of one function: `bind w A = C(A,2) · w (A-1)`, and then `b₃ = 3·Δw 1`,
`b₄ = 6·Δ²w 1`. It proves the two *first-order* readings — `b₃ > 0 ↔ w 1 < w 2`
(`lt_of_b3_pos`) and `b₄ > 0 ↔ Δw 1 < Δw 2` (`lt_of_b4_pos`) — and stops there.

This file composes them, which is one step and gives something neither gives alone:

    b₃ > 0  ∧  b₄ > 0   ⟹   w 1 < w 2 < w 3 .

So the coordination weight is strictly increasing *through* `z = 3`, and its maximum
over `{1,2,3}` is at `3` — i.e. **the turnover is at `A ≥ 4`**. AME2020 supplies both
hypotheses (`b₃ = +1.426222`, `b₄ = +9.243387` MeV, isospin-averaged; both stay
positive under the Coulomb-corrected convention), so the antecedent is measured, not
assumed.

## Why the composition is worth stating separately

The corpus already locates the turnover at `A = 4`, by a completely different route:
Wigner `SU(4)`'s `[1ⁿ]` has `dim = C(4,n)`, which **vanishes** for `n ≥ 5`, so the
maximally-symmetric regime ends at `A = 4`
(`QOU.Mass.AntisymmetricCasimirIsTwoBody`, `QOU.Mass.SU4CasimirIsAffineInPairCount`).
That is a *support* bound and it is an **upper** bound on where the peak can sit.

The bound here is a **lower** bound, and it comes from measured cumulant signs with no
representation theory in it at all. The two arguments are independent — different
inputs, opposite directions — and they meet at `A = 4`. Neither alone pins the
location; together they do.

## Second result — the missing channel is not a small correction

Every mechanism the arc has closed is *saturating*: a uniform bond over a simple graph
(`QOU.Mass.UniformBondSimpleGraphExclusion`), a bounded-degree coordination term
(`QOU.Mass.CoordinationSaturation`), a two-body `SU(4)` invariant
(`QOU.Mass.SU4CasimirIsAffineInPairCount`). In the `w` coordinate every one of them is
**non-increasing**, which is exactly why each lands at `b₃ ≤ 0`.

Split `w = u + v` with `u` the saturating background and `v` the channel that is
*absent* at coordination one, `v 1 = 0`. Then

    b₃ ≤ 3 · v 2 ,

so `v 2 ≥ b₃/3` — the channel must be **at least the whole measured deficit**,
`≥ 0.4754 MeV/pair` (isospin average) or `≥ 0.6027` (Coulomb-corrected). It cannot be
a perturbative correction sitting on top of a background that nearly works.

## Scope — read before citing

Both results are **arithmetic consequences of the measured signs**, in the reparameterised
coordinate. They derive no magnitude and propose no functional; the magnitude gate
(`qou-edt7`, `qou-brng`) is untouched. What they do is constrain the shape any future
derivation must produce, at zero free parameters.

Nothing here contains `q`. That is the point of recording it under bean `qou-edt7`'s
off-gate question: the hypotheses are measured cumulant signs and the conclusions are
inequalities between values of `w`, so the statement holds for *every* substrate
modulus. It is not a derivation of the deuteron deficit, and it is not gated by the
2026-08-02 owner ruling either, because it never asks what `q₀` is.

Base ring is a generic strictly-ordered `CommRing` (AGENTS.md §7c): the content is
order arithmetic, with no archimedean input and no `ℝ`.

Bean `qou-edt7`.
-/
import QOU.Mass.CoordinationWeightDifferences

namespace QOU.Mass.CumulantTurnoverLowerBound

open QOU.Mass.CoordinationWeightDifferences

variable {R : Type*} [CommRing R] [LinearOrder R] [IsStrictOrderedRing R]

/-- **The rise continues to `z = 3`.** `b₃ > 0` makes the first forward difference
positive; `b₄ > 0` makes the second difference larger still, so the second forward
difference is positive too. -/
theorem w2_lt_w3_of_b3_b4_pos {w : ℕ → R} (h3 : 0 < b3 w) (h4 : 0 < b4 w) :
    w 2 < w 3 := by
  have h1 : w 1 < w 2 := lt_of_b3_pos h3
  have h2 : fwdDiff w 1 < fwdDiff w 2 := lt_of_b4_pos h4
  have hd1 : (0 : R) < fwdDiff w 1 := by
    simp only [fwdDiff]
    linarith
  have hd2 : (0 : R) < fwdDiff w 2 := lt_trans hd1 h2
  simp only [fwdDiff] at hd2
  linarith

/-- The coordination weight rises across both steps the measurement reaches. -/
theorem w1_lt_w2_lt_w3 {w : ℕ → R} (h3 : 0 < b3 w) (h4 : 0 < b4 w) :
    w 1 < w 2 ∧ w 2 < w 3 :=
  ⟨lt_of_b3_pos h3, w2_lt_w3_of_b3_b4_pos h3 h4⟩

/-- **The turnover is at `A ≥ 4`.** Both coordinations below `3` carry a strictly
smaller weight than `z = 3` does, so the maximum of `w` over `{1,2,3}` sits at `3`,
i.e. at mass number `A = 4`. -/
theorem max_at_three {w : ℕ → R} (h3 : 0 < b3 w) (h4 : 0 < b4 w) :
    w 1 < w 3 ∧ w 2 < w 3 := by
  have h12 : w 1 < w 2 := lt_of_b3_pos h3
  have h23 : w 2 < w 3 := w2_lt_w3_of_b3_b4_pos h3 h4
  exact ⟨lt_trans h12 h23, h23⟩

/-- The contrapositive, and the falsifiable form: a coordination weight whose value at
`z = 3` does not exceed its value at `z = 2` cannot carry both measured signs. -/
theorem not_both_pos_of_w3_le {w : ℕ → R} (h : w 3 ≤ w 2) :
    ¬ (0 < b3 w ∧ 0 < b4 w) :=
  fun hb => absurd (w2_lt_w3_of_b3_b4_pos hb.1 hb.2) (not_lt.mpr h)

section Channel

/-- **The absent channel must carry at least the whole deficit.** Write the coordination
weight as a saturating background `u` plus a channel `v` that vanishes at coordination
one. With `u` non-increasing across the one step it is evaluated at, the entire measured
rise is charged to `v 2`. -/
theorem b3_le_three_mul_channel {u v : ℕ → R} (hv : v 1 = 0) (hu : u 2 ≤ u 1) :
    b3 (fun z => u z + v z) ≤ 3 * v 2 := by
  rw [b3_eq]
  simp only [fwdDiff, hv]
  linarith

/-- Consequently a positive three-body cumulant forces a strictly positive channel at
coordination two — the deficit is an **absence** at `z = 1`, not a suppression of
something the background already supplies. -/
theorem channel_pos_of_b3_pos {u v : ℕ → R} (hv : v 1 = 0) (hu : u 2 ≤ u 1)
    (h3 : 0 < b3 (fun z => u z + v z)) : 0 < v 2 := by
  have hb := b3_le_three_mul_channel hv hu
  linarith

end Channel


/-- **First projection of `max_at_three` (`qou-qqm4`).**
Under `0 < b3 w` and `0 < b4 w`, `w 1 < w 3`. -/
theorem w1_lt_w3_of_b3_b4_pos {w : ℕ → R} (h3 : 0 < b3 w) (h4 : 0 < b4 w) :
    w 1 < w 3 :=
  (max_at_three h3 h4).1

end QOU.Mass.CumulantTurnoverLowerBound
