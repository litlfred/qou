---
# qou-s028
title: 'Stability: Swarm & Merge-Manager Continuity Handover'
status: in-progress
type: epic
priority: high
tags:
    - stability
created_at: 2026-11-24T08:06:16Z
updated_at: 2026-11-28T12:23:24Z
parent: qou-5vkl
blocked_by:
    - qou-10v9
    - qou-rtxm
    - b9cj
    - qou-0uga
    - qou-hksc
    - qou-lpep
    - qou-vo9t
    - qou-yvgk
    - qou-dke6
    - qou-wsha
    - qou-n4r9
    - qou-kdh5
    - qou-trd0
    - qou-ziag
    - qou-q1tk
    - qou-cfwx
    - qou-eggf
    - qou-v6so
    - qou-4f8t
    - qou-4un2
    - qou-qs0e
    - qou-5bkr
    - qou-w3dm
    - qou-efxy
    - qou-35a8
    - qou-mm2j
    - qou-u81q
    - qou-e9pp
    - qou-sogb
    - qou-37kk
    - qou-t3nx
    - qou-7vh1
    - qou-za1a
    - qou-agvb
    - qou-bes8
---

## 0. Swarm Work-Item Contract — `'Stability'` Epic Swarm (`qou-s028`)

A **Swarm** is a first-class work item (`type: epic` in `beans`) with explicit **Acceptance Criteria / End State**, **Structured Work-Item Queues**, **On-Demand + Optional Periodic Human-Consumable Status Reporting**, and **Live Cold-Start Handover Notes**.

### Defined End-State / Exit Criteria for the `'Stability'` Swarm
- [x] **EC-1 (Four Open Derivation Gaps Closed or Framed Under Rule-13a — COMPLETE ON `main`):** All `9/9` Open-Gap PRs (`#9245, #9278` `⁴He`; `#9247, #9249` `m_τ`; `#9251, #9253` `N_gen = 3`; `#9255, #9257, #9240` `a₀`) proved (`0 sorry`), 80-dps SHA-stamped, and **MERGED** onto `origin/main` (plus survey/slides synced in **MERGED `#9298`**).
- [x] **EC-2 (Precision & Anchor Hygiene Gates Green — COMPLETE ON `main`):** `#9237` (`63 -> 21`), `#9303` (`7` dashboard witnesses), `#9293` (`3919ec27381`), and `#9302` (`33d9d30f73c`) **ALL MERGED** onto `origin/main` (`q0_anchor_ratchet.py --strict` `63 -> 0` & `precision-gates.sh` `100%` exit `0`).
- [x] **EC-3 (Monograph One-Voice & Commentary Ratchets at Zero + `Convention C/D` Excised — COMPLETE ON `main`):** `voice-leak-baseline.json` `{}` (**MERGED `#9271`**), `Convention C/D` excision (`#9288, #9296, #9300, #9280, #9316`), `paper-commentary-audit.ts` `0 / 3,753` (`#9305, #9314, #9318`), and `L1–L5` `voice-leak-ratchet.ts` `0 / 3,743` (`#9311`) **ALL MERGED** onto `origin/main` (`0` live, `0` baseline across both audits/ratchets!).
- [x] **EC-4 (`Epic qou-xip2` Backlog Drain, Wave C & Post-Merge Bean Reconciliation — COMPLETE ON `main`):** All `10/10` Backlog Drain Batches `1–10` (`#9237, #9238, #9259, #9241, #9261, #9263, #9265, #9267, #9269`), `#9276`, all `4/4` Wave C PRs (`#8161, #8351, #8392, #8393`), `#9323` (`qou-x60n` `30/30` refutation audits), `#9243` (`qou-cvu9`), and `#9309` (`scripts/close-merged-pr-beans.py`) **ALL MERGED** onto `origin/main` (`+146+` beans reconciled on `origin/cat/cat-harness/beans`).
- [ ] **EC-5 (Owner Architectural Decisions `Q2`, `Q3`, `Q4` & Swarm/Merge KG Landed):**
  * **Q2 Option 1 (`qou-wywz`):** **COMPLETE & MERGED (`#9286`)**.
  * **Q4 Option 1 (`qou-mba8`, `qou-anx0`, `qou-lanx`, `qou-nmjd`):** **COMPLETE & MERGED (`#9280` & `#9316`)**.
  * **Swarm/Merge-Train/Sibling-Launch Skills & KG:** **COMPLETE & MERGED** in both `qou` (`#9290` & `#9309`) AND `litlfred/cat-harness:main` (`#1397` -> `afa287c7a99`, `merge-guard.ts` `9/9` PASS!).
  * **Q3 Option 1 (`qou-lref`):** Stage 1 (`0` outbound `QOU.*` cut-edges + `apply-lean-reservoir-migration.py`) **MERGED (`#9274`)**; Stage 2 (`0c54179d3b6`): **ALL `7/7` standalone Reservoir `[[lean_lib]]`s (`1,787` modules) + `UGB` (`46/46`) `100%` `.olean`-GREEN (`0 RED`, `0` cut-edges)**; now sweeping `QOU` (`2,098` `QOU.<Chapter>` modules, `task-426`) -> Ready PR -> merge -> `--fixup-branch` across remaining open PRs.

---

## Purpose — Cold-Start Continuity & Stall-Safe Handover (`qou-s028`)

This **Stability** Swarm epic is updated and pushed to `origin/cat/cat-harness/beans` on **every routine Swarm Monitor checkin** (currently `*/10 * * * *` periodic mode, and also renderable on-demand anytime). If the active Swarm Coordinator / Merge Manager ever stalls, runs out of context, or disconnects, **any successor agent reading this single bean (`beans show qou-s028`) has 100% of the end-state criteria, work-item queues, owner rulings, fences, worktree map, and commands required to take over seamlessly in `< 60` seconds.**

- **Last Heartbeat Refresh:** `2026-11-24T14:55:09Z` (`2026-11-24 09:55:09 `)
- **`litlfred/qou` `origin/main` Tip:** `7a7671f2360`
- **Live Queue Counts (`litlfred/qou`):** Open PRs = `174` (`164` Ready / `10` Draft) · Merged Since `2026-11-23` = `106` (latest: #9350, #9348, #9346, #9344, #9342, #9340, #9339, #9337, #9335, #9333, #9331, #9329) · Open GitHub Issues = `78`
- **Disk Health (`/`):** `/dev/disk3s1s1  927G  914G   13G  99% /`

---

## 1. Standing Owner Directives & Strict Safety Fences (MUST ENFORCE)

1. **Q1 — Auto-Prepare-Merge All Completed-Workitem PRs & All Newly Finished Epic/Bean Branches (`2026-11-24`):**
   - Every open Ready PR on `litlfred/qou` whose work-items/beans are completed (and not already superseded on `main` or flagged DO-NOT-MERGE) — **including every new PR opened as workers complete epics/beans** — is pre-authorized to run through `/prepare-merge-auto` (`.claude/skills/local/prepare-merge-auto.md`):
     * Rebase onto `origin/main` (use `python3 scripts/qa-sidecar-agent-union.py --against <pre-rebase-ref> --apply` on `.qa.json` conflicts so agent verdicts are NEVER dropped).
     * Check Copilot/human review threads (`gh api repos/litlfred/qou/pulls/<N>/reviews` & `/comments`).
     * Run final-HEAD local gates (`GitHub Actions` auto-triggers are disabled, so `checks=0` is NOT a gate — local gates ARE the gate): `bun run scripts/run-validate.ts content/quantum-observable-universe` + `npx tsx scripts/paper-commentary-audit.ts` (if prose/content touched), `python3 scripts/lean-library-sweep.py` / `scripts/lean-content-sweep.sh <touched .lean>` (if `.lean` touched; **NEVER run `lake build`**), `compute-qa.py` + `witness-shape-guard.py` (if witnesses touched).
     * Revert the **9 contended `qou-v0t8` tree-wide audit witnesses** (`computations/audits/q0-anchor-consistency-audit.witness.json`, `computations/*-audit.witness.json`) before pushing.
     * Merge via `gh pr merge <N> -R litlfred/qou --rebase` (**NEVER pass `--delete-branch`!**).
     * Immediately verify `MISSING: 0` via `python3 scripts/verify-merge-replay.py --branch origin/<branch> --merged $(git rev-parse origin/main)`.
2. **Q2 Option 1 (`qou-wywz` — Authorized):** Thread the Three-Stop Leibniz Relational Spine across Ch. 0 (`introduction/intro.md`), Ch. 2 (`quantum-observable-universes/rieffel-metric-quotient-faithfulness`), and Ch. 13 (`gravity-spacetime/cr-structure-lorentzian-lift` + Fefferman `(3,1)` Lorentzian lift) with verified DOIs (`barbour-bertotti1982` `10.1098/rspa.1982.0102`, `rovelli1996` `10.1007/BF02302261`, `earman1989`) -> open Ready PR -> auto-prepare-merge.
3. **Q3 Option 1 (`qou-lref` — Authorized: START NOW, Merge When Ready, Then Fixup Open PRs & Update Skills):**
   - Isolate `MathlibExt` + the `6` Reservoir-ready Tier-B `[[lean_lib]]`s (`HeckeTemperleyLieb`, `TwistedFrobeniusHopf`, `ToricConicOpt`, `CompactQuantumMetrics`, `QCalculus`, `BraidKnotOctonion`) in `folio/quantum-observable-universe/lean/lakefile.toml` (`0` outbound `QOU.*` cut-edges) and collapse the `83` `QOU/*` folders + `106` loose files into `12` canonical `QOU.<Chapter>` subgraphs.
   - Persist `scripts/apply-lean-reservoir-migration.py` (including `--fixup-branch` mode) and update `.claude/skills/local/` Lean/detangler skills.
   - Merge onto `main` when green, then run `apply-lean-reservoir-migration.py --fixup-branch` across remaining open PRs so they rebase cleanly!
4. **Q4 Option 1 (`qou-mba8`, `qou-anx0`, `qou-lanx`, `qou-nmjd` — Authorized):** Rebuild `appendix-mass-binding-algorithms` into the compact `9`-block $\mathcal{L}_0\text{--}\mathcal{L}_4$ QOU-Delta Algorithms Annex (fixing all 6 mathematical contradictions + stripping `CAL-1/2/3` & `../../../` leaks) and consolidate all `14` back-matter appendices into `6` Annexes (`A–F`) with uniform 80-dps witness-backed master reference tables & propagated $(m_e, \mathfrak{D}_\beta, m_\pi)$ uncertainties.
5. **`/idle-backlog` Compute-Wait Rule (`2026-11-24`):** Any sibling waiting on background single-core compute MUST pull right-scoped, non-compute-heavy beans (without running `git checkout` mid-build) instead of sleeping on timers.
6. **STRICT PUBLIC-RELEASE & DO-NOT-MERGE FENCE:**
   - NEVER touch or merge PR `#9217`, Active Set 1 PRs (`#9178, #9176, #9174, #8734, #8692, #8735`), or DO-NOT-MERGE PR `#8150` (refuted $S_5$ theta characteristics).
   - NEVER touch `CITATION.cff`, `home_page/`, `README.md`, `CONTRIBUTING.md`, `CONTRIBUTORS.md`, `authors-note/`, `scripts/build-site.sh`, `scripts/publish-main-local.sh`, or `/Users/litlfred/space_cats/qou` working tree (owned by external public-release agent).
   - Git author MUST be `litlfred <litlfred@users.noreply.github.com>` everywhere. Single-threaded resource caps (`nice -n 10`, `LEAN_NUM_THREADS=1`, `OMP_NUM_THREADS=1`, `RAYON_NUM_THREADS=1`, NO `lake build`). `NO FITTING EXCEPT CAL-1/2/3`, `mp.dps = 80`, zero `float64`.
7. **Mandatory Sibling Launch Briefing (`2026-11-24` STRICT):** Subagents start with zero conversation history. Every `invoke_subagent` prompt MUST explicitly inject:
   - *For Merge Steward (`merge-manager`):* `cat-harness/sdlc/skills/sdlc-core/{merge-manager-watcher,merge-queue,merge-to-main,merge-conflict-patterns}.md` + `.claude/skills/local/prepare-merge-auto.md` (`Process_MergeTrain` overlap batching, combined `Task_LocalGates` once per train, `Process_MergeRefusal` culprit hand-back, post-merge `beans update <id> --status completed` + push `cat/cat-harness/beans`, `verify-merge-replay.py` `MISSING: 0`, NEVER `--delete-branch`).
   - *For Task Siblings:* `.claude/skills/local/*.md` domain skills FIRST + `continual-progress.md` + `idle-backlog.md` (pull non-compute-heavy beans while waiting on single-core compute; zero passive sleep timers; never `git checkout` mid-build) + `merge-queue.md` sibling submission (**NEVER self-merge**; hand `ready-to-merge` / `ready: <sha>` + 6-line merge request to `merge-steward`) + strict `one-voice` external-reader prose (`0` `Convention C/D` or `CAL-1/2/3` labels) + revert the 9 `qou-v0t8` contended audit witnesses + public-release fence.
8. **Swarm Status Report Cadence:** On-demand anytime + optional periodic cron (`*/10 * * * *`, `ExactTiming: true`), zero internal shorthands, running `sync_stability_epic.py` on every tick to refresh and push `qou-s028` to `origin/cat/cat-harness/beans`.

---

## 2. Live 10-Worktree Ownership & Branch Map (`/Users/litlfred/space_cats/qou-wt/*`)

| Worktree | Checked-Out Branch & HEAD | Assigned Track & Responsibility | Latest Commit Subject |
| :--- | :--- | :--- | :--- |
| `merge-runner` | `mt-local/9350` @ `fdc16f757f6` (`dirty=0`) | Serial prepare-merge-auto Runner onto origin/main (Wave A -> Wave B -> Wave C) | chore(library): remove 802 third-party PDF binaries for public release (kee |
| `ws6-exposition-pdf` | `claude/public-prep-remove-third-party-library-pdfs-20261124` @ `fdc16f757f6` (`dirty=0`) | Q1 Staged-Branch PR Opener (Wave B, 14 branches) & Completed-Workitem Open-PR Auditor (Wave C) | chore(library): remove 802 third-party PDF binaries for public release (kee |
| `ws4-mathlib-infra` | `claude/q3-lean-reservoir-libs-codemod-20261124` @ `0c54179d3b6` (`dirty=0`) | Q3 Option 1: Lean 83->12 QOU.<Chapter> Subgraphs + 7 Top-Level Reservoir lean_libs + apply-lean-reservoir-migration.py --fixup-branch + skill updates | refactor(lean,qou-lref): execute Q3 Option 1 7+1 Reservoir lean_libs & 83-> |
| `main-base` | `HEAD` @ `d7e1269e1e0` (`dirty=0`) | Q2 Option 1: Three-Stop Leibniz Relational Spine (Ch. 0 intro, Ch. 2 Rieffel/Jimbo, Ch. 13 Fefferman Lorentzian) + live DOIs | feat(qou-1buz,qou-d8up,qou-exr5,qou-f13w,qou-fiaf,qou-ni2p): disambiguate F |
| `ws5-nov19-rebase` | `claude/accuracy-scorecard-tool-skill-publish-qa-20261124` @ `a228713c4e2` (`dirty=0`) | Q4 Option 1: Compact 9-Block L0-L4 Algorithms Annex (fixing 6 bugs) + 14->6 Annexes A-F with 80-dps Frechet-Jacobian Master Tables | feat(accuracy,qa): 80-dps ACCURACY.md scorecard generator, skill, and publi |
| `ws12-pr9180` | `claude/crosscheck-9zcl-r0fd-fls0-f0qa-cmjv-20261124` @ `0da7f9d9e53` (`dirty=0`) | Gap 1B (qou-3kkz): 4He Tetrahedral K_4 Flux-Ring & 462D 3D Jacobi Variational Compression + idle beans qou-bgur, qou-kjik | chore(witness): stamp 80-dps witnesses for qou-9zcl, qou-r0fd, qou-fls0 & q |
| `ws1-precision` | `claude/precision-4w7k-5le1-5rf8-58zq-20261124` @ `b5b35f6882d` (`dirty=0`) | ws1-precision (#9104): 12-Witness q0 Precision Refill (11/12 all_nuclides_sdp + gates) + idle beans qou-n2dp, qou-5d0x | fix(precision,audits): qou-mass 80-dps literal hygiene, q0 pin classifier M |
| `ws15-p3-p5-p6` | `claude/editorial-audit-0sq1-20d3-9rbo-73y1-20261124` @ `fab95788eda` (`dirty=0`) | ws1-precision Witness 12/12 (markov-trace-two-row-tower-rust) + idle beans qou-73kb, qou-m1tr | feat(braids-and-knots,audits): forward-interprets fix, Sniady remark & x631 |
| `ws2-bridge-hecke` | `claude/frobenius-gram-a71h-z21-bisect-85o2-20261124` @ `33d9d30f73c` (`dirty=0`) | q0-Anchor Final 21 Consistency Drain (qou-q0rf) + idle beans qou-jdrx, qou-ke35 | precision-gates: clear new CODATA stale-edition and witness-value-copy regr |
| `ws3-l2-physics` | `claude/prose-bib-ahys-bagd-a8rj-d93c-df74-ffkf-20261124` @ `755c67e52bb` (`dirty=0`) | One-Voice Final 31->0 Monograph Commentary-Audit Drain (paper-commentary-audit.ts ratchet -> 0) | feat(qou-ahys,qou-bagd,qou-a8rj,qou-d93c,qou-df74,qou-ffkf): wire Neumann/S |

---

## 3. Live Sampled Compute / Sweep Processes

- `41206 0.0 1136 01:35:50 zsh -c cd /Users/litlfred/space_cats/qou-wt/ws4-mathlib-infra && \\012export LEAN_NUM_THREADS=1 RAYON_NUM_`
- `41217 0.0 16800 01:35:49 python3 scripts/lean-library-sweep.py --package QOU --jobs 1 --shadow /tmp/ws51-codemod-shadow`

---

## 4. Highest-Numbered Active Ready PRs on `litlfred/qou` (Merge-Runner Queue)

- #9352 (`claude/accuracy-scorecard-tool-skill-publish-qa-20261124`): feat(accuracy,qa): 80-dps ACCURACY.md scorecard tool, skill, README li
- #9217 (`claude/project-thread-di0nax`): Public release prep: CITATION.cff
- #9178 (`claude/exposition-statement-rulings-2026-11-16`): Exposition: owner rulings on false or under-derived statements
- #9174 (`claude/convention-c-ledger-2026-11-21`): convention-C ledger: adjudicate the 8 unadjudicated comparison sites
- #9159 (`claude/project-thread-ipc33x`): Corpus-grep path 7 (block QA sidecar); fits_AME labelled as comparison
- #9045 (`claude/merge-coordinator-memory-2026-11-22`): merge-coordinator memory: rebase-merge 405 with no merge commit
- #8751 (`claude/q0-anchor-refill-drain-2026-11-21`): Drain the q0-anchor refill ratchet (30 → in progress)
- #8741 (`claude/gg-internucleon-bond-2026-11-21`): γγ inter-nucleon bond: which bond words does reading 3 admit in a nucl
- #8560 (`claude/uic-scoping-kjik-banner-reland-2026-11-20`): Re-land #7439's three items, then close the q-precision input ceiling 
- #8512 (`cat/round88-triangulation3dindex-helicityparity-blochk3torsion-immirzihorizontower-strangeidentityscope-bridge`): feat(qou): formalize 1-efficient 3d-index invariance, helicity parity,

---

## 5. `< 60`-Second Cold-Start Takeover Checklist for Next Swarm / Merge Manager

If the prior coordinator has stalled (`last Heartbeat Refresh` > 20 min old and no active turns):
1. **Sync & Read This Epic:**
   ```bash
   git -C /private/tmp/qou-beans-latest pull --rebase origin cat/cat-harness/beans
   cd /Users/litlfred/space_cats/qou && beans show qou-s028
   ```
2. **Audit Running Processes & Worktrees Before Spawning Workers:**
   ```bash
   ps -eo pid,pcpu,rss,etime,command | grep -E 'python|lean|cargo|bun|tsx' | grep -v grep
   for d in /Users/litlfred/space_cats/qou-wt/*; do echo "=== $d ==="; git -C "$d" status -sb; git -C "$d" log -1 --oneline; done
   ```
   *(Never `git checkout` inside a worktree that still has a live PID running from Step 2!)*
3. **Start Your 10-Minute Cron (`*/10 * * * *`, `ExactTiming: true`)** and run `sync_stability_epic.py` (or `cat-harness` `stability-handover-sync`) on every tick.
4. **Resume Serial `prepare-merge-auto` in `/Users/litlfred/space_cats/qou-wt/merge-runner`** across remaining Wave A (`#9238, #9241, #9234, #9230, #9228, #9227, #9225, #9223`), Wave B (newly opened Open-Gap, Backlog-Drain Batch 3/5/6/7/8/9–10, Q2, Q3, Q4, `ws1-precision`, `q0-anchor`, `one-voice` PRs), and Wave C (vetted completed-workitem open PRs).
5. **Coordinate Q3 Option 1 Landing + Open-PR Fixups:** As soon as `claude/q3-lean-reservoir-libs-*` passes sweeps and merges onto `main`, run `python3 scripts/apply-lean-reservoir-migration.py --fixup-branch` on each remaining open Lean PR branch before rebasing/merging it.

2026-11-27 (thread 'Get QOU site running on harness'): owner asked that stability, eightfold+SM and accuracy show on the work-plan milestones dashboard (milestone-rollup.ts rolls up milestones only). Parented to milestone qou-5vkl (Platform, tooling and hygiene); it had no parent, so it was an orphan off the dashboard.


## Linked workstreams (2026-11-27T23:40Z, Carl: "Make sure all the things that we're working on are linked under the stability epic. So if we restart the stability epic these all restart")

Every open bean touched on 2026-11-27 (262 beans; 6 were already children of this epic) is now reachable from qou-s028. Its workstream root is recorded in `blocked_by` on this epic. Roots that are milestones or other epics cannot be made children of an epic, so the link is a blocked-by edge. Existing parents are unchanged.

**To restart:** walk qou-s028's `blocked_by` list, then each root's children.

Roots (number of beans active today under each):
qou-10v9 (140, L2 1 ppQ program, includes qou-myts), qou-rtxm (28, Lean foundations; includes qou-dk7p, qou-3fdg, qou-e1uf and hkmt), b9cj (18, open conjectures), qou-0uga (14, SM/eightfold; includes qou-x08k), qou-hksc (9), qou-lpep (9, exposition), qou-vo9t (7, Bring/Yekutieli gerbes), qou-yvgk (4, knot volume).

Single-bean roots: qou-dke6, qou-wsha, qou-n4r9, qou-kdh5, qou-trd0, qou-ziag, qou-q1tk, qou-cfwx, qou-eggf, qou-v6so, qou-4f8t, qou-4un2, qou-qs0e, qou-5bkr, qou-w3dm, qou-efxy, qou-35a8, qou-mm2j, qou-u81q, qou-e9pp, qou-sogb, qou-37kk, qou-t3nx, qou-7vh1, qou-za1a, qou-agvb, qou-bes8.

Named in the request and covered through these roots: qou-jmgu, qou-swk4, qou-kdh5, qou-3fdg, qou-h0zz, qou-qvpl, qou-e1uf, qou-brng, qou-pvu4, qou-m45w, qou-ku91, qou-efxy, hkmt, qou-qexu, qou-0xk8, qou-h315, qou-sv7h, qou-za1a.


## Active Antigravity Swarm Handover — 2026-11-28T10:15Z (Coordinator `92bff8c9-777d-458a-a380-8dd5bf5cc0f3`)

- **`origin/main` Tip:** `2cc11f7f1c6` (`1,594` commits landed since Nov 24 `4517e0bceee`; `34` open PRs)
- **Active Coordinator:** Antigravity foreground session `92bff8c9-777d-458a-a380-8dd5bf5cc0f3` (foreground kept open for owner; 10-minute status cron active; coordinating cleanly with Claude sessions via `cat/cat-harness/beans` + PR comments).
- **Dispatched Child Siblings Under `qou-s028`:**
  1. **`qou-ii2k` (`ws1-precision` -> `claude/speculative-open-problems-split-20261128`):** Create `folio/speculative-open-problems/` & move problem framing for RH, P vs NP, Yang-Mills, BSD, Collatz, and Millennium unification out of `folio/quantum-observable-universe/`, keeping neutral sound algebra in the main book + coordinating with open PRs `#9984` & `#9979` + recording owner ruling in `docs/coordination/owner-rulings.md`.
  2. **`qou-yzp7` (`ws6-exposition-pdf` -> `claude/fluid-dynamics-qns-tonedown-20261128`):** Keep `fluid-dynamics/` NS framing in main book, toned down throughout to a `q`-deformed hydrodynamic model (`ns-classical-formulation.md`, `ns-surreal-bound.md`, `p4/p5`, Lean docstrings).
  3. **`qou-0jo7` (`ws5-nov19-rebase` -> `claude/postmerge-qa-scorecard-boundary-20261128`):** Clear post-merge QA reds on `main` (`JonesTractableOrders.lean` transcendental boundary, `base-ring-audit --shrink`, refresh import-cone-stale scorecard witnesses at proton pin + regenerate `ACCURACY.md`).
  4. **`qou-d9iv` (`ws15-p3-p5-p6` & `ws12-pr9180`):** Rebase, applicability-audit against Nov 27-28 rulings (aether terminology, proton pin, base-ring units, T3 valence scope), verify, and open PRs for `ConfinementLayerMullikenStoichiometry` (`qou-5lct`) and exploratory `AlphaQuartetPauliWignerSaturation` (`qou-v2om`).
  5. **`merge-steward` (`merge-runner`):** Active single-writer Merge Steward under 24h grant (`to 2026-11-28T14:20Z`), enforcing FAST MERGES (`gen-block-jsonld.sh --check` pre-merge, post-merge QA + `close-merged-pr-beans.py` + `publish-main-local.sh` post-merge, never `--delete-branch`).

## 2026-11-28 Owner Directive — Proton Pin ONLY; Muon Pin ON HOLD (STRICT)
Verbatim (`2026-11-28`): *"make sure you are working proton pin... no longer muon (on hold, until rederivation)"*.
- All active compute producers, probes, and witnesses MUST run on the **proton pin** (`physical_proton`).
- The **muon pin** is **ON HOLD** until `m_μ/m_e = Vol(4₁)/ℏ_q²` (or its replacement under the new lepton ladder) is genuinely derived; zero newly-added active muon-pin witnesses may merge onto `main`.

## 2026-11-28 Merge Steward Train Landing (`4594f0db1376`)
- Landed orphan-beans PR **#9557** onto `cat/cat-harness/beans` (`6b6ae8e8784`).
- Confirmed ghost stacked PRs **#9569** (`146be50840a`) and **#9579** (`bf6edf4d68a`) are already ancestors of `origin/main` (`0` commits ahead).
- Landed 10 Category (a) `main` PRs + Priority Sibling-2 PR **#9994** (`qou-yzp7`) onto `origin/main` (`2cc11f7f1c62` -> `4594f0db137603dc057e2fd47a070648bdc536c7`), `MISSING: 0` across all:
  `#9502` (`32c51829a9d`, closed `qou-mk34`), `#9629` (`f22289709b8`), `#9687` (`00a77cbee51`), `#9722` (`6f89037b0c0`), `#9737` (`5c2b8ef8a22`), `#9747` (`e04d18bbd9d`), `#9777` (`3571e500084`), `#9811` (`aa875534101`), `#9995` (`b9b18345023`, lossless `--merge` recovery after GitHub rebase-merge dropped `#9934`'s 2 commits over merge-from-main `e23577eb3ab`), `#9983` (`3fbba15854a`), and `#9994` (`4594f0db137`, closed `qou-yzp7`).

2026-11-28 (merge-steward): Landed PR #9996 (`qou-ii2k` speculative-open-problems split -> `fc10afc52fad532b0ae16a321185369fe4dcc8f6`, closed `qou-ii2k`, commented on #9984/#9979) and PR #9997 (`qou-5lct` Mulliken stoichiometry -> `2ef4ef0744ad28ff38a558f3e4288c728e00e19d`, closed `qou-5lct`, `qou-d9iv` kept `in-progress` for `qou-v2om`).

2026-11-28 (merge-steward): Landed PR #9998 (Owner Card A1 hadron-level knot table retirement -> `4e47aed7aee7743b607f62773d7c5f3d7e1fc172`) and PR #9999 (`qou-v2om` / `qou-d9iv` Tranche B -> `8fcfa9e031cb68e47bfbd05cb31fbaa2fbf60c3d`; closed `qou-v2om` and `qou-d9iv`).

2026-11-28 (merge-steward): Landed rebased Category (c) PR #9778 (`claude/pretzel-237-level2-blocks`) and post-merge QA PR #10001 (`qou-0jo7` -> `d6f663156699b2137363b7e6ea9607deea4d7530`; closed `qou-0jo7`; `ACCURACY.md` scorecard & `transcendental-boundary-audit` now GREEN on `main`).

2026-11-28 (merge-steward): Landed PR #10000 (`qou-f3hr`, `qou-j5b6`, `qou-bbr4` closed) and rebased Category (c) PR #9721 (`claude/strand-end-merge-ceiling-2026-11-27`) onto `origin/main` -> `087485613e37d7688b2009dfa317a6abb23fd1bd`.

2026-11-28 (merge-steward): Landed #10004 (`ef0b7571363f`), #10002 (`83b456280276`) onto `origin/main`; updated `qou-q0gw`/`qou-m45w` and closed completed leaf beans (`qou-cw8i`).

2026-11-28 (merge-steward): Landed rebased Category (c) PR #9767 (`claude/energy-scale-bridge-2026-11-27` -> `91076f6cc123768f656c7cc0cc0261dc792692c5`; closed `qou-h940`).

## 2026-11-28 Merge Steward — PR #10005 Landed (`2b5246217d5c`) & 4 Rust `crates/` + Annex A Child Beans Registered
- Landed PR **#10005** (`qou-vhm1` -> `2b5246217d5cfb7f0f1721e621bf11186f6635b1`, `MISSING: 0`; closed `qou-vhm1`).
- Registered 4 active `in-progress` child beans under `qou-s028`:
  - **`qou-crwk`**: crates/ workspace & tools KG migration: move Rust engines to top-level crates/* + Cargo workspace + defineTool KG nodes + local skill
  - **`qou-gsgg`**: crates/gs-basis + crates/qou-gg-core: standalone non-commutative Groebner-Shirshov library + pure-Rust 4-photon & Z=0..118 T3/Hopf chart generator
  - **`qou-qval`**: crates/qou-values: fast >=80-dps MPFR proton-pinned witnessed-value evaluator & witness emitter with Frechet-Jacobian uncertainties
  - **`qou-ggtb`**: crates/qou-gg-eval + crates/qou-clarabel + Annex A gamma-gamma hadron/light-nuclei datum table (A=1..4)

## 2026-11-28 Merge Steward — PR #9723 Landed (`63aa63af7d56`) & 2 New Child Beans Registered
- Landed PR **#9723** (`qou-x08k` exterior-quotient axiom fields -> `63aa63af7d56cf1f14b8c3951c622c90f29524fe`, `MISSING: 0`; closed `qou-x08k`).
- Registered 2 active `in-progress` child beans under `qou-s028`:
  - **`qou-intr`**: Introduction redo & Paper PDF TeX fix: 3 summary tables (gamma-gamma hadrons, Eightfold status, 26 SM parameters) + proton-pin / E=mc_q^2 currency + fix Paper PDF TeX errors
  - **`qou-cbot`**: Compute bottlenecks audit & Rust crates/* acceleration map: profile slow Python producers/sweeps across computations/ and map exact crates/* targets
- Landed PR **#9705** (paper retitle *"On the Mechanics of Quantum Observables"* -> `ea3443986de5954b84d279aab406a7b3c333dff0`, `MISSING: 0`; `speculative-open-problems` & `ACCURACY.md` preserved).

- **2026-11-28 (`#9941` landed)**: Merged PR `#9941` (`hkmt` glued TL `MonoidalCategory`, `6118b03bd24a` -> `e21d9686cec98143ba7ec2a00b3f9543b9242c92`, `17/17` replayed, `MISSING: 0`, 26th PR landed in session).
