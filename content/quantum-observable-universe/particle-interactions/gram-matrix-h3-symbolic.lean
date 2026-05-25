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

/-- **THEOREM (DEFERRED — Phase 1b-2).** The Gram matrix is invertible
    when `u > 1` (equivalently `q > 1`).

    **Why `u > 1` rather than `u ≠ 1`** (correctness fix, 2026-05-25):
    sympy factorization of det numerator yields

      ```
      det(G(u)) = -(u-1)(u+1)(u³+u-1)⁵(u³+u²+1)⁵·p(u)·r(u) / (u¹⁰(u²+1)¹²)
        p(u) = u⁶-u⁵+u⁴-u³+2u²-u+1                 (no real roots)
        r(u) = u⁶+u⁵+2u⁴+u³+u²+u+1                 (no positive roots)
      ```

    revealing a SECOND positive real root at `u ≈ 0.6823278` (the
    real root of `u³+u-1 = 0`) — the older hypothesis `u ≠ 1` was
    insufficient. The framework substrate has `q_0 ≈ 1.110 > 1`,
    so `u_0 > 1` is the natural domain.

    **Proof strategy** (factor-by-factor positivity for `u > 1`):
    - `u - 1 > 0`                  by `u > 1`
    - `u + 1 > 0`                  by `u > 0`
    - `u³ + u - 1 > 1`             by `u > 1` (so `u³ > 1, u > 1`)
    - `u³ + u² + 1 > 0`            by `u > 0` (positive monomials)
    - `p(u) > 0`                   unconditionally on ℝ (no real roots;
                                    numerical minimum on `[0, ∞)` ≈ 0.86)
    - `r(u) > 0` for `u > 0`       (all-positive coefficient polynomial)
    - denominator `u¹⁰(u²+1)¹² > 0` for `u > 0`

    Therefore `det(G(u)) = -(strictly positive) ≠ 0` for `u > 1`.

    **Numerical evidence** (sympy + Mathlib's `Matrix.det`):
    - `det(gramMatrix 1) = 0`                    (classical limit)
    - `det(gramMatrix 0.6823278) = 0`            (newly-found root)
    - `det(gramMatrix u_0) ≈ −0.189` at `u_0 ≈ 1.054`
    - `rank(gramMatrix u_0) = 6`                 (full rank at substrate)

    The `sorry` is conjectural-conditional per CLAUDE.md §3b-cond;
    discharging it requires lifting the symbolic factorisation into
    Lean. Witness sidecar:
    `folio-assistant/computations/gram-h3-det-factorization.witness.json`. -/
theorem gramMatrix_det_ne_zero (u : ℝ) (hu_gt_one : 1 < u) :
    (gramMatrix u).det ≠ 0 := by
  -- See proof strategy in the docstring. The full Lean proof requires
  -- expanding Matrix.det of the 6×6 rational-function matrix and showing
  -- it equals the factorization above — substantial Mathlib symbolic
  -- determinant work. Numerical witness:
  -- `gram-h3-det-factorization.witness.json` asserts the factorization
  -- and the two-positive-real-roots fact (`u=1` and `u≈0.6823`).
  sorry

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
