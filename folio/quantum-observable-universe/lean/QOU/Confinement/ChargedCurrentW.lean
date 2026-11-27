/-
# The charged W exchange inside a crossing, and the n → p e⁻ ν̄ amplitude `M(q)`

Bean `qou-99qc` (N1), also `qou-g0jn`, `qou-0whz`. Owner (Carl), 2026-11-20: the bar image of a photon is
NOT taken to be a photon (so `φ₀, φ₁` stay underived); derive the W as a charged element and the β-decay
amplitude; *"the β-decay rate should depend on q"*. Pre-registered in
`computations/probes/qbeta_n1_charged_w/PREREGISTRATION.md`.

## Setting

`V = K²`, basis `u` (`K u = q u`, `T³ = +½`) and `d`. On `V ⊗ V` (basis `uu, ud, du, dd`) the Jimbo
crossing `Rc` (`uu ↦ q uu`, `ud ↦ du`, `du ↦ ud + h du`, `dd ↦ q dd`, `h = q − q⁻¹`), the same matrix as
`IsospinRaisingRoundTrip.Rc` (#8632, re-stated here so this file depends on Mathlib only).

## Part A — the strand-tracked crossing has a charged part, and it is chiral

`Rc` labels its output by POSITION. Re-labelled by STRAND (compose with the swap `P`):

* `Rc_strand`    : `P·Rc = R₀ + h·(E⊗F)` (positive crossing),
* `Rcinv_strand` : `P·Rc⁻¹ = R₀' − h·(F⊗E)` (negative crossing), with `Rc⁻¹ = Rc − h` (`Rc_mul_inv`).

`R₀, R₀'` are diagonal (charge-neutral on each strand, `R0_neutral`). `E⊗F` raises the charge of the strand
entering on the left by one and lowers the other (`EF_raises`, `EF_total`); `F⊗E` does the opposite
(`FE_lowers`). So a positive crossing carries **only** a `W⁺`-type exchange, with coupling `+h`, and a negative
crossing **only** the opposite exchange, with coupling `−h`. Charge conjugation `u ↔ d` swaps the two
(`chargeConj_EF`). The W exchange is therefore not bar-closed: `σ ↦ σ⁻¹` sends `+h·E⊗F` to `−h·F⊗E`.
`beta_vertex_pos`, `beta_vertex_neg`: with a `d` quark on the left strand and a `ν = u` lepton on the right,
the amplitude `d ν → u e⁻` is `h` for `σ` and `0` for `σ⁻¹`.

(The off-diagonal `ud ↔ du` of `Rc` itself is a transposition: no strand changes flavour. That is the term
`qou-g0jn` RESULT 1 measured. The flavour-changing term is the `h` term, visible only after strand tracking.)

## Part B — the lepton strand passing a three-strand nucleon gives `h·q·T⁺`

On `V^{⊗4}`, sector with two `u` (6 states `uudd, udud, uddu, duud, dudu, dduu`), `S1, S2, S3` are `σ₁, σ₂, σ₃`.
Nucleon on positions 1–3, lepton strand on position 4.

* `passage_left_pos` / `beta_amp_left_pos` : for the leftward positive passage `σ₁σ₂σ₃`, the block
  `n ⊗ ν → e⁻ ⊗ p` is **`(h·q)·T⁺`** with `T⁺ = Δ²(E)` (`Eu`, the Jimbo coproduct of #8632). So the
  isospin raising operator that #8632 posited as `n → p` is DERIVED here from a lepton crossing the nucleon,
  with coupling `h·q`.
* `noflip_left_pos` : the charge-neutral block is `q·1`.
* `reverse_left_pos` : the same braid gives `0` for `p ⊗ e⁻ → ν ⊗ n` (chirality).
* `beta_amp_left_neg` : the leftward negative passage gives `0` for `n ν → p e⁻`.
* `beta_amp_right_neg` : the rightward negative passage gives **`−(h/q)·T⁺`**, and `−h/q` is the bar image
  `q ↦ q⁻¹` of `h·q` (`bar_coupling`).

## Part C — `|M|²`

* `Eu_transpose` : `T⁺ᵀ = T⁻`, so in the tensor basis `AᵀA = (hq)²·T⁻T⁺`.
* `normSq_isospinHalf` : for every neutron state in the isospin-½ eigenspace (`span{(−q,1,0), (−q²,0,1)}`,
  where `T⁻T⁺ = 1`), `‖A v‖² = (hq)²·‖v‖² = (q² − 1)²·‖v‖²`.
* `normSq_isospinThreeHalf` : on isospin 3/2, `(hq)²·[2]²`.
* `amp_at_one`, `normSq_strictMono` : the amplitude vanishes at `q = 1`; for `1 < q < q'` the rate factor
  `(q² − 1)²` is strictly increasing.

## What is NOT proved

That the lepton is a second copy of `V` with `ν = u, e⁻ = d` (an assumption, as in `qou-g0jn` PRE-REG 3);
which passage (leftward positive, coupling `hq`, or rightward negative, `h/q`) is the physical one; any MeV
scale (`G_F` does not emerge); the Gamow–Teller (spin) part. The electron here is the `d` of the lepton strand,
NOT the `e⁻ = σ₀σ₁σ₀` coordinate of the γγ normal form, and the photon weights do not enter.

Base ring (§7c): generic `[Field K]`; an ordered field only for `normSq_strictMono`. No `ℝ`, no `sorry`.

-- Ref: [jimbo1986] https://doi.org/10.1007/BF00400222
-- Ref: [kassel1995] Quantum Groups, Springer GTM 155, §VIII (universal R-matrix of U_q(sl₂))
-/
import Mathlib.Data.Matrix.Mul
import Mathlib.LinearAlgebra.Matrix.Notation
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.FinCases
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.Linarith
import Mathlib.Algebra.Order.Field.Basic

namespace QOU.QuarkState.ChargedCurrentW

open Matrix

variable {K : Type*} [Field K]

/-- `h = q − q⁻¹`. -/
def hh (q : K) : K := q - q⁻¹

/-! ## Part A: `V ⊗ V`, basis `uu, ud, du, dd` (columns are images) -/

/-- Jimbo `Ř`. -/
def Rc (q : K) : Matrix (Fin 4) (Fin 4) K :=
  !![q, 0, 0, 0; 0, 0, 1, 0; 0, 1, q - q⁻¹, 0; 0, 0, 0, q]

/-- The swap `P`. -/
def swap : Matrix (Fin 4) (Fin 4) K := !![1, 0, 0, 0; 0, 0, 1, 0; 0, 1, 0, 0; 0, 0, 0, 1]

/-- `E ⊗ F` : `du ↦ ud` (left strand `d → u`, right strand `u → d`). -/
def EF : Matrix (Fin 4) (Fin 4) K := !![0, 0, 0, 0; 0, 0, 1, 0; 0, 0, 0, 0; 0, 0, 0, 0]

/-- `F ⊗ E` : `ud ↦ du`. -/
def FE : Matrix (Fin 4) (Fin 4) K := !![0, 0, 0, 0; 0, 0, 0, 0; 0, 1, 0, 0; 0, 0, 0, 0]

/-- Neutral part of the positive crossing. -/
def R0 (q : K) : Matrix (Fin 4) (Fin 4) K := !![q, 0, 0, 0; 0, 1, 0, 0; 0, 0, 1, 0; 0, 0, 0, q]

/-- Neutral part of the negative crossing. -/
def R0' (q : K) : Matrix (Fin 4) (Fin 4) K := !![q⁻¹, 0, 0, 0; 0, 1, 0, 0; 0, 0, 1, 0; 0, 0, 0, q⁻¹]

/-- `K ⊗ 1` (charge of the left strand). -/
def K1 (q : K) : Matrix (Fin 4) (Fin 4) K := !![q, 0, 0, 0; 0, q, 0, 0; 0, 0, q⁻¹, 0; 0, 0, 0, q⁻¹]

/-- `1 ⊗ K` (charge of the right strand). -/
def K2 (q : K) : Matrix (Fin 4) (Fin 4) K := !![q, 0, 0, 0; 0, q⁻¹, 0, 0; 0, 0, q, 0; 0, 0, 0, q⁻¹]

/-- Charge conjugation `u ↔ d` on both strands. -/
def Cc : Matrix (Fin 4) (Fin 4) K := !![0, 0, 0, 1; 0, 0, 1, 0; 0, 1, 0, 0; 1, 0, 0, 0]

/-- Entrywise check of a `4 × 4` identity. -/
local macro "mat4" : tactic =>
  `(tactic| (ext i j; fin_cases i <;> fin_cases j <;>
    simp [Matrix.mul_apply, Fin.sum_univ_four, Matrix.one_apply] <;> (try field_simp) <;> (try ring)))

theorem swap_sq : (swap : Matrix (Fin 4) (Fin 4) K) * swap = 1 := by
  simp only [swap]; mat4

/-- **Strand-tracked positive crossing:** `P·Ř = R₀ + h·(E⊗F)`. -/
theorem Rc_strand (q : K) : swap * Rc q = R0 q + hh q • EF := by
  simp only [swap, Rc, R0, EF, hh]; mat4

/-- **Strand-tracked negative crossing:** `P·Ř⁻¹ = R₀' − h·(F⊗E)`, with `Ř⁻¹ = Ř − h`. -/
theorem Rcinv_strand (q : K) : swap * (Rc q - hh q • 1) = R0' q - hh q • FE := by
  simp only [swap, Rc, R0', FE, hh]; mat4

/-- `Ř − h` is the inverse of `Ř`. -/
theorem Rc_mul_inv (q : K) (hq : q ≠ 0) : Rc q * (Rc q - hh q • 1) = 1 := by
  simp only [Rc, hh]; mat4

theorem R0_neutral (q : K) : K1 q * R0 q = R0 q * K1 q ∧ K2 q * R0 q = R0 q * K2 q := by
  constructor <;> (simp only [K1, K2, R0]; mat4)

theorem R0'_neutral (q : K) : K1 q * R0' q = R0' q * K1 q ∧ K2 q * R0' q = R0' q * K2 q := by
  constructor <;> (simp only [K1, K2, R0']; mat4)

/-- `E⊗F` raises the left strand's charge: `(K⊗1)(E⊗F) = q²·(E⊗F)(K⊗1)`, and lowers the right one. -/
theorem EF_raises (q : K) (hq : q ≠ 0) :
    K1 q * EF = q ^ 2 • (EF * K1 q) ∧ K2 q * EF = (q⁻¹) ^ 2 • (EF * K2 q) := by
  constructor <;> (simp only [K1, K2, EF]; mat4)

/-- `F⊗E` lowers the left strand's charge. -/
theorem FE_lowers (q : K) (hq : q ≠ 0) :
    K1 q * FE = (q⁻¹) ^ 2 • (FE * K1 q) ∧ K2 q * FE = q ^ 2 • (FE * K2 q) := by
  constructor <;> (simp only [K1, K2, FE]; mat4)

/-- Total charge is conserved by the exchange. -/
theorem EF_total (q : K) : (K1 q * K2 q) * EF = EF * (K1 q * K2 q) := by
  simp only [K1, K2, EF]; mat4

/-- Charge conjugation exchanges the two currents. -/
theorem chargeConj_EF : (Cc : Matrix (Fin 4) (Fin 4) K) * EF * Cc = FE := by
  simp only [Cc, EF, FE]; mat4

/-- **The β vertex of one positive crossing:** strand-tracked, `d ν ↦ u e⁻` with amplitude `h`
(input `du` = index 2, output `ud` = index 1). -/
theorem beta_vertex_pos (q : K) : ((swap : Matrix (Fin 4) (Fin 4) K) * Rc q) 1 2 = hh q := by
  rw [Rc_strand]; simp [R0, EF]

/-- **Chirality:** the negative crossing has no `d ν ↦ u e⁻` term. -/
theorem beta_vertex_neg (q : K) (hq : q ≠ 0) : ((swap : Matrix (Fin 4) (Fin 4) K) * (Rc q - hh q • 1)) 1 2 = 0 := by
  rw [Rcinv_strand q]; simp [R0', FE]

/-! ## Part B: the lepton strand passing a three-strand nucleon

Sector of `V^{⊗4}` with two `u`; basis `uudd, udud, uddu, duud, dudu, dduu` (indices `0 … 5`). -/

/-- `σ₁` on the sector. -/
def S1 (q : K) : Matrix (Fin 6) (Fin 6) K :=
  !![q, 0, 0, 0, 0, 0; 0, 0, 0, 1, 0, 0; 0, 0, 0, 0, 1, 0;
     0, 1, 0, q - q⁻¹, 0, 0; 0, 0, 1, 0, q - q⁻¹, 0; 0, 0, 0, 0, 0, q]

/-- `σ₂` on the sector. -/
def S2 (q : K) : Matrix (Fin 6) (Fin 6) K :=
  !![0, 1, 0, 0, 0, 0; 1, q - q⁻¹, 0, 0, 0, 0; 0, 0, q, 0, 0, 0;
     0, 0, 0, q, 0, 0; 0, 0, 0, 0, 0, 1; 0, 0, 0, 0, 1, q - q⁻¹]

/-- `σ₃` on the sector. -/
def S3 (q : K) : Matrix (Fin 6) (Fin 6) K :=
  !![q, 0, 0, 0, 0, 0; 0, 0, 1, 0, 0, 0; 0, 1, q - q⁻¹, 0, 0, 0;
     0, 0, 0, 0, 1, 0; 0, 0, 0, 1, q - q⁻¹, 0; 0, 0, 0, 0, 0, q]

/-- Entrywise check of a `6 × 6` identity. -/
local macro "mat6" : tactic =>
  `(tactic| (ext i j; fin_cases i <;> fin_cases j <;>
    simp [Matrix.mul_apply, Fin.sum_univ_succ, Matrix.one_apply] <;> (try field_simp) <;> (try ring)))

theorem S13_comm (q : K) : S1 q * S3 q = S3 q * S1 q := by simp only [S1, S3]; mat6

/-- `σ₂σ₃` on the sector. -/
def S23 (q : K) : Matrix (Fin 6) (Fin 6) K :=
  !![0, 0, 1, 0, 0, 0; q, 0, q - q⁻¹, 0, 0, 0; 0, q, q * (q - q⁻¹), 0, 0, 0;
     0, 0, 0, 0, q, 0; 0, 0, 0, 0, 0, q; 0, 0, 0, 1, q - q⁻¹, q * (q - q⁻¹)]

theorem S23_eq (q : K) : S2 q * S3 q = S23 q := by simp only [S2, S3, S23]; mat6

/-- The leftward positive passage `σ₁σ₂σ₃` (lepton from position 4 to 1). -/
def Lpass (q : K) : Matrix (Fin 6) (Fin 6) K :=
  !![0, 0, q, 0, 0, 0; 0, 0, 0, 0, q, 0; 0, 0, 0, 0, 0, q;
     q, 0, q - q⁻¹, 0, q * (q - q⁻¹), 0; 0, q, q * (q - q⁻¹), 0, 0, q * (q - q⁻¹);
     0, 0, 0, q, q * (q - q⁻¹), q ^ 2 * (q - q⁻¹)]

theorem passage_left_pos (q : K) (hq : q ≠ 0) : S1 q * S2 q * S3 q = Lpass q := by
  rw [mul_assoc, S23_eq]; simp only [S1, S23, Lpass]; mat6

/-- `T⁺ = Δ²(E) : W₋ → W₊` (Jimbo; bases `udd, dud, ddu` → `duu, udu, uud`), as in #8632. -/
def Eu (q : K) : Matrix (Fin 3) (Fin 3) K := !![0, 1, q; 1, 0, 1; q⁻¹, 1, 0]

/-- `T⁻ = Δ²(F) : W₊ → W₋`. -/
def Fd (q : K) : Matrix (Fin 3) (Fin 3) K := !![0, 1, q⁻¹; 1, 0, 1; q, 1, 0]

/-- `n ⊗ ν` : `udd·u, dud·u, ddu·u`. -/
def inNnu : Fin 3 → Fin 6 := ![2, 4, 5]
/-- `e⁻ ⊗ p` : `d·duu, d·udu, d·uud`. -/
def outEp : Fin 3 → Fin 6 := ![5, 4, 3]
/-- `ν ⊗ n` : `u·udd, u·dud, u·ddu`. -/
def outNuN : Fin 3 → Fin 6 := ![0, 1, 2]
/-- `p ⊗ e⁻` : `duu·d, udu·d, uud·d`. -/
def inPe : Fin 3 → Fin 6 := ![3, 1, 0]

/-- **The β amplitude of the leftward positive passage is `(h·q)·T⁺`.** -/
theorem beta_amp_left_pos (q : K) (hq : q ≠ 0) :
    (S1 q * S2 q * S3 q).submatrix outEp inNnu = (hh q * q) • Eu q := by
  rw [passage_left_pos q hq]
  ext i j; fin_cases i <;> fin_cases j <;> simp [Lpass, Eu, outEp, inNnu, hh] <;> field_simp <;> ring

/-- The charge-neutral part of the same passage is `q·1`. -/
theorem noflip_left_pos (q : K) (hq : q ≠ 0) :
    (S1 q * S2 q * S3 q).submatrix outNuN inNnu = q • (1 : Matrix (Fin 3) (Fin 3) K) := by
  rw [passage_left_pos q hq]
  ext i j; fin_cases i <;> fin_cases j <;> simp [Lpass, outNuN, inNnu]

/-- **Chirality:** the same braid never takes `p ⊗ e⁻` to `ν ⊗ n`. -/
theorem reverse_left_pos (q : K) (hq : q ≠ 0) :
    (S1 q * S2 q * S3 q).submatrix outNuN inPe = 0 := by
  rw [passage_left_pos q hq]
  ext i j; fin_cases i <;> fin_cases j <;> simp [Lpass, outNuN, inPe]

/-- The leftward negative passage `σ₁⁻¹σ₂⁻¹σ₃⁻¹` (each `σᵢ⁻¹ = σᵢ − h`). -/
def Lneg (q : K) : Matrix (Fin 6) (Fin 6) K :=
  (S1 q - hh q • 1) * (S2 q - hh q • 1) * (S3 q - hh q • 1)

/-- **Chirality:** the leftward negative passage has no `n ν → p e⁻` block. -/
theorem beta_amp_left_neg (q : K) (hq : q ≠ 0) : (Lneg q).submatrix outEp inNnu = 0 := by
  simp only [Lneg, S1, S2, S3, hh]
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [Matrix.mul_apply, Fin.sum_univ_succ, Matrix.one_apply, outEp, inNnu] <;> field_simp <;> ring

/-- The rightward negative passage `σ₃⁻¹σ₂⁻¹σ₁⁻¹` (lepton from position 1 to 4). -/
def Rneg (q : K) : Matrix (Fin 6) (Fin 6) K :=
  (S3 q - hh q • 1) * (S2 q - hh q • 1) * (S1 q - hh q • 1)

/-- `ν ⊗ n` as input : `u·udd, u·dud, u·ddu`. -/
def inNuN : Fin 3 → Fin 6 := ![0, 1, 2]

/-- **The rightward negative passage gives `−(h/q)·T⁺`.** -/
theorem beta_amp_right_neg (q : K) (hq : q ≠ 0) :
    (Rneg q).submatrix inPe inNuN = (-(hh q * q⁻¹)) • Eu q := by
  simp only [Rneg, S1, S2, S3, Eu, hh]
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [Matrix.mul_apply, Fin.sum_univ_succ, Matrix.one_apply, inPe, inNuN] <;> field_simp <;> ring

/-- **The two couplings are bar images:** `(h·q)|_{q ↦ q⁻¹} = −h/q`. -/
theorem bar_coupling (q : K) (hq : q ≠ 0) : hh q⁻¹ * q⁻¹ = -(hh q * q⁻¹) := by
  simp only [hh, inv_inv]; ring

/-! ## Part C: `|M|²` -/

theorem Eu_transpose (q : K) : (Eu q)ᵀ = Fd q := by
  ext i j; fin_cases i <;> fin_cases j <;> simp [Eu, Fd]

/-- `T⁻T⁺` is `1` on the isospin-½ vectors `(−q, 1, 0)`, `(−q², 0, 1)`. -/
theorem FE_isospinHalf (q : K) (hq : q ≠ 0) (a b : K) :
    (Fd q * Eu q) *ᵥ ![-(a * q) - b * q ^ 2, a, b] = ![-(a * q) - b * q ^ 2, a, b] := by
  ext i; fin_cases i <;> simp [Fd, Eu, Matrix.mulVec, dotProduct, Fin.sum_univ_three, Matrix.mul_apply]
    <;> field_simp <;> ring

/-- `T⁻T⁺` is `[2]²` on the isospin-3/2 vector `(q⁻², q⁻¹, 1)`. -/
theorem FE_isospinThreeHalf (q : K) (hq : q ≠ 0) (c : K) :
    (Fd q * Eu q) *ᵥ ![c * q⁻¹ ^ 2, c * q⁻¹, c] = (q + q⁻¹) ^ 2 • ![c * q⁻¹ ^ 2, c * q⁻¹, c] := by
  ext i; fin_cases i <;> simp [Fd, Eu, Matrix.mulVec, dotProduct, Fin.sum_univ_three, Matrix.mul_apply]
    <;> field_simp <;> ring

/-- **`|M|²` on the isospin-½ neutron:** `‖A v‖² = (hq)²·‖v‖² = (q² − 1)²·‖v‖²`. -/
theorem normSq_isospinHalf (q : K) (hq : q ≠ 0) (a b : K) :
    let v : Fin 3 → K := ![-(a * q) - b * q ^ 2, a, b]
    let A := (hh q * q) • Eu q
    (A *ᵥ v) ⬝ᵥ (A *ᵥ v) = (q ^ 2 - 1) ^ 2 * (v ⬝ᵥ v) := by
  simp only [hh, Eu, Matrix.mulVec, dotProduct, Fin.sum_univ_three, Matrix.smul_apply]
  simp
  field_simp
  ring

/-- **`|M|²` on the isospin-3/2 state:** `(hq)²·[2]²·‖v‖²`. -/
theorem normSq_isospinThreeHalf (q : K) (hq : q ≠ 0) (c : K) :
    let v : Fin 3 → K := ![c * q⁻¹ ^ 2, c * q⁻¹, c]
    let A := (hh q * q) • Eu q
    (A *ᵥ v) ⬝ᵥ (A *ᵥ v) = (q ^ 2 - 1) ^ 2 * (q + q⁻¹) ^ 2 * (v ⬝ᵥ v) := by
  simp only [hh, Eu, Matrix.mulVec, dotProduct, Fin.sum_univ_three, Matrix.smul_apply]
  simp
  field_simp
  ring

/-- The coupling vanishes at `q = 1`. -/
theorem amp_at_one : hh (1 : K) * 1 = 0 := by simp [hh]

/-- `h·q = q² − 1`. -/
theorem coupling_eq (q : K) (hq : q ≠ 0) : hh q * q = q ^ 2 - 1 := by
  simp only [hh]; field_simp

section Ordered

variable {L : Type*} [Field L] [LinearOrder L] [IsStrictOrderedRing L]

/-- **The rate factor increases with `q` above `1`.** -/
theorem normSq_strictMono {q q' : L} (h1 : 1 < q) (h2 : q < q') :
    (q ^ 2 - 1) ^ 2 < (q' ^ 2 - 1) ^ 2 := by
  have a : 0 < q ^ 2 - 1 := by nlinarith
  have b : q ^ 2 - 1 < q' ^ 2 - 1 := by nlinarith
  nlinarith

end Ordered

end QOU.QuarkState.ChargedCurrentW
