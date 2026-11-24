import QOU.Nuclear.HydrogenFlavourSplit
import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Positivity

/-!
# The neutron is never heavier at the Markov end, and the capture is a block reweighting

Continues `QOU.QBeta.HydrogenFlavourSplit` (ruled functional `E_c = Tr(K^{⊗4}Π_c W)/[2]⁴`,
nucleon on strands `0–2`, the extra strand on the right, i.e. at the end where the K-weighted
partial trace is Markov). Owner ruling 2026-11-22 (reading A with right-hand closure) puts a
newly added strand on the right, which is this placement.

**Sign, for every four-strand word** (ordered field, `1 < q`):
* `eps_eq_one_sub_mul_tp`: `tp − tn = (1 − q⁻²)·tp`, so the split has the sign of `tp`;
* `left_abs_tn_le` / `left_abs_tn_lt`: `|tn| ≤ |tp|`, strictly when `tp ≠ 0`;
* `left_increasing_reading_neutron_lighter`: every strictly increasing reading of the absolute
  sector trace makes the neutron lighter, whatever the capture word;
* `left_signed_reading_iff`: under the signed reading the neutron is heavier iff `tp < 0`.

**Capture factors** (generic field). With `ε(V³)` the three-strand split,
* `wAL_eps_eq_factor`: the adjacent capture multiplies it by `c_adj = (q⁴+1)/(q²(q²+1))`;
* `wL_eps_eq_blocks`: the cabled capture multiplies the `(3)` block of `ε(V³)` by
  `c₃ = (q⁸+1)/(q⁶(q²+1))` and the `(2,1)` block by `c₂₁ = (q⁴+1)/(q⁴(q²+1))`.
These are identities between the closed forms proved in `HydrogenFlavourSplit`. The mechanism
(the normalised K-partial trace of the capture word is a scalar, resp. central in the
three-strand braid image) is checked exactly in
`computations/probes/np_splitting/np_capture_conditional_expectation_probe.py` and is not
formalised here.
-/

namespace QOU.QBeta.HydrogenCaptureFactor

open QOU.QBeta.HydrogenFlavourSplit

section Sign

variable {R : Type*} [Field R] [LinearOrder R] [IsStrictOrderedRing R]

theorem eps_eq_one_sub_mul_tp {q : R} (hq : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0) (w : List Letter) :
    tpL q (word1 q w) (word3 q w) (word2 q w) - tnL q (word1 q w) (word3 q w) (word2 q w)
      = (1 - q⁻¹ ^ 2) * tpL q (word1 q w) (word3 q w) (word2 q w) := by
  rw [left_ratio q hq h2 w]; ring

theorem invsq_lt_one {q : R} (hq : 1 < q) : q⁻¹ ^ 2 < 1 := by
  have h0 : 0 < q⁻¹ := inv_pos.mpr (lt_trans zero_lt_one hq)
  have h1 : q⁻¹ < 1 := inv_lt_one_of_one_lt₀ hq
  nlinarith

theorem h2_ne {q : R} (hq : 1 < q) : q ^ 2 + 1 ≠ 0 := by positivity

theorem left_abs_tn_le {q : R} (hq : 1 < q) (w : List Letter) :
    |tnL q (word1 q w) (word3 q w) (word2 q w)| ≤ |tpL q (word1 q w) (word3 q w) (word2 q w)| := by
  have hq0 : q ≠ 0 := ne_of_gt (lt_trans zero_lt_one hq)
  rw [left_ratio q hq0 (h2_ne hq) w, abs_mul, abs_of_pos (pow_pos (inv_pos.mpr (lt_trans zero_lt_one hq)) 2)]
  have := invsq_lt_one hq
  have ha := abs_nonneg (tpL q (word1 q w) (word3 q w) (word2 q w))
  nlinarith

theorem left_abs_tn_lt {q : R} (hq : 1 < q) (w : List Letter)
    (ht : tpL q (word1 q w) (word3 q w) (word2 q w) ≠ 0) :
    |tnL q (word1 q w) (word3 q w) (word2 q w)| < |tpL q (word1 q w) (word3 q w) (word2 q w)| := by
  have hq0 : q ≠ 0 := ne_of_gt (lt_trans zero_lt_one hq)
  rw [left_ratio q hq0 (h2_ne hq) w, abs_mul, abs_of_pos (pow_pos (inv_pos.mpr (lt_trans zero_lt_one hq)) 2)]
  have := invsq_lt_one hq
  have ha := abs_pos.mpr ht
  nlinarith

/-- **Every strictly increasing reading makes the neutron lighter, for every word**, with the
extra strand at the Markov end. -/
theorem left_increasing_reading_neutron_lighter {q : R} (hq : 1 < q) (w : List Letter)
    (ht : tpL q (word1 q w) (word3 q w) (word2 q w) ≠ 0) (f : R → R) (hf : StrictMono f) :
    f |tnL q (word1 q w) (word3 q w) (word2 q w)| < f |tpL q (word1 q w) (word3 q w) (word2 q w)| :=
  hf (left_abs_tn_lt hq w ht)

/-- **Signed reading**: the neutron sector exceeds the proton sector iff `tp < 0`. -/
theorem left_signed_reading_iff {q : R} (hq : 1 < q) (w : List Letter) :
    tpL q (word1 q w) (word3 q w) (word2 q w) < tnL q (word1 q w) (word3 q w) (word2 q w)
      ↔ tpL q (word1 q w) (word3 q w) (word2 q w) < 0 := by
  have hq0 : q ≠ 0 := ne_of_gt (lt_trans zero_lt_one hq)
  rw [left_ratio q hq0 (h2_ne hq) w]
  have h1 := invsq_lt_one hq
  have h0 : (0 : R) < q⁻¹ ^ 2 := pow_pos (inv_pos.mpr (lt_trans zero_lt_one hq)) 2
  constructor
  · intro h; nlinarith
  · intro h; nlinarith

end Sign

section Capture

variable {R : Type*} [Field R]

/-- `ε(V³) = E_p − E_n` on three strands (FlavourWeightSplit: `−fV3`). -/
def epsV3 (q : R) : R :=
  -((q ^ 2 - 1) * (q ^ 12 - 3 * q ^ 10 + 3 * q ^ 8 - 5 * q ^ 6 + 3 * q ^ 4 - 3 * q ^ 2 + 1)
    / (q ^ 4 * (q ^ 2 + 1) ^ 3))

/-- The `(3)` block of `ε(V³)`: `V³` acts as `1` there, so it is `h/[2]³`. -/
def epsV3Sym (q : R) : R := q ^ 2 * (q ^ 2 - 1) / (q ^ 2 + 1) ^ 3

/-- The `(2,1)` block of `ε(V³)`. -/
def epsV3Std (q : R) : R :=
  -((q ^ 2 - 1) * (q ^ 4 - q ^ 2 + 1) * (q ^ 8 - 2 * q ^ 6 - 2 * q ^ 2 + 1)
    / (q ^ 4 * (q ^ 2 + 1) ^ 3))

def cAdj (q : R) : R := (q ^ 4 + 1) / (q ^ 2 * (q ^ 2 + 1))
def cSym (q : R) : R := (q ^ 8 + 1) / (q ^ 6 * (q ^ 2 + 1))
def cStd (q : R) : R := (q ^ 4 + 1) / (q ^ 4 * (q ^ 2 + 1))

theorem blocks_sum (q : R) (hq : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0) :
    epsV3Sym q + epsV3Std q = epsV3 q := by
  unfold epsV3Sym epsV3Std epsV3; field_simp; ring

theorem wAL_eps_eq_factor (q : R) (hq : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0) :
    (tpL q (word1 q wAL) (word3 q wAL) (word2 q wAL) - tnL q (word1 q wAL) (word3 q wAL) (word2 q wAL))
      / (q + q⁻¹) ^ 4 = cAdj q * epsV3 q := by
  rw [wAL_eps q hq h2]; unfold cAdj epsV3; field_simp; ring

theorem wL_eps_eq_blocks (q : R) (hq : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0) :
    (tpL q (word1 q wL) (word3 q wL) (word2 q wL) - tnL q (word1 q wL) (word3 q wL) (word2 q wL))
      / (q + q⁻¹) ^ 4 = cSym q * epsV3Sym q + cStd q * epsV3Std q := by
  rw [wL_eps q hq h2]; unfold cSym epsV3Sym cStd epsV3Std; field_simp; ring

end Capture

end QOU.QBeta.HydrogenCaptureFactor
