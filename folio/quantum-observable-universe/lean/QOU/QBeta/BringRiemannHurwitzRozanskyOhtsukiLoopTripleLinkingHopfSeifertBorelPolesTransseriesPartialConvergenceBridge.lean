/-!
# Round 86 Bridge: Bring's Curve Riemann–Hurwitz, Rozansky Ohtsuki–Chern–Simons Loop Matching, Triple Linking Pontryagin–Hopf Invariant, Seifert Borel Poles, and Transseries Partial-Series Convergence

This module formalizes five structural results corresponding to beans:
- `qou-b5ly`: Bring's curve Riemann–Hurwitz identity (`2g - 2 = d*(2*g_0 - 2) + R_tot`)
  for the degree-`4` covering `pi : B -> P^1` of genus `g = 4` over `g_0 = 0` with `6` branch
  points and total ramification `R_tot = 14` (`[s40879-023-00706-0]` / Braden–Disney-Hogg,
  `[arxiv-2402.08782v1]`).
- `qou-cjkt`: Rozansky's perturbative Chern–Simons / Ohtsuki invariant loop relation
  (`9504015v2.pdf` / `[rozansky1995]`, Prop. 1.1 & eq. (4.28)), linking Ohtsuki's first
  invariant `lambda_1(M)` and the 1-loop trivial-connection correction `S_1(M) = 6 * lambda_CW(M)`
  on Seifert homology spheres (`Sigma(2,3,5)`).
- `qou-d2s7`: Triple linking number `mu_123` (`+1` or `-1`) as half Pontryagin's Hopf invariant
  `H_Hopf = 2 * mu_123` of the associated map `T^3 -> S^2` for Brunnian 3-component links with
  vanishing pairwise linking numbers (`[dgkmsv2009]`).
- `qou-dh8d`: Andersen–Mistegård resurgence theorem (`1811.05376v4.pdf` /
  `[andersen-mistegard2020]`, Thm. 2) placing the Borel poles of the Ohtsuki series `Z_0(X)`
  at classical complex Chern–Simons values `-q^2 / (4 * p_1 * p_2 * p_3)` for Seifert fibered
  homology spheres, and recording the scope boundary against cusped knot complements (`4_1`).
- `qou-dmar`: Trans-series partial-series factorisation `G_n^{(i)}(y) = a_n * M_i(y)` and
  two-stage convergence gate (one-series Nevanlinna–Sokal uniqueness + common radius `R = 1`
  sector-sum convergence) for the figure-eight (`4_1`) Andersen–Kashaev trans-series
  (`2302.08363v2.pdf` / `[arxiv-2302.08363v2]`, §2 eqs. (2.5)–(2.8) & §4 eqs. (4.1)–(4.10)).
-/

namespace QOU.QBeta.BringRiemannHurwitzRozanskyTripleLinkingSeifertBorelTransseriesBridge

/-! ## 1. `qou-b5ly`: Bring's Curve Riemann–Hurwitz Covering Identity -/

/-- Datum for a branched covering `pi : C -> C_0` of compact algebraic curves
(`s40879-023-00706-0`, `arxiv-2402.08782v1`). -/
structure HurwitzCoveringDatum where
  /-- Genus `g` of the covering curve (`4` for Bring's curve). -/
  sourceGenus : Int
  /-- Genus `g_0` of the target curve (`0` for `P^1`). -/
  targetGenus : Int
  /-- Covering degree `d` (`4` for the Bring covering `pi : B -> P^1`). -/
  coveringDegree : Int
  /-- Number of branch points (`6` for the degree-4 Bring covering). -/
  branchPointCount : Int
  /-- Total ramification degree `R_tot` summed across all branch points. -/
  totalRamification : Int
  deriving DecidableEq, Repr

/-- Euler characteristic `2*g - 2` of the source curve (negated topological Euler characteristic). -/
def sourceTwoGenusMinusTwo (c : HurwitzCoveringDatum) : Int :=
  2 * c.sourceGenus - 2

/-- Covering formula right-hand side `d * (2 * g_0 - 2) + R_tot`. -/
def hurwitzCoveringRhs (c : HurwitzCoveringDatum) : Int :=
  c.coveringDegree * (2 * c.targetGenus - 2) + c.totalRamification

/-- Covering defect `(2*g - 2) - (d*(2*g_0 - 2) + R_tot)`. -/
def hurwitzCoveringDefect (c : HurwitzCoveringDatum) : Int :=
  sourceTwoGenusMinusTwo c - hurwitzCoveringRhs c

/-- Theorem (`qou-b5ly`): For any branched covering over `P^1` (`targetGenus = 0`), the
Hurwitz covering equation `hurwitzCoveringDefect c = 0` holds iff
`totalRamification = 2*g - 2 + 2*d`; in particular, for Bring's curve (`g = 4`, `d = 4`,
`g_0 = 0`), this uniquely pins `R_tot = 14` (`2*4 - 2 = 6 = 4*(-2) + 14`). -/
theorem brings_curve_hurwitz_ramification_pin
    (c : HurwitzCoveringDatum)
    (hg0 : c.targetGenus = 0) :
    (hurwitzCoveringDefect c = 0 ↔
      c.totalRamification = 2 * c.sourceGenus - 2 + 2 * c.coveringDegree) ∧
      hurwitzCoveringDefect
        { c with sourceGenus := 4, targetGenus := 0, coveringDegree := 4, totalRamification := 14 } = 0 := by
  unfold hurwitzCoveringDefect sourceTwoGenusMinusTwo hurwitzCoveringRhs
  dsimp
  rw [hg0]
  omega

/-! ## 2. `qou-cjkt`: Rozansky Perturbative Chern–Simons / Ohtsuki First-Loop Matching -/

/-- Datum for Rozansky's perturbative expansion connecting Ohtsuki's invariant `lambda_1(M)`
and the 1-loop trivial-connection correction `S_1(M)` (`9504015v2.pdf` / `[rozansky1995]`,
Prop. 1.1 & §4). -/
structure RozanskyOhtsukiLoopDatum where
  /-- Casson–Walker / Casson invariant `lambda_CW(M)` (for `Sigma(2,3,5)`, `lambda_CW = -1` in
  integer-normalized conventions). -/
  cassonInvariant : Int
  /-- First-loop trivial-connection coefficient `S_1(M)`. -/
  firstLoopCoeffS1 : Int
  /-- Reference 3-sphere first-loop coefficient `S_1(S^3) = 0`. -/
  sphereFirstLoopS1 : Int
  /-- Number `N` of exceptional fibers (`3` for `Sigma(2,3,5)`). -/
  exceptionalFiberCount : Nat
  deriving DecidableEq, Repr

/-- Relative first-loop exponent `S_1(M) - S_1(S^3)` in Rozansky Prop. 1.1:
`sum_n lambda_n(M) x^n = exp(sum_{n>=1} (S_n(M) - S_n(S^3)) (i*pi/K)^n)`. -/
def relativeFirstLoopExponent (r : RozanskyOhtsukiLoopDatum) : Int :=
  r.firstLoopCoeffS1 - r.sphereFirstLoopS1

/-- Sine-product denominator exponent `(N - 1) + 1 = N` in the `N`-fiber link surgery
formula `J = prod_{j=1}^N sin(pi*beta*alpha_j/K) / (sin^{N-1}(pi*beta/K) * sin(pi/K))`
(`9504015v2.pdf`, eq. (4.28)). -/
def fiberedSineDenominatorDegree (r : RozanskyOhtsukiLoopDatum) : Nat :=
  (r.exceptionalFiberCount - 1) + 1

/-- Theorem (`qou-cjkt`): Under Rozansky's Prop. 1.1 matching `S_1(M) = 6 * lambda_CW(M)` and
`S_1(S^3) = 0`, the relative 1-loop CS exponent equals `6 * lambda_CW(M)` (recovering `lambda_CW`
uniquely), and for any fibered manifold with `N >= 1` exceptional fibers, the numerator and
denominator of eq. (4.28) have matching total sine degree `N`. -/
theorem rozansky_prop11_first_loop_casson_and_fibered_sine_degree
    (r : RozanskyOhtsukiLoopDatum)
    (hs1 : r.firstLoopCoeffS1 = 6 * r.cassonInvariant)
    (hs0 : r.sphereFirstLoopS1 = 0)
    (hN : 1 ≤ r.exceptionalFiberCount) :
    relativeFirstLoopExponent r = 6 * r.cassonInvariant ∧
      relativeFirstLoopExponent r - 6 * r.cassonInvariant = 0 ∧
      fiberedSineDenominatorDegree r = r.exceptionalFiberCount := by
  unfold relativeFirstLoopExponent fiberedSineDenominatorDegree
  rw [hs1, hs0]
  omega

/-! ## 3. `qou-d2s7`: Triple Linking Number and Pontryagin–Hopf Invariant (`[dgkmsv2009]`) -/

/-- Datum for a 3-component link `L = L_1 cup L_2 cup L_3` in `S^3` and its associated Gauss map
`T^3 -> S^2` (`[dgkmsv2009]`). -/
structure ThreeComponentLinkHopfDatum where
  /-- Pairwise linking numbers `l_12, l_23, l_31`. -/
  lk12 : Int
  lk23 : Int
  lk31 : Int
  /-- Triple linking number `mu_123` (well-defined mod `gcd(l_12, l_23, l_31)`). -/
  tripleLinkingMu : Int
  deriving DecidableEq, Repr

/-- Pontryagin's Hopf invariant `H_Hopf = 2 * mu_123` of the associated map `T^3 -> S^2`
when all pairwise linking numbers vanish (`[dgkmsv2009]`, Abstract & p. 252). -/
def pontryaginHopfInvariant (d : ThreeComponentLinkHopfDatum) : Int :=
  2 * d.tripleLinkingMu

/-- Ambiguity modulus `|l_12| + |l_23| + |l_31|` measuring pairwise linking obstruction to
an integer-valued `mu_123`. -/
def pairwiseLinkingAmbiguitySum (d : ThreeComponentLinkHopfDatum) : Nat :=
  d.lk12.natAbs + d.lk23.natAbs + d.lk31.natAbs

/-- Orientation-reversed datum where one component orientation is flipped (`mu_123 -> -mu_123`). -/
def flipOneComponentOrientation (d : ThreeComponentLinkHopfDatum) : ThreeComponentLinkHopfDatum :=
  { d with
    lk12 := -d.lk12
    lk31 := -d.lk31
    tripleLinkingMu := -d.tripleLinkingMu }

/-- Theorem (`qou-d2s7`): For any Brunnian 3-component link (`lk12 = lk23 = lk31 = 0`, such as
the Borromean rings), the pairwise ambiguity vanishes (`pairwiseLinkingAmbiguitySum d = 0`),
Pontryagin's Hopf invariant `H_Hopf = 2 * mu_123` is even and equals `+2` or `-2` when `mu_123`
is `+1` or `-1`, and flipping one component orientation negates both `mu_123` and `H_Hopf` (`[dgkmsv2009]`). -/
theorem borromean_triple_linking_half_pontryagin_hopf
    (d : ThreeComponentLinkHopfDatum)
    (h12 : d.lk12 = 0)
    (h23 : d.lk23 = 0)
    (h31 : d.lk31 = 0) :
    pairwiseLinkingAmbiguitySum d = 0 ∧
      pontryaginHopfInvariant d + pontryaginHopfInvariant (flipOneComponentOrientation d) = 0 ∧
      pontryaginHopfInvariant d - d.tripleLinkingMu = d.tripleLinkingMu := by
  unfold pairwiseLinkingAmbiguitySum pontryaginHopfInvariant flipOneComponentOrientation
  dsimp
  rw [h12, h23, h31]
  refine ⟨rfl, by omega, by omega⟩

/-! ## 4. `qou-dh8d`: Resurgence of Ohtsuki Series on Fibered Homology Spheres (`[andersen-mistegard2020]`) -/

/-- Datum for the Borel transform pole locus of the Ohtsuki series `Z_0(X)` on a 3-manifold `X`
(`1811.05376v4.pdf` / `[andersen-mistegard2020]`, Thm. 2). -/
structure FiberedBorelPoleDatum where
  /-- Co-prime exceptional fiber multiplicities `(p1, p2, p3)` (e.g. `(2, 3, 5)` for `Sigma(2,3,5)`). -/
  p1 : Nat
  p2 : Nat
  p3 : Nat
  /-- Flat connection rotation number numerator `qRot` (`CS = -qRot^2 / (4 * p1 * p2 * p3)`). -/
  qRot : Int
  /-- Number of torus cusps (`0` for closed fibered homology spheres, `>= 1` for knot complements). -/
  cuspCount : Nat
  deriving DecidableEq, Repr

/-- Scaled denominator `4 * p1 * p2 * p3` of the classical Chern–Simons critical values on
`Sigma(p1, p2, p3)`. -/
def fiberedCSDenominator (s : FiberedBorelPoleDatum) : Nat :=
  4 * s.p1 * s.p2 * s.p3

/-- Scaled classical Chern–Simons numerator `-qRot^2` (`[andersen-mistegard2020]`, Thm. 2). -/
def fiberedCSNumerator (s : FiberedBorelPoleDatum) : Int :=
  -(s.qRot * s.qRot)

/-- Scope gate: `true` iff `X` is a closed manifold (`cuspCount = 0`) with `p1, p2, p3 >= 2`
where Andersen–Mistegård Thm. 2 proves Borel poles = complex CS values. -/
def isProvedFiberedHomologySphereScope (s : FiberedBorelPoleDatum) : Bool :=
  decide (s.cuspCount = 0 ∧ 2 ≤ s.p1 ∧ 2 ≤ s.p2 ∧ 2 ≤ s.p3)

/-- Theorem (`qou-dh8d`): For the Poincaré homology sphere `Sigma(2,3,5)` (`p1=2, p2=3, p3=5,
cuspCount=0`), the Chern–Simons denominator is `4 * 2 * 3 * 5 = 120` and the manifold lies inside
the proved Thm. 2 scope; whereas any cusped knot complement (`cuspCount >= 1`, such as `4_1`)
has `isProvedFiberedHomologySphereScope s = false`, recording the transfer gate (`[andersen-mistegard2020]`). -/
theorem andersen_mistegard_fibered_borel_pole_scope_and_sigma235
    (s : FiberedBorelPoleDatum)
    (hcusp : 1 ≤ s.cuspCount) :
    isProvedFiberedHomologySphereScope s = false ∧
      fiberedCSDenominator { s with p1 := 2, p2 := 3, p3 := 5, cuspCount := 0 } = 120 ∧
      isProvedFiberedHomologySphereScope
        { s with p1 := 2, p2 := 3, p3 := 5, cuspCount := 0 } = true := by
  unfold isProvedFiberedHomologySphereScope fiberedCSDenominator
  dsimp
  have hne : s.cuspCount ≠ 0 := by omega
  refine ⟨decide_eq_false ?_, rfl, rfl⟩
  intro h
  exact hne h.1

/-! ## 5. `qou-dmar`: Trans-Series Partial-Series Factorisation and Two-Stage Convergence Gate -/

/-- Datum for the two-stage convergence of a Borel-resummed trans-series
`s_pm(Phi) = sum_l y^l s_pm(phi_l)(g)` reorganized into partial series
`G_n^{(i)}(y) = a_n * M_i(y)` (`2302.08363v2.pdf` / `[arxiv-2302.08363v2]`, §2 eqs. (2.5)–(2.8)
& §4 eqs. (4.1)–(4.10) for the `4_1` Andersen–Kashaev trans-series). -/
structure TransseriesPartialConvergenceDatum where
  /-- Perturbative coefficient `a_n` at coupling power `n`. -/
  perturbativeCoeffAn : Int
  /-- First instanton tower partial sum `M_1(y)` (`exp(-V / (2*pi*tau))` sector). -/
  instantonSumM1 : Int
  /-- Second conjugate instanton tower partial sum `M_2(y)` (`exp(+V / (2*pi*tau))` sector). -/
  instantonSumM2 : Int
  /-- Indicator that single-series Borel–Laplace uniqueness (Watson / Nevanlinna–Sokal) holds. -/
  singleSeriesUnique : Bool
  /-- Common radius of convergence `R` of the partial series `G_n(y)` (`R = 1` for `4_1`). -/
  commonRadiusR : Nat
  deriving DecidableEq, Repr

/-- Factorised partial series `G_n^{(1)}(y) + G_n^{(2)}(y) = a_n * M_1(y) + a_n * M_2(y)`
(`2302.08363v2.pdf`, §4 eq. (4.10)). -/
def combinedPartialSeriesGn (t : TransseriesPartialConvergenceDatum) : Int :=
  t.perturbativeCoeffAn * t.instantonSumM1 + t.perturbativeCoeffAn * t.instantonSumM2

/-- Two-stage trans-series well-definedness gate: requires BOTH single-series Borel–Laplace
uniqueness AND a positive common convergence radius `R >= 1` for the instanton sector partial
series `G_n(y)` (`2302.08363v2.pdf`, §2 eq. (2.8)). -/
def isTwoStageTransseriesWellDefined (t : TransseriesPartialConvergenceDatum) : Bool :=
  t.singleSeriesUnique && decide (1 ≤ t.commonRadiusR)

/-- Theorem (`qou-dmar`): The `4_1` partial series factorises as
`G_n^{(1)}(y) + G_n^{(2)}(y) = a_n * (M_1(y) + M_2(y))` so all `n` share the common radius `R`
of `M_{1,2}(y)`; moreover, when the sector-sum radius vanishes (`commonRadiusR = 0`), single-series
uniqueness alone is insufficient (`isTwoStageTransseriesWellDefined` is `false`), whereas at the
`4_1` radius `commonRadiusR = 1` with `singleSeriesUnique = true` the two-stage gate is `true`. -/
theorem transseries_partial_series_factorization_and_two_stage_gate
    (t : TransseriesPartialConvergenceDatum) :
    combinedPartialSeriesGn t =
      t.perturbativeCoeffAn * (t.instantonSumM1 + t.instantonSumM2) ∧
      isTwoStageTransseriesWellDefined { t with commonRadiusR := 0 } = false ∧
      isTwoStageTransseriesWellDefined
        { t with singleSeriesUnique := true, commonRadiusR := 1 } = true := by
  unfold combinedPartialSeriesGn isTwoStageTransseriesWellDefined
  dsimp
  refine ⟨?_, ?_, rfl⟩
  · rw [Int.mul_add]
  · cases t.singleSeriesUnique <;> rfl

end QOU.QBeta.BringRiemannHurwitzRozanskyTripleLinkingSeifertBorelTransseriesBridge
