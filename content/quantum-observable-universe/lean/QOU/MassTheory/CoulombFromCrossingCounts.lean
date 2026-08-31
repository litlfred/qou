/-
# The Coulomb shape IS reachable from the crossing counts — just not linearly

Owner, 2026-08-30: *"explore A^{1/3} Coulomb geometry"*.

This file sharpens the scope of `QOU.MassTheory.CrossingCountAffine`, which is
mine, merged the same day, and which I then over-read in that PR's own summary.

## The over-read, stated plainly

`CrossingCountAffine.no_crossing_combination_is_protonPairs` excludes
`a·n₊ + b·n₋ + c = Z(Z-1)` for **constant** `a b c` — a statement about the
**linear** class and nothing wider. The PR that landed it concluded *"the target
is a `Z(Z-1)` multiplicity from somewhere the crossing counts do not reach"*.

That is a scope-(b) reading of a scope-(b) result about a **strictly smaller
class**. AGENTS.md §"Before declaring refuted" distinguishes *"this construction
alone does not reproduce the numbers"* from *"this ingredient cannot appear in
any closure"*, and the linear exclusion licenses only the first. The counts do
reach `Z(Z-1)`; they reach it **quadratically**, which the theorem never touched.

## What is proved here

The two channel identities are already measured and proved
(`CrossingCountAffine.counts_affine`, 12 nuclei to `A = 39`):

    n₊ + n₋ = 10A - 2        (the mirror-invariant "Coulomb" channel)
    n₊ - n₋ = 4Z             (the "strong" channel, carrying all charge)

The second is invertible. `Z = (n₊ - n₋)/4`, so

    16·Z(Z-1) = (n₊ - n₋)·(n₊ - n₋ - 4)

exactly — `protonPairs_from_counts`, division-free over a bare `CommRing`, no
hypotheses. So the proton-pair multiplicity a Coulomb energy needs is a
**quadratic** function of the very counts the linear theorem excludes, and
`counts_determine_protonPairs` records that the two counts determine it outright.

`quadratic_escapes_linear_exclusion` puts the two side by side in one statement:
the same `(A, Z)` at which every linear combination fails is one at which the
quadratic form succeeds. Nothing is contradicted; a boundary is located.

## And the length scale

A Coulomb energy is `∝ Z(Z-1)/R` with `R ∝ A^{1/3}`, so the framework needs a
dimensionless quantity scaling as `A^{-1/3}`. The natural candidate — the cube
root of a hyperbolic volume — is **blocked by measurement, not by taste**:
`computations/meson/atom-branch-hyperbolicity.witness.json` reports **0 of 4**
branch closures hyperbolic for the proton, **0 of 4** for the neutron and **0 of
32** for the deuteron. Every one degenerate, so there is no volume to take a
root of at the atom-braid level.

The count channel needs no hyperbolic structure — it is defined for every braid
word — and `n₊ + n₋ = 10A - 2` is extensive, so a cube root of it is
*available* where a volume is not. `coulombChannel_extensive` and
`cubed_scale_is_the_channel` state that, and nothing more.

**🛑 Availability is not derivation, and this file claims only the former.**
Taking a cube root writes the exponent `1/3` in by hand; since the channel is
affine in `A`, `(n₊+n₋)^{1/3}` is `A^{1/3}` with extra steps. Bean **`qou-nf9l`
(completed)** refuted all three corpus combinatorial classes for *producing* a
cube root of `A`, and its census records that every `1/3` in the corpus is a
**fixed index 3**, never an `A`-th root. Worse for the exponent specifically:
that audit's 8-pair mirror fit gives `p* = 0.252 ± 0.020`, putting `1/4` at
0.1σ and **`1/3` at 4.1σ** — independently reproduced on 5 pairs in the
companion probe. So `A^{1/3}` is not what the data wants and nothing here
rescues it.

The **cube root itself is deliberately not defined here**: it is an archimedean
construct (§7c) and this file stays over a generic `CommRing`, stating instead
what its cube must satisfy.

## Scope

Everything here is an **identity**, holding for all values, with no anchor, no
fit and no CODATA. It does **not** claim the Coulomb term of the semi-empirical
mass formula is derived — `a_C` is nowhere, the `1/R` is not derived from the
substrate, and the assignment of `n₊ ± n₋` to channels is `qou-toul`'s, taken as
input. It claims exactly one thing: **the ingredient is not excluded**, and the
corpus (including my own PR body) had recorded that it was.

Beans `qou-brng`, `qou-0c19`, `qou-nial`.
-/
import Mathlib.Algebra.Ring.Defs
import Mathlib.Tactic.Ring
import Mathlib.Tactic.LinearCombination

namespace QOU.MassTheory.CoulombFromCrossingCounts

variable {R : Type*} [CommRing R]

/-! ## 1. The two channels, as measured -/

/-- Positive crossings of the `A`-nucleon atom braid, `Z` protons. Measured in
`level3_em_channel_parity_probe` on 12 nuclei to `A = 39`. -/
def nPlus (A Z : R) : R := 5 * A - 1 + 2 * Z

/-- Negative crossings. -/
def nMinus (A Z : R) : R := 5 * A - 1 - 2 * Z

/-- The number of proton pairs, doubled to stay division-free: `Z(Z-1)`. -/
def protonPairs (Z : R) : R := Z * (Z - 1)

/-- The unsigned (mirror-invariant) channel is **extensive**: `10A - 2`,
depending on `A` alone. -/
@[simp] theorem coulombChannel_extensive (A Z : R) :
    nPlus A Z + nMinus A Z = 10 * A - 2 := by
  unfold nPlus nMinus; ring

/-- The signed channel is `4Z` — it carries all of the charge dependence. -/
@[simp] theorem strongChannel_eq (A Z : R) :
    nPlus A Z - nMinus A Z = 4 * Z := by
  unfold nPlus nMinus; ring

/-! ## 2. The counts DO reach the proton-pair multiplicity — quadratically -/

/-- **The point of this file.** `Z(Z-1)` is an exact quadratic function of the
crossing counts, with no hypotheses and no division:

    16·Z(Z-1) = (n₊ - n₋)·(n₊ - n₋ - 4)

`CrossingCountAffine.no_crossing_combination_is_protonPairs` excludes the
**linear** combinations only; this is what lies immediately outside that class. -/
theorem protonPairs_from_counts (A Z : R) :
    16 * protonPairs Z = (nPlus A Z - nMinus A Z) * (nPlus A Z - nMinus A Z - 4) := by
  unfold protonPairs nPlus nMinus; ring

/-- Stated as a determination: the two counts fix the proton-pair number. Any
`(A, Z)` and `(A', Z')` agreeing on both channels agree on `Z(Z-1)`. Over a ring
where `16 ≠ 0`; `ℤ` and `ℚ` qualify. -/
theorem counts_determine_protonPairs [NoZeroDivisors R] {A Z A' Z' : R}
    (hplus : nPlus A Z = nPlus A' Z') (hminus : nMinus A Z = nMinus A' Z')
    (h16 : (16 : R) ≠ 0) : protonPairs Z = protonPairs Z' := by
  have h : (16 : R) * protonPairs Z = 16 * protonPairs Z' := by
    rw [protonPairs_from_counts A Z, protonPairs_from_counts A' Z',
      hplus, hminus]
  exact mul_left_cancel₀ h16 h

/-! ## 3. The two statements side by side

The linear exclusion and the quadratic construction are both true, of the same
counts, at the same `(A, Z)`. -/

/-- **Located, not contradicted.** For every choice of linear coefficients there
is a `Z` at which the linear form misses `Z(Z-1)` — that is
`CrossingCountAffine`'s content — while the quadratic form matches at *every*
`Z`, with the coefficient fixed in advance. Over `ℤ`. -/
theorem quadratic_escapes_linear_exclusion (A : ℤ) :
    (∀ a b c : ℤ, ¬ (∀ Z : ℤ, a * nPlus A Z + b * nMinus A Z + c = protonPairs Z))
      ∧ (∀ Z : ℤ, 16 * protonPairs Z
            = (nPlus A Z - nMinus A Z) * (nPlus A Z - nMinus A Z - 4)) := by
  constructor
  · intro a b c hEq
    -- the second difference in Z kills every affine form but returns 2 on Z(Z-1)
    have e0 := hEq 0
    have e1 := hEq 1
    have e2 := hEq 2
    unfold nPlus nMinus protonPairs at e0 e1 e2
    -- e2 - 2*e1 + e0 : LHS second difference is 0, RHS is 2
    have : (0 : ℤ) = 2 := by linear_combination e2 - 2 * e1 + e0
    norm_num at this
  · intro Z; exact protonPairs_from_counts A Z

/-! ## 4. The length scale — what its cube must satisfy

A Coulomb energy is `∝ Z(Z-1)/R` with `R ∝ A^{1/3}`. The cube root is
archimedean (§7c) and is deliberately NOT taken here; what is stated is the
algebraic condition its cube satisfies, which is where the substrate content
lives. -/

/-- A scale `s` **is** the Coulomb-channel length scale exactly when its cube is
that channel. Purely definitional — recorded so the downstream archimedean
specialisation has a generic statement to instantiate, rather than introducing
`Real.rpow` on this side of the wall. -/
def IsChannelScale (A Z s : R) : Prop := s ^ 3 = nPlus A Z + nMinus A Z

/-- Such a scale's cube is affine in `A` with slope `10` — extensive, hence its
root grows as `A^{1/3}`. No hyperbolic volume is required anywhere: the count
channel is defined for every braid word, degenerate or not, which is what makes
it available where `atom-branch-hyperbolicity` measured **0 of 40** branch
closures hyperbolic across p, n and the deuteron. -/
theorem cubed_scale_is_the_channel {A Z s : R} (h : IsChannelScale A Z s) :
    s ^ 3 = 10 * A - 2 := by
  rw [h, coulombChannel_extensive]

/-- And the scale is mirror-invariant: it does not see the charge, which is
correct for a nuclear radius and is the one place the channel assignment's
"reversed parity" is the *right* way round. -/
theorem channelScale_mirror_invariant {A Z W s t : R}
    (hz : IsChannelScale A Z s) (hw : IsChannelScale A W t) :
    s ^ 3 = t ^ 3 := by
  rw [cubed_scale_is_the_channel hz, cubed_scale_is_the_channel hw]

end QOU.MassTheory.CoulombFromCrossingCounts
