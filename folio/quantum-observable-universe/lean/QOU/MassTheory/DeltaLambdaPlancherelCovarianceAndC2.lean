import Mathlib.Tactic
import QOU.BraidKnot.IdentityIContentDecomposition
import QOU.Mathlib.IdentityIHLFBridge

/-!
# Plancherel Covariance Kernel, Reordered-Word Second-Order Trace Coefficients, and the Deuteron $H_6(q)$ Character Table

This module formalizes three linked algebraic results in the $\Delta_\lambda$ and
reordered-word Markov trace programme:

1. **Transpose-Involution Symmetry and the First-Principles Plancherel Covariance Kernel $\mathrm{cov}(k) \le 0$**:
   Under partition conjugation $\lambda \mapsto \lambda'$, the content of cell $(i,j)$,
   $c(i,j) = j - i$, negates ($c(j,i) = -c(i,j)$), so its square $c(i,j)^2 = (j - i)^2$ is
   invariant. Consequently the centered second content moment
   $$\omega_3(\lambda) = \sum_{\square \in \lambda} c(\square)^2 - \binom{k}{2}$$
   satisfies $\omega_3(\lambda') = \omega_3(\lambda)$ while $f^{\lambda'} = f^\lambda$.
   For every partition $\lambda \in \mathrm{partitionsOf}\;k$, the datum
   `derivedPartitionDatum lam` computes $f^\lambda = \mathrm{dimHLF}\;\lambda$ from the
   Frame–Robinson–Thrall hook-length quotient (`QOU.BraidKnot.IdentityI.dimHLF`, proved equal
   to the genuine standard Young tableau cardinality `dimSYT` in
   `QOU.Mathlib.dimSYT_eq_dimHLF`) and $\sum_{\square \in \lambda} c(\square)^2 =
   \mathrm{sumSqContents}\;\lambda$ directly from the cell coordinates of $\lambda$.
   The seam-closing theorem `partitionsS1_to_S7_eq_derived` proves in Lean that the explicit
   tables `partitionsS1` through `partitionsS7` are identical to
   `derivedPartitionsOf k = (partitionsOf k).map derivedPartitionDatum`.
   Evaluating the exact Plancherel sums across `derivedPartitionsOf k` for
   $k = 1, \dots, 7$ proves the Burnside-Plancherel and centered-content identities
   $$\sum_{\lambda \vdash k} (f^\lambda)^2 = k!, \qquad
     \sum_{\lambda \vdash k} (f^\lambda)^2 \omega_3(\lambda) = 0,$$
   together with vanishing at $k \in \{1, 2\}$ ($\mathrm{cov}(1) = \mathrm{cov}(2) = 0$) and
   strict negativity of the cubic covariance kernel
   $$\mathrm{cov}(k) = \sum_{\lambda \vdash k} (f^\lambda)^3 \omega_3(\lambda) < 0$$
   for $k = 3, 4, 5, 6, 7$ ($\mathrm{cov}(3) = -4$, $\mathrm{cov}(4) = -16$,
   $\mathrm{cov}(5) = -320$, $\mathrm{cov}(6) = -10400$, $\mathrm{cov}(7) = -163520$).

2. **Sufficient Two-Leg Sign Reduction for the Tilted Plancherel Expectation**:
   For $g(\theta) = \mathbb{E}_{2+\theta}[\omega_3]$, the remainder dominance condition
   $|g(1) - g'(0)| < -g'(0)$ implies both $g'(0) < 0$ (`legA2_of_legA3`) and $g(1) < 0$
   (`tilted_expectation_neg_of_two_legs`), and is equivalent under $g'(0) < 0$ and
   $g(1) = r \cdot g'(0)$ to the two-sided transfer-ratio bound $0 < r < 2$
   (`transfer_ratio_in_zero_two_implies_legA3`). When $g(1) < 0$, the unnormalized cubic
   kernel $\mathrm{cov}(k) = \bigl(\sum_\lambda (f^\lambda)^3\bigr) g(1)$ is strictly negative.

3. **Reordered-Word Second-Order Coefficients $c_2$ and the Deuteron $H_6(q)$ Character Sum**:
   Under $\hbar_q = 1 - q^{-1} = \varepsilon - \varepsilon^2 + O(\varepsilon^3)$ where
   $q = 1 + \varepsilon$, a trace difference series
   $\Delta\mathrm{tr}_M(1+\varepsilon) = a_0 + a_1 \varepsilon + a_2 \varepsilon^2 + O(\varepsilon^3)$
   has $\hbar_q$-coefficients $c_0 = a_0$, $c_1 = a_1$, and $c_2 = a_1 + a_2$.
   Decomposing by diagonal-insertion subset size $|S| \in \{0, 1, 2\}$ yields the exact
   dyadic rationals for the six canonical reordered atom words:
   $$c_2(pp) = \frac{33}{32}, \quad c_2(pn) = \frac{25}{32}, \quad c_2(nn) = \frac{1}{16}, \quad
     c_2(\mathrm{T}) = \frac{99}{128}, \quad c_2({}^3\mathrm{He}) = \frac{157}{128}, \quad
     c_2({}^4\mathrm{He}) = \frac{439}{512},$$
   the exact $A = 3$ mirror sum $c_2(\mathrm{T}) + c_2({}^3\mathrm{He}) = 2$, the
   intra-nucleon ordering-invariant $A = 2$ content-cancellation identity
   $c_2(pp) + c_2(nn) - 2 c_2(pn) = -15/32$, the second-order chain-over-atom ratios
   ($12/11$, $232/157$, $960/439$), and the exact two-row Wedderburn character decomposition
   of the deuteron in $H_6(q)$ reproducing $(c_0, c_1, c_2) = (1/8, 1/16, 25/32)$.

**Derivation seam for Sections 2, 4, and 5.**
* In **Section 2**, there is **no Young-diagram table seam**: every entry of `partitionsS1`
  through `partitionsS7` is proved equal in Lean (`partitionsS1_to_S7_eq_derived`) to
  `derivedPartitionsOf k = (partitionsOf k).map derivedPartitionDatum`, where `partitionsOf`,
  `dimHLF`, and `sumSqContents` compute the partition enumeration, hook-length dimension, and
  squared-content sum directly from the cell coordinates of $\lambda$, and
  `derivedPartitionDatum_sytDim_eq_dimSYT` bridges `dimHLF` to the genuine standard Young
  tableau count `QOU.Mathlib.dimSYT`.
* In **Sections 4 and 5**, `canonicalDatumPP` through `canonicalDatumHe4` and
  `deuteronIrrep6` through `deuteronIrrep33` record the exact rational Taylor/cycle
  coefficients $(a_0, a_1, a_2, s_0, s_1, s_2)$ and quadratic $\varepsilon$-series evaluated
  on the canonical reordered braid words and $H_6(q)$ Hoefsmit matrices by the exact rational
  companion probe `computations/deltalambda/delta_lambda_covariance_and_reordered_c2_probe.py`.
  The braid-word diagonal-insertion cycle count and $H_6(q)$ Hoefsmit matrix trace evaluation
  live in that exact rational Python computation rather than in Lean; every theorem in
  Sections 4 and 5 is Lean-proved for those exact rational coefficient tables.
-/

namespace QOU.MassTheory.DeltaLambdaPlancherelCovarianceAndC2

open QOU.BraidKnot.IdentityI (colLen sumSqContents sz prodHooks dimHLF partsFuel partitionsOf)
open QOU.Mathlib (dimSYT dimSYT_eq_dimHLF)

/-! ## Section 1: Box Content, Transpose Involution, and Content-Square Invariance -/

/-- The content $c(i,j) = j - i$ of a Young diagram box at zero-indexed row $i$ and column $j$. -/
def boxContent (row col : ℤ) : ℤ :=
  col - row

/-- The squared content $c(i,j)^2 = (j - i)^2$ of a Young diagram box at row $i$ and column $j$. -/
def boxContentSq (row col : ℤ) : ℤ :=
  (boxContent row col) ^ 2

/-- Conjugating a Young diagram transposes row and column indices and negates the box content:
$c(j,i) = -c(i,j)$. -/
theorem boxContent_transpose (row col : ℤ) :
    boxContent col row = -boxContent row col := by
  unfold boxContent
  ring

/-- The squared box content is invariant under Young diagram transposition:
$c(j,i)^2 = c(i,j)^2$. -/
theorem boxContentSq_transpose (row col : ℤ) :
    boxContentSq col row = boxContentSq row col := by
  unfold boxContentSq boxContent
  ring

/-- Non-vacuity witness: off-diagonal boxes have strictly positive squared content and non-zero
opposite contents under transposition. -/
theorem boxContent_transpose_nonvacuous :
    boxContent 0 2 = 2 ∧ boxContent 2 0 = -2 ∧ boxContentSq 0 2 = 4 ∧ boxContentSq 2 0 = 4 := by
  decide

/-- Combinatorial Plancherel datum for an irreducible representation $\lambda \vdash k$ of $S_k$,
recording its standard Young tableau dimension $f^\lambda$ and total squared box content
$\sum_{\square \in \lambda} c(\square)^2$. -/
structure PartitionPlancherelDatum where
  /-- Standard Young tableau dimension $f^\lambda = \dim V^\lambda$. -/
  sytDim : ℚ
  /-- Sum of squared box contents $\sum_{\square \in \lambda} c(\square)^2$. -/
  contentSqSum : ℚ
  deriving DecidableEq, Repr

/-- First-principles Plancherel datum computed directly from the Young diagram `lam : List ℕ`
via the Frame–Robinson–Thrall hook-length dimension `dimHLF lam` and the cell-by-cell
squared-content sum `sumSqContents lam = ∑_{i} ∑_{j < λ_i} (j - i)^2`. -/
def derivedPartitionDatum (lam : List ℕ) : PartitionPlancherelDatum :=
  ⟨(dimHLF lam : ℚ), (sumSqContents lam : ℚ)⟩

/-- For every partition `p : Nat.Partition n`, the `sytDim` field of `derivedPartitionDatum`
on the sorted part list `p.parts.sort (· ≥ ·)` equals the genuine standard Young tableau
cardinality `dimSYT p` (via `QOU.Mathlib.dimSYT_eq_dimHLF`). -/
theorem derivedPartitionDatum_sytDim_eq_dimSYT {n : ℕ} (p : Nat.Partition n) :
    (derivedPartitionDatum (p.parts.sort (· ≥ ·))).sytDim = (dimSYT p : ℚ) := by
  simp only [derivedPartitionDatum]
  exact_mod_cast (dimSYT_eq_dimHLF p).symm

/-- Complete list of first-principles Plancherel data for all integer partitions of `k`,
obtained by mapping `derivedPartitionDatum` over the computable partition enumerator
`partitionsOf k`. -/
def derivedPartitionsOf (k : ℕ) : List PartitionPlancherelDatum :=
  (partitionsOf k).map derivedPartitionDatum

/-- The centered second content moment $\omega_3(\lambda) = \sum_{\square \in \lambda} c(\square)^2 - \binom{k}{2}$
for a partition $\lambda \vdash k$. -/
def omega3 (k : ℚ) (d : PartitionPlancherelDatum) : ℚ :=
  d.contentSqSum - k * (k - 1) / 2

/-- The unnormalized Plancherel dimension-square weight $(f^\lambda)^2$ of a partition datum. -/
def plancherelDimSq (d : PartitionPlancherelDatum) : ℚ :=
  d.sytDim ^ 2

/-- The unnormalized Plancherel centered-content contribution $(f^\lambda)^2 \omega_3(\lambda)$. -/
def plancherelMeanTerm (k : ℚ) (d : PartitionPlancherelDatum) : ℚ :=
  d.sytDim ^ 2 * omega3 k d

/-- The cubic Plancherel covariance kernel contribution $(f^\lambda)^3 \omega_3(\lambda)$. -/
def plancherelCovTerm (k : ℚ) (d : PartitionPlancherelDatum) : ℚ :=
  d.sytDim ^ 3 * omega3 k d

/-- Conjugate partitions $\lambda, \lambda' \vdash k$ have equal SYT dimension and equal sum of
squared box contents, hence identical centered content moment $\omega_3(\lambda') = \omega_3(\lambda)$. -/
theorem omega3_eq_of_conjugate (k : ℚ) (d dConj : PartitionPlancherelDatum)
    (hContent : dConj.contentSqSum = d.contentSqSum) :
    omega3 k dConj = omega3 k d := by
  unfold omega3
  rw [hContent]

/-- Conjugate partitions $\lambda, \lambda' \vdash k$ contribute equal cubic terms
$(f^{\lambda'})^3 \omega_3(\lambda') = (f^\lambda)^3 \omega_3(\lambda)$ to the Plancherel covariance
kernel. -/
theorem plancherelCovTerm_eq_of_conjugate (k : ℚ) (d dConj : PartitionPlancherelDatum)
    (hDim : dConj.sytDim = d.sytDim) (hContent : dConj.contentSqSum = d.contentSqSum) :
    plancherelCovTerm k dConj = plancherelCovTerm k d := by
  unfold plancherelCovTerm omega3
  rw [hDim, hContent]

/-- Pairing a non-self-conjugate partition $\lambda$ with its transpose $\lambda'$ doubles its
cubic Plancherel covariance contribution. -/
theorem plancherelCovTerm_pair_sum (k : ℚ) (d dConj : PartitionPlancherelDatum)
    (hDim : dConj.sytDim = d.sytDim) (hContent : dConj.contentSqSum = d.contentSqSum) :
    plancherelCovTerm k d + plancherelCovTerm k dConj = 2 * plancherelCovTerm k d := by
  rw [plancherelCovTerm_eq_of_conjugate k d dConj hDim hContent]
  ring

/-! ## Section 2: First-Principles Plancherel Covariance Kernel $\mathrm{cov}(k) \le 0$ for $S_1 \dots S_7$ -/

/-- Total Plancherel dimension-square sum $\sum_{\lambda \vdash k} (f^\lambda)^2$ across a partition table. -/
def plancherelDimSqSum (parts : List PartitionPlancherelDatum) : ℚ :=
  (parts.map plancherelDimSq).sum

/-- Total unnormalized Plancherel expectation $\sum_{\lambda \vdash k} (f^\lambda)^2 \omega_3(\lambda)$
of the centered second content moment. -/
def plancherelOmega3MeanSum (k : ℚ) (parts : List PartitionPlancherelDatum) : ℚ :=
  (parts.map (plancherelMeanTerm k)).sum

/-- Total cubic Plancherel covariance kernel
$\mathrm{cov}(k) = \sum_{\lambda \vdash k} (f^\lambda)^3 \omega_3(\lambda)$. -/
def plancherelCovarianceKernel (k : ℚ) (parts : List PartitionPlancherelDatum) : ℚ :=
  (parts.map (plancherelCovTerm k)).sum

/-- Total cubic SYT dimension sum $\sum_{\lambda \vdash k} (f^\lambda)^3$, the denominator of the
$\beta = 3$ tilted expectation $g(1)$. -/
def plancherelDimCubeSum (parts : List PartitionPlancherelDatum) : ℚ :=
  (parts.map (fun d => d.sytDim ^ 3)).sum

/-- Partition table of $S_1$: $\lambda = (1)$ with $f^{(1)} = 1$ and $\sum c^2 = 0$. -/
def partitionsS1 : List PartitionPlancherelDatum :=
  [⟨1, 0⟩]

/-- Partition table of $S_2$: $\lambda \in \{(2), (1,1)\}$ with $f^\lambda = 1$ and $\sum c^2 = 1$. -/
def partitionsS2 : List PartitionPlancherelDatum :=
  [⟨1, 1⟩, ⟨1, 1⟩]

/-- Partition table of $S_3$: $\lambda \in \{(3), (2,1), (1,1,1)\}$ with
$(f^\lambda, \sum c^2) \in \{(1, 5), (2, 2), (1, 5)\}$. -/
def partitionsS3 : List PartitionPlancherelDatum :=
  [⟨1, 5⟩, ⟨2, 2⟩, ⟨1, 5⟩]

/-- Partition table of $S_4$: $\lambda \in \{(4), (3,1), (2,2), (2,1,1), (1^4)\}$ with
$(f^\lambda, \sum c^2) \in \{(1, 14), (3, 6), (2, 2), (3, 6), (1, 14)\}$. -/
def partitionsS4 : List PartitionPlancherelDatum :=
  [⟨1, 14⟩, ⟨3, 6⟩, ⟨2, 2⟩, ⟨3, 6⟩, ⟨1, 14⟩]

/-- Partition table of $S_5$: all 7 partitions of $5$ ordered from $(5)$ to $(1^5)$. -/
def partitionsS5 : List PartitionPlancherelDatum :=
  [⟨1, 30⟩, ⟨4, 15⟩, ⟨5, 6⟩, ⟨6, 10⟩, ⟨5, 6⟩, ⟨4, 15⟩, ⟨1, 30⟩]

/-- Partition table of $S_6$: all 11 partitions of $6$ ordered from $(6)$ to $(1^6)$. -/
def partitionsS6 : List PartitionPlancherelDatum :=
  [⟨1, 55⟩, ⟨5, 31⟩, ⟨9, 15⟩, ⟨10, 19⟩, ⟨5, 7⟩, ⟨16, 10⟩,
   ⟨10, 19⟩, ⟨5, 7⟩, ⟨9, 15⟩, ⟨5, 31⟩, ⟨1, 55⟩]

/-- Partition table of $S_7$: all 15 partitions of $7$ ordered from $(7)$ to $(1^7)$. -/
def partitionsS7 : List PartitionPlancherelDatum :=
  [⟨1, 91⟩, ⟨6, 56⟩, ⟨14, 31⟩, ⟨15, 35⟩, ⟨14, 16⟩, ⟨35, 19⟩, ⟨20, 28⟩,
   ⟨21, 11⟩, ⟨21, 11⟩, ⟨35, 19⟩, ⟨15, 35⟩, ⟨14, 16⟩, ⟨14, 31⟩, ⟨6, 56⟩, ⟨1, 91⟩]

/-- **Seam-Closing Theorem for the $S_1 \dots S_7$ Plancherel Tables:**
Every explicit table `partitionsS1` through `partitionsS7` equals the first-principles table
`derivedPartitionsOf k = (partitionsOf k).map derivedPartitionDatum` computed directly from
Young-diagram hook lengths (`dimHLF`) and cell contents (`sumSqContents`). -/
theorem partitionsS1_to_S7_eq_derived :
    partitionsS1 = derivedPartitionsOf 1 ∧
    partitionsS2 = derivedPartitionsOf 2 ∧
    partitionsS3 = derivedPartitionsOf 3 ∧
    partitionsS4 = derivedPartitionsOf 4 ∧
    partitionsS5 = derivedPartitionsOf 5 ∧
    partitionsS6 = derivedPartitionsOf 6 ∧
    partitionsS7 = derivedPartitionsOf 7 := by
  decide

/-- Burnside-Plancherel dimension-square sum $\sum_{\lambda \vdash k} (f^\lambda)^2 = k!$ for
$k = 1, \dots, 7$. -/
theorem plancherelDimSqSum_S1_to_S7 :
    plancherelDimSqSum partitionsS1 = 1 ∧
    plancherelDimSqSum partitionsS2 = 2 ∧
    plancherelDimSqSum partitionsS3 = 6 ∧
    plancherelDimSqSum partitionsS4 = 24 ∧
    plancherelDimSqSum partitionsS5 = 120 ∧
    plancherelDimSqSum partitionsS6 = 720 ∧
    plancherelDimSqSum partitionsS7 = 5040 := by
  norm_num [plancherelDimSqSum, plancherelDimSq, partitionsS1, partitionsS2, partitionsS3,
    partitionsS4, partitionsS5, partitionsS6, partitionsS7]

/-- The Plancherel expectation of the centered second content moment vanishes identically,
$\sum_{\lambda \vdash k} (f^\lambda)^2 \omega_3(\lambda) = 0$, for every $k = 1, \dots, 7$. -/
theorem plancherelOmega3MeanSum_zero_S1_to_S7 :
    plancherelOmega3MeanSum 1 partitionsS1 = 0 ∧
    plancherelOmega3MeanSum 2 partitionsS2 = 0 ∧
    plancherelOmega3MeanSum 3 partitionsS3 = 0 ∧
    plancherelOmega3MeanSum 4 partitionsS4 = 0 ∧
    plancherelOmega3MeanSum 5 partitionsS5 = 0 ∧
    plancherelOmega3MeanSum 6 partitionsS6 = 0 ∧
    plancherelOmega3MeanSum 7 partitionsS7 = 0 := by
  norm_num [plancherelOmega3MeanSum, plancherelMeanTerm, omega3, partitionsS1, partitionsS2,
    partitionsS3, partitionsS4, partitionsS5, partitionsS6, partitionsS7]

/-- Exact integer values of the cubic Plancherel covariance kernel
$\mathrm{cov}(k) = \sum_{\lambda \vdash k} (f^\lambda)^3 \omega_3(\lambda)$ for $k = 1, \dots, 7$. -/
theorem plancherelCovarianceKernel_exact_S1_to_S7 :
    plancherelCovarianceKernel 1 partitionsS1 = 0 ∧
    plancherelCovarianceKernel 2 partitionsS2 = 0 ∧
    plancherelCovarianceKernel 3 partitionsS3 = -4 ∧
    plancherelCovarianceKernel 4 partitionsS4 = -16 ∧
    plancherelCovarianceKernel 5 partitionsS5 = -320 ∧
    plancherelCovarianceKernel 6 partitionsS6 = -10400 ∧
    plancherelCovarianceKernel 7 partitionsS7 = -163520 := by
  norm_num [plancherelCovarianceKernel, plancherelCovTerm, omega3, partitionsS1, partitionsS2,
    partitionsS3, partitionsS4, partitionsS5, partitionsS6, partitionsS7]

/-- Exact integer values of the cubic Plancherel covariance kernel evaluated directly on the
first-principles Young-diagram enumerator `derivedPartitionsOf k` for $k = 1, \dots, 7$,
without passing through any hand-entered table. -/
theorem plancherelCovarianceKernel_derived_exact_S1_to_S7 :
    plancherelCovarianceKernel 1 (derivedPartitionsOf 1) = 0 ∧
    plancherelCovarianceKernel 2 (derivedPartitionsOf 2) = 0 ∧
    plancherelCovarianceKernel 3 (derivedPartitionsOf 3) = -4 ∧
    plancherelCovarianceKernel 4 (derivedPartitionsOf 4) = -16 ∧
    plancherelCovarianceKernel 5 (derivedPartitionsOf 5) = -320 ∧
    plancherelCovarianceKernel 6 (derivedPartitionsOf 6) = -10400 ∧
    plancherelCovarianceKernel 7 (derivedPartitionsOf 7) = -163520 := by
  rcases partitionsS1_to_S7_eq_derived with ⟨h1, h2, h3, h4, h5, h6, h7⟩
  rw [← h1, ← h2, ← h3, ← h4, ← h5, ← h6, ← h7]
  exact plancherelCovarianceKernel_exact_S1_to_S7

/-- The cubic Plancherel covariance kernel is strictly negative for $k = 3, \dots, 7$ and
non-positive for all $k = 1, \dots, 7$. -/
theorem plancherelCovarianceKernel_nonpos_and_strict_neg :
    plancherelCovarianceKernel 1 partitionsS1 ≤ 0 ∧
    plancherelCovarianceKernel 2 partitionsS2 ≤ 0 ∧
    plancherelCovarianceKernel 3 partitionsS3 < 0 ∧
    plancherelCovarianceKernel 4 partitionsS4 < 0 ∧
    plancherelCovarianceKernel 5 partitionsS5 < 0 ∧
    plancherelCovarianceKernel 6 partitionsS6 < 0 ∧
    plancherelCovarianceKernel 7 partitionsS7 < 0 := by
  norm_num [plancherelCovarianceKernel, plancherelCovTerm, omega3, partitionsS1, partitionsS2,
    partitionsS3, partitionsS4, partitionsS5, partitionsS6, partitionsS7]

/-! ## Section 3: Sufficient Two-Leg Sign Reduction for the Tilted Plancherel Expectation -/

/-- The transfer-remainder dominance bound $|g(1) - g'(0)| < -g'(0)$ implies that the leading
Plancherel covariance derivative is strictly negative ($g'(0) < 0$), since $0 \le |g(1) - g'(0)|$. -/
theorem legA2_of_legA3 (g1 gp0 : ℚ) (hLegA3 : |g1 - gp0| < -gp0) :
    gp0 < 0 := by
  have hNonneg : 0 ≤ |g1 - gp0| := abs_nonneg (g1 - gp0)
  linarith

/-- Sufficient sign lemma from transfer-remainder dominance: if the Taylor transfer remainder
$R = g(1) - g'(0)$ is strictly dominated in magnitude by $-g'(0)$, i.e. $|g(1) - g'(0)| < -g'(0)$,
then the tilted expectation at $\theta = 1$ satisfies $g(1) < 0$. -/
theorem tilted_expectation_neg_of_two_legs (g1 gp0 : ℚ)
    (hLegA3 : |g1 - gp0| < -gp0) :
    g1 < 0 := by
  have hUpper : g1 - gp0 < -gp0 := (abs_lt.mp hLegA3).2
  linarith

/-- If $|g(1) - g'(0)| < -g'(0)$ holds and $g(1) = \mathrm{cov} / D$ with cubic dimension sum
$D = \sum_{\lambda \vdash k} (f^\lambda)^3 > 0$, then the cubic Plancherel covariance kernel
$\mathrm{cov}$ is strictly negative. -/
theorem covariance_kernel_neg_of_two_legs (cov denom g1 gp0 : ℚ)
    (hDenom : 0 < denom) (hDef : g1 = cov / denom)
    (hLegA3 : |g1 - gp0| < -gp0) :
    cov < 0 := by
  have hg1 : g1 < 0 := tilted_expectation_neg_of_two_legs g1 gp0 hLegA3
  rw [hDef] at hg1
  have hMul : (cov / denom) * denom < 0 * denom := mul_lt_mul_of_pos_right hg1 hDenom
  have hNe : denom ≠ 0 := ne_of_gt hDenom
  have hEq : (cov / denom) * denom = cov := div_mul_cancel₀ cov hNe
  linarith

/-- Two-sided transfer-ratio bound implies transfer-remainder dominance: when $g'(0) < 0$,
$g(1) = r \cdot g'(0)$, and the transfer ratio lies in the open interval $0 < r < 2$,
both bounds $0 < r$ and $r < 2$ combine to give $|g(1) - g'(0)| < -g'(0)$. -/
theorem transfer_ratio_in_zero_two_implies_legA3 (g1 gp0 r : ℚ)
    (hLegA2 : gp0 < 0) (hRatio : g1 = r * gp0) (hr0 : 0 < r) (hr2 : r < 2) :
    |g1 - gp0| < -gp0 := by
  rw [hRatio, abs_lt]
  constructor
  · nlinarith
  · nlinarith

/-- Equivalent transfer-ratio form of the two-leg sign reduction: when $g'(0) < 0$ and the
transfer ratio $r = g(1) / g'(0)$ lies in the open interval $(0, 2)$, the transfer-remainder
dominance condition $|g(1) - g'(0)| < -g'(0)$ holds and the tilted expectation $g(1)$ is
strictly negative. -/
theorem tilted_expectation_neg_of_transfer_ratio_in_zero_two (g1 gp0 r : ℚ)
    (hLegA2 : gp0 < 0) (hRatio : g1 = r * gp0) (hr0 : 0 < r) (hr2 : r < 2) :
    g1 < 0 :=
  tilted_expectation_neg_of_two_legs g1 gp0
    (transfer_ratio_in_zero_two_implies_legA3 g1 gp0 r hLegA2 hRatio hr0 hr2)

/-- Non-vacuity witness at $k = 4$: $\mathrm{cov}(4) = -16$ and $\sum_{\lambda \vdash 4} (f^\lambda)^3 = 64$,
so $g(1) = -1 / 4 < 0$. -/
theorem tilted_expectation_S4_exact :
    plancherelCovarianceKernel 4 partitionsS4 / plancherelDimCubeSum partitionsS4 = -1 / 4 := by
  norm_num [plancherelCovarianceKernel, plancherelCovTerm, omega3, plancherelDimCubeSum, partitionsS4]

/-! ## Section 4: Reordered-Word Second-Order Coefficients $c_2$ and Diagonal-Insertion Split

**Derivation seam (`canonicalDatum*` tables).** The structures `canonicalDatumPP` through
`canonicalDatumHe4` below record the exact rational $\varepsilon$-Taylor coefficients
$(a_0, a_1, a_2)$ and diagonal-insertion subset-size contributions $(s_0, s_1, s_2)$ computed
from the canonical (`intra_order = borromean`) and pre-reordering (`intra_order = grouped`)
braid words by the exact rational companion probe
`computations/deltalambda/delta_lambda_covariance_and_reordered_c2_probe.py`.
Every theorem in Section 4 is Lean-proved for those exact rational coefficient tables. -/

/-- Second-order $\hbar_q$-expansion coefficient $c_2 = a_1 + a_2$ from the $\varepsilon = q - 1$
Taylor coefficients $\Delta\mathrm{tr}_M(1+\varepsilon) = a_0 + a_1 \varepsilon + a_2 \varepsilon^2 + O(\varepsilon^3)$,
using $\varepsilon = \hbar_q / (1 - \hbar_q) = \hbar_q + \hbar_q^2 + O(\hbar_q^3)$. -/
def c2FromEpsTaylor (a1 a2 : ℚ) : ℚ :=
  a1 + a2

/-- Total second-order coefficient $c_2 = c_2^{(|S|=0)} + c_2^{(|S|=1)} + c_2^{(|S|=2)}$ assembled
from the three diagonal-insertion subset-size classes $|S| \in \{0, 1, 2\}$. -/
def c2FromInsertionClasses (s0 s1 s2 : ℚ) : ℚ :=
  s0 + s1 + s2

/-- Algebraic verification of the $\varepsilon \to \hbar_q$ quadratic coordinate change:
substituting $\varepsilon(\hbar_q) = \hbar_q + \hbar_q^2$ into $a_0 + a_1 \varepsilon + a_2 \varepsilon^2$
and truncating modulo $\hbar_q^3$ yields coefficient $a_0$ at $\hbar_q^0$, $a_1$ at $\hbar_q^1$,
and $c_2 = a_1 + a_2$ at $\hbar_q^2$. -/
theorem eps_to_hbar_quadratic_truncation (a0 a1 a2 h : ℚ) :
    a0 + a1 * (h + h ^ 2) + a2 * (h + h ^ 2) ^ 2 =
      a0 + a1 * h + c2FromEpsTaylor a1 a2 * h ^ 2 + a2 * (2 * h ^ 3 + h ^ 4) := by
  unfold c2FromEpsTaylor
  ring

/-- Complete order-2 diagonal-insertion expansion datum for an atom braid word, storing the
$\varepsilon$-Taylor coefficients $(a_0, a_1, a_2)$ and the $|S| = 0, 1, 2$ class contributions
to $c_2$. -/
structure InsertionExpansionDatum where
  /-- Zeroth-order coefficient $a_0 = c_0 = [\varepsilon^0]\Delta\mathrm{tr}_M$. -/
  a0 : ℚ
  /-- First-order coefficient $a_1 = c_1 = [\varepsilon^1]\Delta\mathrm{tr}_M$. -/
  a1 : ℚ
  /-- Second-order $\varepsilon$-Taylor coefficient $a_2 = [\varepsilon^2]\Delta\mathrm{tr}_M$. -/
  a2 : ℚ
  /-- Pure-permutation ($|S| = 0$) normaliser contribution to $c_2$. -/
  s0 : ℚ
  /-- Single-deletion ($|S| = 1$) contribution to $c_2$. -/
  s1 : ℚ
  /-- Double-deletion ($|S| = 2$) contribution to $c_2$. -/
  s2 : ℚ
  deriving DecidableEq, Repr

/-- First-order $\hbar_q$ trace coefficient $c_1$ of an insertion expansion datum. -/
def InsertionExpansionDatum.c1 (d : InsertionExpansionDatum) : ℚ :=
  d.a1

/-- Second-order $\hbar_q$ trace coefficient $c_2 = a_1 + a_2$ of an insertion expansion datum. -/
def InsertionExpansionDatum.c2 (d : InsertionExpansionDatum) : ℚ :=
  c2FromEpsTaylor d.a1 d.a2

/-- Sum of the $|S| = 0, 1, 2$ insertion classes of an insertion expansion datum. -/
def InsertionExpansionDatum.classSum (d : InsertionExpansionDatum) : ℚ :=
  c2FromInsertionClasses d.s0 d.s1 d.s2

/-- Canonical reordered-word (`intra_order = borromean`) insertion expansion datum for `pp` ($Z=2, N=0$). -/
def canonicalDatumPP : InsertionExpansionDatum :=
  ⟨1 / 8, 1 / 8, 29 / 32, 0, 7 / 8, 5 / 32⟩

/-- Canonical reordered-word (`intra_order = borromean`) insertion expansion datum for `pn` / $^2\mathrm{H}$ ($Z=1, N=1$). -/
def canonicalDatumPN : InsertionExpansionDatum :=
  ⟨1 / 8, 1 / 16, 23 / 32, 0, 27 / 32, -1 / 16⟩

/-- Canonical reordered-word (`intra_order = borromean`) insertion expansion datum for `nn` ($Z=0, N=2$). -/
def canonicalDatumNN : InsertionExpansionDatum :=
  ⟨1 / 8, 0, 1 / 16, 0, 13 / 16, -3 / 4⟩

/-- Canonical reordered-word (`intra_order = borromean`) insertion expansion datum for `T` / $^3\mathrm{H}$ ($Z=1, N=2$). -/
def canonicalDatumT : InsertionExpansionDatum :=
  ⟨3 / 32, 1 / 64, 97 / 128, 5 / 32, 123 / 128, -11 / 32⟩

/-- Canonical reordered-word (`intra_order = borromean`) insertion expansion datum for $^3\mathrm{He}$ ($Z=2, N=1$). -/
def canonicalDatumHe3 : InsertionExpansionDatum :=
  ⟨3 / 32, 1 / 8, 141 / 128, 5 / 32, 65 / 64, 7 / 128⟩

/-- Canonical reordered-word (`intra_order = borromean`) insertion expansion datum for $^4\mathrm{He}$ ($Z=2, N=2$). -/
def canonicalDatumHe4 : InsertionExpansionDatum :=
  ⟨7 / 128, 7 / 128, 411 / 512, 11 / 64, 25 / 32, -49 / 512⟩

/-- For all six canonical reordered atom words (`pp`, `pn`, `nn`, `T`, `³He`, `⁴He`), the
$\varepsilon$-Taylor sum $c_2 = a_1 + a_2$ agrees identically with the $|S| \in \{0, 1, 2\}$
diagonal-insertion class sum and takes the exact dyadic rational values
$33/32, 25/32, 1/16, 99/128, 157/128, 439/512$. -/
theorem canonical_reordered_c2_exact_and_class_split :
    canonicalDatumPP.c2 = 33 / 32 ∧ canonicalDatumPP.classSum = canonicalDatumPP.c2 ∧
    canonicalDatumPN.c2 = 25 / 32 ∧ canonicalDatumPN.classSum = canonicalDatumPN.c2 ∧
    canonicalDatumNN.c2 = 1 / 16 ∧ canonicalDatumNN.classSum = canonicalDatumNN.c2 ∧
    canonicalDatumT.c2 = 99 / 128 ∧ canonicalDatumT.classSum = canonicalDatumT.c2 ∧
    canonicalDatumHe3.c2 = 157 / 128 ∧ canonicalDatumHe3.classSum = canonicalDatumHe3.c2 ∧
    canonicalDatumHe4.c2 = 439 / 512 ∧ canonicalDatumHe4.classSum = canonicalDatumHe4.c2 := by
  norm_num [InsertionExpansionDatum.c2, InsertionExpansionDatum.classSum,
    c2FromEpsTaylor, c2FromInsertionClasses,
    canonicalDatumPP, canonicalDatumPN, canonicalDatumNN,
    canonicalDatumT, canonicalDatumHe3, canonicalDatumHe4]

/-- The $|S| = 0$ pure-permutation class contribution to $c_2$ is species-blind: it vanishes
for all three $A = 2$ words (`pp`, `pn`, `nn`) and equals $5/32$ for both $A = 3$ mirror nuclei
(`T` and `³He`). -/
theorem canonical_s0_species_blind :
    canonicalDatumPP.s0 = 0 ∧
    canonicalDatumPN.s0 = 0 ∧
    canonicalDatumNN.s0 = 0 ∧
    canonicalDatumT.s0 = 5 / 32 ∧
    canonicalDatumHe3.s0 = 5 / 32 ∧
    canonicalDatumHe4.s0 = 11 / 64 := by
  norm_num [canonicalDatumPP, canonicalDatumPN, canonicalDatumNN,
    canonicalDatumT, canonicalDatumHe3, canonicalDatumHe4]

/-- Exact $A = 3$ mirror sum identity: on the canonical reordered atom words, the triton and
helion second-order coefficients sum to the exact integer $2$:
$$c_2(\mathrm{T}) + c_2({}^3\mathrm{He}) = \frac{99}{128} + \frac{157}{128} = 2.$$ -/
theorem canonical_c2_mirror_sum_A3 :
    canonicalDatumT.c2 + canonicalDatumHe3.c2 = 2 := by
  norm_num [InsertionExpansionDatum.c2, c2FromEpsTaylor, canonicalDatumT, canonicalDatumHe3]

/-- The $A = 2$ content-cancelling linear combination $c_2(pp) + c_2(nn) - 2 c_2(pn)$. -/
def contentCancellationCombinationA2 (c2PP c2PN c2NN : ℚ) : ℚ :=
  c2PP + c2NN - 2 * c2PN

/-- Content-cancellation invariance at $A = 2$: the second-order combination
$c_2(pp) + c_2(nn) - 2 c_2(pn) = -15/32$ is identically preserved between the canonical
(`borromean`: $33/32, 25/32, 1/16$) and pre-reordering (`grouped`: $357/32, 403/32, 217/16$)
intra-nucleon words. -/
theorem contentCancellationCombinationA2_invariance :
    contentCancellationCombinationA2 canonicalDatumPP.c2 canonicalDatumPN.c2 canonicalDatumNN.c2 = -15 / 32 ∧
    contentCancellationCombinationA2 (357 / 32) (403 / 32) (217 / 16) = -15 / 32 ∧
    contentCancellationCombinationA2 canonicalDatumPP.c2 canonicalDatumPN.c2 canonicalDatumNN.c2 =
      contentCancellationCombinationA2 (357 / 32) (403 / 32) (217 / 16) := by
  norm_num [contentCancellationCombinationA2, InsertionExpansionDatum.c2, c2FromEpsTaylor,
    canonicalDatumPP, canonicalDatumPN, canonicalDatumNN]

/-- Pairwise linear-chain over bound-atom ratio for $A = 3$ and $A = 4$ nuclei. -/
def pairwiseChainOverAtom (chainSum atomVal : ℚ) : ℚ :=
  chainSum / atomVal

/-- Exact first-order ($c_1$) and second-order ($c_2$) pairwise-chain over bound-atom ratios for
$\mathrm{T}$, ${}^3\mathrm{He}$, and ${}^4\mathrm{He}$ on the canonical reordered word, and
verification that $|r_2 - 1| < |r_1 - 1|$ in every case. -/
theorem canonical_chain_over_atom_ratios_order1_and_order2 :
    let r1T := pairwiseChainOverAtom (canonicalDatumPN.c1 + canonicalDatumNN.c1) canonicalDatumT.c1
    let r1He3 := pairwiseChainOverAtom (canonicalDatumPP.c1 + canonicalDatumPN.c1) canonicalDatumHe3.c1
    let r1He4 := pairwiseChainOverAtom
      (canonicalDatumPP.c1 + canonicalDatumPN.c1 + canonicalDatumNN.c1) canonicalDatumHe4.c1
    let r2T := pairwiseChainOverAtom (canonicalDatumPN.c2 + canonicalDatumNN.c2) canonicalDatumT.c2
    let r2He3 := pairwiseChainOverAtom (canonicalDatumPP.c2 + canonicalDatumPN.c2) canonicalDatumHe3.c2
    let r2He4 := pairwiseChainOverAtom
      (canonicalDatumPP.c2 + canonicalDatumPN.c2 + canonicalDatumNN.c2) canonicalDatumHe4.c2
    r1T = 4 ∧ r1He3 = 3 / 2 ∧ r1He4 = 24 / 7 ∧
    r2T = 12 / 11 ∧ r2He3 = 232 / 157 ∧ r2He4 = 960 / 439 ∧
    |r2T - 1| < |r1T - 1| ∧ |r2He3 - 1| < |r1He3 - 1| ∧ |r2He4 - 1| < |r1He4 - 1| := by
  norm_num [pairwiseChainOverAtom, InsertionExpansionDatum.c1, InsertionExpansionDatum.c2,
    c2FromEpsTaylor, canonicalDatumPP, canonicalDatumPN, canonicalDatumNN,
    canonicalDatumT, canonicalDatumHe3, canonicalDatumHe4]

/-! ## Section 5: Deuteron ($^2\mathrm{H}$) at $H_6(q)$ Two-Row Wedderburn Character Decomposition

**Derivation seam (`deuteronIrrep*` tables).** The structures `deuteronIrrep6`,
`deuteronIrrep51`, `deuteronIrrep42`, and `deuteronIrrep33` below record the exact rational
quadratic $\varepsilon$-series of the $H_6(1+\varepsilon)$ Hoefsmit irreducible characters
$\chi^\lambda(W_{\mathrm{free}})$, $\chi^\lambda(W_{\mathrm{atom}})$, and Convention-D
Wedderburn weights $y_\lambda(1+\varepsilon)$ computed by the companion probe
`computations/deltalambda/delta_lambda_covariance_and_reordered_c2_probe.py`.
Every theorem in Section 5 is Lean-proved for those exact rational series tables. -/

/-- Truncated quadratic $\varepsilon$-series datum $c_0 + c_1 \varepsilon + c_2 \varepsilon^2 + O(\varepsilon^3)$
for an $H_6(q)$ Wedderburn character or weight at $q = 1 + \varepsilon$. -/
structure QuadEpsSeries where
  /-- Coefficient of $\varepsilon^0$. -/
  e0 : ℚ
  /-- Coefficient of $\varepsilon^1$. -/
  e1 : ℚ
  /-- Coefficient of $\varepsilon^2$. -/
  e2 : ℚ
  deriving DecidableEq, Repr

/-- Termwise difference $\chi^\lambda(W_{\mathrm{free}}) - \chi^\lambda(W_{\mathrm{atom}})$ of two
quadratic $\varepsilon$-series. -/
def QuadEpsSeries.sub (a b : QuadEpsSeries) : QuadEpsSeries :=
  ⟨a.e0 - b.e0, a.e1 - b.e1, a.e2 - b.e2⟩

/-- Termwise sum of two quadratic $\varepsilon$-series. -/
def QuadEpsSeries.add (a b : QuadEpsSeries) : QuadEpsSeries :=
  ⟨a.e0 + b.e0, a.e1 + b.e1, a.e2 + b.e2⟩

/-- Cauchy product of two quadratic $\varepsilon$-series truncated modulo $\varepsilon^3$:
$$(y_0 + y_1 \varepsilon + y_2 \varepsilon^2)(d_0 + d_1 \varepsilon + d_2 \varepsilon^2)
  = y_0 d_0 + (y_0 d_1 + y_1 d_0)\varepsilon + (y_0 d_2 + y_1 d_1 + y_2 d_0)\varepsilon^2 + O(\varepsilon^3).$$ -/
def QuadEpsSeries.mulModEps3 (y d : QuadEpsSeries) : QuadEpsSeries :=
  ⟨y.e0 * d.e0, y.e0 * d.e1 + y.e1 * d.e0, y.e0 * d.e2 + y.e1 * d.e1 + y.e2 * d.e0⟩

/-- Per-partition $H_6(q)$ Wedderburn character datum for the deuteron ($^2\mathrm{H}$, $Z=1, N=1$),
recording $\chi^\lambda(W_{\mathrm{free}})$, $\chi^\lambda(W_{\mathrm{atom}})$, and the Convention-D
Wedderburn weight $y_\lambda(1+\varepsilon)$ through order $\varepsilon^2$. -/
structure DeuteronH6IrrepDatum where
  /-- Free two-nucleon character $\chi^\lambda(W_{\mathrm{free}})$ mod $\varepsilon^3$. -/
  chiFree : QuadEpsSeries
  /-- Bound deuteron character $\chi^\lambda(W_{\mathrm{atom}})$ mod $\varepsilon^3$. -/
  chiAtom : QuadEpsSeries
  /-- Convention-D Wedderburn weight $y_\lambda(1+\varepsilon)$ mod $\varepsilon^3$. -/
  yWeight : QuadEpsSeries
  deriving DecidableEq, Repr

/-- Free-minus-bound character difference $\Delta\chi^\lambda = \chi^\lambda(W_{\mathrm{free}}) - \chi^\lambda(W_{\mathrm{atom}})$. -/
def DeuteronH6IrrepDatum.deltaChi (d : DeuteronH6IrrepDatum) : QuadEpsSeries :=
  QuadEpsSeries.sub d.chiFree d.chiAtom

/-- Weighted Wedderburn contribution $y_\lambda(1+\varepsilon)\,\Delta\chi^\lambda(1+\varepsilon) \pmod{\varepsilon^3}$. -/
def DeuteronH6IrrepDatum.weightedContrib (d : DeuteronH6IrrepDatum) : QuadEpsSeries :=
  QuadEpsSeries.mulModEps3 d.yWeight d.deltaChi

/-- Deuteron $H_6(q)$ character datum for the trivial partition $\lambda = (6)$. -/
def deuteronIrrep6 : DeuteronH6IrrepDatum :=
  { chiFree := ⟨1, 4, 8⟩
    chiAtom := ⟨1, 4, 17 / 2⟩
    yWeight := ⟨7 / 64, 0, 35 / 64⟩ }

/-- Deuteron $H_6(q)$ character datum for $\lambda = (5,1)$. -/
def deuteronIrrep51 : DeuteronH6IrrepDatum :=
  { chiFree := ⟨1, -3, -7 / 2⟩
    chiAtom := ⟨0, -5, -27 / 2⟩
    yWeight := ⟨5 / 64, 0, 5 / 64⟩ }

/-- Deuteron $H_6(q)$ character datum for $\lambda = (4,2)$. -/
def deuteronIrrep42 : DeuteronH6IrrepDatum :=
  { chiFree := ⟨1, -3, 17 / 2⟩
    chiAtom := ⟨0, 1, 31 / 2⟩
    yWeight := ⟨3 / 64, 0, -5 / 64⟩ }

/-- Deuteron $H_6(q)$ character datum for $\lambda = (3,3)$. -/
def deuteronIrrep33 : DeuteronH6IrrepDatum :=
  { chiFree := ⟨1, 4, 20⟩
    chiAtom := ⟨1, -2, -1 / 2⟩
    yWeight := ⟨1 / 64, 0, -3 / 64⟩ }

/-- Total two-row Wedderburn trace difference $\sum_{\ell(\lambda)\le 2} y_\lambda \Delta\chi^\lambda$
for the deuteron in $H_6(q)$ through order $\varepsilon^2$. -/
def deuteronH6TwoRowTraceDiff : QuadEpsSeries :=
  QuadEpsSeries.add
    (QuadEpsSeries.add deuteronIrrep6.weightedContrib deuteronIrrep51.weightedContrib)
    (QuadEpsSeries.add deuteronIrrep42.weightedContrib deuteronIrrep33.weightedContrib)

/-- Per-partition free-minus-bound character differences $\Delta\chi^\lambda$ and weighted
contributions $y_\lambda \Delta\chi^\lambda$ across the four active two-row partitions
$(6), (5,1), (4,2), (3,3)$ of $H_6(q)$ for the deuteron. -/
theorem deuteronH6_per_partition_deltaChi_and_weightedContrib :
    deuteronIrrep6.deltaChi = ⟨0, 0, -1 / 2⟩ ∧
    deuteronIrrep51.deltaChi = ⟨1, 2, 10⟩ ∧
    deuteronIrrep42.deltaChi = ⟨1, -4, -7⟩ ∧
    deuteronIrrep33.deltaChi = ⟨0, 6, 41 / 2⟩ ∧
    deuteronIrrep6.weightedContrib = ⟨0, 0, -7 / 128⟩ ∧
    deuteronIrrep51.weightedContrib = ⟨5 / 64, 5 / 32, 55 / 64⟩ ∧
    deuteronIrrep42.weightedContrib = ⟨3 / 64, -3 / 16, -13 / 32⟩ ∧
    deuteronIrrep33.weightedContrib = ⟨0, 3 / 32, 41 / 128⟩ := by
  norm_num [DeuteronH6IrrepDatum.deltaChi, DeuteronH6IrrepDatum.weightedContrib,
    QuadEpsSeries.sub, QuadEpsSeries.mulModEps3,
    deuteronIrrep6, deuteronIrrep51, deuteronIrrep42, deuteronIrrep33]

/-- The $H_6(q)$ two-row Wedderburn character sum for the deuteron reproduces the exact
$\varepsilon$-Taylor coefficients $(a_0, a_1, a_2) = (1/8, 1/16, 23/32)$ and the exact
$\hbar_q$-coefficients $(c_0, c_1, c_2) = (1/8, 1/16, 25/32)$ of the diagonal-insertion
expansion `canonicalDatumPN`. -/
theorem deuteronH6TwoRowTraceDiff_reproduces_canonical_pn :
    deuteronH6TwoRowTraceDiff = ⟨1 / 8, 1 / 16, 23 / 32⟩ ∧
    deuteronH6TwoRowTraceDiff.e0 = canonicalDatumPN.a0 ∧
    deuteronH6TwoRowTraceDiff.e1 = canonicalDatumPN.c1 ∧
    c2FromEpsTaylor deuteronH6TwoRowTraceDiff.e1 deuteronH6TwoRowTraceDiff.e2 = 25 / 32 ∧
    c2FromEpsTaylor deuteronH6TwoRowTraceDiff.e1 deuteronH6TwoRowTraceDiff.e2 = canonicalDatumPN.c2 := by
  norm_num [deuteronH6TwoRowTraceDiff, DeuteronH6IrrepDatum.deltaChi,
    DeuteronH6IrrepDatum.weightedContrib, QuadEpsSeries.sub, QuadEpsSeries.add,
    QuadEpsSeries.mulModEps3, deuteronIrrep6, deuteronIrrep51, deuteronIrrep42, deuteronIrrep33,
    InsertionExpansionDatum.c1, InsertionExpansionDatum.c2, c2FromEpsTaylor, canonicalDatumPN]

end QOU.MassTheory.DeltaLambdaPlancherelCovarianceAndC2
