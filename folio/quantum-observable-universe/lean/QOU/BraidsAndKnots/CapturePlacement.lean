import QOU.BraidsAndKnots.HydrogenCaptureWeightSpace
import QOU.QuarkState.OverStrandWeight

/-!
# Where the electron sits in the hydrogen capture braid: the reflection symmetry

Pre-registration: `computations/probes/hydrogen_capture_lean/PREREGISTRATION-placement.md`.

The four-strand capture braid of `HydrogenCaptureWeightSpace` gives `S = −h²[3]_q/q²` with the
proton on strands `0–2` (`capL`) and `+h²[3]_q/q²` with the proton on strands `1–3` (`capR`).
This file asks what structure relates the two placements.

**Reflection.** Let `Π = X^{⊗n} ∘ P_rev` (bit flip on every strand after reversing the strand
order). On two strands `Π` commutes with the Jimbo `Ř` (`PiTwo_mul_Rch`), so on `n` strands it
sends `σ_i` to `σ_{n−2−i}` with the crossing sign kept. On the two four-dimensional weight spaces
of `HydrogenCaptureWeightSpace` it is the identity matrix in that file's bases, so the statement is
letter by letter: `gA (i, b) = gB (rev i, b)` (`gA_eq_gB_rev`). Consequences, for every word:

* `wordA_flip`, `wordB_flip`: reflecting a word swaps its two weight-space matrices.
* `FplusR_flip`, `FminusR_flip`: `F(O₊)` with the proton on the right equals `−F(O₋)` with the
  proton on the left for the reflected word, and the other way round. This is the §46 mirror
  identity of the m_n own-identity notes, there checked on a computed family; here for all words,
  hence (the functional being linear) for every photon weight and gluon arm.
* `S_R_flip`: `S_R(flip w) = −S_L(w)`.
* `writhe_flip`: reflection keeps every inverse flag, so the negative capture stays negative.

**What `Π` does not preserve.** `Π T³ Π⁻¹ = −T³`, and it sends the weight `K = diag(q, q⁻¹)` to
`diag(q⁻¹, q)` (`PiTwo_mul_Kdiag`). The right partial trace with `diag(q, q⁻¹)` is Markov
(`OverStrandWeight.ptr_markov`); the **left** partial trace is Markov with `diag(q⁻¹, q)`
(`ptrL_markov`) and is not a scalar with `diag(q, q⁻¹)` (`ptrL_other_not_scalar`). So for the
fixed `Ř`, the Markov end and the weight come as a pair, and `Π` exchanges the two pairs.
`F` with the weight `K` inserted (`S2L`, `S2R`): `S2R K (flip w) = −S2L K⁻¹ (w)` (`S2R_flip`).

Reading (not a theorem): every structure tested commutes with `Π` once the Markov end, `K` and the
sign of `T³` are carried along. The placement is therefore fixed only relative to the Markov end.
The corpus puts new strands at the Markov end (`GammaGammaAtom`: nucleus strand 0, electron `k`
on strand `k`), which gives `capL`. That is the tower convention, not a consequence of `Π`-breaking
structure.

Generic field, `q ≠ 0`. No numerical value enters.
-/

namespace QOU.BraidsAndKnots.CapturePlacement

open Matrix QOU.BraidsAndKnots.HydrogenCaptureWeightSpace

variable {R : Type*} [Field R]

/-! ### Two strands: `Π`, the weight, and the two partial traces -/

/-- `Π = (X ⊗ X) ∘ swap` on `C² ⊗ C²`, basis `e₀₀, e₀₁, e₁₀, e₁₁`: `e₀₀ ↔ e₁₁`, the rest fixed. -/
def PiTwo : Matrix (Fin 4) (Fin 4) R := !![0, 0, 0, 1; 0, 1, 0, 0; 0, 0, 1, 0; 1, 0, 0, 0]

/-- The weight `K ⊗ K` with `K = diag(d₀, d₁)`. -/
def Kdiag (d₀ d₁ : R) : Matrix (Fin 4) (Fin 4) R :=
  !![d₀ * d₀, 0, 0, 0; 0, d₀ * d₁, 0, 0; 0, 0, d₁ * d₀, 0; 0, 0, 0, d₁ * d₁]

/-- **`Π` commutes with the Jimbo crossing.** On `n` strands this is `Π σ_i Π⁻¹ = σ_{n−2−i}`. -/
theorem PiTwo_mul_Rch (q : R) :
    PiTwo * QOU.QuarkState.OverStrandWeight.Rch q = QOU.QuarkState.OverStrandWeight.Rch q * PiTwo := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [PiTwo, QOU.QuarkState.OverStrandWeight.Rch, Matrix.mul_apply, Fin.sum_univ_four]

theorem PiTwo_mul_PiTwo : (PiTwo : Matrix (Fin 4) (Fin 4) R) * PiTwo = 1 := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [PiTwo, Matrix.mul_apply, Fin.sum_univ_four]

/-- **`Π` inverts the weight**: `Π (K ⊗ K) Π = K' ⊗ K'` with the two entries of `K` exchanged. -/
theorem PiTwo_mul_Kdiag (d₀ d₁ : R) :
    PiTwo * Kdiag d₀ d₁ * PiTwo = Kdiag d₁ d₀ := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [PiTwo, Kdiag, Matrix.mul_apply, Fin.sum_univ_four] <;> ring

/-- Partial quantum trace over the **first** factor with weight `diag(d₀, d₁)`. -/
def ptrL (d₀ d₁ : R) (M : Matrix (Fin 4) (Fin 4) R) : Matrix (Fin 2) (Fin 2) R :=
  !![d₀ * M 0 0 + d₁ * M 2 2, d₀ * M 0 1 + d₁ * M 2 3;
     d₀ * M 1 0 + d₁ * M 3 2, d₀ * M 1 1 + d₁ * M 3 3]

/-- **The left peel is Markov with the exchanged weight** `diag(q⁻¹, q)`, with the same `q²`. -/
theorem ptrL_markov (q : R) (hq : q ≠ 0) :
    ptrL q⁻¹ q (QOU.QuarkState.OverStrandWeight.Rch q) = (q ^ 2) • (1 : Matrix (Fin 2) (Fin 2) R) := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [ptrL, QOU.QuarkState.OverStrandWeight.Rch] <;> field_simp <;> ring

/-- **The left peel is not Markov with the right peel's weight** `diag(q, q⁻¹)` (for `q⁴ ≠ 1`). -/
theorem ptrL_other_not_scalar (q : R) (hq : q ≠ 0) (h4 : q ^ 4 ≠ 1) :
    ¬ ∃ c : R, ptrL q q⁻¹ (QOU.QuarkState.OverStrandWeight.Rch q) = c • (1 : Matrix (Fin 2) (Fin 2) R) := by
  rintro ⟨c, hc⟩
  have h00 := congrFun (congrFun hc 0) 0
  have h11 := congrFun (congrFun hc 1) 1
  simp [ptrL, QOU.QuarkState.OverStrandWeight.Rch] at h00 h11
  apply h4
  have e : q * q + q⁻¹ * (q - q⁻¹) = q⁻¹ * q := by rw [h11, ← h00]
  field_simp at e
  linear_combination e

/-! ### Four strands: reflection of words on the weight spaces -/

/-- Strand reflection of a letter: `σ_i^{±1} ↦ σ_{2−i}^{±1}`. -/
def flipLetter (l : Letter) : Letter := (l.1.rev, l.2)

/-- Strand reflection of a word. -/
def flipWord (w : List Letter) : List Letter := w.map flipLetter

/-- **`Π` on the weight spaces, letter by letter.** -/
theorem gA_eq_gB_rev (q : R) (l : Letter) : gA q l = gB q (flipLetter l) := by
  obtain ⟨i, b⟩ := l
  fin_cases i <;> cases b <;> rfl

theorem gB_eq_gA_rev (q : R) (l : Letter) : gB q l = gA q (flipLetter l) := by
  obtain ⟨i, b⟩ := l
  fin_cases i <;> cases b <;> rfl

theorem wordA_flip (q : R) (w : List Letter) : wordA q (flipWord w) = wordB q w := by
  induction w with
  | nil => rfl
  | cons l w ih =>
    simp only [flipWord, List.map_cons] at ih ⊢
    simp only [wordA, wordB, ih, gB_eq_gA_rev q l]

theorem wordB_flip (q : R) (w : List Letter) : wordB q (flipWord w) = wordA q w := by
  induction w with
  | nil => rfl
  | cons l w ih =>
    simp only [flipWord, List.map_cons] at ih ⊢
    simp only [wordA, wordB, ih, gA_eq_gB_rev q l]

/-- `F(O₊)` with the proton on strands `1–3` (electron strand `0`), one-one weight space. -/
def FplusR (WB : Matrix (Fin 4) (Fin 4) R) : R := WB 0 0 + WB 1 1 + WB 2 2
/-- `F(O₋)` with the proton on strands `1–3`, one-zero weight space. -/
def FminusR (WA : Matrix (Fin 4) (Fin 4) R) : R := -(WA 1 1 + WA 2 2 + WA 3 3)

/-- The orientation sum with the proton on the left. -/
def SL (q : R) (w : List Letter) : R := FplusL (wordB q w) + FminusL (wordA q w)
/-- The orientation sum with the proton on the right. -/
def SR (q : R) (w : List Letter) : R := FplusR (wordB q w) + FminusR (wordA q w)

/-- **Mirror identity, `O₊`**: right placement of the reflected word = `−F(O₋)` on the left. -/
theorem FplusR_flip (q : R) (w : List Letter) :
    FplusR (wordB q (flipWord w)) = -FminusL (wordA q w) := by
  simp only [FplusR, FminusL, wordB_flip]; ring

/-- **Mirror identity, `O₋`**. -/
theorem FminusR_flip (q : R) (w : List Letter) :
    FminusR (wordA q (flipWord w)) = -FplusL (wordB q w) := by
  simp only [FminusR, FplusL, wordA_flip]

/-- **The orientation sum flips under reflection, for every word.** -/
theorem SR_flip (q : R) (w : List Letter) : SR q (flipWord w) = -SL q w := by
  simp only [SR, SL, FplusR_flip, FminusR_flip]; ring

/-- `SR` here is the quantity of `HydrogenCaptureWeightSpace.capR_S`. -/
theorem SR_capR (q : R) (hq : q ≠ 0) (h3 : q ^ 4 + q ^ 2 + 1 ≠ 0) :
    SR q capR = (q ^ 2 - 1) ^ 2 * (q ^ 4 + q ^ 2 + 1) / q ^ 6 := by
  rw [← capR_S q hq h3]; simp only [SR, FplusR, FminusR]; ring

/-- The reflected left capture and the corpus right capture have the same orientation sum. -/
theorem SR_flip_capL_eq_SR_capR (q : R) (hq : q ≠ 0) (h3 : q ^ 4 + q ^ 2 + 1 ≠ 0) :
    SR q (flipWord capL) = SR q capR := by
  rw [SR_flip, SR_capR q hq h3, SL, capL_S q hq h3]; ring

/-- Reflection keeps every inverse flag (so the Hopf-closure orientation and the writhe). -/
theorem writhe_flip (w : List Letter) : (flipWord w).map Prod.snd = w.map Prod.snd := by
  simp [flipWord, flipLetter, Function.comp_def]

/-! ### The weighted functional `tr(T³ K W Π_O)` -/

/-- On these weight spaces `K = q^{2T³}` is the scalar `k₊` (one-one space, `T³ = +1`) or `k₋`
(one-zero space, `T³ = −1`); `K = diag(q, q⁻¹)` per strand gives `k₊ = q²`, `k₋ = q⁻²`. -/
def S2L (kp km q : R) (w : List Letter) : R := kp * FplusL (wordB q w) + km * FminusL (wordA q w)
def S2R (kp km q : R) (w : List Letter) : R := kp * FplusR (wordB q w) + km * FminusR (wordA q w)

/-- **Weighted mirror identity.** Reflection exchanges `K` with `K⁻¹` (`k₊ ↔ k₋`). -/
theorem S2R_flip (kp km q : R) (w : List Letter) :
    S2R kp km q (flipWord w) = -S2L km kp q w := by
  simp only [S2R, S2L, FplusR_flip, FminusR_flip]; ring

/-- With the same weight on both sides the two placements are **not** negatives: the defect is
`(k₊ − k₋)(F₊ − F₋)` of the left word. -/
theorem S2L_add_S2R_flip (kp km q : R) (w : List Letter) :
    S2L kp km q w + S2R kp km q (flipWord w)
      = (kp - km) * (FplusL (wordB q w) - FminusL (wordA q w)) := by
  simp only [S2R, S2L, FplusR_flip, FminusR_flip]; ring

end QOU.BraidsAndKnots.CapturePlacement
