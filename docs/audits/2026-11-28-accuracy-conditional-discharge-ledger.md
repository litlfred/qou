# Accuracy Table Conditional-to-Proved Audit & Reduction Ledger (`qou-vhm1`)

**Date:** 2026-11-28  
**Beans:** `qou-vhm1` (under Stability Epic `qou-s028` & Accuracy Epic `qou-myts`; related: `qou-a3ps`, `qou-l4t2`, `qou-aemx`, `qou-rpt1`, `qou-myxi`, `qou-dk7p`)  
**Owner Ruling Applied (2026-11-28):** Strictly proton-pinned $q_0 = q_{\mathrm{at}}(80) = 1.1099785827513808075916690956107688798744991218736\ldots$ (`q0Anchor = "proton"`, `physical_proton` in `computations/q0_anchor_manifest.json`); muon pin is **on hold** until rederivation and no muon-pin columns or comparisons are evaluated here.  
**File Fence:** `ACCURACY.md` and the 16 scorecard witnesses are untouched on this branch; post-merge regeneration runs `python3 scripts/generate-accuracy-scorecard.py --write`.

## 1. Artefacts Delivered

1. **Lean 4 — Electroweak Conditional Discharge (`0 sorry`, standard axioms only):**  
   [`folio/quantum-observable-universe/lean/QOU/StandardModel/ElectroweakConditionalDischarge.lean`](../../folio/quantum-observable-universe/lean/QOU/StandardModel/ElectroweakConditionalDischarge.lean)
   - Zero `[Field]` / `field_simp` markers (`scripts/base-ring-audit.py --check`: `0` new hits);
   - Zero transcendental/analytic tokens (`scripts/transcendental-boundary-audit.py --check`: `0` new hits);
   - Constructive `[CommRing R]` / `Rˣ` algebra + ordered-ring root uniqueness + proton-pinned `LawvereCut.Cut ℚ` interval certificate `ewNvProtonCut` (`width = 3 × 10⁻¹⁰`, relative width `0.00114 ppb`).
2. **Lean 4 — Electromagnetic `α_EM` & Rydberg `R_∞` Conditional Reduction (`0 sorry`, standard axioms only):**  
   [`folio/quantum-observable-universe/lean/QOU/StandardModel/AlphaEmConditionalReduction.lean`](../../folio/quantum-observable-universe/lean/QOU/StandardModel/AlphaEmConditionalReduction.lean)
   - Zero `[Field]` / `field_simp` markers (`0` new base-ring hits) and zero transcendental tokens (`0` new boundary hits);
   - Reconciles `BringMapChain` (`χ = -6`, `g = 4`, `b₁ = 8`) with `(2,4,5)` tiling `2/(3π)`, proves `[9]_q[10]_q` Clebsch–Gordan & bar-breaking over `[CommRing R]`, composes `EmPhotonJoinRules` (`-h²`) + `EmFormBLoopMeasure` (`μ_L = μ₁`) + `EmTwoLoopMeasureConnected`, certifies proton-pinned `emInvAlphaProtonCut` (`width = 3 × 10⁻¹⁰`, `0.00219 ppb`) and `rydbergFactorProtonCut`, and isolates `FormBMinimalKernelClass` + `FormCPinned`.
3. **80-dps Proton-Pinned Verification Probe & Witness (`0 float64`, `0` inline CODATA literals):**  
   [`computations/probes/accuracy_conditional_discharge_probe.py`](../../computations/probes/accuracy_conditional_discharge_probe.py) & [`computations/probes/accuracy-conditional-discharge-probe.witness.json`](../../computations/probes/accuracy-conditional-discharge-probe.witness.json)

---

## 2. Executive Before / After Hypothesis Ledger (Proton-Pinned $q_0$)

| Scorecard Observable (`ACCURACY.md`) | Proton-Pinned Prediction (`80-dps` trunc.) | Residual vs Experiment | Sub-Premises Before (`ACCURACY.md` / Legacy Carrier) | Discharged Unconditionally on `main` + This PR (`0 sorry`) | Remaining Open Mathematical / Physical Premises | Epistemic Status |
|---|---:|---:|---:|---:|---|---|
| **Tau/electron** $m_\tau / m_e$ (`Table 3.1a`) | `3477.442306` | `+61.06 ppm` (`+0.92σ` CODATA-22; `+0.44σ` PDG-24) | `5` (`S₃/ℤ₃` circulant trace/norm, `F⁵` stretch, `S₃` doublet degeneracy, monic quadratic resolvent, finite-$q$ `Q = 2/3` equipartition) | **`4` proved** (`S3CirculantKoideTraceIdentity.lean` + `LeptonMassGrowthBound.lean` $q^3$ bound; also proves bare `TL₃(q)` departs by $(q-q^{-1})^2 / [3(q^2+q^{-2})] > 0$) | **`1`**: `KoideCirculantEquipartitionHypothesis` ($2\|b(q)\|^2 = a(q)^2$ topological protection + lepton mass-map hierarchy `qou-se9w`) | **Conditional** |
| **Fine-structure** $\alpha_{\mathrm{EM}}^{-1}$ **Form B** (`Table 3.3a`) | `137.035999126951` | `-0.365 ppb` (`-2.38σ`) | `8` (`ArchimedeanLimit`, `BlochSuslinUniqueness`, `BringZeroModeBlochClass`, smooth Bring $g=4$, `[9][10]` tree algebra, 1-loop $-h^2$ skein, multi-loop measure $\mu_L$, phase-4 $\mu_1 = 1/(8\pi)$ + additive sum) | **`6` proved / eliminated** (`archimedeanLimit_Ioo` + `LiTwo_reflection'`; `blochWignerFiveTerm_blochD` + `blochSuslinRigidity_blochD`; `BringZeroModeBlochClass` bypassed via `em_bringZeroMode_from_finite_map`; `em_betti_period_eq_gauss_bonnet_iff_g4`; `em_formB_all_loop_reduction`; `emFormB_and_rydberg_proton_cut_certified`) | **`2`** (`FormBMinimalKernelClass`): (i) phase-4 measure `GermPeriodShare` + `HeatKernelLeadingCoeff` ($\mu_1 = 1/(8\pi)$), (ii) additive self-energy assembly ($\Delta_2 = 0$) | **Conditional** (all 3 legacy premise names discharged/bypassed) |
| **Fine-structure** $\alpha_{\mathrm{EM}}^{-1}$ **Form C** (`Table 3.3a`) | `137.035999173696` | `-0.024 ppb` (`-0.16σ`) | `6` (Bring $g=4$ & $(8\pi)^2$ measure, 4-topology $-h^2$, cubic root existence/uniqueness, $\Delta_{B_3}(q) \ge 0$ summability, connected cumulant $\kappa_2$, weight-3 $\Delta_{B_3}$ derivation & arm choice) | **`4` proved** (`twoLoop_blochB3_tiling_measure`, `exists_unique_pos_cubic_root`, `deltaB3_summable` / `deltaB3_nonneg`, `excess_lies_in_connected`, `formC_pinned_and_dilog_duplication_status`) | **`2`** (`FormCPinned` + `qou-aemx`): (i) single scalar equation `deltaB3 q = deltaReq q α` (deriving connected weight-3 period $\zeta(3)-\operatorname{Li}_3(q^{-2})$), (ii) non-residual arm selection | **Conditional** |
| **Rydberg** $R_\infty h c$ **Form B / Form C** (`Table 3.3a`) | `13.605693132756 eV` (B) / `13.605693123473 eV` (C) | `+0.725 ppb` (B) / `+0.043 ppb` (`+0.14σ`, C) | `8` (Form B) / `6` (Form C) + rational `α²/2` propagation | **`6` (B) / `4` (C) + `rydbergFactorProtonCut` proved** (`emFormB_and_rydberg_proton_cut_certified`; $m_e$ is Calibration Input 1) | **`2`** (strictly inherited from `FormBMinimalKernelClass` or `FormCPinned`; zero extra coupling assumptions) | **Conditional** |
| **Electroweak VEV** $v_{\mathrm{weak}} = N_v m_p$ (`Table 3.4a`) | `246.219643562414 GeV` ($N_v = 262.418168819231$) | `-29.37 ppb` (`-0.11σ`) | `9` (`EwVevReducedHypotheses`: smooth Bring $g=4$, Seifert zero-mode $1/\pi$, `[2][4][6][8]` algebra & bar-parity, $k=1$ dressing, `SU(2)_L` $b_0 = -19/6$ sign $s=-1$, $(q+1)^2\hbar_q^2 = h^2$, $\sin^2\theta_W(0)=3/8$, cubic uniqueness & interval cut, self-consistency $\alpha_v N_v = 1$) | **`6` proved** (`bringMap_connected_and_euler`, `ew_em_genusAffine_unique_domain`, `ew_carrier_product_clebsch_gordan`, `twoEwTreeU_bar_and_classical`, `sixOneLoopB0_su2_neg_and_abelian_pos`, `cleared_anomalyFree_neutral_forces_three_eighths`, `ewNvProton_cut_certified`, `minimalEwBridge_discharges_legacy_classes`) | **`1` bundled physical bridge** (`MinimalElectroweakVevBridgeClass`, `3` fields: `Nv_pos`, `duality_self_consistency`, `su2_vev_assembly`, encapsulating open discrete choices `qou-rpt1` / `qou-myxi`) | **Conditional** |

---

## 3. Detailed Theorem-by-Theorem Audit

### 3.1 Electroweak Weak Scale (`ElectroweakConditionalDischarge.lean`)

1. **Finite Regular-Map Discharge of Bring Genus (`BringMapChain` $\implies g = 4, \chi = -6, b_1 = 8$):**
   - `bringMap_connected_and_euler` & `bringMap_genus_eq_four_iff`: Directly from the `120`-dart `S₅` regular map `(σ, α)` (`V = 30, E = 60, F = 24`), `bringMapEuler = -6` and `orbits σ α = 1`, forcing `g = 4` and `bringMapBettiOne = 8` by finite group theory alone (no Radó triangulation or Riemann–Hurwitz input).
   - `ewSeifertSum_eq_neg_bringMapEuler` & `ew_zero_mode_and_habiro_period_cancellation`: Proves `g_W + g_Z + g_H = 1 + 2 + 3 = 6 = -bringMapEuler` and `(12 p) * p⁻¹ = 12` over any `[CommRing R]` with unit `p : Rˣ`.
   - `ew_em_genusAffine_unique_domain`: Upgrades `ElectroweakVevGaps.genusAffine_unique` from `[Field K]` to `[CommRing R] [IsDomain R] [CharZero R]`, proving `a = 0 ∧ b = 4` is the unique affine carrier-genus rule matching both EM (`8`) and EW (`12`) numerators.
2. **Constructive `[CommRing R]` / `Rˣ` Quantum-Integer Tree Algebra:**
   - `qBalU_telescoping`, `qBalU_bar`, `qBalU_one`: Division-free balanced quantum integers over any `[CommRing R]` with unit `q : Rˣ`.
   - `qBalU_ew_chebyshev_factors` & `ew_carrier_product_clebsch_gordan`: Exact Chebyshev factorizations in `x = q + q⁻¹` and the nine-channel `SU(2)_q` Clebsch–Gordan identity
     $$[2]_q[4]_q[6]_q[8]_q = [17]_q + 3[15]_q + 5[13]_q + 7[11]_q + 8[9]_q + 8[7]_q + 7[5]_q + 5[3]_q + 2[1]_q$$
     (`384 = 2 × 192` at `q = 1`), plus `twoEwTreeU_bar_and_classical` (`twoEwTreeU q⁻¹ * q² = twoEwTreeU q`).
     *(Note: A naive transcription $q[16]_q[17]_q - [4]_q + 1/[2]_q$ evaluates to $268.5 \neq 192$ at $q = 1$; the true tree term in `ElectroweakBringSchwingerBridge.lean` is $N_v^{\mathrm{tree}}(q) = \tfrac{1}{2} q [2]_q [4]_q [6]_q [8]_q$, whose exact Clebsch–Gordan expansion is proved above.)*
3. **Signed Bar-Odd Loop Step, Constant Measure & `SU(2)_L` Beta Sign:**
   - `barOdd_join_habiro_bridge_and_const_measure`: Links `EmPhotonJoinRules.barOdd_eq` (`-h²`) and `EmFormBLoopMeasure.formB_measure_const` (`μ_L = μ₁`) with `(q - q⁻¹)² = (q + 1)²(1 - q⁻¹)²` over `[CommRing R]`.
   - `sixOneLoopB0_su2_neg_and_abelian_pos`: Proves `6 b₀(SU(2)_L) = -19 < 0` vs abelian `6 b₀ > 0` over any strict ordered commutative ring without division.
4. **Constructive Anomaly-Free Hypercharge & $\sin^2\theta_W(0) = 3/8$:**
   - `cleared_anomalyFree_neutral_forces_three_eighths`: Over `[CommRing R] [IsDomain R] [CharZero R]`, cleared perturbative anomaly cancellation factors as $-18 Y_Q (Y_u + 4 Y_Q)(Y_u - 2 Y_Q) = 0$, and one neutral lepton forces $Y_Q^2 = 1$ ($y_Q = \pm 1/6$) and $8\,\mathrm{Tr}((6 T_3)^2) = 3\,\mathrm{Tr}((6 Q)^2)$ ($576 = 576 \iff \sin^2\theta_W(0) = 3/8$), with zero `[Field]` or `field_simp`.
5. **Proton-Pinned `LawvereCut.Cut ℚ` Rational Interval Certificate (`0.00114 ppb` width):**
   - `ewClearedVevCubic_unique_and_bracket` & `ewNvProton_cut_certified`: Certifies over `ℚ` that for every $(T, H, cH)$ in the proton-pinned enclosure $T \in [262418473706849/10^{12},\, 262418473706851/10^{12}]$, $H \in [312543141/3906250000,\, 80011044097/10^{12}]$, $cH \in [392741669/(5\times 10^{11}),\, 785483339/10^{12}]$, the unique root $N_v \ge 200$ satisfies
     $$N_v(q_0) \in \left[\frac{2624181688191}{10^{10}},\, \frac{2624181688194}{10^{10}}\right], \qquad \Delta N_v = 3 \times 10^{-10} \;\;(\text{rel. } 1.14 \times 10^{-12}),$$
     $25{,}700\times$ tighter than the `-29.37 ppb` observational comparison residual.
6. **What Remains Open on $v_{\mathrm{weak}}$ (`MinimalElectroweakVevBridgeClass`):**
   - `minimalEwBridge_discharges_legacy_classes` proves that `MinimalElectroweakVevBridgeClass` implies `EwVevReducedHypotheses`, `EwVevHypotheses`, and `ElectroweakVevFixedPointClass` (with consistency witness `trivialModelMinimalEwBridge`).
   - Why $v_{\mathrm{weak}}$ remains **Conditional** (not `Derived`): As proved in `ElectroweakVevGaps.lean` (`su2_coupling_not_selfConsistent` and `treeK_strictMono`), the $k = 1$ exponent on $[2]_q/2$, the bar-breaking factor $q$, the per-carrier zero-mode counting rule, and the identification of the loop coupling with $\alpha_v = m_p/v$ rather than $\alpha_2 > 1/30$ remain unproved physical/categorical identifications (`qou-rpt1`, `qou-myxi`).

### 3.2 Electromagnetic $\alpha_{\mathrm{EM}}$ & Rydberg $R_\infty$ (`AlphaEmConditionalReduction.lean`)

1. **Elimination of the Three Legacy Form-B Scorecard Premises (`ArchimedeanLimit`, `BlochSuslinUniqueness`, `BringZeroModeBlochClass`):**
   - `ArchimedeanLimit x` is proved on `(0,1)` (`DilogPartAConvergence.archimedeanLimit_Ioo`) and at `0` (`archimedeanLimit_zero`), alongside `LiTwo_duplication` and `LiTwo_reflection'` (`qou-a3ps`).
   - `BlochSuslinUniqueness` in its corrected complex form is proved for `blochD` (`blochWignerFiveTerm_blochD`, `blochSuslinRigidity_blochD`).
   - `BringZeroModeBlochClass` (expected false by period transcendence) is **not needed**: `em_bringZeroMode_from_finite_map` proves `(bringMapBettiOne : ℝ) / bringSurfaceArea = bringZeroModeValue` (`8 / (12\pi) = 2/(3\pi)`) directly from `BringMapChain` + `(2,4,5)` angle defect, and `em_betti_period_eq_gauss_bonnet_iff_g4` proves the Betti/Gauss–Bonnet coincidence `2g = 8 ↔ g = 4` over `[CommRing R] [IsDomain R] [CharZero R]`.
2. **All-Loop Form-B Skein & Measure Reduction (`em_formB_all_loop_reduction`):**
   - Composes `EmPhotonJoinRules.barOdd_eq` (`-h²` at any two fermion-loop positions) with `EmFormBLoopMeasure.formB_coeff_of_recursion` to fix $c_L = [2]_q \mu_1 (-h^2)^L$ for all $L \ge 0$ and $\mu_L = \mu_1$ (`connected (formBMeasure μ₁) = μ₁ - μ₁²`), alongside the nine-channel Clebsch–Gordan identity $[9]_q[10]_q = \sum_{m=1}^9 [2m]_q$ (`em_carrier_product_clebsch_gordan`).
3. **Proton-Pinned `LawvereCut.Cut ℚ` Certificate for Form-B $\alpha_{\mathrm{EM}}^{-1}$ & $R_\infty / m_e$:**
   - `emFormB_and_rydberg_proton_cut_certified` proves over `ℚ` that for every $(T_0, H, h^2 H)$ in the proton-pinned enclosure $T_0 \in [137035415444371/10^{12},\, 34258853861093/(2.5\times 10^{11})]$, $H \in [312543141/3906250000,\, 80011044097/10^{12}]$, $h^2 H \in [1748489689/(5\times 10^{11}),\, 3496979379/10^{12}]$, every root $A \ge 100$ of the cleared Form-B cubic lies inside
     $$\alpha_{\mathrm{EM}}^{-1}(q_0) \in \left[\frac{1370359991268}{10^{10}},\, \frac{1370359991271}{10^{10}}\right], \qquad \frac{R_\infty}{m_e} = \frac{1}{2A^2} \in \texttt{rydbergFactorProtonCut}.$$
4. **Minimal Open Kernels (`FormBMinimalKernelClass` & `FormCPinned`):**
   - Form B (`formBMinimalKernel_imp_twoLoopZeroFixedPoint`, `trivialModelFormB`): Isolated to `GermPeriodShare μ₁ a₀` + `HeatKernelLeadingCoeff a₀` ($\mu_1 = 1/(8\pi)$) and additive self-energy assembly ($\Delta_2 = 0$).
   - Form C (`formC_pinned_and_dilog_duplication_status`): Isolated via `FormCPinned q α ↔ deltaB3 q = deltaReq q α` to deriving the connected weight-3 period $\Delta_{B_3}(q) = \zeta(3) - \operatorname{Li}_3(q^{-2})$ and canonical arm selection (`qou-aemx`).
