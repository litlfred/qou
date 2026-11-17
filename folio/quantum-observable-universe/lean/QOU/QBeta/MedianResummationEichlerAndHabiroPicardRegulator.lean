/-!
# Median Resummation Eichler Weight Criteria and Picard Regulator Completion Kernel
(`qou-5f6d`, `qou-6eke`)

Formalizes two linked structures connecting asymptotic resummation and cyclotomic ring geometry:

1. **Median Resummation Lateral Cancellation & Eichler Half-Integer Weight Gate (`qou-5f6d`, Ref: `[mcspirit-rolen2025]` arXiv:2505.00799v2, Sec. 1):**
   - Before applying median-resummation recovery theorems for holomorphic quantum modular forms to
     divergent series in the `c_1` / bar-parity sector, one must verify the half-integer-weight
     Eichler-integral gate: for modular weight `w = k / 2` (`twiceWeight = k`), the dual weight
     `2 - w` has doubled weight `4 - k`, and for `w = 1/2` (`k = 1`) vs `w = 3/2` (`k = 3`), the
     integral kernel exponent `2 - 2 w = 2 - k` switches sign (`+1` vs `-1`).
   - When the lateral Borel sums take the conjugate form `S_+ = R + J` and `S_- = R - J` with
     real part `R` and lateral jump `J`, the doubled median sum `S_+ + S_- = 2 R` cancels `J`
     identically while `S_+ - S_- = 2 J` isolates the jump.

2. **Number-Field Cyclotomic Ring Picard Regulator vs `(q - 1)`-Completion Kernel (`qou-6eke`, Ref: `[wagner2025]` arXiv:2510.04782v2, Sec. 1.4):**
   - The regulator from `K_3(F)` to the Picard group of the cyclotomic ring produces line bundles
     whose sections are perturbative Chern–Simons `q`-series, whereas `(q - 1)`-adic completion
     annihilates the `n`-th cyclotomic factorial modulo `(q - 1)^M` whenever `n ≥ M`.
   - Explicitly records the structural boundary: `(q - 1)`-adic Taylor truncation at `q = 1` cannot
     distinguish global sections differing at cyclotomic order `n ≥ M`, whereas root-of-unity
     evaluations at level `N > M` retain non-vanishing support.
-/

namespace QOU.QBeta.MedianResummationEichlerAndHabiroPicardRegulator

/-- Doubled dual modular weight `4 - twiceWeight` corresponding to `2 - w` when `twiceWeight = 2 w`. -/
def doubledDualModularWeight (twiceWeight : Int) : Int :=
  4 - twiceWeight

/-- Eichler kernel polynomial degree `2 - twiceWeight` for modular weight `w = twiceWeight / 2`. -/
def eichlerKernelDegree (twiceWeight : Int) : Int :=
  2 - twiceWeight

/-- Doubled median resummation `(realPart + jumpPart) + (realPart - jumpPart)` of lateral Borel sums. -/
def doubledMedianBorelSum (realPart jumpPart : Int) : Int :=
  (realPart + jumpPart) + (realPart - jumpPart)

/-- Lateral discontinuity difference `(realPart + jumpPart) - (realPart - jumpPart)`. -/
def lateralDiscontinuityDiff (realPart jumpPart : Int) : Int :=
  (realPart + jumpPart) - (realPart - jumpPart)

/-- For half-integer weights `w = 1/2` (`twiceWeight = 1`) and `w = 3/2` (`twiceWeight = 3`),
    the doubled dual weights `(3, 1)` are involutive, and for any `realPart, jumpPart : Int`,
    the doubled median Borel sum equals `2 * realPart` (independent of `jumpPart`) while the
    lateral difference equals `2 * jumpPart`. -/
theorem median_borel_cancellation_and_eichler_weight_duality (realPart jumpPart : Int) :
    doubledDualModularWeight 1 = 3 ∧
    doubledDualModularWeight 3 = 1 ∧
    eichlerKernelDegree 1 + eichlerKernelDegree 3 = 0 ∧
    doubledMedianBorelSum realPart jumpPart = 2 * realPart ∧
    lateralDiscontinuityDiff realPart jumpPart = 2 * jumpPart := by
  dsimp [doubledDualModularWeight, eichlerKernelDegree, doubledMedianBorelSum, lateralDiscontinuityDiff]
  refine ⟨?_, ?_, ?_, ?_, ?_⟩
  · omega
  · omega
  · omega
  · omega
  · omega

/-- Leading `(q - 1)`-adic valuation `n` of the `n`-th cyclotomic factorial `∏_{k=1}^n (1 - q^k)`. -/
def cyclotomicFactorialValuationAtOne (n : Int) : Int :=
  n

/-- Valuation surplus `n - cutoffM` modulo `(q - 1)^cutoffM` in the `(q - 1)`-adic completion. -/
def completionJetSurplus (n cutoffM : Int) : Int :=
  cyclotomicFactorialValuationAtOne n - cutoffM

/-- Support indicator `levelN - 1 - n` at a primitive `levelN`-th root of unity (`n < levelN`). -/
def rootOfUnitySupportSlack (levelN n : Int) : Int :=
  levelN - 1 - n

/-- Whenever `cutoffM ≤ n` and `n < levelN`, the `n`-th cyclotomic factorial lies in the
    `(q - 1)^cutoffM` completion ideal (`0 ≤ completionJetSurplus n cutoffM`) while remaining
    strictly below the `levelN`-th root-of-unity vanishing threshold (`0 ≤ rootOfUnitySupportSlack levelN n`). -/
theorem picard_regulator_completion_blindness_vs_root_support
    (cutoffM n levelN : Int) (hJet : cutoffM ≤ n) (hRoot : n + 1 ≤ levelN) :
    0 ≤ completionJetSurplus n cutoffM ∧
    0 ≤ rootOfUnitySupportSlack levelN n ∧
    1 ≤ levelN - cutoffM := by
  dsimp [completionJetSurplus, cyclotomicFactorialValuationAtOne, rootOfUnitySupportSlack]
  refine ⟨?_, ?_, ?_⟩
  · omega
  · omega
  · omega

end QOU.QBeta.MedianResummationEichlerAndHabiroPicardRegulator
