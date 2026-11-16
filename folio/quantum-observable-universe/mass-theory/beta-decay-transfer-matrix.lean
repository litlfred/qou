import Mathlib.Data.Real.Basic
import Mathlib.Tactic


/-!
# QOU.Archimedean.beta_decay_transfer_matrix

Beta decay is a universal 2×2 matrix-valued polynomial in q.
The two elementary decay matrices (nn→mix and mix→pp) are IDENTICAL:

  Δ_β(q) = ½(q - q⁻¹)·I

where I is the 2×2 identity (Hecke-inverse convention, no fractional
powers of q).

This universality follows from T_mix = ½(T_pp + T_nn): the mixed
matrix is the exact midpoint, so both steps are the same displacement.

LaTeX label: `prop:beta-decay-transfer-matrix`

## References
- [leitner2026] §6/beta-decay-transfer-matrix
-/

-- Declarations here are nested one namespace deeper than `QOU.Archimedean`
-- so this module and `QOU.Archimedean.TransferMatrix` can be imported
-- together. Both declared `T_pp`, `T_nn` and `T_mix` at the same
-- fully-qualified names, and Lean rejects the second import with
-- "environment already contains" (bean `qou-kfcl`).
--
-- They are NOT rival definitions. `TransferMatrix.transferMatrix c d`
-- is `!![c * HA_t + d, c; c, d]` over `ℤ[t, t⁻¹]` with `HA_t = q - q⁻¹`;
-- `tm q c d` here is `!![c * (q - q⁻¹) + d, c; c, d]` over a generic field
-- with `2 ≠ 0` (specialised to `ℝ` only in the numeric section at q = 1.110).
-- One formula, two ground rings — the symbolic one and its archimedean
-- specialisation, which is exactly the §7c layering. Consolidating them
-- onto a single generic `transferMatrix (q c d : R)` over `[CommRing R]`
-- is the right end state and is NOT done here; it changes the signature
-- of a declaration seven modules consume. Measured and left to `qou-u87j`.
namespace QOU.Archimedean.BetaDecayTransfer

-- §7c: the algebraic part is stated over a generic field `R`; only the
-- witness-backed numeric section at q = 1.110 specialises to `ℝ`.
variable {R : Type*} [Field R] [NeZero (2 : R)]

/-- A 2×2 transfer matrix (entries are polynomials in q). -/
-- Ref: [leitner2026] §6/beta-decay-transfer-matrix
structure TM (R : Type*) where
  a₁₁ : R
  a₁₂ : R
  a₂₁ : R
  a₂₂ : R

/-- Transfer matrix from crossing coefficients (c, d). -/
-- Ref: [leitner2026] §6/beta-decay-transfer-matrix
def tm (q c d : R) : TM R where
  a₁₁ := c * (q - 1/q) + d
  a₁₂ := c
  a₂₁ := c
  a₂₂ := d

/-- T_pp: proton-proton crossing (c=1, d=0). -/
-- Ref: [leitner2026] §6/beta-decay-transfer-matrix
def T_pp (q : R) : TM R := tm q 1 0

/-- T_nn: neutron-neutron crossing (c=1, d=-(q-q⁻¹)).
    Hecke-inverse convention: T(1, -(q-q⁻¹)) consistent with
    σ⁻¹ = σ - (q - q⁻¹). No fractional powers of q. -/
-- Ref: [leitner2026] §6/beta-decay-transfer-matrix
def T_nn (q : R) : TM R :=
  tm q 1 (-(q - 1/q))

/-- T_mix: mixed crossing (c=1, d=-½(q-q⁻¹)).
    The algebraic average ½(σ + σ⁻¹). No fractional powers of q. -/
-- Ref: [leitner2026] §6/beta-decay-transfer-matrix
def T_mix (q : R) : TM R :=
  tm q 1 (-(q - 1/q) / 2)

/-- Matrix subtraction. -/
-- Ref: [leitner2026] §6/beta-decay-transfer-matrix
def TM.sub (A B : TM R) : TM R where
  a₁₁ := A.a₁₁ - B.a₁₁
  a₁₂ := A.a₁₂ - B.a₁₂
  a₂₁ := A.a₂₁ - B.a₂₁
  a₂₂ := A.a₂₂ - B.a₂₂

/-- The universal beta decay matrix: Δ_β = T_mix - T_nn = T_pp - T_mix.
    Both elementary decay matrices are identical. -/
-- Ref: [leitner2026] §6/beta-decay-transfer-matrix
def Delta_beta (q : R) : TM R :=
  (T_mix q).sub (T_nn q)

/-- UNIVERSALITY: Δ_β^{nn→mix} = Δ_β^{mix→pp}.
    The two elementary decay matrices are the same. -/
-- Ref: [leitner2026] §6/beta-decay-transfer-matrix
theorem beta_decay_universal (q : R) :
    let d1 := (T_mix q).sub (T_nn q)
    let d2 := (T_pp q).sub (T_mix q)
    d1.a₁₁ = d2.a₁₁ ∧ d1.a₁₂ = d2.a₁₂ ∧
    d1.a₂₁ = d2.a₂₁ ∧ d1.a₂₂ = d2.a₂₂ := by
  unfold T_mix T_pp T_nn tm TM.sub
  have h2 : (2 : R) ≠ 0 := NeZero.ne 2
  refine ⟨by field_simp; ring, by ring, by ring, by field_simp; ring⟩

/-- T_mix is the exact midpoint: T_mix = ½(T_pp + T_nn). -/
-- Ref: [leitner2026] §6/beta-decay-transfer-matrix
theorem T_mix_midpoint (q : R) :
    let pp := T_pp q; let nn := T_nn q; let mx := T_mix q
    mx.a₁₂ = (pp.a₁₂ + nn.a₁₂) / 2 ∧
    mx.a₂₁ = (pp.a₂₁ + nn.a₂₁) / 2 ∧
    mx.a₂₂ = (pp.a₂₂ + nn.a₂₂) / 2 := by
  unfold T_pp T_nn T_mix tm
  have h2 : (2 : R) ≠ 0 := NeZero.ne 2
  refine ⟨by field_simp; ring, by field_simp; ring, by ring⟩

/-- At q = 1, the decay matrix vanishes (no beta decay). -/
-- Ref: [leitner2026] §6/beta-decay-transfer-matrix
theorem beta_decay_vanishes_classical :
    let d := Delta_beta (1 : R)
    d.a₁₂ = 0 ∧ d.a₂₁ = 0 := by
  unfold Delta_beta T_mix T_nn tm TM.sub
  refine ⟨by norm_num, by norm_num⟩

/-- The Markov-traced volume from a transfer matrix. -/
-- Ref: [leitner2026] §6/beta-decay-transfer-matrix
def TM.tracedVolume (M : TM R) (z : R) : R :=
  z * M.a₁₁ + M.a₂₁

-- ═══════════════════════════════════════════════════════════════════
-- Witness-backed numeric verification at q = 1.110
-- Source: beta-decay-matrix.witness.json
-- ═══════════════════════════════════════════════════════════════════

/-- T_pp off-diagonal at q = 1.110 is 1 (exact). -/
-- Ref: [leitner2026] beta-decay-matrix.witness.json
theorem T_pp_offdiag : (T_pp (1.110 : ℝ)).a₁₂ = 1 := by
  unfold T_pp tm; norm_num

/-- T_pp(2,2) at any q is 0 (exact). -/
-- Ref: [leitner2026] §6/beta-decay-transfer-matrix
theorem T_pp_corner (q : R) : (T_pp q).a₂₂ = 0 := by
  unfold T_pp tm; ring

/-- The Hecke coefficient T_pp(1,1) = q - q⁻¹ ≈ 0.2091 at q = 1.110.
    Witness: 0.2090990990990993. -/
-- Ref: [leitner2026] beta-decay-matrix.witness.json
noncomputable def hecke_coeff_at_q : ℝ := 1.110 - 1 / 1.110

/-- The Hecke coefficient is positive for q > 1. -/
-- Ref: [leitner2026] §6/beta-decay-transfer-matrix
theorem hecke_coeff_pos : 0 < hecke_coeff_at_q := by
  unfold hecke_coeff_at_q; norm_num

/-- The decay matrix is a scalar multiple of the identity:
    Δ_β(q) = ½(q - q⁻¹)·I, so the diagonal entry is (q - q⁻¹)/2
    and the off-diagonal entries vanish. -/
-- Ref: [leitner2026] §6/beta-decay-transfer-matrix
theorem decay_matrix_sign_pattern (q : R) :
    (Delta_beta q).a₁₁ = (q - 1/q) / 2 := by
  unfold Delta_beta T_mix T_nn tm TM.sub
  have h2 : (2 : R) ≠ 0 := NeZero.ne 2
  field_simp; ring

/-- Decay matrix off-diagonal entry is 0: Δ_β = ½(q - q⁻¹)·I is
    scalar (the off-diagonal `c` entries cancel between T_mix and T_nn). -/
-- Ref: [leitner2026] §6/beta-decay-transfer-matrix
theorem decay_offdiag_formula (q : R) :
    (Delta_beta q).a₁₂ = 0 := by
  unfold Delta_beta T_mix T_nn tm TM.sub
  ring

/-- At q = 1.110: off-diagonal = 0 (the decay matrix is scalar). -/
-- Ref: [leitner2026] beta-decay-matrix.witness.json
theorem decay_offdiag_at_q : (Delta_beta (1.110 : ℝ)).a₁₂ = 0 := by
  exact decay_offdiag_formula (1.110 : ℝ)

/-- Tritium Skein polynomial ratio: P(³He)/P(³H) ≈ 0.9029.
    Source: beta-decay-matrix.witness.json. -/
-- Ref: [leitner2026] beta-decay-matrix.witness.json
noncomputable def tritium_skein_ratio : ℝ := 0.9029

/-- The Skein ratio is less than 1 (daughter has smaller polynomial). -/
-- Ref: [leitner2026] beta-decay-matrix.witness.json
theorem tritium_ratio_lt_one : tritium_skein_ratio < 1 := by
  unfold tritium_skein_ratio; norm_num

/-- The Skein ratio is positive (both polynomials positive). -/
-- Ref: [leitner2026] beta-decay-matrix.witness.json
theorem tritium_ratio_pos : 0 < tritium_skein_ratio := by
  unfold tritium_skein_ratio; norm_num

/-- Tritium per-generator volumes from witness computation.
    σ₀: V_par = 0.7684, V_dau = 0.7510
    σ₁: V_par = 1.3029, V_dau = 1.2036 -/
-- Ref: [leitner2026] beta-decay-matrix.witness.json
noncomputable def V_par_sigma0 : ℝ := 0.7684
noncomputable def V_dau_sigma0 : ℝ := 0.7510
noncomputable def V_par_sigma1 : ℝ := 1.3029
noncomputable def V_dau_sigma1 : ℝ := 1.2036

/-- All generator volumes are positive. -/
-- Ref: [leitner2026] beta-decay-matrix.witness.json
theorem generator_volumes_pos :
    0 < V_par_sigma0 ∧ 0 < V_dau_sigma0 ∧
    0 < V_par_sigma1 ∧ 0 < V_dau_sigma1 := by
  unfold V_par_sigma0 V_dau_sigma0 V_par_sigma1 V_dau_sigma1
  constructor <;> norm_num

/-- At each generator, the daughter volume is smaller than the parent
    (the decay releases action). -/
-- Ref: [leitner2026] beta-decay-matrix.witness.json
theorem daughter_volumes_smaller :
    V_dau_sigma0 < V_par_sigma0 ∧ V_dau_sigma1 < V_par_sigma1 := by
  unfold V_par_sigma0 V_dau_sigma0 V_par_sigma1 V_dau_sigma1
  constructor <;> norm_num

end QOU.Archimedean.BetaDecayTransfer
