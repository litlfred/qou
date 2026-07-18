import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Analysis.SpecialFunctions.Log.Deriv
import Mathlib.Topology.Algebra.InfiniteSum.Basic
import Mathlib.NumberTheory.ZetaValues
import Mathlib.Tactic


/-!
# Dilogarithm Archimedean-limit primitives (`QOU.QPochhammer`)

Importable lib-module home for the **sorry-free concrete primitives** of
the Faddeev–Kashaev / Archimedean-limit construction:

* `denomPolyLocal` / `partialProductLocal` — the q-Pochhammer partial
  product `Φ_n(x; q)`;
* `LiTwo` — the classical dilogarithm series `Σ_{k≥1} x^k / k²`;
* the boundary lemmas `LiTwo_zero`, `denomPoly_zero`,
  `partialProduct_zero`, `faddeev_limit_at_zero`;
* the open conjecture class `ArchimedeanLimit`, its stated form
  `partialProduct_to_LiTwo`, and the unconditional boundary instance
  `archimedeanLimit_zero`.

These were previously defined only in the content-block sibling
`mass-theory/dilogarithm-archimedean-limit.lean`, which — being a content
sibling, not a Lake module — is not importable.  Downstream blocks that
need the concrete primitives (`predicted-spectra/cl2-pentagon-and-faddeev-partial`,
and the `dilogarithm-archimedean-limit` block itself) now import this
module, giving the definitions a single source of truth.  The conjecture
class `ArchimedeanLimit` and its boundary instance were promoted here too
(2026-06-29) so that the sibling `phi-q-wkb-greens-function.lean`, whose
`WKBGreensFunction` class `extends ArchimedeanLimit`, can import the class
rather than depend on a non-importable content sibling.

-- Ref: [manuscript] conj:dilogarithm-archimedean-limit
-- Ref: [manuscript] def:q-pochhammer-partial-product
-- Ref: [faddeev1994] Faddeev, "Current-like variables in massive and massless integrable models," Lectures 1994
-- Ref: [kashaev1997] Kashaev, "The hyperbolic volume of knots from the quantum dilogarithm," Lett. Math. Phys. 39 (1997)
-/

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
      ∃ δ > (0 : ℝ), ∀ (q : ℝ) (n : ℕ),
        (1 - δ < q) ∧ (q < 1) ∧ (n : ℝ) * (1 - q) > δ⁻¹ →
          ‖(1 - q) * Real.log (partialProductLocal q x n) - LiTwo x‖ < ε

/-- Stated form of the conjecture (sorry-free at the level of Lean,
    inhabited only via a `[ArchimedeanLimit x]` typeclass instance). -/
-- Ref: [manuscript] conj:dilogarithm-archimedean-limit
theorem partialProduct_to_LiTwo (x : ℝ) [h : ArchimedeanLimit x]
    (ε : ℝ) (hε : 0 < ε) :
    ∃ δ > (0 : ℝ), ∀ (q : ℝ) (n : ℕ),
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

/-! ## Part B primitives — the substrate `q → 1⁺` continuation

Sorry-free primitives for the Part-B derivation
(`docs/audits/2026-07-17-dilog-archimedean-limit-partB-pole-cancellation.md`,
`computations/dilog_archimedean_partB_probe.py`): the substrate continuation
crosses the cusp `x = 1`, where the factors `1 − x qᵏ` with `k > k*` turn
negative. The two facts formalizable within this module's imports (`Log.Basic`,
`InfiniteSum.Basic`) are the **algebraic pole-subtraction** and the reduction of
the **cusp value** `LiTwo 1` to the Basel series.  -/

/-- **Pole-subtraction (algebraic core of Part B).** For a negative factor
    `1 − w < 0` (i.e. `w > 1`), the principal `log|1 − w| = log(w − 1)` splits as
    the **algebraic pole** `log w` plus the convergent remainder `log(1 − w⁻¹)`:

    `log(w − 1) = log w + log(1 − w⁻¹)`.

    This is exactly the subtraction that regularizes each `k > k*` factor in the
    Part-B continuation (the `+iπ` branch phase lives on the complex side and is
    the Faddeev modular anomaly; here we isolate the real magnitude). -/
theorem log_neg_factor_split (w : ℝ) (hw : 1 < w) :
    Real.log (w - 1) = Real.log w + Real.log (1 - w⁻¹) := by
  have hw0 : 0 < w := lt_trans one_pos hw
  rw [← Real.log_mul (by positivity)
        (by nlinarith [inv_pos.mpr hw0, inv_lt_one_iff₀.mpr (Or.inr hw)])]
  congr 1
  field_simp

/-- **The cusp value `LiTwo 1` is the Basel series** `∑' 1/(k+1)²` (definitional:
    `1^(k+1) = 1`). This isolates the entire remaining analytic input of Part B to
    a single named Mathlib result: `LiTwo 1 = π²/6` follows from
    `hasSum_zeta_two` (`Mathlib.NumberTheory.ZetaValues`, the Basel problem —
    `∑' n:ℕ, 1/n² = π²/6`, whose `n=0` term is `0`), the extended-Bloch / Rogers
    regulator constant `ζ(2) = Li₂(1)` that Part B derives as the quantum-dilog
    inversion constant. -/
theorem LiTwo_one_eq_tsum : LiTwo 1 = ∑' k : ℕ, (1 : ℝ) / ((k : ℝ) + 1) ^ 2 := by
  unfold LiTwo
  simp

/-- **The cusp value is `ζ(2) = π²/6`.** Closes the last analytic input of the
    Part-B derivation: the residual `LiTwo 1` left after the pole-subtraction and
    the `T_w` Frobenius truncation is the Basel constant, obtained here from
    Mathlib's `hasSum_zeta_two` (Basel problem, `∑' n:ℕ, 1/n² = π²/6`) by splitting
    off the vanishing `n = 0` term.  This is the extended-Bloch / Rogers regulator
    constant `ζ(2) = Li₂(1)` that Part B identifies as the (quantum-)dilogarithm
    inversion constant. -/
-- Ref: [manuscript] conj:dilogarithm-archimedean-limit
theorem LiTwo_one : LiTwo 1 = Real.pi ^ 2 / 6 := by
  rw [LiTwo_one_eq_tsum, ← hasSum_zeta_two.tsum_eq,
      hasSum_zeta_two.summable.tsum_eq_zero_add]
  push_cast
  simp

/-! ## Part A primitives — the sub-unity reduction (`x ∈ (0,1)`, `q ∈ (0,1)`)

The elementary (sub-unity) direction of `conj:dilogarithm-archimedean-limit`.
These are the **sorry-free algebraic steps** that turn `log Φ_n(x; q)` into the
per-factor `-log(1 - x qᵏ)` series; each factor then expands via the classical
`-log(1 - y) = Σ_{m≥1} yᵐ/m` power series (Mathlib `hasSum_pow_div_log`).  The
remaining input of Part A — the *uniform / Tauberian* exchange of the `q → 1⁻`,
`n → ∞` limit with the `m`-sum that produces `Li₂(x) = Σ x^m/m²` — is the
analytic core, still carried by the `ArchimedeanLimit` class (not discharged
here).  These primitives are the scaffolding that a proof of that exchange
builds on. -/

/-- **Per-factor log expansion.** Each Faddeev factor contributes the classical
    series `-log(1 - y) = Σ_{m≥1} yᵐ/m` for `|y| < 1` (Mathlib
    `hasSum_pow_div_log_of_abs_lt_one`).  Applied with `y = x qᵏ` this is the
    per-crossing term of the archimedean limit. -/
theorem neg_log_one_sub_hasSum {y : ℝ} (hy : |y| < 1) :
    HasSum (fun m : ℕ => y ^ (m + 1) / (m + 1)) (-Real.log (1 - y)) :=
  Real.hasSum_pow_div_log_of_abs_lt_one hy

/-- The recursive `denomPolyLocal` is the finite product of Faddeev factors
    `∏_{k<n} (1 - x qᵏ)`. -/
theorem denomPolyLocal_eq_prod (q x : ℝ) (n : ℕ) :
    denomPolyLocal q x n = ∏ k ∈ Finset.range n, (1 - x * q ^ k) := by
  induction n with
  | zero => simp [denomPolyLocal]
  | succ m ih => rw [denomPolyLocal, Finset.prod_range_succ, ih]; ring

/-- **First Part-A reduction:** the log of the partial product is the finite sum
    of the per-factor logs, `log Φ_n(x; q) = Σ_{k<n} -log(1 - x qᵏ)`, whenever
    every factor is positive (guaranteed for `x ∈ [0,1)`, `q ∈ [0,1]`). -/
theorem partialProduct_log_eq (q x : ℝ) (n : ℕ)
    (hpos : ∀ k ∈ Finset.range n, (0 : ℝ) < 1 - x * q ^ k) :
    Real.log (partialProductLocal q x n)
      = ∑ k ∈ Finset.range n, -Real.log (1 - x * q ^ k) := by
  unfold partialProductLocal
  rw [Real.log_inv, denomPolyLocal_eq_prod,
      Real.log_prod _ _ (fun k hk => (hpos k hk).ne')]
  simp

/-- **Second Part-A reduction:** each per-factor log becomes the `Li`-type power
    series, so `log Φ_n(x; q) = Σ_{k<n} Σ'_{m} (x qᵏ)^{m+1}/(m+1)`.  Requires each
    Faddeev factor to be both positive and inside the radius of convergence
    (`|x qᵏ| < 1`), automatic for `x ∈ [0,1)`, `q ∈ [0,1]`.  This is the exact,
    finite-`n` reduction of the log partial product to the double `(k, m)` series
    whose `q → 1⁻` limit is `Li₂`; the outstanding Part-A input is the uniform
    (Tauberian) exchange of that limit with the `m`-sum, still carried by
    `ArchimedeanLimit`. -/
theorem partialProduct_log_eq_tsum (q x : ℝ) (n : ℕ)
    (hpos : ∀ k ∈ Finset.range n, (0 : ℝ) < 1 - x * q ^ k)
    (hlt : ∀ k ∈ Finset.range n, |x * q ^ k| < 1) :
    Real.log (partialProductLocal q x n)
      = ∑ k ∈ Finset.range n, ∑' m : ℕ, (x * q ^ k) ^ (m + 1) / (m + 1) := by
  rw [partialProduct_log_eq q x n hpos]
  exact Finset.sum_congr rfl
    (fun k hk => ((neg_log_one_sub_hasSum (hlt k hk)).tsum_eq).symm)

end QOU.QPochhammer
