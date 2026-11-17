/-
Copyright (c) 2026 QOU Authors. All rights reserved.
Formalization for beans:
  - qou-dlet: Detangler backward-edge DAG acyclicity and under-complexity band verification
  - qou-t6rw: Finkelstein (0806.3105v3) nucleon doublet writhe-only degeneracy vs rotation-number lift
  - qou-vwu9: Eightfold Way 3-chapter architecture partition conservation and cumulative offset monotonicity
  - qou-wp6m: Atomic shell-filling 2n^2 capacity, half-shell Hund's rule maximum, and LP duality scaling
  - qou-ywsk: Bring-surface 181-block migration scoping gap (181 - 6 = 175) and detangler cap overflow
-/

namespace QOU.Eightfold.DetanglerDagFinkelsteinNucleonThreeChapterShellFillingAndBringsScoping

/-!
## 1. Bean `qou-dlet`: Detangler Backward-Edge DAG & Under-Complexity Distribution
Every inter-block `uses[]` edge `(srcPos, dstPos)` is backward when `dstPos < srcPos` in topological
document order, which strictly excludes 2-cycles and preserves section-band counts under
intra-section additions.
-/

/-- Difference `srcPos - dstPos` measuring the backward topological span of a `uses[]` edge. -/
def backwardEdgeSpan (srcPos dstPos : Int) : Int :=
  srcPos - dstPos

/-- Number of sections below the detangler lower threshold (`c < 3`) out of `totalSections`
    when `inBandCount` lie in `[3, 18]` and `overBandCount` lie above `18`. -/
def underComplexitySectionCount (totalSections inBandCount overBandCount : Nat) : Nat :=
  totalSections - inBandCount - overBandCount

/-- Detangler validation theorem for `qou-dlet`:
    (1) Any two composable backward edges `posC < posB` and `posB < posA` have strictly
        positive transitive backward span `backwardEdgeSpan posA posC >= 2`, ruling out cycles;
    (2) On the 21-section distribution (`0` over-band sections), moving 2 sections from `< 3`
        into `[3, 18]` shifts `underComplexitySectionCount` from `20` to `18`. -/
theorem detangler_backward_dag_and_under_complexity_shift
    (posA posB posC : Int) (hCB : posC < posB) (hBA : posB < posA) :
    2 ≤ backwardEdgeSpan posA posC ∧
    underComplexitySectionCount 21 1 0 = 20 ∧
    underComplexitySectionCount 21 3 0 = 18 := by
  dsimp [backwardEdgeSpan, underComplexitySectionCount]
  refine ⟨by omega, by decide, by decide⟩

/-!
## 2. Bean `qou-t6rw`: Cross-Check `0806.3105v3` (`[finkelstein2008]`) on the Nucleon Doublet
-- Ref: [finkelstein2008]
In Finkelstein's model, `6 * Q_e = -(w + r + 1)` and `6 * t_0 = -(r + 1)`.
-/

/-- Proton-minus-neutron electric charge difference `6 * (Q_p - Q_n)` in Finkelstein's
    `(w, r)` coordinates: `-(w_p + r_p + 1) - (-(w_n + r_n + 1)) = (w_n - w_p) + (r_n - r_p)`. -/
def finkelsteinSixChargeDiff (wProton rProton wNeutron rNeutron : Int) : Int :=
  (-(wProton + rProton + 1)) - (-(wNeutron + rNeutron + 1))

/-- Proton-minus-neutron hypercharge-half difference `6 * (t_0(p) - t_0(n)) = r_n - r_p`. -/
def finkelsteinSixT0Diff (rProton rNeutron : Int) : Int :=
  (-(rProton + 1)) - (-(rNeutron + 1))

/-- Decisive nucleon-doublet cross-check (`qou-t6rw` / `qou-nrty`):
    (1) At equal carrier writhe `wProton = wNeutron`, a writhe-only ansatz (`rProton = rNeutron`)
        gives `finkelsteinSixChargeDiff w r w r = 0` (failing to separate proton and neutron);
    (2) Introducing a rotation step `rProton = rNeutron - 6` at equal writhe separates the
        nucleon charges by `6 * (Q_p - Q_n) = 6` (`Q_p - Q_n = +1`), while shifting `6 * t_0`
        by `6`;
    (3) Conversely, keeping `t_0(p) = t_0(n)` (`rProton = rNeutron`) requires a writhe step
        `wProton = wNeutron - 6` to achieve `6 * (Q_p - Q_n) = 6`. -/
theorem finkelstein_nucleon_doublet_separation_dichotomy (wShared rNeutron : Int) :
    finkelsteinSixChargeDiff wShared rNeutron wShared rNeutron = 0 ∧
    finkelsteinSixChargeDiff wShared (rNeutron - 6) wShared rNeutron = 6 ∧
    finkelsteinSixT0Diff (rNeutron - 6) rNeutron = 6 ∧
    finkelsteinSixChargeDiff (wShared - 6) rNeutron wShared rNeutron = 6 ∧
    finkelsteinSixT0Diff rNeutron rNeutron = 0 := by
  dsimp [finkelsteinSixChargeDiff, finkelsteinSixT0Diff]
  refine ⟨by omega, by omega, by omega, by omega, by omega⟩

/-!
## 3. Bean `qou-vwu9`: Eightfold Way 3-Chapter Architecture Partition Invariants
-/

/-- Total block count across the 3-chapter Eightfold Way architecture. -/
def threeChapterTotalBlocks (c1 c2 c3 : Int) : Int :=
  c1 + c2 + c3

/-- Cumulative chapter boundary offsets `(c1, c1 + c2, c1 + c2 + c3)`. -/
def threeChapterBoundaryDeux (c1 c2 : Int) : Int :=
  c1 + c2

/-- Strict monotonicity of the 3-chapter cumulative boundaries and exact block conservation
    whenever each of the 3 chapters is non-empty (`0 < c1, 0 < c2, 0 < c3`). -/
theorem three_chapter_architecture_boundary_monotonicity
    (c1 c2 c3 : Int) (h1 : 0 < c1) (h2 : 0 < c2) (h3 : 0 < c3) :
    0 < c1 ∧
    c1 < threeChapterBoundaryDeux c1 c2 ∧
    threeChapterBoundaryDeux c1 c2 < threeChapterTotalBlocks c1 c2 c3 ∧
    threeChapterTotalBlocks c1 c2 c3 - threeChapterBoundaryDeux c1 c2 = c3 := by
  dsimp [threeChapterBoundaryDeux, threeChapterTotalBlocks]
  omega

/-!
## 4. Bean `qou-wp6m`: Atomic Shell-Filling `2n^2` Capacity, Hund's Rule & LP Duality Scaling
-- Ref: [bertsimas1997], [manuscript]
-/

/-- Spin-orbital capacity `2 * (2 * l + 1)` of an azimuthal subshell `l`. -/
def subshellSpinOrbitalCapacity (lAzimuthal : Nat) : Nat :=
  2 * (2 * lAzimuthal + 1)

/-- Closed-form principal shell capacity `2 * n^2`. -/
def principalShellCapacity (nPrincipal : Nat) : Nat :=
  2 * nPrincipal ^ 2

/-- Maximum number of singly-occupied orbitals under Hund's rule for `kElectrons` placed
    into `mOrbitals` degenerate spatial orbitals (`0 <= kElectrons <= 2 * mOrbitals`):
    `min(kElectrons, 2 * mOrbitals - kElectrons)`. -/
def hundMaxSinglyOccupied (mOrbitals kElectrons : Int) : Int :=
  if kElectrons ≤ mOrbitals then kElectrons else 2 * mOrbitals - kElectrons

/-- Homogeneous LP dual objective `Z * y0` for atomic number `Z` and chemical potential `y0`. -/
def shellFillingLpDualObjective (zAtomic y0Dual : Int) : Int :=
  zAtomic * y0Dual

/-- Complete verification for `qou-wp6m`:
    (1) Summing `subshellSpinOrbitalCapacity l` over `0 <= l < n` equals `principalShellCapacity n = 2n^2`
        for shells `n = 1, 2, 3, 4` (`2, 8, 18, 32`);
    (2) For any occupancy `0 <= k <= 2 * m`, `hundMaxSinglyOccupied m k <= m` with equality at
        half-filling `k = m`;
    (3) The LP dual objective `Z * y0` is additive in `Z`. -/
theorem shell_filling_capacity_hund_and_lp_duality
    (mOrbitals kElectrons z1 z2 y0Dual : Int)
    (hLow : 0 ≤ kElectrons) (hHigh : kElectrons ≤ 2 * mOrbitals) :
    subshellSpinOrbitalCapacity 0 = principalShellCapacity 1 ∧
    subshellSpinOrbitalCapacity 0 + subshellSpinOrbitalCapacity 1 = principalShellCapacity 2 ∧
    subshellSpinOrbitalCapacity 0 + subshellSpinOrbitalCapacity 1 + subshellSpinOrbitalCapacity 2 =
      principalShellCapacity 3 ∧
    subshellSpinOrbitalCapacity 0 + subshellSpinOrbitalCapacity 1 + subshellSpinOrbitalCapacity 2 +
      subshellSpinOrbitalCapacity 3 = principalShellCapacity 4 ∧
    0 ≤ hundMaxSinglyOccupied mOrbitals kElectrons ∧
    hundMaxSinglyOccupied mOrbitals kElectrons ≤ mOrbitals ∧
    hundMaxSinglyOccupied mOrbitals mOrbitals = mOrbitals ∧
    shellFillingLpDualObjective (z1 + z2) y0Dual =
      shellFillingLpDualObjective z1 y0Dual + shellFillingLpDualObjective z2 y0Dual := by
  dsimp [subshellSpinOrbitalCapacity, principalShellCapacity, hundMaxSinglyOccupied, shellFillingLpDualObjective]
  have hAdd : (z1 + z2) * y0Dual = z1 * y0Dual + z2 * y0Dual := Int.add_mul z1 z2 y0Dual
  refine ⟨by decide, by decide, by decide, by decide, ?_, ?_, ?_, hAdd⟩
  · split <;> omega
  · split <;> omega
  · split <;> omega

/-!
## 5. Bean `qou-ywsk`: Bring-Surface 181-Block Scoping Discrepancy
`folio/quantum-observable-universe/brings-surface/` holds `181` blocks. Moving a scoped subset
of `kSubset` blocks versus all `181` blocks differs by `181 - kSubset` blocks (`175` at `kSubset = 6`).
-/

/-- Scoping discrepancy `totalBringsBlocks - kSubset` between a whole-chapter move and a
    subset move. -/
def bringsMigrationScopingGap (totalBringsBlocks kSubset : Int) : Int :=
  totalBringsBlocks - kSubset

/-- Excess above the detangler section cap `18` if `movedBlocks` are placed into a single section. -/
def singleSectionDetanglerOverflow (movedBlocks : Int) : Int :=
  movedBlocks - 18

/-- Verification of the `qou-ywsk` scoping theorem:
    (1) At `totalBringsBlocks = 181` and `kSubset = 6`, the scoping discrepancy is `175` blocks;
    (2) Placing all `181` blocks into a single section overflows the `18`-block detangler cap
        by `163` blocks, whereas a `6`-block subset stays strictly below the cap (`6 - 18 = -12 < 0`). -/
theorem brings_surface_scoping_discrepancy_and_overflow :
    bringsMigrationScopingGap 181 6 = 175 ∧
    singleSectionDetanglerOverflow 181 = 163 ∧
    singleSectionDetanglerOverflow 6 = -12 := by
  decide

end QOU.Eightfold.DetanglerDagFinkelsteinNucleonThreeChapterShellFillingAndBringsScoping
