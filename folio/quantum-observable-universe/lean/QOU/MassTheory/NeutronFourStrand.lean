import QOU.BraidsAndKnots.NucleonWeightSpaceTwoTerm
import QOU.QuarkState.PairwiseChargeEnergyBeta

/-!
# The neutron identity with a lepton strand (four strands, choice C-lep)

Pre-registration: `computations/probes/mn_own_identity/PREREGISTRATION-four-strand.md`.
Companion of `QOU.MassTheory.NeutronOwnIdentity` (three strands).

Choice **C-lep** (#8636 Part B): a fourth strand on the same `V` is the lepton doublet,
`ν = u`, `e⁻ = d`. The `T³ = 0` block of `V^{⊗4}` is six-dimensional and is indexed here by
`Fin 3 ⊕ Fin 3`:

* `N = n ⊗ ν`, basis `(uddu, dudu, dduu)` — the neutron weight space `(udd, dud, ddu)` ⊗ `u`;
* `P = p ⊗ e`, basis `(uudd, udud, duud)` — the proton weight space `(uud, udu, duu)` ⊗ `d`.

`σ₁, σ₂` act on the nucleon strands, so they are block-diagonal with the three-strand Jimbo
blocks of `NucleonWeightSpaceTraces` (`B` on `N`, `A` on `P`). `σ₃` crosses the third quark with
the lepton and maps `N` to `P` (`uddu ↦ udud + h·uddu`). Its matrix is read off the Jimbo Ř
(`Ř(uu) = q uu`, `Ř(dd) = q dd`, `Ř(ud) = du`, `Ř(du) = ud + h du`); the probe
`mn_four_strand_probe.py` checks it against the full 16-dimensional action, and this file checks
that `σ₁, σ₂, σ₃` satisfy the Hecke and braid relations of `H₄(q)` on the block.

## What is proved (generic `[Field R]`, no number enters)

1. `trN_V3_eq_trP_V3`: the spectator reading `V³ ⊗ 1` has equal sector traces on `N` and `P`
   (both equal `tr_{W}(V³) = −P(q)/q⁶`). With `K^{⊗4} = 1` on both sectors, the identity read on
   either sector gives `m_n = m_p` (arm L-A).
2. `trN_w`, `trP_w`: for the #8636 selected word `w = σ₁σ₃⁻¹`, `tr_N(w) = 1` and
   `tr_P(w) = 1 − h²` (arm L-B). They differ at first order in `q − 1`.
3. `twoTerm_connected_zero`: the covariant all-pairs pair charge is a scalar on each sector
   (`−1/3` on `N`, `−1` on `P`, SM charges with `ν 0`, `e −1`), so the connected two-term part
   of **every** element vanishes on both sectors. The two-term trace adds nothing to arms L-A or
   L-B; this is derived, not dropped.

## What is NOT claimed

That the ratio `tr_N(w)/tr_P(w)` is the neutron's factor. That is the pre-registered reading L-B,
stated as `NeutronIdentityLB`; it misses CODATA by +4.46 % (probe).
-/

namespace QOU.MassTheory.NeutronFourStrand

open Matrix
open QOU.BraidsAndKnots.NucleonWeightSpaceTraces
open QOU.BraidsAndKnots.NucleonWeightSpaceTwoTerm

variable {R : Type*} [Field R]

/-- Block index: `inl` = `N = n⊗ν`, `inr` = `P = p⊗e`. -/
abbrev Ix := Fin 3 ⊕ Fin 3

/-- `σ₁` on the `T³ = 0` block of `V^{⊗4}`. -/
def s1 (q : R) : Matrix Ix Ix R := fromBlocks (B₁ q) 0 0 (A₁ q)
/-- `σ₂` on the block. -/
def s2 (q : R) : Matrix Ix Ix R := fromBlocks (B₂ q) 0 0 (A₂ q)
/-- `σ₂⁻¹` on the block. -/
def s2Inv (q : R) : Matrix Ix Ix R := fromBlocks (B₂Inv q) 0 0 (A₂Inv q)

/-- The off-diagonal part of `σ₃`: `uddu ↔ udud`, `dudu ↔ duud`. -/
def E : Matrix (Fin 3) (Fin 3) R := !![0, 1, 0; 0, 0, 1; 0, 0, 0]

/-- Its transpose, written out. -/
def Et : Matrix (Fin 3) (Fin 3) R := !![0, 0, 0; 1, 0, 0; 0, 1, 0]

/-- `σ₃` (third quark crossing the lepton) on the block. -/
def s3 (q : R) : Matrix Ix Ix R :=
  fromBlocks !![q - q⁻¹, 0, 0; 0, q - q⁻¹, 0; 0, 0, q] E Et !![q, 0, 0; 0, 0, 0; 0, 0, 0]

/-- `σ₃⁻¹ = σ₃ − h` on the block. -/
def s3Inv (q : R) : Matrix Ix Ix R :=
  fromBlocks !![0, 0, 0; 0, 0, 0; 0, 0, q⁻¹] E Et
    !![q⁻¹, 0, 0; 0, -(q - q⁻¹), 0; 0, 0, -(q - q⁻¹)]

/-- Entrywise check of an identity between matrices on the block. -/
macro "block_ext" : tactic => `(tactic| (
  ext i j
  rcases i with i | i <;> rcases j with j | j <;> fin_cases i <;> fin_cases j <;>
    simp [s1, s2, s3, s3Inv, E, Et, B₁, B₂, A₁, A₂, Matrix.mul_apply, Fintype.sum_sum_type,
      Fin.sum_univ_three, fromBlocks] <;>
    first | done | ring1 | (field_simp; ring1)))

theorem s3_mul_s3Inv (q : R) (hq : q ≠ 0) : s3 q * s3Inv q = 1 := by
  ext i j
  rcases i with i | i <;> rcases j with j | j <;> fin_cases i <;> fin_cases j <;>
    simp [s3, s3Inv, E, Et, Matrix.mul_apply, Fintype.sum_sum_type, Fin.sum_univ_three,
      fromBlocks, Matrix.one_apply, hq] <;>
    first | done | ring1 | (field_simp; ring1)

/-- `σ₃⁻¹ = σ₃ − h`. -/
theorem s3Inv_eq (q : R) : s3Inv q = s3 q - (q - q⁻¹) • (1 : Matrix Ix Ix R) := by
  ext i j
  rcases i with i | i <;> rcases j with j | j <;> fin_cases i <;> fin_cases j <;>
    simp [s3, s3Inv, E, Et, fromBlocks, Matrix.one_apply] <;> ring

/-- Hecke relation for `σ₃`: `σ₃² = h σ₃ + 1`. -/
theorem s3_hecke (q : R) (hq : q ≠ 0) : s3 q * s3 q = (q - q⁻¹) • s3 q + 1 := by
  have h := s3_mul_s3Inv q hq
  rw [s3Inv_eq, Matrix.mul_sub, Matrix.mul_smul, Matrix.mul_one] at h
  rw [← h]; abel

/-- Far commutation `σ₁σ₃ = σ₃σ₁`. -/
theorem s1_s3_comm (q : R) : s1 q * s3 q = s3 q * s1 q := by
  block_ext

/-- Braid relation `σ₂σ₃σ₂ = σ₃σ₂σ₃`. -/
theorem s2_s3_braid (q : R) (hq : q ≠ 0) : s2 q * s3 q * s2 q = s3 q * s2 q * s3 q := by
  ext i j
  rcases i with i | i <;> rcases j with j | j <;> fin_cases i <;> fin_cases j <;>
    simp [s2, s3, E, Et, B₂, A₂, Matrix.mul_apply, Fintype.sum_sum_type, Fin.sum_univ_three,
      fromBlocks] <;>
    first | done | ring1 | (field_simp; ring1)

/-- Sector traces. -/
def trN (M : Matrix Ix Ix R) : R := trace (toBlocks₁₁ M)
def trP (M : Matrix Ix Ix R) : R := trace (toBlocks₂₂ M)

/-- `V = σ₁σ₂⁻¹` on the block and `V³ ⊗ 1`. -/
def V4 (q : R) : Matrix Ix Ix R := s1 q * s2Inv q
def V3_4 (q : R) : Matrix Ix Ix R := V4 q * V4 q * V4 q

theorem V3_4_eq (q : R) :
    V3_4 q = fromBlocks (borromeanV3B q) 0 0 (borromeanV3A q) := by
  simp [V3_4, V4, s1, s2Inv, fromBlocks_multiply, borromeanV3B, borromeanVB, borromeanV3A,
    borromeanVA]

/-- **Arm L-A.** The spectator reading has equal sector traces. -/
theorem trN_V3_eq_trP_V3 (q : R) (hq : q ≠ 0) : trN (V3_4 q) = trP (V3_4 q) := by
  rw [trN, trP, V3_4_eq, toBlocks_fromBlocks₁₁, toBlocks_fromBlocks₂₂, trace_borromeanV3A q hq,
    trace_borromeanV3B q hq]

/-- The #8636 selected four-strand word `w = σ₁σ₃⁻¹`. -/
def w (q : R) : Matrix Ix Ix R := s1 q * s3Inv q

/-- **Arm L-B, neutron sector.** `tr_N(σ₁σ₃⁻¹) = 1`. -/
theorem trN_w (q : R) (hq : q ≠ 0) : trN (w q) = 1 := by
  simp [trN, w, s1, s3Inv, fromBlocks_multiply, B₁, Matrix.trace_fin_three, hq]

/-- **Arm L-B, proton sector.** `tr_P(σ₁σ₃⁻¹) = 1 − h²`. -/
theorem trP_w (q : R) (hq : q ≠ 0) : trP (w q) = 1 - (q - q⁻¹) ^ 2 := by
  simp [trP, w, s1, s3Inv, fromBlocks_multiply, A₁, E, Et, Matrix.trace_fin_three, hq]
  ring

/-- The two sector traces of `w` differ by `h²`: a first-order separation in `q − 1`. -/
theorem trN_w_sub_trP_w (q : R) (hq : q ≠ 0) : trN (w q) - trP (w q) = (q - q⁻¹) ^ 2 := by
  rw [trN_w q hq, trP_w q hq]; ring

/-- **Two-term, both arms.** On each sector the covariant all-pairs pair charge of every basis
state is the same scalar (`N`: `uddu, dudu, dduu` with charges `2/3, −1/3, −1/3, 0` in some order,
pair sum `−1/3`; `P`: `uudd, udud, duud` with `2/3, 2/3, −1/3, −1`, pair sum `−1`), so the
connected two-term insertion vanishes on any element `M`. -/
theorem twoTerm_connected_zero (h3 : (3 : R) ≠ 0) (M : Matrix Ix Ix R) :
    QOU.QuarkState.PairwiseChargeEnergyBeta.connTrace
        ((-1 / 3 : R) • (1 : Matrix (Fin 3) (Fin 3) R)) (toBlocks₁₁ M) = 0 ∧
      QOU.QuarkState.PairwiseChargeEnergyBeta.connTrace
        ((-1 : R) • (1 : Matrix (Fin 3) (Fin 3) R)) (toBlocks₂₂ M) = 0 :=
  ⟨QOU.QuarkState.PairwiseChargeEnergyBeta.connTrace_smul_one h3 _ _,
    QOU.QuarkState.PairwiseChargeEnergyBeta.connTrace_smul_one h3 _ _⟩

/-- **Reading L-B** (pre-registered conjecture, not claimed): the neutron's factor is the
sector-trace ratio of the selected word. -/
def NeutronIdentityLB (q mμ me mn FBor : R) : Prop :=
  mn = 2 * mμ * (FBor * (trN (w q) / trP (w q))) - 12 * me

/-- Under L-B the neutron factor is `1/(1 − h²)` exactly. -/
theorem LB_factor (q mμ me mn FBor : R) (hq : q ≠ 0) (h : NeutronIdentityLB q mμ me mn FBor) :
    mn = 2 * mμ * (FBor / (1 - (q - q⁻¹) ^ 2)) - 12 * me := by
  rw [h, trN_w q hq, trP_w q hq]; ring

end QOU.MassTheory.NeutronFourStrand
