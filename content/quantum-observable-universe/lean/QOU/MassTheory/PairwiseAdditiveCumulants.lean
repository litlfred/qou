import Mathlib.Tactic

/-!
# A pairwise-additive binding functional has vanishing connected cumulants

Companion to `QOU.MassTheory.MayerThreeBodySign`. Together they say that
**neither** assembly the corpus carries can produce a positive connected 3-body
Ursell cumulant, and that they fail in *opposite* directions.

## The two assemblies

**Multiplicative (Mayer).** `W(K) = 1 − ∏_{i<j} f_ij`, normalised at the
deuteron — what `he4_body_order_shortfall_location_probe.py` and PROBE 2 use.
`MayerThreeBodySign.lt_of_b3_pos` gives `b₃ > 0 → f_pn > 2/3`, and every
measured `f_pn` is below `2/3`, so **`b₃ < 0`**.

**Pairwise-additive (the log form).** `B = −α·∑_{i<j} ln f_ij`. The 2026-08-08
audit §10a *derives* this one: `tr_M` is multiplicative over independent
subsystems and energy is extensive, so the map from trace to energy solves
`f(xy) = f(x) + f(y)` — Cauchy — whose continuous solutions are `c·ln x`. Its
conclusion is that "the log form is forced".

This file computes what that form gives.

## Result

For a pairwise-additive map — `B(A) = C(A,2)·g` for a common bond value `g` —
the Ursell inversion

    b₂ = B(2),  b₃ = B(3) − 3·b₂,  b₄ = B(4) − 6·b₂ − 4·b₃

returns `b₂ = g` and **`b₃ = 0`, `b₄ = 0`** — identically, for every `g`.
`pairwise_b3_eq_zero`, `pairwise_b4_eq_zero`.

This is not "small": it is exactly zero, because the cumulant expansion is
*defined* to strip the pairwise part. A pairwise-additive assembly has no
connected content above two bodies to give.

## The trilemma

| assembly | `b₃` |
|---|---|
| multiplicative `1 − ∏f` | `< 0` (`MayerThreeBodySign`) |
| pairwise-additive log form | `= 0` (here) |
| AME2020 | `= +1.426222` MeV |

`ame_b3_pos` records the third row from the same literals the 08-29 probe uses.
`no_pairwise_matches_ame` and `trilemma` state the consequence: neither assembly
reaches the measured sign.

## What this does not say

It does **not** refute the §10a derivation, and it does not propose a
replacement. It says that if the log form is forced, the corpus is committed to
a functional with no 3-body content, while the body-order programme
(`thm:binding-closure-conditional`) needs some. One of the two has an unstated
hypothesis. My reading — judgement, not a result — is that §10a's Cauchy step
assumes the trace factorises over *independent* subsystems, which is exactly
what a bound state is not; that is where I would look first. Recorded in bean
`qou-edt7`.

Choosing a functional *because* it lands `b₃ > 0` would be the anchor inversion
the Δ_λ gate forbids, in new clothes.

Base ring: generic `[Field R]` for the cumulant algebra — nothing archimedean is
needed for the vanishing (AGENTS.md §7c); the AME comparison is over `ℚ`.
-/

namespace QOU.MassTheory.PairwiseAdditiveCumulants

variable {R : Type*} [Field R]

/-- The binding of an `A`-body system under a pairwise-additive assembly with a
common bond value `g`: one `g` per pair, `C(A,2)` pairs. -/
def pairwiseBinding (g : R) (A : ℕ) : R := (Nat.choose A 2 : R) * g

/-- The Ursell 2-body cumulant. -/
def b2 (B : ℕ → R) : R := B 2

/-- The connected 3-body cumulant. -/
def b3 (B : ℕ → R) : R := B 3 - 3 * b2 B

/-- The connected 4-body cumulant. -/
def b4 (B : ℕ → R) : R := B 4 - 6 * b2 B - 4 * b3 B

@[simp] theorem pairwiseBinding_two (g : R) : pairwiseBinding g 2 = g := by
  unfold pairwiseBinding
  rw [show Nat.choose 2 2 = 1 from rfl]
  push_cast
  ring

@[simp] theorem pairwiseBinding_three (g : R) : pairwiseBinding g 3 = 3 * g := by
  unfold pairwiseBinding
  rw [show Nat.choose 3 2 = 3 from rfl]
  push_cast
  ring

@[simp] theorem pairwiseBinding_four (g : R) : pairwiseBinding g 4 = 6 * g := by
  unfold pairwiseBinding
  rw [show Nat.choose 4 2 = 6 from rfl]
  push_cast
  ring

/-- `b₂` recovers the bond value. -/
theorem pairwise_b2 (g : R) : b2 (pairwiseBinding g) = g := by
  simp [b2]

/-- **The connected 3-body cumulant of a pairwise-additive map is exactly zero**,
for every bond value. Not small — zero. -/
theorem pairwise_b3_eq_zero (g : R) : b3 (pairwiseBinding g) = 0 := by
  simp [b3, b2]

/-- Likewise at 4 bodies. -/
theorem pairwise_b4_eq_zero (g : R) : b4 (pairwiseBinding g) = 0 := by
  simp [b4, b3, b2]

/-- AME2020's connected 3-body cumulant, from the literals the 2026-08-29 probe
uses: `(B(³H) + B(³He))/2 − 3·B(²H)`, in MeV. -/
def ameB3 : ℚ := (8481798 + 7718043) / (2 * 1000000) - 3 * (2224566 / 1000000)

theorem ame_b3_pos : 0 < ameB3 := by
  unfold ameB3; norm_num

/-- **No pairwise-additive assembly reproduces the measured 3-body cumulant.**
Its `b₃` is zero; AME's is positive. -/
theorem no_pairwise_matches_ame (g : ℚ) : b3 (pairwiseBinding g) ≠ ameB3 := by
  rw [pairwise_b3_eq_zero]
  exact ne_of_lt ame_b3_pos

/-- **The trilemma.** A pairwise-additive assembly gives `b₃ = 0`; a
multiplicative assembly below the `2/3` threshold gives `b₃ < 0`
(`MayerThreeBodySign.b3_neg_of_le`); AME gives `b₃ > 0`. Stated here as the
disjunction that has to be broken: any assembly reproducing the measured sign is
neither of the two. -/
theorem trilemma (g : ℚ) (h : b3 (pairwiseBinding g) = ameB3) : False :=
  no_pairwise_matches_ame g h

end QOU.MassTheory.PairwiseAdditiveCumulants
