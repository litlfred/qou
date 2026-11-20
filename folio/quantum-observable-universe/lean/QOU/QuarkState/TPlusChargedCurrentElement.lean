/-
# N3: the β-decay amplitude as a `T⁺` matrix element times a charged-current crossing

Bean `qou-99qc`, route N3 of 2026-11-20. Companion probe
`computations/probes/qbeta_n3/n3_tplus_matrix_element_probe.py`.

## Setting

Hadron side as in `IsospinRaisingRoundTrip.lean` (PR #8632, restated here so this file is
self-contained): the neutron weight space `W₋` (basis `udd, dud, ddu`) and the proton weight
space `W₊` (basis `duu, udu, uud`) of `V^{⊗3}`, with `σ₁, σ₂` restricted, and
`T⁺ = Δ²(E) : W₋ → W₊`, `T⁻ = Δ²(F) : W₊ → W₋`.

Lepton side: one quark strand crosses one lepton strand on `V ⊗ V` (basis `uu, ud, du, dd`;
lepton doublet `ν ↔ u`, `e ↔ d`). The weak insertion on that crossing is
`W − σ = −h·P_L`, `P_L = P₊ = (Ř + q⁻¹)/[2]` (`weakVertex_sub_letter`,
`WeakVertexLeftProjector.lean`, at `q > 1`).

## What is proved (generic `[Field K]`, no `ℝ`, no `sorry`)

* `Fd_eq_transpose`, `sm1_symm`, `sm2_symm`, `sp1_symm`, `sp2_symm`: under the standard form
  on the weight bases the Hecke generators are self-adjoint and `T⁻ = (T⁺)ᵀ`. So the pairing
  in which `⟨p|T⁺|n⟩` is read is the one the construction already carries.
* `tplus_norm_sq`: if `T⁻T⁺ v = λ v` then `‖T⁺ v‖² = λ ‖v‖²`. With `FE_quad` (#8632,
  `λ ∈ {[2]², 1}`) the normalised hadronic `|⟨p|T⁺|n⟩|²` is `1` on isospin `½` and `[2]²` on
  isospin `3/2`, independent of every invariant normalisation (forced).
* `hecke_energy_transport`: if `T⁺` intertwines `X₋` and `X₊` and `X₋ v = μ v`, then
  `X₊ (T⁺ v) = μ (T⁺ v)`. Every Hecke-built energy is the same on the neutron state and on its
  `T⁺` image, so **no `H₃` operator yields a nonzero `Q_β`** (scope (b), invariant: the
  intertwining `Eu_sm1`, `Eu_sm2`).
* `Pp_eigen`, `Pp_idem`: `P₊` is the `q`-line projector of `Ř`.
* `exchange_quark_left`, `exchange_quark_right`: the charge-exchange amplitude of `−h·P₊`
  (quark `d → u`, lepton `ν → e`, strand-following frame) is `−h q/[2]` when the quark
  strand is on the left and `−h q⁻¹/[2]` when it is on the right.
* `exchange_closed_left/right`: closed forms `−q(q²−1)/(q²+1)` and `−(q²−1)/(q(q²+1))`.
* `exchange_bar`: `q ↦ q⁻¹` sends the left amplitude to minus the right one.
* `exchange_vanish_iff`: the amplitude is `0` iff `h = 0` (classical limit).

## What is NOT proved / remains a choice

Which side the quark strand sits on (`q^{±1}`), whether the nucleon is the isospin-`½` or
the isospin-`3/2` component (the ruled `Δ_S` lives on `3/2`, `isospinHalf_deltaS`), the
current–current factorisation `M = ⟨p|T⁺|n⟩ · (lepton exchange)`, and any energy scale.
`Q_β` is not produced by this construction (see `hecke_energy_transport`).

-- Ref: [jimbo1986] https://doi.org/10.1007/BF00400222 (q-Schur–Weyl duality)
-/
import Mathlib.LinearAlgebra.Matrix.Trace
import Mathlib.Data.Matrix.Mul
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.FinCases
import Mathlib.Tactic.Ring

namespace QOU.QuarkState.TPlusChargedCurrentElement

open Matrix

variable {K : Type*} [Field K]

/-- `h = q − q⁻¹`. -/
def hh (q : K) : K := q - q⁻¹
/-- `[2] = q + q⁻¹`. -/
def b2 (q : K) : K := q + q⁻¹

/-! ## Hadron side (restated from `IsospinRaisingRoundTrip`) -/

/-- `σ₁` on `W₋`. -/
def sm1 (q : K) : Matrix (Fin 3) (Fin 3) K := !![0, 1, 0; 1, q - q⁻¹, 0; 0, 0, q]
/-- `σ₂` on `W₋`. -/
def sm2 (q : K) : Matrix (Fin 3) (Fin 3) K := !![q, 0, 0; 0, 0, 1; 0, 1, q - q⁻¹]
/-- `σ₁` on `W₊`. -/
def sp1 (q : K) : Matrix (Fin 3) (Fin 3) K := !![q - q⁻¹, 1, 0; 1, 0, 0; 0, 0, q]
/-- `σ₂` on `W₊`. -/
def sp2 (q : K) : Matrix (Fin 3) (Fin 3) K := !![q, 0, 0; 0, q - q⁻¹, 1; 0, 1, 0]
/-- `T⁺ = Δ²(E) : W₋ → W₊`. -/
def Eu (q : K) : Matrix (Fin 3) (Fin 3) K := !![0, 1, q; 1, 0, 1; q⁻¹, 1, 0]
/-- `T⁻ = Δ²(F) : W₊ → W₋`. -/
def Fd (q : K) : Matrix (Fin 3) (Fin 3) K := !![0, 1, q⁻¹; 1, 0, 1; q, 1, 0]

theorem Fd_eq_transpose (q : K) : Fd q = (Eu q)ᵀ := by
  ext i j; fin_cases i <;> fin_cases j <;> rfl

theorem sm1_symm (q : K) : (sm1 q)ᵀ = sm1 q := by
  ext i j; fin_cases i <;> fin_cases j <;> rfl
theorem sm2_symm (q : K) : (sm2 q)ᵀ = sm2 q := by
  ext i j; fin_cases i <;> fin_cases j <;> rfl
theorem sp1_symm (q : K) : (sp1 q)ᵀ = sp1 q := by
  ext i j; fin_cases i <;> fin_cases j <;> rfl
theorem sp2_symm (q : K) : (sp2 q)ᵀ = sp2 q := by
  ext i j; fin_cases i <;> fin_cases j <;> rfl

/-- **The hadronic norm is forced by the `T⁻T⁺` eigenvalue.** -/
theorem tplus_norm_sq (q lam : K) (v : Fin 3 → K)
    (hv : (Fd q * Eu q) *ᵥ v = lam • v) :
    (Eu q *ᵥ v) ⬝ᵥ (Eu q *ᵥ v) = lam * (v ⬝ᵥ v) := by
  have key : (Eu q *ᵥ v) ⬝ᵥ (Eu q *ᵥ v) = v ⬝ᵥ ((Fd q * Eu q) *ᵥ v) := by
    rw [Fd_eq_transpose, ← mulVec_mulVec, mulVec_transpose, dotProduct_comm v, ← dotProduct_mulVec]
  rw [key, hv, dotProduct_smul, smul_eq_mul]

/-- **No Hecke energy distinguishes `n` from `T⁺ n`.** -/
theorem hecke_energy_transport {n : Type*} [Fintype n] (E Xm Xp : Matrix n n K)
    (hint : E * Xm = Xp * E) (mu : K) (v : n → K) (hv : Xm *ᵥ v = mu • v) :
    Xp *ᵥ (E *ᵥ v) = mu • (E *ᵥ v) := by
  rw [mulVec_mulVec, ← hint, ← mulVec_mulVec, hv, mulVec_smul]

section Hadron
variable {q : K} (hq : q ≠ 0)
include hq

theorem Eu_sm1 : Eu q * sm1 q = sp1 q * Eu q := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [Eu, sm1, sp1, Matrix.mul_apply, Fin.sum_univ_three] <;> field_simp <;> ring

theorem Eu_sm2 : Eu q * sm2 q = sp2 q * Eu q := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [Eu, sm2, sp2, Matrix.mul_apply, Fin.sum_univ_three] <;> field_simp <;> ring

/-- Instance: the eigenvalue of `σ₁` on a neutron state is carried to the proton state. -/
theorem sigma1_energy_equal (mu : K) (v : Fin 3 → K) (hv : sm1 q *ᵥ v = mu • v) :
    sp1 q *ᵥ (Eu q *ᵥ v) = mu • (Eu q *ᵥ v) :=
  hecke_energy_transport _ _ _ (Eu_sm1 hq) mu v hv

/-- Instance for a word: `σ₁σ₂⁻¹`-type words are products, and intertwining is
multiplicative; shown here for the product `σ₁σ₂`. -/
theorem Eu_sm12 : Eu q * (sm1 q * sm2 q) = (sp1 q * sp2 q) * Eu q := by
  rw [← Matrix.mul_assoc, Eu_sm1 hq, Matrix.mul_assoc, Eu_sm2 hq, Matrix.mul_assoc]

end Hadron

/-! ## Lepton side: one quark–lepton crossing on `V ⊗ V` (basis `uu, ud, du, dd`) -/

/-- Jimbo `Ř` (columns = images): `ud ↦ du`, `du ↦ ud + h du`. -/
def Rc (q : K) : Matrix (Fin 4) (Fin 4) K :=
  !![q, 0, 0, 0; 0, 0, 1, 0; 0, 1, q - q⁻¹, 0; 0, 0, 0, q]

/-- `P₊ = (Ř + q⁻¹)/[2]`, the left line at `q > 1`. -/
def Pp (q : K) : Matrix (Fin 4) (Fin 4) K := (b2 q)⁻¹ • (Rc q + q⁻¹ • 1)

/-- The weak insertion `W − σ = −h·P_L`. -/
def ins (q : K) : Matrix (Fin 4) (Fin 4) K := -(hh q) • Pp q

section Lepton
variable {q : K} (hq : q ≠ 0) (hb : q ^ 2 + 1 ≠ 0)
include hq hb

theorem b2_ne : b2 q ≠ 0 := by
  unfold b2; intro h; apply hb
  have : q * (q + q⁻¹) = q ^ 2 + 1 := by field_simp
  rw [← this, h, mul_zero]

theorem Pp_eigen : Rc q * Pp q = q • Pp q := by
  have := b2_ne hq hb
  unfold Pp b2 at *
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [Rc, Matrix.mul_apply, Fin.sum_univ_four, Matrix.one_apply] <;> field_simp <;> ring

theorem Pp_idem : Pp q * Pp q = Pp q := by
  have := b2_ne hq hb
  unfold Pp b2 at *
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [Rc, Matrix.mul_apply, Fin.sum_univ_four, Matrix.one_apply] <;> field_simp <;> ring

/-- Quark on the left: input `du` (quark `d`, lepton `ν`); strand-following output with the
labels exchanged is again `du` in the position basis (lepton `e` now left, quark `u` right). -/
theorem exchange_quark_left : ins q 2 2 = -(hh q) * q / b2 q := by
  have := b2_ne hq hb
  simp [ins, Pp, Rc, hh, b2] at *
  field_simp; ring

/-- Quark on the right: input `ud` (lepton `ν`, quark `d`); exchanged output is `ud`. -/
theorem exchange_quark_right : ins q 1 1 = -(hh q) * q⁻¹ / b2 q := by
  have := b2_ne hq hb
  simp [ins, Pp, Rc, hh, b2] at *
  field_simp

theorem exchange_closed_left : -(hh q) * q / b2 q = -(q * (q ^ 2 - 1) / (q ^ 2 + 1)) := by
  unfold hh b2; field_simp

theorem exchange_closed_right :
    -(hh q) * q⁻¹ / b2 q = -((q ^ 2 - 1) / (q * (q ^ 2 + 1))) := by
  unfold hh b2; field_simp

end Lepton

/-- **Bar parity**: `q ↦ q⁻¹` sends the left-placement amplitude to minus the right one. -/
theorem exchange_bar (q : K) :
    -(hh q⁻¹) * q⁻¹ / b2 q⁻¹ = -(-(hh q) * q⁻¹ / b2 q) := by
  unfold hh b2; rw [inv_inv]; ring

/-- The amplitude vanishes exactly in the classical limit `h = 0`. -/
theorem exchange_vanish_iff {q : K} (hq : q ≠ 0) (hb : b2 q ≠ 0) :
    -(hh q) * q / b2 q = 0 ↔ hh q = 0 := by
  constructor
  · intro h
    rcases div_eq_zero_iff.mp h with h | h
    · rcases mul_eq_zero.mp h with h | h
      · exact neg_eq_zero.mp h
      · exact absurd h hq
    · exact absurd h hb
  · intro h; simp [h]

end QOU.QuarkState.TPlusChargedCurrentElement

#print axioms QOU.QuarkState.TPlusChargedCurrentElement.tplus_norm_sq
#print axioms QOU.QuarkState.TPlusChargedCurrentElement.hecke_energy_transport
#print axioms QOU.QuarkState.TPlusChargedCurrentElement.Eu_sm12
#print axioms QOU.QuarkState.TPlusChargedCurrentElement.Pp_idem
#print axioms QOU.QuarkState.TPlusChargedCurrentElement.exchange_quark_left
#print axioms QOU.QuarkState.TPlusChargedCurrentElement.exchange_quark_right
#print axioms QOU.QuarkState.TPlusChargedCurrentElement.exchange_bar
#print axioms QOU.QuarkState.TPlusChargedCurrentElement.exchange_vanish_iff
