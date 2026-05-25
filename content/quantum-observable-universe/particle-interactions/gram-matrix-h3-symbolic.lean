/-!
# QOU.Interactions.GramMatrixH3Symbolic

**Symbolic categorical instance of `HasH3GramMatrix ℝ q`** for the
H_3(q) Hoefsmit-seminormal Gram matrix on the 6-element NF basis.

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
- ⏳ **det_ne_zero** — STATED, proof DEFERRED to Phase 1b-2 (the
  determinant is a rational function in `u` that VANISHES at `u = 1`
  (classical limit `q = 1`); for `q > 0, q ≠ 1`, det ≠ 0. The
  formal proof requires computing the determinant symbolically and
  factoring out the (q−1) zero — substantial but routine sympy/Lean
  work, scoped as the next follow-up.) Numerical witness:
  det(G(q_0)) ≈ −0.189205253071 at q_0 ≈ 1.110.

Ref: [manuscript] def:universal-ilp-algorithm
Ref: [manuscript] prop:frobenius-gram-matrix
Ref: [manuscript] docs/audits/2026-05-25-option-e-crystal-weight-delta-lambda.md
Ref: [halverson_ram_1998] Hoefsmit seminormal Gram on H_3(q)
Ref: sympy-computed via `tools/compute_symbolic_gram.py` (PR #1256)
Ref: numerical regression guard: `gram-matrix-dual.witness.json`
-/

import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.LinearAlgebra.Matrix.Determinant.Basic
import Mathlib.LinearAlgebra.Matrix.Symmetric
import Mathlib.Tactic
import Mathlib.Analysis.SpecialFunctions.Pow.NNReal

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
    when `u > 0` and `u ≠ 1` (equivalently `q > 0, q ≠ 1`).

    **Proof strategy** (not yet executed in Lean):
    1. Compute `det (gramMatrix u)` symbolically — a rational function
       in `u` (the determinant of the 6×6 matrix of Laurent polynomials).
    2. Show: numerator of `det` is a polynomial `p(u)` with `p(1) = 0`
       (rank drop at classical limit) but `p(u) ≠ 0` for generic `u`.
    3. Specifically, factor `p(u) = (u−1) · q(u)` where `q(u)` is
       non-zero on `(0, ∞) \ {1}`.

    **Numerical evidence** (sympy + Mathlib's `Matrix.det`):
    - `det(gramMatrix 1) = 0`     (classical limit, expected rank-drop)
    - `det(gramMatrix u_0) ≈ −0.189` at `u_0 = √q_0`, `q_0 ≈ 1.110`
    - `rank(gramMatrix u_0) = 6` (full rank at substrate)

    The `sorry` is conjectural-conditional per CLAUDE.md §3b-cond;
    discharging it requires the symbolic determinant factorisation
    (substantial but routine — scoped as the Phase 1b-2 follow-up). -/
theorem gramMatrix_det_ne_zero (u : ℝ) (hu_pos : 0 < u) (hu_ne_one : u ≠ 1) :
    (gramMatrix u).det ≠ 0 := by
  -- See proof strategy in the docstring.
  -- Numerical check (witness): det at u = √1.110 ≈ -0.189 ≠ 0.
  sorry

end QOU.Interactions.GramMatrixH3Symbolic

/-! ## Integration with HasH3GramMatrix typeclass

To produce a concrete `instance : HasH3GramMatrix ℝ q` for `q > 0, q ≠ 1`,
use `u = Real.sqrt q` and instantiate the typeclass with `gramMatrix u`,
discharging the three axioms via the theorems above. The instance form is:

```lean
noncomputable instance gramInstanceAtPositiveQ (q : ℝ) (hq_pos : 0 < q) (hq_ne_one : q ≠ 1) :
    HasH3GramMatrix ℝ q where
  entries := QOU.Interactions.GramMatrixH3Symbolic.gramMatrix (Real.sqrt q)
  is_symm := gramMatrix_isSymm _
  diag_top_one := gramMatrix_top_left _
  det_ne_zero := gramMatrix_det_ne_zero _
                   (Real.sqrt_pos.mpr hq_pos)
                   (by intro h; apply hq_ne_one; rw [← h]; exact (Real.sq_sqrt hq_pos.le).symm)
```

This is encoded in [`universal-ilp-algorithm.lean`](universal-ilp-algorithm.lean)
Phase 1b-2 follow-up (after `gramMatrix_det_ne_zero` sorry is discharged). -/
