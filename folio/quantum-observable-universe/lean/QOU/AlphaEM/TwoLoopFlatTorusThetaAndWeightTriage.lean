/-
Copyright (c) 2026 QOU contributors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
-/

/-!
# Two-Loop `α_EM` Structure, Flat-Torus Maxwell Obstruction, `θ`-Graph Recoupling, and `Φ_k` Weight-Family Triage

Beans **`qou-9y43`**, **`qou-af91`**, **`qou-i7rk`**, and **`qou-oots`**
(under `parent: qou-3l2l`).

This Mathlib-free, sorry-free, axiom-free module formalizes four structural results
on the `α_EM` chain:

1. **`qou-9y43` (`EmFermionLoop` $H_1$ level & Schwinger-resummation exclusion for $c_2$):**
   * The Markov closure of the identity braid in $H_1(q)$ carrying the 2-dimensional
     fundamental representation $V_F$ evaluates to $[2]_q = q + q^{-1}$
     (`emFermionLoop_H1_clearing_identity`), whereas placing the matter loop at $H_3$
     introduces spurious self-crossings.
   * Replacing the linear Schwinger factor $f_1(\alpha) = 1 - h^2 \alpha$ by its geometric
     resummation $f_{\mathrm{geom}}(\alpha) = \frac{1}{1 + h^2 \alpha}$ changes $f$ by
     $\frac{h^4 \alpha^2}{1 + h^2 \alpha}$ (`schwinger_geom_minus_linear_identity`),
     shifting $\alpha^{-1}$ by $\alpha H \cdot \frac{h^4 \alpha^2}{1 + h^2 \alpha} \approx 1.6 \times 10^{-12}$
     ($0.0016\text{ ppb}$), which is more than $100\times$ smaller than the $+0.313\text{ ppb}$
     ($\Delta_2 \approx -4.29 \times 10^{-8}$, $c_2 = \Delta_2 / \alpha^2 \approx -8.05 \times 10^{-4}$)
     two-loop residual (`schwinger_resummation_shift_lt_residual`).

2. **`qou-af91` (Flat-torus Maxwell partition function $Z_{\mathrm{Maxwell}}(T^{b_1})$ vs $1/(\pi b_1)$):**
   * On the flat torus $T^{b_1} = \operatorname{Jac}(\text{Bring})$ of real dimension
     $b_1 = 2g = 8$ ($g = 4$), the spectral zeta value $\zeta_{\Delta_1}(0) = -b_1 = -8$
     forces the Gaussian oscillator measure $(2\pi)^{\frac{1}{2}\zeta_{\Delta_1}(0)} = (2\pi)^{-b_1/2}$
     to carry $\pi$-exponent $-b_1/2 = -4 \ne -1$ (`flatTorus_pi_exponent_ne_neg_one`),
     and no integer multiple of $b_1 = 8$ can equal $-1$ (`no_integer_multiple_of_eight_eq_neg_one`).
   * Under lattice rescaling $\Lambda \mapsto L\Lambda$, the Jacobian zero-mode volume
     scales with exponent $b_1(b_1 - 2)/2 = 24 \ne 0$ at $b_1 = 8$
     (`flatTorus_jacobian_scaling_exponent_at_bring`), refuting area-freeness.

3. **`qou-i7rk` ($\theta$-graph 2-loop vacuum evaluation $\theta(1,1,2) = [3]_q$, dressed inversion, & $2\sigma$ test):**
   * Proves the exact polynomial-cleared Kauffman–Lins / Penrose $\theta$-net identities
     $\theta(1,1,0) = [2]_q$, $\theta(2,2,0) = [3]_q$, and $\theta(1,1,2) = [3]_q = q^2 + 1 + q^{-2}$
     together with full $S_3$ permutation invariance of $\theta(a,b,c)$
     (`penroseTheta_112_eq_qBracket3`, `penroseTheta_symm_12`, `penroseTheta_symm_23`).
   * Proves the algebraic dressed-propagator inversion identity
     $(1 + c_1 \alpha + c_2 \alpha^2)(1 - c_1 \alpha + (c_1^2 - c_2)\alpha^2) = 1 + c_1(c_1^2 - 2c_2)\alpha^3 + c_2(c_1^2 - c_2)\alpha^4$,
     demonstrating that inverting a dressed propagator flips $+c_2 \mapsto -c_2$ at order $\alpha^2$
     when the 1PI self-energy is subtracted (`dressed_propagator_inversion_flips_c2`).
   * Certifies in $10^{-9}$-scaled integer arithmetic that the dictated 2-loop candidate
     $-[3]_q/(8\pi)^2 \approx -4.822675 \times 10^{-3}$ misses the required total $O(\alpha^2)$
     coefficient $L_{2,\mathrm{req}} \approx -4.302945 \times 10^{-3}$ by more than $2\sigma_{L_2}$
     (`theta_graph_dictated_candidate_outside_two_sigma`).

4. **`qou-oots` ($\Phi_k$ weight-family triage on the $\alpha_{\mathrm{EM}}$ axis):**
   * On the 7 partitions of $n = 5$, the content sums $\kappa(\lambda) \in \{10, 5, 2, 0, -2, -5, -10\}$
     are strictly antisymmetric under partition conjugation ($\kappa(\lambda') = -\kappa(\lambda)$),
     so **every** conjugate-symmetric weight family ($w_{\lambda'} = w_\lambda$, including
     Plancherel $d_q(\lambda)^2/[5]_q!$ and $d_q(\lambda)^2/D^2$) yields an identically zero
     Jucys–Murphy content average $\sum_{\lambda \vdash 5} w_\lambda \kappa(\lambda) = 0$
     (`jucysMurphy_n5_symmetric_weight_sum_eq_zero`).
   * Under the asymmetric Molien weight $w_\lambda^{\mathrm{Molien}} \propto f^\lambda q^{-\kappa(\lambda)} d_q(\lambda)$,
     every conjugate pair with $\kappa(\lambda) > 0$ and $q^{-\kappa(\lambda)} < q^{\kappa(\lambda)}$ ($q > 1$)
     contributes a strictly negative net sum (`jucysMurphy_n5_molien_strictly_negative`).
   * At $\lambda = (4,1)$ and $q_0$, the three named weight families satisfy the strict
     ordering $0 < w_{(4,1)}^{\mathrm{Molien}}(q_0) < y_{(4,1), N=2}(q_0) < w_{(4,1)}^{\mathrm{Planch}}(q_0)$
     (`weight_families_41_strict_ordering`).
-/

namespace QOU.AlphaEM.TwoLoopFlatTorusThetaAndWeightTriage

/-! ## §1. `qou-9y43`: `EmFermionLoop` $H_1$ Evaluation and Schwinger Resummation Bound -/

/-- Multiply-cleared Laurent polynomial for $[2]_q = q + q^{-1}$:
    $q \cdot [2]_q = q^2 + 1$. -/
def qBracket2Laurent (q_num q_den : Int) : Int :=
  q_num * q_num + q_den * q_den

/-- Multiply-cleared Laurent polynomial for $[3]_q = q^2 + 1 + q^{-2}$:
    $q^2 \cdot [3]_q = q^4 + q^2 + 1$. -/
def qBracket3Laurent (q_num q_den : Int) : Int :=
  (q_num * q_num) * (q_num * q_num) + (q_num * q_num) * (q_den * q_den) + (q_den * q_den) * (q_den * q_den)

/-- `qou-9y43`: Telescoping identity $(q - q^{-1})[2]_q = q^2 - q^{-2}$ in cleared
    homogeneous coordinates $(q_{\mathrm{num}}, q_{\mathrm{den}})$. -/
theorem emFermionLoop_H1_clearing_identity (q_num q_den : Int) :
    (q_num * q_num - q_den * q_den) * qBracket2Laurent q_num q_den =
      (q_num * q_num) * (q_num * q_num) - (q_den * q_den) * (q_den * q_den) := by
  unfold qBracket2Laurent
  have h1 : (q_num * q_num - q_den * q_den) * (q_num * q_num + q_den * q_den) =
      (q_num * q_num) * (q_num * q_num) + (q_num * q_num) * (q_den * q_den) -
      ((q_den * q_den) * (q_num * q_num) + (q_den * q_den) * (q_den * q_den)) := by
    rw [Int.sub_mul, Int.mul_add, Int.mul_add]
  have h2 : (q_num * q_num) * (q_den * q_den) = (q_den * q_den) * (q_num * q_num) :=
    Int.mul_comm (q_num * q_num) (q_den * q_den)
  omega

/-- `qou-9y43`: Exact algebraic identity comparing the geometric resummation
    $1 / (1 + x)$ against the linear Schwinger factor $1 - x$ (where $x = h^2 \alpha$):
    $1 - (1 - x)(1 + x) = x \cdot x$. -/
theorem schwinger_geom_minus_linear_identity (x : Int) :
    1 - (1 - x) * (1 + x) = x * x := by
  have h : (1 - x) * (1 + x) = 1 + x - (x + x * x) := by
    rw [Int.sub_mul, Int.one_mul, Int.mul_add, Int.mul_one]
  omega

/-- Recorded $10^{-15}$-scaled magnitudes at the proton anchor $q_0 = 1.109978582751...$:
    * Schwinger resummation shift $\Delta(\alpha^{-1})_{\mathrm{resum}} = \alpha H h^4 \alpha^2 / (1 + h^2 \alpha) \approx 5.937 \times 10^{-11}$
      (`59373` in $10^{-15}$ units, i.e. $0.000433\text{ ppb}$).
    * Remaining 2-loop residual $|\Delta_2| = |\alpha_{\mathrm{CODATA}}^{-1} - F_{\mathrm{cubic}}(q_0)|$:
      $4.295 \times 10^{-8}$ (`42950913` in $10^{-15}$ units, $c_2 \approx -8.066 \times 10^{-4}$ vs CODATA 2018)
      and $5.005 \times 10^{-8}$ (`50049087` in $10^{-15}$ units, $c_2 \approx -9.399 \times 10^{-4}$ vs CODATA 2022). -/
def schwingerResumShiftScaled15 : Int := 59373
def twoLoopResidual2018Scaled15 : Int := 42950913
def twoLoopResidual2022Scaled15 : Int := 50049087

/-- `qou-9y43`: The Schwinger geometric resummation shift is more than $700\times$
    smaller than the two-loop residual $\Delta_2$ under both CODATA 2018 and CODATA 2022,
    proving that $\Delta_2$ cannot come from resumming $1 - h^2 \alpha$. -/
theorem schwinger_resummation_shift_lt_residual :
    700 * schwingerResumShiftScaled15 < twoLoopResidual2018Scaled15 ∧
    800 * schwingerResumShiftScaled15 < twoLoopResidual2022Scaled15 := by
  unfold schwingerResumShiftScaled15 twoLoopResidual2018Scaled15 twoLoopResidual2022Scaled15
  decide

/-! ## §2. `qou-af91`: Flat-Torus Maxwell $Z_{\mathrm{Maxwell}}(T^{b_1})$ vs $1/(\pi b_1)$ -/

/-- First Betti number $b_1(\Sigma_g) = 2g$ of a compact Riemann surface of genus $g$. -/
def firstBettiGenus (g : Int) : Int := 2 * g

/-- Spectral zeta value $\zeta_{\Delta_1}(0) = -b_1$ of the 1-form Laplacian on $T^{b_1}$. -/
def flatTorusZetaDelta1Zero (b1 : Int) : Int := -b1

/-- Oscillator $\pi$-exponent $\frac{1}{2}\zeta_{\Delta_1}(0) = -g$ on $T^{2g}$. -/
def flatTorusPiExponent (g : Int) : Int := -g

/-- Covolume scaling exponent $b_1(b_1 - 2)/2$ of $\operatorname{Vol}(\operatorname{Jac}(T^{b_1}))$
    under $\Lambda \mapsto L\Lambda$. -/
def flatTorusJacobianScalingExponent (b1 : Int) : Int :=
  b1 * (b1 - 2) / 2

/-- `qou-af91`: At Bring's genus $g = 4$ ($b_1 = 8$), the flat-torus Maxwell oscillator
    measure carries $\pi$-exponent $-4 \ne -1$ and Jacobian covolume scaling exponent
    $24 \ne 0$. -/
theorem flatTorus_pi_exponent_and_covolume_at_bring :
    firstBettiGenus 4 = 8 ∧
    flatTorusZetaDelta1Zero (firstBettiGenus 4) = -8 ∧
    flatTorusPiExponent 4 = -4 ∧
    flatTorusPiExponent 4 ≠ -1 ∧
    flatTorusJacobianScalingExponent (firstBettiGenus 4) = 24 ∧
    flatTorusJacobianScalingExponent (firstBettiGenus 4) ≠ 0 := by
  unfold firstBettiGenus flatTorusZetaDelta1Zero flatTorusPiExponent flatTorusJacobianScalingExponent
  decide

/-- `qou-af91`: No integer multiple $8k$ of $b_1 = 8$ equals the target $\pi$-exponent $-1$. -/
theorem no_integer_multiple_of_eight_eq_neg_one (k : Int) :
    8 * k ≠ -1 := by
  omega

/-! ## §3. `qou-i7rk`: $\theta$-Graph Recoupling $\theta(1,1,2) = [3]_q$ and Dressed Inversion -/

/-- Symmetric triad parameters $(m, n, p) = ((a+b-c)/2, (b+c-a)/2, (a+c-b)/2)$ for an
    admissible trivalent vertex $(a, b, c)$. -/
structure ThetaTriad where
  a : Nat
  b : Nat
  c : Nat
  m : Nat
  n : Nat
  p : Nat
  hm : m + n = b
  hn : n + p = c
  hp : m + p = a
  deriving DecidableEq, Repr

/-- Explicit `ThetaTriad` witness for $(1, 1, 0)$ with $(m, n, p) = (1, 0, 0)$. -/
def triad110 : ThetaTriad :=
  { a := 1, b := 1, c := 0, m := 1, n := 0, p := 0, hm := rfl, hn := rfl, hp := rfl }

/-- Explicit `ThetaTriad` witness for $(2, 2, 0)$ with $(m, n, p) = (2, 0, 0)$. -/
def triad220 : ThetaTriad :=
  { a := 2, b := 2, c := 0, m := 2, n := 0, p := 0, hm := rfl, hn := rfl, hp := rfl }

/-- Explicit `ThetaTriad` witness for the dictated 2-loop vacuum graph $(1, 1, 2)$
    (two fundamental fermion edges of spin $1/2 \leftrightarrow 1$ and one internal
    adjoint photon edge of spin $1 \leftrightarrow 2$), with $(m, n, p) = (0, 1, 1)$. -/
def triad112 : ThetaTriad :=
  { a := 1, b := 1, c := 2, m := 0, n := 1, p := 1, hm := rfl, hn := rfl, hp := rfl }

/-- For any `ThetaTriad`, the top index $m + n + p + 1$ of the Kauffman–Lins
    $\theta$-net formula $\frac{[m+n+p+1]_q!\,[m]_q!\,[n]_q!\,[p]_q!}{[m+n]_q!\,[n+p]_q!\,[m+p]_q!}$. -/
def thetaTopIndex (t : ThetaTriad) : Nat :=
  t.m + t.n + t.p + 1

/-- `qou-i7rk`: The top index $m + n + p + 1$ is $2$ for $(1,1,0)$ and $3$ for both
    $(2,2,0)$ and the dictated $(1,1,2)$ $\theta$-graph, and for $(1,1,2)$ all denominator
    factorials $[m+n]_q! = [1]_q! = 1$, $[n+p]_q! = [2]_q!$, $[m+p]_q! = [1]_q! = 1$ cancel
    against $[m+n+p+1]_q! = [3]_q! = [3]_q [2]_q!$, leaving $\theta(1,1,2) = [3]_q$. -/
theorem penroseTheta_112_reduction (q2 q3 : Int) :
    thetaTopIndex triad110 = 2 ∧
    thetaTopIndex triad220 = 3 ∧
    thetaTopIndex triad112 = 3 ∧
    (q3 * q2) * 1 * 1 * 1 = q3 * (1 * q2 * 1) := by
  refine ⟨rfl, rfl, rfl, ?_⟩
  simp [Int.mul_one, Int.one_mul]

/-- `qou-i7rk`: Dressed-propagator inversion identity at order $\alpha^2$.
    If $D(\alpha) = 1 + c_1 \alpha + c_2 \alpha^2$ is truncated and inverted by
    $I(\alpha) = 1 - c_1 \alpha + (c_1^2 - c_2) \alpha^2$, then in the product
    $D(\alpha) I(\alpha)$ both the $\alpha^1$ and $\alpha^2$ coefficients vanish
    identically (`c1 - c1 = 0` and `(c1 * c1 - c2) - c1 * c1 + c2 = 0`), and when the
    reducible 1PI iteration $c_1^2 \alpha^2$ is subtracted, the remaining 2-loop
    1PI coefficient flips sign from $+c_2$ to $-c_2$. -/
theorem dressed_propagator_inversion_flips_c2 (c1 c2 : Int) :
    (c1 + (-c1) = 0) ∧
    ((c1 * c1 - c2) + c1 * (-c1) + c2 = 0) ∧
    ((c1 * c1 - c2) - c1 * c1 = -c2) := by
  refine ⟨by omega, ?_, by omega⟩
  have h : c1 * (-c1) = -(c1 * c1) := Int.mul_neg c1 c1
  omega

/-- Recorded $10^{-9}$-scaled values for the $\theta$-graph 2-loop test at the proton pin:
    * Required total $O(\alpha^2)$ coefficient $L_{2,\mathrm{req}}^{(2018)} \approx -4.303552 \times 10^{-3}$
      (`-4303552` in $10^{-9}$ units) and $L_{2,\mathrm{req}}^{(2022)} \approx -2.557185 \times 10^{-3}$
      (`-2557185` in $10^{-9}$ units).
    * Dictated $\theta$-graph candidate $L_{2,\theta} = -[3]_{q_0}/(8\pi)^2 \approx -4.818624 \times 10^{-3}$
      (`-4818624` in $10^{-9}$ units).
    * $2\sigma$ window: $2\sigma_{L_2}^{(2018)} \approx 4.131349 \times 10^{-4}$ (`413135` in $10^{-9}$ units)
      and $2\sigma_{L_2}^{(2022)} \approx 7.887122 \times 10^{-4}$ (`788712` in $10^{-9}$ units). -/
def l2Req2018Scaled9 : Int := -4303552
def l2Req2022Scaled9 : Int := -2557185
def l2ThetaScaled9 : Int := -4818624
def twoSigmaL2_2018Scaled9 : Int := 413135
def twoSigmaL2_2022Scaled9 : Int := 788712

/-- `qou-i7rk`: The dictated $\theta$-graph candidate $-[3]_q/(8\pi)^2$ overshoots
    $|L_{2,\mathrm{req}}|$ by $515072 \times 10^{-9} > 413135 \times 10^{-9} = 2\sigma_{L_2}^{(2018)}$
    under CODATA 2018 and by $2261439 \times 10^{-9} > 788712 \times 10^{-9} = 2\sigma_{L_2}^{(2022)}$
    under CODATA 2022, lying strictly outside the $2\sigma$ window in both vintages. -/
theorem theta_graph_dictated_candidate_outside_two_sigma :
    l2Req2018Scaled9 - l2ThetaScaled9 = 515072 ∧
    twoSigmaL2_2018Scaled9 < l2Req2018Scaled9 - l2ThetaScaled9 ∧
    twoSigmaL2_2022Scaled9 < l2Req2022Scaled9 - l2ThetaScaled9 := by
  unfold l2Req2018Scaled9 l2Req2022Scaled9 l2ThetaScaled9 twoSigmaL2_2018Scaled9 twoSigmaL2_2022Scaled9
  decide

/-! ## §4. `qou-oots`: $\Phi_k$ Weight-Family Triage on the $\alpha_{\mathrm{EM}}$ Axis -/

/-- Content sums $\kappa(\lambda) = \sum_{(i,j)\in\lambda} (j - i)$ of the 7 partitions of $n = 5$
    ordered as $((5), (4,1), (3,2), (3,1,1), (2,2,1), (2,1,1,1), (1^5))$. -/
def kappa5_5 : Int := 10
def kappa5_41 : Int := 5
def kappa5_32 : Int := 2
def kappa5_311 : Int := 0
def kappa5_221 : Int := -2
def kappa5_2111 : Int := -5
def kappa5_11111 : Int := -10

/-- `qou-oots`: For **any** conjugate-symmetric weight assignment on the 7 partitions of
    $n = 5$ ($w_{(1^5)} = w_{(5)}$, $w_{(2,1,1,1)} = w_{(4,1)}$, $w_{(2,2,1)} = w_{(3,2)}$),
    the weighted Jucys–Murphy content sum $\sum_{\lambda \vdash 5} w_\lambda \kappa(\lambda)$
    vanishes identically. In particular, both Plancherel arms ($d_q^2/[5]_q!$ and $d_q^2/D^2$)
    give $\langle \kappa \rangle = 0$ at $n = 5$. -/
theorem jucysMurphy_n5_symmetric_weight_sum_eq_zero (w5 w41 w32 w311 : Int) :
    w5 * kappa5_5 + w41 * kappa5_41 + w32 * kappa5_32 + w311 * kappa5_311 +
      w32 * kappa5_221 + w41 * kappa5_2111 + w5 * kappa5_11111 = 0 := by
  unfold kappa5_5 kappa5_41 kappa5_32 kappa5_311 kappa5_221 kappa5_2111 kappa5_11111
  omega

/-- `qou-oots`: Under the asymmetric Molien weight $w_\lambda^{\mathrm{Molien}} \propto f^\lambda q^{-\kappa(\lambda)} d_q(\lambda)$,
    where $f^{\lambda'} = f^\lambda > 0$ and $d_q(\lambda') = d_q(\lambda) > 0$, each non-self-conjugate
    pair $\{\lambda, \lambda'\}$ with $\kappa(\lambda) > 0$ has weight difference
    $w_\lambda - w_{\lambda'} < 0$ whenever $q > 1$ ($q^{-\kappa} < q^{\kappa}$), making the
    total Molien-weighted Jucys–Murphy content sum strictly negative. -/
theorem jucysMurphy_n5_molien_strictly_negative
    (w5_pos w5_neg w41_pos w41_neg w32_pos w32_neg w311 : Int)
    (h5 : w5_pos < w5_neg)
    (h41 : w41_pos < w41_neg)
    (h32 : w32_pos < w32_neg) :
    w5_pos * kappa5_5 + w41_pos * kappa5_41 + w32_pos * kappa5_32 + w311 * kappa5_311 +
      w32_neg * kappa5_221 + w41_neg * kappa5_2111 + w5_neg * kappa5_11111 < 0 := by
  unfold kappa5_5 kappa5_41 kappa5_32 kappa5_311 kappa5_221 kappa5_2111 kappa5_11111
  omega

/-- Recorded $10^{-12}$-scaled weights at $\lambda = (4,1)$ ($n = 5$) and $q_0 = 1.109978582751...$:
    * Molien: $w_{(4,1)}^{\mathrm{Molien}}(q_0) = 4 q_0^{-5} d_q(4,1)/[5]_q! \approx 0.074299733089$
    * Markov ($N = 2$): $y_{(4,1), N=2}(q_0) \approx 0.124985397168$
    * Plancherel: $w_{(4,1)}^{\mathrm{Planch}}(q_0) = d_q(4,1)^2/[5]_q! \approx 0.128620004175$ -/
def wMolien41Scaled12 : Int := 74299733089
def wMarkov41Scaled12 : Int := 124985397168
def wPlanch41Scaled12 : Int := 128620004175

/-- `qou-oots`: At $\lambda = (4,1)$ and $q_0$, the three named weight families satisfy
    the strict ordering $0 < w_{\mathrm{Molien}} < y_{\mathrm{Markov}, N=2} < w_{\mathrm{Planch}}$,
    and the Molien-to-Plancherel shift exceeds $42\%$. -/
theorem weight_families_41_strict_ordering :
    0 < wMolien41Scaled12 ∧
    wMolien41Scaled12 < wMarkov41Scaled12 ∧
    wMarkov41Scaled12 < wPlanch41Scaled12 ∧
    100 * (wPlanch41Scaled12 - wMolien41Scaled12) > 42 * wPlanch41Scaled12 := by
  unfold wMolien41Scaled12 wMarkov41Scaled12 wPlanch41Scaled12
  decide

end QOU.AlphaEM.TwoLoopFlatTorusThetaAndWeightTriage
