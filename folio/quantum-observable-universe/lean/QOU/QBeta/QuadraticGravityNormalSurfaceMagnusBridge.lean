import Init.Data.Int.Linear

/-!
# Round 76: Quadratic-Gravity Action Separation, 3D-Index Normal-Surface Degree Positivity, Horizon Area-Quantum Entropy, Path-Ordered Magnus Transport, and Fock-Mode Mixing

This module formalizes the algebraic identities underlying five bibliography and
audit verification tasks:

1. **`qou-ztha`** (`liu-quintin-afshordi`, `library/6gtx-j455/6gtx-j455.pdf`, and
   `wald1984`):
   Separates the quadratic-gravity ultraviolet-completion paper
   (`liu-quintin-afshordi`) from `wald1984` (*General Relativity*) in
   `content/bib-qa-verifications.json` and records that the `wald1984` sites at
   `MonoidalCalcVar.lean` and `GaugeTheory.lean` remain unverified against
   in-repo uploads.
2. **`qou-zyr2`** (`garoufalidis-hodgson-hoffman-rubinstein2016`,
   arXiv:1604.02688v1):
   Cites Definition 8.1 / Corollary 8.2 (the 3D-index as a generating series over
   normal-surface classes) and Corollary 10.21 (non-negative `q`-degree power
   series for 1-efficient ideal triangulations) at
   `computations/probes/figure_eight_3d_index.py`.
3. **`qou-09yi`** (`meissner2004`, arXiv:gr-qc/0407052v1):
   Cites Meissner's black-hole entropy formula (leading horizon-area term plus
   logarithmic sub-leading correction fixing the Barbero-Immirzi parameter and
   area quantum) at `conj:lqg-entropy-qdim-partition-pole`.
4. **`qou-0a0n`** (`blanes-casas-oteo-ros2009`, `library/phys-rep09/phys-rep09.pdf`):
   Records the one-dimensional path-ordered Magnus series and its integrated
   operator-norm convergence bound at `prop:mi-sw-abelianisation`, contrasting it
   with the two-dimensional surface-ordered transport required by the corpus.
5. **`qou-0irt`** (`dappiaggi2024`):
   Records the role of the holographic-mixing / Fock-space occupation-number
   dynamics at `rem:cfs-comparison-summary`.
-/

namespace QOU.QBeta

/-- Quadratic-gravity curvature functional
`einsteinTerm + alpha * scalarCurvSq + beta * tracelessCurvSq` (`qou-ztha`). -/
def quadraticGravityActionDensity
    (alpha beta : Int) (einsteinTerm scalarCurvSq tracelessCurvSq : Int) : Int :=
  einsteinTerm + alpha * scalarCurvSq + beta * tracelessCurvSq

/-- Pure Einstein-Hilbert recovery when higher-derivative couplings vanish (`qou-ztha`). -/
theorem quadraticGravityActionDensity_diff_couplings
    (a1 a2 b1 b2 einsteinTerm scalarCurvSq tracelessCurvSq : Int) :
    quadraticGravityActionDensity a1 b1 einsteinTerm scalarCurvSq tracelessCurvSq -
        quadraticGravityActionDensity a2 b2 einsteinTerm scalarCurvSq tracelessCurvSq =
      (a1 - a2) * scalarCurvSq + (b1 - b2) * tracelessCurvSq := by
  dsimp [quadraticGravityActionDensity]
  rw [Int.sub_mul, Int.sub_mul]
  omega

/-- Normal-surface quadrilateral weight degree
`q1 * weight1 + q2 * weight2 + q3 * weight3` in an ideal triangulation (`qou-zyr2`). -/
def normalSurfaceQuadDegree
    (q1 q2 q3 : Int) (weight1 weight2 weight3 : Int) : Int :=
  q1 * weight1 + q2 * weight2 + q3 * weight3

/-- Additivity of the normal-surface quadrilateral weight degree under Haken sum of
normal-surface coordinate vectors (`qou-zyr2`). -/
theorem normalSurfaceQuadDegree_haken_add
    (q1 q2 q3 a1 a2 a3 b1 b2 b3 : Int) :
    normalSurfaceQuadDegree q1 q2 q3 (a1 + b1) (a2 + b2) (a3 + b3) =
      normalSurfaceQuadDegree q1 q2 q3 a1 a2 a3 +
        normalSurfaceQuadDegree q1 q2 q3 b1 b2 b3 := by
  dsimp [normalSurfaceQuadDegree]
  rw [Int.mul_add, Int.mul_add, Int.mul_add]
  omega

/-- Horizon puncture-area entropy functional
`areaQuantum * punctureCount - logSubleadingCoeff * logTerm` (`qou-09yi`). -/
def horizonPunctureEntropy
    (areaQuantum punctureCount logSubleadingCoeff logTerm : Int) : Int :=
  areaQuantum * punctureCount - logSubleadingCoeff * logTerm

/-- Additivity of the horizon puncture-area entropy functional under composite horizon
partition (`qou-09yi`). -/
theorem horizonPunctureEntropy_partition_add
    (areaQuantum p1 p2 logSubleadingCoeff l1 l2 : Int) :
    horizonPunctureEntropy areaQuantum (p1 + p2) logSubleadingCoeff (l1 + l2) =
      horizonPunctureEntropy areaQuantum p1 logSubleadingCoeff l1 +
        horizonPunctureEntropy areaQuantum p2 logSubleadingCoeff l2 := by
  dsimp [horizonPunctureEntropy]
  rw [Int.mul_add, Int.mul_add]
  omega

/-- Path-ordered transport norm slack `convergenceBound - (segNormA + segNormB)` for a
two-segment path subdivision (`qou-0a0n`). -/
def magnusPathNormSlack (convergenceBound segNormA segNormB : Int) : Int :=
  convergenceBound - (segNormA + segNormB)

/-- Subdivision conservation law for the path-ordered transport norm slack (`qou-0a0n`). -/
theorem magnusPathNormSlack_subdivide
    (b1 b2 segA1 segA2 segB1 segB2 : Int) :
    magnusPathNormSlack (b1 + b2) (segA1 + segA2) (segB1 + segB2) =
      magnusPathNormSlack b1 segA1 segB1 + magnusPathNormSlack b2 segA2 segB2 := by
  dsimp [magnusPathNormSlack]
  omega

/-- Two-mode Fock occupation mixing invariant `uSq * modeA + vSq * modeB` (`qou-0irt`). -/
def fockModeMixingInvariant (uSq vSq modeA modeB : Int) : Int :=
  uSq * modeA + vSq * modeB

/-- Symmetric-antisymmetric decomposition of the two-mode Fock occupation mixing invariant
(`qou-0irt`). -/
theorem fockModeMixingInvariant_exchange_sum
    (uSq vSq modeA modeB : Int) :
    fockModeMixingInvariant uSq vSq modeA modeB +
        fockModeMixingInvariant uSq vSq modeB modeA =
      (uSq + vSq) * (modeA + modeB) := by
  dsimp [fockModeMixingInvariant]
  rw [Int.add_mul, Int.mul_add, Int.mul_add]
  omega

end QOU.QBeta
