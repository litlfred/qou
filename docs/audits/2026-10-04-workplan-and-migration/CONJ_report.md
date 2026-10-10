# CONJ slice — open-conjecture umbrella and register (2026-10-04)

All counts here are `[M]` from qou `main` @ 348e299cc unless marked otherwise. This is a read-only analysis, and per the owner's hard rule (2026-10-04) it is **descriptive only**. It recommends no edit, restatement or correction of any conjecture, proof, Lean declaration or number. Anything that looks wrong is marked **needs-owner**.

## 1. What the inventory measured
- **182 paper blocks** use the `conjecture(…)` builder under `folio/quantum-observable-universe/` `[M]`. The 2026-09-08 audit §5.1 counted 181 `[D]`. 177 of them carry a `lean.ref`, 174 of those resolve to a declaration, and 5 have no ref `[M]`.
- **Lean (comment-stripped scan):** 923 distinct `class` names, of which 86 have an `instance` anywhere `[M]`. That number counts every class, including typeclass infrastructure, so it is **not** a conjecture count. PR #7180's figure of "187 Prop classes with no instance" is `[D]` from that branch's commit message: it ships only a bean body, with no list, so it was not re-derived. Do not quote it as current.
- Of the 182 blocks, only **6 have a real (non-comment) instance**. All 6 are partial or special cases. `BorromeanQuark`'s instance is trivial (`fun q => …`, `rfl`), and bean qou-7yj0 already tracks it.
- **b9cj lists only 23 carriers** `[B]`, uses pre-migration `content/` paths, and was last updated 08-01. It covers about 13 % of the register.

## 2. The umbrella and its sub-epics
**Umbrella: reuse `b9cj`** as a story-free epic (`promote-epic`). Its title already reads "track all open conjectures", it holds 24 children, and every alternative would create a 371st epic. Its body needs a bean-level rewrite to point at the register (Appendix). The 24 `cj*` carriers move from b9cj to their family sub-epic.

### 2a. FORMAL mathematical conjectures (108 blocks)
| sub-epic | bean to BE the epic | blocks | note |
|---|---|---|---|
| CONJ-VOL volume conjecture & hyperbolic volumes | NEW (absorbs qou-nalu, qou-u1b5, qou-0yqu as stories; qou-cpfn completed) | 12 | Kashaev, Whitehead, 4₁, 5₂ sum rule, Borromean |
| CONJ-DILOG q-dilog archimedean limit / Faddeev rigidity | **qou-r9ih** (children qou-03lh, qou-icx5, qou-lbth) | 4 | Part A proved in Lean `[B: block note 07-24]`; Part B open |
| CONJ-PERIOD periods, Bloch group, irrationality, Goncharov | NEW | 13 | aspirational number theory |
| CONJ-AJ AJ / strong-AJ | **c7vs** (qou-iiz4, qou-y7o7 become stories) | 0 blocks | strong AJ for 4₁ is a *published theorem* (Nguyen–Tran). The Lean work is formalisation, conditional on `TransferLemmas` (no instance) |
| CONJ-RES resurgence / Stokes / alien calculus / q-Gevrey | **qou-frzo** (qou-q04o, qou-7b7v become stories) | 6 | Borel variable = proper time is `conj:schwinger-measure-computational-time` |
| CONJ-HABIRO Habiro / jet / GS filtration | NEW | 14 | 12 of 14 carry q₀ or empirical words (see §3) |
| CONJ-HECKE Hecke / KLR / crystal / Markov / Wenzl | NEW (qou-otbb → P3) | 20 | includes `covariance_kernel_conjecture`, proved for k ≤ 8 `[B]` |
| CONJ-QGL q-geometric Langlands | NEW | 7 | 4 carriers, all `holds : Prop` shaped (qou-hprp) |
| CONJ-SURR surreal / infinitesimal | NEW | 9 | |
| CONJ-BRING Bring / tetraplectic geometry | NEW | 6 | |
| CONJ-QRH q-RH / explicit formula | NEW | 5 | `QExplicitFormula` is proved only for the empty spectrum `[B qou-qexu]` |
| CONJ-PNP P≠NP-in-QOU | **qou-b1je** (qou-yi7h, qou-f9wl become stories) | 3 | |
| CONJ-QNS q-Navier–Stokes / Gevrey persistence | **qou-a3n3** | 6 | |
| CONJ-QCOLL q-Collatz | **qcz14** (its parent qcz1 is a *scrapped* session log) | 1 | |
| CONJ-ASP BSD, Yang–Mills mass gap | NEW | 2 | aspirational encodings |
| CONJ-HYG §3b carrier hygiene | **qou-5p7n** | — | holds-Prop, residual = 0 and trivially-inhabited carriers |
| CONJ-CITED citation-justified classes | **qou-pddf** | — | |

### 2b. NOT formal conjectures: 74 physical-identification blocks
These blocks use the `conjecture` builder, but their statement *is* an identification of a physical observable. Examples are the Higgs as T(2,8), magic numbers, the Weinberg angle, the proton assembly and the Bohr radius. Families: PH-MASS 28, PH-SM 28, PH-ATOM 11, PH-COSMO 7. **Recommendation: keep them out of the formal umbrella.** Put them under P1 (mass/binding chain) and P4 (SM/eightfold way) as "identification hypotheses", so a formal sub-epic never inherits an empirical premise. Whether to re-label them is a **needs-owner** decision. This report proposes no content change.

## 3. Formal-vs-empirical flags (the STRICT rule)
- **47 formally phrased blocks carry an empirical-dependence signal** `[M, keyword]`. Either the block evaluates at the calibrated **q₀**, which audit §5.3 calls "structurally tautological. We defined q₀ to enforce it" `[D]`, or its text uses fit / near-match / CODATA / measured / ppm language. This is a keyword screen, not a judgement: each block needs owner review. Worst concentrations are HABIRO (12/14), HECKE (10/20), RES (6/6), PNP (3/3) and VOL (4/12).
- **Spot-checked as genuine:** `conj:hecke-monodromy-step-two` fixes its level by q₀ (`k+2 = 2πi/ln q₀ ≈ 60.218 i`).
- **Lean classes whose fields compare to measured values** `[D audit §5.2]`:
  - `QOU.Borromean.MassFormula`, with `|m_p/m_e − 1836.152673426| ≤ residual`
  - `QbetaCkTruncationCanonicalClass`, which axiomatises a 3.47 % near-match
  - `gram_kappa_numerical_value`, with `|κ − 1.722| < 0.001`

  All three are PH-family, but any formal theorem conditional on them inherits the empirical premise. This is **needs-owner**.
- **Beans that would put an empirical value into a formal question:**
  - qou-z8me: is a measured B = 8.0001 exactly 8?
  - qou-avra: "fit D(m) cofactors to one Habiro element"
  - qou-68ge: c₃ "anti-fit, high-variance"
  - qou-p7n5: c₂ reproduced from R(q₀)

## 4. Duplicate clusters (survivor first)
- qou-085a ← qou-206h, qou-o29t, qou-6a7u (`covariance_kernel_conjecture`, same declaration)
- qou-qu2t ← qou-7hfy (`qbeta_ck_truncation_canonical`)
- qou-cfxs ← qou-6icw, qou-nyij (`HyperbolicVolumeIndependence`)
- qou-r75d ← qou-th1n (`WhiteheadVolumeConjecture`)
- qou-2szo ← qou-vx3g (Kashaev pieceVolume)
- qou-iv9f ← qou-e32b, qou-aja6 (P≠NP faithfulness leg / `JetHorizonTransfer.transfer`)
- qou-hprp ← qou-tsnp (`holds : Prop` carriers, 23 vs 12; m-confidence)
- qou-3qla ← qou-h6o3 (45 convention-C resurgence audits)
- qou-cons ← qou-r64l (Φ₁/Φ₂ entire)
- qou-ntef ← qou-4iy0 (A_ω residual)
- qou-ri9w ← qou-9dvz (5₂ FW↔GGM)
- qou-ls7l ← qou-kcii (Habiro witness)
- cj2d5 ← qou-9595
- cj504 ← qou-lmr1

**Pattern:** the auto-generated beans from 08-04 ("Conjecture: X"), 08-12 ("X gap (X.lean)") and 08-01/08-31 ("PROVE(lean): X") each re-filed the same declaration. That is three generator runs with no dedupe.

## 5. Landed but still open (low confidence, verify)
`main` carries "W5b: Whitehead-chain squeeze sorry-free — THIRD volume-conjecture instance" (9a1c80e) and "BRICK 5 — unconditional VC squeeze" (adb66dd). The Kashaev block's note says three instances are machine-proved `[B]`. Yet these remain open: qou-t2sc, qou-dw20, qou-1gkf, qou-x5mg, qou-sho7, and qou-e1dc ("land PR #4532", not in the open-PR list). They are marked `close-evidence?`. It is unclear whether each targets the Whitehead *chain* or the Whitehead *link*.

## 6. Stalled claims
**55 open CONJ beans are `in-progress` with no update since before 2026-09-20.** They include the epics b9cj, qou-b1je, qou-iiz4, qou-a3n3 and qou-frzo, and the q-Collatz milestones qcz6/14/15. The full list is in the mapping evidence column. Several are parented to scrapped session logs (qou-89f9: 8 children; qcz1), so they are orphaned in practice.

## 7. Routing of the rest
- 68 beans are citation, remark or cross-check intake ("Cite X at Y", "Remark interpreting …"). They are not conjecture work and go to **P5 library-intake**.
- 30 go to P1 Q_β, 15 to P1 extensive binding, 2 to P1 α_em, 4 to P4 and 3 to P3.

## 8. Owner decisions (13 needs-owner rows; one asked here in full)
**The question with the most leverage:** should the 74 physical-identification blocks that use the `conjecture` builder sit under the conjecture umbrella, or under P1/P4?
- **Option A (recommended):** P1/P4. The umbrella then holds only formal mathematics, as the STRICT rule asks.
- **Option B:** a PH sub-epic inside the umbrella. One place to look, but formal and empirical work mix.
- **If you say nothing,** the mapping assumes A.

The other 12 needs-owner items are listed in the mapping:
- qou-wzgm pairs a formal conjecture with a PH one.
- Content-change beans: qou-6eik, qou-8b0q, qou-af6z, qou-fl4t, qou-6766, qou-tdp0, qou-xsv8, qou-unob.
- WALL beans: qou-l1h5, qou-innq.
- qou-z8me (measured coefficient), qou-kzka (marked PRUNED).
- The register's statuses also flag these for owner review: `conj:brunnian-property-of-borromean` and `conj:poincare-lefschetz-borromean` may state classical theorems, and `conj:n-v-leading-order-derivation` says its bridge "is now a THEOREM".

## 9. Skill gaps
1. **No conjecture register.** Nothing joins block ↔ `lean.ref` ↔ instance ↔ beans. b9cj was a hand list and went stale in 4 weeks. A generic `conjecture-register` skill/sidecar, built like `audit-coverage`, would answer "what is open" by measurement.
2. **No `formal | identification` field on `conjecture()`.** The STRICT owner rule cannot be checked mechanically without it. This report used a keyword screen.
3. **No create-time dedupe keyed on Lean declaration** for generated beans (see the §4 pattern).
4. **Session-log parents** (`qcz1`, `qou-89f9` scrapped) orphan live work. A check for "open child of scrapped parent" belongs in `health`.

## Appendix — conjecture register (182 blocks)
`formal?`: **F** = formal, no signal. **F-flag** = formal statement with a q₀ or empirical signal, owner to review. **E** = physical identification. `#open beans` = open beans anywhere in the store whose body mentions the label or Lean class name. It overlaps across rows and is not a count of attack beans.

| conjecture | family | formal? | status | Lean carrier | #open beans |
|---|---|---|---|---|---|
| `archimedean-realisation-volume-compatibility` | VOL | F | open | `realisation_volume_compatibility` | 0 |
| `b1-hyperbolic-rows-theorem` | VOL | F | open | `b1_hyperbolic_rows` | 4 |
| `brunnian-property-of-borromean` | VOL | F | classical theorem (Brunnian property of Borromean rings is known) — needs-owner | `borromean_brunnian` | 2 |
| `geom-universality` | VOL | F-flag @q0 | open | `geom_universality` | 1 |
| `geom-yekutieli-alignment` | VOL | F | open | `geom_yekutieli_alignment` | 1 |
| `jsj-decomposition-linearity` | VOL | F | open | `JSJ_volume_additivity` | 2 |
| `kashaev-surreal` | VOL | F-flag @q0 +emp-words | conditional | `KashaevSurreal` | 4 |
| `kashaev-volume-conjecture` | VOL | F | open (proved for 4₁, Whitehead chain, Borromean per block note) | `VolumeConjecture` | 13 |
| `mirror-3d-3d-correspondence` | VOL | F-flag @q0 +emp-words | open | `Mirror3d3dCorrespondence` | 4 |
| `pachner-pentagon-borromean` | VOL | F | open | `PachnerPentagonBorromean` | 1 |
| `poincare-lefschetz-borromean` | VOL | F | classical theorem (Poincaré–Lefschetz duality) as stated? — needs-owner | `PoincareLefschetzBorromean` | 2 |
| `shared-denominator-cusp-holonomy` | VOL | F-flag @q0 | open | `shared_denominator_cusp_holonomy` | 1 |
| `algebraic-geometric-dilog-equivalence` | DILOG | F-flag @q0 | open | `algebraic_geometric_equivalence` | 1 |
| `dilogarithm-archimedean-limit` | DILOG | F-flag @q0 | Part A proved (Lean); Part B open | `ArchimedeanLimit` | 6 |
| `dim-master-pentagon` | DILOG | F | open | `DimMasterPentagon` | 3 |
| `phi-q-wkb-greens-function` | DILOG | F | instance exists (check: partial/trivial) | `WKBGreensFunction` | 0 |
| `borel-zagier-qou-volumes` | PERIOD | F | open | `BorelZagierQouVolumes` | 7 |
| `borromean-bloch-group-element` | PERIOD | F-flag @q0 | open | `BorromeanBlochGroupElement` | 7 |
| `bring-figure-eight-depth-2-witness` | PERIOD | F | open | `BringFigureEightDepth2Witness` | 6 |
| `bring-hyperbolic-knot-bloch-decomposition` | PERIOD | F-flag +emp-words | open | `bring_hyperbolic_decomposition` | 1 |
| `bring-trilog-depth-3-witness` | PERIOD | F | open | `BringTrilogDepth3Witness` | 6 |
| `gb-depth-period-correspondence` | PERIOD | F | open | `GBDepthPeriodCorrespondence` | 3 |
| `hyperbolic-volume-transcendence` | PERIOD | F-flag @q0 | instance exists (check: partial/trivial) | `HyperbolicVolumeIndependence` | 13 |
| `joint-galois-braid-action` | PERIOD | F | open | `JointGaloisBraidAction` | 2 |
| `qou-infra-discharges-goncharov-zeta5` | PERIOD | F | open | `QouInfraDischargesGoncharovZeta5` | 7 |
| `qou-motivic-galois-instance` | PERIOD | F | open | `(no lean.ref)` | 0 |
| `single-volume-irrationality` | PERIOD | F | open | `SingleVolumeIrrationality` | 7 |
| `three-knot-jet-order-independence` | PERIOD | F-flag @q0 | open | `JetOrderIndependence` | 4 |
| `two-filtration-bridge` | PERIOD | F | open | `TwoFiltrationBridge` | 13 |
| `c1-ggm-bar-parity-faces` | RES | F-flag +emp-words | open | `doorV_parity_no_identity` | 2 |
| `modular-s-transform-q-q-tilde` | RES | F-flag @q0 | open | `ModularSTransformQQTilde` | 2 |
| `q-zero-stokes-region-identification` | RES | F-flag @q0 | open | `QZeroStokesIdentification` | 1 |
| `qdifference-kernel-prolongation-symbol` | RES | F-flag @q0 +emp-words | open | `QDifferenceKernelIsProlongationSymbol` | 19 |
| `schwinger-measure-computational-time` | RES | F-flag @q0 +emp-words | open | `BorelProperTimeIdentification` | 2 |
| `stokes-dt-bps-bridge` | RES | F-flag +emp-words | open | `StokesDTBPSBridge` | 11 |
| `archimedean-remainder-exponential-decay` | HABIRO | F-flag @q0 | open | `ArchimedeanRemainderExponentialDecay` | 0 |
| `brane-tower-z-habiro` | HABIRO | F-flag @q0 +emp-words | open | `BraneTowerZHabiro` | 1 |
| `crossing-graded-mass-expansion` | HABIRO | F-flag @q0 | open | `CrossingGradedMassExpansion` | 3 |
| `cyclotomic-boundary-at-keystone` | HABIRO | F-flag +emp-words | open | `(no lean.ref)` | 1 |
| `gs-archimedean-agreement-residue` | HABIRO | F-flag @q0 | open | `archimedean_agreement` | 10 |
| `gs-archimedean-agreement-trace` | HABIRO | F-flag @q0 | open | `archimedean_agreement` | 9 |
| `gs-residue-at-root-existence` | HABIRO | F-flag @q0 | open | `ResidueAtRoot` | 1 |
| `gs-spectral-decomposition-existence` | HABIRO | F-flag @q0 | open | `spectral_decomposition` | 7 |
| `gs-spectral-sum-finite` | HABIRO | F-flag @q0 | open | `spectral_sum_finite` | 0 |
| `jet-convergence-classical-limit` | HABIRO | F | open | `jet_convergence_classical_limit` | 8 |
| `jet-filtered-knot-factor` | HABIRO | F-flag +emp-words | open | `jet_filtered_knot_factor` | 7 |
| `jet-tower-uniform-delta-max` | HABIRO | F | open | `JetTowerUniformDeltaMax` | 1 |
| `lifted-crossing-locality` | HABIRO | F-flag @q0 | open | `LiftedCrossingLocality` | 2 |
| `tau-all-orders-bridge` | HABIRO | F-flag @q0 | open | `tau_all_orders_bridge` | 0 |
| `atom-braid-exterior-algebra` | HECKE | F | open | `AtomBraidExteriorAlgebraStructure` | 0 |
| `block-multiplicativity-v-free` | HECKE | F-flag @q0 | open | `BlockMultiplicativityVFree` | 0 |
| `categorical-linking-operation` | HECKE | F | open | `CategoricalLinkingOperation` | 1 |
| `confinement-grading-correspondence` | HECKE | F | open | `ConfinementGradingCorrespondence` | 0 |
| `confinement-nf-structure-forcing` | HECKE | F | open | `ConfinementNfStructureForcing` | 2 |
| `crystal-graph-realization` | HECKE | F | open | `CrystalGraphRealization` | 6 |
| `depth-stratified-frobenius-reciprocity` | HECKE | F-flag +emp-words | open | `DepthStratifiedFrobeniusReciprocity` | 1 |
| `diagrammatic-double-magic-lr-fusion` | HECKE | F | open | `DoubleMagicConjecture` | 2 |
| `explicit-central-idempotent` | HECKE | F-flag +emp-words | open | `ExplicitCentralIdempotentConjecture` | 0 |
| `graded-baer-star-Hq` | HECKE | F | open | `GradedBaerStarHq` | 0 |
| `gs-graded-markov-trace-existence` | HECKE | F-flag @q0 | open | `GradedMarkovTraceExistence` | 4 |
| `hecke-monodromy-step-two` | HECKE | F-flag @q0 +emp-words | open | `HeckeMonodromy` | 4 |
| `kazhdan-lusztig-classical-limit` | HECKE | F | open | `KazhdanLusztigClassicalLimit` | 4 |
| `lusztig-canonical-basis-q-eq-1` | HECKE | F-flag @q0 | open | `LusztigCanonicalBasisQEq1` | 2 |
| `on-p-modular-hecke` | HECKE | F-flag @q0 | open | `OnPModularHecke` | 1 |
| `psd-trace-orthogonality` | HECKE | F-flag @q0 +emp-words | open | `psd_trace_orthogonality_holds_for_all_atoms` | 0 |
| `reverse-limit-q-to-infinity` | HECKE | F-flag @q0 +emp-words | open | `ReverseLimitQToInfinity` | 1 |
| `root-of-unity-mtc-truncation` | HECKE | F | open | `RootOfUnityMTCTruncation` | 1 |
| `wenzl-positivity-implies-substrate-positivity` | HECKE | F-flag @q0 | open | `WenzlPositivityImpliesSubstratePositivity` | 1 |
| `whipple-rotation-intertwining` | HECKE | F | open | `WhippleRotationIntertwining` | 0 |
| `q-geometric-langlands` | QGL | F | open | `QGeometricLanglandsConjecture` | 1 |
| `q-gl-classical-limit` | QGL | F | open | `q_gl_classical_limit` | 4 |
| `q-gl-fiber-functor` | QGL | F | open | `q_gl_fiber_functor` | 5 |
| `q-gl-kummer-filtration` | QGL | F | open | `q_gl_kummer_filtration` | 5 |
| `q-oper-hecke` | QGL | F | open | `q_oper_hecke` | 5 |
| `quantum-langlands-dual` | QGL | F | open | `QuantumLanglandsDual` | 2 |
| `tannaka-krein-isomorphism` | QGL | F | open | `IsTannakaKreinDual` | 1 |
| `archimedean-stpart` | SURR | F | open | `ArchimedeanIsStandardPart` | 2 |
| `classical-limit-stpart` | SURR | F | open | `ClassicalLimitStpart` | 3 |
| `diophantine-birthday` | SURR | F-flag @q0 | open | `DiophantineBirthday` | 10 |
| `infinitesimal-frobenius` | SURR | F-flag +emp-words | open | `InfinitesimalFrobenius` | 0 |
| `infinitesimal-observability` | SURR | F | open | `InfinitesimalObservability` | 0 |
| `jones-birthday` | SURR | F | open | `JonesBirthday` | 2 |
| `local-infinitesimal-field` | SURR | F-flag @q0 | open | `LocalInfinitesimalField` | 5 |
| `surreal-limit-transfer` | SURR | F | open | `SurrealLimitTransfer` | 1 |
| `vacuum-epsilon` | SURR | F | instance exists (check: partial/trivial) | `VacuumEpsilon` | 5 |
| `cl3-zeta5-geometric-realization` | BRING | F | open | `Cl3Zeta5GeometricRealization` | 1 |
| `klein-bring-icosahedral-bridge` | BRING | F | instance exists (check: partial/trivial) | `KleinBringIcosahedralBridge` | 1 |
| `orbital-fourier-decomposition` | BRING | F | open | `orbital_fourier_decomposition` | 0 |
| `orbital-space-normal-bundle` | BRING | F | open | `orbital_space_normal_bundle` | 1 |
| `tetraplectic-askey-localisation` | BRING | F | open | `(no lean.ref)` | 1 |
| `tetraplectic-sw-localisation-bridge` | BRING | F | open | `(no lean.ref)` | 1 |
| `adelic-critical-line-persistence` | QRH | F | open | `AdelicCriticalLinePersistence` | 0 |
| `classical-riemann-hypothesis` | QRH | F | open | `ClassicalRiemannHypothesis` | 7 |
| `explicit-formula` | QRH | F | open | `explicit_formula` | 2 |
| `macroscopic-stability-equivalence` | QRH | F | open | `macroscopic_stability_equivalence` | 0 |
| `wigner-axiom` | QRH | F | open | `WignerAxiom` | 4 |
| `p-vs-np-qou` | PNP | F-flag @q0 +emp-words | open | `PvsNPQou` | 1 |
| `qou-p-neq-np` | PNP | F-flag @q0 | open | `QouPNeqNp` | 8 |
| `quantum-computational-universality` | PNP | F-flag @q0 | open | `QuantumComputationalUniversality` | 1 |
| `critical-exponent` | QNS | F | instance exists (check: partial/trivial) | `CriticalExponent` | 0 |
| `levi-degeneracy` | QNS | F-flag +emp-words | open | `LeviDegeneracy` | 1 |
| `ns-counterexample` | QNS | F-flag +emp-words | instance exists (check: partial/trivial) | `NSCounterexample` | 0 |
| `q-aubin-lions` | QNS | F | open | `QAubinLions` | 0 |
| `regularity-breakdown` | QNS | F | open | `RegularityBreakdown` | 1 |
| `spectral-normal-form` | QNS | F | open | `SpectralNormalForm` | 6 |
| `q-collatz` | QCOLL | F-flag @q0 | open | `QCollatz` | 10 |
| `q-birch-swinnerton-dyer` | ASP | F | open | `QBirchSwinnertonDyer` | 3 |
| `yang-mills-mass-gap` | ASP | F | open | `YangMillsMassGap` | 1 |
| `active-set-trace-concentration` | PH-MASS | E (physical identification) | open | `(no lean.ref)` | 0 |
| `alpha-k-categorical-closure` | PH-MASS | E (physical identification) +measured-cmp | open | `AlphaKCategoricalClosure` | 1 |
| `binding-manybody-eq-jet-filtration` | PH-MASS | E (physical identification) +measured-cmp | open | `BindingManyBodyJetFiltration` | 8 |
| `binding-qbeta-complex-volume` | PH-MASS | E (physical identification) +measured-cmp | open | `ComplexVolumeMatch` | 7 |
| `borromean-baryon-mass-formula` | PH-MASS | E (physical identification) +measured-cmp | open | `MassFormula` | 11 |
| `canonical-knot-id-sdp` | PH-MASS | E (physical identification) +measured-cmp | instance exists (check: partial/trivial) | `CanonicalKnotIdSDP` | 9 |
| `complex-mass-constituent-functional` | PH-MASS | E (physical identification) +measured-cmp | open | `ComplexMassConstituent` | 0 |
| `flavor-split-habiro-derivation` | PH-MASS | E (physical identification) +measured-cmp | open | `topological_flavor_split` | 2 |
| `hoefsmit-scattering-pipeline` | PH-MASS | E (physical identification) | open | `hoefsmit_scattering_pipeline` | 4 |
| `im-q-physical-role` | PH-MASS | E (physical identification) +measured-cmp | open | `ImQPhysicalRole` | 7 |
| `inter-nucleon-channel-color-tube` | PH-MASS | E (physical identification) +measured-cmp | open | `InterNucleonChannelColorTube` | 2 |
| `isospin-from-canonical-bowtie` | PH-MASS | E (physical identification) +measured-cmp | open | `IsospinFromCanonicalBowtie` | 6 |
| `kashaev-density-equals-sdp-multiplicity` | PH-MASS | E (physical identification) +measured-cmp | open | `KashaevDensityEqualsSdpMultiplicity` | 7 |
| `knot-factor-frobenius-pairing` | PH-MASS | E (physical identification) +measured-cmp | open | `KnotFactorFrobeniusPairing` | 1 |
| `lepton-mass-tower-canonical` | PH-MASS | E (physical identification) +measured-cmp | open | `lepton_mass_ratio` | 1 |
| `lepton-tower-h-n-plus-1-branching` | PH-MASS | E (physical identification) +measured-cmp | open | `lepton_xi` | 0 |
| `mass-endomorphism` | PH-MASS | E (physical identification) +measured-cmp | open | `MassEndomorphism` | 7 |
| `mass-volume-factorization` | PH-MASS | E (physical identification) +measured-cmp | open | `MassVolumeFactorization` | 1 |
| `proton-borromean-assembly` | PH-MASS | E (physical identification) +measured-cmp | open | `ProtonBorromeanAssembly` | 1 |
| `q-integer-mass-formula` | PH-MASS | E (physical identification) +measured-cmp | open | `QIntegerMassFormula` | 6 |
| `qbeta-ck-truncation-canonical` | PH-MASS | E (physical identification) +measured-cmp | open | `QbetaCkTruncationCanonicalClass` | 0 |
| `qbeta-trace-counit-convergence` | PH-MASS | E (physical identification) | open | `QBetaTraceCounitConvergence` | 0 |
| `reeb-linking-cwf-normalization` | PH-MASS | E (physical identification) +measured-cmp | open | `ReebLinkingCWF` | 0 |
| `reidemeister-mass-invariance` | PH-MASS | E (physical identification) | conditional | `reidemeister_mass_invariance` | 2 |
| `rho-k-pair-gen-canonical-form` | PH-MASS | E (physical identification) +measured-cmp | open | `PairGenCanonical` | 1 |
| `rho-prefactor-structural` | PH-MASS | E (physical identification) | open | `RhoPrefactorStructural` | 0 |
| `staircase-ew-residual` | PH-MASS | E (physical identification) | open | `StaircaseEWResidual` | 1 |
| `z-eq-n-rho-correction` | PH-MASS | E (physical identification) +measured-cmp | open | `ZeqNRhoCorrection` | 1 |
| `borromean-quark` | PH-SM | E (physical identification) +measured-cmp | instance exists (check: partial/trivial) | `BorromeanQuark` | 11 |
| `c-from-color-flavor-swap` | PH-SM | E (physical identification) +measured-cmp | open | `CFromColorFlavorSwap` | 1 |
| `categorical-higgs-mechanism` | PH-SM | E (physical identification) | open | `CategoricalHiggsMechanism` | 1 |
| `cemetery-group-emergence` | PH-SM | E (physical identification) | open | `CemeteryGroupEmergence` | 0 |
| `color-superconductivity-borromean` | PH-SM | E (physical identification) | open | `first_order_transition` | 0 |
| `complex-chirality-rotation` | PH-SM | E (physical identification) | open | `ComplexChiralityRotation` | 1 |
| `cp-violation-spectral-form` | PH-SM | E (physical identification) | open | `CPViolationSpectralForm` | 2 |
| `cpt-d6-d7-d8-closure` | PH-SM | E (physical identification) | open | `CPTClosure` | 1 |
| `cpt-orbit-closure-density` | PH-SM | E (physical identification) | open | `cpt_orbit_closure_density` | 1 |
| `electroweak-higgs-torus-link-triplet` | PH-SM | E (physical identification) +measured-cmp | open | `EWHiggsTorusLinkTriplet` | 1 |
| `g-action-on-substrate` | PH-SM | E (physical identification) +measured-cmp | open | `GActionOnSubstrate` | 2 |
| `gauge-hecke-realization` | PH-SM | E (physical identification) | open | `GaugeHeckeRealization` | 0 |
| `hecke-anyonic-substrate` | PH-SM | E (physical identification) | open | `HeckeAnyonicSubstrate` | 8 |
| `higgs-t28` | PH-SM | E (physical identification) +measured-cmp | instance exists (check: partial/trivial) | `HiggsAsT28` | 0 |
| `n-v-bring-action` | PH-SM | E (physical identification) +measured-cmp | instance exists (check: partial/trivial) | `NVBringAction` | 2 |
| `n-v-leading-order-derivation` | PH-SM | E (physical identification) +measured-cmp | block says bridge now a theorem — still labelled conjecture (needs-owner) | `n_v_leading_order` | 1 |
| `n-v-tower-depth-ninety` | PH-SM | E (physical identification) +measured-cmp | open | `tower_depth_m_e_to_v_is_ninety` | 2 |
| `p-from-braid-mirror` | PH-SM | E (physical identification) | open | `PFromBraidMirror` | 2 |
| `sm-colour-stabilizer-action` | PH-SM | E (physical identification) +measured-cmp | open | `ColourStabilizerAction` | 2 |
| `sm-gauge-truncation` | PH-SM | E (physical identification) +measured-cmp | open | `StandardModelTruncation` | 2 |
| `sm-hypercharge-invariant` | PH-SM | E (physical identification) +measured-cmp | open | `HyperchargeInvariant` | 6 |
| `spin-from-so3-fiber` | PH-SM | E (physical identification) | open | `SpinFromSo3Fiber` | 4 |
| `symmetric-crystal-pair-production` | PH-SM | E (physical identification) | open | `SymmetricCrystalPairProduction` | 1 |
| `t-from-trace-cyclicity` | PH-SM | E (physical identification) | open | `TFromTraceCyclicity` | 1 |
| `type-b-folding-cpt` | PH-SM | E (physical identification) | open | `TypeBFoldingCpt` | 3 |
| `weak-spectral-completeness` | PH-SM | E (physical identification) +measured-cmp | open | `WeakSpectralCompleteness` | 0 |
| `weinberg-angle-categorical` | PH-SM | E (physical identification) +measured-cmp | open | `WeinbergAngleCategorical` | 4 |
| `wigner-su4-from-spin-isospin` | PH-SM | E (physical identification) +measured-cmp | open | `WignerSU4FromSpinIsospin` | 4 |
| `bohr-radius-categorical` | PH-ATOM | E (physical identification) | open | `bohr_radius_categorical` | 0 |
| `double-magic-delta-i-bound` | PH-ATOM | E (physical identification) | open | `DeltaIBoundConjecture` | 1 |
| `e-hartree-categorical-derivation` | PH-ATOM | E (physical identification) +measured-cmp | instance exists (check: partial/trivial) | `EHartreeCategoricalDerivation` | 1 |
| `h2s-angle-s3-braid-holonomy` | PH-ATOM | E (physical identification) +measured-cmp | open | `H2SAngleS3HolonomyConjecture` | 2 |
| `hydrogen-shell-writhe` | PH-ATOM | E (physical identification) | open | `hydrogen_shell_writhe` | 0 |
| `magic-numbers-bring` | PH-ATOM | E (physical identification) | open | `MagicNumbersBring` | 3 |
| `magic-numbers-from-q` | PH-ATOM | E (physical identification) +measured-cmp | open | `magic_numbers_from_q` | 5 |
| `palindromicity-orbital-type` | PH-ATOM | E (physical identification) | instance exists (check: partial/trivial) | `PalindromicityOrbitalType` | 0 |
| `shell-closure-nf-term-count` | PH-ATOM | E (physical identification) | instance exists (check: partial/trivial) | `ShellClosureNFTermCount` | 1 |
| `shell-space-is-self-square` | PH-ATOM | E (physical identification) | open | `ShellSpaceIsSelfSquare` | 0 |
| `shell-transition-knot` | PH-ATOM | E (physical identification) | open | `ShellTransitionKnot` | 1 |
| `bigbang-heatdeath` | PH-COSMO | E (physical identification) | open | `BigBangHeatDeath` | 1 |
| `casimir-epsilon-vacuum` | PH-COSMO | E (physical identification) | open | `CasimirEpsilonVacuum` | 3 |
| `casimir-first-q-correction` | PH-COSMO | E (physical identification) +measured-cmp | open | `FirstInteractingCasimirCorrection` | 0 |
| `dispersion-suppression-scale` | PH-COSMO | E (physical identification) | open | `dispersion_suppression_scale` | 1 |
| `lqg-entropy-qdim-partition-pole` | PH-COSMO | E (physical identification) | open | `LQGEntropyQDimPartitionPole` | 2 |
| `os-reflection-positivity-from-reeb` | PH-COSMO | E (physical identification) | open | `OSReflectionPositivity` | 1 |
| `q-harmonic-flow` | PH-COSMO | E (physical identification) | open | `QHarmonicFlow` | 0 |
**Lean-only or bean-only conjectures with no block:**
| conjecture | family | formal? | status | epic | Lean carrier |
|---|---|---|---|---|---|
| `VolumeConjecture41` | VOL | F | literature theorem; milestone qou-cpfn completed | CONJ-VOL | `Knot/FigureEightVolume.lean` |
| `WhiteheadVolumeConjecture` | VOL | F | open | CONJ-VOL | `Knot/WhiteheadVolumeConjecture.lean` |
| `VdVWhiteheadLemma4` | VOL | F (literature lemma) | no instance | CONJ-VOL (qou-u1b5) | `Knot/WhiteheadLinkScaffold.lean` |
| 5₂ saddle sum rule Σ Re V_j = −3π²/2 | VOL | F | open, routes 5/8/9 | CONJ-VOL (qou-0yqu) | — |
| `HypMinimizerUnique` | P3 | F (classical fact; Lean wall) | instance count 1 `[M]` | P3 (qou-r111) | `Archimedean/HyperbolicGeodesic.lean` |
| `TransferLemmas` (strong AJ 4₁) | AJ | F (published) | no instance | CONJ-AJ | `Machinery/StrongAJFigureEight.lean` |
| `JetHorizonTransfer` | PNP | F | no instance | CONJ-PNP | `Information/JetHorizonTransfer.lean` |
| `covariance_kernel_conjecture` / `KernelPincerLegs` | HECKE | F | proved k ≤ 8 | CONJ-HECKE | `BraidsAndKnots/YoungDiagramKernel*.lean` |
| Gevrey persistence (q-NS) | QNS | F | open, no carrier | CONJ-QNS | — |
| `ZToCkMappingClass`, `ProlongationPeriodMeanQuantumDim`, `BindingFollowsQBessel`, `TransferMatrixEigenphase` | P1 | F-flag (on the L2 chain) | no instance | P1 | `QBeta/…`, `Mass/…` |
| `He4DemandClosure`, `TorusKnotMass` (cj01, cj212) | PH-MASS | E | no instance | P1 | `Interactions/NuclearOperatorRegimes.lean`, `BraidKnot/TorusKnotMass.lean` |
| `conj:s5-so3-fiber-action` | PH | E | cited in 3 `.ts`, **no block** `[D §5.2]` | P1 | — |
