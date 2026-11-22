/-
# Which word creates the β⁻ lepton pair: what the γγ grammar admits

Bean `qou-99qc` (task W, owner 2026-11-21: a proposal, for ruling, of the word that creates the
e⁻ν̄ pair). Companion probe `computations/probes/beta_pair_creation_word/` (pre-registered).

## Part A — word-level exclusions (scope (b), invariant: writhe)

`GammaGammaWord` (`QOU.Mass.GammaGammaWordSelection`, the `qou-ales` grammar) has writhe `0`
(`writhe_eq_zero`). So none of the corpus's odd-writhe lepton / weak objects is a γγ word:

* `passage_not_gammaGamma` : the derived charged-current passage `σ₀σ₁σ₂` (#8638), writhe 3;
* `trefoil_not_gammaGamma` : the electron knot `σ₀³` (`def:electron-knot`), writhe 3;
* `weakKnot_not_gammaGamma` : the weak knot `T(3,5) = (σ₁σ₂)⁵` on strands 1–3, writhe 10;
* `singleCrossing_not_gammaGamma` : the single lepton crossing `σ₂` (the bare W vertex of #8638
  Part A), writhe 1.

The word that IS admitted, and that the probe finds cost-minimal among γγ words with a non-zero
charged-current block and reading-3 feasibility: `borromeanLepton := V₁³ = (σ₁σ₂⁻¹)³`, the Borromean
core moved to strands 1–3 (two nucleon strands and the lepton strand). `borromeanLepton_isGammaGamma`.

## Part B — its charged-current block (exact, generic field)

On the two-`u` sector of `V^{⊗4}` (basis `uudd, udud, uddu, duud, dudu, dduu`, the matrices
`S1, S2, S3` of `ChargedCurrentW.lean`, #8638, restated so this part needs Mathlib only), the process
`W = V₁³ · β_Bor` acts by `ρ(W) = (S2·S3⁻¹)³ (S1·S2⁻¹)³` (nucleon braid first). Both factors are pure
braids, so position labels are strand labels. `cc_column_udd` computes `ρ(W)` on the input
`n ⊗ ν = udd ⊗ u` exactly; its `p ⊗ e⁻` components (indices 3, 1, 0 = `duu·d, udu·d, uud·d`) are the
column of the β block:

  `(q²−1)⁴(q⁴−q²+2)/q⁴`, `(q²−1)²(q³−q−1)(q³−q+1)(q⁶−2q⁴+3q²−1)/q⁹`,
  `(q²−1)²(q⁴−q²+1)(q⁶−2q⁴+3q²−1)/q⁸`.

Every entry carries `(q²−1)² = (hq)²`, so the block is `O(h²)` and vanishes at `q = 1`
(`cc_column_at_one`). Non-zero at `q = 2` (`cc_column_ne_zero_at_two`), so the block is not
identically zero.

## What is NOT claimed

* That `V₁³` is THE pair-creation word. The cost-minimality behind it is measured over a stated
  finite family in the probe (γγ words of length ≤ 8 on four strands), and reading 3 is evaluated
  numerically at `q₀`; neither is proved here. With mirror vertices allowed, eight words tie.
* The lepton labels `ν = u, e⁻ = d` on the fourth strand (premise L, #8673) are an assumption.
* No energy, no `Q_β`. Nothing here reads CODATA.

Base ring (§7c): Part A is combinatorics; Part B is generic `[Field K]`. No `ℝ`, no `sorry`.

-- Ref: [jimbo1986] https://doi.org/10.1007/BF00400222
-- Ref: [jones1987] https://doi.org/10.2307/1971403
-/
import QOU.Mass.GammaGammaWordSelection
import Mathlib.Data.Matrix.Mul
import Mathlib.LinearAlgebra.Matrix.Notation
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.FinCases
import Mathlib.Tactic.Ring

namespace QOU.QBeta.PairCreationWordGammaGamma

open QOU.Mass.GammaGammaWordSelection Matrix

/-! ## Part A — words -/

/-- `σᵢ` and `σᵢ⁻¹` as crossings. -/
def pos (i : ℕ) : Crossing := ⟨i, true⟩
def neg (i : ℕ) : Crossing := ⟨i, false⟩

/-- The derived charged-current passage `σ₀σ₁σ₂` (#8638, leftward positive). -/
def passage : Word := [pos 0, pos 1, pos 2]
/-- The electron trefoil `σ₀³`. -/
def trefoil : Word := [pos 0, pos 0, pos 0]
/-- The weak knot `T(3,5) = (σ₁σ₂)⁵`, on strands 1–3. -/
def weakKnot : Word := List.flatten (List.replicate 5 [pos 1, pos 2])
/-- The single lepton crossing `σ₂`. -/
def singleCrossing : Word := [pos 2]
/-- `V₁³ = (σ₁σ₂⁻¹)³`: the Borromean core on strands 1–3. -/
def borromeanLepton : Word := vertex 1 ++ vertex 1 ++ vertex 1

theorem not_gammaGamma_of_writhe_ne {w : Word} (h : writhe w ≠ 0) : ¬ GammaGammaWord w :=
  fun hg => h (writhe_eq_zero hg)

theorem passage_not_gammaGamma : ¬ GammaGammaWord passage :=
  not_gammaGamma_of_writhe_ne (by decide)

theorem trefoil_not_gammaGamma : ¬ GammaGammaWord trefoil :=
  not_gammaGamma_of_writhe_ne (by decide)

theorem weakKnot_not_gammaGamma : ¬ GammaGammaWord weakKnot :=
  not_gammaGamma_of_writhe_ne (by decide)

theorem singleCrossing_not_gammaGamma : ¬ GammaGammaWord singleCrossing :=
  not_gammaGamma_of_writhe_ne (by decide)

theorem borromeanLepton_isGammaGamma : GammaGammaWord borromeanLepton := by
  unfold borromeanLepton
  rw [List.append_assoc]
  exact .cons 1 (.cons 1 (by simpa using GammaGammaWord.cons 1 GammaGammaWord.nil))

/-- The writhe of the passage is `3`, of `T(3,5)` is `10`. -/
theorem writhe_passage : writhe passage = 3 := by decide
theorem writhe_weakKnot : writhe weakKnot = 10 := by decide

/-! ## Part B — the charged-current block of `V₁³ · β_Bor` -/

section Sector

variable {K : Type*} [Field K] {q : K}

/-- `σ₁` (1-based; `σ₀` 0-based) on the two-`u` sector. -/
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

/-- `σ₂⁻¹ = σ₂ − h`. -/
def S2i (q : K) : Matrix (Fin 6) (Fin 6) K := S2 q - (q - q⁻¹) • (1 : Matrix (Fin 6) (Fin 6) K)
/-- `σ₃⁻¹ = σ₃ − h`. -/
def S3i (q : K) : Matrix (Fin 6) (Fin 6) K := S3 q - (q - q⁻¹) • (1 : Matrix (Fin 6) (Fin 6) K)

/-- `ρ(V₁³ · β_Bor) = (S2·S3⁻¹)³ (S1·S2⁻¹)³`. -/
def rhoW (q : K) : Matrix (Fin 6) (Fin 6) K :=
  S2 q * S3i q * (S2 q * S3i q) * (S2 q * S3i q) * (S1 q * S2i q * (S1 q * S2i q) * (S1 q * S2i q))

local macro "vec6" M:ident u:ident v:ident : tactic =>
  `(tactic| (ext i; fin_cases i <;>
    simp [$M:ident, $u:ident, $v:ident, S2i, S3i, S1, S2, S3, Matrix.mulVec, dotProduct,
      Fin.sum_univ_succ, Matrix.sub_apply, Matrix.smul_apply, Matrix.one_apply] <;>
    (try field_simp) <;> (try ring)))

/-- State after 0 letters. -/
def w0 (q : K) : Fin 6 → K := ![0, 0, 1, 0, 0, 0]

/-- State after 1 letters. -/
def w1 (q : K) : Fin 6 → K := ![0, 0, 1/q, 0, 0, 0]

/-- State after 2 letters. -/
def w2 (q : K) : Fin 6 → K := ![0, 0, 0, 0, 1/q, 0]

/-- State after 3 letters. -/
def w3 (q : K) : Fin 6 → K := ![0, 0, 0, 0, -(q - 1)*(q + 1)/q^2, 1/q]

/-- State after 4 letters. -/
def w4 (q : K) : Fin 6 → K := ![0, 0, -(q - 1)*(q + 1)/q^2, 0, -(q - 1)^2*(q + 1)^2/q^3, 1]

/-- State after 5 letters. -/
def w5 (q : K) : Fin 6 → K := ![0, 0, -(q - 1)*(q + 1)/q^3, 0, (q^6 - 2*q^4 + 3*q^2 - 1)/q^4, -(q - 1)^2*(q + 1)^2/q^3]

/-- State after 6 letters. -/
def w6 (q : K) : Fin 6 → K := ![0, 0, (q^6 - 2*q^4 + 3*q^2 - 1)/q^4, 0, (q - 1)^2*(q + 1)^2*(q^4 - q^2 + 1)/q^5, -(q - 1)^2*(q + 1)^2/q^2]

/-- State after 7 letters. -/
def w7 (q : K) : Fin 6 → K := ![0, (q^6 - 2*q^4 + 3*q^2 - 1)/q^4, 0, (q - 1)^2*(q + 1)^2*(q^4 - q^2 + 1)/q^5, 0, -(q - 1)^2*(q + 1)^2/q^3]

/-- State after 8 letters. -/
def w8 (q : K) : Fin 6 → K := ![(q^6 - 2*q^4 + 3*q^2 - 1)/q^4, (q - 1)*(q + 1)*(q^6 - 2*q^4 + 3*q^2 - 1)/q^5, 0, (q - 1)^2*(q + 1)^2*(q^4 - q^2 + 1)/q^4, -(q - 1)^2*(q + 1)^2/q^3, -(q - 1)^3*(q + 1)^3/q^4]

/-- State after 9 letters. -/
def w9 (q : K) : Fin 6 → K := ![(q^6 - 2*q^4 + 3*q^2 - 1)/q^5, -(q - 1)^2*(q + 1)^2*(q^6 - 2*q^4 + 3*q^2 - 1)/q^6, (q - 1)*(q + 1)*(q^6 - 2*q^4 + 3*q^2 - 1)/q^5, -(q - 1)^2*(q + 1)^2*(q^6 - 2*q^4 + 3*q^2 - 1)/q^5, (q - 1)^2*(q + 1)^2*(q^4 - q^2 + 1)/q^4, -(q - 1)^3*(q + 1)^3/q^5]

/-- State after 10 letters. -/
def w10 (q : K) : Fin 6 → K := ![-(q - 1)^2*(q + 1)^2*(q^6 - 2*q^4 + 3*q^2 - 1)/q^6, -(q^6 - 3*q^4 + 2*q^2 - 1)*(q^6 - 2*q^4 + 3*q^2 - 1)/q^7, (q - 1)*(q + 1)*(q^6 - 2*q^4 + 3*q^2 - 1)/q^4, -(q - 1)^2*(q + 1)^2*(q^6 - 2*q^4 + 3*q^2 - 1)/q^4, -(q - 1)^3*(q + 1)^3/q^5, (q - 1)^2*(q + 1)^2*(q^6 - 2*q^4 + 3*q^2 - 1)/q^6]

/-- State after 11 letters. -/
def w11 (q : K) : Fin 6 → K := ![-(q - 1)^2*(q + 1)^2*(q^6 - 2*q^4 + 3*q^2 - 1)/q^7, (q - 1)^2*(q + 1)^2*(q^4 - q^2 + 1)*(q^6 - 2*q^4 + 3*q^2 - 1)/q^8, -(q^6 - 3*q^4 + 2*q^2 - 1)*(q^6 - 2*q^4 + 3*q^2 - 1)/q^7, (q - 1)^4*(q + 1)^4*(q^4 - q^2 + 2)/q^5, -(q - 1)^2*(q + 1)^2*(q^6 - 2*q^4 + 3*q^2 - 1)/q^4, (q - 1)^2*(q + 1)^2*(q^6 - 2*q^4 + 3*q^2 - 1)/q^7]

/-- State after 12 letters. -/
def w12 (q : K) : Fin 6 → K := ![(q - 1)^2*(q + 1)^2*(q^4 - q^2 + 1)*(q^6 - 2*q^4 + 3*q^2 - 1)/q^8, (q - 1)^2*(q + 1)^2*(q^3 - q - 1)*(q^3 - q + 1)*(q^6 - 2*q^4 + 3*q^2 - 1)/q^9, -(q^6 - 3*q^4 + 2*q^2 - 1)*(q^6 - 2*q^4 + 3*q^2 - 1)/q^6, (q - 1)^4*(q + 1)^4*(q^4 - q^2 + 2)/q^4, (q - 1)^2*(q + 1)^2*(q^6 - 2*q^4 + 3*q^2 - 1)/q^7, -(q - 1)^2*(q + 1)^2*(q^4 - q^2 + 1)*(q^6 - 2*q^4 + 3*q^2 - 1)/q^8]

theorem step1 (hq : q ≠ 0) : S2i q *ᵥ w0 q = w1 q := by
  vec6 S2i w0 w1

theorem step2 (hq : q ≠ 0) : S1 q *ᵥ w1 q = w2 q := by
  vec6 S1 w1 w2

theorem step3 (hq : q ≠ 0) : S2i q *ᵥ w2 q = w3 q := by
  vec6 S2i w2 w3

theorem step4 (hq : q ≠ 0) : S1 q *ᵥ w3 q = w4 q := by
  vec6 S1 w3 w4

theorem step5 (hq : q ≠ 0) : S2i q *ᵥ w4 q = w5 q := by
  vec6 S2i w4 w5

theorem step6 (hq : q ≠ 0) : S1 q *ᵥ w5 q = w6 q := by
  vec6 S1 w5 w6

theorem step7 (hq : q ≠ 0) : S3i q *ᵥ w6 q = w7 q := by
  vec6 S3i w6 w7

theorem step8 (hq : q ≠ 0) : S2 q *ᵥ w7 q = w8 q := by
  vec6 S2 w7 w8

theorem step9 (hq : q ≠ 0) : S3i q *ᵥ w8 q = w9 q := by
  vec6 S3i w8 w9

theorem step10 (hq : q ≠ 0) : S2 q *ᵥ w9 q = w10 q := by
  vec6 S2 w9 w10

theorem step11 (hq : q ≠ 0) : S3i q *ᵥ w10 q = w11 q := by
  vec6 S3i w10 w11

theorem step12 (hq : q ≠ 0) : S2 q *ᵥ w11 q = w12 q := by
  vec6 S2 w11 w12

/-- **`ρ(V₁³·β_Bor)` on the input `n ⊗ ν = udd ⊗ u`.** -/
theorem cc_column_udd (hq : q ≠ 0) : rhoW q *ᵥ w0 q = w12 q := by
  simp only [rhoW, ← Matrix.mulVec_mulVec, Matrix.mul_assoc]
  rw [step1 hq, step2 hq, step3 hq, step4 hq, step5 hq, step6 hq, step7 hq, step8 hq, step9 hq,
    step10 hq, step11 hq, step12 hq]

/-- **The β-block column vanishes at `q = 1`** (each entry carries `(q² − 1)²`). -/
theorem cc_column_at_one :
    w12 (1 : K) 3 = 0 ∧ w12 (1 : K) 1 = 0 ∧ w12 (1 : K) 0 = 0 := by
  simp [w12]

end Sector

/-- **The block is not identically zero:** the `duu·d` entry at `q = 2` is `81·14/16`. -/
theorem cc_column_ne_zero_at_two : w12 (2 : ℚ) 3 ≠ 0 := by
  simp [w12]; norm_num

end QOU.QBeta.PairCreationWordGammaGamma
