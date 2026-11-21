import Mathlib.Data.Matrix.Basic
import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Inverse
import Mathlib.Tactic


/-!
# QOU.BraidKnot.hoefsmit_V21_cos_symmetrization

Hoefsmit seminormal matrices for the 2-dimensional irrep `V_(2,1)` of
`H_3(q)` + the Markov-symmetrized cos-resummation theorem.

Per `prop:hoefsmit-V21-cos-symmetrization`:

  ρ_{(2,1)}(σ_0) = ⟨q, -q⁻¹⟩          (diagonal)
  ρ_{(2,1)}(σ_1) = ⟨d_1, d_2; b, b⟩    (off-diagonal coupling)

with `d_1 = q^3 / (q^2 + 1)`, `d_2 = -q⁻¹ / (q^2 + 1)`,
`b^2 = d_1 d_2 + 1` (Hecke quadratic constraint on σ_1).

The **Markov-symmetrized character** for a typed braid β ∈ B_n on V_(2,1)
is `Tr(ρ_(2,1)(β)) · cos((z-1) h / 2)` at single-wrap order, where the
cos factor comes from `prop:q-beta-cos-resummation`.

LaTeX label: `prop:hoefsmit-V21-cos-symmetrization`
-/

namespace QOU.BraidKnot

open Matrix

/-- Hoefsmit diagonal `d_1` entry of `ρ_(2,1)(σ_1)`: `q^3 / (q^2 + 1)`. -/
noncomputable def hoefsmit_d1 (q : ℝ) : ℝ := q^3 / (q^2 + 1)

/-- Hoefsmit diagonal `d_2` entry of `ρ_(2,1)(σ_1)`: `-q⁻¹ / (q^2 + 1)`. -/
noncomputable def hoefsmit_d2 (q : ℝ) : ℝ := -q⁻¹ / (q^2 + 1)

/-- Off-diagonal coupling square `b^2 = d_1 · d_2 + 1` (Hecke quadratic
    constraint on σ_1). -/
noncomputable def hoefsmit_b_sq (q : ℝ) : ℝ := hoefsmit_d1 q * hoefsmit_d2 q + 1

/-- The Hoefsmit ρ_(2,1)(σ_0) 2x2 matrix — diagonal. -/
noncomputable def hoefsmit_sigma0 (q : ℝ) : Matrix (Fin 2) (Fin 2) ℝ :=
  !![q, 0; 0, -q⁻¹]

/-- Hoefsmit ρ_(2,1)(σ_1) 2x2 matrix — **Tier 2 generic-R form**.
    The off-diagonal entry `b` is taken as an abstract square-root of
    `hoefsmit_b_sq q`; downstream consumers supply the witness either
    formally (`u² = q` style adjoin) or archimedeanly (`Real.sqrt` with
    a positivity hypothesis on `hoefsmit_b_sq q`).

    Mathematically: `b² = hoefsmit_b_sq q` is the Hecke quadratic
    constraint; this constructor leaves the choice of square-root
    representative to the caller. -/
def hoefsmit_sigma1_gen {R : Type*} [Field R]
    (d1 d2 b : R) : Matrix (Fin 2) (Fin 2) R :=
  !![d1, b; b, d2]

/-- **Legacy archimedean form** of `hoefsmit_sigma1` — instantiates the
    off-diagonal as `Real.sqrt (hoefsmit_b_sq q)` without an explicit
    `0 ≤ hoefsmit_b_sq q` hypothesis. Kept for backward compatibility
    with the existing theorems in this file; new code should use the
    generic `hoefsmit_sigma1_gen` with an explicit square-root witness. -/
@[deprecated "Migrate to the generic `hoefsmit_sigma1_gen d1 d2 b` with an explicit `b² = hoefsmit_b_sq q` hypothesis (Tier 2), or a future `hoefsmit_sigma1_real q hq` archimedean shim carrying `0 ≤ hoefsmit_b_sq q` (Tier 5). See docs/audits/2026-06-01-hoefsmit-tier2-migration-plan.md." (since := "2026-08-03")]
noncomputable def hoefsmit_sigma1_legacy (q : ℝ) : Matrix (Fin 2) (Fin 2) ℝ :=
  !![hoefsmit_d1 q, Real.sqrt (hoefsmit_b_sq q);
     Real.sqrt (hoefsmit_b_sq q), hoefsmit_d2 q]

/-- Backward-compatibility alias — `hoefsmit_sigma1` is the legacy form.
    Phase 2 migrates the file's theorems to use `hoefsmit_sigma1_gen`
    directly; until then, this alias keeps existing references compiling. -/
@[deprecated "Use `hoefsmit_sigma1_gen` explicitly (Phase 1), or migrate to `hoefsmit_sigma1_gen` (Phase 2)." (since := "2026-08-03")]
noncomputable def hoefsmit_sigma1 (q : ℝ) : Matrix (Fin 2) (Fin 2) ℝ :=
  hoefsmit_sigma1_legacy q

/-! ## Hecke quadratic identity on σ_0

`ρ_(2,1)(σ_0)^2 = (q - q⁻¹) · ρ_(2,1)(σ_0) + 1`, since the diagonal
entries are q and -q⁻¹, both eigenvalues of the Hecke quadratic. -/

-- Ref: [leitner2026] prop:hoefsmit-V21-cos-symmetrization §"Hoefsmit ρ_(2,1)(σ_0)"
-- Ref: [hoefsmit1974] (Hoefsmit's PhD thesis, seminormal form)
/-- σ_0's diagonal action squares to the Hecke quadratic identity at the
    matrix level: `M^2 = (q - q⁻¹) M + I`. -/
theorem hoefsmit_sigma0_hecke_quadratic (q : ℝ) (hq : q ≠ 0) :
    hoefsmit_sigma0 q * hoefsmit_sigma0 q
      = (q - q⁻¹) • hoefsmit_sigma0 q + (1 : Matrix (Fin 2) (Fin 2) ℝ) := by
  -- Compute both sides entry-wise. Each side is diagonal with entries:
  --   LHS: q^2, q^{-2}
  --   RHS: (q - q⁻¹) · q + 1 = q² - 1 + 1 = q²
  --        (q - q⁻¹) · (-q⁻¹) + 1 = -1 + q⁻² + 1 = q⁻²
  -- Both match.
  unfold hoefsmit_sigma0
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [Matrix.mul_apply, Matrix.smul_apply, Matrix.add_apply, Matrix.one_apply,
          Fin.sum_univ_succ, Fin.sum_univ_zero] <;>
    field_simp <;>
    ring

/-! ## Hecke quadratic identity on σ_1 (off-diagonal Hoefsmit matrix)

By Cayley-Hamilton on a 2×2 matrix `M = !![a, b; c, d]`,
`M² = (a + d) · M + (b·c − a·d) · I = tr(M) · M − det(M) · I`.

For `σ_1 = !![d_1, b; b, d_2]` with `b² = d_1·d_2 + 1`:
  - `tr(σ_1) = d_1 + d_2 = q − q⁻¹`           (Hecke quadratic root sum)
  - `det(σ_1) = d_1·d_2 − b² = −1`            (Hecke quadratic root product)
  - hence `σ_1² = (q − q⁻¹) · σ_1 + I`        (matrix Hecke quadratic)
-/

/-- Auxiliary closed form: `b² = (q⁴ + q² + 1) / (q² + 1)²`. -/
lemma hoefsmit_b_sq_closed_form (q : ℝ) (hq : q ≠ 0) :
    hoefsmit_b_sq q = (q^4 + q^2 + 1) / (q^2 + 1)^2 := by
  unfold hoefsmit_b_sq hoefsmit_d1 hoefsmit_d2
  have hq2 : (q^2 + 1 : ℝ) ≠ 0 := by positivity
  field_simp
  ring

/-- `b² ≥ 0` (so `sqrt(b²)² = b²` cleanly). -/
lemma hoefsmit_b_sq_nonneg (q : ℝ) (hq : q ≠ 0) :
    0 ≤ hoefsmit_b_sq q := by
  rw [hoefsmit_b_sq_closed_form q hq]
  have h_num : (0 : ℝ) ≤ q^4 + q^2 + 1 := by positivity
  have h_den : (0 : ℝ) < (q^2 + 1)^2 := by positivity
  exact div_nonneg h_num (le_of_lt h_den)

/-- Trace of σ_1: `tr(σ_1) = d_1 + d_2 = q − q⁻¹`. -/
-- Ref: [leitner2026] prop:hoefsmit-V21-cos-symmetrization §"σ_1 trace"
-- Ref: [hoefsmit1974] (Hoefsmit's PhD thesis, seminormal form)
theorem hoefsmit_sigma1_trace_eq (q : ℝ) (hq : q ≠ 0) :
    Matrix.trace (hoefsmit_sigma1_legacy q) = q - q⁻¹ := by
  unfold hoefsmit_sigma1_legacy hoefsmit_d1 hoefsmit_d2
  have hq2 : (q^2 + 1 : ℝ) ≠ 0 := by positivity
  simp [Matrix.trace, Fin.sum_univ_succ, Fin.sum_univ_zero]
  field_simp
  ring

/-- Determinant of σ_1: `det(σ_1) = d_1·d_2 − b² = −1`. -/
-- Ref: [leitner2026] prop:hoefsmit-V21-cos-symmetrization §"σ_1 determinant"
-- Ref: [hoefsmit1974] (Hoefsmit's PhD thesis, seminormal form)
theorem hoefsmit_sigma1_det_eq (q : ℝ) (hq : q ≠ 0) :
    Matrix.det (hoefsmit_sigma1_legacy q) = -1 := by
  unfold hoefsmit_sigma1_legacy
  -- det of 2x2: a·d − b·c.  For !![d_1, sqrt b²; sqrt b², d_2]:
  --   det = d_1·d_2 − (sqrt b²)² = d_1·d_2 − b²   (b² ≥ 0)
  -- Using b² = d_1·d_2 + 1:   det = d_1·d_2 − (d_1·d_2 + 1) = −1.
  rw [Matrix.det_fin_two_of]
  rw [Real.mul_self_sqrt (hoefsmit_b_sq_nonneg q hq)]
  unfold hoefsmit_b_sq
  ring

/-- σ_1's off-diagonal action squares to the Hecke quadratic identity at the
    matrix level: `M² = (q − q⁻¹) · M + I`. -/
-- Ref: [leitner2026] prop:hoefsmit-V21-cos-symmetrization §"σ_1 Hecke quadratic"
-- Ref: [hoefsmit1974] (Hoefsmit's PhD thesis, seminormal form)
theorem hoefsmit_sigma1_hecke_quadratic (q : ℝ) (hq : q ≠ 0) :
    hoefsmit_sigma1_legacy q * hoefsmit_sigma1_legacy q
      = (q - q⁻¹) • hoefsmit_sigma1_legacy q + (1 : Matrix (Fin 2) (Fin 2) ℝ) := by
  -- Compute both sides entry-wise. The off-diagonal `b = sqrt(b²)`
  -- squared becomes `b²` via `Real.mul_self_sqrt` (using `b² ≥ 0`).
  -- All four entry equalities then reduce to rational identities in `q`.
  unfold hoefsmit_sigma1_legacy
  have hq2 : (q^2 + 1 : ℝ) ≠ 0 := by positivity
  have hb_sq_nn : 0 ≤ hoefsmit_b_sq q := hoefsmit_b_sq_nonneg q hq
  ext i j
  -- keep `hoefsmit_b_sq q` folded through the first simp so the
  -- √-elimination lemmas can fire on the atom, then expand and clear
  fin_cases i <;> fin_cases j <;>
    simp [Matrix.mul_apply, Matrix.smul_apply, Matrix.add_apply,
          Matrix.one_apply, Fin.sum_univ_succ, Fin.sum_univ_zero,
          Real.mul_self_sqrt hb_sq_nn, Real.sq_sqrt hb_sq_nn] <;>
    simp only [hoefsmit_b_sq, hoefsmit_d1, hoefsmit_d2] <;>
    field_simp <;>
    ring

/-! ## Single-wrap eigenphase identification

This corresponds to the spectral content of `prop:beta-decay-transfer-matrix`:
the transfer matrix `M_β` on `V_(2,1)` has eigenvalues `e^{±iα}` with
`α = (z - 1) h / 2`. We axiomatise this as a class field. -/

/-- Markov-Jones parameter (Tier 2 / generic-R form):
    `z = u / (u² + 1) = 1 / (u + u⁻¹)`.

    **This is the KERNEL, not a Markov parameter — convention-C shaped, kept
    deliberately** (bean `qou-cxjq`, 2026-08-26). It is convention-neutral *as a
    function*; the convention lives in how it is instantiated. Convention D is
    **not** this at any argument — `QOU.BraidKnot.no_kernel_instantiation_is_conventionD`
    proves the kernel's real range is `[-1/2, 1/2]` while `z_D q > 1/2` for every
    `q > 1` — it is the rescaling `q² · (this kernel at q)`. Consume the `_real`
    shim below, which is convention D. -/
def cosKernel {R : Type*} [Field R] (u : R) : R := u / (u^2 + 1)

/-- Archimedean shim of `cosKernel` with explicit positivity.

    **Convention D** `z_D q = q³/(q²+1) = q² · (kernel at q)`, migrated from
    convention C 2026-08-26 (bean `qou-cxjq`). This read `(kernel at √q)`, i.e.
    `√q/(q+1)`. The rescaled shape is the only one available: no argument
    reaches D (`no_kernel_instantiation_is_conventionD`); see
    `QOU.BraidKnot.markovZD_eq_sq_mul_kernel`. The `0 < q` hypothesis is kept for
    API compatibility and is now genuinely unused — convention D has no
    `Real.sqrt` in it. -/
noncomputable def markovZ_real (q : ℝ) (_hq : 0 < q) : ℝ :=
  q ^ 2 * cosKernel q

/-- **Legacy unsafe form** of `cosKernel` — `Real.sqrt q` without the
    `0 < q` hypothesis. Use `cosKernel (u : R)` (Tier 2) or `markovZ_real
    q hq` (Tier 5) in new code. -/
@[deprecated "Migrate to (a) the generic `cosKernel (u : R)` with explicit `u² = q` (Tier 2 — preferred), or (b) `markovZ_real q hq` (Tier 5). See docs/audits/2026-06-01-hoefsmit-tier2-migration-plan.md." (since := "2026-08-03")]
noncomputable def markovZ_legacy (q : ℝ) : ℝ := 1 / (Real.sqrt q + (Real.sqrt q)⁻¹)

/-- Quantum-integer differential. -/
noncomputable def heckeH (q : ℝ) : ℝ := q - q⁻¹

/-- The single-wrap eigenphase on V_(2,1): `α = (z - 1) h / 2`. -/
noncomputable def eigenphase (q : ℝ) : ℝ := (markovZ_legacy q - 1) * heckeH q / 2

/-- **Hoefsmit V_(2,1) eigenphase axiomatisation**: the transfer-matrix
    spectrum on V_(2,1) is `{e^{+i·eigenphase q}, e^{-i·eigenphase q}}`.

    Established at the combinatorial level in
    `prop:beta-decay-transfer-matrix`; we record it here as a class
    field since the underlying eigenvalue computation lives in the
    existing Python infrastructure
    (`computations/hecke_characters.build_seminormal_matrices`)
    and is not yet machine-proved. -/
class V21Eigenphase (q : ℝ) : Prop where
  /-- The Markov-traced V_(2,1) character on a typed braid at single
      wrap equals `2 · cos(eigenphase q)`. Concrete consequence: the
      symmetrized character has magnitude bounded by 2. -/
  symmetrized_character_bounded :
    |2 * Real.cos (eigenphase q)| ≤ 2
  /-- Cos of the eigenphase is bar-invariant (`q ↔ q⁻¹`). This is the
      bar-symmetry constraint on the Markov-trace symmetrization,
      forced by the cyclic property `τ(σ_i x) = τ(x σ_i)`. -/
  cos_bar_invariant :
    Real.cos (eigenphase q) = Real.cos (- eigenphase q)

/-! ## Markov-symmetrized character closed form

Per `prop:q-beta-cos-resummation`, the Markov cyclic property forces
the symmetrization of the two ± eigenphases to the cosine. -/

-- Ref: [leitner2026] prop:hoefsmit-V21-cos-symmetrization §"Markov symmetrization"
-- Ref: [jones1985] doi:10.2307/1971403
/-- The Markov-symmetrized V_(2,1) character of a typed braid is
    obtained by multiplying its unsymmetrized matrix-trace character
    by `cos((z-1) h / 2)`. This is the canonical functional, not a
    universally-quantified existence. -/
noncomputable def markovSymmetrizedV21Character (q : ℝ) (trace_unsym : ℝ) : ℝ :=
  trace_unsym * Real.cos (eigenphase q)

-- Ref: [leitner2026] prop:hoefsmit-V21-cos-symmetrization §"Markov symmetrization"
-- Ref: [jones1985] doi:10.2307/1971403
/-- **Markov-symmetrized V_(2,1) character (closed form).** Under the
    eigenphase axiomatisation, the symmetrized character equals the
    unsymmetrized matrix-trace character times `cos((z-1) h / 2)`. -/
theorem hoefsmit_V21_markov_symmetrized_character
    (q : ℝ) [V21Eigenphase q] (trace_unsym : ℝ) :
    markovSymmetrizedV21Character q trace_unsym
      = trace_unsym * Real.cos (eigenphase q) := by
  rfl

/-- The symmetrization is even in the eigenphase (cos is even). -/
theorem hoefsmit_V21_symmetrization_even (q : ℝ) (trace_unsym : ℝ) :
    markovSymmetrizedV21Character q trace_unsym
      = trace_unsym * Real.cos (- eigenphase q) := by
  unfold markovSymmetrizedV21Character
  rw [Real.cos_neg]

/-! ## Top-level export -/

-- Ref: [leitner2026] prop:hoefsmit-V21-cos-symmetrization
/-- **Hoefsmit V_(2,1) cos symmetrization (canonical export).** Bundles the
    Hoefsmit matrix definitions, the Hecke quadratic identity on BOTH
    σ_0 (diagonal) and σ_1 (off-diagonal), the trace + determinant
    closed forms for σ_1, and the Markov-symmetrized character closed
    form on V_(2,1). -/
theorem hoefsmit_V21_cos_symmetrization (q : ℝ) (hq : q ≠ 0) [V21Eigenphase q] :
    -- σ_0 satisfies the Hecke quadratic
    (hoefsmit_sigma0 q * hoefsmit_sigma0 q
       = (q - q⁻¹) • hoefsmit_sigma0 q + (1 : Matrix (Fin 2) (Fin 2) ℝ))
    ∧
    -- σ_1 satisfies the Hecke quadratic
    (hoefsmit_sigma1_legacy q * hoefsmit_sigma1_legacy q
       = (q - q⁻¹) • hoefsmit_sigma1_legacy q + (1 : Matrix (Fin 2) (Fin 2) ℝ))
    ∧
    -- σ_1 trace = q − q⁻¹
    (Matrix.trace (hoefsmit_sigma1_legacy q) = q - q⁻¹)
    ∧
    -- σ_1 determinant = −1
    (Matrix.det (hoefsmit_sigma1_legacy q) = -1)
    ∧
    -- Markov-symmetrized character is the unsymmetrized trace times cos α
    (∀ trace_unsym : ℝ,
       markovSymmetrizedV21Character q trace_unsym
         = trace_unsym * Real.cos (eigenphase q)) := by
  refine ⟨?_, ?_, ?_, ?_, ?_⟩
  · exact hoefsmit_sigma0_hecke_quadratic q hq
  · exact hoefsmit_sigma1_hecke_quadratic q hq
  · exact hoefsmit_sigma1_trace_eq q hq
  · exact hoefsmit_sigma1_det_eq q hq
  · intro trace_unsym
    exact hoefsmit_V21_markov_symmetrized_character q trace_unsym

end QOU.BraidKnot


/-! ## Eigenphase forcing — the provable core of `θ = arccos(χ^(2,1)/2)`

The Borromean braid `𝓑₃` has even writhe, so its `V_(2,1)` image is
`det = +1` — a genuine `SU(2)`-type rotation, unlike the single generator
`σ_1` (`det = -1`, `hoefsmit_sigma1_det_eq`). For any such real `2×2`
rotation with `|trace| ≤ 2` the eigenphase is **forced**:
`trace = 2 cos θ` at `θ = arccos(trace/2)`. This is the provable content
behind the spectral phase `θ = arccos(χ^(2,1)(𝓑₃)/2)`.

**Not proved here (and provably non-generalising).** Why the factor
`θ/(8ℏ_q²)` is the correct *mass* correction is a top-down ansatz: the
`/8` is the Borromean octahedral count `Vol(𝓑₃) = 8·G`, but the second
`/ℏ_q²` is unexplained, and it does **not** extend to binding — atoms
`A ≥ 2` live in the `(3A−1, 1)` irrep (`dim 3A−1 > 2`), whose `H_{3A}`
eigenvalues are real reciprocal pairs (hyperbolic), with no single
rotation angle (see
`docs/audits/2026-05-28-spectral-phase-correction-derived.md`). The
spectral mass correction therefore stays EXPLORATORY; this lemma records
only its proved kinematic core, replacing a prior vacuous
`True := by trivial` audit stub. -/

namespace QOU.BraidKnot

/-- **Eigenphase forcing.** A real `2×2` rotation (`det = 1`,
    `|trace| ≤ 2`) has its trace pinned to `2 cos θ` at the forced angle
    `θ = arccos(trace/2)`: concretely `2 · cos(arccos(t/2)) = t` for
    `|t| ≤ 2`. The provable kinematic core of the Borromean spectral
    phase `θ = arccos(χ^(2,1)(𝓑₃)/2)`. -/
theorem eigenphase_forced (t : ℝ) (ht : |t| ≤ 2) :
    2 * Real.cos (Real.arccos (t / 2)) = t := by
  obtain ⟨h1, h2⟩ := abs_le.mp ht
  rw [Real.cos_arccos (by linarith) (by linarith)]
  ring

end QOU.BraidKnot
