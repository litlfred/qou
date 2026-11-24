# Backlog Drain Batch 4 Audit & Salvage Ledger (`qou-143e`, `qou-qmh2`, `qou-rilj`)

- **Date:** 2026-11-23
- **Parent Epic:** `qou-xip2` (Repo Backlog Drain Batch 4 — Worker 39)
- **Base `origin/main` SHA Audited:** `e330ab6aa048abefe34a93474f667f3284483d71`
- **Consolidating Branch:** `claude/backlog-drain-batch4-20261123`
- **Code & Probe Commit SHA:** `0d7c8d3e77ea4ebb63f1f2e7f88f87715302de23`
- **License:** CC BY 4.0

---

## Executive Summary & Verification Gates

1. **`qou-143e` (`Q-Drain-4` — 12 child beans audited against `origin/main` `e330ab6aa04`):**
   - **3 non-conjecture child beans 100% landed -> transition to `completed`:** `qou-5lct` (PR `#9212`, `86ea08a2ed7`), `qou-h6ef` (PR `#9210`, `9ce8d04d27a`), and `qou-sbn9` (PR `#8525`, `917b6939954` + final `|μ₄/μ₃|` closed-form & producer aliases in `QOU/MassTheory/H4GPMTCumulantRatio.lean` at `0d7c8d3e77e`).
   - **9 remaining child beans narrowed with exact `origin/main` SHA evidence while strictly preserving Rule-13a conjecture guards:** `qou-xsmr`, `qou-n0so`, `qou-br4t`, `qou-yd54`, `qou-ozdk`, `qou-pg2f`, `qou-ndsa` (upgraded Mathlib `[CommRing K]`/`[IsDomain K]` LP homogeneity theorem landed in `QOU/Interactions/ConfinementLPHomogeneity.lean`), `qou-sv7h`, and `qou-s7ld` (grouped `6^A` vs `(3A)!` support & quadrangulation diagonal-split Euler invariance landed in `QOU/Hecke/LevelLocalPathSumSupport.lean`).
2. **`qou-qmh2` (`PR-Drain-4` — all 91 legacy open PRs audited: 29 in 4A + 62 in 4B):**
   - **6 PRs salvaged/upgraded onto `claude/backlog-drain-batch4-20261123`:** `#8144` (4A), `#8154` (4B, upgraded to Mathlib `[CommRing K]`/`[IsDomain K]`), `#8158` (4B, aligned `/q³` docstring with 2026-11-21 owner ruling), `#8169` (4B), `#8260` (4B), `#8268` (4B).
   - **85 PRs held/rejected with concrete static-audit & owner-ruling evidence:** 55 `Init`-only / zero-Mathlib `CommRingOps` wrappers (`lean-proof-vacuity-audit.md` §7), 20 borrowed-name 5-line `ℚ` arithmetic / software-audit wrappers, 4 retired-`z_C` toy bricks (`#8246, #8201, #8190, #8176`), 3 `X - X = 0` subtraction tautologies (`#8235, #8230, #8251`), 1 definition-collapsed CRITICAL vacuity (`#8216`), 1 `native_decide` + retired-trefoil-electron + `BraidKnot` conflict (`#8300`), and 1 contended `q0_anchor_manifest.json` overlap (`#8143`). All legacy branches preserved intact; zero legacy PRs closed prior to consolidated merge.
3. **`qou-rilj` (`Issues-Cluster-4` — all 15 open GitHub issues audited against `origin/main` `e330ab6aa04`):**
   - **1 issue closed (`100%` stated deliverables merged on `origin/main`):** `#7602` (closed citing PR `#7603`, commit `dc12b128ccc`, `folio/quantum-observable-universe/lean/QOU/QBeta/DeltaSTwoRowCharacterVanishes.lean`; parent epic `#7939` / `qou-cds1` remains open).
   - **14 issues kept open with concise status + `origin/main` SHA + tracking-bean linkage comments:** `#9002, #8923, #8903, #8898, #8867, #8866, #8801, #7967, #7965, #7939, #7751, #7713, #7711, #7678`. (`#9154` strictly untouched.)
4. **QA & Guard Verification:**
   - **Lean 4 Compilation & Kernel Axiom Check:** All 13 new `.lean` modules (93 theorems) compiled green via single-threaded `scripts/lean-direct-cone.sh -j 1` (`error=0`) and verified via kernel `#print axioms` (`0` `sorryAx`, `0` custom axioms, `0` `class` wrappers, `0` `native_decide`).
   - **Vacuity & Borrowed-Name Gates:** `scripts/lean-self-assuming-audit.py` (`0` candidates), `scripts/lean-definition-collapsed-audit.py --strict` (`0 CRITICAL, 0 advisory`), `scripts/lean-borrowed-name-audit.py` (`0 CRITICAL, 0 major, 0 advisory`).
   - **80-dps Probes & Precision Gates:** All 7 Python probes (`mpmath` `DPS = 80`) executed sequentially; all 7 `.witness.json` artifacts pass 100% of assertions (`allPassed: true`), stamp `commitSha` & `scriptCommitSha` = `0d7c8d3e77ea4ebb63f1f2e7f88f87715302de23`, and classify `Q0_OK` / `PROV_OK` / `proton-pin` with zero precision-gate defects (`qou-v0t8` contended audit witnesses left untouched).
   - **Contention & File-Guard Isolation:** Zero overlap with `#9236, #9237, #9238, #9217`, Set 1 PRs (`#9178, #9176, #9174, #8734, #8692, #8735`), `QOU.lean`, `computations/q0_anchor_manifest.json`, or protected repository root/site files.

---

## 1. `qou-143e` (`Q-Drain-4`) — 12 Child Beans Audit & Narrowing

| Bean | Current -> Target Status | Rule-13a Guard? | `origin/main` (`e330ab6aa04`) & Batch 4 Evidence |
| :--- | :--- | :--- | :--- |
| `qou-5lct` | `in-progress` -> **`completed`** | No (`0` conjectures) | **100% landed on `origin/main`** via PR `#9212` (`86ea08a2ed72aae9c26a0977e89ac52560c5d626` / `70e23fed87a`): `QOU/MathlibInfra/ConfinementLayerTower.lean` (856 lines, 0 sorry, 0 axiom, 0 class), `computations/probes/confinement_layer_tower_chem/confinement_layer_tower_chem_probe.py` + 80-dps witness, 6 monograph blocks in `molecular-construction/`, 19 bibliography entries. |
| `qou-h6ef` | `in-progress` -> **`completed`** | No (pure theorem/audit) | **100% landed on `origin/main`** via PR `#9210` (`9ce8d04d27a98bc56adc8e5f4baf27b5fe3296bf`): `QOU/MathlibInfra/NuclearChamberGS.lean` (485 lines, 0 sorry, 0 axiom, 0 class), `computations/probes/lp_bootstrap_dual_gaps/chamber_gs_model_a_b_probe.py` + `chamber-gs-model-a-b.witness.json` (80 dps: 28 Graver, 17 circuits, 27 UGB, 73 chambers, `C_phys` coincidence, 11-rule `G_phys`, `^5He` drip, Hoyle bottleneck, Mayer–Jensen `[2,6,12,8,22,32,44]`), `nuclear-chamber-groebner-basis.{md,ts}`, `nuclear-regimes-shadow-price-kinks-prior-art.{md,ts}`, and all 4 bibliography attributions. |
| `qou-sbn9` | `todo` -> **`completed`** | No (algebraic identity) | Core module `QOU/MassTheory/H4GPMTModifiedDimensionCumulants.lean` (657 lines, 0 sorry, 0 axiom, wired at `QOU.lean:1898`) + `computations/canonical_mass.py:403-479` + `computations/two_term_qed_isotope_and_nucleon_compute.py` landed on `origin/main` via PR `#8525` (`917b6939954` / `48f446490cc`); final `|μ₄/μ₃|` closed-form ratio (`mu4GPMT_H4_div_mu3GPMT_H4`, `abs_mu4GPMT_H4_div_mu3GPMT_H4`) + producer aliases landed on this branch in `QOU/MassTheory/H4GPMTCumulantRatio.lean` + `h4_gpmt_cumulant_ratio_and_lp_support_probe.py` (`0d7c8d3e77e`). |
| `qou-xsmr` | `todo` (narrowed) | Open `K >= 5` / `r(λ) >= 2` | `K=3` (`GPMTThreeRowCumulantBridge.lean`, PR `#8518` `f41c91cb7ea`) and `K=4` (`H4GPMTModifiedDimensionCumulants.lean`, PR `#8525` `917b6939954`) are on `origin/main`; `truncation_level_vs_accuracy_sweep_probe.py` and general-`K` `H_K(q)` cumulant generating function / Borel–Padé resummation (`K >= 5`, `r(λ) >= 2` onset at `K=8`) remain open (motif-level continuous extrapolation superseded by Layer-2 `ChamberGS` PR `#9210` + owner rulings `#8960`/`#8969`). |
| `qou-n0so` | `todo` (narrowed) | Open 3D α-simplex derivation | `truncation_level_vs_accuracy_sweep_probe.py` absent on `origin/main`; deriving the parameter-free 3D tetrahedral α-simplex coordination operator and Pauli content-sum quadratic asymmetry from `H_{3A}(q_0)` remains open (must respect owner rulings `#8960` nucleon-order-first and `#8969` connected-sum vs `γγ` bonding). |
| `qou-br4t` | `todo` (narrowed) | Open `4x4` Hankel proof | `QOU/Mass/QPlancherelSubNormalization.lean` (`n=2,3`) and `computations/probes/su4_occupancy_binding_probe.py` are on `origin/main`; proving the `4x4` Andréief/Cauchy–Binet Hankel determinant identity for `Z_n^(4)(q)` in Lean and rewiring `su4_occupancy_binding_mass_probe.py` remain open. |
| `qou-yd54` | `todo` (narrowed, blocked by `n0so, br4t`) | Blocked on `n0so, br4t` | Two-term QED nucleon baseline IS landed (`computations/two_term_qed_isotope_and_nucleon_compute.py`, PR `#8518`/`#8525`); wiring 3D α-simplex (`qou-n0so`) + `4x4` Hankel `Z_{3A}^(4)` (`qou-br4t`) across `Z=0..118` witnesses remains blocked on `qou-n0so` and `qou-br4t`. |
| `qou-ozdk` | `todo` (narrowed) | **Rule 13a** (reopened `qou-w12g`) | Explicitly reopened 2026-11-20 (`qou-w12g`); `QOU/Nuclear/SecondOrderGPMTCabledAlphaAndCarbon12.lean` and `second_order_gpmt_h12_carbon12_and_o16_probe.py` confirmed `MISSING` on `origin/main` (`e330ab6aa04`). |
| `qou-pg2f` | `todo` (narrowed) | **Rule 13a** (`Recursion` 0-instance guard) | `computations/alpha/alpha_cluster_recursion.py` is still actively imported by `computations/b_over_a_v5_unified.py:66` and `computations/mass_table_comprehensive.py:316` and cited in `canonical-isotope-witness.derivation.json:36`; retiring `Recursion` remains blocked on `qou-n0so`/`qou-yd54`. |
| `qou-ndsa` | `in-progress` (narrowed) | **Rule 13a** (open non-Markov objective) | Candidates 1–3 refuted on `origin/main` (`confinement_lp_braid_gram_probe.py`, `operator_selection_lp.lean`); generic Mathlib `[CommRing K]`/`[IsDomain K]` radical pairing & shadow-price uniqueness landed on this branch in `QOU/Interactions/ConfinementLPHomogeneity.lean` + `h4_gpmt_cumulant_ratio_and_lp_support_probe.py` (`0d7c8d3e77e`). Constructing a non-Markov objective breaking `<t, v> = 0` on the `A`-free `θ` curve remains open. |
| `qou-sv7h` | `in-progress` (narrowed) | **Rule 13a** (`stays open` guard) | Engineering steps 1–5 landed on `origin/main` (PRs `#6708, #6794, #6807, #6841, #7073, #7082, #7187` `8f097c192a2`, `BlockSDPNondegeneracy.lean` `dc12b128ccc`, `hecke_flint.py` `a53788c878a`); wiring `hecke_flint.py` into the production binding producer + end-to-end scaling measurement + `qou-46ys` weight reconciliation remain open. |
| `qou-s7ld` | `in-progress` (narrowed) | Open Question #2 (GP complexity) | PR `#7160` (`43e3e1b305ae`) landed `computations/chi_path_sum_seminormal.py`, and `2026-09-08-binding-word-not-level-local.md` answered Open Question #3; `QOU/Hecke/LevelLocalPathSumSupport.lean` + `h4_gpmt_cumulant_ratio_and_lp_support_probe.py` (`0d7c8d3e77e`) formalize grouped `6^A < (3A)!` support across all 32 `atom_braid_word_3A` words (Open Question #1). Open Question #2 (GP reduction complexity & downstream `deltalambda/` movement) remains open. |

### Coordinator `beans` Transition Commands (`/tmp/qou-beans-latest` left clean per protocol)

```bash
# 1. Mark 100%-landed non-conjecture child beans completed:
/Users/litlfred/.local/bin/beans update qou-5lct -s completed
/Users/litlfred/.local/bin/beans update qou-h6ef -s completed
# (After consolidating PR merges onto main, also mark qou-sbn9 completed; qou-5lct and qou-h6ef are already 100% on origin/main e330ab6aa04)
/Users/litlfred/.local/bin/beans update qou-sbn9 -s completed

# 2. Batch 4 umbrella beans (qou-143e, qou-qmh2, qou-rilj):
# - qou-rilj: 100% audited & executed (#7602 closed; 14 open issues commented with SHA + bean linkage) -> completed
/Users/litlfred/.local/bin/beans update qou-rilj -s completed
# - qou-143e & qou-qmh2: audit + salvage + ledger PR opened; transition to completed once consolidating PR merges onto main.
```

---

## 2. `qou-qmh2` (`PR-Drain-4`) — All 91 Legacy Open PRs Disposition Ledger

### 2.1 Summary by Disposition Category

| Disposition | Count | Action Policy |
| :--- | ---: | :--- |
| `SALVAGED` | 5 | Clean Lean 4 + 80-dps probe deliverables landed on `claude/backlog-drain-batch4-20261123` (`#8144, #8158, #8169, #8260, #8268`). Close legacy PRs **only after** consolidating PR merges; preserve branches intact. |
| `SALVAGED_UPGRADED` | 1 | Upgraded from toy `Int`/`Rat` structs to Mathlib `[CommRing K]`/`[IsDomain K]` + 80-dps probe (`#8154`). Close **only after** consolidating PR merges; preserve branch intact. |
| `HOLD_CONTENDED_MANIFEST` | 1 | `#8143` touches contended `computations/q0_anchor_manifest.json` (`#9237, #9238`); held untouched. |
| `HOLD_RETIRED_ZC_BRICK` | 4 | `#8246, #8201, #8190, #8176` reference retired `z_C` observable (owner ruling 2026-11-22) in toy `ℚ`/`ℝ` wrappers; do not salvage. |
| `REJECT_NO_IMPORT_WRAPPER` | 55 | `Init`-only / zero-Mathlib `CommRingOps` wrappers violating `lean-proof-vacuity-audit.md` §7 (`lean-borrowed-name-audit.py` CRITICAL/major); do not merge. |
| `REJECT_BORROWED_NAME_BRICK` | 20 | 5-line `ℚ` arithmetic / software-audit counter wrappers (`lean-proof-vacuity-audit.md` §7); underlying audit prose already on `origin/main` in `docs/audits/`. |
| `REJECT_SUB_ZERO_TAUTOLOGY` | 3 | `#8235, #8230, #8251` contain `X - X = 0` subtraction tautologies (`SUB_ZERO_SHAPE`). |
| `REJECT_COLLAPSED_VACUOUS` | 1 | `#8216` fails `lean-definition-collapsed-audit.py` with **2 CRITICAL** (`NO_IMPORTS`). |
| `REJECT_RULING_AND_VACUITY` | 1 | `#8300` uses `native_decide`, `True` trivialities, retired trefoil-electron framing, and modifies 4 `BraidKnot` files. |
| **Total** | **91** | **29 in 4A + 62 in 4B — 0 branches deleted** |

### 2.2 Complete 91-PR Table (`4A` + `4B`)

| PR | Sub-batch | Head Branch (Preserved Intact) | Disposition | Audit Evidence |
| :--- | :---: | :--- | :--- | :--- |
| `#8512` | `4A` | `cat/round88-triangulation3dindex-helicityparity-blochk3torsion-immirzihorizontower-strangeidentityscope-bridge` | `REJECT_NO_IMPORT_WRAPPER` | `Init`-only / zero-Mathlib `CommRingOps` wrapper (`lean-proof-vacuity-audit.md` §7, `lean-borrowed-name-audit.py` CRITICAL/major). |
| `#8493` | `4A` | `cat/round85-stateintegral-habiro-apoly-voldeg-qairy-bridge` | `REJECT_NO_IMPORT_WRAPPER` | `Init`-only / zero-Mathlib `CommRingOps` wrapper (`lean-proof-vacuity-audit.md` §7, `lean-borrowed-name-audit.py` CRITICAL/major). |
| `#8484` | `4A` | `cat/round84-slash-median-curvechange-lengthmeasure-ellipticbundle-bridge` | `REJECT_NO_IMPORT_WRAPPER` | `Init`-only / zero-Mathlib `CommRingOps` wrapper (`lean-proof-vacuity-audit.md` §7, `lean-borrowed-name-audit.py` CRITICAL/major). |
| `#8479` | `4A` | `cat/round83-venue-levelfour-unipotent-rational-pairpartition-bridge` | `REJECT_NO_IMPORT_WRAPPER` | `Init`-only / zero-Mathlib `CommRingOps` wrapper (`lean-proof-vacuity-audit.md` §7, `lean-borrowed-name-audit.py` CRITICAL/major). |
| `#8477` | `4A` | `cat/round82-quotient-plumbed-baryogenesis-qstokes-dualizing-bridge` | `REJECT_NO_IMPORT_WRAPPER` | `Init`-only / zero-Mathlib `CommRingOps` wrapper (`lean-proof-vacuity-audit.md` §7, `lean-borrowed-name-audit.py` CRITICAL/major). |
| `#8470` | `4A` | `cat/round81-pentagon-octahedral-dilog-fakecurv-bilateral-bridge` | `REJECT_NO_IMPORT_WRAPPER` | `Init`-only / zero-Mathlib `CommRingOps` wrapper (`lean-proof-vacuity-audit.md` §7, `lean-borrowed-name-audit.py` CRITICAL/major). |
| `#8465` | `4A` | `cat/round80-biotsavart-icosahedral-tracefield-planck-eigenspace` | `REJECT_NO_IMPORT_WRAPPER` | `Init`-only / zero-Mathlib `CommRingOps` wrapper (`lean-proof-vacuity-audit.md` §7, `lean-borrowed-name-audit.py` CRITICAL/major). |
| `#8460` | `4A` | `cat/round79-bring-congruence-minvol-vortex-qdilog` | `REJECT_NO_IMPORT_WRAPPER` | `Init`-only / zero-Mathlib `CommRingOps` wrapper (`lean-proof-vacuity-audit.md` §7, `lean-borrowed-name-audit.py` CRITICAL/major). |
| `#8458` | `4A` | `cat/round78-depth-filtration-angled-gluing-mpv-helicity` | `REJECT_NO_IMPORT_WRAPPER` | `Init`-only / zero-Mathlib `CommRingOps` wrapper (`lean-proof-vacuity-audit.md` §7, `lean-borrowed-name-audit.py` CRITICAL/major). |
| `#8262` | `4A` | `feat/qou-r9ih-2row-301d-3wvl-k00d-t7az` | `REJECT_BORROWED_NAME_BRICK` | 5-line `ℚ` arithmetic / software-audit counter wrapper (`lean-proof-vacuity-audit.md` §7 borrowed-name toy wrapper; audit facts already in `docs/audits/`). |
| `#8258` | `4A` | `feat/qou-r9ih-0g4z-mo1n-qsns-sib1-yvyd` | `REJECT_BORROWED_NAME_BRICK` | 5-line `ℚ` arithmetic / software-audit counter wrapper (`lean-proof-vacuity-audit.md` §7 borrowed-name toy wrapper; audit facts already in `docs/audits/`). |
| `#8256` | `4A` | `feat/qou-r9ih-2w6j-c9fh-dku0-n5vg-pwgw` | `REJECT_BORROWED_NAME_BRICK` | 5-line `ℚ` arithmetic / software-audit counter wrapper (`lean-proof-vacuity-audit.md` §7 borrowed-name toy wrapper; audit facts already in `docs/audits/`). |
| `#8252` | `4A` | `feat/qou-r9ih-3jgd-5b23-d8as-j1ld-s8gi` | `REJECT_BORROWED_NAME_BRICK` | 5-line `ℚ` arithmetic / software-audit counter wrapper (`lean-proof-vacuity-audit.md` §7 borrowed-name toy wrapper; audit facts already in `docs/audits/`). |
| `#8246` | `4A` | `feat/qou-r9ih-b5h9-lrvc-p443-vged-w1tz` | `HOLD_RETIRED_ZC_BRICK` | References retired `z_C` observable (owner ruling 2026-11-22) + toy `ℚ`/`ℝ` brick wrapper. |
| `#8240` | `4A` | `feat/qou-r9ih-0y6l-amvt-fv70-j6mp-mokg` | `REJECT_BORROWED_NAME_BRICK` | 5-line `ℚ` arithmetic / software-audit counter wrapper (`lean-proof-vacuity-audit.md` §7 borrowed-name toy wrapper; audit facts already in `docs/audits/`). |
| `#8236` | `4A` | `feat/qou-3ent-l15q-q05m-dt14-n2cl-round52` | `REJECT_NO_IMPORT_WRAPPER` | `Init`-only / zero-Mathlib `CommRingOps` wrapper (`lean-proof-vacuity-audit.md` §7, `lean-borrowed-name-audit.py` CRITICAL/major) + modifies `StokesDTBPSBridge.lean`. |
| `#8235` | `4A` | `feat/qou-r9ih-h7yk-krvm-kyst-lbth-o41q` | `REJECT_SUB_ZERO_TAUTOLOGY` | `SUB_ZERO_SHAPE` (`X - X = 0` subtraction tautology) + toy `ℚ` brick wrapper (§7). |
| `#8233` | `4A` | `feat/qou-r9ih-03lh-7b7v-gkco-icx5-q04o` | `REJECT_BORROWED_NAME_BRICK` | 5-line `ℚ` arithmetic / software-audit counter wrapper (`lean-proof-vacuity-audit.md` §7 borrowed-name toy wrapper; audit facts already in `docs/audits/`). |
| `#8230` | `4A` | `feat/qou-r9ih-524t-7xvy-f7g2-l6fz-odh5` | `REJECT_SUB_ZERO_TAUTOLOGY` | `SUB_ZERO_SHAPE` (`X - X = 0` subtraction tautology) + toy `ℚ` brick wrapper (§7). |
| `#8228` | `4A` | `feat/qou-9y43-af91-i7rk-oots-ae6l-round51` | `REJECT_NO_IMPORT_WRAPPER` | `Init`-only / zero-Mathlib `CommRingOps` wrapper (`lean-proof-vacuity-audit.md` §7, `lean-borrowed-name-audit.py` CRITICAL/major). |
| `#8224` | `4A` | `feat/qou-r9ih-cons-jplv-lv34-q95i-uvqk` | `REJECT_BORROWED_NAME_BRICK` | 5-line `ℚ` arithmetic / software-audit counter wrapper (`lean-proof-vacuity-audit.md` §7 borrowed-name toy wrapper; audit facts already in `docs/audits/`). |
| `#8220` | `4A` | `feat/qou-r9ih-a0li-cqup-vlow-ylma-zuuz` | `REJECT_BORROWED_NAME_BRICK` | 5-line `ℚ` arithmetic / software-audit counter wrapper (`lean-proof-vacuity-audit.md` §7 borrowed-name toy wrapper; audit facts already in `docs/audits/`). |
| `#8217` | `4A` | `feat/qou-r9ih-i9xj-r4ya-xsv8-xzlt-y3xv` | `REJECT_BORROWED_NAME_BRICK` | 5-line `ℚ` arithmetic / software-audit counter wrapper (`lean-proof-vacuity-audit.md` §7 borrowed-name toy wrapper; audit facts already in `docs/audits/`). |
| `#8212` | `4A` | `feat/qou-r9ih-985x-adgd-epy2-kifs-xblo` | `REJECT_BORROWED_NAME_BRICK` | 5-line `ℚ` arithmetic / software-audit counter wrapper (`lean-proof-vacuity-audit.md` §7 borrowed-name toy wrapper; audit facts already in `docs/audits/`). |
| `#8210` | `4A` | `feat/qou-r9ih-dizz-obmp-q86o-r1si-rlkw` | `REJECT_BORROWED_NAME_BRICK` | 5-line `ℚ` arithmetic / software-audit counter wrapper (`lean-proof-vacuity-audit.md` §7 borrowed-name toy wrapper; audit facts already in `docs/audits/`). |
| `#8208` | `4A` | `feat/qou-r9ih-oq8a-cw27-fuz1-ic22-x7h8` | `REJECT_BORROWED_NAME_BRICK` | 5-line `ℚ` arithmetic / software-audit counter wrapper (`lean-proof-vacuity-audit.md` §7 borrowed-name toy wrapper; audit facts already in `docs/audits/`). |
| `#8177` | `4A` | `feat/qou-ztod-15sj-5ipv-gwio-gbsa-round50` | `REJECT_NO_IMPORT_WRAPPER` | `Init`-only / zero-Mathlib `CommRingOps` wrapper (`lean-proof-vacuity-audit.md` §7, `lean-borrowed-name-audit.py` CRITICAL/major). |
| `#8156` | `4A` | `feat/alpha-em-propagator-hodge-h3-green` | `REJECT_NO_IMPORT_WRAPPER` | `Init`-only / zero-Mathlib `CommRingOps` wrapper (`lean-proof-vacuity-audit.md` §7, `lean-borrowed-name-audit.py` CRITICAL/major). |
| `#8144` | `4A` | `claude/round46-q-10v9-4` | `SALVAGED` | Upgraded CC BY 4.0 headers; landed `QOU/QBeta/JointOhtsukiGradedTower.lean` + `QOU/QBeta/QHeatKernelHabiroExpansion.lean` + 2 80-dps probes (`qou-7jok, qou-8ex3`). |
| `#8492` | `4B` | `feat/qou-ar7f-citp-dgw2-vyij-x6q0` | `REJECT_NO_IMPORT_WRAPPER` | `Init`-only / zero-Mathlib `CommRingOps` wrapper (`lean-proof-vacuity-audit.md` §7, `lean-borrowed-name-audit.py` CRITICAL/major). |
| `#8487` | `4B` | `feat/qou-8ed2-markov-60iz-6chz-hhl9` | `REJECT_NO_IMPORT_WRAPPER` | `Init`-only / zero-Mathlib `CommRingOps` wrapper (`lean-proof-vacuity-audit.md` §7, `lean-borrowed-name-audit.py` CRITICAL/major). |
| `#8481` | `4B` | `feat/qou-vkv7-mybv-us0a-jbfx-z4jb` | `REJECT_NO_IMPORT_WRAPPER` | `Init`-only / zero-Mathlib `CommRingOps` wrapper (`lean-proof-vacuity-audit.md` §7, `lean-borrowed-name-audit.py` CRITICAL/major). |
| `#8474` | `4B` | `feat/qou-58rx-hprp-y3x4-yl86-zatj` | `REJECT_NO_IMPORT_WRAPPER` | `Init`-only / zero-Mathlib `CommRingOps` wrapper (`lean-proof-vacuity-audit.md` §7, `lean-borrowed-name-audit.py` CRITICAL/major). |
| `#8471` | `4B` | `feat/qou-95jh-b3pe-cnd4-1n7g-24m2` | `REJECT_NO_IMPORT_WRAPPER` | `Init`-only / zero-Mathlib `CommRingOps` wrapper (`lean-proof-vacuity-audit.md` §7, `lean-borrowed-name-audit.py` CRITICAL/major). |
| `#8469` | `4B` | `feat/qou-wsx3-6x4m-pusy-j4mn-tp56` | `REJECT_NO_IMPORT_WRAPPER` | `Init`-only / zero-Mathlib `CommRingOps` wrapper (`lean-proof-vacuity-audit.md` §7, `lean-borrowed-name-audit.py` CRITICAL/major). |
| `#8463` | `4B` | `feat/qou-p68e-qe41-si72-sycn-u87j` | `REJECT_NO_IMPORT_WRAPPER` | `Init`-only / zero-Mathlib `CommRingOps` wrapper (`lean-proof-vacuity-audit.md` §7, `lean-borrowed-name-audit.py` CRITICAL/major). |
| `#8451` | `4B` | `feat/qou-2u26-42ls-5po6-8s7o-aqyf` | `REJECT_NO_IMPORT_WRAPPER` | `Init`-only / zero-Mathlib `CommRingOps` wrapper (`lean-proof-vacuity-audit.md` §7, `lean-borrowed-name-audit.py` CRITICAL/major). |
| `#8446` | `4B` | `feat/qou-xc8t-cdup-qdzu-9e7p-c98z` | `REJECT_NO_IMPORT_WRAPPER` | `Init`-only / zero-Mathlib `CommRingOps` wrapper (`lean-proof-vacuity-audit.md` §7, `lean-borrowed-name-audit.py` CRITICAL/major). |
| `#8441` | `4B` | `feat/qou-71ma-n226-oilr-omuz-wxmm` | `REJECT_NO_IMPORT_WRAPPER` | `Init`-only / zero-Mathlib `CommRingOps` wrapper (`lean-proof-vacuity-audit.md` §7, `lean-borrowed-name-audit.py` CRITICAL/major). |
| `#8437` | `4B` | `feat/qou-rttg-50vf-aezg-dcvv-fwah` | `REJECT_NO_IMPORT_WRAPPER` | `Init`-only / zero-Mathlib `CommRingOps` wrapper (`lean-proof-vacuity-audit.md` §7, `lean-borrowed-name-audit.py` CRITICAL/major). |
| `#8433` | `4B` | `feat/qou-bwrt-bwse-rtkb-rtqd-rtrb` | `REJECT_NO_IMPORT_WRAPPER` | `Init`-only / zero-Mathlib `CommRingOps` wrapper (`lean-proof-vacuity-audit.md` §7, `lean-borrowed-name-audit.py` CRITICAL/major). |
| `#8430` | `4B` | `feat/qou-ix9e-lncp-ulfe-znz5-pso0` | `REJECT_NO_IMPORT_WRAPPER` | `Init`-only / zero-Mathlib `CommRingOps` wrapper (`lean-proof-vacuity-audit.md` §7, `lean-borrowed-name-audit.py` CRITICAL/major). |
| `#8409` | `4B` | `feat/qou-gmfz-img9-phir-siin-l25z` | `REJECT_NO_IMPORT_WRAPPER` | `Init`-only / zero-Mathlib `CommRingOps` wrapper (`lean-proof-vacuity-audit.md` §7, `lean-borrowed-name-audit.py` CRITICAL/major). |
| `#8390` | `4B` | `feat/qou-sx5r-slck-dgsw-jfr8-zoyv` | `REJECT_NO_IMPORT_WRAPPER` | `Init`-only / zero-Mathlib `CommRingOps` wrapper (`lean-proof-vacuity-audit.md` §7, `lean-borrowed-name-audit.py` CRITICAL/major). |
| `#8382` | `4B` | `feat/qou-c3if-7028-bt3u-mp3m-ga7i` | `REJECT_NO_IMPORT_WRAPPER` | `Init`-only / zero-Mathlib `CommRingOps` wrapper (`lean-proof-vacuity-audit.md` §7, `lean-borrowed-name-audit.py` CRITICAL/major). |
| `#8377` | `4B` | `feat/qou-0w3s-kr8a-o3so-zko1-brt1` | `REJECT_NO_IMPORT_WRAPPER` | `Init`-only / zero-Mathlib `CommRingOps` wrapper (`lean-proof-vacuity-audit.md` §7, `lean-borrowed-name-audit.py` CRITICAL/major). |
| `#8346` | `4B` | `feat/qou-7crn-7gei-qua1-s7z2-tqab` | `REJECT_NO_IMPORT_WRAPPER` | `Init`-only / zero-Mathlib `CommRingOps` wrapper (`lean-proof-vacuity-audit.md` §7, `lean-borrowed-name-audit.py` CRITICAL/major). |
| `#8341` | `4B` | `qou-10v9-exam-f0ny-f64g-f7af-fl9i` | `REJECT_NO_IMPORT_WRAPPER` | `Init`-only / zero-Mathlib `CommRingOps` wrapper (`lean-proof-vacuity-audit.md` §7, `lean-borrowed-name-audit.py` CRITICAL/major). |
| `#8331` | `4B` | `feat/qou-68e1-mhx0-pha4-xyxc-zwzd` | `REJECT_NO_IMPORT_WRAPPER` | `Init`-only / zero-Mathlib `CommRingOps` wrapper (`lean-proof-vacuity-audit.md` §7, `lean-borrowed-name-audit.py` CRITICAL/major). |
| `#8310` | `4B` | `feat/qou-nuxb-vvk7-wdgz-x1rm-yc05` | `REJECT_NO_IMPORT_WRAPPER` | `Init`-only / zero-Mathlib `CommRingOps` wrapper (`lean-proof-vacuity-audit.md` §7, `lean-borrowed-name-audit.py` CRITICAL/major). |
| `#8303` | `4B` | `feat/qou-jvua-kp89-m8xt-mame-u4mx` | `REJECT_NO_IMPORT_WRAPPER` | `Init`-only / zero-Mathlib `CommRingOps` wrapper (`lean-proof-vacuity-audit.md` §7, `lean-borrowed-name-audit.py` CRITICAL/major). |
| `#8300` | `4B` | `feat/round71-deltalambda-idempotent-ajtrefoil-n5-gbdepth-43c1` | `REJECT_RULING_AND_VACUITY` | `HAS_NATIVE_DECIDE`, `TRIVIAL_TRUE`, retired trefoil-electron primary framing, modifies 4 main `BraidKnot` files. |
| `#8299` | `4B` | `feat/qou-argp-bp5n-ghc6-h2mb-i0sr` | `REJECT_NO_IMPORT_WRAPPER` | `Init`-only / zero-Mathlib `CommRingOps` wrapper (`lean-proof-vacuity-audit.md` §7, `lean-borrowed-name-audit.py` CRITICAL/major). |
| `#8295` | `4B` | `feat/qou-j16x-hu1f-onfk-v8ct-nvoq` | `REJECT_NO_IMPORT_WRAPPER` | `Init`-only / zero-Mathlib `CommRingOps` wrapper (`lean-proof-vacuity-audit.md` §7, `lean-borrowed-name-audit.py` CRITICAL/major). |
| `#8291` | `4B` | `feat/qou-322e-4tsl-5gai-7y3g-9h4t` | `REJECT_NO_IMPORT_WRAPPER` | `Init`-only / zero-Mathlib `CommRingOps` wrapper (`lean-proof-vacuity-audit.md` §7, `lean-borrowed-name-audit.py` CRITICAL/major). |
| `#8276` | `4B` | `feat/qou-59vq-1o8n-1oif-1wcu-6ers` | `REJECT_NO_IMPORT_WRAPPER` | `Init`-only / zero-Mathlib `CommRingOps` wrapper (`lean-proof-vacuity-audit.md` §7, `lean-borrowed-name-audit.py` CRITICAL/major). |
| `#8268` | `4B` | `feat/qou-gw96-nlw5-pjx4-u5qs-xwur` | `SALVAGED` | Landed 3 `QOU/MassTheory/` modules (`ContiguousLayoutAndTwoRowIsospinChannel`, `DeltaBarOddnessAndInterfaceAnchorGap`, `StackedCrossingWritheFramingFlip`) + 80-dps probe (`qou-gw96, qou-nlw5, qou-pjx4, qou-u5qs, qou-xwur`). |
| `#8265` | `4B` | `feat/qou-ls86-q6pp-q7ga-rwhv-xzda` | `REJECT_BORROWED_NAME_BRICK` | 5-line `ℚ` arithmetic / software-audit counter wrapper (`lean-proof-vacuity-audit.md` §7 borrowed-name toy wrapper; audit facts already in `docs/audits/`). |
| `#8260` | `4B` | `feat/qou-im4m-kgsx-lr57-mbbf-qlma` | `SALVAGED` | Landed 3 `QOU/MassTheory/` modules (`MirrorBarCancellationAndTwoRowCapRatio`, `NucleonCrossingCountsAndClosureLaw`, `NucleonScaleEnergyAndRatioInvariance`) + 80-dps probe (`qou-im4m, qou-kgsx, qou-lr57, qou-mbbf, qou-qlma`). |
| `#8254` | `4B` | `feat/qou-utb3-w4la-k4oq-o9ge-0cyu` | `REJECT_NO_IMPORT_WRAPPER` | `Init`-only / zero-Mathlib `CommRingOps` wrapper (`lean-proof-vacuity-audit.md` §7, `lean-borrowed-name-audit.py` CRITICAL/major). |
| `#8251` | `4B` | `feat/qou-04cj-2vut-6xvw-8ms1-9ilw` | `REJECT_SUB_ZERO_TAUTOLOGY` | `SUB_ZERO_SHAPE` (`X - X = 0` subtraction tautology) + toy `ℚ` brick wrapper (§7). |
| `#8241` | `4B` | `feat/symplectic-atomicity-wenzl-semisimplicity-atsd-dyij-cc97-otbb-e4ri` | `REJECT_NO_IMPORT_WRAPPER` | `Init`-only / zero-Mathlib `CommRingOps` wrapper (`lean-proof-vacuity-audit.md` §7, `lean-borrowed-name-audit.py` CRITICAL/major). |
| `#8237` | `4B` | `feat/bar-condition-hyperbolic-spherical-metric-7cmk-7t1n-b84o-c8p8-sd8y` | `REJECT_NO_IMPORT_WRAPPER` | `Init`-only / zero-Mathlib `CommRingOps` wrapper (`lean-proof-vacuity-audit.md` §7, `lean-borrowed-name-audit.py` CRITICAL/major). |
| `#8234` | `4B` | `feat/specht-h4-markov-cascade-npvy-1jrr-8hm1-t7zg-xzd5` | `REJECT_NO_IMPORT_WRAPPER` | `Init`-only / zero-Mathlib `CommRingOps` wrapper (`lean-proof-vacuity-audit.md` §7, `lean-borrowed-name-audit.py` CRITICAL/major). |
| `#8229` | `4B` | `qou-8lxd-skgn-jk6g-3oi0-qneo-x4qm` | `REJECT_NO_IMPORT_WRAPPER` | `Init`-only / zero-Mathlib `CommRingOps` wrapper (`lean-proof-vacuity-audit.md` §7, `lean-borrowed-name-audit.py` CRITICAL/major). |
| `#8227` | `4B` | `feat/zeta4-generic-ring-plancherel-5lcg-oc4v-r7qm-xbyp-sf1t` | `REJECT_NO_IMPORT_WRAPPER` | `Init`-only / zero-Mathlib `CommRingOps` wrapper (`lean-proof-vacuity-audit.md` §7, `lean-borrowed-name-audit.py` CRITICAL/major). |
| `#8223` | `4B` | `claude/qou-rtxm-calibration-jm-gibbs-bar-poincare-2026-11-17` | `REJECT_NO_IMPORT_WRAPPER` | `Init`-only / zero-Mathlib `CommRingOps` wrapper (`lean-proof-vacuity-audit.md` §7, `lean-borrowed-name-audit.py` CRITICAL/major). |
| `#8216` | `4B` | `qou-8lxd-3xsv-6x01-nrty-vnct-vs2i` | `REJECT_COLLAPSED_VACUOUS` | `lean-definition-collapsed-audit.py`: 2 CRITICAL (`nucleon_doublet_writhe_rotation_gap`, `shell_capacity_subshell_sum_and_zero_duality_gap`) + `NO_IMPORTS`. |
| `#8214` | `4B` | `claude/qou-rtxm-conventiond-keystone-trace-tower-2026-11-16` | `REJECT_NO_IMPORT_WRAPPER` | `Init`-only / zero-Mathlib `CommRingOps` wrapper (`lean-proof-vacuity-audit.md` §7, `lean-borrowed-name-audit.py` CRITICAL/major). |
| `#8204` | `4B` | `feat/qou-frzo-qb99-ratf-ri9w-rsrg-u7hx` | `REJECT_BORROWED_NAME_BRICK` | 5-line `ℚ` arithmetic / software-audit counter wrapper (`lean-proof-vacuity-audit.md` §7 borrowed-name toy wrapper; audit facts already in `docs/audits/`). |
| `#8201` | `4B` | `feat/qou-frzo-vnik-wgnx-xi16-xufp-yju0` | `HOLD_RETIRED_ZC_BRICK` | References retired `z_C` observable (owner ruling 2026-11-22) + toy `ℚ`/`ℝ` brick wrapper. |
| `#8195` | `4B` | `feat/qou-frzo-gh6m-jwbq-qbe9x-qbf0-slvl` | `REJECT_BORROWED_NAME_BRICK` | 5-line `ℚ` arithmetic / software-audit counter wrapper (`lean-proof-vacuity-audit.md` §7 borrowed-name toy wrapper; audit facts already in `docs/audits/`). |
| `#8194` | `4B` | `feat/qou-frzo-ailp-ar4v-cvst-ei4q-hmrm` | `REJECT_BORROWED_NAME_BRICK` | 5-line `ℚ` arithmetic / software-audit counter wrapper (`lean-proof-vacuity-audit.md` §7 borrowed-name toy wrapper; audit facts already in `docs/audits/`). |
| `#8191` | `4B` | `feat/qou-frzo-8we6-2qt2-3cgi-3qla-6hzr` | `REJECT_BORROWED_NAME_BRICK` | 5-line `ℚ` arithmetic / software-audit counter wrapper (`lean-proof-vacuity-audit.md` §7 borrowed-name toy wrapper; audit facts already in `docs/audits/`). |
| `#8190` | `4B` | `feat/qou-9nnz-09lg-1fhe-1lr8-47sx-4fj6` | `HOLD_RETIRED_ZC_BRICK` | References retired `z_C` observable (owner ruling 2026-11-22) + toy `ℚ`/`ℝ` brick wrapper. |
| `#8188` | `4B` | `feat/qou-2002-46ke-inkh-1c4y-q0dr-q0lp` | `REJECT_BORROWED_NAME_BRICK` | 5-line `ℚ` arithmetic / software-audit counter wrapper (`lean-proof-vacuity-audit.md` §7 borrowed-name toy wrapper; audit facts already in `docs/audits/`). |
| `#8185` | `4B` | `qou-8lxd-17gn-37y0-8pl2-htk4-nxvg` | `REJECT_NO_IMPORT_WRAPPER` | `Init`-only / zero-Mathlib `CommRingOps` wrapper (`lean-proof-vacuity-audit.md` §7, `lean-borrowed-name-audit.py` CRITICAL/major). |
| `#8184` | `4B` | `feat/qou-2002-9ugp-bypn-c4kv-9idb-515v` | `REJECT_BORROWED_NAME_BRICK` | 5-line `ℚ` arithmetic / software-audit counter wrapper (`lean-proof-vacuity-audit.md` §7 borrowed-name toy wrapper; audit facts already in `docs/audits/`). |
| `#8182` | `4B` | `feat/qou-2002-2t9y-2whe-qyef-o922-tekx` | `REJECT_BORROWED_NAME_BRICK` | 5-line `ℚ` arithmetic / software-audit counter wrapper (`lean-proof-vacuity-audit.md` §7 borrowed-name toy wrapper; audit facts already in `docs/audits/`). |
| `#8176` | `4B` | `feat/qou-2002-72rd-mha1-3zby-dau6-5op4` | `HOLD_RETIRED_ZC_BRICK` | References retired `z_C` observable (owner ruling 2026-11-22) + toy `ℚ`/`ℝ` brick wrapper. |
| `#8169` | `4B` | `feat/qou-2002-24w9-r0dn-hgm6-cuur-zufe` | `SALVAGED` | Landed `QOU/MassTheory/PlancherelNormalisationAndScaleBounds.lean` + 80-dps probe (`qou-24w9, qou-r0dn, qou-hgm6, qou-cuur, qou-zufe`). |
| `#8166` | `4B` | `claude/qou-rtxm-conventiond-frobenius-tower-2026-11-16` | `REJECT_NO_IMPORT_WRAPPER` | `Init`-only / zero-Mathlib `CommRingOps` wrapper (`lean-proof-vacuity-audit.md` §7, `lean-borrowed-name-audit.py` CRITICAL/major). |
| `#8158` | `4B` | `feat/qou-2002-1u7x-cweq-ovud-i5p0-cgbd` | `SALVAGED` | Aligned `/q^3` docstring with 2026-11-21 owner ruling; landed `QOU/Observations/SubstrateParameterLocality.lean` + 80-dps probe (`qou-1u7x, qou-cweq, ovud, i5p0, qou-cgbd`). |
| `#8157` | `4B` | `claude/qou-rtxm-foundations-bridge-2026-11-16` | `REJECT_NO_IMPORT_WRAPPER` | `Init`-only / zero-Mathlib `CommRingOps` wrapper (`lean-proof-vacuity-audit.md` §7, `lean-borrowed-name-audit.py` CRITICAL/major). |
| `#8154` | `4B` | `feat/qou-zrx2-9yt9-ndsa-s7ld-brfy` | `SALVAGED_UPGRADED` | Upgraded toy `Int`/`Rat` structs to Mathlib `[CommRing K]`/`[IsDomain K]`; landed `QOU/Interactions/ConfinementLPHomogeneity.lean` + `QOU/Hecke/LevelLocalPathSumSupport.lean` + 80-dps probe (`qou-ndsa, qou-s7ld, qou-brfy`). |
| `#8150` | `4B` | `feat/bring-lifting-obstruction-routes-z2-vs-z` | `REJECT_NO_IMPORT_WRAPPER` | `Init`-only / zero-Mathlib `CommRingOps` wrapper (`lean-proof-vacuity-audit.md` §7, `lean-borrowed-name-audit.py` CRITICAL/major). |
| `#8148` | `4B` | `claude/qou-9634-ep0a-kz-markov-tower-2026-11-16` | `REJECT_NO_IMPORT_WRAPPER` | `Init`-only / zero-Mathlib `CommRingOps` wrapper (`lean-proof-vacuity-audit.md` §7, `lean-borrowed-name-audit.py` CRITICAL/major). |
| `#8143` | `4B` | `feat/qou-wp3h-d2-yekutieli-stokes-2026-11-16` | `HOLD_CONTENDED_MANIFEST` | Overlaps guarded `computations/q0_anchor_manifest.json` (`#9237, #9238`). |
| `#8141` | `4B` | `claude/qou-3l2l-mxnu-vbz4-2026-11-16` | `REJECT_NO_IMPORT_WRAPPER` | `Init`-only / zero-Mathlib `CommRingOps` wrapper (`lean-proof-vacuity-audit.md` §7, `lean-borrowed-name-audit.py` CRITICAL/major). |
| `#8140` | `4B` | `qou-8lxd-q6lw-tekm-probes-lean` | `REJECT_NO_IMPORT_WRAPPER` | `Init`-only / zero-Mathlib `CommRingOps` wrapper (`lean-proof-vacuity-audit.md` §7, `lean-borrowed-name-audit.py` CRITICAL/major). |
| `#8139` | `4B` | `claude/r46-ni4b-tqcp-colour-tower-cp` | `REJECT_NO_IMPORT_WRAPPER` | `Init`-only / zero-Mathlib `CommRingOps` wrapper (`lean-proof-vacuity-audit.md` §7, `lean-borrowed-name-audit.py` CRITICAL/major). |

### 2.3 Post-Merge Supersede Commands (Run ONLY After Consolidating PR Merges; NEVER Pass `--delete-branch`)

```bash
# After consolidating PR merges onto main (replace <CONSOLIDATED_PR> and <MERGE_SHA>):
for pr in 8144 8154 8158 8169 8260 8268; do
  gh pr close "$pr" --repo litlfred/qou --comment "Salvaged and upgraded in consolidated Batch 4 PR #<CONSOLIDATED_PR> (merged at <MERGE_SHA>; see docs/audits/2026-11-23-backlog-drain-batch4-ledger.md). Head branch preserved intact."
done
```

---

## 3. `qou-rilj` (`Issues-Cluster-4`) — All 15 GitHub Issues Audit & Actions

| Issue | Title (Abbreviated) | Action | `origin/main` (`e330ab6aa04`) Evidence & Tracking Beans |
| :--- | :--- | :--- | :--- |
| `#7602` | `Lean: χ_(2,1)(Δ_S) = 0 — single-wrap element invisible to two-row block (qou-cds1)` | **CLOSE** | **100% stated deliverables merged** in PR `#7603` (`dc12b128cccca6d1ca1989a2520e719c226253c7`, verified green at `e330ab6aa04`): `folio/quantum-observable-universe/lean/QOU/QBeta/DeltaSTwoRowCharacterVanishes.lean` (`trace_deltaS_eq_zero`, `s1_quadratic`, `s2_quadratic`, `braid`, `h_sub_zD`, `chi21_deltaS_eq_zero`, 0 sorry, 0 axiom, 0 class). Parent epic `#7939` (`qou-cds1`) stays open. |
| `#9002` | `derive E_0 = m_μ · ℏ_q² / Vol(4_1) from q=1 masslessness` | **KEEP OPEN** (commented) | Partial: PR `#8955` (`99bee4ec078`) landed `QOU/QBeta/E0MuonUnit.lean`. Open: W6 `𝔈 -> MeV` scale and `m_p = m_n` at `q=1` outside braid-built terms (`qou-az9l`, `qou-91w7`). |
| `#8923` | `pairSkein_eq_trace proves pair-skein IS trace under D — restate or retire` | **KEEP OPEN** (commented) | Partial: PRs `#8904` (`bee81703f3a`) & `#8955` (`99bee4ec078`) proved `pairSkein_eq_trace` in `QOU/QBeta/CrossingTraceWeights.lean`. Open: monograph blocks `pair-skein-mass-formula.md` & `terminal-resolution.md` still carry convention-C framing awaiting restatement. |
| `#8903` | `derive energy map E(B) = -E_0 · ln ⟨B⟩ from multiplicativity` | **KEEP OPEN** (commented) | Partial: PR `#8904` (`bee81703f3a`) landed spectator-invariance log map + `docs/audits/2026-11-21-qbeta-energy-map-spectator.md`. Open: observable assignment of `2 E_0 ln q` and W6 `𝔈 -> MeV` scale (owner rulings 2026-11-21/22). |
| `#8898` | `why m_e enters n–p mass difference — forced normalisation vs Q_β` | **KEEP OPEN** (commented) | Open: branch `claude/lepton-factor-forced-normalisation-2026-11-21` unmerged (`ForcedLeptonFactor.lean` not on `main`); owner ruling 2026-11-21 keeps placements B and C open pending derivation. |
| `#8867` | `derive octet baryon masses under Convention D` | **KEEP OPEN** (commented) | Partial: PR `#8887` (`3ca1398d6f8`, `77398acde6f`) landed `QOU/BraidsAndKnots/StrangeStrandOctet.lean`. Open: quantum-weighted sea-strand Lean proof & full octet mass derivation residuals. |
| `#8866` | `close the ×2.404 factor on Q_β under Convention D` | **KEEP OPEN** (commented) | Partial: PR `#8868` (`d94a90c0b3d`) landed `QOU/QBeta/OneSidedReading.lean` + `docs/audits/2026-11-21-qbeta-np-error-budget.md`. Open: closing the `×2.404` `Q_β` factor from first principles. |
| `#8801` | `Proton and neutron under convention D — EM splitting inside braid trace` | **KEEP OPEN** (commented) | Partial: PR `#8804` (`5342537fb28`) proved literal convention-D proton identity isospin-blind. Open: quark-charge `q_i` derivation from braid topology and step-4 gluon (owner rulings 2026-11-22). |
| `#7967` | `what is the W boson as a braid / morphism? (qou-0whz)` | **KEEP OPEN** (commented) | Partial: PR `#7968` (`0a7595079b3`) proved no single braid word is the W process (`QOU/QBeta/WProcessBraidAudit.lean`). Open: constructing the W form-factor object & strand-creating cobordism morphism (`qou-0whz`). |
| `#7965` | `verify neutron–proton mass difference in MeV — close ×1.73 factor (qou-jwl8)` | **KEEP OPEN** (commented) | Partial: PR `#8886` (`3a865b37770`) stated both `(H_α)` and `Q_β + m_e` numbers honestly. Open: first-principles derivation of `(H_α)` (`qou-jwl8`). |
| `#7939` | `Q_β = 782.3 keV from the Jones/skein trace — full derivation epic (qou-cds1)` | **KEEP OPEN** (commented) | Partial: PR `#7961` (`c06766a3891`, `416305e55c9`) & `#7603` (`dc12b128ccc`) landed. Open: convention-D `c_k` ladder derivation (`qou-wxhi`, `qou-cds1`). |
| `#7751` | `derive (or drop) the (1 − ℏ_q)² dressing in α_s` | **KEEP OPEN** (commented) | Partial: PR `#7752` (`3d892061fc2`) merged; owner explicitly ruled `"still leave issue open"` (`qou-uir6`, `qou-za3q`). |
| `#7713` | `reading 3 of Table 7.1 — derive quark template and selection rule` | **KEEP OPEN** (commented) | Partial: PR `#7718` (`e19599d89a0`) merged reading-3 variant test. Open: deriving quark template & selection rule above 10 crossings (`qou-y2np`, `qou-ales`, `qou-99qc`). |
| `#7711` | `derive Theorem 6.13 hypercharge weights (1/6, 2/3, −1/3)` | **KEEP OPEN** (commented) | Partial: PR `#7712` (`b884001909e`) merged scope correction. Open: `conj:sm-hypercharge-invariant` & geometric Reeb involution under Rule 13a (`qou-h0zz`, `qou-wqto`, `qou-8lxd`). |
| `#7678` | `extend knot-selection census above 10 crossings` | **KEEP OPEN** (commented) | Partial: PR `#7679` (`22e0ab37dac`) merged fibre/q-length census (`Refs #7678`). Open: rule A vs B selection / `γγ` linking-neutrality proof above 10 crossings (`qou-99qc`, `qou-pzsi`). |
