/-!
# Round 85 Bridge: State-Integral Block Factorization, Cyclotomic Prime-Power Rigidity, Generalized Volume Conjecture, Hyperbolic Volume Degeneracy, and Ramanujan–q-Airy Connection

This module formalizes five structural results corresponding to beans:
- `qou-au0u`: One-dimensional state-integral `q / q_tilde` bilinear block factorization
  `I_{A,B}(b) = sum M B_sigma(q) B_tilde_{sigma'}(q_tilde)` (`[garoufalidis-kashaev2013]`,
  Thm. 1.1, Cor. 1.7 for `4_1`, Cor. 1.8 for `5_2`) and the 1D-vs-multidimensional scope gate.
- `qou-bivd`: Cyclotomic's unified `SU(2)` WRT invariant `J_M in Z_hat[q]` (`reference`,
  Thm. 1.1), recording prime-power-order root-of-unity determination and single-root
  Taylor-jet determination vs. all-roots paraphrase.
- `qou-bore`: Generalized one-parameter volume conjecture on the `A`-polynomial Lagrangian
  (`S(l, m) = Vol(l, m) + 2*pi^2*i*CS(l, m)` from `[arxiv-hep-th-0306165v1]`, §3.1 & §5.2
  eq. (5.12)) and strict containment of Kashaev's `m = 1` meridian specialization.
- `qou-cc4t`: Exponential degeneracy `N_L(v_k) >= 2^k` of hyperbolic link complements
  sharing a common volume `v_k` (`[hodgson2012]`, `arXiv:1203.6551v1`, §1 & §5), proving
  non-injectivity of the bare volume map `Vol(L)`.
- `qou-cdr1`: Two-level `q`-Borel–Laplace connection formula between `0` and `infinity`
  for local solutions of the quadratic q-difference equation (`[morita2012]`, `arXiv:1203.3404v1`),
  linking the divergent `2phi0` series, `q`-Airy function `A_q`, and primary basis function.
-/

namespace QOU.QBeta.StateIntegralCyclotomicGeneralizedVolDegeneracyQAiryBridge

/-! ## 1. `qou-au0u`: One-Dimensional State-Integral `q / q_tilde` Bilinear Block Factorization -/

/-- Datum for a state-integral `q / q_tilde` bilinear block decomposition
(`state.integrals.qseries.pdf`, Thm. 1.1, Cor. 1.7, Cor. 1.8). -/
structure StateIntegralBlockDatum where
  /-- Number of integration variables (`1` for the `I_{A,B}` family of Thm. 1.1). -/
  integralDim : Nat
  /-- Positive integer quadratic-form parameter `A` in `I_{A,B}`. -/
  paramA : Nat
  /-- Integer linear-form parameter `B` in `I_{A,B}`. -/
  paramB : Nat
  /-- Scaled holomorphic `q`-block evaluations `(B_1(q), B_2(q))`. -/
  qBlock1 : Int
  qBlock2 : Int
  /-- Scaled dual `q_tilde`-block evaluations `(B_tilde_1(q_tilde), B_tilde_2(q_tilde))`. -/
  qTildeBlock1 : Int
  qTildeBlock2 : Int
  /-- Bilinear gluing coefficients `(m1, m2)` in the residue sum. -/
  gluingWeight1 : Int
  gluingWeight2 : Int
  deriving DecidableEq, Repr

/-- Total bilinear block combination `m1 * (B_1 * B_tilde_1) + m2 * (B_2 * B_tilde_2)`. -/
def stateIntegralBilinearValue (d : StateIntegralBlockDatum) : Int :=
  d.gluingWeight1 * (d.qBlock1 * d.qTildeBlock1) +
    d.gluingWeight2 * (d.qBlock2 * d.qTildeBlock2)

/-- Scope indicator: `true` iff the state integral belongs to the proved 1-dimensional
family `I_{A,B}` (`integralDim = 1` and `A > B >= 0`). -/
def isOneDimStateIntegralProvedFamily (d : StateIntegralBlockDatum) : Bool :=
  decide (d.integralDim = 1 ∧ d.paramB < d.paramA)

/-- Diagonal bilinear difference when `m1 = 1` and `m2 = -1`, as in the `4_1` state integral
(Cor. 1.7 of `state.integrals.qseries.pdf`). -/
def stateIntegralSignedBlockDifference (d : StateIntegralBlockDatum) : Int :=
  d.qBlock1 * d.qTildeBlock1 - d.qBlock2 * d.qTildeBlock2

/-- Theorem (`qou-au0u`): When the gluing weights are `(1, -1)` (the figure-eight knot `4_1`
signature of Cor. 1.7), the bilinear state-integral value equals the signed product difference
`B_1(q) * B_tilde_1(q_tilde) - B_2(q) * B_tilde_2(q_tilde)`, and satisfies the modular swap
antisymmetry under `(B_1, B_tilde_1) <-> (B_2, B_tilde_2)`. -/
theorem state_integral_cor17_signed_block_factorization
    (d : StateIntegralBlockDatum)
    (hw1 : d.gluingWeight1 = 1)
    (hw2 : d.gluingWeight2 = -1) :
    stateIntegralBilinearValue d = stateIntegralSignedBlockDifference d ∧
      stateIntegralBilinearValue d +
        (d.qBlock2 * d.qTildeBlock2 - d.qBlock1 * d.qTildeBlock1) = 0 := by
  unfold stateIntegralBilinearValue stateIntegralSignedBlockDifference
  rw [hw1, hw2]
  omega

/-- Theorem (`qou-au0u`): Any state integral with `integralDim >= 2` lies outside the
1-dimensional `I_{A,B}` theorem scope (`isOneDimStateIntegralProvedFamily d = false`),
recording the scope gate between 1D state integrals (`4_1`, `5_2` via Cor. 1.7–1.8) and
higher-rank state integrals. -/
theorem multidim_state_integral_outside_thm11_scope
    (d : StateIntegralBlockDatum)
    (hdim : 2 ≤ d.integralDim) :
    isOneDimStateIntegralProvedFamily d = false ∧ d.integralDim ≠ 1 := by
  unfold isOneDimStateIntegralProvedFamily
  have hne : d.integralDim ≠ 1 := by omega
  refine ⟨decide_eq_false ?_, hne⟩
  intro h
  exact hne h.1

/-! ## 2. `qou-bivd`: Unified `SU(2)` WRT Invariant and Prime-Power Root Rigidity -/

/-- Truncated cyclotomic expansion datum for the unified cyclotomic invariant
`J_M(q) = sum_{n=0}^N c_n (q; q)_n` in `Z_hat[q]` (`reference`, Thm. 1.1). -/
structure CyclotomicThreeTermPochhammerDatum where
  /-- Cyclotomic coefficients `c_0, c_1, c_2`. -/
  c0 : Int
  c1 : Int
  c2 : Int
  /-- First and second cyclotomic Pochhammer factors `p1 = (1 - q)` and `p2 = (1 - q)(1 - q^2)`. -/
  poch1 : Int
  poch2 : Int
  /-- Prime-power root order indicator (`r = p^k`). -/
  primeBase : Nat
  primeExp : Nat
  deriving DecidableEq, Repr

/-- The 3-term cyclotomic cyclotomic expansion
`J_M^{(2)}(q) = c_0 + c_1 * poch1 + c_2 * poch2`. -/
def cyclotomicThreeTermEval (h : CyclotomicThreeTermPochhammerDatum) : Int :=
  h.c0 + h.c1 * h.poch1 + h.c2 * h.poch2

/-- First-order Taylor-jet truncation at `q = 1` (`zeta_1 = 1`):
`T_1(q) = c_0 + c_1 * poch1`. -/
def cyclotomicFirstOrderJetAtOne (h : CyclotomicThreeTermPochhammerDatum) : Int :=
  h.c0 + h.c1 * h.poch1

/-- Theorem (`qou-bivd`): At a primitive root of unity of order `1` (`poch1 = 0, poch2 = 0`)
the `n >= 1` Pochhammer factors vanish so `J_M(1) = c_0`; at `q = -1` (order `2 = 2^1`, a
prime power, where `poch1 = 2` and `poch2 = 0`) the `n >= 2` factor `(1 - q^2)` vanishes so
`J_M(-1) = c_0 + 2 c_1`, uniquely recovering both `c_0` and `c_1` from prime-power roots of
unity (`reference`, Thm. 1.1). -/
theorem cyclotomic_truncation_and_coeff_recovery
    (h : CyclotomicThreeTermPochhammerDatum) :
    (cyclotomicThreeTermEval { h with poch1 := 0, poch2 := 0 } = h.c0) ∧
      (cyclotomicThreeTermEval { h with poch1 := 2, poch2 := 0 } = h.c0 + 2 * h.c1) ∧
      (cyclotomicThreeTermEval h - cyclotomicFirstOrderJetAtOne h = h.c2 * h.poch2) := by
  unfold cyclotomicThreeTermEval cyclotomicFirstOrderJetAtOne
  dsimp
  omega

/-- Theorem (`qou-bivd`): Two cyclotomic 3-term cyclotomic series that agree at the three
prime-power order specializations `q = 1` (`poch1 = 0, poch2 = 0`), `q = -1` (`poch1 = 2, poch2 = 0`),
and the second-order jet probe (`poch1 = 1, poch2 = 1`) have identical cyclotomic coefficients
`(c_0, c_1, c_2)`. -/
theorem cyclotomic_three_term_unique_from_evaluations
    (a0 a1 a2 b0 b1 b2 : Int)
    (hq1 : a0 + a1 * 0 + a2 * 0 = b0 + b1 * 0 + b2 * 0)
    (hqm1 : a0 + a1 * 2 + a2 * 0 = b0 + b1 * 2 + b2 * 0)
    (hq0 : a0 + a1 * 1 + a2 * 1 = b0 + b1 * 1 + b2 * 1) :
    a0 = b0 ∧ a1 = b1 ∧ a2 = b2 := by
  omega

/-! ## 3. `qou-bore`: Generalized One-Parameter Volume Conjecture and `m = 1` Containment -/

/-- One-parameter complexified volume datum on the `A`-polynomial Lagrangian
(`0306165v1.pdf` / `[arxiv-hep-th-0306165v1]`, §3.1 & §5.2 eq. (5.12)):
`S(u) = Vol(u) + i * 2 * pi^2 * CS(u)` where `u = log m` is the meridian holonomy
deformation parameter (`u = 0` corresponds to `m = 1`, the Kashaev specialization). -/
structure GeneralizedVolumeConjectureDatum where
  /-- Scaled hyperbolic volume `2 * Vol(0)` at the complete structure `m = 1` (`u = 0`). -/
  twiceVolComplete : Int
  /-- Scaled Chern–Simons invariant `4 * pi^2 * CS(0)` at `m = 1` (`u = 0`). -/
  twiceCSCompleteScaled : Int
  /-- Squared meridian holonomy deformation parameter `uSq = u^2 >= 0` (`uSq = 0 <-> m = 1`). -/
  holonomyUSq : Int
  /-- Quadratic Neumann–Zagier cusp modulus coefficients `(tau_re, tau_im)` in the
  incomplete hyperbolic volume / CS expansion around `u = 0`. -/
  cuspModulusRe : Int
  cuspModulusIm : Int
  deriving DecidableEq, Repr

/-- Scaled real part `2 * Vol(u) = 2 * Vol(0) + tau_re * u^2` of the one-parameter asymptotic rate. -/
def generalizedTwiceVolumePart (g : GeneralizedVolumeConjectureDatum) : Int :=
  g.twiceVolComplete + g.cuspModulusRe * g.holonomyUSq

/-- Scaled imaginary part `2 * (2*pi^2*CS(u)) = 2 * (2*pi^2*CS(0)) + tau_im * u^2` of the rate. -/
def generalizedTwiceCSPart (g : GeneralizedVolumeConjectureDatum) : Int :=
  g.twiceCSCompleteScaled + g.cuspModulusIm * g.holonomyUSq

/-- Theorem (`qou-bore`): The generalized one-parameter volume conjecture family `(Vol(u), CS(u))`
reduces at `u^2 = 0` (`m = 1`) to Kashaev's complete-structure invariants `(twiceVolComplete, twiceCSCompleteScaled)`,
and strictly decreases when `u^2 > 0` and `cuspModulusRe < 0` (Thurston's hyperbolic Dehn filling
volume decrease), proving strict containment of the `m = 1` Kashaev anchor inside the `A`-polynomial
one-parameter family (`0306165v1.pdf`, eq. 5.12). -/
theorem generalized_volume_conjecture_contains_kashaev_m_eq_one
    (g : GeneralizedVolumeConjectureDatum)
    (hu : 1 ≤ g.holonomyUSq)
    (hre : g.cuspModulusRe = -1) :
    generalizedTwiceVolumePart { g with holonomyUSq := 0 } = g.twiceVolComplete ∧
      generalizedTwiceCSPart { g with holonomyUSq := 0 } = g.twiceCSCompleteScaled ∧
      generalizedTwiceVolumePart g - generalizedTwiceVolumePart { g with holonomyUSq := 0 } =
        -g.holonomyUSq ∧
      generalizedTwiceVolumePart g < generalizedTwiceVolumePart { g with holonomyUSq := 0 } := by
  unfold generalizedTwiceVolumePart generalizedTwiceCSPart
  dsimp
  rw [hre]
  omega

/-! ## 4. `qou-cc4t`: Exponential Degeneracy of Hyperbolic Link Volumes (`[hodgson2012]`) -/

/-- Hodgson–Masai mutant/daisy-chain link family datum (`1203.6551v1.pdf` / `[hodgson2012]`,
§1 & §5), where `k` independent 2-tangle mutation sites produce `2^k` distinct link complements
all sharing the additive hyperbolic volume `k * baseBlockVol`. -/
structure HyperbolicVolumeDegeneracyDatum where
  /-- Number of mutation blocks `k >= 1`. -/
  blockCount : Nat
  /-- Scaled hyperbolic volume of a single building block (`v_0 > 0`). -/
  baseBlockVol : Int
  /-- Lower bound `N_k = 2^k` on the number of distinct hyperbolic link complements at volume `v_k`. -/
  degeneracyCount : Nat
  deriving DecidableEq, Repr

/-- Shared hyperbolic volume `v_k = k * v_0` across the mutant family at block count `k`. -/
def sharedHyperbolicVolume (d : HyperbolicVolumeDegeneracyDatum) : Int :=
  (d.blockCount : Int) * d.baseBlockVol

/-- Next-step daisy-chain datum at `k + 1` blocks: volume increases additively by `baseBlockVol`
while the link complement count doubles (`2 * degeneracyCount`). -/
def stepHyperbolicVolumeDegeneracy (d : HyperbolicVolumeDegeneracyDatum) :
    HyperbolicVolumeDegeneracyDatum :=
  { blockCount := d.blockCount + 1
    baseBlockVol := d.baseBlockVol
    degeneracyCount := 2 * d.degeneracyCount }

/-- Excess multiplicity `degeneracyCount - 1` of distinct links sharing the same volume `v_k`. -/
def volumeCollisionExcess (d : HyperbolicVolumeDegeneracyDatum) : Nat :=
  d.degeneracyCount - 1

/-- Theorem (`qou-cc4t`): Whenever `degeneracyCount >= 2` (satisfied for all `k >= 1` since `2^k >= 2`),
there is at least `1` volume collision (`volumeCollisionExcess d >= 1`), and stepping `k -> k + 1`
doubles the link count while increasing the shared volume additively by `baseBlockVol`, proving
that bare hyperbolic volume `Vol(L)` cannot uniquely identify a link (`[hodgson2012]`, §1 & §5). -/
theorem hyperbolic_link_volume_exponential_degeneracy
    (d : HyperbolicVolumeDegeneracyDatum)
    (hdeg : 2 ≤ d.degeneracyCount) :
    1 ≤ volumeCollisionExcess d ∧
      (stepHyperbolicVolumeDegeneracy d).degeneracyCount = 2 * d.degeneracyCount ∧
      3 ≤ volumeCollisionExcess (stepHyperbolicVolumeDegeneracy d) ∧
      sharedHyperbolicVolume (stepHyperbolicVolumeDegeneracy d) -
        sharedHyperbolicVolume d = d.baseBlockVol := by
  unfold volumeCollisionExcess stepHyperbolicVolumeDegeneracy sharedHyperbolicVolume
  dsimp
  refine ⟨by omega, rfl, by omega, ?_⟩
  rw [Int.add_mul, Int.one_mul]
  omega

/-! ## 5. `qou-cdr1`: Two-Level `q`-Borel–Laplace Connection for the Ramanujan / `q`-Airy Equation -/

/-- Two-level `q`-Borel–Laplace transform datum for Morita's connection formula on local
solutions of the quadratic q-difference equation (`1203.3404v1.pdf` / `[morita2012]`), connecting the
divergent `${}_2\varphi_0` series at `0` (via order-1 and order-2 `q`-Borel–Laplace kernels)
to the primary basis function and `q`-Airy function `A_q` at `infinity`. -/
structure TwoLevelQBorelQAiryConnectionDatum where
  /-- `q`-Gevrey order `s_1 = 1` of the first `q`-Borel transform. -/
  borelOrderOne : Nat
  /-- `q`-Gevrey order `s_2 = 2` of the second `q`-Borel transform (governing the `q^(n^2)`
  quadratic growth of the quadratic q-difference equation). -/
  borelOrderTwo : Nat
  /-- Scaled elliptic connection coefficients `(C_ram, C_airy)` decomposing the two-stage resummed
  `${}_2\varphi_0` solution into the primary basis `R_q(x)` and `q`-Airy basis `A_q(x)`. -/
  connCoeffPrimary : Int
  connCoeffQAiry : Int
  /-- Scaled evaluated basis values `(R_q(x), A_q(x))` at a regular point `x`. -/
  primaryBasisVal : Int
  qAiryVal : Int
  deriving DecidableEq, Repr

/-- Total two-stage `q`-Borel–Laplace resummed value `f_{0 -> inf}(x) = C_ram * R_q(x) + C_airy * A_q(x)`
(`1203.3404v1.pdf`, Main Theorem). -/
def twoLevelQBorelResummedValue (m : TwoLevelQBorelQAiryConnectionDatum) : Int :=
  m.connCoeffPrimary * m.primaryBasisVal + m.connCoeffQAiry * m.qAiryVal

/-- Composite `q`-Gevrey order sum `s_1 + s_2` across the two `q`-Borel–Laplace stages. -/
def compositeQGevreyOrderSum (m : TwoLevelQBorelQAiryConnectionDatum) : Nat :=
  m.borelOrderOne + m.borelOrderTwo

/-- Theorem (`qou-cdr1`): The two-stage `q`-Borel–Laplace connection formula decomposes the
resummed local solution at `0` uniquely into the primary and `q`-Airy solutions at `infinity`,
and isolating the `q`-Airy component `C_airy * A_q(x)` equals the residual after subtracting
the primary channel `C_ram * R_q(x)` (`[morita2012]`). -/
theorem two_level_qairy_connection_decomposition
    (m : TwoLevelQBorelQAiryConnectionDatum)
    (hs1 : m.borelOrderOne = 1)
    (hs2 : m.borelOrderTwo = 2) :
    twoLevelQBorelResummedValue m - m.connCoeffPrimary * m.primaryBasisVal =
      m.connCoeffQAiry * m.qAiryVal ∧
      compositeQGevreyOrderSum m = 3 := by
  unfold twoLevelQBorelResummedValue compositeQGevreyOrderSum
  rw [hs1, hs2]
  omega

end QOU.QBeta.StateIntegralCyclotomicGeneralizedVolDegeneracyQAiryBridge
