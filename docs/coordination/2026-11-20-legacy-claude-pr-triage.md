# Legacy claude/* PR triage (2026-11-20)

Workstream W5 of the 2026-11-20 coordinator plan. Scope: the 41 human-thread `claude/*` PRs
(#8519 … #5338). PRs owned by W1–W4 are excluded. Nothing here closes or merges anything: the
coordinator does that with owner permission.

Main measured at `917b69399` (shallow clone, 55 commits of history, so "superseded by" cites the
file on main that carries the result rather than a commit sha; history before that is not fetched).

## Method

Every number below was measured by scripts kept in this session's scratchpad and re-runnable from
the PR API. For each PR:

1. **Added declarations.** Lean `theorem|lemma|def|abbrev|structure|class|instance|inductive` names
   on `+` lines of `.lean` patches; Python top-level `def|class` on `+` lines of `.py` patches.
   Each name is `git grep`ped on `origin/main` (by its last component). The count is a
   **name-match**: a hit means a declaration of that name exists on main, not that it is the same
   statement. Short generic names (`support`, `tr_add`) can hit unrelated files; where that matters
   the main location is named below.
2. **Added files.** Exact path on main, with `content/` → `folio/` normalised (the tree rename).
3. **Added lines.** For PRs with mostly modified files: the fraction of the PR's added lines
   (stripped, longer than 12 chars) that appear verbatim in the same file on main.
4. **Beans.** Ids named in the PR title/body, status read from the branch-mounted `beans/defs/`.
   `?` = no such bean on the mount.

`.beans/` edits on old PRs are dead paths: beans moved to the branch mount (`58a1f3231c`,
issue #7642) and are no longer merged through PRs.

## Verdict summary

| verdict | count | PRs |
|---|---|---|
| MERGE-CANDIDATE | 2 | #8519, #8102 |
| PORT-CORE-TO-MAIN | 26 | ranked list below; the rest are marked low / remainder |
| CLOSE-SUPERSEDED | 11 | #7769, #7481, #7441, #7406, #7229, #7225, #7218, #7210, #6359, #6025, #5338 |
| NEEDS-OWNER-DECISION | 2 | #7205, #6178 |

## Table

| PR | behind | added decls on main (lean / py) | beans | verdict | evidence |
|---|---|---|---|---|---|
| #8519 | 2 | 1/1 / 0/4 | — | **MERGE-CANDIDATE** | Paper PDF build + publish on merge. Body cites owner ruling 2026-11-18 ("1a", "2 y"). 419/426 added files absent from main. ⚠ Contradicts AGENTS.md §"Build output (gh-pages)" (rendered site deprecated 2026-09-27, "do not restore a push trigger"); the PR adds a path-filtered push trigger in `.github/workflows/paper-pdf.yml`. The newer owner ruling governs, but AGENTS.md must be updated in the same merge or the next agent will revert it. |
| #8134 | 62 | 4/30 / – | — | PORT-CORE (low) | Braid-closure commutator span; 26 Lean decls absent (`ClosureUnseen.lean` absent). Not mass/binding. Touches `fluid-dynamics/helicity-conservation.*`. |
| #8111 | 101 | 6/28 / 6/11 | — | **PORT-CORE (rank 3)** | Bridge B n–p mass-scale exclusions: `NucleonIsospinExclusions.lean` + 5 probes + audit, all absent. |
| #8110 | 102 | 5/25 (hits are generic names) / 1/2 | — | **PORT-CORE (rank 1)** | Term 4 co-Casimir on the radical quotient. `coCasimirSurv` occurs nowhere on main; `CoCasimirSurvivingBlocks.lean` absent. |
| #8102 | 102 | 1/2 / – | — | **MERGE-CANDIDATE** (rebase first) | Dangling `computation.script` paths; 0/82 added lines on main; `parity-regime-dispatch.{md,ts}` absent. Mechanical and corpus-derived (exemption 2). |
| #8096 | 193 | 4/17 / 4/6 | qou-4jhp in-progress | **PORT-CORE (rank 2)** | Reeb-holonomy Laplacian (`HeckeReebHolonomyLaplacian.lean` absent; `reebLaplacianB` nowhere on main). Touches `computations/hecke_core_legacy.py` → W2. |
| #8054 | 730 | – | — | PORT-CORE (trivial) | 5-line append to `.claude/agent-memory/lean-verifier/session-log.md`; 0/5 on main. |
| #7936 | 609 | 0/11 / – | — | PORT-CORE (low) | `MathlibExt/KummerObstruction.lean` absent. |
| #7913 | 605 | 9/321 / 5/8 | 10 completed, qou-xblo in-progress | **PORT-CORE (rank 5)** | Volume/dilog bricks, 20 new files, all absent. Large; split before porting. |
| #7909 | 739 | 0/9 / – | — | PORT-CORE (low) | Bring's-surface colour-ratio Möbius matrix; 5 files absent. |
| #7878 | 840 | – | qou-s4ws scrapped (session epic, not the ingest) | PORT-CORE (mechanical) | Library ingest of Wenzl / Turaev / Proctor 1988; `folio/references/{proctor1988,turaev1988}.json`, `library/proctor1988/` absent. Re-run the ingest on main rather than replay 445 files. |
| #7874 | 845 | 6/47 / – | qou-gl34 todo, qou-aycj ? | PORT-CORE (remainder) | 123/187 added files already on main; 42 absent incl. `MathlibExt/Bicommutant.lean`, `SchurWeyl/QSchurMoves.lean`, `QSchurUpperBound.lean`, two audits. |
| #7865 | 845 | – | qou-hlx7 in-progress, qou-qs0e todo | PORT-CORE | Scope edit to `mass-theory/p-from-braid-mirror.{md,ts}`; 0/47 added lines on main. |
| #7845 | 876 | – | qou-qs4c in-progress, qou-qs0e todo | PORT-CORE | Audit doc only (Option I vs II impact), absent. |
| #7834 | 952 | 1/17 / – | qou-b5qg completed, qou-r1bn ? | PORT-CORE | `StandardModel/BringRealStructureTransport.lean` + audit absent. |
| #7817 | 965 | – / 6/9 | cds1/fd2u/wlnx/zuva in-progress | PORT-CORE (probe + audit only) | 18/1037 added lines on main. Its AGENTS.md / bean edits are stale against the current text; port only `probes/gg_ntower/gg_scalar_per_step_probe.py` + witness. |
| #7773 | 1315 | 64/81 / 22/24 | qou-a1hh in-progress | PORT-CORE (remainder) | 14/20 added files on main. Absent: `molecular_word_corpus_lb_probe.py`, two witnesses, 17 Lean decls (`junction_window_*`, `chain_trace`, …). |
| #7769 | 1315 | 63/69 / 19/19 | qou-a1hh | **CLOSE-SUPERSEDED** | Same line of work as #7773: its decls and files are a strict subset of #7773's (measured: 0 decls, 0 files not in #7773); 14/18 files on main. |
| #7763 | 1276 | – | qou-q261 todo | PORT-CORE | `scripts/corpus-search.ts` + `.mcp.json` fix; 0/111 lines on main. |
| #7590 | 1680 | – | qou-iax1 completed | PORT-CORE (re-derive) | rem-qstar figure refresh to the CODATA-2022 muon pin; 1/31 lines on main. Bean completed but text never landed. Re-derive the figures on main (precision exemption) instead of replaying. |
| #7481 | 1980 | 9/9 / 4/4 | 0fmb/6moa/img9/s7z2 in-progress | **CLOSE-SUPERSEDED** | All decls on main: `IwahoriHecke/TLCarrierBridge.lean`, `ParticleInteractions/operator_selection_lp.lean`, `QBeta/TraceNondegeneracyInsufficient.lean`; py in `canonical_trm_reference.py`. |
| #7477 | 2015 | – | 3ral/db24/eggf in-progress | PORT-CORE (code fix only) | 2/603 lines on main. AGENTS.md figure corrections are stale against current text; the one laundered-float64 fix should be re-checked on main. |
| #7441 | 2151 | 7/8 / – | qou-pdix in-progress | **CLOSE-SUPERSEDED** | 7/8 decls in `QBeta/ModularDoubleLocusSeparation.lean` on main; only `modular_cannot_bridge'` (primed variant) missing. |
| #7406 | 2445 | – / 11/11 | 5jqv/ix0x/sw8n in-progress | **CLOSE-SUPERSEDED** | 11/11 defs on main (`audits/bond_order_jbullet_citation_probe.py`); main commit `24156dd47` cites #7406. |
| #7229 | 3250 | – | sv7h/f2pf/oiz3 in-progress | **CLOSE-SUPERSEDED** | Code fully on main (`hecke_core_legacy.py` 30/30 lines, `binding_scaling_endtoend_probe.py` 83/85); remainder is `.beans/` text. |
| #7225 | 3378 | 21/21 / – | brng/ix0x in-progress | **CLOSE-SUPERSEDED** | All 21 decls in `Habiro/CyclotomicEvaluationRingHom.lean` on main. |
| #7218 | 3412 | 2/2 / 0/3 | za3q/gba1/56qy in-progress | **CLOSE-SUPERSEDED** (residual noted) | Lean decls in `MassTheory/MagnusCurvatureCommutator.lean`; 251/1034 lines. Residual: three private probe helpers (`_refuse_to_clobber`, `_sibling_sign`, `_smap`) and bean text. |
| #7210 | 3438 | – | vyvt completed | **CLOSE-SUPERSEDED** | Bean-ledger-only (`.beans/`), dead path since the bean mount. |
| #7205 | 3489 | – / 2/2 | 0e2p completed, 3nva/cds1 in-progress | **NEEDS-OWNER-DECISION** | The PR is itself the owner ask (CAL-2 proxy dataset). Frame below. |
| #7136 | 3704 | 1/32 / – | qou-kwoa completed | **PORT-CORE (rank 4)** | Geck–Pfeiffer Schur element: 6 Lean files under old `content/` path, all absent (`TwDual` nowhere on main). Bean says completed, the Lean never landed. |
| #7123 | 3834 | – / 14/20 | 43co/auq3/mw1p completed, qspu todo | PORT-CORE (remainder) | TL closure part landed (`tl_gs_reduction_probe.py` 277/277); `hecke_normal_form_confluence_probe.py` + witness absent. |
| #6361 | 7448 | 2/9 / 2/2 | cds1 in-progress | PORT-CORE | 0/572 lines; interval lemmas (`wtNumer_neg_of_between`, `zC_lt_zD`) and the `ConventionDAdmissibleRoots.lean` additions absent. Q_β-ladder relevant. |
| #6359 | 7430 | 6/6 / 2/2 | 768r in-progress, r13s todo | **CLOSE-SUPERSEDED** | All in `Mass/MilnorDefinedTriplesVanish.lean` on main. |
| #6350 | 7476 | – / 2/2 | — | PORT-CORE (probe only) | `alpha/mkmpi_l2_conditionality_ablation_probe.py` absent; its AGENTS.md edit ("0/5") is stale (main says 0/6). |
| #6342 | 7467 | – / 2/3 | cds1/t39x in-progress | PORT-CORE (low) | Two Q_β probes + witnesses absent; 24/1149 lines. |
| #6307 | 7733 | – / 5/7 | — | PORT-CORE → **W2** | Symbolic NF fold perf in `hecke_core_symbolic.py` (18/154 lines on main). Compute territory. |
| #6178 | 8187 | – / 1/9 | 6oxh/fsva/nldm ? | **NEEDS-OWNER-DECISION** | 176-site AME-literal → registry drain. Frame below. |
| #6025 | 9299 | – / 3/3 | — | **CLOSE-SUPERSEDED** | 474/591 lines on main; `stamp_joint_tower_witness.py` 101/101, README 35/35; remainder is `.beans/`. |
| #5861 | 10037 | 1/1 / – | gwe9 in-progress, we9a completed | PORT-CORE (small) | `barrett1993` reference is on main, but the glossary edits and `KeystonePivotalSpherical.lean` changes (0/53 lines) are not. |
| #5402 | 13618 | – / 1/6 | j4mn/xc8t/1n7g/24m2 in-progress | PORT-CORE | `jet_algebraic_dependence_verification.py` + witness + audit absent (311/885 lines). |
| #5338 | 13633 | – | vy77/u1b5/kc8h completed | **CLOSE-SUPERSEDED** | Bean-ledger-only (`.beans/`), dead path; the beans are completed. |

## Ports ranked by value to the mass/binding programme (judgement)

1. **#8110** Term 4 co-Casimir on the radical quotient — small (3 files), Lean-only core.
2. **#8096** Reeb-holonomy Laplacian for μ_λ — binding; one shared file with W2.
3. **#8111** Bridge B n–p exclusions — Lean no-go plus probes.
4. **#7136** Geck–Pfeiffer Schur element — Hecke character theory feeding `dettw`.
5. **#7913** volume/dilog bricks — `Vol(K)` side of the mass formula; large, split it.

Each port is one PR titled "Port #N onto main: …", verified with lean-direct (`-DautoImplicit=false
-s 65536`, cone rebuilt with `lean-direct-cone.sh -B`) and `#print axioms`.

## Decisions for the owner

### #7205 — which dataset serves the Q_β calibration proxy

- **The decision.** `codata_constants.Q_BETA_MEV` (the neutron β-decay Q-value, proxy for
  calibration CAL-2) is AME-2020 today; the PR proposes the CODATA-2022 value
  `(m_n − m_p) − m_e`. The two differ by +190.85 ppb = 0.208 σ (PR body), so this is a
  dataset-consistency question, not accuracy: CAL-1 (`m_e`) already comes from CODATA 2022.
- **Option A — adopt CODATA 2022.** Costs: the PR's 116-file blast radius, re-run of the Q_β
  producers. Risks: every recorded Q_β residual moves by ~0.19 ppm; the PR is 3489 commits behind,
  so it must be re-derived on main rather than merged. Commits to: one dataset for all three
  calibrations, matching the 2026-08-22 muon-pin ruling.
- **Option B — keep AME-2020.** Costs nothing. Risks: CAL-1 and CAL-2 stay on different datasets.
- **Default if no answer:** nothing changes; the PR stays open.
- **Recommendation (judgement):** A, re-derived on main as a fresh PR, because the owner's stated
  rule for the muon pin was "one dataset for CAL-1/2/3" and this is the same rule.

### #6178 — the AME-literal → values-registry drain

- **The decision.** Whether producers that hand-type AME-2020 binding energies should read the
  named registry constants instead (176 sites, 76 producers). The PR found the hand-typed values
  were typos (e.g. ³H `8.481821` vs AME `8.4817962`) and that 12 `data_loaded` assertions failed on
  main at the time.
- **Option A — re-run the drain on main.** Costs: a mechanical sweep of the same order (the PR is
  8187 commits behind and cannot be merged); producers re-run. Risks: witness values move at the
  1e-6 level; partially done already — `computations/ame-registry-routing-triage.witness.json`
  exists on main, so the remaining REVIEW count must be re-measured first. Commits to: registry as
  the single source of AME values. Arguably precision exemption 1 (replaces a literal with a
  derived value), but at sweep scale AGENTS.md says ask.
- **Option B — leave it.** Costs nothing now. Risks: typoed literals stay live.
- **Default if no answer:** nothing changes.
- **Recommendation (judgement):** A, after re-measuring the triage on main, because the typos are
  wrong numbers in compared quantities, which is where the physics lives.

### Not a decision, a flag: #8519 vs AGENTS.md

The owner ruled on 2026-11-18 (per #8519's body) that the paper PDF publishes on merge to main.
AGENTS.md §"Build output (gh-pages)" still says the rendered site is deprecated (2026-09-27) and
tells agents not to restore a push trigger. #8519 should carry the AGENTS.md update; otherwise the
next agent reading AGENTS.md will undo it.
