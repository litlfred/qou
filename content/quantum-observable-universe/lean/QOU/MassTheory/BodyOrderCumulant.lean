/-
  Body-order cumulant orthogonality (GAP-A-4 class-D value leg).

  Companion to
    computations/probes/b4_value_cumulant_target_probe.py
    docs/scope/2026-07-05-gap-a4-ursell-operator-magnitude-scoping.md

  Context.  The ⁴He binding decomposes into connected k-body Ursell cumulants
  `b_k`. In the all-pairs (binomial) cluster model with no 0/1-body binding,
  the connected 4-body cumulant is the 4th forward finite difference at 0,

      b₄  =  B(4) − 4·B(3) + 6·B(2) − 4·B(1) + B(0).

  The value-leg probe found (numerically) that the framework's existing binding
  forms carry NO connected 4-body content — `B_sym` is 2-body additive, `B_vol`
  is 1-body linear — so the missing ⁴He `b₄ ≈ 9.24 MeV` requires a genuinely new
  4-body object. This file proves that orthogonality, and its non-vacuous
  converse: the 4th difference is a real cumulant extractor.

  Base ring (§7c): generic `[CommRing R]` — pure ring identities, no ordering,
  no archimedean construct, no q₀.
-/
import Mathlib.Algebra.Ring.Defs
import Mathlib.Data.Nat.Choose.Basic
import Mathlib.Tactic.Ring
import Mathlib.Tactic.NormNum

namespace QOU.MassTheory

variable {R : Type*} [CommRing R]

/-- The connected 4-body cumulant of a binding sequence `B : ℕ → R`, as the 4th
forward finite difference at 0 (Newton binomial transform, 0/1-body dropped):
`b₄ = B(4) − 4·B(3) + 6·B(2) − 4·B(1) + B(0)`. -/
def fourthDiff (B : ℕ → R) : R := B 4 - 4 * B 3 + 6 * B 2 - 4 * B 1 + B 0

/-- **Orthogonality (1-body).** A 1-body-LINEAR binding `B_vol(A) = a·A` has
connected 4-body cumulant `0`. -/
theorem fourthDiff_linear (a : R) : fourthDiff (fun n => a * (n : R)) = 0 := by
  simp only [fourthDiff]; push_cast; ring

/-- **Orthogonality (2-body).** A 2-body-ADDITIVE binding proportional to the pair
count (here `b·A(A−1) = 2·C(A,2)·b`, integer form to avoid division) has connected
4-body cumulant `0`. This is `B_sym`'s bond-additive structure. -/
theorem fourthDiff_pairwise (b : R) :
    fourthDiff (fun n => b * ((n : R) * ((n : R) - 1))) = 0 := by
  simp only [fourthDiff]; push_cast; ring

/-- **Non-vacuity / extraction.** A genuine 4-body binding `c·C(A,4)` has connected
4-body cumulant exactly `c`. So `fourthDiff` is a real cumulant extractor (not
identically zero), and the missing ⁴He `b₄` demands an irreducibly 4-body object —
no 1- or 2-body form (the two orthogonality lemmas above) can supply it. -/
theorem fourthDiff_fourBody (c : R) :
    fourthDiff (fun n => c * (Nat.choose n 4 : R)) = c := by
  have h4 : Nat.choose 4 4 = 1 := by decide
  have h3 : Nat.choose 3 4 = 0 := by decide
  have h2 : Nat.choose 2 4 = 0 := by decide
  have h1 : Nat.choose 1 4 = 0 := by decide
  have h0 : Nat.choose 0 4 = 0 := by decide
  simp only [fourthDiff, h4, h3, h2, h1, h0, Nat.cast_one, Nat.cast_zero]; ring

end QOU.MassTheory
