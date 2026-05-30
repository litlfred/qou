/-
  Diagonal entries of the Frobenius Gram matrix for H_3(R, q) over the
  normal-form basis `{1, σ_0, σ_1, σ_0σ_1, σ_1σ_0, σ_0σ_1σ_0}`.

  The Frobenius Gram matrix is `G_{ij} = tr_M(b_i · b_j)` evaluated on
  the 6-element normal-form basis of `H_3(R, q)`.  Each diagonal entry
  is derived from the Hecke relation `σ_i² = h · σ_i + 1` (with
  `h := q - q⁻¹`) and the Markov axioms `tr_M(1) = 1`,
  `tr_M(σ_i) = z`, and `tr_M(x · σ_n) = z · tr_M(x)` for `x ∈ H_n`,
  where `z := 1 / (√q + 1/√q)`.

  Companion to `prop:frobenius-gram-matrix` and to the
  `gram_matrix q` stub in
  `particle-interactions/universal-ilp-algorithm.lean` L28-29, which a
  follow-up PR will wire to consume these definitions.

  Reference Python: `folio-assistant/computations/gram-matrix-dual.py`
  (line 138, `G = np.zeros((6, 6))` is filled by `_build_gram()`).
  Numerical cross-check witness:
  `folio-assistant/computations/gram-matrix-dual.witness.json`
  records the values at `q = q_0 ≈ 1.1099798`:

      G_{0,0} = 1.0
      G_{1,1} = G_{2,2} = 1.1043880698  (= h·z + 1)
      G_{3,3} = G_{4,4} = 0.3646057349  (= h²·z² + h·z + z²)
      G_{5,5} = 1.3508934855            (= h⁴·z² + 3h²·z² + h³·z + 3h·z + 1)

  LaTeX label: `rem:h3-gram-diagonal` (helper Lean infrastructure).
-/

-- Ref: [manuscript] prop:frobenius-gram-matrix; companion to
--      particle-interactions/universal-ilp-algorithm.lean

import Mathlib.Data.Real.Basic
import Mathlib.Analysis.SpecialFunctions.Pow.Real

namespace QOU.BraidKnot.H3GramDiagonal

/-! ## Auxiliary scalars -/

/-- Hecke deformation parameter `h := q - q⁻¹`. -/
noncomputable def h (q : ℝ) : ℝ := q - q⁻¹

/-- Markov-Jones parameter `z := 1 / (√q + 1/√q)`.

    Mirrors `markovZax` in `markov-axioms-primitive.lean`.  Re-declared
    here so this module is self-contained pending the eventual
    consolidation into a single shared file. -/
noncomputable def z (q : ℝ) : ℝ := 1 / (Real.sqrt q + (Real.sqrt q)⁻¹)

/-! ## Diagonal entries

    Each entry below is `G_{i,i} = tr_M(b_i · b_i)` where `b_i` is the
    `i`-th normal-form basis element `{1, σ_0, σ_1, σ_0σ_1, σ_1σ_0,
    σ_0σ_1σ_0}`.

    Derivation sketches accompany each entry; the symbolic form has
    been cross-checked against the Python reference at `q_0`.
-/

/-- `G_{0,0} = tr_M(1 · 1) = tr_M(1) = 1` (Markov axiom M1). -/
noncomputable def diag_0 (_q : ℝ) : ℝ := 1

/-- `G_{1,1} = tr_M(σ_0 · σ_0) = tr_M(σ_0²) = tr_M(h·σ_0 + 1)
            = h · tr_M(σ_0) + tr_M(1) = h · z + 1`.

    Uses the Hecke relation `σ_i² = h · σ_i + 1` and the Markov axioms
    M1, M3. -/
noncomputable def diag_1 (q : ℝ) : ℝ := h q * z q + 1

/-- `G_{2,2} = tr_M(σ_1 · σ_1) = h · z + 1`.  Same derivation as
    `diag_1` with `σ_0 ↔ σ_1` (the Hecke relation is uniform in the
    generator index). -/
noncomputable def diag_2 (q : ℝ) : ℝ := h q * z q + 1

/-- `G_{3,3} = tr_M(σ_0σ_1 · σ_0σ_1) = tr_M(σ_0σ_1σ_0σ_1)`.

    Derivation:
    ```
      σ_0σ_1σ_0σ_1 = σ_0 · σ_1σ_0σ_1
                   = σ_0 · σ_0σ_1σ_0    [braid relation σ_1σ_0σ_1 = σ_0σ_1σ_0]
                   = σ_0² · σ_1σ_0
                   = (h·σ_0 + 1) · σ_1σ_0
                   = h · σ_0σ_1σ_0 + σ_1σ_0
    ```
    Hence
    ```
      tr_M(σ_0σ_1σ_0σ_1) = h · tr_M(σ_0σ_1σ_0) + tr_M(σ_1σ_0)
                         = h · (h·z² + z) + z²        [trefoil + adjacent traces]
                         = h²·z² + h·z + z².
    ```
-/
noncomputable def diag_3 (q : ℝ) : ℝ :=
  (h q)^2 * (z q)^2 + h q * z q + (z q)^2

/-- `G_{4,4} = tr_M(σ_1σ_0 · σ_1σ_0) = h²·z² + h·z + z²`.  Same
    derivation as `diag_3` with the generator pair swapped; the
    braid-relation symmetry collapses both to the same closed form. -/
noncomputable def diag_4 (q : ℝ) : ℝ :=
  (h q)^2 * (z q)^2 + h q * z q + (z q)^2

/-- `G_{5,5} = tr_M(σ_0σ_1σ_0 · σ_0σ_1σ_0) = tr_M((σ_0σ_1σ_0)²)`.

    Derivation (five-step Hecke + braid reduction):
    ```
      (σ_0σ_1σ_0)² = σ_0σ_1 · σ_0² · σ_1σ_0
                   = σ_0σ_1 · (h·σ_0 + 1) · σ_1σ_0
                   = h · σ_0σ_1σ_0σ_1σ_0 + σ_0σ_1 · σ_1σ_0
                   = h · σ_0σ_1σ_0σ_1σ_0 + σ_0 · σ_1² · σ_0
                   = h · σ_0σ_1σ_0σ_1σ_0 + σ_0 · (h·σ_1 + 1) · σ_0
                   = h · σ_0σ_1σ_0σ_1σ_0 + h · σ_0σ_1σ_0 + σ_0²
                   = h · σ_0σ_1σ_0σ_1σ_0 + h · σ_0σ_1σ_0 + h·σ_0 + 1.
    ```
    Now `σ_0σ_1σ_0σ_1σ_0 = h · σ_0σ_1σ_0σ_1 + h · σ_0σ_1 + σ_1` by an
    analogous reduction, and inserting traces gives
    ```
      tr_M(σ_0σ_1σ_0σ_1σ_0) = h · (h²·z² + h·z + z²) + h · z² + z
                            = h³·z² + h²·z + 2h·z² + z.
    ```
    Therefore
    ```
      G_{5,5} = h · (h³·z² + h²·z + 2h·z² + z)
                + h · (h·z² + z) + h·z + 1
              = h⁴·z² + 3h²·z² + h³·z + 3h·z + 1.
    ```
-/
noncomputable def diag_5 (q : ℝ) : ℝ :=
  (h q)^4 * (z q)^2 + 3 * (h q)^2 * (z q)^2 + (h q)^3 * z q + 3 * h q * z q + 1

/-! ## Assembly -/

/-- Collected diagonal of the Frobenius Gram matrix on the NF basis
    `{1, σ_0, σ_1, σ_0σ_1, σ_1σ_0, σ_0σ_1σ_0}`. -/
noncomputable def diag (q : ℝ) : Fin 6 → ℝ
  | 0 => diag_0 q
  | 1 => diag_1 q
  | 2 => diag_2 q
  | 3 => diag_3 q
  | 4 => diag_4 q
  | 5 => diag_5 q

/-! ## Symmetry lemmas (free from the closed forms) -/

/-- `G_{1,1} = G_{2,2}` (generator-swap symmetry). -/
theorem diag_1_eq_diag_2 (q : ℝ) : diag_1 q = diag_2 q := rfl

/-- `G_{3,3} = G_{4,4}` (braid-relation symmetry under `σ_0σ_1 ↔ σ_1σ_0`). -/
theorem diag_3_eq_diag_4 (q : ℝ) : diag_3 q = diag_4 q := rfl

end QOU.BraidKnot.H3GramDiagonal
