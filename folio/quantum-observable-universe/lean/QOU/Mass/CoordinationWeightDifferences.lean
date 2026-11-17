/-
# The body-order cumulants are the finite differences of one function

`qou-edt7` asks what assembly can produce the measured `b₃ > 0`, given that both
corpus assemblies provably cannot:

* `QOU.MassTheory.MayerThreeBodySign.lt_of_b3_pos` — the multiplicative Mayer
  form `W = 1 - Π f` forces `b₃ < 0` at every measured bond factor;
* `QOU.Mass.PairwiseCumulantVanishing.b3_eq_zero_of_isPairwise` — the
  pairwise-additive form forces `b₃ = 0`, exactly, whatever the bond functional.

This file does **not** propose a third functional. Choosing a functional because
it lands `b₃ > 0` is the anchor inversion the bean forbids. It changes variables,
and under the change of variables the two walls turn out to be **one wall**, seen
from two sides.

## The change of variables

Write a binding map on the mass number as

    bind w A = C(A,2) * w (A-1)

`w z` is the mean binding **per nucleon pair** at coordination `z = A-1`. This is
a definition and not a model: given any `bind`, the function `w z := bind (z+1) /
C(z+1,2)` recovers it. Nothing is assumed by writing it.

## The identity

`b₃ = 3 · Δw 1` and `b₄ = 6 · Δ²w 1`, where `Δ` is the forward difference. In
general `bₙ = C(n,2) · Δ^{n-2} w 1`, term by term via the subset-of-a-subset rule
`C(n,k)·C(k,2) = C(n,2)·C(n-2,k-2)`.

**Scope on the general-`n` claim.** Only `n = 3` and `n = 4` are proved here.
The general statement is verified symbolically for `n = 2..8` against an
arbitrary `w` in
`computations/probes/body_order_is_finite_difference_of_coordination_weight_probe.py`;
that is a check, not a proof, and it is not claimed as one.

## What it buys

An infinite tower of unknown many-body coefficients becomes one unknown function
of one integer variable, and the three separate facts become three readings of
its shape:

* `w` **constant** ⟹ `b₃ = 0` and `b₄ = 0` — the pairwise wall, recovered here
  as the `Δw = 0` case of a strictly more general statement;
* `w` **non-increasing** ⟹ `b₃ ≤ 0` — so the Mayer sign is not a separate
  obstruction, it is what any saturating `w` gives;
* `b₄ > 0` ⟺ `w` **convex** at `z = 1`.

So `b₃ > 0` is not exotic and needs no new functional. It says exactly one
thing: **the mean binding per pair is larger at coordination 2 than at
coordination 1.** The falsifiable form is `not_antitone_of_b3_pos` below.

## What it does NOT buy — read this before citing the file

The identity is a **reparameterisation** and is therefore tautologically
available. It derives no magnitude and cannot: `w` is defined by inverting
`bind`, so fitting `w` to AME2020 is fitting the binding to AME2020 with extra
steps. Nothing here closes the magnitude gate, and nothing here should be cited
as evidence that it is closer to closing.

Base ring is a generic `CommRing` for the identities (AGENTS.md §7c) — they are
inclusion-exclusion bookkeeping, with no ordering and no archimedean input. The
sign results, and only those, ask for a `LinearOrderedCommRing`.

Bean `qou-edt7`. Companion probe:
`computations/probes/body_order_is_finite_difference_of_coordination_weight_probe.py`
-/
import Mathlib.Algebra.Order.Ring.Defs
import Mathlib.Data.Nat.Choose.Basic
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith

namespace QOU.Mass.CoordinationWeightDifferences

section Identities

variable {R : Type*} [CommRing R]

/-- The **coordination weight** assembly: a nucleus of mass number `A` carries
`C(A,2)` pairs, each contributing the mean weight `w (A-1)` of a nucleon at
coordination `z = A-1`. Every binding map is of this form for exactly one `w`;
this is a change of variables, not a hypothesis. -/
def bind (w : ℕ → R) (A : ℕ) : R := (A.choose 2 : R) * w (A - 1)

/-- The **forward difference** `Δw z = w (z+1) - w z`. -/
def fwdDiff (w : ℕ → R) (z : ℕ) : R := w (z + 1) - w z

/-- The **connected three-body cumulant**, by Möbius inversion over the subset
lattice with `bind _ 0 = bind _ 1 = 0`. -/
def b3 (w : ℕ → R) : R := bind w 3 - 3 * bind w 2

/-- The **connected four-body cumulant**. -/
def b4 (w : ℕ → R) : R := bind w 4 - 4 * bind w 3 + 6 * bind w 2

/-- A one-body and a bare nucleon carry no pairs, so the inversion may run from
`k = 0` without changing anything. -/
theorem bind_one (w : ℕ → R) : bind w 1 = 0 := by
  simp [bind]

theorem bind_zero (w : ℕ → R) : bind w 0 = 0 := by
  simp [bind]

/-- **`b₃` is three times the first difference of the coordination weight.**
The `3` is `C(3,2)`, the number of pairs in a triple. -/
theorem b3_eq (w : ℕ → R) : b3 w = 3 * fwdDiff w 1 := by
  simp [b3, bind, fwdDiff]
  ring

/-- **`b₄` is six times the second difference.** The `6` is `C(4,2)`. -/
theorem b4_eq (w : ℕ → R) : b4 w = 6 * (w 3 - 2 * w 2 + w 1) := by
  unfold b4 bind
  norm_num [show Nat.choose 4 2 = 6 from rfl]
  ring

/-- The second difference, written as a difference of differences, so that the
`bₙ = C(n,2)·Δ^{n-2}w 1` shape is visible at `n = 4` too. -/
theorem b4_eq_diff_of_diff (w : ℕ → R) :
    b4 w = 6 * (fwdDiff w 2 - fwdDiff w 1) := by
  rw [b4_eq]; simp [fwdDiff]; ring

/-- **The pairwise wall, recovered.** A constant coordination weight — which is
what a pairwise-additive assembly with a transferable bond is — has vanishing
connected three-body cumulant. This is
`QOU.Mass.PairwiseCumulantVanishing.b3_eq_zero_of_isPairwise` as the `Δw = 0`
case; the point is that it is no longer a separate fact. -/
theorem b3_eq_zero_of_const (w : ℕ → R) (c : R) (hw : ∀ z, w z = c) :
    b3 w = 0 := by
  simp [b3_eq, fwdDiff, hw]

/-- And the four-body cumulant likewise. -/
theorem b4_eq_zero_of_const (w : ℕ → R) (c : R) (hw : ∀ z, w z = c) :
    b4 w = 0 := by
  rw [b4_eq, hw 1, hw 2, hw 3]
  ring

/-- **Inverse Ursell reconstruction of `bind w 3` and `bind w 4` from `w 1`, `b₃`, and `b₄` (`qou-edt7`).**
In any commutative ring `R`, `bind w 3 = 3 * w 1 + b3 w` and `bind w 4 = 6 * w 1 + 4 * b3 w + b4 w`. -/
theorem bind_three_and_four_ursell_reconstruct (w : ℕ → R) :
    bind w 3 = 3 * w 1 + b3 w ∧
      bind w 4 = 6 * w 1 + 4 * b3 w + b4 w := by
  refine ⟨?_, ?_⟩
  · unfold b3 bind
    norm_num [show Nat.choose 2 2 = 1 from rfl]
    ring
  · unfold b4 b3 bind
    norm_num [show Nat.choose 2 2 = 1 from rfl]
    ring

end Identities

section Signs

variable {R : Type*} [CommRing R] [LinearOrder R] [IsStrictOrderedRing R]

/-- **A non-increasing coordination weight forces `b₃ ≤ 0`.**

This is the wall, and it subsumes the Mayer result rather than sitting beside
it: any assembly whose mean binding per pair does not *rise* with coordination
gives a non-positive connected three-body cumulant. A saturating assembly is
non-increasing, so it lands here — the multiplicative form's `b₃ < 0` is an
instance, not a coincidence. -/
theorem b3_nonpos_of_le {w : ℕ → R} (h : w 2 ≤ w 1) : b3 w ≤ 0 := by
  rw [b3_eq, fwdDiff]
  have : w (1 + 1) - w 1 ≤ 0 := by
    have h' : w (1 + 1) = w 2 := by norm_num
    rw [h']; linarith
  nlinarith [this]

/-- **The falsifiable form**, and the one measurement instantiates.

AME2020 gives `b₃ = +1.426222 MeV > 0` (Ursell inversion of the deuteron and the
isospin-averaged `A = 3` binding). So the physical coordination weight **rises**
from coordination 1 to coordination 2: `w 1 < w 2`. That single inequality is
the entire content of "nature's `b₃` is positive", and it is what a derivation
of the magnitude has to produce. -/
theorem lt_of_b3_pos {w : ℕ → R} (h : 0 < b3 w) : w 1 < w 2 := by
  by_contra hc
  exact absurd (b3_nonpos_of_le (not_lt.mp hc)) (not_le.mpr h)

/-- Restated as the refutation of a hypothesis class: `b₃ > 0` rules out every
assembly whose coordination weight is non-increasing at the bottom of the
ladder. -/
theorem not_le_of_b3_pos {w : ℕ → R} (h : 0 < b3 w) : ¬ (w 2 ≤ w 1) :=
  fun hle => absurd (b3_nonpos_of_le hle) (not_le.mpr h)

/-- **`b₄ > 0` is convexity at `z = 1`**, i.e. the *rise* itself accelerates:
the step from coordination 2 to 3 is larger than the step from 1 to 2. Measured,
both hold — `Δw 1 = 0.475` and `Δw 2 = 2.016 MeV` per pair. -/
theorem lt_of_b4_pos {w : ℕ → R} (h : 0 < b4 w) : fwdDiff w 1 < fwdDiff w 2 := by
  rw [b4_eq_diff_of_diff] at h
  nlinarith [h]

end Signs

end QOU.Mass.CoordinationWeightDifferences
