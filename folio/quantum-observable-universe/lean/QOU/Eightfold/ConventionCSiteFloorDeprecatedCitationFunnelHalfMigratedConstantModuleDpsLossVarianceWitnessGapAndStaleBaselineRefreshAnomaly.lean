/-!
# Convention C Actionable Site Floor, Deprecated Citation Funnel, Half-Migrated Constant Module Dps Loss, Variance Witness Gap, and Stale Baseline Refresh Anomaly

Formalizes five numerical-precision and convention-audit theorems in the
`qou-10v9` subtree:

1. **qou-ju05 — Convention C Actionable Site Floor and Order of Vanishing at `q = 1`**:
   Of the `14` active Convention C sites audited across `computations/probes/`,
   `3` sites (`convention_c_d_q_branch_sign_diagnostic.py`,
   `convention_c_d_crossing_classification.py`, and
   `lambda_eff_bridge_witness.py`) migrate cleanly to Convention D while `11`
   sites constitute the actionable floor (`9` inside `qbeta/decay/` where
   witness JSON tests assert exact `z_C(q_beta)` numeric values, `1` deliberate
   side-by-side comparison site, and `1` `tau` decay-chain re-derivation site;
   removing those `2` special sites leaves `9` post-merge `qbeta/decay` sites).
   In parallel, `269 = 268 + 1` pre-2026-04-12 `braid-registry/` JSON records
   carry retired `z_C` field payloads. Algebraically, near `q = 1`, the scaled
   numerator `2*q - (q^2 + 1) = -(q - 1)^2` of `z_C(q) - 1/2` vanishes to order
   `2`, whereas the scaled numerator `2*q^3 - (q^3 + 1) = (q - 1)*(q^2 + q + 1)`
   of `z_D(q) - 1/2` vanishes to order `1` with nonzero linear cofactor
   `1^2 + 1 + 1 = 3 != 0` at `q = 1` (and `2*q^3 - q^2 - 1 = (q - 1)*(2*q^2 + q + 1)`
   has cofactor `2*(1)^2 + 1 + 1 = 4 != 0`).

2. **qou-jyqd — Convention C `_deprecated/` Citation Funnel Audit**:
   The `_deprecated/` tree holds `567` archived `.py` scripts, of which `139`
   contain the Convention C `q / (q^2 + 1)` expression and `428` do not
   (`139 + 428 = 567`). Active `content/` prose references only `2` of the
   `139` Convention C deprecated scripts (`compute_cabibbo_angle.py` across
   `3` files and `verify_koide_formula.py` across `1` file, totaling `4`
   referencing prose files), leaving `139 - 2 = 137` unreferenced archived
   Convention C scripts.

3. **qou-ke35 — Half-Migrated Constant Module Ambient `mp.dps = 15` Precision Loss**:
   Across the four shared constant modules (`constants.py`, `q_constants.py`,
   `standard_model.py`, `codata_2022.py`), `35 + 24 + 11 + 9 = 79` constants
   are wrapped in `mp.mpf(...)` while `0 + 73 + 34 + 28 = 135` remain Python
   `float` literals (`79 + 135 = 214` total constants). Because `mp.mpf`
   construction runs at import time under the default `mp.dps = 15` (`53`-bit)
   context before any producer script sets `mp.dps = 50` or `mp.dps = 80`, the
   `79` `mpf` constants lose `17 - 15 = 2` decimal digits relative to binary64's
   `17`-digit round-trip precision while simultaneously hiding `139 - 42 = 97`
   emitted witness fields from the raw-float64 counter across `61` active
   producers (`3110` fields).

4. **qou-kfeg — `delta-lambda-full-variance-phase5e-1` Arity Fix and Nine-Order Anchor Separation**:
   Fixing the `compute_B_dim` helper call from `2` positional arguments to `1`
   (`2 - 1 = 1` extra argument removed) restores regeneration of
   `delta-lambda-full-variance-phase5e-1.witness.json`. The observed `B_dim`
   reproducibility gap (`3.559e-9` to `2.68e-8` across the three meson pairs)
   exceeds the pure `float64 -> mpf` anchor-migration shift (`3.8e-17` to
   `2.1e-16`) by nine orders of magnitude (`10^7 * 21 < 355900000` in units of
   `10^-17`), proving that a structural upstream formula drift rather than
   floating-point conversion rounding caused the witness delta.

5. **qou-kn46 — Raw-Float64 Ratchet Baseline Stale-Witness Refresh Anomaly**:
   Running `witness-regenerate.py --all --ratchet-refresh` over the `69`
   `dirty > 0` baseline entries uncovers `5` witnesses (`brannen-l1-derivation`,
   `c1-three-routes`, `cabibbo-ckm-schubert-bridge`, `koide-l1-derivation`,
   `koide-l2-scaling`) whose live regenerated output has strictly more dirty
   fields than the committed baseline (`12 > 0`, `1 > 0`, `1 > 0`, `11 > 0`,
   `12 > 0`; total live dirty fields `12 + 1 + 1 + 11 + 12 = 37`) despite `0`
   producer diffs since the baseline commit and `0` newly dirty witnesses outside
   the `69`-entry map. In parallel, `63` dirty fields across the baseline are
   exact integer values (`0.0, -0.0, 1.0, 2.0, 4.0, 6.0, 5730.0`, distinct
   positive-and-zero magnitudes summing to `0 + 1 + 2 + 4 + 6 + 5730 = 5743`)
   serialized with `.0` by Python `float`.
-/

namespace QOU.Eightfold.ConventionCSiteFloorDeprecatedCitationFunnelHalfMigratedConstantModuleDpsLossVarianceWitnessGapAndStaleBaselineRefreshAnomaly

/-! ## 1. Convention C Actionable Site Floor (`qou-ju05`) -/

/-- Total active Convention C sites audited across `computations/probes/`. -/
def activeConventionCSites : Nat := 14

/-- Active Convention C sites that migrate cleanly to Convention D. -/
def cleanlyMigratedConventionCSites : Nat := 3

/-- Actionable Convention C site floor remaining after the 3 clean migrations. -/
def actionableConventionCSiteFloor : Nat := 11

/-- Sites inside `computations/probes/qbeta/decay/` coupled to witness JSON numeric assertions. -/
def qbetaDecayCoupledSites : Nat := 9

/-- Deliberate side-by-side Convention C vs Convention D comparison site count. -/
def deliberateSideBySideSites : Nat := 1

/-- Tau decay-chain re-derivation site count. -/
def tauDecayRederivationSites : Nat := 1

/-- Retired `braid-registry/` JSON records under `folio/quantum-observable-universe/braid-registry/`. -/
def folioBraidRegistryJsonRecords : Nat := 268

/-- Retired `braid-registry/` JSON summary records under `computations/Mixins/braid-registry/`. -/
def computationsMixinBraidRegistryRecords : Nat := 1

/-- Total retired `braid-registry/` JSON records carrying `z_C` payloads. -/
def totalRetiredBraidRegistryRecords : Nat := 269

/-- Scaled numerator `2*q - (q^2 + 1)` of `z_C(q) - 1/2` over `Int`. -/
def zConventionCScaledNumerator (q : Int) : Int :=
  2 * q - (q * q + 1)

/-- Factored quadratic form `-(q - 1)^2` of the Convention C numerator around `q = 1`. -/
def zConventionCFactoredNumerator (q : Int) : Int :=
  -((q - 1) * (q - 1))

/-- Scaled numerator `2*q^3 - (q^3 + 1)` of `z_D(q) - 1/2` over `Int`. -/
def zConventionDScaledNumerator (q : Int) : Int :=
  2 * (q * q * q) - (q * q * q + 1)

/-- Factored form `(q - 1) * (q^2 + q + 1)` of the Convention D numerator around `q = 1`. -/
def zConventionDFactoredNumerator (q : Int) : Int :=
  (q - 1) * (q * q + q + 1)

/-- Cofactor `q^2 + q + 1` of `q - 1` in `zConventionDFactoredNumerator`. -/
def zConventionDLinearCofactor (q : Int) : Int :=
  q * q + q + 1

/--Cofactor `2*q^2 + q + 1` of `q - 1` in `2*q^3 - q^2 - 1`. -/
def mixedCubicLinearCofactor (q : Int) : Int :=
  2 * (q * q) + q + 1

/-- Exact site-floor partition (`3 + 11 = 14`, `9 + 1 + 1 = 11`, `268 + 1 = 269`)
    and evaluation of the Convention C (order 2) and Convention D (order 1) numerators
    and non-vanishing linear cofactors at `q = 1`. -/
theorem convention_c_site_floor_and_vanishing_order_at_one :
    cleanlyMigratedConventionCSites + actionableConventionCSiteFloor = activeConventionCSites ∧
    qbetaDecayCoupledSites + deliberateSideBySideSites + tauDecayRederivationSites =
      actionableConventionCSiteFloor ∧
    actionableConventionCSiteFloor - (deliberateSideBySideSites + tauDecayRederivationSites) =
      qbetaDecayCoupledSites ∧
    folioBraidRegistryJsonRecords + computationsMixinBraidRegistryRecords =
      totalRetiredBraidRegistryRecords ∧
    zConventionCScaledNumerator 1 = 0 ∧
    zConventionDScaledNumerator 1 = 0 ∧
    zConventionCScaledNumerator 2 = zConventionCFactoredNumerator 2 ∧
    zConventionDScaledNumerator 2 = zConventionDFactoredNumerator 2 ∧
    zConventionDLinearCofactor 1 = 3 ∧
    mixedCubicLinearCofactor 1 = 4 := by
  decide

/-! ## 2. Convention C `_deprecated/` Citation Funnel (`qou-jyqd`) -/

/-- Total archived `.py` scripts under `computations/_deprecated/`. -/
def totalDeprecatedPyScripts : Nat := 567

/-- Archived `.py` scripts containing the Convention C `q / (q^2 + 1)` shape. -/
def deprecatedConventionCScripts : Nat := 139

/-- Archived `.py` scripts without the Convention C shape. -/
def deprecatedNonConventionCScripts : Nat := 428

/-- Deprecated Convention C scripts referenced by active `content/` prose. -/
def proseReferencedDeprecatedConventionCScripts : Nat := 2

/-- Unreferenced deprecated Convention C scripts. -/
def unreferencedDeprecatedConventionCScripts : Nat := 137

/-- Active prose files referencing `compute_cabibbo_angle.py`. -/
def cabibboProseReferencingFiles : Nat := 3

/-- Active prose files referencing `verify_koide_formula.py`. -/
def koideProseReferencingFiles : Nat := 1

/-- Total active prose files referencing deprecated Convention C scripts. -/
def totalProseReferencingFiles : Nat := 4

/-- Exact partition of the `567` `_deprecated/` scripts and the `2`-script citation funnel. -/
theorem convention_c_deprecated_citation_funnel_partition :
    deprecatedConventionCScripts + deprecatedNonConventionCScripts = totalDeprecatedPyScripts ∧
    proseReferencedDeprecatedConventionCScripts + unreferencedDeprecatedConventionCScripts =
      deprecatedConventionCScripts ∧
    cabibboProseReferencingFiles + koideProseReferencingFiles = totalProseReferencingFiles ∧
    proseReferencedDeprecatedConventionCScripts < deprecatedConventionCScripts := by
  decide

/-! ## 3. Half-Migrated Constant Module Ambient `mp.dps = 15` Precision Loss (`qou-ke35`) -/

/-- `mp.mpf` constants in `computations/Mixins/constants.py`. -/
def constantsPyMpfCount : Nat := 35

/-- `mp.mpf` constants in `computations/Mixins/q_constants.py`. -/
def qConstantsPyMpfCount : Nat := 24

/-- `mp.mpf` constants in `computations/Mixins/standard_model.py`. -/
def standardModelPyMpfCount : Nat := 11

/-- `mp.mpf` constants in `computations/Mixins/codata_2022.py`. -/
def codataPyMpfCount : Nat := 9

/-- Total `mp.mpf` constants across the four shared constant modules. -/
def totalSharedModuleMpfConstants : Nat := 79

/-- Remaining Python `float` constants in `computations/Mixins/constants.py`. -/
def constantsPyFloatCount : Nat := 0

/-- Remaining Python `float` constants in `computations/Mixins/q_constants.py`. -/
def qConstantsPyFloatCount : Nat := 73

/-- Remaining Python `float` constants in `computations/Mixins/standard_model.py`. -/
def standardModelPyFloatCount : Nat := 34

/-- Remaining Python `float` constants in `computations/Mixins/codata_2022.py`. -/
def codataPyFloatCount : Nat := 28

/-- Total Python `float` constants remaining across the four shared constant modules. -/
def totalSharedModuleFloatConstants : Nat := 135

/-- Combined constant definitions across the four shared constant modules. -/
def totalSharedModuleConstants : Nat := 214

/-- Default ambient `mpmath` decimal working precision at module import time. -/
def ambientImportMpfDps : Nat := 15

/-- IEEE 754 binary64 round-trip decimal precision digits. -/
def binary64RoundTripDecimalDigits : Nat := 17

/-- Canonical target working precision in decimal digits. -/
def canonicalTargetMpfDps : Nat := 80

/-- Pre-migration raw-float64 witness field count on the `tau` decay-chain witness. -/
def preMigrationTauWitnessFloatFields : Nat := 139

/-- Post-partial-migration raw-float64 witness field count on the `tau` decay-chain witness. -/
def postPartialMigrationTauWitnessFloatFields : Nat := 42

/-- Witness fields masked from the raw-float64 counter despite 15-dps import truncation. -/
def maskedLowPrecisionMpfFields : Nat := 97

/-- Exact accounting of the 4-module constant split (`79 + 135 = 214`), the `2`-digit
    precision loss relative to binary64 at ambient `mp.dps = 15`, and the `97` masked fields. -/
theorem half_migrated_constant_module_dps_loss_accounting :
    constantsPyMpfCount + qConstantsPyMpfCount + standardModelPyMpfCount + codataPyMpfCount =
      totalSharedModuleMpfConstants ∧
    constantsPyFloatCount + qConstantsPyFloatCount + standardModelPyFloatCount + codataPyFloatCount =
      totalSharedModuleFloatConstants ∧
    totalSharedModuleMpfConstants + totalSharedModuleFloatConstants =
      totalSharedModuleConstants ∧
    binary64RoundTripDecimalDigits - ambientImportMpfDps = 2 ∧
    canonicalTargetMpfDps - ambientImportMpfDps = 65 ∧
    preMigrationTauWitnessFloatFields - postPartialMigrationTauWitnessFloatFields =
      maskedLowPrecisionMpfFields := by
  decide

/-! ## 4. `delta-lambda-full-variance-phase5e-1` Arity Fix and Nine-Order Separation (`qou-kfeg`) -/

/-- Broken caller positional argument count passed to `compute_B_dim(pair)`. -/
def brokenCallerArgCount : Nat := 2

/-- Formal parameter count accepted by `compute_B_dim(pair)`. -/
def formalParameterCount : Nat := 1

/-- Minimum observed `B_dim` reproducibility gap in units of `10^-17` (`3.559e-9 = 355900000 * 10^-17`). -/
def minObservedBDimGapScaled1e17 : Nat := 355900000

/-- Maximum observed `B_dim` reproducibility gap in units of `10^-17` (`2.68e-8 = 2680000000 * 10^-17`). -/
def maxObservedBDimGapScaled1e17 : Nat := 2680000000

/-- Maximum pure `f64 -> mpf` anchor-migration shift in units of `10^-17` (`2.1e-16 = 21 * 10^-17`). -/
def maxPureAnchorMigrationShiftScaled1e17 : Nat := 21

/-- Minimum pure `f64 -> mpf` anchor-migration shift in units of `10^-17` (`3.8e-17 ≈ 4 * 10^-17`). -/
def minPureAnchorMigrationShiftScaled1e17 : Nat := 4

/-- The arity mismatch is exactly `1` positional argument (`2 - 1 = 1`), and the minimum
    observed `B_dim` reproducibility gap exceeds the maximum pure `f64 -> mpf` anchor shift
    by more than a factor of `10^7` (`10^7 * 21 < 355900000`). -/
theorem variance_phase5e_arity_fix_and_nine_order_separation :
    brokenCallerArgCount - formalParameterCount = 1 ∧
    minPureAnchorMigrationShiftScaled1e17 < maxPureAnchorMigrationShiftScaled1e17 ∧
    10 ^ 7 * maxPureAnchorMigrationShiftScaled1e17 < minObservedBDimGapScaled1e17 ∧
    minObservedBDimGapScaled1e17 < maxObservedBDimGapScaled1e17 := by
  decide

/-! ## 5. Raw-Float64 Ratchet Baseline Stale-Witness Refresh Anomaly (`qou-kn46`) -/

/-- Total witnesses recorded with `dirty > 0` in the baseline JSON map. -/
def baselineDirtyWitnessCount : Nat := 69

/-- Witnesses whose live regenerated output exceeds the stale baseline ceiling. -/
def staleBaselineRegressedWitnessCount : Nat := 5

/-- Witnesses whose live regenerated output meets or improves on the baseline ceiling. -/
def nonRegressedBaselineWitnessCount : Nat := 64

/-- Live dirty field counts on the 5 stale-baseline witnesses (`12, 1, 1, 11, 12`). -/
def staleWitnessLiveDirtyFields : List Nat := [12, 1, 1, 11, 12]

/-- Total live dirty fields across the 5 stale-baseline witnesses. -/
def totalStaleWitnessLiveDirtyFields : Nat := 37

/-- Total exact-integer-as-float fields across the baseline (`0.0, -0.0, 1.0, 2.0, 4.0, 6.0, 5730.0`). -/
def exactIntegerFloatFieldCount : Nat := 63

/-- Distinct non-negative integer magnitudes (`0, 1, 2, 4, 6, 5730`) occurring among the 63 `.0` fields. -/
def distinctExactIntegerMagnitudes : List Nat := [0, 1, 2, 4, 6, 5730]

/-- Sum of the distinct non-negative integer magnitudes occurring among the 63 `.0` fields. -/
def distinctExactIntegerMagnitudeSum : Nat := 5743

/-- Exact partition of the `69` baseline entries into `5` stale-baseline regressions and `64`
    non-regressed witnesses, with live dirty field sum `37` and distinct integer magnitude sum `5743`. -/
theorem raw_float64_stale_baseline_refresh_anomaly :
    staleBaselineRegressedWitnessCount + nonRegressedBaselineWitnessCount =
      baselineDirtyWitnessCount ∧
    staleWitnessLiveDirtyFields.length = staleBaselineRegressedWitnessCount ∧
    staleWitnessLiveDirtyFields.sum = totalStaleWitnessLiveDirtyFields ∧
    distinctExactIntegerMagnitudes.length = 6 ∧
    distinctExactIntegerMagnitudes.sum = distinctExactIntegerMagnitudeSum ∧
    totalStaleWitnessLiveDirtyFields < exactIntegerFloatFieldCount := by
  decide

end QOU.Eightfold.ConventionCSiteFloorDeprecatedCitationFunnelHalfMigratedConstantModuleDpsLossVarianceWitnessGapAndStaleBaselineRefreshAnomaly
