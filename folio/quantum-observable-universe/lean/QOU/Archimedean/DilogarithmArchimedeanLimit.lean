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

-- Ref: [leitner2026] conj:dilogarithm-archimedean-limit
-- Ref: [leitner2026] def:q-pochhammer-partial-product
-- Ref: [faddeev1994] Faddeev, "Current-like variables in massive and massless integrable models," Lectures 1994
-- Ref: [kashaev1997] Kashaev, "The hyperbolic volume of knots from the quantum dilogarithm," Lett. Math. Phys. 39 (1997)
-/

namespace QOU.QPochhammer

/-- Local restatement of the q-Pochhammer denominator, kept self-
    contained so this Lean file does not depend on its sibling
    `q-pochhammer-partial-product.lean`. The two definitions agree
    by inspection. -/
-- Ref: [leitner2026] def:q-pochhammer-partial-product
def denomPolyLocal (q x : ℝ) : ℕ → ℝ
  | 0 => 1
  | n + 1 => (1 - x * q ^ n) * denomPolyLocal q x n

/-- Local restatement of the partial product. -/
-- Ref: [leitner2026] def:q-pochhammer-partial-product
noncomputable def partialProductLocal (q x : ℝ) (n : ℕ) : ℝ :=
  (denomPolyLocal q x n)⁻¹

/-- The classical real dilogarithm series `Σ_{k≥1} x^k / k²`,
    given as a `tsum`. On the closed unit disc the series converges
    absolutely and equals the principal-branch real dilogarithm
    `Real.dilog` (when Mathlib provides it). The `tsum` is `0`
    outside the radius of convergence by Mathlib's convention,
    which suffices for the boundary lemmas below. -/
-- Ref: [leitner2026] conj:dilogarithm-archimedean-limit
noncomputable def LiTwo (x : ℝ) : ℝ :=
  ∑' k : ℕ, x ^ (k + 1) / ((k : ℝ) + 1) ^ 2

/-- Boundary lemma: `LiTwo 0 = 0`. Each term in the series has
    `0 ^ (k+1) = 0`. -/
-- Ref: [leitner2026] conj:dilogarithm-archimedean-limit
@[simp] theorem LiTwo_zero : LiTwo 0 = 0 := by
  unfold LiTwo
  simp

/-- Boundary lemma: at `x = 0` every factor `(1 - x q^k) = 1`, so
    `denomPolyLocal q 0 n = 1`. -/
-- Ref: [leitner2026] def:q-pochhammer-partial-product
theorem denomPoly_zero (q : ℝ) (n : ℕ) :
    denomPolyLocal q 0 n = 1 := by
  induction n with
  | zero => rfl
  | succ k ih =>
    simp [denomPolyLocal, ih]

/-- Boundary lemma: at `x = 0` the partial product is identically
    `1`. -/
-- Ref: [leitner2026] def:q-pochhammer-partial-product
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
-- Ref: [leitner2026] conj:dilogarithm-archimedean-limit
theorem faddeev_limit_at_zero
    (q : ℝ) (n : ℕ) :
    (1 - q) * Real.log (partialProductLocal q 0 n) - LiTwo 0 = 0 := by
  rw [partialProduct_zero, LiTwo_zero]
  simp

/-- The Archimedean-limit conjecture, packaged as a typeclass.
    A concrete instance asserts the convergence
    `(1 - q) · log Φ_n(x; q) → Li₂(x)` along Faddeev's scaling. -/
-- Ref: [leitner2026] conj:dilogarithm-archimedean-limit
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
-- Ref: [leitner2026] conj:dilogarithm-archimedean-limit
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
-- Ref: [leitner2026] conj:dilogarithm-archimedean-limit
theorem LiTwo_one : LiTwo 1 = Real.pi ^ 2 / 6 := by
  rw [LiTwo_one_eq_tsum, ← hasSum_zeta_two.tsum_eq,
      hasSum_zeta_two.summable.tsum_eq_zero_add]
  push_cast
  simp

/-- **Bar-odd cusp partner** `LiTwo (-1) = -π²/12`.  The alternating Basel value
    `-η(2) = -ζ(2)/2`, the natural `sinh`/bar-odd companion of the bar-even
    `LiTwo 1 = π²/6`.  Proved by the duplication `LiTwo 1 + LiTwo (-1) = π²/12`:
    the combined summand `g n = ((-1)^{n+1} + 1)/(n+1)²` vanishes on even `n`, and
    its odd reindex `n = 2k+1` is `½·(k+1)⁻²`, so `∑ g = ½·ζ(2) = π²/12` (the
    even/odd `Function.Injective.hasSum_iff` reindex, as in Mathlib's
    `hasSum_log_sub_log_of_abs_lt_one`).  Subtracting `∑ (n+1)⁻² = ζ(2)` leaves
    `LiTwo (-1) = π²/12 - π²/6 = -π²/12`. -/
theorem LiTwo_neg_one : LiTwo (-1) = -Real.pi ^ 2 / 12 := by
  -- shifted Basel: ∑_k (k+1)⁻² = π²/6
  have hone : HasSum (fun k : ℕ => (1 : ℝ) / ((k : ℝ) + 1) ^ 2) (Real.pi ^ 2 / 6) := by
    have h := (hasSum_nat_add_iff (f := fun n : ℕ => (1 : ℝ) / (n : ℝ) ^ 2) 1).mpr
                (by simpa using hasSum_zeta_two)
    simpa using h
  -- half of it, the odd-reindexed value
  have hhalf : HasSum (fun k : ℕ => (1 / 2 : ℝ) * (1 / ((k : ℝ) + 1) ^ 2))
      (Real.pi ^ 2 / 12) := by
    have := hone.mul_left (1 / 2 : ℝ); convert this using 1; ring
  -- the combined summand g sums to π²/12 via the odd reindex
  have hinj : Function.Injective (fun k : ℕ => 2 * k + 1) := by
    intro a b hab; dsimp only at hab; omega
  have hg : HasSum
      (fun n : ℕ => ((-1 : ℝ)) ^ (n + 1) / ((n : ℝ) + 1) ^ 2 + 1 / ((n : ℝ) + 1) ^ 2)
      (Real.pi ^ 2 / 12) := by
    rw [← hinj.hasSum_iff]
    · -- reindexed function equals hhalf's summand
      have hfun :
          (fun n : ℕ => ((-1 : ℝ)) ^ (n + 1) / ((n : ℝ) + 1) ^ 2 + 1 / ((n : ℝ) + 1) ^ 2)
            ∘ (fun k : ℕ => 2 * k + 1)
          = fun k : ℕ => (1 / 2 : ℝ) * (1 / ((k : ℝ) + 1) ^ 2) := by
        funext k
        simp only [Function.comp]
        have he : ((-1 : ℝ)) ^ (2 * k + 1 + 1) = 1 := Even.neg_one_pow ⟨k + 1, by ring⟩
        have hk : ((k : ℝ) + 1) ≠ 0 := by positivity
        rw [he]; push_cast; field_simp; ring
      rw [hfun]; exact hhalf
    · -- g vanishes off the odds (i.e. on even m)
      intro m hm
      have hmeven : Even m := by
        rcases Nat.even_or_odd m with he | ho
        · exact he
        · obtain ⟨k, rfl⟩ := ho; exact absurd ⟨k, rfl⟩ hm
      have hpow : ((-1 : ℝ)) ^ (m + 1) = -1 := Odd.neg_one_pow hmeven.add_one
      simp only [hpow]; ring
  -- subtract the ζ(2) copy: g n - (n+1)⁻² = (-1)^{n+1}(n+1)⁻²
  have hfneg := hg.sub hone
  simp only [add_sub_cancel_right] at hfneg
  unfold LiTwo
  rw [hfneg.tsum_eq]; ring

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

/-- **Third Part-A reduction (the `m`-series):** interchanging the finite `k`-sum
    with the `m`-tsum (`Summable.tsum_finsetSum`) and summing the geometric
    `k`-series (`geom_sum_eq`) puts `log Φ_n(x; q)` in closed `m`-series form

    `log Φ_n(x; q) = Σ'_m  x^{m+1}/(m+1) · (q^{(m+1)n} − 1)/(q^{m+1} − 1)`.

    This is the exact, finite-`n` object whose `q → 1⁻` limit is `Li₂(x)`: each
    `(q^{(m+1)n} − 1)/(q^{m+1} − 1) → n → ∞`-regularised factor tends to `1/(m+1)`
    as `q → 1⁻`, turning the summand into `x^{m+1}/(m+1)²`.  The termwise limit +
    dominated-convergence exchange with the `m`-sum is the remaining analytic core
    (the `ArchimedeanLimit` class), NOT discharged here. -/
theorem partialProduct_log_eq_mseries (q x : ℝ) (n : ℕ)
    (hpos : ∀ k ∈ Finset.range n, (0 : ℝ) < 1 - x * q ^ k)
    (hlt : ∀ k ∈ Finset.range n, |x * q ^ k| < 1)
    (hq1 : ∀ m : ℕ, q ^ (m + 1) ≠ 1) :
    Real.log (partialProductLocal q x n)
      = ∑' m : ℕ, x ^ (m + 1) / ((m : ℝ) + 1)
          * ((q ^ ((m + 1) * n) - 1) / (q ^ (m + 1) - 1)) := by
  rw [partialProduct_log_eq_tsum q x n hpos hlt,
      ← Summable.tsum_finsetSum
        (fun k hk => (neg_log_one_sub_hasSum (hlt k hk)).summable)]
  refine tsum_congr (fun m => ?_)
  have hrw : ∀ k ∈ Finset.range n,
      (x * q ^ k) ^ (m + 1) / ((m : ℝ) + 1)
        = x ^ (m + 1) / ((m : ℝ) + 1) * (q ^ (m + 1)) ^ k := by
    intro k _; rw [mul_pow, pow_right_comm]; ring
  rw [Finset.sum_congr rfl hrw, ← Finset.mul_sum, geom_sum_eq (hq1 m) n, ← pow_mul]

/-! ## Dilogarithm functional equations

The **duplication (Landen) identity** `Li₂(x) + Li₂(-x) = ½ Li₂(x²)` is a pure
power-series identity — provable, like `LiTwo_neg_one` (its `x = 1` special case),
by the even/odd `Function.Injective.hasSum_iff` reindex.  The **Euler reflection**
`Li₂(x) + Li₂(1-x) = π²/6 - ln x·ln(1-x)` is a *different kind* of identity: it
mixes the series with logarithms, so its proof needs the derivative
`d/dx Li₂(x) = -ln(1-x)/x` (a `HasDerivAt` of the `LiTwo` tsum) + FTC — machinery
Mathlib lacks a `Real.dilog` for.  It is stated below as a **queued formalization**
(honest `sorry`, not discharged). -/

/-- Absolute summability of the `LiTwo` summand on the open unit disc: dominated,
    term by term, by the geometric series `Σ |y|^{k+1}` (each `(k+1)⁻² ≤ 1`). -/
theorem liTwo_summand_summable {y : ℝ} (hy : |y| < 1) :
    Summable (fun k : ℕ => y ^ (k + 1) / ((k : ℝ) + 1) ^ 2) := by
  have hgeom : Summable (fun k : ℕ => |y| ^ (k + 1)) := by
    simpa [pow_succ] using (summable_geometric_of_lt_one (abs_nonneg y) hy).mul_right |y|
  apply Summable.of_norm_bounded hgeom
  intro k
  rw [Real.norm_eq_abs, abs_div, abs_pow,
      abs_of_pos (by positivity : (0 : ℝ) < ((k : ℝ) + 1) ^ 2)]
  exact div_le_self (pow_nonneg (abs_nonneg y) _)
    (by nlinarith [Nat.cast_nonneg (α := ℝ) k])

/-- **Duplication (Landen) identity** `Li₂(x) + Li₂(-x) = ½ Li₂(x²)` for `|x| < 1`.
    Generalises `LiTwo_neg_one` (the `x = 1` boundary case).  The combined summand
    vanishes on even indices; its odd reindex `k = 2j+1` collapses `x^{2j+2}` to
    `(x²)^{j+1}` and halves the weight, via the even/odd
    `Function.Injective.hasSum_iff` reindex + `HasSum.unique`. -/
theorem LiTwo_duplication (x : ℝ) (hx : |x| < 1) :
    LiTwo x + LiTwo (-x) = (1 / 2) * LiTwo (x ^ 2) := by
  have hxabs : |(-x)| < 1 := by rwa [abs_neg]
  have hx2abs : |x ^ 2| < 1 := by
    rw [abs_pow]; exact pow_lt_one₀ (abs_nonneg x) hx (by norm_num)
  have hxs : HasSum (fun k : ℕ => x ^ (k + 1) / ((k : ℝ) + 1) ^ 2) (LiTwo x) :=
    (liTwo_summand_summable hx).hasSum
  have hnxs : HasSum (fun k : ℕ => (-x) ^ (k + 1) / ((k : ℝ) + 1) ^ 2) (LiTwo (-x)) :=
    (liTwo_summand_summable hxabs).hasSum
  have hx2s : HasSum (fun k : ℕ => (x ^ 2) ^ (k + 1) / ((k : ℝ) + 1) ^ 2) (LiTwo (x ^ 2)) :=
    (liTwo_summand_summable hx2abs).hasSum
  have hg := hxs.add hnxs
  have hinj : Function.Injective (fun j : ℕ => 2 * j + 1) := by
    intro a b hab; dsimp only at hab; omega
  have hvanish : ∀ m ∉ Set.range (fun j : ℕ => 2 * j + 1),
      (fun k : ℕ => x ^ (k + 1) / ((k : ℝ) + 1) ^ 2 + (-x) ^ (k + 1) / ((k : ℝ) + 1) ^ 2) m = 0 := by
    intro m hm
    have hmeven : Even m := by
      rcases Nat.even_or_odd m with he | ho
      · exact he
      · obtain ⟨k, rfl⟩ := ho; exact absurd ⟨k, rfl⟩ hm
    have hpow : ((-x) : ℝ) ^ (m + 1) = -(x ^ (m + 1)) := by
      rw [neg_pow, Odd.neg_one_pow hmeven.add_one]; ring
    simp only [hpow]; ring
  have hodd := (hinj.hasSum_iff hvanish).mpr hg
  have hhalf : HasSum (fun j : ℕ => (1 / 2 : ℝ) * ((x ^ 2) ^ (j + 1) / ((j : ℝ) + 1) ^ 2))
      ((1 / 2) * LiTwo (x ^ 2)) := hx2s.mul_left (1 / 2)
  have hfun :
      (fun k : ℕ => x ^ (k + 1) / ((k : ℝ) + 1) ^ 2 + (-x) ^ (k + 1) / ((k : ℝ) + 1) ^ 2)
        ∘ (fun j : ℕ => 2 * j + 1)
      = fun j : ℕ => (1 / 2 : ℝ) * ((x ^ 2) ^ (j + 1) / ((j : ℝ) + 1) ^ 2) := by
    funext j
    simp only [Function.comp]
    have hoddpow : ((-x) : ℝ) ^ (2 * j + 1 + 1) = x ^ (2 * j + 1 + 1) := by
      rw [neg_pow, Even.neg_one_pow ⟨j + 1, by ring⟩]; ring
    rw [hoddpow, show 2 * j + 1 + 1 = 2 * (j + 1) from by ring, pow_mul]
    have h2 : (2 * (j : ℝ) + 2) ≠ 0 := by positivity
    have hj : ((j : ℝ) + 1) ≠ 0 := by positivity
    push_cast; field_simp; ring
  rw [hfun] at hodd
  exact hodd.unique hhalf

/-
**Euler reflection** `Li₂(x) + Li₂(1-x) = π²/6 - ln x · ln(1-x)` for `x ∈ (0,1)`
is now **PROVED sorry-free** in the downstream module
`QOU.Archimedean.DilogReflection` as `LiTwo_reflection'`.  The proof required
building the dilogarithm derivative `d/dx Li₂(x) = -ln(1-x)/x` (a `HasDerivAt`
of the `LiTwo` tsum, which Mathlib lacks — no `Real.dilog`), Abel's limit
theorem, continuity of `Li₂` at 0, and `ln x·ln(1-x) → 0`.  That development
lives downstream because it needs the heavy analytic imports
(`Mathlib.Analysis.Complex.AbelLimit`, `SmoothSeries`, `MeanValue`,
`Pow.Asymptotics`, `Log.NegMulLog`); folding them into this base file — imported
by six modules — would bloat every consumer's dependency cone.  The formerly
`sorry`-carrying stub here was removed 2026-07-19; use `LiTwo_reflection'`.
-- Ref: [leitner2026] Euler reflection formula; Lewin, "Polylogarithms and Associated Functions" (1981)
-/

end QOU.QPochhammer
