/-!
# QOU.Interactions.GramMatrixH3Symbolic

**Symbolic categorical Gram matrix `gramMatrix u`** for the H_3(q)
Hoefsmit-seminormal basis (6-element NF) — direct-use form (no
typeclass indirection per main commit `91cb2671b`'s revert of the
Phase 1a typeclass).

Phase 1b deliverable (PR follow-up to PR #1255 Option E Phase 1a).

## What this file does

Replaces the deferred "rational-encode 36 decimal entries" plan
with explicit **categorical closed-form** entries (sympy-computed,
verified to 1e-16 against `gram-matrix-dual.witness.json` at q_0).

Each of the 21 upper-triangle entries is a Laurent polynomial in
`u = √q`, where `q > 0` (substrate hypothesis). The entries with
ONLY even powers of `u` are equivalent to rational functions in `q`;
the entries with ODD powers carry an explicit `√q` factor.

## NF basis (6 elements)

```
  b_0 = 1            (empty word)
  b_1 = σ_0
  b_2 = σ_1
  b_3 = σ_0σ_1
  b_4 = σ_1σ_0
  b_5 = σ_0σ_1σ_0    (canonical of σ_0σ_1σ_0 = σ_1σ_0σ_1)
```

## Markov trace TR_M

Per `tools/pyhecke/python/pyhecke/gram.py:60`:
  TR_M = [1, z, z, z², z², h·z² + z]
where z = √q/(q+1) and h = q - q⁻¹.

## Symbolic Gram (upper triangle, in u = √q)

```
  G[0,0] = 1
  G[0,1] = G[0,2] = u/(u²+1) = √q/(q+1)
  G[0,3] = G[0,4] = u²/(u²+1)² = q/(q+1)²
  G[0,5] = (u² + u - 1)/(u²+1)
  G[1,1] = G[2,2] = (u² + u - 1)/u
  G[1,2] = u²/(u²+1)² = q/(q+1)²
  G[1,3] = G[1,4] = G[2,3] = G[2,4] = (u² + u - 1)/(u²+1)
  G[1,5] = G[2,5] = G[3,3] = G[4,4] = (u⁴ + u - 1)(u⁴ + u³ - 1)/[u²(u²+1)²]
  G[3,4] = ((u² + u - 1)/u)² = G[1,1]²
  G[3,5] = G[4,5] = (u¹⁰ + u⁹ − u⁸ − u⁵ + u² + u − 1)/[u⁴(u²+1)]
  G[5,5] = (u¹² + u¹¹ − 2u¹⁰ − u⁹ + 2u⁸ + u⁷ − u⁶ − u⁵ + 2u⁴ + u³ − 2u² − u + 1)/u⁶
```

## Phase 1b status

- ✅ **is_symm** — proved (sympy-verified all 15 G[i,j]−G[j,i] = 0)
- ✅ **diag_top_one** — proved (G[0,0] = 1 by definition)
- ⏳ **det_ne_zero** — STATED with **corrected hypothesis `u > 1`**;
  proof of the symbolic-factorization step deferred to Phase 1b-2.

  **Correctness finding (2026-05-25, this branch):** the
  determinant has TWO positive real roots, not one:
    `u = 1`                         (classical limit; expected)
    `u ≈ 0.6823278038`              (root of `u³ + u − 1 = 0`)
  Equivalently `q ≈ 0.4656` (root of `q³ + 2q² + q − 1 = 0`).
  The original hypothesis `0 < u ∧ u ≠ 1` was therefore too weak.
  Strengthened to `u > 1` here — covers the framework substrate
  (q_0 ≈ 1.110 ⟹ u_0 ≈ 1.054 > 1) and makes the factorization
  positivity argument tractable in Lean. See
  `docs/audits/2026-05-25-gram-h3-det-second-root-correctness-finding.md`.

  Numerical witness: `det(G(q_0)) ≈ −0.189205253071` at q_0 ≈ 1.110.
  Symbolic factorization witness:
  `folio-assistant/computations/gram-h3-det-factorization.witness.json`
  (emits the explicit 6-factor product).

Ref: [manuscript] def:universal-ilp-algorithm
Ref: [manuscript] prop:frobenius-gram-matrix
Ref: [manuscript] docs/audits/2026-05-25-option-e-crystal-weight-delta-lambda.md
Ref: [halverson_ram_1998] Hoefsmit seminormal Gram on H_3(q)
Ref: sympy regression guard `folio-assistant/computations/gram_h3_symbolic_regression.py`
     (transcribes the same closed-form entries; emits witness asserting
     match-to-pyhecke and symmetry at 50 dps)
Ref: numerical pyhecke source: `gram-matrix-dual.witness.json`
-/

import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.LinearAlgebra.Matrix.Determinant.Basic
import Mathlib.LinearAlgebra.Matrix.Symmetric
import Mathlib.Tactic

namespace QOU.Interactions.GramMatrixH3Symbolic

open Real

/-- The 21 upper-triangle Gram entries on H_3(q) NF basis, in terms
    of `u = √q` (so `q = u²` is the Hecke parameter). The entries are
    Laurent polynomials in `u` (cleanly factored). -/
noncomputable def gramEntry (u : ℝ) : Fin 6 → Fin 6 → ℝ
  | 0, 0 => 1
  | 0, 1 => u / (u^2 + 1)
  | 0, 2 => u / (u^2 + 1)
  | 0, 3 => u^2 / (u^2 + 1)^2
  | 0, 4 => u^2 / (u^2 + 1)^2
  | 0, 5 => (u^2 + u - 1) / (u^2 + 1)
  | 1, 0 => u / (u^2 + 1)
  | 1, 1 => (u^2 + u - 1) / u
  | 1, 2 => u^2 / (u^2 + 1)^2
  | 1, 3 => (u^2 + u - 1) / (u^2 + 1)
  | 1, 4 => (u^2 + u - 1) / (u^2 + 1)
  | 1, 5 => (u^4 + u - 1) * (u^4 + u^3 - 1) / (u^2 * (u^2 + 1)^2)
  | 2, 0 => u / (u^2 + 1)
  | 2, 1 => u^2 / (u^2 + 1)^2
  | 2, 2 => (u^2 + u - 1) / u
  | 2, 3 => (u^2 + u - 1) / (u^2 + 1)
  | 2, 4 => (u^2 + u - 1) / (u^2 + 1)
  | 2, 5 => (u^4 + u - 1) * (u^4 + u^3 - 1) / (u^2 * (u^2 + 1)^2)
  | 3, 0 => u^2 / (u^2 + 1)^2
  | 3, 1 => (u^2 + u - 1) / (u^2 + 1)
  | 3, 2 => (u^2 + u - 1) / (u^2 + 1)
  | 3, 3 => (u^4 + u - 1) * (u^4 + u^3 - 1) / (u^2 * (u^2 + 1)^2)
  | 3, 4 => (u^2 + u - 1)^2 / u^2
  | 3, 5 => (u^10 + u^9 - u^8 - u^5 + u^2 + u - 1) / (u^4 * (u^2 + 1))
  | 4, 0 => u^2 / (u^2 + 1)^2
  | 4, 1 => (u^2 + u - 1) / (u^2 + 1)
  | 4, 2 => (u^2 + u - 1) / (u^2 + 1)
  | 4, 3 => (u^2 + u - 1)^2 / u^2
  | 4, 4 => (u^4 + u - 1) * (u^4 + u^3 - 1) / (u^2 * (u^2 + 1)^2)
  | 4, 5 => (u^10 + u^9 - u^8 - u^5 + u^2 + u - 1) / (u^4 * (u^2 + 1))
  | 5, 0 => (u^2 + u - 1) / (u^2 + 1)
  | 5, 1 => (u^4 + u - 1) * (u^4 + u^3 - 1) / (u^2 * (u^2 + 1)^2)
  | 5, 2 => (u^4 + u - 1) * (u^4 + u^3 - 1) / (u^2 * (u^2 + 1)^2)
  | 5, 3 => (u^10 + u^9 - u^8 - u^5 + u^2 + u - 1) / (u^4 * (u^2 + 1))
  | 5, 4 => (u^10 + u^9 - u^8 - u^5 + u^2 + u - 1) / (u^4 * (u^2 + 1))
  | 5, 5 => (u^12 + u^11 - 2*u^10 - u^9 + 2*u^8 + u^7 - u^6 - u^5 +
             2*u^4 + u^3 - 2*u^2 - u + 1) / u^6

/-- The H_3(q) Gram matrix as a Mathlib `Matrix`. -/
noncomputable def gramMatrix (u : ℝ) : Matrix (Fin 6) (Fin 6) ℝ :=
  Matrix.of (gramEntry u)

/-! ## Structural theorems on the symbolic entries -/

/-- **THEOREM.** The Gram matrix is symmetric:
    `G[i,j] = G[j,i]` for all `i, j ∈ Fin 6`.

    Proved by direct case analysis on the 36 pairs; each cell-equality
    is `rfl` after `unfold gramEntry` because we encoded the entries
    explicitly symmetrically. Numerically verified at q_0 to ≤ 1e-16. -/
theorem gramMatrix_isSymm (u : ℝ) : (gramMatrix u).IsSymm := by
  ext i j
  fin_cases i <;> fin_cases j <;> rfl

/-- **THEOREM.** The top-left Gram entry is `1 = tr_M(1)`. -/
theorem gramMatrix_top_left (u : ℝ) : gramMatrix u 0 0 = 1 := by
  unfold gramMatrix gramEntry
  simp [Matrix.of_apply]

/-! ## Positivity scaffolding for the determinant factorization

Six lemmas decomposing each factor of the sympy-verified factorization

  ```
  det(G(u)) = -(u-1)(u+1)(u³+u-1)⁵(u³+u²+1)⁵·p(u)·r(u) / (u¹⁰(u²+1)¹²)
    p(u) = u⁶-u⁵+u⁴-u³+2u²-u+1                 (no real roots)
    r(u) = u⁶+u⁵+2u⁴+u³+u²+u+1                 (no positive roots)
  ```

into individually-provable factor-positivity statements for `u > 1`.
These compose into the full `gramMatrix_det_ne_zero` discharge (modulo
the single remaining sorry, which is the symbolic 6×6 matrix-det
expansion — see below). -/

/-- `u - 1 > 0` for `u > 1`. Immediate from hypothesis. -/
theorem det_factor_u_minus_one_pos {u : ℝ} (hu : 1 < u) : 0 < u - 1 := by
  linarith

/-- `u + 1 > 0` for `u > 1`. From `u > 1 > -1`. -/
theorem det_factor_u_plus_one_pos {u : ℝ} (hu : 1 < u) : 0 < u + 1 := by
  linarith

/-- `u³ + u − 1 > 1` for `u > 1`. Factorisation
    `u³ + u − 2 = (u − 1)·(u² + u + 2)` with both factors positive. -/
theorem det_factor_cubic_one_pos {u : ℝ} (hu : 1 < u) : 1 < u^3 + u - 1 := by
  have h1 : 0 < u - 1 := by linarith
  have h2 : 0 < u^2 + u + 2 := by nlinarith [sq_nonneg u, hu]
  nlinarith [mul_pos h1 h2]

/-- `u³ + u² + 1 > 0` for `u > 0`. Sum of positive monomials. -/
theorem det_factor_cubic_two_pos {u : ℝ} (hu : 0 < u) : 0 < u^3 + u^2 + 1 := by
  have h1 : 0 < u^3 := by positivity
  have h2 : 0 < u^2 := by positivity
  linarith

/-- `p(u) = u⁶ − u⁵ + u⁴ − u³ + 2u² − u + 1 > 0` for all real `u`.
    Sympy confirms p has no real roots (all 6 roots complex with
    nonzero imaginary part); numerical minimum on ℝ ≈ 0.859.

    Sum-of-squares decomposition (verified by expansion):
      p(u) = (u³ − u²/2 − 1/2)²  +  (3/4)·u⁴
           + (3/2)·(u − 1/3)²    +  7/12
    Each piece is non-negative and the constant 7/12 > 0, so p > 0. -/
theorem det_factor_p_pos (u : ℝ) :
    0 < u^6 - u^5 + u^4 - u^3 + 2*u^2 - u + 1 := by
  have h1 : 0 ≤ (u^3 - u^2/2 - 1/2)^2 := sq_nonneg _
  have h2 : 0 ≤ u^4 := by positivity
  have h3 : 0 ≤ (u - 1/3)^2 := sq_nonneg _
  nlinarith [h1, h2, h3]

/-- `r(u) = u⁶ + u⁵ + 2u⁴ + u³ + u² + u + 1 > 0` for `u > 0`.
    All-positive coefficients ⇒ sum of positives for `u > 0`. -/
theorem det_factor_r_pos {u : ℝ} (hu : 0 < u) :
    0 < u^6 + u^5 + 2*u^4 + u^3 + u^2 + u + 1 := by
  have h6 : 0 < u^6 := by positivity
  have h5 : 0 < u^5 := by positivity
  have h4 : 0 < u^4 := by positivity
  have h3 : 0 < u^3 := by positivity
  have h2 : 0 < u^2 := by positivity
  linarith

/-- Denominator `u¹⁰ · (u² + 1)¹² > 0` for `u > 0`. -/
theorem det_denominator_pos {u : ℝ} (hu : 0 < u) :
    0 < u^10 * (u^2 + 1)^12 := by
  have h1 : 0 < u^10 := by positivity
  have h2 : 0 < (u^2 + 1)^12 := by positivity
  exact mul_pos h1 h2

/-- The combined factored expression
    `-(u-1)(u+1)(u³+u-1)⁵(u³+u²+1)⁵·p(u)·r(u) / (u¹⁰(u²+1)¹²)` is
    **strictly negative** for `u > 1`, hence nonzero. This is the
    sympy-verified factorization of `det(gramMatrix u)`. -/
theorem det_factored_form_neg {u : ℝ} (hu : 1 < u) :
    -((u - 1) * (u + 1) * (u^3 + u - 1)^5 * (u^3 + u^2 + 1)^5
      * (u^6 - u^5 + u^4 - u^3 + 2*u^2 - u + 1)
      * (u^6 + u^5 + 2*u^4 + u^3 + u^2 + u + 1))
      / (u^10 * (u^2 + 1)^12) < 0 := by
  have hu_pos : 0 < u := by linarith
  have h_um1 : 0 < u - 1 := det_factor_u_minus_one_pos hu
  have h_up1 : 0 < u + 1 := det_factor_u_plus_one_pos hu
  have h_c1_lt : 1 < u^3 + u - 1 := det_factor_cubic_one_pos hu
  have h_c1 : 0 < u^3 + u - 1 := by linarith
  have h_c2 : 0 < u^3 + u^2 + 1 := det_factor_cubic_two_pos hu_pos
  have h_p : 0 < u^6 - u^5 + u^4 - u^3 + 2*u^2 - u + 1 := det_factor_p_pos u
  have h_r : 0 < u^6 + u^5 + 2*u^4 + u^3 + u^2 + u + 1 := det_factor_r_pos hu_pos
  have h_denom : 0 < u^10 * (u^2 + 1)^12 := det_denominator_pos hu_pos
  have h_c1_5 : 0 < (u^3 + u - 1)^5 := by positivity
  have h_c2_5 : 0 < (u^3 + u^2 + 1)^5 := by positivity
  have h_num : 0 < (u - 1) * (u + 1) * (u^3 + u - 1)^5 * (u^3 + u^2 + 1)^5
                   * (u^6 - u^5 + u^4 - u^3 + 2*u^2 - u + 1)
                   * (u^6 + u^5 + 2*u^4 + u^3 + u^2 + u + 1) := by positivity
  have h_ratio : 0 < ((u - 1) * (u + 1) * (u^3 + u - 1)^5 * (u^3 + u^2 + 1)^5
                       * (u^6 - u^5 + u^4 - u^3 + 2*u^2 - u + 1)
                       * (u^6 + u^5 + 2*u^4 + u^3 + u^2 + u + 1))
                      / (u^10 * (u^2 + 1)^12) := div_pos h_num h_denom
  linarith

/-- **THEOREM** (Phase 1b-2 partial discharge — 2026-05-25):
    `det(gramMatrix u) ≠ 0` for `u > 1`.

    **Proof structure:** The factor-positivity scaffolding above proves
    that the factored form
      `-(u-1)(u+1)(u³+u-1)⁵(u³+u²+1)⁵·p(u)·r(u) / (u¹⁰(u²+1)¹²)`
    is strictly negative for `u > 1`. The remaining gap (single
    `sorry`) is the symbolic identification
      `(gramMatrix u).det = (factored form above)`
    — a 6×6 symbolic Matrix.det expansion verified at machine precision
    via the sympy witness
    `folio-assistant/computations/gram-h3-det-factorization.witness.json`
    but not yet bridged into Mathlib's symbolic determinant machinery.

    The remaining sorry is **bounded**: it's a single algebraic identity
    between two explicit closed-form rational functions, with both sides
    individually computable (sympy independently confirms equality). A
    follow-up Phase 1b-3 will close it via `Matrix.det_succ_column_zero`
    recursion plus `ring` / `field_simp`.

    Numerical witness:
    - `det(gramMatrix 1.054) ≈ −0.189` (substrate-pin value, factored
      form gives same value)
    - `det(gramMatrix 1) = 0` (rank drop, excluded by hypothesis u > 1)
    - `det(gramMatrix 0.6823278) = 0` (second root, also excluded) -/
theorem gramMatrix_det_ne_zero (u : ℝ) (hu_gt_one : 1 < u) :
    (gramMatrix u).det ≠ 0 := by
  -- The factored form is strictly negative for u > 1:
  have h_fact_neg :
      -((u - 1) * (u + 1) * (u^3 + u - 1)^5 * (u^3 + u^2 + 1)^5
        * (u^6 - u^5 + u^4 - u^3 + 2*u^2 - u + 1)
        * (u^6 + u^5 + 2*u^4 + u^3 + u^2 + u + 1))
        / (u^10 * (u^2 + 1)^12) < 0 := det_factored_form_neg hu_gt_one
  -- The symbolic identity (gramMatrix u).det = factored form: deferred
  -- to Phase 1b-3 follow-up (Matrix.det_succ_column_zero × 5 + ring).
  -- Sympy witness confirms this identity at machine precision; see
  -- `gram-h3-det-factorization.witness.json`.
  have h_det_eq_factored :
      (gramMatrix u).det = -((u - 1) * (u + 1) * (u^3 + u - 1)^5
        * (u^3 + u^2 + 1)^5
        * (u^6 - u^5 + u^4 - u^3 + 2*u^2 - u + 1)
        * (u^6 + u^5 + 2*u^4 + u^3 + u^2 + u + 1))
        / (u^10 * (u^2 + 1)^12) := by
    -- Ref: sympy Berkowitz det + factor in
    -- `folio-assistant/computations/gram_h3_det_factorization.py`.
    -- Phase 1b-3 follow-up: bridge sympy factorization into Mathlib
    -- via Matrix.det_succ_column_zero recursion. The identity is
    -- between two explicit closed-form rationals; both sides are
    -- algorithmically computable.
    sorry
  rw [h_det_eq_factored]
  exact ne_of_lt h_fact_neg

end QOU.Interactions.GramMatrixH3Symbolic

/-! ## Direct-use pattern

`HasH3GramMatrix` was reverted from `universal-ilp-algorithm.lean`
(main commit `91cb2671b`, 2026-05-25, "Phase 1a typeclass infrastructure
is superseded by the symbolic Gram entries — the typeclass-driven approach
added an unnecessary layer of indirection when the categorical entries
are directly definable"). Downstream consumers use `gramMatrix u`
directly with the three structural theorems below.

Substrate-domain usage (q > 1, the framework's actual domain):

```lean
example (q : ℝ) (hq_gt_one : 1 < q) :
    ∃ G : Matrix (Fin 6) (Fin 6) ℝ,
      G.IsSymm ∧ G 0 0 = 1 ∧ G.det ≠ 0 := by
  refine ⟨gramMatrix (Real.sqrt q), gramMatrix_isSymm _, gramMatrix_top_left _, ?_⟩
  apply gramMatrix_det_ne_zero
  -- sqrt is strictly monotone on (0, ∞), sqrt 1 = 1
  calc 1 = Real.sqrt 1 := Real.sqrt_one.symm
    _ < Real.sqrt q := Real.sqrt_lt_sqrt zero_le_one hq_gt_one
```

**Hypothesis (2026-05-25):** the original `det_ne_zero` form took
`(hu_pos : 0 < u) (hu_ne_one : u ≠ 1)` — too weak per the
correctness finding above. Strengthened to `1 < u`, which both
implies `u > 0` and discards both determinant roots cleanly. -/
