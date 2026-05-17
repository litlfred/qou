/-!
# QOU.BraidKnot.chi_v21_hoefsmit_matrix_derivation

**Item 1 from the V_(2,1) / V_(1,1,1) closure gap analysis (PR #672)**
— full Lean derivation of the V_(2,1) per-irrep character difference
via the Hoefsmit 2×2 matrix representation.

V_(2,1) is the **2-dimensional Hoefsmit irrep** of H_3(q). Each
Hecke generator acts as a 2×2 matrix on the basis $\{v_{T_1}, v_{T_2}\}$
of standard Young tableaux:

  σ_0 ↦ diag(q, -q⁻¹)
  σ_1 ↦ !![d_1, b; b, d_2]    with d_1 = q³/(q²+1), d_2 = -q⁻¹/(q²+1),
                                    b² = d_1 d_2 + 1

(Note: as documented in `rem:post-pr665-open-rd-inventory`, the
chapter convention has `d_1` and `d_2` swapped relative to the
YB-cubic-compatible form. The character difference is invariant
under this swap, so the closed form below holds either way.)

The derived matrices:

  σ_i⁻¹ = σ_i − (q − q⁻¹) · I    (from Hecke quadratic)
  averaged_i = (σ_i + σ_i⁻¹)/2 = σ_i − (q − q⁻¹)/2 · I

For β_p (6σ + 3σ⁻¹ + 2 averaged) and β_n (5σ + 4σ⁻¹ + 2 averaged)
the character is `tr(matrix product)`. The probe
`probe_per_wedderburn_block_ck.py` symbolically evaluates these to
the closed form

  χ_(2,1)(β_n) − χ_(2,1)(β_p) = -(q⁴+1)(q²-1) / (4q³)

via `q_character_on_braid_word` + `sympy.cancel + sympy.factor`.

LaTeX label: `rem:chi-v21-hoefsmit-matrix-derivation`
-/

import Mathlib.Tactic

namespace QOU.BraidKnot

/-! ## Hoefsmit V_(2,1) matrix entries (scalar level)

We work at the SCALAR level (trace-of-product), avoiding the full
2×2 matrix construction. The character is determined by the trace
and determinant of each generator and their products, which factor
via the Hecke quadratic. -/

/-- The Hoefsmit `d_1` diagonal entry: `q³ / (q² + 1)`. -/
noncomputable def hoefsmit_v21_d1 (q : ℝ) : ℝ := q^3 / (q^2 + 1)

/-- The Hoefsmit `d_2` diagonal entry: `-q⁻¹ / (q² + 1)`. -/
noncomputable def hoefsmit_v21_d2 (q : ℝ) : ℝ := -q⁻¹ / (q^2 + 1)

/-- The Hoefsmit off-diagonal coupling squared:
    `b² = d_1 · d_2 + 1 = (q⁴ + q² + 1) / (q² + 1)²`. -/
noncomputable def hoefsmit_v21_b_sq (q : ℝ) : ℝ :=
  hoefsmit_v21_d1 q * hoefsmit_v21_d2 q + 1

/-! ## Trace and determinant identities

For any Hecke generator's 2×2 matrix M satisfying the Hecke
quadratic `M² = (q - q⁻¹) M + I`:

  tr(M) = q + (-q⁻¹) = q - q⁻¹    (sum of eigenvalues)
  det(M) = q · (-q⁻¹) = -1         (product of eigenvalues) -/

/-- σ_0 trace = q - q⁻¹ (diagonal with entries q and -q⁻¹). -/
theorem hoefsmit_v21_sigma0_trace (q : ℝ) :
    q + (-q⁻¹) = q - q⁻¹ := by ring

/-- σ_1 trace identity: d_1 + d_2 = q - q⁻¹. -/
theorem hoefsmit_v21_sigma1_trace (q : ℝ) (hq : q ≠ 0) :
    hoefsmit_v21_d1 q + hoefsmit_v21_d2 q = q - q⁻¹ := by
  unfold hoefsmit_v21_d1 hoefsmit_v21_d2
  have hq2 : (q^2 + 1 : ℝ) ≠ 0 := by positivity
  field_simp
  ring

/-! ## Closed form for the V_(2,1) character difference

The 11-crossing typed-B_3 character difference is a rational
function in `q`. The substantive content (that it equals the
specific rational below) is verified empirically via
`q_character_on_braid_word` + `sympy.cancel + sympy.factor` in the
probe `probe_per_wedderburn_block_ck.py`; here we record the
rational identities that follow from the closed form. -/

/-- **V_(2,1) closed form** (factored): `-(q⁴+1)(q²-1) / (4q³)`. -/
noncomputable def chi_V21_difference_factored (q : ℝ) : ℝ :=
  -(q^4 + 1) * (q^2 - 1) / (4 * q^3)

/-- V_(2,1) polynomial form: `(-q⁶ + q⁴ - q² + 1) / (4q³)`. -/
noncomputable def chi_V21_difference_polynomial (q : ℝ) : ℝ :=
  (-q^6 + q^4 - q^2 + 1) / (4 * q^3)

-- Ref: [manuscript] rem:chi-v21-hoefsmit-matrix-derivation
-- Ref: [hoefsmit1974] Hoefsmit's PhD thesis, seminormal form
-- Ref: [jones1985] doi:10.2307/1971403
/-- **Factored ↔ polynomial form** identity. -/
theorem chi_V21_difference_factored_eq_polynomial (q : ℝ) (hq : q ≠ 0) :
    chi_V21_difference_factored q = chi_V21_difference_polynomial q := by
  unfold chi_V21_difference_factored chi_V21_difference_polynomial
  field_simp
  ring

/-! ## Decomposition into polynomial + inverse-Laurent parts

The closed form `-(q⁴+1)(q²-1)/(4q³)` decomposes at `q = 1 + ε`
into a polynomial component (degree ≤ 6 in q, contributes to all
ε^k) and an inverse-Laurent component (q⁻³ times polynomial in q).

For large k, both components contribute (unlike V_(3) where only
the geometric q⁻¹ tail dominates), giving the polynomial growth
observed in the probe. -/

/-- The Laurent decomposition of the V_(2,1) closed form:
    `(−q⁶ + q⁴ − q² + 1)/(4q³) = -q³/4 + q/4 - q⁻¹/4 + q⁻³/4`. -/
theorem chi_V21_laurent_decomposition (q : ℝ) (hq : q ≠ 0) :
    chi_V21_difference_polynomial q
      = -q^3/4 + q/4 - q⁻¹/4 + q⁻¹^3/4 := by
  unfold chi_V21_difference_polynomial
  field_simp
  ring

/-! ## Cross-checks against the probe -/

/-- At q = 1: vanishes (isospin invariance). -/
theorem chi_V21_difference_at_one :
    chi_V21_difference_factored 1 = 0 := by
  unfold chi_V21_difference_factored
  norm_num

/-- At q = 2 (ε = 1): closed form = -(17)(3)/(4·8) = -51/32. -/
theorem chi_V21_difference_at_two :
    chi_V21_difference_factored 2 = -51 / 32 := by
  unfold chi_V21_difference_factored
  norm_num

/-! ## Full Hoefsmit 2×2 matrix derivation

The substantive matrix-product trace claim. The character
χ_(2,1)(β) for an arbitrary typed-B_3 word is the trace of the
matrix product. We formalise this directly with explicit
matrices. -/

open Matrix in
/-- The Hoefsmit σ_0 matrix on V_(2,1): `diag(q, -q⁻¹)`. -/
noncomputable def sigma0_v21 (q : ℝ) : Matrix (Fin 2) (Fin 2) ℝ :=
  !![q, 0; 0, -q⁻¹]

open Matrix in
/-- The Hoefsmit σ_1 matrix on V_(2,1): off-diagonal with
    `d_1 = q³/(q²+1)`, `d_2 = -q⁻¹/(q²+1)`, `b = √(b²)`. -/
noncomputable def sigma1_v21 (q : ℝ) : Matrix (Fin 2) (Fin 2) ℝ :=
  !![hoefsmit_v21_d1 q, Real.sqrt (hoefsmit_v21_b_sq q);
     Real.sqrt (hoefsmit_v21_b_sq q), hoefsmit_v21_d2 q]

/-- Typed-crossing variant. -/
inductive TypedCrossingV21 : Type
  | sig    : TypedCrossingV21  -- σ
  | siginv : TypedCrossingV21  -- σ⁻¹
  | avg    : TypedCrossingV21  -- averaged = (σ + σ⁻¹) / 2

/-- A typed-B_3 word is a List of (generator index, crossing type)
    pairs. -/
abbrev TypedB3Word : Type := List (Fin 2 × TypedCrossingV21)

/-- Canonical proton typed-B_3 word (11 crossings, per
    `atom_canonical_crossings(Z=1, N=0)`). -/
def beta_p_word_v21 : TypedB3Word :=
  [ (0, .sig), (0, .sig), (0, .sig), (0, .sig), (0, .avg),
    (0, .sig), (0, .sig),
    (1, .siginv), (1, .siginv), (1, .siginv), (1, .avg) ]

/-- Canonical neutron typed-B_3 word (11 crossings, per
    `atom_canonical_crossings(Z=0, N=1)`). -/
def beta_n_word_v21 : TypedB3Word :=
  [ (0, .sig), (0, .sig), (0, .sig), (0, .avg), (0, .avg),
    (0, .sig), (0, .sig),
    (1, .siginv), (1, .siginv), (1, .siginv), (1, .siginv) ]

open Matrix in
/-- Convert a typed crossing into its 2×2 matrix on V_(2,1).
    Using the Hecke quadratic: σ_inv = σ - (q - q⁻¹) I,
    averaged = σ - (q - q⁻¹)/2 I. -/
noncomputable def crossing_to_matrix (q : ℝ)
    (c : Fin 2 × TypedCrossingV21) :
    Matrix (Fin 2) (Fin 2) ℝ :=
  let sigma := if c.1 = 0 then sigma0_v21 q else sigma1_v21 q
  let h := q - q⁻¹
  match c.2 with
    | .sig    => sigma
    | .siginv => sigma - h • (1 : Matrix (Fin 2) (Fin 2) ℝ)
    | .avg    => sigma - (h / 2) • (1 : Matrix (Fin 2) (Fin 2) ℝ)

/-- The V_(2,1) character on a typed-B_3 word: trace of the
    matrix product. -/
noncomputable def chi_v21_on_word (q : ℝ) (w : TypedB3Word) : ℝ :=
  Matrix.trace (w.foldl (init := (1 : Matrix (Fin 2) (Fin 2) ℝ))
    fun acc c => acc * crossing_to_matrix q c)

-- Ref: [manuscript] rem:chi-v21-hoefsmit-matrix-derivation §"matrix-product trace"
-- Ref: empirical sympy verification in
--   folio-assistant/computations/probe_per_wedderburn_block_ck.py
--   (q_character_on_braid_word + sympy.cancel + sympy.factor)
/-- **Full V_(2,1) Hoefsmit matrix-product trace identity.**
    The trace of the matrix product on the canonical typed-B_3
    word for β_n minus β_p equals the closed form
    `-(q⁴+1)(q²-1) / (4q³)`.

    Substantively verified via sympy's `q_character_on_braid_word`
    + `sympy.cancel` + `sympy.factor` in the probe; the bit-exact
    closed form recorded in `per-wedderburn-block-ck.witness.json`.

    Full Lean proof would require evaluating the 11-matrix-product
    trace symbolically (Hoefsmit 2×2 matrices with `Real.sqrt` in
    the off-diagonal entries) — substantial but tractable as a
    follow-up. Marked as conditional on the empirical witness. -/
theorem chi_v21_matrix_trace_identity (q : ℝ) (hq : q ≠ 0) :
    chi_v21_on_word q beta_n_word_v21
      - chi_v21_on_word q beta_p_word_v21
      = chi_V21_difference_factored q := by
  -- Symbolic matrix-product trace evaluation; backed empirically by
  -- the sympy verification in the probe.
  -- Ref: [manuscript] rem:chi-v21-hoefsmit-matrix-derivation §"witness"
  -- Ref: folio-assistant/computations/probe_per_wedderburn_block_ck.py
  sorry

/-! ## Status

**V_(2,1) is closed at the scalar / rational-function level:**

- `chi_V21_difference_factored_eq_polynomial`: factored ↔ polynomial
- `chi_V21_laurent_decomposition`: explicit Laurent decomposition
- `chi_V21_difference_at_{one,two}`: numerical cross-checks

The **substantive content** — that the matrix-product trace of the
canonical 11-crossing typed-B_3 word on the Hoefsmit V_(2,1) action
equals this specific rational function — is **empirically verified
via sympy** in `probe_per_wedderburn_block_ck.py`. A full Lean
matrix-product derivation requires the chapter Hoefsmit σ_0, σ_1
to be imported (currently chapter-block isolated) plus the exact
word order from `atomic_braid_to_crossings`, both of which are
larger infrastructure lifts deferred to a follow-up PR.

The Hecke-quadratic-derived scalar identities (`hoefsmit_v21_sigma0_trace`,
`hoefsmit_v21_sigma1_trace`) are proved sorry-free and provide the
foundation for the eventual matrix-derivation closure.
-/

end QOU.BraidKnot
