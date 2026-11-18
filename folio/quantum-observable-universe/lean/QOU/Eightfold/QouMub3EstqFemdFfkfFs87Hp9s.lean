/-
Copyright (c) 2026 Quantum Observable Universe. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Gulko, S.
-/

/-!
# Quantitative Source Cross-Checks: Few-Body Triplet Clusters, Character Support Bounds, Newton-Hodge Slopes, Plancherel Support Endpoints, and Cusp Lattice Norm Ratio

This module formalizes exact algebraic and arithmetic identities behind five source
verification tasks in the `qou-mub3` lane:

1. **`qou-estq` (`[klein-fewbody]` at `conj:binding-manybody-eq-jet-filtration`)**:
   Models the nuclear-EFT body-order expansion into two-body pair interactions and
   irreducible three-body triplet interactions, proving that the scaled pair and triplet
   cluster counts $3A(A-1)$ and $A(A-1)(A-2)$ evaluate to $(18, 6)$ for the triton ($A=3$)
   and $(36, 24)$ for helium-4 ($A=4$), while the three-body contribution vanishes for
   $A=2$ and activates at $A=3$.

2. **`qou-femd` (`[biane2000]` at `prop:q-plancherel-asymptotic-skeleton`)**:
   Models the disjoint-support character factorization threshold $2l \le n$ and the
   fourth-power concentration budget $K^4 \delta + K^4 q_{\text{inv}}$, proving exact
   linear scaling in the factorization defect $\delta$ and non-negativity of the support
   margin $n - 2l$ at the half-size boundary.

3. **`qou-ffkf` (`[freed2010]` at `QOU.Glossary.FIsocrystal`)**:
   Models the Newton-Hodge polygon height $r \cdot s$ of an isocrystal component of
   multiplicity $r$ and slope $s$, proving additivity of total polygon height across
   direct sums and vanishing of the internal slope spread when the two slopes coincide.

4. **`qou-fs87` (`[ivanov-olshanski2003]` at `prop:q-plancherel-asymptotic-skeleton`)**:
   Models the semicircle support kernel $4 - x^2$ of the limiting Young-diagram profile
   on $|x| \le 2$ and the cycle-length variance weight, proving that the kernel vanishes
   at both endpoints $x = \pm 2$, attains its maximum $4$ at $x = 0$, and satisfies
   exact even symmetry.

5. **`qou-hp9s` (`[dang-purcell]` at `prop:cusp-shape-bar-parity`)**:
   Models the quadratic norm $a^2 + 3b^2$ on the Eisenstein-type lattice $\mathbb{Z}[1, \omega]$
   (scaled by $4$ so $2\omega = 1 + i\sqrt{3}$ has coordinates $(1, 1)$ and the rectangular
   figure-eight cusp modulus $2\sqrt{3}i$ has scaled coordinates $(0, 4)$), proving that
   the norm-squared ratio between the rectangular cusp modulus and the unit tetrahedron
   shape parameter is $48 / 4 = 12$ and that bar conjugation $(a, b) \mapsto (a, -b)$
   preserves the quadratic norm.

-- Ref: [klein-fewbody]
-- Ref: [biane2000]
-- Ref: [freed2010]
-- Ref: [ivanov-olshanski2003]
-- Ref: [dang-purcell]
-/

namespace QOU.Eightfold.QouMub3EstqFemdFfkfFs87Hp9s

/-! ## 1. `qou-estq`: Few-Body Pair and Triplet Cluster Expansion -/

/-- Six times the number of two-body pairs $6 \binom{A}{2} = 3 A (A - 1)$ in an
$A$-nucleon system. -/
def pairClusterCountScaled6 (massNumber : Int) : Int :=
  3 * massNumber * (massNumber - 1)

/-- Six times the number of three-body triplets $6 \binom{A}{3} = A (A - 1) (A - 2)$
in an $A$-nucleon system. -/
def tripletClusterCountScaled6 (massNumber : Int) : Int :=
  massNumber * (massNumber - 1) * (massNumber - 2)

/-- Combined two-body and irreducible three-body binding energy scaled by $6$. -/
def manyBodyEnergyScaled6 (massNumber pairCoupling tripletCoupling : Int) : Int :=
  pairClusterCountScaled6 massNumber * pairCoupling +
    tripletClusterCountScaled6 massNumber * tripletCoupling

/-- `qou-estq`: The three-body cluster count vanishes at $A = 2$, equals $6$ (one triplet)
at $A = 3$ (triton), and equals $24$ (four triplets) at $A = 4$ (helium-4). -/
theorem few_body_triplet_activation_and_cluster_ratio
    (pairCoupling tripletCoupling : Int) :
    tripletClusterCountScaled6 2 = 0 ∧
    tripletClusterCountScaled6 3 = 6 ∧
    tripletClusterCountScaled6 4 = 24 ∧
    manyBodyEnergyScaled6 3 pairCoupling tripletCoupling -
      manyBodyEnergyScaled6 3 pairCoupling 0 = 6 * tripletCoupling := by
  refine ⟨by decide, by decide, by decide, ?_⟩
  dsimp [manyBodyEnergyScaled6, pairClusterCountScaled6, tripletClusterCountScaled6]
  omega

/-! ## 2. `qou-femd`: Disjoint-Support Factorization Margin and Fourth-Power Budget -/

/-- Support margin $n - 2l$ governing the regime $l \le n / 2$ where character
approximate factorization holds. -/
def supportHalfMargin (diagramSize cycleSupport : Int) : Int :=
  diagramSize - 2 * cycleSupport

/-- Fourth-power concentration budget $K^4 \delta + K^4 q_{\text{inv}}$ governing the
character deviation bound. -/
def concentrationFourthBudget (constFourth defectDelta invQ : Int) : Int :=
  constFourth * defectDelta + constFourth * invQ

/-- `qou-femd`: The support margin vanishes at the exact boundary $n = 2l$, and the
fourth-power concentration budget is additive in the factorization defect $\delta$. -/
theorem character_support_margin_and_budget_additivity
    (cycleSupport constFourth defectDelta invQ : Int) :
    supportHalfMargin (2 * cycleSupport) cycleSupport = 0 ∧
    supportHalfMargin (2 * cycleSupport + 2) cycleSupport = 2 ∧
    concentrationFourthBudget constFourth (defectDelta + 1) invQ -
      concentrationFourthBudget constFourth defectDelta invQ = constFourth := by
  refine ⟨?_, ?_, ?_⟩
  · dsimp [supportHalfMargin]
    omega
  · dsimp [supportHalfMargin]
    omega
  · dsimp [concentrationFourthBudget]
    rw [Int.mul_add, Int.mul_one]
    omega

/-! ## 3. `qou-ffkf`: Isocrystal Slope Polygon Height and Spread -/

/-- Total polygon height $r_1 s_1 + r_2 s_2$ of a two-component filtered object with
multiplicities $(r_1, r_2)$ and integer-scaled slopes $(s_1, s_2)$. -/
def twoSlopePolygonHeight (mult1 slope1 mult2 slope2 : Int) : Int :=
  mult1 * slope1 + mult2 * slope2

/-- Slope spread $s_2 - s_1$ measuring departure from a single-slope (isoclinic) object. -/
def twoSlopeSpread (slope1 slope2 : Int) : Int :=
  slope2 - slope1

/-- `qou-ffkf`: When both slopes equal $s$, the slope spread vanishes and the total
polygon height collapses to $(r_1 + r_2) s$. -/
theorem isoclinic_slope_collapse_and_height_sum (mult1 mult2 commonSlope : Int) :
    twoSlopeSpread commonSlope commonSlope = 0 ∧
    twoSlopePolygonHeight mult1 commonSlope mult2 commonSlope =
      (mult1 + mult2) * commonSlope := by
  refine ⟨?_, ?_⟩
  · dsimp [twoSlopeSpread]
    omega
  · dsimp [twoSlopePolygonHeight]
    rw [Int.add_mul]

/-! ## 4. `qou-fs87`: Semicircle Boundary Kernel and Even Symmetry -/

/-- Quadratic kernel $4 - x^2$ inside the limiting Young-diagram profile on $[-2, 2]$. -/
def boundaryQuadraticKernel (coordX : Int) : Int :=
  4 - coordX * coordX

/-- `qou-fs87`: The quadratic kernel $4 - x^2$ vanishes at both endpoints $x = \pm 2$,
attains $4$ at the origin $x = 0$, and is invariant under reflection $x \mapsto -x$. -/
theorem boundary_kernel_endpoints_and_reflection (coordX : Int) :
    boundaryQuadraticKernel 2 = 0 ∧
    boundaryQuadraticKernel (-2) = 0 ∧
    boundaryQuadraticKernel 0 = 4 ∧
    boundaryQuadraticKernel (-coordX) = boundaryQuadraticKernel coordX := by
  refine ⟨by decide, by decide, by decide, ?_⟩
  dsimp [boundaryQuadraticKernel]
  rw [Int.neg_mul_neg]

/-! ## 5. `qou-hp9s`: Cusp Lattice Norm Ratio and Bar-Conjugation Invariance -/

/-- Scaled quadratic norm $a^2 + 3b^2$ of $a + b i \sqrt{3}$ on the triangular/rectangular
cusp lattice. -/
def cuspLatticeNormScaled4 (realPart sqrt3Part : Int) : Int :=
  realPart * realPart + 3 * (sqrt3Part * sqrt3Part)

/-- `qou-hp9s`: In scaled coordinates where $2\omega = 1 + i\sqrt{3}$ has norm $4$ and the
figure-eight rectangular cusp modulus $4 i \sqrt{3}$ has norm $48$, the norm ratio is $12$
and bar conjugation $(a, b) \mapsto (a, -b)$ preserves the norm identically. -/
theorem cusp_lattice_norm_ratio_and_bar_invariance (realPart sqrt3Part : Int) :
    cuspLatticeNormScaled4 1 1 = 4 ∧
    cuspLatticeNormScaled4 0 4 = 48 ∧
    cuspLatticeNormScaled4 0 4 = 12 * cuspLatticeNormScaled4 1 1 ∧
    cuspLatticeNormScaled4 realPart (-sqrt3Part) =
      cuspLatticeNormScaled4 realPart sqrt3Part := by
  refine ⟨by decide, by decide, by decide, ?_⟩
  dsimp [cuspLatticeNormScaled4]
  rw [Int.neg_mul_neg]

end QOU.Eightfold.QouMub3EstqFemdFfkfFs87Hp9s
