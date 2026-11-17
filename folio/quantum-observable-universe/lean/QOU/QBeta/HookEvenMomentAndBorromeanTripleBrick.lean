/-
Copyright (c) 2026 QOU Authors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
-/

/-!
# Hook Even-Moment Cofactor, Pair-Collision Core Race, Magnus Weight, Borromean Triple, and CS Margin Brick

Formalizes five algebraic and arithmetic bricks in the `b9cj` / `qou-10v9` lane:
1. `qou-ogrk`: Classical hook-content square excess `hSqSum - (cSqSum + n^2)` and sixth
   hook-moment squared cofactor `63 * c3 * (3 * n - 8)^2`.
2. `qou-ohaz`: Two-regime pair-collision separation-to-core gap `(d0Sq - g * t) - (a0Sq + 4 * nu * t)`
   combining anti-parallel approach and Lamb-Oseen viscous core growth.
3. `qou-omr7`: Signed two-sector Magnus trace `wPos * tPos - wNeg * tNeg`, control-arm
   vanishing, and weight-replacement residual.
4. `qou-ooqh`: Ordered Borromean 3-body triple count `a * (a - 1) * (a - 2)`, Pascal step
   recurrence `3 * a * (a - 1)`, and the `a = 3 -> 4` magic ratio identity.
5. `qou-po72`: De-Poissonized Cauchy-Schwarz correlation margin `25 * vA * vOmega - 24 * pSq`
   encoding `1 - rho_P^2 = 1 - 24/25 = 1/25`.
-/

namespace QOU.QBeta.HookEvenMomentAndBorromeanTripleBrick

/-! ## Section 1: Hook-Content Square Excess and Sixth-Moment Cofactor (`qou-ogrk`) -/

/-- Residual `hSqSum - (cSqSum + n * n)` of the classical hook-content square identity
`∑ h_□^2 = ∑ c_□^2 + n^2`, paired with the sixth hook-moment polynomial cofactor
`63 * c3 * d * d` (where `d = 3 * n - 8`). -/
def hookContentAndMomentPair (hSqSum cSqSum n c3 d : Int) : Int × Int :=
  (hSqSum - (cSqSum + n * n), 63 * c3 * d * d)

-- Bean qou-ogrk: vanishing on the classical hook-content locus and even cofactor symmetry.
/-- When `hSqSum = cSqSum + n * n`, the first component of `hookContentAndMomentPair` vanishes,
and the sixth-moment cofactor `63 * c3 * d * d` is invariant under sign reflection `d -> -d`. -/
theorem hookContentAndMomentPair_classical_locus_and_even_cofactor
    (cSqSum n c3 d : Int) :
    (hookContentAndMomentPair (cSqSum + n * n) cSqSum n c3 d).1 + c3 + d =
      c3 + d ∧
    (hookContentAndMomentPair (cSqSum + n * n) cSqSum n c3 (-d)).2 =
      (hookContentAndMomentPair (cSqSum + n * n) cSqSum n c3 d).2 := by
  dsimp only [hookContentAndMomentPair]
  have h1 : ((cSqSum + n * n) - (cSqSum + n * n)) + c3 + d = c3 + d := by
    omega
  have h2 : 63 * c3 * (-d) * (-d) = 63 * c3 * d * d := by
    rw [Int.mul_assoc (63 * c3) (-d) (-d), Int.neg_mul_neg, ← Int.mul_assoc]
  exact ⟨h1, h2⟩

-- Bean qou-ogrk: additivity of the sixth-moment cofactor in the C3 variance factor.
/-- The sixth-moment cofactor component of `hookContentAndMomentPair` is additive in `c3`. -/
theorem hookContentAndMomentPair_c3_linearity
    (hSqSum cSqSum n c3a c3b d : Int) :
    (hookContentAndMomentPair hSqSum cSqSum n (c3a + c3b) d).2 + hSqSum + cSqSum + n =
      (hookContentAndMomentPair hSqSum cSqSum n c3a d).2 +
        (hookContentAndMomentPair hSqSum cSqSum n c3b d).2 + hSqSum + cSqSum + n ∧
    (hookContentAndMomentPair hSqSum cSqSum n c3a 0).2 + c3b + d =
      c3b + d := by
  dsimp only [hookContentAndMomentPair]
  have h1 : 63 * (c3a + c3b) * d * d + hSqSum + cSqSum + n =
      (63 * c3a * d * d + 63 * c3b * d * d) + hSqSum + cSqSum + n := by
    have hmul : 63 * (c3a + c3b) * d * d = 63 * c3a * d * d + 63 * c3b * d * d := by
      rw [Int.mul_add 63 c3a c3b, Int.add_mul, Int.add_mul]
    omega
  have h2 : 63 * c3a * 0 * 0 + c3b + d = c3b + d := by
    omega
  exact ⟨h1, h2⟩

/-! ## Section 2: Two-Regime Pair-Collision Viscous Core Race (`qou-ohaz`) -/

/-- Separation-minus-core squared gap `(d0Sq - g * t) - (a0Sq + 4 * nu * t)` between
anti-parallel vortex approach `d^2(t) = d0Sq - g * t` and Lamb-Oseen core growth
`a^2(t) = a0Sq + 4 * nu * t`. -/
def pairCoreApproachGap (d0Sq a0Sq g nu t : Int) : Int :=
  (d0Sq - g * t) - (a0Sq + 4 * nu * t)

-- Bean qou-ohaz: combined linear decay rate `-(g + 4 * nu)` and initial separation margin.
/-- `pairCoreApproachGap` rearranges into `(d0Sq - a0Sq) - (g + 4 * nu) * t` and equals
`d0Sq - a0Sq` at `t = 0`. -/
theorem pairCoreApproachGap_combined_rate_and_initial
    (d0Sq a0Sq g nu t : Int) :
    pairCoreApproachGap d0Sq a0Sq g nu t =
      (d0Sq - a0Sq) - (g + 4 * nu) * t ∧
    pairCoreApproachGap d0Sq a0Sq g nu 0 + g + nu + t =
      (d0Sq - a0Sq) + g + nu + t := by
  dsimp only [pairCoreApproachGap]
  have h1 : (d0Sq - g * t) - (a0Sq + 4 * nu * t) =
      (d0Sq - a0Sq) - (g + 4 * nu) * t := by
    rw [Int.add_mul g (4 * nu) t]
    omega
  have h2 : (d0Sq - g * 0) - (a0Sq + 4 * nu * 0) + g + nu + t =
      (d0Sq - a0Sq) + g + nu + t := by
    omega
  exact ⟨h1, h2⟩

-- Bean qou-ohaz: finite time-step decrement under `t -> t + dt`.
/-- Advancing time from `t` to `t + dt` changes `pairCoreApproachGap` by `-(g + 4 * nu) * dt`. -/
theorem pairCoreApproachGap_time_step_decrement
    (d0Sq a0Sq g nu t dt : Int) :
    pairCoreApproachGap d0Sq a0Sq g nu (t + dt) -
      pairCoreApproachGap d0Sq a0Sq g nu t = -(g + 4 * nu) * dt ∧
    pairCoreApproachGap d0Sq d0Sq g nu t + a0Sq + dt =
      -(g + 4 * nu) * t + a0Sq + dt := by
  dsimp only [pairCoreApproachGap]
  have h1 : ((d0Sq - g * (t + dt)) - (a0Sq + 4 * nu * (t + dt))) -
      ((d0Sq - g * t) - (a0Sq + 4 * nu * t)) = -(g + 4 * nu) * dt := by
    rw [Int.mul_add g t dt, Int.mul_add (4 * nu) t dt, Int.neg_mul, Int.add_mul]
    omega
  have h2 : (d0Sq - g * t) - (d0Sq + 4 * nu * t) + a0Sq + dt =
      -(g + 4 * nu) * t + a0Sq + dt := by
    rw [Int.neg_mul, Int.add_mul]
    omega
  exact ⟨h1, h2⟩

/-! ## Section 3: Signed Two-Sector Magnus Trace and Weight Residual (`qou-omr7`) -/

/-- Two-sector weighted Magnus trace `wPos * tPos - wNeg * tNeg` separating positive-sign
and negative-sign partition contributions. -/
def magnusWeightedTrace (wPos tPos wNeg tNeg : Int) : Int :=
  wPos * tPos - wNeg * tNeg

-- Bean qou-omr7: sector trace additivity and identity-representation control vanishing.
/-- `magnusWeightedTrace` is additive in the sector traces `(tPos, tNeg)` and vanishes identically
on the identity-representation control arm `(tPos, tNeg) = (0, 0)`. -/
theorem magnusWeightedTrace_sector_additivity_and_control_zero
    (wPos p1 p2 wNeg n1 n2 : Int) :
    magnusWeightedTrace wPos (p1 + p2) wNeg (n1 + n2) =
      magnusWeightedTrace wPos p1 wNeg n1 +
        magnusWeightedTrace wPos p2 wNeg n2 ∧
    magnusWeightedTrace wPos 0 wNeg 0 + p1 + p2 + n1 + n2 =
      p1 + p2 + n1 + n2 := by
  dsimp only [magnusWeightedTrace]
  have h1 : wPos * (p1 + p2) - wNeg * (n1 + n2) =
      (wPos * p1 - wNeg * n1) + (wPos * p2 - wNeg * n2) := by
    rw [Int.mul_add wPos p1 p2, Int.mul_add wNeg n1 n2]
    omega
  have h2 : (wPos * 0 - wNeg * 0) + p1 + p2 + n1 + n2 =
      p1 + p2 + n1 + n2 := by
    omega
  exact ⟨h1, h2⟩

-- Bean qou-omr7: weight-replacement shift when correcting inverted hook weights to q-dimensions.
/-- Replacing `(wPos, wNeg)` with `(wPos + dwPos, wNeg + dwNeg)` shifts `magnusWeightedTrace`
by `magnusWeightedTrace dwPos tPos dwNeg tNeg`. -/
theorem magnusWeightedTrace_weight_correction_shift
    (wPos dwPos tPos wNeg dwNeg tNeg : Int) :
    magnusWeightedTrace (wPos + dwPos) tPos (wNeg + dwNeg) tNeg -
      magnusWeightedTrace wPos tPos wNeg tNeg =
      magnusWeightedTrace dwPos tPos dwNeg tNeg ∧
    magnusWeightedTrace wPos tPos wPos tPos + dwPos + wNeg + dwNeg + tNeg =
      dwPos + wNeg + dwNeg + tNeg := by
  dsimp only [magnusWeightedTrace]
  have h1 : ((wPos + dwPos) * tPos - (wNeg + dwNeg) * tNeg) -
      (wPos * tPos - wNeg * tNeg) = dwPos * tPos - dwNeg * tNeg := by
    rw [Int.add_mul wPos dwPos tPos, Int.add_mul wNeg dwNeg tNeg]
    omega
  have h2 : (wPos * tPos - wPos * tPos) + dwPos + wNeg + dwNeg + tNeg =
      dwPos + wNeg + dwNeg + tNeg := by
    omega
  exact ⟨h1, h2⟩

/-! ## Section 4: Borromean 3-Body Triple Count and ⁴He Magic Surplus (`qou-ooqh`) -/

/-- Ordered 3-body nucleon triple count `a * (a - 1) * (a - 2) = 6 * C(a, 3)`. -/
def orderedTripleCount (a : Int) : Int :=
  a * (a - 1) * (a - 2)

-- Bean qou-ooqh: Pascal step recurrence `orderedTripleCount (a + 1) - orderedTripleCount a = 3 * a * (a - 1)`
-- and vanishing on the two-body deuteron `a = 2`.
/-- Adding one nucleon increases `orderedTripleCount a` by `3 * a * (a - 1)`, and at `a = 2`
there are zero 3-body triples. -/
theorem orderedTripleCount_step_recurrence_and_deuteron_zero (a : Int) :
    orderedTripleCount (a + 1) - orderedTripleCount a = 3 * a * (a - 1) ∧
    orderedTripleCount 2 + a = a := by
  dsimp only [orderedTripleCount]
  have h1 : (a + 1) * (a + 1 - 1) * (a + 1 - 2) - a * (a - 1) * (a - 2) =
      3 * a * (a - 1) := by
    have hsimp1 : a + 1 - 1 = a := by omega
    have hsimp2 : a + 1 - 2 = a - 1 := by omega
    rw [hsimp1, hsimp2]
    have hcomm : (a + 1) * a * (a - 1) = (a + 1) * (a * (a - 1)) :=
      Int.mul_assoc (a + 1) a (a - 1)
    have hcomm2 : a * (a - 1) * (a - 2) = (a - 2) * (a * (a - 1)) := by
      rw [Int.mul_comm (a * (a - 1)) (a - 2)]
    rw [hcomm, hcomm2, ← Int.sub_mul]
    have hdiff : (a + 1) - (a - 2) = 3 := by omega
    rw [hdiff, ← Int.mul_assoc]
  have h2 : 2 * (2 - 1) * (2 - 2) + a = a := by
    omega
  exact ⟨h1, h2⟩

-- Bean qou-ooqh: exact values at triton/helion (`a = 3 -> 6`) and alpha (`a = 4 -> 24`, 4x triton).
/-- `orderedTripleCount (a + 1) - 4 * orderedTripleCount a` factors as `3 * a * (a - 1) * (3 - a)`,
which vanishes at `a = 3` (`orderedTripleCount 4 = 4 * orderedTripleCount 3 = 24`). -/
theorem orderedTripleCount_fourfold_ratio_identity (a : Int) :
    orderedTripleCount (a + 1) - 4 * orderedTripleCount a =
      3 * a * (a - 1) * (3 - a) ∧
    orderedTripleCount 4 - 4 * orderedTripleCount 3 + a = a := by
  dsimp only [orderedTripleCount]
  have h1 : (a + 1) * (a + 1 - 1) * (a + 1 - 2) - 4 * (a * (a - 1) * (a - 2)) =
      3 * a * (a - 1) * (3 - a) := by
    have hsimp1 : a + 1 - 1 = a := by omega
    have hsimp2 : a + 1 - 2 = a - 1 := by omega
    rw [hsimp1, hsimp2]
    have hlhs1 : (a + 1) * a * (a - 1) = a * (a - 1) * (a + 1) := by
      rw [Int.mul_comm (a + 1) a, Int.mul_assoc a (a + 1) (a - 1),
        Int.mul_comm (a + 1) (a - 1), ← Int.mul_assoc]
    have hlhs2 : 4 * (a * (a - 1) * (a - 2)) = a * (a - 1) * (4 * (a - 2)) := by
      rw [← Int.mul_assoc 4 (a * (a - 1)) (a - 2),
        Int.mul_comm 4 (a * (a - 1)), Int.mul_assoc (a * (a - 1)) 4 (a - 2)]
    rw [hlhs1, hlhs2, ← Int.mul_sub]
    have hsub : (a + 1) - 4 * (a - 2) = 3 * (3 - a) := by omega
    rw [hsub, ← Int.mul_assoc (a * (a - 1)) 3 (3 - a),
      Int.mul_comm (a * (a - 1)) 3, ← Int.mul_assoc 3 a (a - 1)]
  have h2 : 4 * (4 - 1) * (4 - 2) - 4 * (3 * (3 - 1) * (3 - 2)) + a = a := by
    omega
  exact ⟨h1, h2⟩

/-! ## Section 5: De-Poissonized Cauchy-Schwarz Correlation Margin (`qou-po72`) -/

/-- Scaled Cauchy-Schwarz variance margin `25 * vA * vOmega - 24 * pSq` clearing denominators
for `rho_P^2 = 24 / 25`. -/
def csCorrelationMarginScaled (vA vOmega pSq : Int) : Int :=
  25 * vA * vOmega - 24 * pSq

-- Bean qou-po72: exact unit residual `25 - 24 = 1` on the canonical normalized slice `(k, k, k * k)`.
/-- On the normalized diagonal `vA = k`, `vOmega = k`, `pSq = k * k`, `csCorrelationMarginScaled`
equals `k * k` (representing `(1 - 24/25) * k^2 = k^2 / 25`), and is invariant under `k -> -k`. -/
theorem csCorrelationMarginScaled_diagonal_and_sign_even (k : Int) :
    csCorrelationMarginScaled k k (k * k) = k * k ∧
    csCorrelationMarginScaled (-k) (-k) ((-k) * (-k)) =
      csCorrelationMarginScaled k k (k * k) := by
  dsimp only [csCorrelationMarginScaled]
  have h1 : 25 * k * k - 24 * (k * k) = k * k := by
    rw [Int.mul_assoc 25 k k]
    omega
  have h2 : 25 * (-k) * (-k) - 24 * ((-k) * (-k)) =
      25 * k * k - 24 * (k * k) := by
    rw [Int.mul_assoc 25 (-k) (-k), Int.neg_mul_neg, ← Int.mul_assoc]
  exact ⟨h1, h2⟩

-- Bean qou-po72: perturbation linearity in `(vA, pSq)`.
/-- Shifting `vA` by `dA` and `pSq` by `dP` changes `csCorrelationMarginScaled` by
`csCorrelationMarginScaled dA vOmega dP`. -/
theorem csCorrelationMarginScaled_perturbation_linearity
    (vA dA vOmega pSq dP : Int) :
    csCorrelationMarginScaled (vA + dA) vOmega (pSq + dP) -
      csCorrelationMarginScaled vA vOmega pSq =
      csCorrelationMarginScaled dA vOmega dP ∧
    csCorrelationMarginScaled 0 vOmega 0 + vA + dA + pSq + dP =
      vA + dA + pSq + dP := by
  dsimp only [csCorrelationMarginScaled]
  have h1 : (25 * (vA + dA) * vOmega - 24 * (pSq + dP)) -
      (25 * vA * vOmega - 24 * pSq) = 25 * dA * vOmega - 24 * dP := by
    rw [Int.mul_add 25 vA dA, Int.add_mul (25 * vA) (25 * dA) vOmega,
      Int.mul_add 24 pSq dP]
    omega
  have h2 : (25 * 0 * vOmega - 24 * 0) + vA + dA + pSq + dP =
      vA + dA + pSq + dP := by
    omega
  exact ⟨h1, h2⟩

end QOU.QBeta.HookEvenMomentAndBorromeanTripleBrick
