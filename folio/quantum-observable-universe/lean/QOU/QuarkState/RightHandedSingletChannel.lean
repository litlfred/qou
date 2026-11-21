import Mathlib.LinearAlgebra.Matrix.Trace
import Mathlib.Data.Matrix.Mul
import Mathlib.LinearAlgebra.Matrix.Notation
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.FinCases
import Mathlib.Tactic.Ring

/-!
# The right line of the matter ⊗ Higgs crossing is a weak singlet (route Y, step 2: `e_R`)

Bean `qou-99qc`. Owner (Carl, 2026-11-21): *"1 Find e_R in corpus"*. Pre-registered in
`computations/probes/qbeta_yukawa_er_singlet/PREREGISTRATION.md` (commit `ba04169b03`).

## Setting (all corpus objects)

`V = K²`, basis `u` (`T³ = +½`), `d` (`T³ = −½`). On `V ⊗ V` (basis `uu, ud, du, dd`, indices
`0,1,2,3`) the Jimbo crossing `Rc` (`uu ↦ q uu`, `ud ↦ du`, `du ↦ ud + h du`, `dd ↦ q dd`,
`h = q − q⁻¹`) is the matrix of `ChargedCurrentW.Rc` (#8638) and of the `Ř` in
`YukawaVacuumPairing.compress_*`. Its `−q⁻¹`-eigenline is the corpus `rightLine` of that letter
(`LeftLineDefinition.lean`: for `q > 1` the left line is the `q`-line, `leftLine_eq_Pp_iff`; that
identification is cited, not imported, so this file depends on Mathlib only).

## Results (generic field `K`, §7c; no order, no `ℝ`)

1. **The right line is one line** (`Rc_mulVec_sing`, `cosing_vecMul_Rc`,
   `functional_eq_of_rightLine`): it is spanned by `s = q·ud − du`, and a functional supported on
   it (`φ ∘ Rc = −q⁻¹ φ`) is `φ(ud) • s*`, `s* = (0, 1, −q⁻¹, 0)`. Hypotheses `q ≠ 0`,
   `q² + 1 ≠ 0`.
2. **It has `T³ = 0`** (`gradings_mulVec_sing`): under strand gradings `diag(a₁, b₁) ⊗ diag(a₂, b₂)`
   with `a₁b₂ = b₁a₂` (two doublets: same `T³` spacing) the line has eigenvalue `a₁b₂`. With the
   hypercharge form `a = x r`, `b = x r⁻¹` this is `x₁x₂`: the `T³` factor `r` cancels and the
   charge is the sum of the two hypercharge centres (`singlet_weight_hypercharge`).
3. **Projector, quantum dimension, weak blindness** (`PR_idem`, `PR_eq`, `Rc_mul_PR`,
   `qtrace_PR`, `qtrace_PL`, `weak_insertion_kills_singlet`): `P_R = [2]⁻¹(q − Rc)` is idempotent,
   `Tr((K⊗K)P_R) = 1` and `Tr((K⊗K)(1 − P_R)) = q² + 1 + q⁻²` with `K = diag(q, q⁻¹)`. The weak
   insertion `−h·P_L` (`WeakVertexLeftProjector.weakVertex_sub_letter`) annihilates the line.
4. **Charges of the four channels** (`channel_charges`, `channel_hypercharges`, integer tables,
   `6Q` and `6Y`): with the Standard-Model charges as input labels, the singlet of
   (matter) ⊗ (Higgs) has `Q = Q(matter up) + Q(Higgs down)`. Lepton ⊗ `Φ̃` → `Q = −1, Y = −2`
   (`e_R`); quark ⊗ `Φ̃` → `−1/3, −2/3` (`d_R`); quark ⊗ `Φ` → `2/3, 4/3` (`u_R`); lepton ⊗ `Φ` →
   `0, 0` (`ν_R`). These are the right-handed rows of battery B2
   (`HyperchargeBatteryReduction.lean`). Per `hypercharge_determined_of_isospin_zero`, `Y` adds no
   information beyond `Q` on a `T³ = 0` object.
5. **Distinct from `e_L`** (`eR_ne_eL_isospin`): `2T³ = 0` against `−1`.
6. **The induced energy** (`PR_diag`, `PR_diag_sum`): compressing `P_R` by a vev in one Higgs slot
   gives the picked matter slot the entry `q²/(q²+1)` (state `ud`) or `1/(q²+1)` (state `du`).
   Which one depends on the strand ORDER (matter left or Higgs left), a selection; the two sum to 1
   and both are `½` at `q = 1` (`PR_diag_at_one`).
7. **The split is free** (`split_def`, `split_equal_yukawa`): with Yukawa strengths
   `y_u, y_d, y_ν, y_e` (one per channel, each forced up to that scalar by 1.) the #8676 split is
   `y_d² c̃ + y_ν² c − y_u² c − y_e² c̃`, `(c, c̃)` the two entries of 6. Equal strengths give 0.
   No strength is derived.

## What is NOT claimed

* That this line IS the right-handed electron. Reading it so makes `e_R` a two-strand
  (lepton ⊗ Higgs) channel rather than a strand: an identification, scope (a), put to the owner.
* Any Yukawa strength, any MeV number, any identification of a split with `Q_β`.
* The Standard-Model charges are input labels (as in #8676), and Premise L (lepton = doublet
  strand) is assumed for the lepton rows.

-- Ref: [jimbo1986] https://doi.org/10.1007/BF00400222
-- Ref: [kassel1995] Quantum Groups, Springer GTM 155, §VIII
-/

namespace QOU.QuarkState.RightHandedSingletChannel

open Matrix

variable {K : Type*} [Field K]

/-- The Jimbo crossing on `V ⊗ V` (basis `uu, ud, du, dd`). -/
def Rc (q : K) : Matrix (Fin 4) (Fin 4) K :=
  !![q, 0, 0, 0; 0, 0, 1, 0; 0, 1, q - q⁻¹, 0; 0, 0, 0, q]

/-- The singlet vector `s = q·ud − du`. -/
def sing (q : K) : Fin 4 → K := ![0, q, -1, 0]

/-- The dual singlet `s* = ud* − q⁻¹ du*`. -/
def cosing (q : K) : Fin 4 → K := ![0, 1, -q⁻¹, 0]

/-- The right-line projector `P_R = [2]⁻¹ (q − Rc)`. -/
def PR (q : K) : Matrix (Fin 4) (Fin 4) K := (q + q⁻¹)⁻¹ • (q • (1 : Matrix (Fin 4) (Fin 4) K) - Rc q)

/-- The two-strand weight grading `diag(a₁, b₁) ⊗ diag(a₂, b₂)`. -/
def KK (a₁ b₁ a₂ b₂ : K) : Matrix (Fin 4) (Fin 4) K :=
  !![a₁ * a₂, 0, 0, 0; 0, a₁ * b₂, 0, 0; 0, 0, b₁ * a₂, 0; 0, 0, 0, b₁ * b₂]

local macro "mat4" : tactic =>
  `(tactic| (ext i j; fin_cases i <;> fin_cases j <;>
    simp [Matrix.mul_apply, Fin.sum_univ_four, Matrix.one_apply] <;> (try field_simp) <;> (try ring)))

/-! ## 1. The right line -/

theorem Rc_mulVec_sing (q : K) (hq : q ≠ 0) : Rc q *ᵥ sing q = (-q⁻¹) • sing q := by
  ext i; fin_cases i <;> simp [Rc, sing, mulVec, dotProduct, Fin.sum_univ_four] <;> field_simp <;> ring

theorem cosing_vecMul_Rc (q : K) (hq : q ≠ 0) : cosing q ᵥ* Rc q = (-q⁻¹) • cosing q := by
  ext i; fin_cases i <;> simp [Rc, cosing, vecMul, dotProduct, Fin.sum_univ_four] <;> field_simp <;> ring

/-- **Forced up to one scalar.** A functional supported on the right line of the crossing
(`φ ∘ Rc = −q⁻¹ φ`) is `φ(ud) • s*`. So the shape of the three-point vertex is forced and only its
strength (a Yukawa coupling) is free. -/
theorem functional_eq_of_rightLine (q : K) (hq : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0) (φ : Fin 4 → K)
    (hφ : φ ᵥ* Rc q = (-q⁻¹) • φ) : φ = φ 1 • cosing q := by
  have e0 := congrFun hφ 0
  have e1 := congrFun hφ 1
  have e3 := congrFun hφ 3
  simp [Rc, vecMul, dotProduct, Fin.sum_univ_four] at e0 e1 e3
  have hq2 : q + q⁻¹ ≠ 0 := by
    intro h; apply h2
    have : q * (q + q⁻¹) = q ^ 2 + 1 := by field_simp
    rw [← this, h, mul_zero]
  have z0 : φ 0 = 0 := by
    have : (q + q⁻¹) * φ 0 = 0 := by linear_combination e0
    rcases mul_eq_zero.mp this with h | h
    · exact absurd h hq2
    · exact h
  have z3 : φ 3 = 0 := by
    have : (q + q⁻¹) * φ 3 = 0 := by linear_combination e3
    rcases mul_eq_zero.mp this with h | h
    · exact absurd h hq2
    · exact h
  ext i; fin_cases i <;> simp [cosing, z0, z3]
  linear_combination e1

/-! ## 2. `T³ = 0` and the charge of the line -/

/-- Under two doublet gradings with the same `T³` spacing (`a₁b₂ = b₁a₂`) the singlet is a weight
vector of weight `a₁b₂`. -/
theorem gradings_mulVec_sing (q a₁ b₁ a₂ b₂ : K) (h : a₁ * b₂ = b₁ * a₂) :
    KK a₁ b₁ a₂ b₂ *ᵥ sing q = (a₁ * b₂) • sing q := by
  ext i; fin_cases i <;> simp [KK, sing, mulVec, dotProduct, Fin.sum_univ_four, h] <;> ring

/-- With the hypercharge form `a = x r`, `b = x r⁻¹` (centre `x`, `T³` factor `r`) the singlet has
weight `x₁x₂`: the `T³` factor cancels (`T³ = 0`) and the hypercharges add. -/
theorem singlet_weight_hypercharge (q x₁ x₂ r : K) (hr : r ≠ 0) :
    KK (x₁ * r) (x₁ * r⁻¹) (x₂ * r) (x₂ * r⁻¹) *ᵥ sing q = (x₁ * x₂) • sing q := by
  have h : x₁ * r * (x₂ * r⁻¹) = x₁ * r⁻¹ * (x₂ * r) := by ring
  rw [gradings_mulVec_sing q _ _ _ _ h]
  congr 1; field_simp

/-! ## 3. Projector, quantum dimension, weak blindness -/

theorem PR_eq (q : K) (hq : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0) :
    PR q = (q + q⁻¹)⁻¹ • vecMulVec (sing q) (cosing q) := by
  have hq2 : q + q⁻¹ ≠ 0 := by
    intro h; apply h2
    have : q * (q + q⁻¹) = q ^ 2 + 1 := by field_simp
    rw [← this, h, mul_zero]
  simp only [PR, Rc, sing, cosing]
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [vecMulVec, Matrix.one_apply] <;> field_simp <;> (try ring)

theorem PR_idem (q : K) (hq : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0) : PR q * PR q = PR q := by
  have hq2 : q ^ 2 + 1 ≠ 0 := h2
  simp only [PR, Rc]
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [Matrix.mul_apply, Fin.sum_univ_four, Matrix.one_apply, Matrix.smul_apply] <;>
    field_simp <;> ring

theorem Rc_mul_PR (q : K) (hq : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0) : Rc q * PR q = (-q⁻¹) • PR q := by
  simp only [PR, Rc]
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [Matrix.mul_apply, Fin.sum_univ_four, Matrix.one_apply, Matrix.smul_apply] <;>
    field_simp <;> ring

/-- **Quantum dimension 1.** With `K = diag(q, q⁻¹)` on both strands, `Tr((K⊗K) P_R) = 1`. -/
theorem qtrace_PR (q : K) (hq : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0) :
    trace (KK q q⁻¹ q q⁻¹ * PR q) = 1 := by
  simp only [trace, diag, Matrix.mul_apply, Fin.sum_univ_four]
  simp [PR, Rc, KK]
  field_simp

/-- The left (triplet) line has quantum dimension `q² + 1 + q⁻² = [3]`. -/
theorem qtrace_PL (q : K) (hq : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0) :
    trace (KK q q⁻¹ q q⁻¹ * (1 - PR q)) = q ^ 2 + 1 + q⁻¹ ^ 2 := by
  simp only [trace, diag, Matrix.mul_apply, Fin.sum_univ_four]
  simp [PR, Rc, KK, Matrix.one_apply, Matrix.sub_apply]
  field_simp
  ring_nf

/-- **The weak insertion does not see the line.** `−h·P_L` with `P_L = 1 − P_R` kills `s`. -/
theorem weak_insertion_kills_singlet (q : K) (hq : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0) :
    (-(q - q⁻¹)) • (1 - PR q) *ᵥ sing q = 0 := by
  ext i; fin_cases i <;>
    simp [PR, Rc, sing, mulVec, dotProduct, Fin.sum_univ_four, Matrix.one_apply, Matrix.sub_apply] <;>
    field_simp <;> (try ring_nf) <;> simp

/-! ## 4–5. Charges of the four channels (integer tables, `6Q`, `6T³`, `6Y`)

Doublet labels: `(up, down)` charges `6Q`. Lepton `(0, −6)`, quark `(4, −2)`, Higgs
`Φ = (φ⁺, φ⁰) = (6, 0)`, conjugate Higgs `Φ̃ = (φ⁰*, φ⁻) = (0, −6)`. The singlet of
(matter on the left) ⊗ (Higgs on the right) has the charge of `ud`, i.e. matter-up + Higgs-down,
which equals matter-down + Higgs-up because both are doublets. -/

/-- `6Q` of the singlet channel: matter-up plus Higgs-down. -/
def singletSixQ (m h : ℤ × ℤ) : ℤ := m.1 + h.2

def lepton : ℤ × ℤ := (0, -6)
def quark : ℤ × ℤ := (4, -2)
def higgs : ℤ × ℤ := (6, 0)
def higgsConj : ℤ × ℤ := (0, -6)

/-- The two components of the singlet carry the same charge for each of the four channels. -/
theorem channel_charge_consistent :
    ∀ m ∈ [lepton, quark], ∀ h ∈ [higgs, higgsConj], m.1 + h.2 = m.2 + h.1 := by decide

/-- The four channel charges: `e_R` (−1), `d_R` (−1/3), `u_R` (+2/3), `ν_R` (0). -/
theorem channel_charges :
    singletSixQ lepton higgsConj = -6 ∧ singletSixQ quark higgsConj = -2 ∧
    singletSixQ quark higgs = 4 ∧ singletSixQ lepton higgs = 0 := by decide

/-- `6Y = 2·6Q − 2·6T³` (cleared Gell-Mann–Nishijima); on the singlet `T³ = 0`. These are the
right-handed rows `{−2, −2/3, +4/3, 0}` of battery B2 (`HyperchargeBatteryReduction`). -/
theorem channel_hypercharges :
    2 * singletSixQ lepton higgsConj = -12 ∧ 2 * singletSixQ quark higgsConj = -4 ∧
    2 * singletSixQ quark higgs = 8 ∧ 2 * singletSixQ lepton higgs = 0 := by decide

/-- `e_R` channel and `e_L` differ in isospin: `2T³ = 0` against `−1`; same charge `6Q = −6`. -/
theorem eR_ne_eL_isospin :
    singletSixQ lepton higgsConj = lepton.2 ∧ (0 : ℤ) ≠ -1 := by decide

/-! ## 6. The induced energy -/

/-- Diagonal of `P_R`: `0, q²/(q²+1), 1/(q²+1), 0`. -/
theorem PR_diag (q : K) (hq : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0) :
    PR q 0 0 = 0 ∧ PR q 1 1 = q ^ 2 / (q ^ 2 + 1) ∧ PR q 2 2 = 1 / (q ^ 2 + 1) ∧ PR q 3 3 = 0 := by
  refine ⟨?_, ?_, ?_, ?_⟩ <;> simp [PR, Rc, Matrix.one_apply] <;> field_simp <;> ring

theorem PR_diag_sum (q : K) (hq : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0) :
    q ^ 2 / (q ^ 2 + 1) + 1 / (q ^ 2 + 1) = 1 := by field_simp

theorem PR_diag_at_one (h2 : (1 : K) + 1 ≠ 0) :
    (1 : K) ^ 2 / (1 ^ 2 + 1) = 1 / 2 ∧ (1 : K) / (1 ^ 2 + 1) = 1 / 2 := by
  constructor <;> norm_num

/-! ## 7. The split is free -/

/-- The #8676 split `χ(q,d) + χ(ℓ,u) − χ(q,u) − χ(ℓ,d)` with `χ = y²·(diagonal entry)`. `cPhi` is
the entry for the `Φ` channels (`u_R`, `ν_R`), `cConj` for the `Φ̃` channels (`d_R`, `e_R`). -/
def split (yu yd yn ye cPhi cConj : K) : K :=
  yd ^ 2 * cConj + yn ^ 2 * cPhi - yu ^ 2 * cPhi - ye ^ 2 * cConj

theorem split_def (yu yd yn ye cPhi cConj : K) :
    split yu yd yn ye cPhi cConj = (yd ^ 2 - ye ^ 2) * cConj + (yn ^ 2 - yu ^ 2) * cPhi := by
  unfold split; ring

/-- Equal Yukawa strengths give split 0: the type × flavour interaction #8676 needs comes only from
the strengths, which this construction does not fix. -/
theorem split_equal_yukawa (y cPhi cConj : K) : split y y y y cPhi cConj = 0 := by
  unfold split; ring

end QOU.QuarkState.RightHandedSingletChannel
