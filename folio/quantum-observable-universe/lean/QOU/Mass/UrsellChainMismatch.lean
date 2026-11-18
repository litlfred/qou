/-
# 🛑 RETRACTION OF NOVELTY (2026-09-03) — §3 of this file DUPLICATES an existing result

**The mathematics below is correct. The claim that §3 was new is not, and it was
mine.** Read this before citing anything in this file.

`QOU.Mass.UniformBondSimpleGraphExclusion` (landed on `main` `c9d47234ce`,
2026-08-30 — **four days before** this file merged, bean `qou-edt7`) already
proves the §3 exclusion, and proves it **more generally**:

| here (§3) | there | relation |
|---|---|---|
| `bondAdditive_nonpositive` — `n(3) − 3 ≤ 0` at `n(2) = 1` | `b3Uniform_nonpos` — `ε(e₃ − 3e₂) ≤ 0` for `e₃ ≤ 3`, `e₂ ≥ 1`, `ε ≥ 0` | **theirs is strictly more general**; mine is the `e₂ = 1` case, and mine additionally needs `b₂ ≠ 0` because it divides |
| `bRatioOfBondCounts_chain` (`−1`) | `b3Uniform_neg_of_chain` | same |
| `bRatioOfBondCounts_allPairs` (`0`) | `b3Uniform_eq_zero_of_complete` | same |
| `no_uniform_bond_model_reproduces_b3` | `not_uniform_simple_of_b3_pos` | same |

The invariant is identical — *a simple graph on three vertices has at most
`C(3,2) = 3` edges while the Ursell inversion subtracts three*.

**And the "surviving escape" was not a new direction either.** The required
amplification I computed, `w/w_d = 5399947/4449132 = 1.2137079772`, **is** the
corpus's `w(2)/w(1)`, recorded at 60 digits in
`coordination-weight-rise-and-turnover.witness.json` as
`1.21370760735284029758…` — the two agree to `3.05e-7`, the difference being that
I fed a rounded AME ratio and that probe did not. Its own source line calls that
number *"the entire content of `b₃ > 0`"*. Worse for my framing: the obvious
mechanism on that axis, single-ratio (Markov-power) scaling `ε(z) = ε(1)·r^{z−1}`,
is already **REFUTED** there — the two available ratios disagree by ~44 %, for
every `r`, convention-independently.

**How it happened.** I ran the six-path corpus-grep *after* merging instead of
before. Path 3 (`computations/`) surfaces
`coordination_weight_rise_and_turnover_probe.py` on the first pattern tried, and
its docstring names `UniformBondSimpleGraphExclusion` in the third paragraph. The
checklist is not expensive; I simply did not run it at the point it was for.

## What survives as this file's own contribution

Only §1–§2, and only as a **reconciliation of my own earlier capstone** rather
than as new mathematics: `all_channels_b3_sign_probe` reported four channels
failing and read them as four findings, and the pair/bond count mismatch shows
that ch3/ch4/ch5 are **one identity** while ch1 (`−1.3995`, the shipped,
non-additive channel) is not explained by it. That link between the exclusion and
the four *measured* channel values is not in `qou-edt7`.

§3 is now best read as an **independent re-derivation** of `b3Uniform_nonpos` by
a different route (Ursell counts rather than graph edges), arriving at the same
invariant and the same numbers. That has some corroboration value. It has **no
priority**, and this file must not be cited as establishing the exclusion — cite
`UniformBondSimpleGraphExclusion` for that.

Beans `qou-brng` (this arc), `qou-edt7` (the prior result).
-/

/-
# The additive channels' `b₃ = -b₂` is the Ursell inversion, not a three-body term

This file reframes a result of my own. `all_channels_b3_sign_probe` measured that
all four evaluable binding channels give `b₃/b₂ < 0`, and read the three
bond-additive ones clustering at `≈ -1` as a shared physical failure. **For those
three it is not physics. It is arithmetic**, and this file is the arithmetic.

## The mismatch

The Ursell inversion presumes an **all-pairs** decomposition. Its three-body
cumulant

    b₃ = B̄(3) - 3 b₂

subtracts `C(3,2) = 3` pair terms, because that is how many pairs three objects
have.

The bond set is a **chain**, with `A - 1` bonds — and `QOU.Mass.StrandLayoutForcesChain`
proves that is *forced* by the strand layout rather than chosen. The two counts

| `A` | pairs `C(A,2)` | chain bonds `A-1` |
|---|---|---|
| 2 | 1 | 1 |
| 3 | **3** | **2** |
| 4 | 6 | 3 |

**agree at `A = 2` and diverge from `A = 3`** — which is exactly where `b₃` lives.

## The consequence, exactly

If binding is bond-additive on the chain with a uniform bond `b`, then
`B(A) = (A-1)·b`, so

    b₂ = B(2) = b ,   b₃ = B(3) - 3b₂ = 2b - 3b = -b ,   b₃/b₂ = -1

**identically, for every `b`** (`chainAdditive_bRatio_eq_neg_one`). The `-1` is
the inversion charging three pairs against a model carrying two bonds — a deficit
of exactly one pair, hence `-b₂` (`pair_deficit_at_three`).

So the measured `ch3 = -0.9679`, `ch4 = -0.9681`, `ch5 = -1.0205` are not three
independent findings about the physics. They are one arithmetic identity, and
they sit slightly off `-1` only because their bonds are not all of the same type.

## What this does and does not change

**Does not change:** `ch1 = -1.3995`, the **shipped** channel, is *not* explained
by this — it is not bond-additive, its trace prefactor is exponential in `A`, and
it fails for its own reasons. The measured `b₃/b₂ = +0.6411239316` is untouched;
it is AME data and no inversion convention alters it.

**Does change:** how the earlier capstone should be read. "Four channels fail"
overstates the independence — three of the four fail *together*, for a reason
that is a property of the inversion applied to a chain, not of any channel.

**And it relocates the question.** A chain-additive model cannot produce a
positive `b₃` no matter what its bond weight is, so asking a chain model for one
is asking the wrong object.

## The generalisation — it is not about the chain either (§3)

Changing the bond set does not help. For any binding additive over a bond set
with a **uniform** bond value the value cancels and only the counts survive:
`b₃/b₂ = n(3)/n(2) - 3`. Two bound nucleons have exactly one bond, and a simple
bond set on three has at most `C(3,2) = 3`, so

    b₃/b₂ = n(3) - 3 ≤ 0   for EVERY uniform pairwise-bond model,

with the chain at `-1` and all-pairs at exactly `0`. The measured value is
`+0.641`, so no such model reaches it — the chain is not the culprit, the
uniformity is (`no_uniform_bond_model_reproduces_b3`).

**The surviving escape is non-uniformity.** If the `A = 3` bonds are *stronger*
than the deuteron bond, `b₃/b₂ = 3w/w_d - 3 > 0` whenever `w > w_d`. Nothing
here touches that, and it is the direction to take next.

## Scope

Scope **(b)** on **uniform** pairwise-bond-additive binding models, with the
invariant named: the bond count on three nodes is capped at `C(3,2) = 3` while
the Ursell inversion subtracts three pair terms. Scope **(a)** on everything
else — this excludes no channel, refutes no physics, and says nothing about
`ch1`, about non-uniform bond weights, or about non-pairwise carriers.

Ground ring: generic `[Field R]` — pure arithmetic, no ordering and no
archimedean structure (§7c). `CharZero` for the numerals.

Beans `qou-brng`.
-/
import Mathlib.Algebra.Field.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.LinearCombination
import Mathlib.Data.Nat.Choose.Basic
import Mathlib.Algebra.Order.Field.Rat
import QOU.Mass.CarrierCrossingQuantisation

namespace QOU.Mass.UrsellChainMismatch

open QOU.Mass.CarrierCrossingQuantisation

variable {R : Type*} [Field R] [CharZero R]

/-! ## 1. The two counts, and where they diverge -/

/-- Pairs among `A` objects — what the Ursell inversion charges for. -/
def pairCount (A : ℕ) : ℕ := A.choose 2

/-- Bonds in a chain on `A` nucleons — what the forced layout supplies
(`QOU.Mass.StrandLayoutForcesChain`). -/
def chainBondCount (A : ℕ) : ℕ := A - 1

/-- **They agree at `A = 2`.** -/
theorem counts_agree_at_two : pairCount 2 = chainBondCount 2 := by decide

/-- **And diverge at `A = 3`, by exactly one pair.** That single missing pair is
the whole of the `-b₂` below. -/
theorem pair_deficit_at_three : pairCount 3 - chainBondCount 3 = 1 := by decide

/-- The divergence is not a small-`A` accident: it widens. -/
theorem counts_diverge_at_four : pairCount 4 - chainBondCount 4 = 3 := by decide

/-! ## 2. The identity -/

/-- Binding of a chain of `A` nucleons that is additive over bonds with a uniform
bond value `b`: one term per bond, and a chain has `A - 1` of them. -/
def chainBinding (b : R) (A : ℕ) : R := ((A : R) - 1) * b

omit [CharZero R] in
/-- The deuteron: one bond. -/
theorem chainBinding_two (b : R) : chainBinding b 2 = b := by
  unfold chainBinding; norm_num

omit [CharZero R] in
/-- `A = 3`: two bonds. -/
theorem chainBinding_three (b : R) : chainBinding b 3 = 2 * b := by
  unfold chainBinding; norm_num

omit [CharZero R] in
/-- **The Ursell three-body cumulant of a chain-additive model is `-b₂`,
identically.** `B(3) - 3B(2) = 2b - 3b = -b`. No choice of bond value, weighting
or scale changes it — the `-1` is the inversion's three pair terms meeting the
chain's two bonds. -/
theorem chainAdditive_b3_eq_neg_b2 (b : R) :
    chainBinding b 3 - 3 * chainBinding b 2 = -chainBinding b 2 := by
  rw [chainBinding_two, chainBinding_three]; ring

omit [CharZero R] in
/-- **Hence `b₃/b₂ = -1` for every chain-additive model.** This is what the three
bond-additive channels were measuring; it is an identity, not three findings. -/
theorem chainAdditive_bRatio_eq_neg_one {b : R} (hb : b ≠ 0) :
    (chainBinding b 3 - 3 * chainBinding b 2) / chainBinding b 2 = -1 := by
  rw [chainAdditive_b3_eq_neg_b2, chainBinding_two]
  field_simp

/-- **So a chain-additive model can never produce a positive `b₃`.** Asking it for
one is asking the wrong object — which is the reframing, and the reason this is a
question about the comparison rather than about the physics. -/
theorem chainAdditive_b3_never_positive {b : R} (hb : b ≠ 0) :
    ¬ (chainBinding b 3 - 3 * chainBinding b 2) / chainBinding b 2 = 
      950815 / 1483044 := by
  rw [chainAdditive_bRatio_eq_neg_one hb]
  intro h
  rw [eq_div_iff (by norm_num : (1483044 : R) ≠ 0)] at h
  have h2 : (2433859 : R) = 0 := by linear_combination -h
  norm_num at h2

/-! ## 3. The generalisation: NO uniform pairwise-bond model can be positive

The chain is one bond set. The `-1` above is what *that* bond set gives, but the
argument does not need it: for a binding that is additive over a bond set with a
**uniform** bond value `b` (uniform meaning the bond value does not depend on
`A`), only the bond *counts* survive into the cumulant ratio —

    b₂ = n(2)·b ,  b₃ = n(3)·b - 3·n(2)·b ,  b₃/b₂ = n(3)/n(2) - 3 .

Two nucleons that are bound have exactly one bond, so `n(2) = 1`; and a simple
bond set on three nucleons has at most `C(3,2) = 3` of them. Hence
`b₃/b₂ = n(3) - 3 ≤ 0` for **every** such model — the chain (`n(3) = 2`) gives
`-1`, all-pairs (`n(3) = 3`) gives exactly `0`, and nothing reaches the measured
`+0.641`.

**Scope (b)**, invariant named: the bond count on three nodes is capped at three
while the Ursell inversion subtracts three pair terms. **The escape is
non-uniformity** — a model whose `A = 3` bonds are *stronger* than the deuteron
bond is not covered, since then `b₃/b₂ = 3w/w_d - 3 > 0` whenever `w > w_d`.
That is the surviving direction, and it is the one to take next. -/

/-- `b₃/b₂` for a bond-additive model with uniform bond value, as a function of
the bond counts alone — the bond value cancels. -/
def bRatioOfBondCounts (n2 n3 : ℕ) : ℚ := (n3 : ℚ) / (n2 : ℚ) - 3

/-- The chain is the `n(3) = 2` row. -/
theorem bRatioOfBondCounts_chain : bRatioOfBondCounts 1 2 = -1 := by
  unfold bRatioOfBondCounts; norm_num

/-- All-pairs is the `n(3) = 3` row — exactly zero, and still not positive. -/
theorem bRatioOfBondCounts_allPairs : bRatioOfBondCounts 1 3 = 0 := by
  unfold bRatioOfBondCounts; norm_num

/-- **Every uniform pairwise-bond model gives a non-positive `b₃`.** The bond
count on three nucleons cannot exceed `C(3,2) = 3`, and the inversion subtracts
three. -/
theorem bondAdditive_nonpositive (n3 : ℕ) (h : n3 ≤ 3) :
    bRatioOfBondCounts 1 n3 ≤ 0 := by
  unfold bRatioOfBondCounts
  have : ((n3 : ℚ)) ≤ 3 := by exact_mod_cast h
  simp only [Nat.cast_one, div_one]
  linarith

/-- **So no uniform pairwise-bond model reproduces the AME `b₃/b₂`.** The
measured value is strictly positive; every such model is `≤ 0`. -/
theorem no_uniform_bond_model_reproduces_b3 (n3 : ℕ) (h : n3 ≤ 3) :
    bRatioOfBondCounts 1 n3 ≠ rMeasured := by
  have hle : bRatioOfBondCounts 1 n3 ≤ 0 := bondAdditive_nonpositive n3 h
  have hpos : (0 : ℚ) < rMeasured := by unfold rMeasured; norm_num
  intro heq
  rw [heq] at hle
  linarith

/-- Adding the two-edge value to the three-edge additive discrepancy cancels to zero (`qou-dgkf`). -/
omit [CharZero R] in
theorem chainAdditive_b3_add_b2_eq_zero (b : R) :
    (chainBinding b 3 - 3 * chainBinding b 2) + chainBinding b 2 = 0 := by
  rw [chainAdditive_b3_eq_neg_b2 b, neg_add_cancel]

end QOU.Mass.UrsellChainMismatch
