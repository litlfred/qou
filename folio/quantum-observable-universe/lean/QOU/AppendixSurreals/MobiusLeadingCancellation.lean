/-
  Möbius surreal renormalization — the leading-coefficient cancellation,
  generic-R (§7c: no archimedean content).

  `rem:mobius-surreal-renormalization` (appendix-surreals) writes the Möbius
  knot-energy's Hadamard finite part as `std(I₁ − I₂)` for two infinite
  surreals of `ord_ω = +1`, and reduces its finiteness to the algebraic
  leading-coefficient match `[ω^{+1}]I₁ = [ω^{+1}]I₂`. This file formalizes
  that *algebraic reduction*: in any module carrying a distinguished
  "finite part" submodule `F` and an infinite unit `Ω` independent of it,
  a difference of two `ord ≤ 1` elements is finite **iff** their leading
  coefficients agree.

  HONEST SCOPE. This is the cancellation step only. NOT formalized here:
  (i) the analytic input that the two Möbius integrals share the same
  leading coefficient (`|ϱ(s)−ϱ(t)| = D(s,t) + O(|s−t|³)` near the
  diagonal); (ii) the surreal field `No`, its `ω`-order valuation, and the
  standard-part map (the `st = 𝓛^med` identification,
  `rem:st-is-median-resummation`). The abstraction (module + finite-part
  submodule + independent infinite unit) is the weakest structure in which
  the reduction is a theorem, per the §7c base-ring convention.

  Audit: docs/audits/2026-07-19-jets-alien-qmobius-bring-interaction.md §3.3.

  -- Ref: [leitner2026] appendix-surreals, rem:mobius-surreal-renormalization
-/

import Mathlib.Algebra.Module.Submodule.Basic
import Mathlib.Tactic.Abel

namespace QOU.AppendixSurreals.MobiusLeadingCancellation

variable {R : Type*} [Ring R] {M : Type*} [AddCommGroup M] [Module R M]

/-- The infinite unit `Ω` is independent of the finite part `F`: no nonzero
    scalar multiple of `Ω` is finite. In the surreal application `Ω` plays
    `ω^{+1}` and `F` the finite (`ord_ω ≤ 0`) elements. -/
def IndependentOfFinite (F : Submodule R M) (Ω : M) : Prop :=
  ∀ a : R, a • Ω ∈ F → a = 0

/-- **Leading-coefficient cancellation.** For `ord ≤ 1` elements
    `a • Ω + f` and `b • Ω + g` (with `f, g` finite), the difference is
    finite iff the leading coefficients agree: `[Ω](I₁) = [Ω](I₂)`.
    This is the algebraic content of the Möbius surreal renormalization's
    finiteness bound. -/
theorem sub_mem_finite_iff {F : Submodule R M} {Ω : M}
    (hindep : IndependentOfFinite F Ω)
    {a b : R} {f g : M} (hf : f ∈ F) (hg : g ∈ F) :
    (a • Ω + f) - (b • Ω + g) ∈ F ↔ a = b := by
  have key : (a • Ω + f) - (b • Ω + g) = (a - b) • Ω + (f - g) := by
    rw [sub_smul]; abel
  constructor
  · intro hmem
    rw [key] at hmem
    have hlead : (a - b) • Ω ∈ F := by
      have := F.sub_mem hmem (F.sub_mem hf hg)
      simpa using this
    exact sub_eq_zero.mp (hindep _ hlead)
  · intro hab
    subst hab
    have h2 : (a • Ω + f) - (a • Ω + g) = f - g := by abel
    rw [h2]
    exact F.sub_mem hf hg

/-- **The Möbius application direction.** Two `ord ≤ 1` elements with the
    *same* leading coefficient `c` (the shared `c·ω` divergence of `I₁`,
    `I₂` in `rem:mobius-surreal-renormalization`) have finite difference —
    the `ω^{+1}` parts cancel. Requires no independence hypothesis. -/
theorem sub_mem_finite_of_leading_eq {F : Submodule R M} {Ω : M}
    {c : R} {f g : M} (hf : f ∈ F) (hg : g ∈ F) :
    (c • Ω + f) - (c • Ω + g) ∈ F := by
  have h2 : (c • Ω + f) - (c • Ω + g) = f - g := by abel
  rw [h2]
  exact F.sub_mem hf hg

end QOU.AppendixSurreals.MobiusLeadingCancellation
