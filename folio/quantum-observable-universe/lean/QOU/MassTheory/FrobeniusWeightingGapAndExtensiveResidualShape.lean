/-
Copyright (c) 2026 QOU Authors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: QOU Formalization Lane
-/

namespace QOU.MassTheory.FrobeniusWeightingGapAndExtensiveResidualShape

/-!
# Partition-Weighting Gap $y_\lambda \chi^\lambda$ & Super-Pairwise Extensive Residual Shape (`qou-gnow`, `qou-j3bs`)

This module formalizes two structural results under `qou-v2om`:

1. **`qou-gnow` (Magnitude Attack A — Gap Between One-Row Chain $\chi^{[3]}$ and Full 3-Partition Weighted Pairing):**
   - For the three 3-strand irreducible partitions $\lambda \in \{[3], [2,1], [1,1,1]\}$
     with dimensions $d_{[3]} = 1, d_{[2,1]} = 2, d_{[1,1,1]} = 1$ and partition
     weights $y_{[3]}, y_{[2,1]}, y_{[1,1,1]}$ satisfying $y_{[3]} + 2 y_{[2,1]} + y_{[1,1,1]} = 1$,
     clearing denominators by $W = w_1 + 2 w_2 + w_3$ decomposes the difference between
     the one-row character $W \cdot \chi_{[3]}$ and the full weighted pairing
     $T_{\mathrm{weighted}} = w_1 \chi_{[3]} + w_2 \chi_{[2,1]} + w_3 \chi_{[1,1,1]}$ as:
     $$W \cdot \chi_{[3]} - T_{\mathrm{weighted}}
       = w_2 \bigl(2 \chi_{[3]} - \chi_{[2,1]}\bigr) + w_3 \bigl(\chi_{[3]} - \chi_{[1,1,1]}\bigr).$$
   - Whenever the non-trivial channels satisfy $2 \chi_{[3]} > \chi_{[2,1]}$ and
     $\chi_{[3]} > \chi_{[1,1,1]}$ with positive weights $w_2, w_3 > 0$, the full
     weighted pairing is strictly smaller than the unweighted one-row baseline $W \cdot \chi_{[3]}$.

2. **`qou-j3bs` (Magnitude Attack B — Non-Monotonicity of the Extensive Residual $R(A)/A = B_{\mathrm{AME}}/A - 2.998$):**
   - Relative to the $2.998\,\mathrm{MeV}$ ($2998\,\mathrm{keV}$) pairwise chain baseline,
     the extensive per-nucleon residual $r(A) = B_{\mathrm{AME}}(A)/A - 2998$ (in keV)
     across the benchmark sequence $^2\mathrm{H}$ ($A=2, B/A=1112$), $^4\mathrm{He}$
     ($A=4, B/A=7074$), $^{56}\mathrm{Fe}$ ($A=56, B/A=8790$), and $^{238}\mathrm{U}$
     ($A=238, B/A=7570$) satisfies:
     - sign inversion between $A = 2$ ($r(2) = -1886 < 0$) and $A \ge 4$ ($r(4) = +4076 > 0$);
     - interior peak at $^{56}\mathrm{Fe}$ ($r(4) < r(56) = 5792$ and $r(56) > r(238) = 4572$),
       proving that no monotone function of $A$ alone can close $R(A)/A$ across $A = 2 \dots 238$.
-/

/-- Cleared weight normalization $W = w_1 + 2 w_2 + w_3$ for 3-strand partition weights (`qou-gnow`). -/
def h3WeightTotal (w1 w2 w3 : Int) : Int :=
  w1 + 2 * w2 + w3

/-- Cleared 3-partition weighted pairing $w_1 \chi_{[3]} + w_2 \chi_{[2,1]} + w_3 \chi_{[1,1,1]}$ (`qou-gnow`). -/
def h3WeightedPairing (w1 w2 w3 chi3 chi21 chi111 : Int) : Int :=
  w1 * chi3 + w2 * chi21 + w3 * chi111

/-- Exact decomposition of the gap between the one-row baseline $W \cdot \chi_{[3]}$ and
the full 3-partition weighted pairing (`qou-gnow`), and strict positivity when the mixed
and sign characters lie below the one-row bound. -/
theorem h3OneRow_minus_weightedPairing_decomp
    (w1 w2 w3 chi3 chi21 chi111 : Int)
    (hw2 : w2 > 0) (hw3 : w3 > 0)
    (h21 : 2 * chi3 > chi21) (h111 : chi3 > chi111) :
    h3WeightTotal w1 w2 w3 * chi3 - h3WeightedPairing w1 w2 w3 chi3 chi21 chi111 =
      w2 * (2 * chi3 - chi21) + w3 * (chi3 - chi111) ∧
      h3WeightTotal w1 w2 w3 * chi3 > h3WeightedPairing w1 w2 w3 chi3 chi21 chi111 := by
  have hEq :
      h3WeightTotal w1 w2 w3 * chi3 - h3WeightedPairing w1 w2 w3 chi3 chi21 chi111 =
        w2 * (2 * chi3 - chi21) + w3 * (chi3 - chi111) := by
    dsimp [h3WeightTotal, h3WeightedPairing]
    rw [Int.add_mul, Int.add_mul, Int.mul_assoc 2 w2 chi3, Int.mul_left_comm 2 w2 chi3]
    rw [Int.mul_sub, Int.mul_sub]
    omega
  have hPos2 : w2 * (2 * chi3 - chi21) > 0 := Int.mul_pos hw2 (by omega)
  have hPos3 : w3 * (chi3 - chi111) > 0 := Int.mul_pos hw3 (by omega)
  refine ⟨hEq, ?_⟩
  omega

/-- Pairwise chain baseline per nucleon in keV ($2.998\,\mathrm{MeV} = 2998\,\mathrm{keV}$) (`qou-j3bs`). -/
def chainBaselineKeV : Int := 2998

/-- Per-nucleon residual $r(A) = (B_{\mathrm{AME}}/A)_{\mathrm{keV}} - 2998$ (`qou-j3bs`). -/
def perNucleonResidualKeV (bOverAKeV : Int) : Int :=
  bOverAKeV - chainBaselineKeV

/-- Representative benchmark $B_{\mathrm{AME}}/A$ values in keV across $A = 2 \dots 238$ (`qou-j3bs`). -/
def bOverADeuteronKeV : Int := 1112
def bOverAHelium4KeV : Int := 7074
def bOverAIron56KeV : Int := 8790
def bOverAUranium238KeV : Int := 7570

/-- Sign flip between $A = 2$ and $A = 4$ and interior-maximum non-monotonicity of the
extensive residual $R(A)/A$ across $A = 2, 4, 56, 238$ (`qou-j3bs`). -/
theorem perNucleonResidual_sign_flip_and_interior_peak :
    perNucleonResidualKeV bOverADeuteronKeV = -1886 ∧
      perNucleonResidualKeV bOverAHelium4KeV = 4076 ∧
      perNucleonResidualKeV bOverAIron56KeV = 5792 ∧
      perNucleonResidualKeV bOverAUranium238KeV = 4572 ∧
      perNucleonResidualKeV bOverADeuteronKeV < 0 ∧
      perNucleonResidualKeV bOverAHelium4KeV > 0 ∧
      perNucleonResidualKeV bOverAHelium4KeV < perNucleonResidualKeV bOverAIron56KeV ∧
      perNucleonResidualKeV bOverAIron56KeV > perNucleonResidualKeV bOverAUranium238KeV := by
  dsimp [perNucleonResidualKeV, chainBaselineKeV,
    bOverADeuteronKeV, bOverAHelium4KeV, bOverAIron56KeV, bOverAUranium238KeV]
  refine ⟨rfl, rfl, rfl, rfl, by decide, by decide, by decide, by decide⟩

end QOU.MassTheory.FrobeniusWeightingGapAndExtensiveResidualShape
