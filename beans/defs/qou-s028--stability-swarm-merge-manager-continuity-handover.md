---
# qou-s028
title: 'Stability: Swarm & Merge-Manager Continuity Handover'
status: in-progress
type: epic
priority: high
created_at: 2026-11-24T08:06:16Z
updated_at: 2026-11-24T08:06:49Z
---

## 0. Swarm Work-Item Contract — `'Stability'` Epic Swarm (`qou-s028`)

A **Swarm** is a first-class work item (`type: epic` in `beans`) with explicit **Acceptance Criteria / End State**, **Structured Work-Item Queues**, **On-Demand + Optional Periodic Human-Consumable Status Reporting**, and **Live Cold-Start Handover Notes**.

### Defined End-State / Exit Criteria for the `'Stability'` Swarm
- [ ] **EC-1 (Four Open Derivation Gaps Closed or Framed Under Rule-13a):** Routes `1A, 1B` (`⁴He`), `2A, 2B` (`m_τ`), `3A, 3B` (`N_gen = 3`), and `4A, 4B, 4C` (`a₀` — `#9240` **MERGED**) proved (`0 sorry`), 80-dps SHA-stamped, PR'd, and merged onto `origin/main`.
- [ ] **EC-2 (Precision & Anchor Hygiene Gates Green):** `ws1-precision` (`12/12` witnesses, `#9104`) and `q0-anchor` consistency drain (`63 -> 21` **MERGED** in `#9237`; final `21 -> 0` in flight) verified and merged onto `origin/main`.
- [ ] **EC-3 (Monograph One-Voice Ratchet at Zero):** All non-fenced `voice-leak-audit.ts` hits drained `20 -> 0` and `voice-leak-baseline.json` shrunk to `{}` (**PR `#9271` OPEN & VERIFIED**, queued in `prepare-merge-auto`).
- [ ] **EC-4 (`Epic qou-xip2` Backlog Drain & Completed-Workitem Open PRs Merged):** All `10/10` backlog-drain batches (`#9237` **MERGED**, `#9238/#9241` + Batches `3,5,6,7,8,9–10` in Wave A/B) and all vetted completed-workitem existing open PRs (`Wave C`) merged via `prepare-merge-auto` (`MISSING: 0`).
- [ ] **EC-5 (Owner Architectural Decisions `Q2`, `Q3`, `Q4` Landed):**
  * **Q2 Option 1 (`qou-wywz`):** Three-stop Leibniz relational spine across Ch. 0, Ch. 2 & Ch. 13 + live DOIs merged.
  * **Q3 Option 1 (`qou-lref`):** `MathlibExt` + `6` standalone Reservoir `[[lean_lib]]`s (`0` outbound `QOU.*` cut-edges) + `83 -> 12` `QOU.<Chapter>` dirs merged, `.claude/skills/local/` updated, and remaining open PRs fixed up via `scripts/apply-lean-reservoir-migration.py --fixup-branch`.
  * **Q4 Option 1 (`qou-mba8`, `qou-anx0`, `qou-lanx`):** Compact `9`-block $\mathcal{L}_0	ext{--}\mathcal{L}_4$ QOU-Delta Algorithms Annex + `14 -> 6` consolidated Annexes (`A–F`) with 80-dps Fréchet–Jacobian master reference tables merged.

---

## Purpose — Cold-Start Continuity & Stall-Safe Handover (`qou-s028`)

This **Stability** Swarm epic is updated and pushed to `origin/cat/cat-harness/beans` on **every routine Swarm Monitor checkin** (currently `*/10 * * * *` periodic mode, and also renderable on-demand anytime). If the active Swarm Coordinator / Merge Manager ever stalls, runs out of context, or disconnects, **any successor agent reading this single bean (`beans show qou-s028`) has 100% of the end-state criteria, work-item queues, owner rulings, fences, worktree map, and commands required to take over seamlessly in `< 60` seconds.**

- **Last Heartbeat Refresh:** `2026-11-24T08:06:48Z` (`2026-11-24 03:06:48 `)
- **`litlfred/qou` `origin/main` Tip:** `169287f3063`
- **Live Queue Counts (`litlfred/qou`):** Open PRs = `199` (`189` Ready / `10` Draft) · Merged Since `2026-11-23` = `43` (latest: #9240, #9238, #9237, #9236, #9232, #9221, #9219, #9216, #9213, #9212, #9211, #9210) · Open GitHub Issues = `95`
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
4. **Q4 Option 1 (`qou-mba8`, `qou-anx0`, `qou-lanx`, `qou-nmjd` — Authorized):** Rebuild `appendix-mass-binding-algorithms` into the compact `9`-block $\mathcal{L}_0	ext{--}\mathcal{L}_4$ QOU-Delta Algorithms Annex (fixing all 6 mathematical contradictions + stripping `CAL-1/2/3` & `../../../` leaks) and consolidate all `14` back-matter appendices into `6` Annexes (`A–F`) with uniform 80-dps witness-backed master reference tables & propagated $(m_e, \mathfrak{D}_eta, m_\pi)$ uncertainties.
5. **`/idle-backlog` Compute-Wait Rule (`2026-11-24`):** Any sibling waiting on background single-core compute MUST pull right-scoped, non-compute-heavy beans (without running `git checkout` mid-build) instead of sleeping on timers.
6. **STRICT PUBLIC-RELEASE & DO-NOT-MERGE FENCE:**
   - NEVER touch or merge PR `#9217`, Active Set 1 PRs (`#9178, #9176, #9174, #8734, #8692, #8735`), or DO-NOT-MERGE PR `#8150` (refuted $S_5$ theta characteristics).
   - NEVER touch `CITATION.cff`, `home_page/`, `README.md`, `CONTRIBUTING.md`, `CONTRIBUTORS.md`, `authors-note/`, `scripts/build-site.sh`, `scripts/publish-main-local.sh`, or `/Users/litlfred/space_cats/qou` working tree (owned by external public-release agent).
   - Git author MUST be `litlfred <litlfred@users.noreply.github.com>` everywhere. Single-threaded resource caps (`nice -n 10`, `LEAN_NUM_THREADS=1`, `OMP_NUM_THREADS=1`, `RAYON_NUM_THREADS=1`, NO `lake build`). `NO FITTING EXCEPT CAL-1/2/3`, `mp.dps = 80`, zero `float64`.
7. **10-Minute Human-Consumable Scorecard Cadence:** Schedule `*/10 * * * *` (`ExactTiming: true`), report plain-English progress with ZERO opaque internal shorthands, and run `sync_stability_epic.py` on every tick to refresh and push `qou-s028` to `origin/cat/cat-harness/beans`.

---

## 2. Live 10-Worktree Ownership & Branch Map (`/Users/litlfred/space_cats/qou-wt/*`)

| Worktree | Checked-Out Branch & HEAD | Assigned Track & Responsibility | Latest Commit Subject |
| :--- | :--- | :--- | :--- |
| `merge-runner` | `claude/backlog-drain-batch4-20261123` @ `a3e10e93ae1` (`dirty=4`) | Serial prepare-merge-auto Runner onto origin/main (Wave A -> Wave B -> Wave C) | docs(qou-qmh2,qou-rilj): record consolidating PR #9241 and executed issue a |
| `ws6-exposition-pdf` | `claude/gap2b-mtau-s3-circulant-koide-test-20261123` @ `3465c90bf3f` (`dirty=0`) | Q1 Staged-Branch PR Opener (Wave B, 14 branches) & Completed-Workitem Open-PR Auditor (Wave C) | docs(gap2b): document 80-dps S3/Z3 circulant Koide & q0 phase test results  |
| `ws4-mathlib-infra` | `claude/q3-lean-reservoir-libs-isolate-20261124` @ `edaa9286445` (`dirty=0`) | Q3 Option 1: Lean 83->12 QOU.<Chapter> Subgraphs + 7 Top-Level Reservoir lean_libs + apply-lean-reservoir-migration.py --fixup-branch + skill updates | docs(probes): add qou-slfm Reeb length/time & LCQ Bekenstein-Hawking analys |
| `main-base` | `consolidate/fix-mass-theory-latex-pdf-errors` @ `25ed94c6271` (`dirty=0`) | Q2 Option 1: Three-Stop Leibniz Relational Spine (Ch. 0 intro, Ch. 2 Rieffel/Jimbo, Ch. 13 Fefferman Lorentzian) + live DOIs | fix(bib,braids-and-knots): wrap math subscripts in 2 bib titles and fix kro |
| `ws5-nov19-rebase` | `consolidate/ws9-qa-doublekind-latex-and-chaptering` @ `b6265d1bf7b` (`dirty=0`) | Q4 Option 1: Compact 9-Block L0-L4 Algorithms Annex (fixing 6 bugs) + 14->6 Annexes A-F with 80-dps Frechet-Jacobian Master Tables | fix(monograph): strip double-kind prefixes, fix appendix chaptering, LaTeX  |
| `ws12-pr9180` | `claude/gap1b-4he-tetrahedral-k4-flux-ring-20261123` @ `9e1b128756e` (`dirty=0`) | Gap 1B (qou-3kkz): 4He Tetrahedral K_4 Flux-Ring & 462D 3D Jacobi Variational Compression + idle beans qou-bgur, qou-kjik | fix(probes): compare unrounded 80-dps A=2 energies in assertion 6 & update  |
| `ws1-precision` | `consolidate/ws1-precision-gates-green` @ `0a0747aad57` (`dirty=0`) | ws1-precision (#9104): 12-Witness q0 Precision Refill (11/12 all_nuclides_sdp + gates) + idle beans qou-n2dp, qou-5d0x | all_nuclides_sdp_admissibility_mp: deduplicate LP solves by A in bounded-RS |
| `ws15-p3-p5-p6` | `claude/ws1-precision-witnesses-11-12-20261124` @ `2685f2c715b` (`dirty=0`) | ws1-precision Witness 12/12 (markov-trace-two-row-tower-rust) + idle beans qou-73kb, qou-m1tr | q0 refill: re-run leray-dss-logphase seed1-C4 (#9104) |
| `ws2-bridge-hecke` | `claude/q0-anchor-final-21-drain-20261124` @ `c5351ea8e98` (`dirty=1`) | q0-Anchor Final 21 Consistency Drain (qou-q0rf) + idle beans qou-jdrx, qou-ke35 | fix(q0-anchor): migrate & declare proton/independent anchors at 80 dps in p |
| `ws3-l2-physics` | `claude/bib-qa-hygiene-nq4h-tv74-20261124` @ `169287f3063` (`dirty=0`) | One-Voice Final 31->0 Monograph Commentary-Audit Drain (paper-commentary-audit.ts ratchet -> 0) | chore(manifest): stamp additive q0_anchor_manifest with suffixed producers  |

---

## 3. Live Sampled Compute / Sweep Processes

- `58921 0.0 1216 12:58 zsh -c WT=/Users/litlfred/space_cats/qou-wt/ws2-bridge-hecke\012cd "$WT" && \\012git status --short && \\012g`
- `61190 90.1 72336 12:34 python3 -u computations/probes/six_strand_photon_pair/six_strand_pair_probe.py`
- `50619 0.0 1232 22:20 zsh -c export LEAN_NUM_THREADS=1 RAYON_NUM_THREADS=1 OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS`
- `50628 0.0 512 22:20 /usr/bin/time -l nice -n 10 python3 -u computations/all_nuclides_sdp_admissibility_mp.py 92 160`
- `50629 88.5 34896 22:20 python3 -u computations/all_nuclides_sdp_admissibility_mp.py 92 160`
- `80760 88.6 872000 03:10 python3 -u computations/probes/gap1b_4he_tetrahedral_k4_flux_ring/gap1b_4he_tetrahedral_k4_flux_ring_probe`

---

## 4. Highest-Numbered Active Ready PRs on `litlfred/qou` (Merge-Runner Queue)

- #9271 (`claude/one-voice-final-31-drain-20261124`): fix(one-voice): drain remaining non-fenced voice leaks (31 -> 11; base
- #9269 (`claude/backlog-drain-batch9-10-20261123`): feat(qou-7igi,qou-mr7s): Backlog Drain Batches 9-10 ClassicalTraceFloo
- #9267 (`claude/backlog-drain-batch8-20261123`): feat(qou-tw5j,qou-q4te): Backlog Drain Batch 8 Bring Sp(8,F2) theta or
- #9265 (`claude/backlog-drain-batch7-20261123`): feat(qou-i9q6,qou-rtjc): Backlog Drain Batch 7 S(U(3)xU(2)) Z_6 iso, H
- #9263 (`claude/backlog-drain-batch6-20261123`): feat(qou-rp3g,qou-ra4e): Backlog Drain Batch 6 C1ConnectionAlgebraicId
- #9261 (`claude/backlog-drain-batch5-20261123`): feat(qou-k8oj,qou-i7r4,qou-v2ef): Backlog Drain Batch 5 TracedVolumeVs
- #9259 (`claude/backlog-drain-batch3-20261123`): feat(qou-c8sz,qou-qj21,qou-1c2a): Backlog Drain Batch 3 qInt bridges, 
- #9257 (`claude/gap4b-oqsu2-haar-entanglement-first-law-20261123`): feat(gravity,lean,probes): Gap 4B O_q(SU(2)) Haar modular entanglement
- #9255 (`claude/gap4-a0-fefferman-lorentzian-modular-20261123`): feat(gravity,lean,probes): Gap 4A Fefferman 4D Lorentzian CR metric & 
- #9253 (`claude/gap3b-t29-composite-decay-threshold-20261123`): feat(sm,lean,probes): Gap 3B T(2,9) -> 3xT(2,3) threshold, Hecke fissi
- #9251 (`claude/gap3-ngen3-bring-prym-riemann-roch-20261123`): feat(sm,lean,probes): Gap 3A Bring Z_3 Kummer-Prym Riemann-Roch N_gen=
- #9249 (`claude/gap2b-mtau-s3-circulant-koide-test-20261123`): feat(sm,lean,probes): Gap 2B S_3/Z_3-circulant Koide trace identity & 
- #9247 (`claude/gap2-mtau-hyperbolic-census-torsion-20261123`): feat(sm,lean,probes): Gap 2A <=8x 3-braid hyperbolic census, torsion t
- #9245 (`claude/gap1-4he-wigner-pauli-12q-20261123`): feat(nuclear,lean,probes): Gap 1A 4He 12q Pauli antisymmetrizer & Wign
- #9243 (`claude/prior-art-doi-verified-pkg-20261123`): bib,intro,qou: add live-DOI-verified consolidated prior-art package (q
- #9241 (`claude/backlog-drain-batch4-20261123`): feat(qou-143e,qou-qmh2,qou-rilj): Backlog Drain Batch 4 Lean 4 theorem
- #9234 (`claude/sm8w-strong-cp-theta-qcd-string-tension-20261123`): feat(sm8w): Strong-CP theta_QCD=0 writhe/det cancellation & SU(3)_c Wi
- #9230 (`claude/sm8w-neutrino-unknot-sweedler-lift-20261123`): feat(sm): Non-zero unknot 0_1 neutrino Sweedler mass lift, Dirac/Major

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
