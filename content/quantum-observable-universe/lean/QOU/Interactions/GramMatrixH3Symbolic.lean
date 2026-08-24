import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.LinearAlgebra.Matrix.Determinant.Basic
import Mathlib.LinearAlgebra.Matrix.NonsingularInverse
import Mathlib.LinearAlgebra.Matrix.PosDef
import Mathlib.LinearAlgebra.Matrix.Symmetric
import Mathlib.Tactic
import QOU.Shared.DetFin


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

## Markov trace TR_M — and WHICH CONVENTION each half of this file is in

  TR_M = [1, z, z, z², z², h·z² + z],   h = q − q⁻¹

with `z` the Markov weight. Everything in this file follows from that one
line, and *which* `z` you put in it decides the answer. Two are in play:

  convention C   z = √q/(q+1)      excised 2026-08-09, re-affirmed 2026-08-15
  convention D   z = q³/(q²+1)     CANONICAL (owner ruling 2026-08-15)

**`gramEntry` / `gramMatrix` and everything proved about them are convention
C.** They are correct — every one of the 21 closed forms below equals the
generic Gram at `z = z_C` exactly — but C is not the canonical frame. The
`gramEntryD` / `gramMatrixD` section further down is the canonical one.

### Why this is not a matter of substituting one `z` for the other

Over `ℚ(q, z)`, with `z` free, the determinant factors as

  det G(q,z) = −(z − q)⁵ (qz + 1)⁵ ((q²+1)z − q³) (q³z + qz + 1) / q⁸

and the third factor is `(q²+1)z − q³`. It vanishes **identically in q**
exactly at `z = q³/(q²+1)` — convention D. So D is not a frame in which this
Gram happens to be singular at the substrate anchor: **D is a root of the H_3
Gram determinant as a polynomial in `z`.** Under D the form has rank 5, a
one-dimensional radical spanned by the three-strand q-antisymmetriser, and a
negative eigenvalue at `q₀` besides.

Consequently `gramMatrix_det_ne_zero` below — the file's headline theorem,
sorry-free and true — is **FALSE in the canonical convention**, and so is the
positive-definiteness reading of it. Both are stated for C and must be cited
as C results. `markovWeightD_root` records the vanishing factor in Lean so
that the scoping is machine-checkable rather than a comment someone can
tidy away; `gramEntryD_zero_one` pins which `z` the D entries were built
from, for the same reason.

Derivation and the six cross-checks (including that this file's own
`gram_det_eq` is reproduced factor for factor from the generic form):
`computations/probes/gram_h3_convention_frame_probe.py`.

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

- ✅ **is_symm** — proved. Holds for EVERY `z`, so it survives the frame
  change; `gramMatrixD_isSymm` is the same statement for D.
- ✅ **diag_top_one** — proved (G[0,0] = tr_M(1) = 1). Also holds for every
  `z`; `gramMatrixD_top_left` is its D counterpart.
- ⚠ **det_ne_zero** — proved, **in convention C only, and false in D.** The
  Phase 1b-2 note below records it as a deferred `sorry`; it was discharged
  (`gramMatrix_det_ne_zero`, sorry-free). What was never in question was the
  proof — what was wrong is the frame. Under the canonical convention the
  determinant is identically zero (`gramMatrixD_det_eq_zero`), so this is not
  a result awaiting strengthening: it is a C-frame result awaiting
  replacement. See the banner above.

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
  `computations/gram-h3-det-factorization.witness.json`
  (emits the explicit 6-factor product).

Ref: [manuscript] def:universal-ilp-algorithm
Ref: [manuscript] prop:frobenius-gram-matrix
Ref: [manuscript] docs/audits/2026-05-25-option-e-crystal-weight-delta-lambda.md
Ref: [halverson_ram_1998] Hoefsmit seminormal Gram on H_3(q)
Ref: sympy regression guard `computations/gram_h3_symbolic_regression.py`
     (transcribes the same closed-form entries; emits witness asserting
     match-to-pyhecke and symmetry at 50 dps)
Ref: numerical pyhecke source: `gram-matrix-dual.witness.json`
-/

namespace QOU.Interactions.GramMatrixH3Symbolic

open Real

/-- The 21 upper-triangle Gram entries on the H_3(q) NF basis **in
    convention C** (`z = √q/(q+1)`, excised 2026-08-09 / re-affirmed
    2026-08-15), in terms of `u = √q` (so `q = u²` is the Hecke parameter).
    The entries are Laurent polynomials in `u` (cleanly factored).

    The `u = √q` parametrisation is forced by C and by nothing else: C's `z`
    is irrational in `q`, so odd powers of `u` appear. The canonical
    `gramEntryD` below is rational in `q` and needs no square root — see
    the file banner. -/
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

/-! **THEOREM (DEFERRED — Phase 1b-2).** The Gram matrix is invertible
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

    -- Ref: [manuscript]
    The `sorry` is conjectural-conditional per AGENTS.md §3b-cond;
    discharging it requires lifting the symbolic factorisation into
    Lean. Witness sidecar:
    `computations/gram-h3-det-factorization.witness.json`. -/
/-! ## Symbolic factorization of det(gramMatrix u) — Phase 1b-2

Per `gram-h3-det-factorization.witness.json` (sympy at 50-dps), the
6×6 Hoefsmit Gram determinant factors as:

```
det(G(u)) = − [ (u−1)·(u+1)·(u³+u−1)⁵·(u³+u²+1)⁵·p(u)·r(u) ] / [ u¹⁰·(u²+1)¹² ]
```
where
- `p(u) = u⁶ − u⁵ + u⁴ − u³ + 2u² − u + 1`
- `r(u) = u⁶ + u⁵ + 2u⁴ + u³ + u² + u + 1`

The numerator has degree 44 in u; the only positive real roots are
`u = 1` (classical limit) and `u ≈ 0.6823` (root of u³+u−1). For
the framework's substrate domain `u > 1`, all six factors are
strictly positive, so the determinant is non-zero.

This section proves the six positivity lemmas + the main theorem
conditional on the symbolic factorization (which is recorded in the
witness as a sympy-verified identity). -/

/-- Factor 1: u − 1. -/
noncomputable def detFactor1 (u : ℝ) : ℝ := u - 1

/-- Factor 2: u + 1. -/
noncomputable def detFactor2 (u : ℝ) : ℝ := u + 1

/-- Factor 3: u³ + u − 1. -/
noncomputable def detFactor3 (u : ℝ) : ℝ := u^3 + u - 1

/-- Factor 4: u³ + u² + 1. -/
noncomputable def detFactor4 (u : ℝ) : ℝ := u^3 + u^2 + 1

/-- Factor 5: p(u) = u⁶ − u⁵ + u⁴ − u³ + 2u² − u + 1 (no real roots). -/
noncomputable def detFactor5 (u : ℝ) : ℝ :=
  u^6 - u^5 + u^4 - u^3 + 2*u^2 - u + 1

/-- Factor 6: r(u) = u⁶ + u⁵ + 2u⁴ + u³ + u² + u + 1
    (all-positive coefficients). -/
noncomputable def detFactor6 (u : ℝ) : ℝ :=
  u^6 + u^5 + 2*u^4 + u^3 + u^2 + u + 1

/-- **POSITIVITY LEMMA 1.** `u − 1 > 0` for `u > 1`. -/
theorem detFactor1_pos (u : ℝ) (hu : 1 < u) : 0 < detFactor1 u := by
  unfold detFactor1; linarith

/-- **POSITIVITY LEMMA 2.** `u + 1 > 0` for `u > 1` (trivially `> 2`). -/
theorem detFactor2_pos (u : ℝ) (hu : 1 < u) : 0 < detFactor2 u := by
  unfold detFactor2; linarith

/-- **POSITIVITY LEMMA 3.** `u³ + u − 1 > 0` for `u > 1`. At `u = 1`:
    `1 + 1 − 1 = 1 > 0`; for `u > 1`, `u³ > 0` and `u − 1 > 0`. -/
theorem detFactor3_pos (u : ℝ) (hu : 1 < u) : 0 < detFactor3 u := by
  unfold detFactor3
  -- u^3 + u - 1 = u^3 + (u - 1), both positive for u > 1
  have h_eq : u^3 + u - 1 = u^3 + (u - 1) := by ring
  rw [h_eq]
  have h_pos : 0 < u := by linarith
  have h_u3 : 0 < u^3 := by positivity
  have h_u1 : 0 < u - 1 := by linarith
  linarith

/-- **POSITIVITY LEMMA 4.** `u³ + u² + 1 > 0` for `u > 1`
    (every term `> 0` when `u > 0`; trivially `> 3` when `u > 1`). -/
theorem detFactor4_pos (u : ℝ) (hu : 1 < u) : 0 < detFactor4 u := by
  unfold detFactor4
  have h_pos : 0 < u := by linarith
  have h1 : 0 < u^3 := by positivity
  have h2 : 0 < u^2 := by positivity
  linarith

/-- **POSITIVITY LEMMA 5.** `p(u) = u⁶ − u⁵ + u⁴ − u³ + 2u² − u + 1 > 0`
    for `u > 1`. Strategy: group as `(u−1)(u⁵ + u³) + (2u² − u + 1)` where
  -- Witness: computations/none
    the first part is positive (product of positives for `u > 1`) and the
    second has discriminant `1 − 8 = −7 < 0`, so is always positive. -/
theorem detFactor5_pos (u : ℝ) (hu : 1 < u) : 0 < detFactor5 u := by
  unfold detFactor5
  have h_pos_u5_u3 : 0 < u^5 + u^3 := by positivity
  have h_u_minus_1 : 0 < u - 1 := by linarith
  -- 2u^2 - u + 1 = 2(u - 1/4)^2 + 7/8 > 0 (discriminant = 1 - 8 = -7 < 0)
  have h_quadratic : 0 < 2*u^2 - u + 1 := by
    have h_quad_eq : 2*u^2 - u + 1 = 2 * (u - 1/4)^2 + 7/8 := by ring
    rw [h_quad_eq]
    have h_sq : 0 ≤ (u - 1/4)^2 := sq_nonneg (u - 1/4)
    linarith
  -- p(u) = (u - 1)·(u⁵ + u³) + (2u² − u + 1)
  have h_eq : u^6 - u^5 + u^4 - u^3 + 2*u^2 - u + 1 =
      (u - 1) * (u^5 + u^3) + (2*u^2 - u + 1) := by ring
  rw [h_eq]
  have h_prod : 0 < (u - 1) * (u^5 + u^3) := mul_pos h_u_minus_1 h_pos_u5_u3
  linarith

/-- **POSITIVITY LEMMA 6.** `r(u) = u⁶ + u⁵ + 2u⁴ + u³ + u² + u + 1 > 0`
    for `u > 0` (all coefficients positive). Trivially `> 7` for `u > 1`. -/
theorem detFactor6_pos (u : ℝ) (hu : 1 < u) : 0 < detFactor6 u := by
  unfold detFactor6
  have h1 : 0 < u := by linarith
  have h2 : 0 < u^6 := by positivity
  have h3 : 0 < u^5 := by positivity
  have h4 : 0 < u^4 := by positivity
  have h5 : 0 < u^3 := by positivity
  have h6 : 0 < u^2 := by positivity
  linarith

/-- **POSITIVITY LEMMA (denominator).** `u^10 · (u² + 1)^12 > 0` for `u > 0`. -/
theorem gram_det_denominator_pos (u : ℝ) (hu_pos : 0 < u) :
    0 < u^10 * (u^2 + 1)^12 := by
  have h_u10 : 0 < u^10 := by positivity
  have h_pow : 0 < (u^2 + 1)^12 := by positivity
  exact mul_pos h_u10 h_pow

/-- **THEOREM (det ≠ 0 conditional on symbolic factorization).** If the
    symbolic Matrix.det of `gramMatrix u` equals the witness's
    factorization, then it is non-zero for `u > 1`.

    The factorization equality itself (`gramMatrix u . det = -(numerator)/(denominator)`)
    is recorded in `gram-h3-det-factorization.witness.json` as a sympy-
    verified identity; the full Lean expansion of `Matrix.det` for the
    6×6 rational-function matrix is multi-thousand-line work scoped as
    a separate follow-up. The conditional discharge below is the
    substantive content: the 6 positivity lemmas + denominator
    positivity give a complete categorical argument modulo the
    sympy-witnessed factorization identity. -/
theorem gramMatrix_det_ne_zero_conditional
    (u : ℝ) (hu_gt_one : 1 < u)
    (factorization_holds :
      (gramMatrix u).det =
        -(detFactor1 u * detFactor2 u
          * (detFactor3 u)^5 * (detFactor4 u)^5
          * detFactor5 u * detFactor6 u)
        / (u^10 * (u^2 + 1)^12)) :
    (gramMatrix u).det ≠ 0 := by
  rw [factorization_holds]
  have h_pos : 0 < u := by linarith
  have h1 := detFactor1_pos u hu_gt_one
  have h2 := detFactor2_pos u hu_gt_one
  have h3 := detFactor3_pos u hu_gt_one
  have h4 := detFactor4_pos u hu_gt_one
  have h5 := detFactor5_pos u hu_gt_one
  have h6 := detFactor6_pos u hu_gt_one
  have h3_5 : 0 < (detFactor3 u)^5 := by positivity
  have h4_5 : 0 < (detFactor4 u)^5 := by positivity
  have h_num_pos :
      0 < detFactor1 u * detFactor2 u
          * (detFactor3 u)^5 * (detFactor4 u)^5
          * detFactor5 u * detFactor6 u := by
    positivity
  have h_denom_pos := gram_det_denominator_pos u h_pos
  have h_quot_neg :
      -(detFactor1 u * detFactor2 u
          * (detFactor3 u)^5 * (detFactor4 u)^5
          * detFactor5 u * detFactor6 u)
        / (u^10 * (u^2 + 1)^12) < 0 := by
    rw [neg_div]
    exact neg_lt_zero.mpr (div_pos h_num_pos h_denom_pos)
  exact ne_of_lt h_quot_neg

/-- Row-scale factors `L_i`; `diagonal L * gram` clears all denominators
    (turning each rational Gram entry into a polynomial). -/
noncomputable def Lval (u : ℝ) : Fin 6 → ℝ
  | 0 => (u^2+1)^2
  | 1 => u^2*(u^2+1)^2
  | 2 => u^2*(u^2+1)^2
  | 3 => u^4*(u^2+1)^2
  | 4 => u^4*(u^2+1)^2
  | 5 => u^6*(u^2+1)^2

/-- Polynomial (denominator-cleared) Gram matrix `= diagonal (Lval u) * gramMatrix u`.
    Verified entrywise in `gram_scale_rel`. -/
noncomputable def gramScaledEntry (u : ℝ) : Fin 6 → Fin 6 → ℝ
  | 0, 0 => u^4+2*u^2+1
  | 0, 1 => u^3+u
  | 0, 2 => u^3+u
  | 0, 3 => u^2
  | 0, 4 => u^2
  | 0, 5 => u^4+u^3+u-1
  | 1, 0 => u^5+u^3
  | 1, 1 => u^7+u^6+u^5+2*u^4-u^3+u^2-u
  | 1, 2 => u^4
  | 1, 3 => u^6+u^5+u^3-u^2
  | 1, 4 => u^6+u^5+u^3-u^2
  | 1, 5 => u^8+u^7+u^5-u^4-u^3-u+1
  | 2, 0 => u^5+u^3
  | 2, 1 => u^4
  | 2, 2 => u^7+u^6+u^5+2*u^4-u^3+u^2-u
  | 2, 3 => u^6+u^5+u^3-u^2
  | 2, 4 => u^6+u^5+u^3-u^2
  | 2, 5 => u^8+u^7+u^5-u^4-u^3-u+1
  | 3, 0 => u^6
  | 3, 1 => u^8+u^7+u^5-u^4
  | 3, 2 => u^8+u^7+u^5-u^4
  | 3, 3 => u^10+u^9+u^7-u^6-u^5-u^3+u^2
  | 3, 4 => u^10+2*u^9+u^8+2*u^7-2*u^5+u^4-2*u^3+u^2
  | 3, 5 => u^12+u^11+u^9-u^8-u^7-u^5+u^4+u^3+u-1
  | 4, 0 => u^6
  | 4, 1 => u^8+u^7+u^5-u^4
  | 4, 2 => u^8+u^7+u^5-u^4
  | 4, 3 => u^10+2*u^9+u^8+2*u^7-2*u^5+u^4-2*u^3+u^2
  | 4, 4 => u^10+u^9+u^7-u^6-u^5-u^3+u^2
  | 4, 5 => u^12+u^11+u^9-u^8-u^7-u^5+u^4+u^3+u-1
  | 5, 0 => u^10+u^9+u^7-u^6
  | 5, 1 => u^12+u^11+u^9-u^8-u^7-u^5+u^4
  | 5, 2 => u^12+u^11+u^9-u^8-u^7-u^5+u^4
  | 5, 3 => u^14+u^13+u^11-u^10-u^9-u^7+u^6+u^5+u^3-u^2
  | 5, 4 => u^14+u^13+u^11-u^10-u^9-u^7+u^6+u^5+u^3-u^2
  | 5, 5 => u^16+u^15+u^13-u^12+u^10+2*u^8+u^6-u^4-u^3-u+1

noncomputable def gramScaled (u : ℝ) : Matrix (Fin 6) (Fin 6) ℝ :=
  Matrix.of (gramScaledEntry u)

set_option maxHeartbeats 40000000 in
set_option maxRecDepth 8000 in
/-- Determinant of the polynomial scaled Gram matrix, by direct
    `det_fin_six` expansion + `ring` (no division — all entries polynomial). -/
theorem gramScaled_det (u : ℝ) :
    (gramScaled u).det =
      -((u-1)*(u+1)*(u^3+u-1)^5*(u^3+u^2+1)^5*(u^6-u^5+u^4-u^3+2*u^2-u+1)*(u^6+u^5+2*u^4+u^3+u^2+u+1))*u^8 := by
  rw [gramScaled, Matrix.det_fin_six]
  simp only [Matrix.of_apply, gramScaledEntry]
  ring

set_option maxHeartbeats 40000000 in
set_option maxRecDepth 8000 in
/-- The scaled matrix equals `diagonal (Lval u) * gramMatrix u` (entrywise,
    after clearing denominators; needs `u ≠ 0`). -/
theorem gram_scale_rel (u : ℝ) (hu : u ≠ 0) :
    Matrix.diagonal (Lval u) * gramMatrix u = gramScaled u := by
  have h1 : (u^2+1) ≠ 0 := by positivity
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [Matrix.mul_apply, Matrix.diagonal, gramMatrix,
      gramScaled, gramScaledEntry, gramEntry, Lval] <;>
    field_simp <;> ring

set_option maxHeartbeats 40000000 in
set_option maxRecDepth 8000 in
/-- Symbolic factorization of `det(gramMatrix u)` for `u ≠ 0`, obtained from
    `gramScaled_det` by dividing out the row scales `∏ Lval = u¹⁸(u²+1)¹²`. -/
theorem gram_det_eq (u : ℝ) (hu : u ≠ 0) :
    (gramMatrix u).det =
      -((u-1)*(u+1)*(u^3+u-1)^5*(u^3+u^2+1)^5*(u^6-u^5+u^4-u^3+2*u^2-u+1)*(u^6+u^5+2*u^4+u^3+u^2+u+1))
      / (u^10 * (u^2+1)^12) := by
  have h1 : (u^2+1) ≠ 0 := by positivity
  have hLd : (∏ i, Lval u i) = u^18*(u^2+1)^12 := by
    rw [Fin.prod_univ_six]; simp only [Lval]; ring
  have key : u^18*(u^2+1)^12 * (gramMatrix u).det =
      -((u-1)*(u+1)*(u^3+u-1)^5*(u^3+u^2+1)^5*(u^6-u^5+u^4-u^3+2*u^2-u+1)*(u^6+u^5+2*u^4+u^3+u^2+u+1))*u^8 := by
    rw [← hLd, ← Matrix.det_diagonal, ← Matrix.det_mul, gram_scale_rel u hu, gramScaled_det]
  rw [eq_div_iff (by positivity : (u^10*(u^2+1)^12 : ℝ) ≠ 0)]
  have hu10 : (u:ℝ)^10 ≠ 0 := pow_ne_zero 10 hu
  field_simp at key ⊢
  linear_combination key

set_option maxHeartbeats 40000000 in
set_option maxRecDepth 8000 in
/-- **THEOREM (PROVED).** The symbolic `Matrix.det` of `gramMatrix u` equals
    the witness-derived factorization, for every real `u`. The 6×6 determinant
    is expanded via `det_fin_six` on the denominator-cleared polynomial matrix
    `gramScaled` (`gramScaled_det`), related back to `gramMatrix` by the row
    scaling `gram_scale_rel` and `∏ Lval = u¹⁸(u²+1)¹²`. The `u = 0` boundary
    (where both sides are `0` under Lean's `x / 0 = 0`) is discharged directly. -/
theorem gramMatrix_det_eq_factorization (u : ℝ) :
    (gramMatrix u).det =
      -(detFactor1 u * detFactor2 u
        * (detFactor3 u)^5 * (detFactor4 u)^5
        * detFactor5 u * detFactor6 u)
      / (u^10 * (u^2 + 1)^12) := by
  rw [detFactor1, detFactor2, detFactor3, detFactor4, detFactor5, detFactor6]
  rcases eq_or_ne u 0 with rfl | hu
  · rw [gramMatrix, Matrix.det_fin_six]
    norm_num [Matrix.of_apply, gramEntry]
  · exact gram_det_eq u hu

/-- **THEOREM (convention C only — FALSE in the canonical convention D).**
    Combines the conditional discharge (above) with the symbolic
    factorization theorem to give `u > 1 ⟹ det(G_C(u)) ≠ 0`.

    Status: FULLY PROVED (sorry-free) — and scoped. The proof is sound; the
    *frame* is not canonical. Convention D is a root of the determinant
    factor `(q²+1)z − q³`, so the D-frame Gram is singular for every `q`
    (`gramMatrixD_det_eq_zero`). Cite this as a C-frame result, never as
    "the H_3 Gram is non-singular". -/
theorem gramMatrix_det_ne_zero (u : ℝ) (hu_gt_one : 1 < u) :
    (gramMatrix u).det ≠ 0 :=
  gramMatrix_det_ne_zero_conditional u hu_gt_one
    (gramMatrix_det_eq_factorization u)

/-! ## Convention D — the canonical frame

Everything above is convention C. This section is the canonical one
(`z = q³/(q²+1)`, owner ruling 2026-08-15).

Three things change and one does not:

* **The entries become rational in `q`.** No `√q`, hence no `Real.sqrt`, so
  nothing here needs `ℝ` for its *statement* — only the `positivity` calls
  on `q² + 1` use the order, and those hold in any `LinearOrderedField`.
  Per AGENTS.md §7c that is a strictly better base-ring position than the
  C section, which cannot escape `ℝ`.
* **The determinant is identically zero**, not merely small: `z_D` is a root
  of the determinant factor `(q²+1)z − q³` (`markovWeightD_root`), so the
  vanishing is an identity in `q`, not a numerical coincidence at the
  substrate anchor. Proved here by exhibiting the radical rather than by a
  `det_fin_six` expansion — cheaper, and it produces the null direction
  instead of merely asserting one exists.
* **Positive-definiteness fails.** It fails already from the radical, before
  any spectral computation; at `q₀` the D-frame spectrum additionally
  carries a negative eigenvalue (`gram-matrix-dual.witness.json`), so the
  form is indefinite, not positive-semi-definite.
* **Symmetry and `G[0,0] = 1` are unchanged**, because they hold for every
  `z` whatever. They are the part of the C section that transfers.

The null direction `(−q³, q², q², −q, −q, 1)` is `−q³ · Σ_w (−1/q)^ℓ(w) T_w`,
the three-strand q-antisymmetriser — the same object
`computations/probes/gram_radical_exact_probe.py` reaches exactly over ℚ at
three rational `q`, and the same one the `qou-u2jg` keystone names from the
trace side. Here it arrives from the determinant, as an identity in `q`.

Ref: [halverson_ram_1998] Hoefsmit seminormal Gram on H_3(q)
Ref: [manuscript] docs/coordination/trace-convention-registry.md
Ref: derivation + six cross-checks
     `computations/probes/gram_h3_convention_frame_probe.py`
-/

/-- The canonical Markov weight, **convention D**: `z = q³/(q² + 1)`. -/
noncomputable def markovWeightD (q : ℝ) : ℝ := q^3 / (q^2 + 1)

/-- **THEOREM.** `z_D` is a root of the determinant factor `(q²+1)z − q³`.

    This is the whole reason the canonical Gram is singular, recorded in Lean
    rather than only in prose: the generic determinant over `ℚ(q,z)` carries
    `(q²+1)z − q³` as a factor, and `markovWeightD` annihilates it for every
    `q`. Stating it here means a later edit cannot quietly relabel this file
    to D and leave a false non-singularity claim standing. -/
theorem markovWeightD_root (q : ℝ) : (q^2 + 1) * markovWeightD q - q^3 = 0 := by
  have hd : (q^2 + 1) ≠ 0 := by positivity
  simp only [markovWeightD]
  field_simp
  ring

/-- The 36 Gram entries on the H_3(q) NF basis in **convention D**, as
    rational functions of `q`. Every denominator is a power of `q² + 1`,
    which is positive over `ℝ` for every `q` — so unlike the C entries these
    need no `q ≠ 0` side condition anywhere. -/
noncomputable def gramEntryD (q : ℝ) : Fin 6 → Fin 6 → ℝ
  | 0, 0 => 1
  | 0, 1 => q^3 / (q^2 + 1)
  | 0, 2 => q^3 / (q^2 + 1)
  | 0, 3 => q^6 / (q^2 + 1)^2
  | 0, 4 => q^6 / (q^2 + 1)^2
  | 0, 5 => (q^7 + q^3) / (q^2 + 1)^2
  | 1, 0 => q^3 / (q^2 + 1)
  | 1, 1 => (q^4 + 1) / (q^2 + 1)
  | 1, 2 => q^6 / (q^2 + 1)^2
  | 1, 3 => (q^7 + q^3) / (q^2 + 1)^2
  | 1, 4 => (q^7 + q^3) / (q^2 + 1)^2
  | 1, 5 => (q^8 + q^4 - q^2) / (q^2 + 1)^2
  | 2, 0 => q^3 / (q^2 + 1)
  | 2, 1 => q^6 / (q^2 + 1)^2
  | 2, 2 => (q^4 + 1) / (q^2 + 1)
  | 2, 3 => (q^7 + q^3) / (q^2 + 1)^2
  | 2, 4 => (q^7 + q^3) / (q^2 + 1)^2
  | 2, 5 => (q^8 + q^4 - q^2) / (q^2 + 1)^2
  | 3, 0 => q^6 / (q^2 + 1)^2
  | 3, 1 => (q^7 + q^3) / (q^2 + 1)^2
  | 3, 2 => (q^7 + q^3) / (q^2 + 1)^2
  | 3, 3 => (q^8 + q^4 - q^2) / (q^2 + 1)^2
  | 3, 4 => (q^8 + 2*q^4 + 1) / (q^2 + 1)^2
  | 3, 5 => (q^9 + q^5 - q^3 + q) / (q^2 + 1)^2
  | 4, 0 => q^6 / (q^2 + 1)^2
  | 4, 1 => (q^7 + q^3) / (q^2 + 1)^2
  | 4, 2 => (q^7 + q^3) / (q^2 + 1)^2
  | 4, 3 => (q^8 + 2*q^4 + 1) / (q^2 + 1)^2
  | 4, 4 => (q^8 + q^4 - q^2) / (q^2 + 1)^2
  | 4, 5 => (q^9 + q^5 - q^3 + q) / (q^2 + 1)^2
  | 5, 0 => (q^7 + q^3) / (q^2 + 1)^2
  | 5, 1 => (q^8 + q^4 - q^2) / (q^2 + 1)^2
  | 5, 2 => (q^8 + q^4 - q^2) / (q^2 + 1)^2
  | 5, 3 => (q^9 + q^5 - q^3 + q) / (q^2 + 1)^2
  | 5, 4 => (q^9 + q^5 - q^3 + q) / (q^2 + 1)^2
  | 5, 5 => (q^10 + q^6 + 2*q^2) / (q^2 + 1)^2

/-- The canonical (convention-D) H_3(q) Gram matrix. -/
noncomputable def gramMatrixD (q : ℝ) : Matrix (Fin 6) (Fin 6) ℝ :=
  Matrix.of (gramEntryD q)

/-- **THEOREM.** The `(0,1)` entry IS the Markov weight, `G[0,1] = tr_M(σ₀) = z`.

    A one-line convention anchor: it pins, in checkable Lean rather than in a
    docstring, which `z` these entries were built from. The corresponding
    C-frame entry is `gramEntry u 0 1 = u/(u²+1) = √q/(q+1)`. -/
theorem gramEntryD_zero_one (q : ℝ) : gramEntryD q 0 1 = markovWeightD q := rfl

/-- **THEOREM.** The canonical Gram matrix is symmetric. Unchanged from C:
    `tr_M(ab) = tr_M(ba)` holds for every Markov weight. -/
theorem gramMatrixD_isSymm (q : ℝ) : (gramMatrixD q).IsSymm := by
  ext i j
  fin_cases i <;> fin_cases j <;> rfl

/-- **THEOREM.** `G[0,0] = tr_M(1) = 1`. Also unchanged from C. -/
theorem gramMatrixD_top_left (q : ℝ) : gramMatrixD q 0 0 = 1 := rfl

/-- The radical direction: `(−q³, q², q², −q, −q, 1)`, which is
    `−q³ · Σ_w (−1/q)^ℓ(w) T_w` — the three-strand q-antisymmetriser in the
    Gröbner–Shirshov normal-form basis `[1, σ₀, σ₁, σ₀σ₁, σ₁σ₀, σ₀σ₁σ₀]`. -/
noncomputable def gramRadicalD (q : ℝ) : Fin 6 → ℝ
  | 0 => -q^3
  | 1 => q^2
  | 2 => q^2
  | 3 => -q
  | 4 => -q
  | 5 => 1

/-- **THEOREM.** The radical direction is non-zero — its last coordinate is
    `1`, for every `q`, including `q = 0`. -/
theorem gramRadicalD_ne_zero (q : ℝ) : gramRadicalD q ≠ 0 := by
  intro hcon
  have h5 : gramRadicalD q 5 = 0 := by rw [hcon]; rfl
  norm_num [gramRadicalD] at h5

set_option maxHeartbeats 2000000 in
/-- **THEOREM.** The q-antisymmetriser is annihilated by the canonical Gram:
    `G_D(q) *ᵥ v = 0`, for every real `q` — no positivity, no `q ≠ 0`, no
    substrate hypothesis. Six row identities, each closed by clearing the
    `(q²+1)` denominators. -/
theorem gramMatrixD_mulVec_radical (q : ℝ) :
    (gramMatrixD q).mulVec (gramRadicalD q) = 0 := by
  have hd : (q^2 + 1) ≠ 0 := by positivity
  ext i
  simp only [Matrix.mulVec, dotProduct, gramMatrixD, Matrix.of_apply,
    Fin.sum_univ_six, gramRadicalD, Pi.zero_apply]
  fin_cases i <;> simp only [gramEntryD] <;> field_simp <;> ring

/-- **THEOREM.** `det G_D(q) = 0` for every real `q`.

    The canonical counterpart of `gramMatrix_det_ne_zero`, and its negation
    in substance: that theorem is true in convention C, this one in D, and D
    is the canonical frame. Proved from the explicit radical via
    `Matrix.exists_mulVec_eq_zero_iff` — which also means the proof *hands
    back* the null direction rather than merely asserting the determinant
    vanishes. -/
theorem gramMatrixD_det_eq_zero (q : ℝ) : (gramMatrixD q).det = 0 := by
  rw [← Matrix.exists_mulVec_eq_zero_iff]
  exact ⟨gramRadicalD q, gramRadicalD_ne_zero q, gramMatrixD_mulVec_radical q⟩

/-- **THEOREM.** The canonical Gram is not positive definite, for any `q`.

    This retracts, in the canonical frame, the positive-definiteness reading
    that the C-frame positivity chain (`detFactor1_pos` … `detFactor6_pos`)
    supports. Note what the proof does *not* need: no spectrum, no `q > 1`,
    no substrate anchor — a single non-zero vector in the radical settles it.
    At `q₀` the D-frame spectrum is in fact indefinite (one zero AND one
    negative eigenvalue), which is strictly worse than this theorem says. -/
theorem gramMatrixD_not_posDef (q : ℝ) : ¬ Matrix.PosDef (gramMatrixD q) := by
  intro hpos
  have hv := gramMatrixD_mulVec_radical q
  have hcon := hpos.2 (gramRadicalD q) (gramRadicalD_ne_zero q)
  rw [hv] at hcon
  simp at hcon

end QOU.Interactions.GramMatrixH3Symbolic

/-! ## Direct-use pattern

`HasH3GramMatrix` was reverted from `universal-ilp-algorithm.lean`
(main commit `91cb2671b`, 2026-05-25, "Phase 1a typeclass infrastructure
is superseded by the symbolic Gram entries — the typeclass-driven approach
added an unnecessary layer of indirection when the categorical entries
are directly definable"). Downstream consumers use `gramMatrix u`
directly with the three structural theorems below.

**Canonical (convention D) usage** — note there is no `Real.sqrt`, no
`q > 1`, and the determinant conclusion runs the other way:

```lean
example (q : ℝ) :
    ∃ G : Matrix (Fin 6) (Fin 6) ℝ,
      G.IsSymm ∧ G 0 0 = 1 ∧ G.det = 0 :=
  ⟨gramMatrixD q, gramMatrixD_isSymm _, gramMatrixD_top_left _,
   gramMatrixD_det_eq_zero _⟩
```

**Convention-C usage, for the C-frame results only** (`z = √q/(q+1)`,
excised 2026-08-09 / re-affirmed 2026-08-15). Do not reach for this to
establish that "the H_3 Gram is non-singular" — canonically it is not:

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
