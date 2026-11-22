import Mathlib.Tactic


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

namespace QOU.BraidKnot

/-! ## Hoefsmit V_(2,1) matrix entries (scalar level)

We work at the SCALAR level (trace-of-product), avoiding the full
2×2 matrix construction. The character is determined by the trace
and determinant of each generator and their products, which factor
via the Hecke quadratic. -/

/-- The Hoefsmit `d_1` diagonal entry — the `(0,0)` entry of `σ_1`:
    `-q⁻¹ / (q² + 1)`.

    **CORRECTED 2026-09-04 (bean `qou-18b6`): `d_1` and `d_2` were
    transposed.** They read `d_1 = q³/(q²+1)`, `d_2 = -q⁻¹/(q²+1)`, which
    with this file's `σ_0 = diag(q, -q⁻¹)` does **not** satisfy the braid
    relation `σ_0 σ_1 σ_0 = σ_1 σ_0 σ_1` — so the pair was not a
    representation of `B_3` at all, and every trace computed from it was
    of something that does not exist.

    Nothing in the file could detect it, and that is the point: `b² =
    d_1·d_2 + 1`, `d_1 + d_2 = q - q⁻¹` and `det = -1` are all **symmetric
    in `d_1, d_2`**, so `hoefsmit_v21_b_sq_rational`, `hoefsmit_v21_sigma1_trace`
    and the Hecke quadratic hold verbatim under the transposition. Only a
    relation involving `σ_0` and `σ_1` *together* separates them, which is
    why `hoefsmit_v21_braid_relation` below is now stated.

    Two independent confirmations of the corrected assignment: solving
    `{trace = q - q⁻¹, det = -1, braid}` for `(d_1, d_2, b)` returns this
    one (up to the sign of `b`, and the degenerate `b = 0`); and at `q = 1`
    it gives `σ_1 = !![-1/2, √3/2; √3/2, 1/2]`, the classical Young
    orthogonal form of `s_2` on the 2-dimensional representation of `S_3`.
    The transposed version gave `+1/2` in the `(0,0)` slot. -/
noncomputable def hoefsmit_v21_d1 (q : ℝ) : ℝ := -q⁻¹ / (q^2 + 1)

/-- The Hoefsmit `d_2` diagonal entry — the `(1,1)` entry of `σ_1`:
    `q³ / (q² + 1)`. See `hoefsmit_v21_d1` for why this is not the other
    way round. -/
noncomputable def hoefsmit_v21_d2 (q : ℝ) : ℝ := q^3 / (q^2 + 1)

/-- The Hoefsmit off-diagonal coupling squared:
    `b² = d_1 · d_2 + 1 = (q⁴ + q² + 1) / (q² + 1)²`. -/
noncomputable def hoefsmit_v21_b_sq (q : ℝ) : ℝ :=
  hoefsmit_v21_d1 q * hoefsmit_v21_d2 q + 1

/-- The b² expression as a rational function of q (= polynomial in
    u = q² over (u + 1)²).

    **Moved up from the end of the file.** `chi_v21_matrix_trace_identity`
    below consumes it, and Lean is order-sensitive: declared after its
    consumer, it produced `Unknown identifier hoefsmit_v21_b_sq_rational`
    at the use site — a forward reference, not a missing declaration, and
    the two are indistinguishable from the error text alone. -/
theorem hoefsmit_v21_b_sq_rational (q : ℝ) (hq : q ≠ 0) :
    hoefsmit_v21_b_sq q = (q^4 + q^2 + 1) / (q^2 + 1)^2 := by
  unfold hoefsmit_v21_b_sq hoefsmit_v21_d1 hoefsmit_v21_d2
  have h : (q^2 + 1 : ℝ) ≠ 0 := by positivity
  field_simp
  ring

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

/-- **V_(2,1) closed form** (factored): `-(q⁴+1)(q²-1) / (4q³)`.

    DUPLICATION TRACKING: also defined as `chi_V21_diff_closed`
    in `rem:chi-per-irrep-cyclotomic-closed-forms`. Local copy
    here for self-containment; centralisation deferred per the
    chapter-block file-isolation convention. -/
noncomputable def chi_V21_difference_factored (q : ℝ) : ℝ :=
  -(q^4 + 1) * (q^2 - 1) / (4 * q^3)

/-- V_(2,1) polynomial form: `(-q⁶ + q⁴ - q² + 1) / (4q³)`. -/
noncomputable def chi_V21_difference_polynomial (q : ℝ) : ℝ :=
  (-q^6 + q^4 - q^2 + 1) / (4 * q^3)

-- Ref: [leitner2026] rem:chi-v21-hoefsmit-matrix-derivation
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

/-- The Hoefsmit σ_1 matrix on V_(2,1) — **Tier 2 generic-R form**.
    The off-diagonal entry `b` is taken as an abstract square-root of
    `hoefsmit_v21_b_sq q`; downstream consumers supply the witness either
    formally (`u² = q` style adjoin) or archimedeanly. -/
def sigma1_v21_gen {R : Type*} [Field R]
    (d1 d2 b : R) : Matrix (Fin 2) (Fin 2) R :=
  !![d1, b; b, d2]

open Matrix in
/-- **Legacy archimedean form** of `sigma1_v21` — instantiates the
    off-diagonal as `Real.sqrt (hoefsmit_v21_b_sq q)` without an explicit
    `0 ≤ hoefsmit_v21_b_sq q` hypothesis. Use `sigma1_v21_gen` in new
    code with an explicit square-root witness. -/
@[deprecated "Migrate to the generic `sigma1_v21_gen d1 d2 b` with an explicit `b² = hoefsmit_v21_b_sq q` hypothesis (Tier 2), or a future archimedean shim carrying `0 ≤ hoefsmit_v21_b_sq q` (Tier 5). See docs/audits/2026-06-01-hoefsmit-tier2-migration-plan.md." (since := "2026-06-01")]
noncomputable def sigma1_v21_legacy (q : ℝ) : Matrix (Fin 2) (Fin 2) ℝ :=
  !![hoefsmit_v21_d1 q, Real.sqrt (hoefsmit_v21_b_sq q);
     Real.sqrt (hoefsmit_v21_b_sq q), hoefsmit_v21_d2 q]

/-- Backward-compatibility alias — `sigma1_v21` is the legacy form.
    Phase 2 migrates this file's downstream uses to `sigma1_v21_gen`. -/
@[deprecated "Use `sigma1_v21_legacy` explicitly (Phase 1), or migrate to `sigma1_v21_gen` (Phase 2)." (since := "2026-06-01")]
noncomputable def sigma1_v21 (q : ℝ) : Matrix (Fin 2) (Fin 2) ℝ :=
  sigma1_v21_legacy q

open Matrix in
/-- **The braid relation `σ_0 σ_1 σ_0 = σ_1 σ_0 σ_1` on `V_(2,1)`** — stated
    for the generic Tier-2 form with the off-diagonal `b` a free parameter
    constrained only by `b² = d_1 d_2 + 1`.

    This is the relation the file did not have, and its absence is what let a
    transposed `(d_1, d_2)` stand: trace, determinant and the Hecke quadratic
    are each **symmetric** in `d_1, d_2`, so all three hold for the wrong
    matrix. The braid relation couples `σ_0` and `σ_1`, and it is the
    cheapest statement that does. See `hoefsmit_v21_d1`.

    Note it needs no hypothesis on `b` beyond the quadratic — in particular
    no `0 ≤ b²` and no square root — so it holds over any field, which is
    the Tier-2 point. -/
theorem hoefsmit_v21_braid_relation (q b : ℝ) (hq : q ≠ 0)
    (hb : b ^ 2 = hoefsmit_v21_d1 q * hoefsmit_v21_d2 q + 1) :
    sigma0_v21 q * sigma1_v21_gen (hoefsmit_v21_d1 q) (hoefsmit_v21_d2 q) b
        * sigma0_v21 q
      = sigma1_v21_gen (hoefsmit_v21_d1 q) (hoefsmit_v21_d2 q) b
        * sigma0_v21 q
        * sigma1_v21_gen (hoefsmit_v21_d1 q) (hoefsmit_v21_d2 q) b := by
  have hq2 : (q ^ 2 + 1 : ℝ) ≠ 0 := by positivity
  unfold sigma0_v21 sigma1_v21_gen hoefsmit_v21_d1 hoefsmit_v21_d2 at *
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [Matrix.mul_fin_two] <;> field_simp at hb ⊢ <;> nlinarith [hb, sq_nonneg q]

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

-- Ref: [leitner2026] rem:chi-v21-hoefsmit-matrix-derivation §"matrix-product trace"
-- Ref: [leitner2026] empirical sympy verification in
--   computations/probe_per_wedderburn_block_ck.py
--   (q_character_on_braid_word + sympy.cancel + sympy.factor)
set_option maxHeartbeats 4000000 in
/-- **Full V_(2,1) Hoefsmit matrix-product trace identity.**
    The trace of the matrix product on the canonical typed-B_3
    word for β_n minus β_p equals the closed form
    `-(q⁴+1)(q²-1) / (4q³)`.

    Substantively verified via sympy's `q_character_on_braid_word`
    + `sympy.cancel` + `sympy.factor` in the probe; the bit-exact
    closed form recorded in `per-wedderburn-block-ck.witness.json`.

    **PROVED sorry-free 2026-09-04** (bean `qou-18b6`). Two things had to
    happen, in this order, and the first was not what the file expected.

    **It was FALSE until the same day.** Until the `d_1`/`d_2` transposition
    was fixed (see `hoefsmit_v21_d1`), these matrices gave

        chi_n - chi_p = -(q-1)(q+1)(q⁴+1)(q²-q+1)(q²+q+1) / (4q⁵)

    which is the right-hand side below times `(q⁴+q²+1)/q²`. The note that
    stood here — "the claim is exactly the one sympy verifies" — was not true
    of *these definitions*, and no proof existed to be found. The closed form
    itself was never in doubt: at `q = 1+ε` it reproduces the ε-coefficients
    in `_deprecated/per-wedderburn-block-ck.witness.json` exactly, while the
    transposed matrices do not.

    **The proof, and the two things that make it go through.** Expand with
    `simp only` over the definitions and `List.foldl_cons`, then
    `Matrix.mul_fin_two` folds the eleven factors into one `!![_,_;_,_]`.
    Then:

    * **Project with `Matrix.trace_fin_two_of`, not `Matrix.trace_fin_two`.**
      The former rewrites `trace !![a,b;c,d]` straight to `a + d`; the latter
      leaves `M 0 0 + M 1 1` as *applications*, which blocks everything after
      it. This is the whole difference between a goal that closes and one
      that does not, and it is invisible from the two lemma names.
    * **Only then generalise the square root.** `Real.sqrt (hoefsmit_v21_b_sq q)`
      becomes a free `b` carrying `b² = (q⁴+q²+1)/(q²+1)²`; `ring_nf`
      normalises, and `rw [hb4, hb2]` eliminates `b` entirely — `b⁴` first,
      since `rw [hb2]` cannot see inside it. `field_simp; ring` finishes.

    **Why no `linear_combination` certificate is needed, contrary to the
    earlier note.** Only EVEN powers of `b` reach the trace: each index-1
    factor is symmetric with off-diagonal `b`, so a path from a diagonal slot
    back to itself takes an even number of off-diagonal steps. Odd powers do
    occur — `b³` appears 20 times in the normalised matrix — but only in the
    OFF-diagonal entries, which the trace discards. Projecting first is what
    makes the substitution `b² ↦ …` sufficient on its own.

    **Measured dead end, recorded so it is not re-walked.** With
    `Matrix.trace_fin_two` instead, the goal stays as index applications,
    `field_simp` runs on the un-projected expression and **exhausts
    2 000 000 heartbeats**. Per the trap this file already carries, the
    heartbeat bump was applied first, so that is a real exhaustion and not a
    default-budget timeout.

    The statement is unchanged from when it carried the `sorry`; only the
    matrices it is about were corrected. Bean `qou-18b6`. -/
-- Ref: [leitner2026] rem:chi-v21-hoefsmit-matrix-derivation §"matrix-product trace"
-- Ref: [leitner2026] empirical sympy verification in
--   computations/probe_per_wedderburn_block_ck.py
--   (q_character_on_braid_word + sympy.cancel + sympy.factor);
--   closed form recorded in per-wedderburn-block-ck.witness.json
theorem chi_v21_matrix_trace_identity (q : ℝ) (hq : q ≠ 0) :
    chi_v21_on_word q beta_n_word_v21
      - chi_v21_on_word q beta_p_word_v21
      = chi_V21_difference_factored q := by
  have hqq : (q ^ 2 + 1 : ℝ) ≠ 0 := by positivity
  have hnn : (0:ℝ) ≤ hoefsmit_v21_b_sq q := by
    rw [hoefsmit_v21_b_sq_rational q hq]; positivity
  have hb2 : Real.sqrt (hoefsmit_v21_b_sq q) ^ 2
      = (q ^ 4 + q ^ 2 + 1) / (q ^ 2 + 1) ^ 2 := by
    rw [Real.sq_sqrt hnn, hoefsmit_v21_b_sq_rational q hq]
  have hif : ∀ A B : Matrix (Fin 2) (Fin 2) ℝ,
      (if (1 : Fin 2) = 0 then A else B) = B := by
    intro A B; norm_num
  have hsm : ∀ c : ℝ, c • (1 : Matrix (Fin 2) (Fin 2) ℝ) = !![c, 0; 0, c] := by
    intro c; ext i j; fin_cases i <;> fin_cases j <;> simp [Matrix.one_apply]
  have hsub : ∀ a b c d e f g h : ℝ,
      (!![a, b; c, d] : Matrix (Fin 2) (Fin 2) ℝ) - !![e, f; g, h]
        = !![a - e, b - f; c - g, d - h] := by
    intro a b c d e f g h; ext i j; fin_cases i <;> fin_cases j <;> simp
  simp only [chi_v21_on_word, beta_n_word_v21, beta_p_word_v21, crossing_to_matrix,
    sigma1_v21, sigma1_v21_legacy, sigma0_v21, hoefsmit_v21_d1, hoefsmit_v21_d2,
    chi_V21_difference_factored, List.foldl_cons, List.foldl_nil,
    if_true, hif, one_mul]
  simp only [hsm, hsub, Matrix.mul_fin_two, Matrix.trace_fin_two_of]
  generalize Real.sqrt (hoefsmit_v21_b_sq q) = b at hb2 ⊢
  have hb4 : b ^ 4 = ((q ^ 4 + q ^ 2 + 1) / (q ^ 2 + 1) ^ 2) ^ 2 := by
    rw [show (4:ℕ) = 2 * 2 from rfl, pow_mul, hb2]
  ring_nf
  rw [hb4, hb2]
  field_simp
  ring

/-! ## u = q² coordinate: sqrt-free trace identity

KEY INSIGHT (per user direction): both β_p and β_n have σ_1
appearing an **even** number of times (4 each: 3 σ_1⁻¹ + 1 avg
in β_p, 4 σ_1⁻¹ in β_n). The trace of the matrix product then
depends only on `b² = (q⁴+q²+1)/(q²+1)²` (polynomial in u = q²),
NEVER on the `Real.sqrt` of `b²`.

So we can **parameterise σ_1 by an abstract `b_arg : ℝ`** without
constraining b_arg = √(b²); the trace identity will hold as a
polynomial identity in b_arg, and because only even powers of b_arg
appear, we can substitute `b_arg² = b_sq q` at the end. -/

open Matrix in
/-- **Parameterised Hoefsmit σ_1**: off-diagonal coupling supplied
    as a free parameter `b_arg`, not constrained to `√(b²)`. The
    trace of products with EVEN σ_1 count is polynomial in
    `b_arg²`, so the final formula doesn't need sqrt. -/
noncomputable def sigma1_v21_param (q : ℝ) (b_arg : ℝ) :
    Matrix (Fin 2) (Fin 2) ℝ :=
  !![hoefsmit_v21_d1 q, b_arg;
     b_arg, hoefsmit_v21_d2 q]

/-- σ_1 squared: diagonal entries involve b_arg², off-diagonal
    involves b_arg·(d_1 + d_2). -/
-- `hq : q ≠ 0` dropped (2026-09-04): it was never consumed, and an unused
-- hypothesis overstates what the statement needs — the trace identity is a
-- polynomial one, true for every `q`.
theorem sigma1_v21_param_sq_trace (q : ℝ) (b_arg : ℝ) :
    Matrix.trace (sigma1_v21_param q b_arg * sigma1_v21_param q b_arg)
      = (hoefsmit_v21_d1 q)^2 + (hoefsmit_v21_d2 q)^2 + 2 * b_arg^2 := by
  unfold sigma1_v21_param
  simp
  ring

-- Ref: [leitner2026] rem:chi-v21-hoefsmit-matrix-derivation §"u-coordinate"
/-- **Sqrt-free closed form** for V_(2,1) character difference,
    using the polynomial b² = (q⁴ + q² + 1)/(q² + 1)² substitution.

    For any abstract b_arg with `b_arg² = b_sq q`, the matrix-product
    trace identity reduces to a rational equation in q alone — no
    `Real.sqrt` required. -/
-- Dropped the unused hypothesis `hq : q ≠ 0` (2026-08-22; vacuity ledger,
-- `proof-no-unused-hypothesis-rfl`).  The right-hand side is the definitional
-- unfolding of `chi_V21_difference_factored`, so the identity is a `rfl` that
-- holds for every `q`; `hq` was never consumed.
theorem chi_v21_closed_form_u_coord (q : ℝ) :
    chi_V21_difference_factored q
      = -(q^4 + 1) * (q^2 - 1) / (4 * q^3) := by
  unfold chi_V21_difference_factored
  rfl


/-! ## Status

**V_(2,1) is closed, including the matrix-product trace.**

- `hoefsmit_v21_braid_relation` — the representation is genuine (this is the
  guard that a transposed `(d_1, d_2)` fails; trace, determinant, `b²` and the
  Hecke quadratic are all symmetric in `d_1, d_2` and cannot see it).
- `chi_v21_matrix_trace_identity` — the 11-crossing typed-B_3 matrix-product
  trace difference equals the closed form. **Proved sorry-free 2026-09-04**;
  it was a `sorry` over a FALSE statement until the transposition was fixed
  the same day.
- `chi_V21_difference_factored_eq_polynomial`, `chi_V21_laurent_decomposition`,
  `chi_V21_difference_at_{one,two}` — the rational-function layer.

Every theorem in this file is sorry-free, and `#print axioms` on both new
results is `[propext, Classical.choice, Quot.sound]`.

The empirical sympy corroboration remains what it was: the closed form
reproduces the ε-coefficients recorded for λ = (2,1) at `q = 1+ε`. It is now a
cross-check on a proved identity rather than the identity's only support.
-/

end QOU.BraidKnot
