/-!
# Archimedean limit of Φ_n(x; q): conjecture statement

The conjecture: under the joint Faddeev scaling q → 1, n → ∞,
n(1-q) → ∞, the rescaled logarithm (1-q) · log Φ_n(x; q) converges
to the classical dilogarithm Li₂(x).

This file provides:
* a concrete Mathlib-backed definition of `LiTwo : ℝ → ℝ` as the
  series Σ_{k≥1} x^k / k², replacing the previous `opaque`
  placeholder. The series converges absolutely on the closed unit
  disc, divergently outside it; at `|x| ≤ 1` the value coincides
  with the principal-branch real dilogarithm.
* unconditional boundary lemmas (`LiTwo_zero`, `partialProduct_zero`)
  that anchor the conjecture's class instances at the only points
  where the Faddeev limit is trivial.
* the conjecture, packaged as the typeclass `ArchimedeanLimit`, with
  one field stating the convergence of `(1-q) log Φ_n(x;q)` to
  `LiTwo x` along Faddeev's joint scaling. The class is the §3b-cond
  hook used by `prop:archimedean-functor-uniqueness`.

A complete sorry-free Lean proof of the convergence still awaits
Mathlib infrastructure (a uniform Tauberian theorem, branch-cut
control on the principal-branch dilogarithm). The class formulation
isolates that gap.

-- Ref: [manuscript] conj:dilogarithm-archimedean-limit
-- Ref: [faddeev1994] Faddeev, "Current-like variables in massive and massless integrable models," Lectures 1994
-- Ref: [kashaev1997] Kashaev, "The hyperbolic volume of knots from the quantum dilogarithm," Lett. Math. Phys. 39 (1997)
-/

import Mathlib.Algebra.BigOperators.Basic
import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Analysis.SpecificLimits.Normed
import Mathlib.Topology.Algebra.InfiniteSum.Basic
import Mathlib.Tactic

namespace QOU.QPochhammer

/-- Local restatement of the q-Pochhammer denominator, kept self-
    contained so this Lean file does not depend on its sibling
    `q-pochhammer-partial-product.lean`. The two definitions agree
    by inspection. -/
-- Ref: [manuscript] def:q-pochhammer-partial-product
def denomPolyLocal (q x : ℝ) : ℕ → ℝ
  | 0 => 1
  | n + 1 => (1 - x * q ^ n) * denomPolyLocal q x n

/-- Local restatement of the partial product. -/
-- Ref: [manuscript] def:q-pochhammer-partial-product
noncomputable def partialProductLocal (q x : ℝ) (n : ℕ) : ℝ :=
  (denomPolyLocal q x n)⁻¹

/-- The classical real dilogarithm series `Σ_{k≥1} x^k / k²`,
    given as a `tsum`. On the closed unit disc the series converges
    absolutely and equals the principal-branch real dilogarithm
    `Real.dilog` (when Mathlib provides it). The `tsum` is `0`
    outside the radius of convergence by Mathlib's convention,
    which suffices for the boundary lemmas below. -/
-- Ref: [manuscript] conj:dilogarithm-archimedean-limit
noncomputable def LiTwo (x : ℝ) : ℝ :=
  ∑' k : ℕ, x ^ (k + 1) / ((k : ℝ) + 1) ^ 2

/-- Boundary lemma: `LiTwo 0 = 0`. Each term in the series has
    `0 ^ (k+1) = 0`. -/
-- Ref: [manuscript] conj:dilogarithm-archimedean-limit
@[simp] theorem LiTwo_zero : LiTwo 0 = 0 := by
  unfold LiTwo
  simp

/-- Boundary lemma: at `x = 0` every factor `(1 - x q^k) = 1`, so
    `denomPolyLocal q 0 n = 1`. -/
-- Ref: [manuscript] def:q-pochhammer-partial-product
theorem denomPoly_zero (q : ℝ) (n : ℕ) :
    denomPolyLocal q 0 n = 1 := by
  induction n with
  | zero => rfl
  | succ k ih =>
    simp [denomPolyLocal, ih]

/-- Boundary lemma: at `x = 0` the partial product is identically
    `1`. -/
-- Ref: [manuscript] def:q-pochhammer-partial-product
@[simp] theorem partialProduct_zero (q : ℝ) (n : ℕ) :
    partialProductLocal q 0 n = 1 := by
  unfold partialProductLocal
  rw [denomPoly_zero]
  simp

/-- Boundary case of the Faddeev limit: at `x = 0` the rescaled
    logarithm of the partial product is `0` for every `(q, n)`,
    matching `LiTwo 0 = 0`. This is the only point at which the
    Faddeev limit is unconditional in Lean (no Tauberian input
    required). -/
-- Ref: [manuscript] conj:dilogarithm-archimedean-limit
theorem faddeev_limit_at_zero
    (q : ℝ) (n : ℕ) :
    (1 - q) * Real.log (partialProductLocal q 0 n) - LiTwo 0 = 0 := by
  rw [partialProduct_zero, LiTwo_zero]
  simp

/-- The Archimedean-limit conjecture, packaged as a typeclass.
    A concrete instance asserts the convergence
    `(1 - q) · log Φ_n(x; q) → Li₂(x)` along Faddeev's scaling. -/
-- Ref: [manuscript] conj:dilogarithm-archimedean-limit
class ArchimedeanLimit (x : ℝ) : Prop where
  /-- The Faddeev limit of the rescaled log partial product equals
      the classical dilogarithm. The hypotheses on `(q, n)` capture
      the joint scaling `q → 1`, `n → ∞`, `n(1-q) → ∞`. -/
  -- Ref: [faddeev1994] https://doi.org/10.1142/S0217732394002793
  faddeev_limit :
    ∀ ε > (0 : ℝ),
      ∃ δ > (0 : ℝ), ∀ q n,
        (1 - δ < q) ∧ (q < 1) ∧ (n : ℝ) * (1 - q) > δ⁻¹ →
          ‖(1 - q) * Real.log (partialProductLocal q x n) - LiTwo x‖ < ε

/-- Stated form of the conjecture (sorry-free at the level of Lean,
    inhabited only via a `[ArchimedeanLimit x]` typeclass instance). -/
-- Ref: [manuscript] conj:dilogarithm-archimedean-limit
theorem partialProduct_to_LiTwo (x : ℝ) [h : ArchimedeanLimit x]
    (ε : ℝ) (hε : 0 < ε) :
    ∃ δ > (0 : ℝ), ∀ q n,
      (1 - δ < q) ∧ (q < 1) ∧ (n : ℝ) * (1 - q) > δ⁻¹ →
        ‖(1 - q) * Real.log (partialProductLocal q x n) - LiTwo x‖ < ε :=
  h.faddeev_limit ε hε

/-- **Unconditional instance at `x = 0`.** The Faddeev limit holds
    trivially at the boundary point `x = 0` because both sides of
    the asserted convergence are identically zero, so the limit is
    the constant zero sequence. This is the only point at which the
    `ArchimedeanLimit` class can be inhabited without further
    Mathlib infrastructure; for every `x ∈ (0, 1)` the instance
    requires the full Tauberian argument from Faddeev 1994 /
    Kashaev 1997. -/
-- Ref: [faddeev1994] Faddeev, "Current-like variables in massive and massless integrable models," Lectures 1994
instance archimedeanLimit_zero : ArchimedeanLimit 0 where
  faddeev_limit := by
    intro ε hε
    refine ⟨1, by norm_num, ?_⟩
    intro q n _
    rw [faddeev_limit_at_zero]
    simpa using hε

end QOU.QPochhammer
