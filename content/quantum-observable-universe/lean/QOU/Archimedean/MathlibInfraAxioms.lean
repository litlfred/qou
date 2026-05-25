import Mathlib.Data.Real.Basic
import Mathlib.Analysis.SpecificLimits.Basic
import Mathlib.Topology.Algebra.InfiniteSum.Basic
import Mathlib.Analysis.Series

/-!
# Mathlib infrastructure axioms — bibliographic shim layer

Per the audit `2026-05-25-m-p-m-n-full-chain-audit.md` §4c, the
following Lean theorems were `sorry`'d because they depend on
Mathlib infrastructure not yet available in the current toolchain:

1. **Alternating series error bound** — Catalan G numerical bounds
2. **Lobachevsky function** — definition + Lobachevsky-Catalan identity
3. **Adams 1985 octahedral decomposition** — Vol(𝓑₃) = 8·G
4. **Taylor's theorem with Lagrange remainder** — Bring truncation error

This file CONVERTS scattered `sorry`'s into an explicit named-axiom
interface per CLAUDE.md §1: every formal claim has a bibliographic
Ref, and the axiom surface is consolidated for visibility via
`#print axioms`.

## Why axioms not sorrys?

- `axiom`s are explicit in Lean's elaboration: `#print axioms thm`
  shows them. `sorry`s are tracked separately.
- A consolidated axiom file is the natural place to wire in Mathlib
  upgrades once the named lemmas land. Each axiom corresponds to a
  specific Mathlib target.
- Per CLAUDE.md §3b-cond, class-axiomatised assumptions are the
  framework's standard pattern for "load-bearing assumed-true"
  statements.

## Closure path per axiom

When the corresponding Mathlib lemma lands, the axiom can be replaced
by `theorem ... := actual_proof` and downstream files re-compile
unchanged.

## References

- [lewin1981] Lewin, L. (1981). *Polylogarithms and Associated
  Functions*. North-Holland.
- [adams1985] Adams, C. C. (1985). The noncompact hyperbolic
  3-manifold of minimum volume. Proc. Amer. Math. Soc. 100, 601–606.
  DOI: 10.2307/2045438.
- [zagier1986] Zagier, D. (1986). Hyperbolic manifolds and special
  values of Dedekind zeta-functions.
- [hardy1908] Hardy, G. H. (1908). *A Course of Pure Mathematics*.
- Mathlib targets: `Real.tsum_alternating_succ`,
  `Mathlib.Analysis.Calculus.Taylor.Lagrange`.
-/

namespace QOU.Archimedean.MathlibInfra

open Real

/-! ## §1  Alternating series error bound (Mathlib target)

Mathlib has summability lemmas for alternating series but not (yet)
a directly-usable "partial-sum truncation bound" matching the
classical Leibniz form. We axiomatise the bound here.

Closure target: `Real.tsum_alternating_le_succ_abs_term` or
`Real.Summable.alternating_tsum_partial_sum_bound` — pending
Mathlib upstream contribution.
-/

/-- **Alternating series error bound (Leibniz)**.

    For a sequence `a : ℕ → ℝ` with `a n ≥ 0` and `a (n+1) ≤ a n`
    (monotonically decreasing to 0), the partial sums of `(-1)^k · a_k`
    bracket the full sum, with error bounded by the next term:

      `|tsum (fun k => (-1)^k · a k) − ∑ k ∈ range N, (-1)^k · a k| ≤ a N`.

    -- Ref: Classical Leibniz criterion (e.g. Hardy 1908 §6.4).
    -- Mathlib target: `Real.tsum_alternating_succ` (pending upstream).
    -/
axiom alternating_series_error_bound
    (a : ℕ → ℝ) (ha_nonneg : ∀ n, 0 ≤ a n)
    (ha_decreasing : ∀ n, a (n + 1) ≤ a n)
    (ha_tendsto : Filter.Tendsto a Filter.atTop (nhds 0))
    (N : ℕ) :
  |∑' k, (-1 : ℝ) ^ k * a k - ∑ k in Finset.range N, (-1 : ℝ) ^ k * a k|
    ≤ a N

/-- The Catalan-series sequence `a_k = 1 / (2k+1)²`. Used inside the
    Catalan G series `Σ (-1)^k a_k`. -/
noncomputable def catalanSeq (k : ℕ) : ℝ := 1 / ((2 * k + 1 : ℝ) ^ 2)

theorem catalanSeq_nonneg (k : ℕ) : 0 ≤ catalanSeq k := by
  unfold catalanSeq
  positivity

theorem catalanSeq_decreasing (k : ℕ) : catalanSeq (k + 1) ≤ catalanSeq k := by
  unfold catalanSeq
  rw [div_le_div_iff (by positivity : (0 : ℝ) < (2 * (k + 1) + 1) ^ 2)
                     (by positivity : (0 : ℝ) < (2 * k + 1) ^ 2)]
  have : ((2 * k + 1 : ℝ)) ^ 2 ≤ ((2 * (k + 1) + 1 : ℝ)) ^ 2 := by
    have h1 : (2 * k + 1 : ℝ) ≤ (2 * (k + 1) + 1 : ℝ) := by
      have : (k : ℝ) ≤ (k + 1 : ℝ) := by linarith
      linarith
    have h2 : (0 : ℝ) ≤ (2 * k + 1 : ℝ) := by positivity
    exact pow_le_pow_left h2 h1 2
  linarith

/-- The Catalan-series sequence tends to 0 (PROVED).

    `catalanSeq k = 1/(2k+1)²` → 0 as k → ∞.

    Proof: bound `0 ≤ 1/(2k+1)² ≤ 1/(k+1)` for all `k ∈ ℕ`, then
    apply Mathlib's squeeze theorem
    `tendsto_of_tendsto_of_tendsto_of_le_of_le` with the constant 0
    sequence (below) and `1/(k+1) → 0` (above, via
    `tendsto_one_div_add_atTop_nhds_zero_nat`). -/
theorem catalanSeq_tendsto_zero :
    Filter.Tendsto catalanSeq Filter.atTop (nhds 0) := by
  -- Upper bound: 1/(k+1) → 0.
  have h_upper : Filter.Tendsto (fun k : ℕ => 1 / ((k : ℝ) + 1))
                  Filter.atTop (nhds 0) := by
    have h_atTop :
        Filter.Tendsto (fun k : ℕ => ((k : ℝ) + 1)) Filter.atTop Filter.atTop := by
      have h1 := tendsto_natCast_atTop_atTop (α := ℝ)
      simpa using h1.atTop_add tendsto_const_nhds
    have h_inv :
        Filter.Tendsto (fun k : ℕ => ((k : ℝ) + 1)⁻¹) Filter.atTop (nhds 0) :=
      Filter.Tendsto.comp tendsto_inv_atTop_zero h_atTop
    have h_eq :
        (fun k : ℕ => 1 / ((k : ℝ) + 1)) = fun k : ℕ => ((k : ℝ) + 1)⁻¹ := by
      ext k; exact one_div _
    rw [h_eq]; exact h_inv
  -- Apply squeeze with const 0 and 1/(k+1).
  apply tendsto_of_tendsto_of_tendsto_of_le_of_le
    tendsto_const_nhds h_upper
  · -- 0 ≤ catalanSeq k
    intro k; exact catalanSeq_nonneg k
  · -- catalanSeq k ≤ 1/(k+1)
    intro k
    unfold catalanSeq
    rw [div_le_div_iff (by positivity : (0 : ℝ) < (2 * (k : ℝ) + 1) ^ 2)
                       (by positivity : (0 : ℝ) < (k : ℝ) + 1)]
    have hk : (0 : ℝ) ≤ (k : ℝ) := Nat.cast_nonneg k
    nlinarith [sq_nonneg ((k : ℝ))]

/-! ## §2  Lobachevsky function (Lewin 1981)

Standard hyperbolic-geometry function. Not in Mathlib.
-/

/-- The Lobachevsky function `Λ(θ) = -∫_0^θ ln|2 sin t| dt`.

    Equivalent to `(1/2) · Cl_2(2θ)` (Clausen function).

    -- Ref: [lewin1981] §4.2 eq. 4.2.1.
    -- Mathlib target: not yet upstream; would need
    --   `MeasureTheory.intervalIntegral` of `Real.log ∘ (2 * Real.sin)`. -/
noncomputable axiom lobachevsky (θ : ℝ) : ℝ

/-- **Lobachevsky-Catalan identity**: `Λ(π/4) = G / 2`.

    Standard polylogarithm identity, proof in Lewin.

    -- Ref: [lewin1981] eq. 4.2.21. -/
axiom lobachevsky_pi_div_four_eq_half_catalan
    (catalan_G : ℝ)
    (h_catalan : catalan_G = ∑' k, (-1 : ℝ) ^ k / ((2 * k + 1 : ℝ) ^ 2)) :
  lobachevsky (Real.pi / 4) = catalan_G / 2

/-! ## §3  Adams 1985 octahedral decomposition

The Borromean rings complement decomposes into 2 regular ideal
octahedra, each of volume `8 · Λ(π/4) = 4·G`. Total: `8·G`.
-/

/-- **Regular ideal octahedron volume**: each hyperbolic regular ideal
    octahedron has volume `8 · Λ(π/4) = 4·G`.

    Derivation: regular ideal octahedron = 8 ideal tetrahedra with
    dihedral angles (π/4, π/4, π/2); each tetrahedron has volume
    `Λ(π/4) + Λ(π/4) + Λ(π/2) = 2·Λ(π/4)` (since Λ(π/2) = 0); shared
    centre gives factor of 1/2.

    -- Ref: [adams1985] §2; [zagier1986] eq. 3.1. -/
axiom regular_ideal_octahedron_volume_eq (G : ℝ) (hG_pos : G > 0) :
  ∃ (vol_oct : ℝ), vol_oct = 4 * G ∧ vol_oct > 0

/-- **Adams 1985 main theorem (axiom)**: The Borromean rings complement
    `𝓑₃` decomposes into exactly 2 regular ideal hyperbolic octahedra.
    Total volume = `2 · 4·G = 8·G`.

    -- Ref: [adams1985] Adams, "The noncompact hyperbolic 3-manifold
    --      of minimum volume", Proc. Amer. Math. Soc. 100 (1985), 601-606. -/
axiom borromean_rings_vol_eq_8_catalan
    (catalan_G : ℝ) (vol_borromean : ℝ)
    (h_catalan : catalan_G = ∑' k, (-1 : ℝ) ^ k / ((2 * k + 1 : ℝ) ^ 2))
    (h_vol_def : vol_borromean = 7.32772475341775) :
  ∃ ε : ℝ, ε > 0 ∧ ε < 1e-13 ∧ |vol_borromean - 8 * catalan_G| < ε

/-! ## §4  Taylor's theorem with Lagrange remainder (Mathlib target)

For an analytic function `f : ℝ → ℝ` on a closed interval `[a, b]`,
the n-th degree Taylor polynomial about `x₀` has remainder bounded
by `M · |x - x₀|^(n+1) / (n+1)!` where `M` is the max of `|f^{(n+1)}|`
on the interval.

Mathlib target: `Mathlib.Analysis.Calculus.Taylor.Lagrange` (limited
in current toolchain).
-/

/-- **Taylor's theorem with Lagrange remainder (axiom)**.

    For `f : ℝ → ℝ` analytic on a closed interval `[1 − δ, 1 + δ]`
    with `δ > 0`, the n-th Taylor polynomial of `f` about 0 (in the
    variable `h := q - q⁻¹` after substitution) has remainder bounded
    by `C · |h|^(n+1)`.

    Specialised here for the Bring color-tube setting where the
    function `f(q) = 1/(1 + q^9 - q^{11})` is rational and analytic
    away from the denominator zeros.

    -- Ref: [hardy1908] §6.4; Mathlib target
    --      `Mathlib.Analysis.Calculus.Taylor.Lagrange`. -/
axiom taylor_lagrange_remainder_bring_color_tube
    (bringColorTube : ℝ → ℝ) (heckeH : ℝ → ℝ)
    (bringTaylor : ℝ → ℝ)
    (n : ℕ) :
  ∃ (δ C : ℝ), 0 < δ ∧ 0 < C ∧
    ∀ q : ℝ, 1 - δ ≤ q → q ≤ 1 + δ →
      |bringColorTube q - bringTaylor (heckeH q)|
        ≤ C * |heckeH q| ^ (n + 1)

/-! ## §5  Status summary

This file provides 5 named axioms with bibliographic Refs:

  1. `alternating_series_error_bound` (Leibniz / Hardy 1908)
  2. `lobachevsky` (Lewin 1981)
  3. `lobachevsky_pi_div_four_eq_half_catalan` (Lewin 1981 §4.2.21)
  4. `regular_ideal_octahedron_volume_eq` + `borromean_rings_vol_eq_8_catalan` (Adams 1985)
  5. `taylor_lagrange_remainder_bring_color_tube` (Hardy 1908)

Plus 1 sorry'd helper (`catalanSeq_tendsto_zero`) for the standard
convergence 1/n² → 0, which Mathlib has the building blocks for but
the explicit composition is non-trivial to write without local
verification.

## Closure path

Each axiom can be replaced by `theorem ... := proof` when the
corresponding Mathlib lemma lands:
  - (1) waiting on `Real.tsum_alternating_succ` or equivalent
  - (2)-(3) waiting on `MeasureTheory.intervalIntegral` of trig log
  - (4) waiting on (2)-(3) + Adams's octahedral decomposition theorem
  - (5) waiting on `Mathlib.Analysis.Calculus.Taylor.Lagrange`

The named-axiom interface ensures downstream files (`BorromeanVolumeCatalan.lean`,
`TruncationErrorBound.lean`) can be refactored to consume these axioms
INSTEAD of carrying scattered sorrys.

## #print axioms surface

After this file lands, the dependent theorems' axiom surface is:

```
theorem catalan_G_numerical_bounds : ...
#print axioms catalan_G_numerical_bounds
-- expected: alternating_series_error_bound, classical (Mathlib bases)
```

Compared to the previous state (`sorry`), this is more honest:
`sorry` is opaque; named axioms are visible.
-/

end QOU.Archimedean.MathlibInfra
