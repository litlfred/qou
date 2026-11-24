---
# qou-s028
title: 'Stability: Swarm & Merge-Manager Continuity Handover'
status: in-progress
type: epic
priority: high
created_at: 2026-11-24T08:06:16Z
updated_at: 2026-11-24T09:40:51Z
---

## 0. Swarm Work-Item Contract — `'Stability'` Epic Swarm (`qou-s028`)

A **Swarm** is a first-class work item (`type: epic` in `beans`) with explicit **Acceptance Criteria / End State**, **Structured Work-Item Queues**, **On-Demand + Optional Periodic Human-Consumable Status Reporting**, and **Live Cold-Start Handover Notes**.

### Defined End-State / Exit Criteria for the `'Stability'` Swarm
- [ ] **EC-1 (Four Open Derivation Gaps Closed or Framed Under Rule-13a):** Routes `1A, 1B` (`⁴He`), `2A, 2B` (`m_τ`), `3A, 3B` (`N_gen = 3`), and `4A, 4B, 4C` (`a₀` — `#9240` **MERGED**) proved (`0 sorry`), 80-dps SHA-stamped, PR'd, and merged onto `origin/main`.
- [ ] **EC-2 (Precision & Anchor Hygiene Gates Green):** `ws1-precision` (`12/12` witnesses, `#9104`) and `q0-anchor` consistency drain (`63 -> 21` **MERGED** in `#9237`; final `21 -> 0` in flight) verified and merged onto `origin/main`.
- [ ] **EC-3 (Monograph One-Voice Ratchet at Zero & `Convention C` Excised from External Reader):**
  * All non-fenced `voice-leak-audit.ts` hits drained `20 -> 0` and `voice-leak-baseline.json` shrunk to `{}` (**PR `#9271` OPEN & VERIFIED**, queued in `prepare-merge-auto`).
  * **Bean `qou-xu3c` (`2026-11-24` owner directive):** Excise all `163` lines across `105` external-reader `.md` files referencing discarded internal `"Convention C"` / `"z_C"` (and internal `"Convention D"` label archaeology), starting with Chapter 6 (`braids-and-knots`, `5` files), and enforce a permanent `voice-leak-audit.ts` ban rule.
- [ ] **EC-4 (`Epic qou-xip2` Backlog Drain & Completed-Workitem Open PRs Merged):** All `10/10` backlog-drain batches (`#9237` **MERGED**, `#9238/#9241` + Batches `3,5,6,7,8,9–10` in Wave A/B) and all vetted completed-workitem existing open PRs (`Wave C`) merged via `prepare-merge-auto` (`MISSING: 0`).
- [ ] **EC-5 (Owner Architectural Decisions `Q2`, `Q3`, `Q4` Landed):**
  * **Q2 Option 1 (`qou-wywz`):** Three-stop Leibniz relational spine across Ch. 0, Ch. 2 & Ch. 13 + live DOIs merged.
  * **Q3 Option 1 (`qou-lref`):** `MathlibExt` + `6` standalone Reservoir `[[lean_lib]]`s (`0` outbound `QOU.*` cut-edges) + `83 -> 12` `QOU.<Chapter>` dirs merged, `.claude/skills/local/` updated, and remaining open PRs fixed up via `scripts/apply-lean-reservoir-migration.py --fixup-branch`.
  * **Q4 Option 1 (`qou-mba8`, `qou-anx0`, `qou-lanx`):** Compact `9`-block $\mathcal{L}_0\text{--}\mathcal{L}_4$ QOU-Delta Algorithms Annex + `14 -> 6` consolidated Annexes (`A–F`) with 80-dps Fréchet–Jacobian master reference tables merged.

---

## Purpose — Cold-Start Continuity & Stall-Safe Handover (`qou-s028`)

This **Stability** Swarm epic is updated and pushed to `origin/cat/cat-harness/beans` on **every routine Swarm Monitor checkin** (currently `*/10 * * * *` periodic mode, and also renderable on-demand anytime). If the active Swarm Coordinator / Merge Manager ever stalls, runs out of context, or disconnects, **any successor agent reading this single bean (`beans show qou-s028`) has 100% of the end-state criteria, work-item queues, owner rulings, fences, worktree map, and commands required to take over seamlessly in `< 60` seconds.**

- **Last Heartbeat Refresh:** `2026-11-24T09:40:50Z` (`2026-11-24 04:40:50 `)
- **`litlfred/qou` `origin/main` Tip:** `106137b4b10`
- **Live Queue Counts (`litlfred/qou`):** Open PRs = `198` (`188` Ready / `10` Draft) · Merged Since `2026-11-23` = `63` (latest: #9288, #9286, #9282, #9278, #9274, #9273, #9271, #9257, #9255, #9253, #9249, #9247) · Open GitHub Issues = `96`
- **Disk Health (`/`):** `/dev/disk3s1s1  927G  911G   16G  99% /`

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
| `merge-runner` | `mt-local/9284` @ `130b5cd13b3` (`dirty=0`) | Serial prepare-merge-auto Runner onto origin/main (Wave A -> Wave B -> Wave C) | chore(witness): stamp 80-dps strong-unified-binding-probe witness (qou-kjik |
| `ws6-exposition-pdf` | `claude/commentary-audit-mass-theory-zero-20261124` @ `47438a90a2f` (`dirty=0`) | Q1 Staged-Branch PR Opener (Wave B, 14 branches) & Completed-Workitem Open-PR Auditor (Wave C) | docs(mass-theory): drain paper-commentary-audit from 22/859 to 0/859 failur |
| `ws4-mathlib-infra` | `claude/q3-lean-reservoir-libs-codemod-20261124` @ `2896ccb1a7f` (`dirty=1`) | Q3 Option 1: Lean 83->12 QOU.<Chapter> Subgraphs + 7 Top-Level Reservoir lean_libs + apply-lean-reservoir-migration.py --fixup-branch + skill updates | refactor(lean,qou-lref): execute Q3 Option 1 7+1 lean_lib isolation & 83->1 |
| `main-base` | `claude/wire-merge-train-and-bean-drain-20261124` @ `711de6a488d` (`dirty=3`) | Q2 Option 1: Three-Stop Leibniz Relational Spine (Ch. 0 intro, Ch. 2 Rieffel/Jimbo, Ch. 13 Fefferman Lorentzian) + live DOIs | docs(lean): clarify comparability vs adjacency in Orbit3Braid docstring (qo |
| `ws5-nov19-rebase` | `claude/q4b-annex-80dps-master-tables-6annexes-20261124` @ `356fcf0e6b0` (`dirty=659`) | Q4 Option 1: Compact 9-Block L0-L4 Algorithms Annex (fixing 6 bugs) + 14->6 Annexes A-F with 80-dps Frechet-Jacobian Master Tables | feat(qou-mba8,qou-nmjd): rebuild compact 9-block L0-L4 algorithms annex and |
| `ws12-pr9180` | `claude/commentary-audit-body-ch7-10-zero-20261124` @ `711de6a488d` (`dirty=0`) | Gap 1B (qou-3kkz): 4He Tetrahedral K_4 Flux-Ring & 462D 3D Jacobi Variational Compression + idle beans qou-bgur, qou-kjik | docs(lean): clarify comparability vs adjacency in Orbit3Braid docstring (qo |
| `ws1-precision` | `claude/hygiene-n2dp-5d0x-refs-20261124` @ `711de6a488d` (`dirty=0`) | ws1-precision (#9104): 12-Witness q0 Precision Refill (11/12 all_nuclides_sdp + gates) + idle beans qou-n2dp, qou-5d0x | docs(lean): clarify comparability vs adjacency in Orbit3Braid docstring (qo |
| `ws15-p3-p5-p6` | `claude/framed-braid-twist-srow3-kebu-jkmh-20261124` @ `ccaa5874ff3` (`dirty=0`) | ws1-precision Witness 12/12 (markov-trace-two-row-tower-rust) + idle beans qou-73kb, qou-m1tr | witness(qou-kebu,qou-jkmh): stamp 80-dps framed braid monodromy & sRow3 aud |
| `ws2-bridge-hecke` | `claude/dashboard-witnesses-w1u2-20261124` @ `208e9e31b66` (`dirty=0`) | q0-Anchor Final 21 Consistency Drain (qou-q0rf) + idle beans qou-jdrx, qou-ke35 | chore(witness): regenerate 7 upstream dashboard witnesses with upstream has |
| `ws3-l2-physics` | `claude/commentary-audit-ch12-16-and-l5-ratchet-20261124` @ `06d7cbbf649` (`dirty=0`) | One-Voice Final 31->0 Monograph Commentary-Audit Drain (paper-commentary-audit.ts ratchet -> 0) | feat(pipeline): add L5 Convention C and z_C ban to voice-leak-audit (qou-xu |

---

## 3. Live Sampled Compute / Sweep Processes

- `77153 0.0 1200 17:25 zsh -c cd /Users/litlfred/space_cats/qou-wt/ws4-mathlib-infra && \\012export LEAN_NUM_THREADS=1 RAYON_NUM_THR`
- `90653 0.0 14752 15:23 python3 scripts/lean-library-sweep.py --package MathlibExt --jobs 1 --shadow /tmp/ws51-codemod-shadow`

---

## 4. Highest-Numbered Active Ready PRs on `litlfred/qou` (Merge-Runner Queue)

- #9307 (`claude/framed-braid-twist-srow3-kebu-jkmh-20261124`): feat(qou-kebu,qou-jkmh): FramedBraidWord semidirect monoid & Nat.Parti
- #9305 (`claude/commentary-audit-mass-theory-zero-20261124`): docs(mass-theory): drain paper-commentary-audit from 22/859 to 0/859 f
- #9303 (`claude/dashboard-witnesses-w1u2-20261124`): fix(dashboard,precision): regenerate 7 upstream dashboard witnesses, d
- #9302 (`claude/ws1-final-3-q0-witnesses-20261124`): fix(precision): regenerate final 3 q0-anchor refill witnesses & restor
- #9300 (`claude/excise-convention-c-corpus-and-ratchet-20261124`): prose(monograph,pipeline): excise Convention C/D labels across Tranche
- #9298 (`claude/pbs-survey-sync-closed-gaps-20261124`): docs(outreach): sync pbs-spacetime-survey article, slides & SVGs with 
- #9296 (`claude/excise-convention-c-mass-theory-20261124`): docs(mass-theory): excise Convention C and internal Convention D label
- #9293 (`claude/q0-anchor-final-21-drain-20261124`): fix(precision,q0-anchor): drain remaining 18 in-scope q0-anchor witnes
- #9292 (`claude/backlog-drain-73kb-m1tr-20261124`): feat(qou-73kb,qou-m1tr): characteristic-free Specht standard basis & 4
- #9290 (`claude/fixup-qou-merge-and-sibling-launch-skills-20261124`): docs(skills): align merge/watch skills with Process_MergeTrain & add s
- #9284 (`claude/strong-unified-binding-audit-qou-kjik-20261124`): fix(nuclear): label strong_unified_binding_probe as 80-dps anchor-inve
- #9280 (`claude/q4a-mba-9block-algorithms-annex-20261124`): feat(qou-mba8,qou-nmjd): compact 9-block L_0--L_4 QOU-Delta Algorithms
- #9276 (`claude/salvage-8143-jekutieli-d2-20261124`): feat(lean,probes,qou-wp3h): salvage #8143 D2 hook converse & Yekutieli
- #9269 (`claude/backlog-drain-batch9-10-20261123`): feat(qou-7igi,qou-mr7s): Backlog Drain Batches 9-10 ClassicalTraceFloo
- #9267 (`claude/backlog-drain-batch8-20261123`): feat(qou-tw5j,qou-q4te): Backlog Drain Batch 8 Bring Sp(8,F2) theta or
- #9265 (`claude/backlog-drain-batch7-20261123`): feat(qou-i9q6,qou-rtjc): Backlog Drain Batch 7 S(U(3)xU(2)) Z_6 iso, H
- #9263 (`claude/backlog-drain-batch6-20261123`): feat(qou-rp3g,qou-ra4e): Backlog Drain Batch 6 C1ConnectionAlgebraicId
- #9261 (`claude/backlog-drain-batch5-20261123`): feat(qou-k8oj,qou-i7r4,qou-v2ef): Backlog Drain Batch 5 TracedVolumeVs

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
