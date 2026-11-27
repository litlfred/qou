import Mathlib.Data.Matrix.Basic
import Mathlib.Tactic

/-!
# QOU.ParticleInteractions.transfer_matrix_identities

Canonical Lean formalization for content block
[`prop:transfer-matrix-identities`](../../../quantum-observable-universe/mass-theory/transfer-matrix-identities.md):
*Transfer matrix identities: $T_{pp}T_{nn} = I$ and $T_{pn}^2 = [2]_q^2/4 \cdot I$*.

Per `prop:beta-decay-transfer-matrix`
(`mass-theory/beta-decay-transfer-matrix.md`), each nucleon pair
contributes a crossing transfer matrix

  `T(c, d) = !![c·(q − q⁻¹) + d, c; c, d]`

with crossing coefficients `(c, d)` depending on the pair type:

  `T_pp = T(1, 0)`,
  `T_nn = T(1, −(q − q⁻¹))`,
  `T_pn = T(1, −(q − q⁻¹)/2)`  (the mixed crossing `½(σ + σ⁻¹)`).

This file **proves** the two identities of the proposition over a
generic field `K` (AGENTS.md §7c base-ring rule — the identities are
purely algebraic; no ordering or square root is used):

* **(i)** `T_pp * T_nn = 1` and `T_nn * T_pp = 1` — these hold for
  every `q : K` (they are ring identities in `h = q − q⁻¹`).
* **(ii)** `T_pn * T_pn = ((q + q⁻¹)^2 / 4) • 1` — requires `q ≠ 0`
  (so `q·q⁻¹ = 1`, giving `1 + (q − q⁻¹)²/4 = (q + q⁻¹)²/4`) and
  `(2 : K) ≠ 0` (the mixed crossing has half-integer coefficients).

Supporting lemmas record the corollary facts stated in the `.md`:
`det T_pp = det T_nn = −1` (unimodularity, forced by the Hecke
eigenvalues `q·(−q⁻¹) = −1`), `trace T_pn = 0`, and
`det T_pn = −(1 + (q − q⁻¹)²/4)`.

The `lean.ref` URI `qou:QOU.ParticleInteractions.transfer_matrix_identities`
resolves to the bundled theorem `transfer_matrix_identities` below.
-/

namespace QOU.ParticleInteractions

open Matrix

variable {K : Type*} [Field K]

/-- General crossing transfer matrix
`T(c, d) = !![c·(q − q⁻¹) + d, c; c, d]` of
`prop:beta-decay-transfer-matrix`, over a generic field `K`. -/
def transferMatrix (q c d : K) : Matrix (Fin 2) (Fin 2) K :=
  !![c * (q - q⁻¹) + d, c; c, d]

/-- Proton–proton crossing transfer matrix `T_pp = T(1, 0)`. -/
def T_pp (q : K) : Matrix (Fin 2) (Fin 2) K :=
  transferMatrix q 1 0

/-- Neutron–neutron crossing transfer matrix `T_nn = T(1, −(q − q⁻¹))` —
the unique convention consistent with the Hecke inverse relation
`σ⁻¹ = σ − (q − q⁻¹)`. -/
def T_nn (q : K) : Matrix (Fin 2) (Fin 2) K :=
  transferMatrix q 1 (-(q - q⁻¹))

/-- Mixed (proton–neutron) crossing transfer matrix
`T_pn = T(1, −(q − q⁻¹)/2)`, from the algebraic average
`½(σ + σ⁻¹)` of the two Hecke crossings. -/
def T_pn (q : K) : Matrix (Fin 2) (Fin 2) K :=
  transferMatrix q 1 (-((q - q⁻¹) / 2))

/-- **Identity (i), left factor**: `T_pp · T_nn = I`.  A ring identity
in `h = q − q⁻¹` — no hypothesis on `q` is needed. -/
theorem T_pp_mul_T_nn (q : K) : T_pp q * T_nn q = 1 := by
  unfold T_pp T_nn transferMatrix
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [Matrix.mul_apply, Fin.sum_univ_two]

/-- **Identity (i), right factor**: `T_nn · T_pp = I`. -/
theorem T_nn_mul_T_pp (q : K) : T_nn q * T_pp q = 1 := by
  unfold T_pp T_nn transferMatrix
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [Matrix.mul_apply, Fin.sum_univ_two]

/-- **Identity (ii)**: `T_pn² = ([2]_q²/4) · I` with `[2]_q = q + q⁻¹`.
The diagonal entry is `1 + (q − q⁻¹)²/4 = (q + q⁻¹)²/4` (using
`q·q⁻¹ = 1`), and the off-diagonal entries cancel:
`(h/2)·1 + 1·(−h/2) = 0`. -/
theorem T_pn_sq (q : K) (hq : q ≠ 0) (h2 : (2 : K) ≠ 0) :
    T_pn q * T_pn q = ((q + q⁻¹) ^ 2 / 4) • (1 : Matrix (Fin 2) (Fin 2) K) := by
  have h4 : (4 : K) ≠ 0 := by
    have : (4 : K) = 2 * 2 := by norm_num
    rw [this]; exact mul_ne_zero h2 h2
  unfold T_pn transferMatrix
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [Matrix.mul_apply, Matrix.smul_apply,
          Fin.sum_univ_two, smul_eq_mul] <;>
    field_simp <;>
    ring

/-- Unimodularity of the pp crossing: `det T_pp = −1` (forced by the
Hecke eigenvalues `q·(−q⁻¹) = −1`). -/
theorem T_pp_det (q : K) : (T_pp q).det = -1 := by
  unfold T_pp transferMatrix
  simp [Matrix.det_fin_two_of]

/-- Unimodularity of the nn crossing: `det T_nn = −1`. -/
theorem T_nn_det (q : K) : (T_nn q).det = -1 := by
  unfold T_nn transferMatrix
  simp [Matrix.det_fin_two_of]

/-- The mixed crossing is traceless: `trace T_pn = 0`.  Needs
`(2 : K) ≠ 0` — in characteristic 2 the half-integer coefficients of
the mixed crossing collapse and the trace is `q − q⁻¹` instead. -/
theorem T_pn_trace (q : K) (h2 : (2 : K) ≠ 0) : (T_pn q).trace = 0 := by
  unfold T_pn transferMatrix
  simp [Matrix.trace_fin_two_of]
  field_simp
  ring_nf

/-- The mixed crossing is not unimodular:
`det T_pn = −(1 + (q − q⁻¹)²/4)` — the algebraic average `½(σ + σ⁻¹)`
is not a group element.  Needs `(2 : K) ≠ 0`. -/
theorem T_pn_det (q : K) (h2 : (2 : K) ≠ 0) :
    (T_pn q).det = -(1 + (q - q⁻¹) ^ 2 / 4) := by
  have h4 : (4 : K) ≠ 0 := by
    have : (4 : K) = 2 * 2 := by norm_num
    rw [this]; exact mul_ne_zero h2 h2
  unfold T_pn transferMatrix
  simp [Matrix.det_fin_two_of]
  field_simp
  ring

/-- **Transfer matrix identities** (`prop:transfer-matrix-identities`):

**(i)** `T_pp · T_nn = T_nn · T_pp = I`;

**(ii)** `T_pn² = ([2]_q²/4) · I` where `[2]_q = q + q⁻¹`.

Stated over a generic field `K` with `q ≠ 0` and `(2 : K) ≠ 0`
(AGENTS.md §7c). This is the declaration resolved by the block's
`lean.ref` URI `qou:QOU.ParticleInteractions.transfer_matrix_identities`. -/
theorem transfer_matrix_identities (q : K) (hq : q ≠ 0) (h2 : (2 : K) ≠ 0) :
    (T_pp q * T_nn q = 1 ∧ T_nn q * T_pp q = 1) ∧
      T_pn q * T_pn q = ((q + q⁻¹) ^ 2 / 4) • (1 : Matrix (Fin 2) (Fin 2) K) :=
  ⟨⟨T_pp_mul_T_nn q, T_nn_mul_T_pp q⟩, T_pn_sq q hq h2⟩

end QOU.ParticleInteractions
