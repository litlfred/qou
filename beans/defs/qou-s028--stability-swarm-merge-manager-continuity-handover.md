---
# qou-s028
title: 'Stability: Swarm & Merge-Manager Continuity Handover'
status: in-progress
type: epic
priority: high
created_at: 2026-11-24T08:06:16Z
updated_at: 2026-11-24T10:55:52Z
---

## 0. Swarm Work-Item Contract — `'Stability'` Epic Swarm (`qou-s028`)

A **Swarm** is a first-class work item (`type: epic` in `beans`) with explicit **Acceptance Criteria / End State**, **Structured Work-Item Queues**, **On-Demand + Optional Periodic Human-Consumable Status Reporting**, and **Live Cold-Start Handover Notes**.

### Defined End-State / Exit Criteria for the `'Stability'` Swarm
- [x] **EC-1 (Four Open Derivation Gaps Closed or Framed Under Rule-13a — COMPLETE ON `main`):** All `9/9` Open-Gap PRs (`#9245, #9278` `⁴He`; `#9247, #9249` `m_τ`; `#9251, #9253` `N_gen = 3`; `#9255, #9257, #9240` `a₀`) proved (`0 sorry`), 80-dps SHA-stamped, and **MERGED** onto `origin/main` (plus survey/slides synced in **MERGED `#9298`**).
- [ ] **EC-2 (Precision & Anchor Hygiene Gates Green):** `#9237` (`63 -> 21`) & `#9303` (`7` dashboard witnesses) **MERGED**; `#9293` + `#9302` (`21 -> 0` `q0_anchor_ratchet.py --strict` & `precision-gates.sh` exit `0`) queued in Merge Train 5.
- [ ] **EC-3 (Monograph One-Voice & Commentary Ratchets at Zero + `Convention C/D` Excised):**
  * `voice-leak-baseline.json` shrunk to `{}` (**MERGED `#9271`**); Ch. 6/core (**MERGED `#9288`**) + Tranche B (**MERGED `#9300`**) landed; `mass-theory` (`#9296 + #9305`), MBA (`#9280`), Ch. 1–8/SM (`#9314`), and Ch. 12–16 + `L5` hard ratchet (`#9311`) in Merge Trains 4 & 5; final `2` blocks + `authors-note` fence exemption in flight on `ws3-l2-physics`.
- [ ] **EC-4 (`Epic qou-xip2` Backlog Drain, Wave C & Post-Merge Bean Reconciliation):** Batches `1–8` (`#9237, #9238, #9259, #9241, #9261, #9263, #9265, #9267`) + `#9276` + `#8161` **MERGED**; Batches `9–10` (`#9269`), Wave C (`#8351, #8392, #8393`), and automated post-merge bean reconciler (`#9309` `scripts/close-merged-pr-beans.py`) in Merge Trains 4 & 5; Tranche 2 `origin/main` bean reconciliation active on `main-base`.
- [ ] **EC-5 (Owner Architectural Decisions `Q2`, `Q3`, `Q4` & Swarm/Merge KG Landed):**
  * **Q2 Option 1 (`qou-wywz`):** **COMPLETE & MERGED (`#9286`)**.
  * **Swarm/Merge-Train/Sibling-Launch Skills:** `qou` skills **MERGED (`#9290`)**; `cat-harness` KG (`#1397`) running CI for `merge-guard.ts 1397 --merge`.
  * **Q3 Option 1 (`qou-lref`):** Stage 1 (`0` outbound `QOU.*` cut-edges + `apply-lean-reservoir-migration.py`) **MERGED (`#9274`)**; Stage 2 (`7` Reservoir `[[lean_lib]]`s + `83 -> 12` `QOU.<Chapter>` dirs) running single-core `.olean` sweep on `ws4-mathlib-infra` -> merge -> `--fixup-branch` across remaining open PRs.
  * **Q4 Option 1 (`qou-mba8`, `qou-anx0`, `qou-lanx`):** Tranche 1 (`9`-block $\mathcal{L}_0\text{--}\mathcal{L}_4$ QOU-Delta Algorithms Annex, `#9280`) queued in Merge Train 5; Tranche 2 (`14 -> 6` Annexes `A–F` + 80-dps Fréchet–Jacobian master reference tables) finalizing on `ws5-nov19-rebase`.

---

## Purpose — Cold-Start Continuity & Stall-Safe Handover (`qou-s028`)

This **Stability** Swarm epic is updated and pushed to `origin/cat/cat-harness/beans` on **every routine Swarm Monitor checkin** (currently `*/10 * * * *` periodic mode, and also renderable on-demand anytime). If the active Swarm Coordinator / Merge Manager ever stalls, runs out of context, or disconnects, **any successor agent reading this single bean (`beans show qou-s028`) has 100% of the end-state criteria, work-item queues, owner rulings, fences, worktree map, and commands required to take over seamlessly in `< 60` seconds.**

- **Last Heartbeat Refresh:** `2026-11-24T10:55:51Z` (`2026-11-24 05:55:51 `)
- **`litlfred/qou` `origin/main` Tip:** `8ec51e68547`
- **Live Queue Counts (`litlfred/qou`):** Open PRs = `181` (`171` Ready / `10` Draft) · Merged Since `2026-11-23` = `83` (latest: #9316, #9314, #9309, #9307, #9305, #9303, #9300, #9298, #9296, #9292, #9290, #9288) · Open GitHub Issues = `83`
- **Disk Health (`/`):** `/dev/disk3s1s1  927G  914G   14G  99% /`

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
| `merge-runner` | `mt-local/8393` @ `43690ea36e3` (`dirty=0`) | Serial prepare-merge-auto Runner onto origin/main (Wave A -> Wave B -> Wave C) | test(qou): add 80-dps witness for Round 84 probe (scriptCommitSha 02a557115 |
| `ws6-exposition-pdf` | `claude/link-audit-refutations-x60n-20261124` @ `32a5731e343` (`dirty=234`) | Q1 Staged-Branch PR Opener (Wave B, 14 branches) & Completed-Workitem Open-PR Auditor (Wave C) | docs(outreach): sync pbs-spacetime-survey article, slides & SVGs with lande |
| `ws4-mathlib-infra` | `claude/q3-lean-reservoir-libs-codemod-20261124` @ `2896ccb1a7f` (`dirty=1`) | Q3 Option 1: Lean 83->12 QOU.<Chapter> Subgraphs + 7 Top-Level Reservoir lean_libs + apply-lean-reservoir-migration.py --fixup-branch + skill updates | refactor(lean,qou-lref): execute Q3 Option 1 7+1 lean_lib isolation & 83->1 |
| `main-base` | `HEAD` @ `ba5be11d5aa` (`dirty=0`) | Q2 Option 1: Three-Stop Leibniz Relational Spine (Ch. 0 intro, Ch. 2 Rieffel/Jimbo, Ch. 13 Fefferman Lorentzian) + live DOIs | fix(witness): sync scriptHash and scriptCommitSha on lp-confinement-nf-forc |
| `ws5-nov19-rebase` | `claude/borromean-recompute-derived-w-bisect-20261124` @ `ba5be11d5aa` (`dirty=0`) | Q4 Option 1: Compact 9-Block L0-L4 Algorithms Annex (fixing 6 bugs) + 14->6 Annexes A-F with 80-dps Frechet-Jacobian Master Tables | fix(witness): sync scriptHash and scriptCommitSha on lp-confinement-nf-forc |
| `ws12-pr9180` | `claude/crosscheck-jingliu-dubois-squier-20261124` @ `a922c21d1ae` (`dirty=13`) | Gap 1B (qou-3kkz): 4He Tetrahedral K_4 Flux-Ring & 462D 3D Jacobi Variational Compression + idle beans qou-bgur, qou-kjik | docs(results,gap3): record Bring Z_3 Kummer-Prym N_gen=3 theorems, F_3[S_5] |
| `ws1-precision` | `claude/ws1-final-3-q0-witnesses-20261124` @ `a12cb085c11` (`dirty=0`) | ws1-precision (#9104): 12-Witness q0 Precision Refill (11/12 all_nuclides_sdp + gates) + idle beans qou-n2dp, qou-5d0x | precision-gates: clear new CODATA stale-edition and witness-value-copy regr |
| `ws15-p3-p5-p6` | `claude/drain-5c64-5pgl-2g9j-compute-20261124` @ `ba5be11d5aa` (`dirty=0`) | ws1-precision Witness 12/12 (markov-trace-two-row-tower-rust) + idle beans qou-73kb, qou-m1tr | fix(witness): sync scriptHash and scriptCommitSha on lp-confinement-nf-forc |
| `ws2-bridge-hecke` | `claude/frobenius-gram-a71h-z21-bisect-85o2-20261124` @ `ba5be11d5aa` (`dirty=0`) | q0-Anchor Final 21 Consistency Drain (qou-q0rf) + idle beans qou-jdrx, qou-ke35 | fix(witness): sync scriptHash and scriptCommitSha on lp-confinement-nf-forc |
| `ws3-l2-physics` | `claude/bach2013-double-slit-and-bib-1qhv-20261124` @ `ba5be11d5aa` (`dirty=0`) | One-Voice Final 31->0 Monograph Commentary-Audit Drain (paper-commentary-audit.ts ratchet -> 0) | fix(witness): sync scriptHash and scriptCommitSha on lp-confinement-nf-forc |

---

## 3. Live Sampled Compute / Sweep Processes

- `23534 0.0 7536 01:06:33 python3 scripts/lean-library-sweep.py --package HeckeTemperleyLieb --jobs 1 --shadow /tmp/ws51-codemod-sha`
- `77153 0.0 1184 01:32:26 zsh -c cd /Users/litlfred/space_cats/qou-wt/ws4-mathlib-infra && \\012export LEAN_NUM_THREADS=1 RAYON_NUM_`

---

## 4. Highest-Numbered Active Ready PRs on `litlfred/qou` (Merge-Runner Queue)

- #9321 (`claude/witness-repair-g5oz-q3f7-20261124`): fix(qbeta,mass-table): resolve red qou-g5oz level-k probe & refresh 80
- #9320 (`claude/pauli-lock-inst-d6-nu-o43i-1a69-20261124`): feat(qou-o43i,qou-1a69): formalize Pauli-lock spin/isospin diagnostic 
- #9318 (`claude/commentary-final2-and-bib-2joi-5sg8-20261124`): feat(pipeline,bib): exempt authors-note in paper-commentary-audit & ve
- #9311 (`claude/commentary-audit-ch12-16-and-l5-ratchet-20261124`): prose(physics,dynamics,pipeline): drain 20 paper-commentary-audit hits
- #9302 (`claude/ws1-final-3-q0-witnesses-20261124`): fix(precision): regenerate final 3 q0-anchor refill witnesses & restor
- #9293 (`claude/q0-anchor-final-21-drain-20261124`): fix(precision,q0-anchor): drain remaining 18 in-scope q0-anchor witnes
- #9269 (`claude/backlog-drain-batch9-10-20261123`): feat(qou-7igi,qou-mr7s): Backlog Drain Batches 9-10 ClassicalTraceFloo
- #9243 (`claude/prior-art-doi-verified-pkg-20261123`): bib,intro,qou: add live-DOI-verified consolidated prior-art package (q
- #9217 (`claude/project-thread-di0nax`): Public release prep: CITATION.cff
- #9178 (`claude/exposition-statement-rulings-2026-11-16`): Exposition: owner rulings on false or under-derived statements
- #9174 (`claude/convention-c-ledger-2026-11-21`): convention-C ledger: adjudicate the 8 unadjudicated comparison sites
- #9159 (`claude/project-thread-ipc33x`): Corpus-grep path 7 (block QA sidecar); fits_AME labelled as comparison
- #9045 (`claude/merge-coordinator-memory-2026-11-22`): merge-coordinator memory: rebase-merge 405 with no merge commit

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
