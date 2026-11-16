/-
Copyright (c) 2026 QOU Contributors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
-/

/-!
# Lepton Two-Step Readout, Two-Strand Link Genus and Higgs Quartic Scale, Meson Negative-Syllable Volume Window, Actinide Sensitivity Slack, and Icosahedral Exceptional Orbits

This module formalizes structural lemmas across five work items under `qou-8lxd`:

1. **`qou-lsp9` (Two-step linear readout recurrence and node-sign criterion)**:
   Any linear functional on the two-strand algebra spanned by $\{1, \sigma_0\}$ reads out
   word powers via $\phi(w) = \alpha b_{w-1} + \beta b_w$, where $b_{n+1} = h b_n + b_{n-1}$.
   Because every two-step shift satisfies $b_{n+1} = (h^2 + 1) b_{n-1} + h b_{n-2}$,
   nonnegative weights $\alpha \ge 0, \beta > 0$ on positive sequence entries $b_{w-1} > 0, b_w > 0$
   yield strictly positive readouts $\phi(w) > 0$ (no sign change / node), whereas achieving a node
   $\phi(w) = 0$ on positive sequence entries requires opposite-sign coefficients $\alpha \beta < 0$.

2. **`qou-pgzo` (Two-strand torus link vs knot Euler characteristic and tree-level scalar quartic scale)**:
   For the two-strand closure $T(2, n)$, odd $n = 2m + 1$ has $1$ component ($\chi = 1 - 2m$,
   minimal surface genus $g = m$) whereas even $n = 2m$ has $2$ components ($\chi = 2 - 2m$,
   minimal surface genus $g = m - 1$). In particular, $T(2, 7)$ ($\mu = 1, \chi = -5$) and
   $T(2, 8)$ ($\mu = 2, \chi = -6$) share surface genus $g = 3$ while differing by $\Delta \chi = 1$
   and $\Delta \mu = 1$. Moreover, in the tree-level scalar potential relation $m_H^2 = 2 \lambda v^2$,
   distinct quartic self-couplings $\lambda_1 \neq \lambda_2$ at fixed vacuum expectation value $v > 0$
   yield distinct squared masses $m_H^2$, so the ratio $m_H^2 / v^2 = 2 \lambda$ is not pinned by $v$ alone.

3. **`qou-qpj9` (Three-braid negative-syllable hyperbolic volume window and crossing lower bound)**:
   Under the negative-syllable volume window $(s - 1) v_8 \le V < 4 s v_8$ for closed three-braids
   with $s \ge 1$ negative syllables where each negative syllable has exponent magnitude at least $3$,
   the total negative crossing count satisfies $c_- \ge 3 s$. A purely positive braid ($s = 0$) lies
   outside the $s \ge 1$ regime; for $s = 1$ ($\pi^\pm$ candidate) the lower volume bound vanishes and
   $c_- \ge 3$, while for $s = 5$ ($J/\psi$ threshold) $c_- \ge 15$ and the volume window spans $[4 v_8, 20 v_8)$.

4. **`qou-ultb` (Actinide cosmochronometry fractional-shift conversion and uncertainty slack)**:
   With log-sensitivity $S = |d\ln \alpha / d\ln q| > 0$, an observational bound $|\delta \alpha / \alpha| \le B$
   converts to $|\delta q / q| \le B / S$. Whenever $B > k \cdot S \cdot \sigma_q$ for an integer slack
   multiplier $k \ge 1$, the implied fractional bound $B / S$ strictly exceeds $k \cdot \sigma_q$.
   On integer-scaled bounds ($B = 2080000 \times 10^{-9}$, $S = 6861933 \times 10^{-6}$,
   $\sigma_q = 122335 \times 10^{-14}$), the slack factor exceeds $247000$.

5. **`qou-b5ic` (Order-60 rotational group exceptional orbits and antipodal chirality pairing)**:
   For the order-60 orientation-preserving icosahedral rotation group acting on $S^2$, the three
   exceptional stabilizer orders $(5, 3, 2)$ produce orbit sizes $(12, 20, 30)$ via $|O_x| \cdot |\text{Stab}(x)| = 60$,
   satisfying the spherical Euler-class deficit identity $(5 - 1) \cdot 12 + (3 - 1) \cdot 20 + (2 - 1) \cdot 30 = 2 \cdot 60 - 2 = 118$.
   Every exceptional orbit size is even and splits into antipodal pairs $\{u, -u\}$, so any sign-reversing
   linear form $\Gamma(-u) = -\Gamma(u)$ sums to zero across each antipodal pair and cannot select a hand $+u$ over $-u$
   by an orbit-level invariant alone.
-/

namespace QOU.Eightfold.LeptonReadoutHiggsScaleMesonSyllableAndIcosahedralOrbit

/-! ## Section 1: Two-Step Linear Readout Recurrence and Node-Sign Criterion (`qou-lsp9`) -/

/-- Linear readout $\phi = \alpha b_{\text{prev}} + \beta b_{\text{curr}}$ of two consecutive sequence values. -/
def twoStepReadout (alpha beta bPrev bCurr : Int) : Int :=
  alpha * bPrev + beta * bCurr

/-- One-step recurrence $b_{\text{next}} = h b_{\text{curr}} + b_{\text{prev}}$. -/
def nextRecurrenceTerm (h bPrev bCurr : Int) : Int :=
  h * bCurr + bPrev

/-- Two-step advancement identity: applying the recurrence twice gives
    $b_{n+2} = (h^2 + 1) b_n + h b_{n-1}$. -/
theorem two_step_recurrence_expansion (h bPrev bCurr : Int) :
    nextRecurrenceTerm h bCurr (nextRecurrenceTerm h bPrev bCurr) =
      (h * h + 1) * bCurr + h * bPrev := by
  dsimp [nextRecurrenceTerm]
  rw [Int.mul_add, Int.add_mul, ← Int.mul_assoc, Int.one_mul]
  omega

/-- Nonnegative weights $\alpha \ge 0, \beta > 0$ on positive entries $b_{\text{prev}} \ge 0, b_{\text{curr}} > 0$
    produce a strictly positive readout $\phi > 0$ (no node). -/
theorem twoStepReadout_pos_of_nonneg_weights
    (alpha beta bPrev bCurr : Int)
    (hAlpha : 0 ≤ alpha) (hBeta : 0 < beta)
    (hPrev : 0 ≤ bPrev) (hCurr : 0 < bCurr) :
    0 < twoStepReadout alpha beta bPrev bCurr := by
  dsimp [twoStepReadout]
  have h1 : 0 ≤ alpha * bPrev := Int.mul_nonneg hAlpha hPrev
  have h2 : 0 < beta * bCurr := Int.mul_pos hBeta hCurr
  omega

/-- If $\phi(\alpha, \beta, b_{\text{prev}}, b_{\text{curr}}) = 0$ on strictly positive sequence entries
    $b_{\text{prev}} > 0, b_{\text{curr}} > 0$ with $\beta > 0$, then $\alpha < 0$ (opposite signs required for a node). -/
theorem node_requires_negative_alpha
    (alpha beta bPrev bCurr : Int)
    (hBeta : 0 < beta) (hPrev : 0 < bPrev) (hCurr : 0 < bCurr)
    (hNode : twoStepReadout alpha beta bPrev bCurr = 0) :
    alpha < 0 := by
  dsimp [twoStepReadout] at hNode
  have hBetaCurr : 0 < beta * bCurr := Int.mul_pos hBeta hCurr
  have hAlphaPrev : alpha * bPrev < 0 := by omega
  have hNotNonneg : ¬ (0 ≤ alpha) := by
    intro hNonneg
    have hNonnegProd : 0 ≤ alpha * bPrev := Int.mul_nonneg hNonneg (Int.le_of_lt hPrev)
    omega
  omega

/-! ## Section 2: Two-Strand Torus Link Genus and Tree-Level Scalar Quartic Scale (`qou-pgzo`) -/

/-- Number of link components of the two-strand closure $T(2, n)$: $1$ for odd $n$, $2$ for even $n$. -/
def twoStrandComponents (n : Nat) : Nat :=
  if n % 2 == 1 then 1 else 2

/-- Minimal surface Euler characteristic $\chi = 2 - n$ for the canonical two-disk $n$-band surface of $T(2, n)$. -/
def twoStrandEulerChar (n : Nat) : Int :=
  2 - (n : Int)

/-- Minimal surface genus $g = (n - \mu) / 2$ of the two-strand closure $T(2, n)$. -/
def twoStrandGenus (n : Nat) : Nat :=
  (n - twoStrandComponents n) / 2

/-- $T(2, 7)$ is a 1-component knot with $\chi = -5$ and genus $g = 3$, whereas $T(2, 8)$ is a 2-component
    link with $\chi = -6$ and the same genus $g = 3$. -/
theorem t27_knot_vs_t28_link_invariants :
    twoStrandComponents 7 = 1 ∧
    twoStrandEulerChar 7 = -5 ∧
    twoStrandGenus 7 = 3 ∧
    twoStrandComponents 8 = 2 ∧
    twoStrandEulerChar 8 = -6 ∧
    twoStrandGenus 8 = 3 := by
  decide

/-- Tree-level squared scalar mass $m_H^2 = 2 \lambda v^2$ (in integer-scaled units). -/
def scalarSquaredMass (lam vSq : Int) : Int :=
  2 * lam * vSq

/-- At any fixed positive squared vacuum expectation value $v^2 > 0$, distinct quartic self-couplings
    $\lambda_1 < \lambda_2$ produce strictly distinct squared scalar masses $m_H^2(\lambda_1) < m_H^2(\lambda_2)$. -/
theorem scalarSquaredMass_strictMono_in_quartic
    (lam1 lam2 vSq : Int)
    (hLam : lam1 < lam2) (hVSq : 0 < vSq) :
    scalarSquaredMass lam1 vSq < scalarSquaredMass lam2 vSq := by
  dsimp [scalarSquaredMass]
  have hDiff : 0 < 2 * (lam2 - lam1) := by omega
  have hProd : 0 < (2 * (lam2 - lam1)) * vSq := Int.mul_pos hDiff hVSq
  have hExpand : (2 * (lam2 - lam1)) * vSq = 2 * lam2 * vSq - 2 * lam1 * vSq := by
    rw [Int.mul_sub, Int.sub_mul]
  omega

/-! ## Section 3: Three-Braid Negative-Syllable Volume Window and Crossing Lower Bound (`qou-qpj9`) -/

/-- Lower bound $3 s$ on negative crossings when each of the $s$ negative syllables has exponent magnitude $\ge 3$. -/
def minNegativeCrossings (s : Nat) : Nat :=
  3 * s

/-- Integer-scaled lower and upper volume window multipliers $(s - 1, 4 s)$ in units of the regular ideal octahedron volume $v_8$. -/
def syllableVolumeWindowMultipliers (s : Nat) : Nat × Nat :=
  (s - 1, 4 * s)

/-- If a closed braid has $s$ negative syllables and uniform syllable lower bound $b \ge 3$, then the total
    negative crossing count $s \cdot b$ is at least $3 s$, and strictly positive whenever $s \ge 1$. -/
theorem negative_crossing_lower_bound
    (s b : Nat) (hS : 1 ≤ s) (hB : 3 ≤ b) :
    minNegativeCrossings s ≤ s * b ∧ 3 ≤ s * b := by
  dsimp [minNegativeCrossings]
  have h1 : s * 3 ≤ s * b := Nat.mul_le_mul_left s hB
  have hComm : 3 * s = s * 3 := Nat.mul_comm 3 s
  omega

/-- Concrete syllable window verification for $s = 1$ ($\pi^\pm$ minimal candidate: multipliers $(0, 4)$, $c_- \ge 3$)
    and $s = 5$ ($J/\psi$ threshold candidate: multipliers $(4, 20)$, $c_- \ge 15$). -/
theorem pion_and_charmonium_syllable_bounds :
    syllableVolumeWindowMultipliers 1 = (0, 4) ∧
    minNegativeCrossings 1 = 3 ∧
    syllableVolumeWindowMultipliers 5 = (4, 20) ∧
    minNegativeCrossings 5 = 15 := by
  decide

/-! ## Section 4: Actinide Cosmochronometry Sensitivity Conversion and Slack (`qou-ultb`) -/

/-- Cross-multiplied sensitivity slack predicate: an observational bound $B$ exceeds $k$ times the
    sensitivity-propagated uncertainty $S \cdot \sigma_q$. -/
def hasSensitivitySlack (bScaled sScaled sigmaScaled k : Nat) : Prop :=
  k * sScaled * sigmaScaled < bScaled

/-- Whenever $B > k \cdot S \cdot \sigma_q$ for $k \ge 1$ and $S, \sigma_q > 0$, the observational bound $B$
    is strictly looser than the $1\sigma$ anchor uncertainty $S \cdot \sigma_q$. -/
theorem sensitivity_slack_implies_looser_than_anchor
    (bScaled sScaled sigmaScaled k : Nat)
    (hK : 1 ≤ k) (hS : 0 < sScaled) (hSigma : 0 < sigmaScaled)
    (hSlack : hasSensitivitySlack bScaled sScaled sigmaScaled k) :
    sScaled * sigmaScaled < bScaled := by
  dsimp [hasSensitivitySlack] at hSlack
  have hProdPos : 0 < sScaled * sigmaScaled := Nat.mul_pos hS hSigma
  have hLe : 1 * (sScaled * sigmaScaled) ≤ k * (sScaled * sigmaScaled) :=
    Nat.mul_le_mul_right (sScaled * sigmaScaled) hK
  have hAssoc : k * (sScaled * sigmaScaled) = k * sScaled * sigmaScaled := by
    rw [Nat.mul_assoc]
  omega

/-- Exact integer-scaled verification for the U II 3859.57 A actinide cosmochronometry bound:
    at common scale $10^{20}$, $B \cdot 10^{20} = 208000000000000000$,
    $S \cdot \sigma_q \cdot 10^{20} = 6861933 \times 122335 = 839454573555$,
    and the slack ratio has floor $k = 247779$. -/
theorem actinide_u2_cosmochronometry_slack_witness :
    hasSensitivitySlack 208000000000000000 6861933 122335 247779 ∧
    ¬ hasSensitivitySlack 208000000000000000 6861933 122335 247780 := by
  dsimp [hasSensitivitySlack]
  decide

/-! ## Section 5: Order-60 Rotational Exceptional Orbits and Antipodal Chirality Pairing (`qou-b5ic`) -/

/-- Exceptional orbit size $|O_x| = 60 / |\text{Stab}(x)|$ for the order-60 rotational group on $S^2$. -/
def exceptionalOrbitSize (stabOrder : Nat) : Nat :=
  60 / stabOrder

/-- The three exceptional stabilizer orders $(5, 3, 2)$ yield orbit sizes $(12, 20, 30)$, each of which is even
    (divisible by $2$ into antipodal pairs $\{u, -u\}$), and satisfy the spherical Euler-class deficit identity
    $(5 - 1) \cdot 12 + (3 - 1) \cdot 20 + (2 - 1) \cdot 30 = 2 \cdot 60 - 2 = 118$. -/
theorem order60_exceptional_orbits_and_euler_deficit :
    exceptionalOrbitSize 5 = 12 ∧
    exceptionalOrbitSize 3 = 20 ∧
    exceptionalOrbitSize 2 = 30 ∧
    (exceptionalOrbitSize 5) % 2 = 0 ∧
    (exceptionalOrbitSize 3) % 2 = 0 ∧
    (exceptionalOrbitSize 2) % 2 = 0 ∧
    (5 - 1) * exceptionalOrbitSize 5 +
      (3 - 1) * exceptionalOrbitSize 3 +
      (2 - 1) * exceptionalOrbitSize 2 = 2 * 60 - 2 := by
  decide

/-- Antipodal cancellation: for any odd chirality functional satisfying $\Gamma(-u) = -\Gamma(u)$,
    the sum over an antipodal pair $\{u, -u\}$ vanishes identically ($\Gamma(u) + (-\Gamma(u)) = 0$),
    whereas a non-zero chirality value $\Gamma(u) \neq 0$ takes strictly opposite values on the two hands. -/
theorem antipodal_pair_chirality_sum_zero_and_distinction
    (gammaU : Int) (hNonzero : gammaU ≠ 0) :
    gammaU + (-gammaU) = 0 ∧ gammaU ≠ -gammaU := by
  omega

end QOU.Eightfold.LeptonReadoutHiggsScaleMesonSyllableAndIcosahedralOrbit
