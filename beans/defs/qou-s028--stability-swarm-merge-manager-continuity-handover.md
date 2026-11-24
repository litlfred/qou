---
# qou-s028
title: 'Stability: Swarm & Merge-Manager Continuity Handover'
status: in-progress
type: epic
priority: high
created_at: 2026-11-24T08:06:16Z
updated_at: 2026-11-24T08:21:23Z
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
  * **Q4 Option 1 (`qou-mba8`, `qou-anx0`, `qou-lanx`):** Compact `9`-block $\mathcal{L}_0\text{--}\mathcal{L}_4$ QOU-Delta Algorithms Annex + `14 -> 6` consolidated Annexes (`A–F`) with 80-dps Fréchet–Jacobian master reference tables merged.

---

## Purpose — Cold-Start Continuity & Stall-Safe Handover (`qou-s028`)

This **Stability** Swarm epic is updated and pushed to `origin/cat/cat-harness/beans` on **every routine Swarm Monitor checkin** (currently `*/10 * * * *` periodic mode, and also renderable on-demand anytime). If the active Swarm Coordinator / Merge Manager ever stalls, runs out of context, or disconnects, **any successor agent reading this single bean (`beans show qou-s028`) has 100% of the end-state criteria, work-item queues, owner rulings, fences, worktree map, and commands required to take over seamlessly in `< 60` seconds.**

- **Last Heartbeat Refresh:** `2026-11-24T08:21:22Z` (`2026-11-24 03:21:22 `)
- **`litlfred/qou` `origin/main` Tip:** `d33a9b58054`
- **Live Queue Counts (`litlfred/qou`):** Open PRs = `196` (`186` Ready / `10` Draft) · Merged Since `2026-11-23` = `46` (latest: #9241, #9240, #9238, #9237, #9236, #9234, #9232, #9230, #9221, #9219, #9216, #9213) · Open GitHub Issues = `93`
- **Disk Health (`/`):** `/dev/disk3s1s1  927G  913G   14G  99% /`

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
7. **10-Minute Human-Consumable Scorecard Cadence:** Schedule `*/10 * * * *` (`ExactTiming: true`), report plain-English progress with ZERO opaque internal shorthands, and run `sync_stability_epic.py` on every tick to refresh and push `qou-s028` to `origin/cat/cat-harness/beans`.

---

## 2. Live 10-Worktree Ownership & Branch Map (`/Users/litlfred/space_cats/qou-wt/*`)

| Worktree | Checked-Out Branch & HEAD | Assigned Track & Responsibility | Latest Commit Subject |
| :--- | :--- | :--- | :--- |
| `merge-runner` | `claude/w7-chen-mult-integral-masstrace-20261123` @ `fc8eefbee82` (`dirty=3`) | Serial prepare-merge-auto Runner onto origin/main (Wave A -> Wave B -> Wave C) | chore(witness): add 80-dps w7-chen-multiplicative-integral witness (qou-9sj |
| `ws6-exposition-pdf` | `claude/salvage-8143-jekutieli-d2-20261124` @ `1a22157fe81` (`dirty=11`) | Q1 Staged-Branch PR Opener (Wave B, 14 branches) & Completed-Workitem Open-PR Auditor (Wave C) | chore(sm8w): stamp 80-dps witness for qou-tcpx Strong-CP & Wilson string te |
| `ws4-mathlib-infra` | `claude/q3-lean-reservoir-libs-isolate-20261124` @ `edaa9286445` (`dirty=6`) | Q3 Option 1: Lean 83->12 QOU.<Chapter> Subgraphs + 7 Top-Level Reservoir lean_libs + apply-lean-reservoir-migration.py --fixup-branch + skill updates | docs(probes): add qou-slfm Reeb length/time & LCQ Bekenstein-Hawking analys |
| `main-base` | `claude/q2-leibniz-relational-spine-20261124` @ `169287f3063` (`dirty=0`) | Q2 Option 1: Three-Stop Leibniz Relational Spine (Ch. 0 intro, Ch. 2 Rieffel/Jimbo, Ch. 13 Fefferman Lorentzian) + live DOIs | chore(manifest): stamp additive q0_anchor_manifest with suffixed producers  |
| `ws5-nov19-rebase` | `claude/q4a-mba-9block-algorithms-annex-20261124` @ `a053f8c64bb` (`dirty=0`) | Q4 Option 1: Compact 9-Block L0-L4 Algorithms Annex (fixing 6 bugs) + 14->6 Annexes A-F with 80-dps Frechet-Jacobian Master Tables | chore(witness): refresh SHA-stamped h4-gpmt-cumulant-ratio-and-lp-support w |
| `ws12-pr9180` | `claude/gap1b-4he-tetrahedral-k4-flux-ring-20261123` @ `9e1b128756e` (`dirty=0`) | Gap 1B (qou-3kkz): 4He Tetrahedral K_4 Flux-Ring & 462D 3D Jacobi Variational Compression + idle beans qou-bgur, qou-kjik | fix(probes): compare unrounded 80-dps A=2 energies in assertion 6 & update  |
| `ws1-precision` | `consolidate/ws1-precision-gates-green` @ `6eaa39aad47` (`dirty=0`) | ws1-precision (#9104): 12-Witness q0 Precision Refill (11/12 all_nuclides_sdp + gates) + idle beans qou-n2dp, qou-5d0x | q0 refill: re-run all-nuclides-sdp-admissibility-mp (#9104) |
| `ws15-p3-p5-p6` | `claude/ws1-precision-witnesses-11-12-20261124` @ `2685f2c715b` (`dirty=1`) | ws1-precision Witness 12/12 (markov-trace-two-row-tower-rust) + idle beans qou-73kb, qou-m1tr | q0 refill: re-run leray-dss-logphase seed1-C4 (#9104) |
| `ws2-bridge-hecke` | `claude/q0-anchor-final-21-drain-20261124` @ `c5351ea8e98` (`dirty=1`) | q0-Anchor Final 21 Consistency Drain (qou-q0rf) + idle beans qou-jdrx, qou-ke35 | fix(q0-anchor): migrate & declare proton/independent anchors at 80 dps in p |
| `ws3-l2-physics` | `claude/bib-qa-hygiene-nq4h-tv74-20261124` @ `169287f3063` (`dirty=0`) | One-Voice Final 31->0 Monograph Commentary-Audit Drain (paper-commentary-audit.ts ratchet -> 0) | chore(manifest): stamp additive q0_anchor_manifest with suffixed producers  |

---

## 3. Live Sampled Compute / Sweep Processes

- `44601 0.0 2544 02:51 zsh -c set -euo pipefail\012export LEAN_NUM_THREADS=1 OMP_NUM_THREADS=1 RAYON_NUM_THREADS=1 LEAN_NO_TREE_SYNC`
- `44988 89.7 56144 00:11 python3 computations/mpf_context_dps_audit.py --strict`
- `58921 0.0 1200 27:32 zsh -c WT=/Users/litlfred/space_cats/qou-wt/ws2-bridge-hecke\012cd "$WT" && \\012git status --short && \\012g`
- `61190 92.8 70400 27:08 python3 -u computations/probes/six_strand_photon_pair/six_strand_pair_probe.py`
- `25963 0.0 1264 05:31 zsh -c WT=/Users/litlfred/space_cats/qou-wt/ws15-p3-p5-p6\012cd "$WT/tools/hecke-engine" && \\012OMP_NUM_THRE`
- `25966 0.0 512 05:31 /usr/bin/time -l nice -n 10 /tmp/ws15-cargo-target/release/hecke-tower-trace --chain 9:10 --chain 10:11 --comp`
- `25968 92.7 83984 05:31 /tmp/ws15-cargo-target/release/hecke-tower-trace --chain 9:10 --chain 10:11 --compare ../../computations/pr`
- `80760 92.5 723856 17:44 python3 -u computations/probes/gap1b_4he_tetrahedral_k4_flux_ring/gap1b_4he_tetrahedral_k4_flux_ring_probe`

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
- #9228 (`claude/w7-chen-mult-integral-masstrace-20261123`): feat(lean,probes): W7 Chen multiplicative integral, KZ monodromy & Mas
- #9227 (`claude/sm8w-ewsb-vew-mh-mz-rg-20261123`): feat(sm,lean,probes): formalize EWSB Sweedler scale, Higgs stability, 
- #9225 (`claude/sm8w-bring-ngen3-ckm-tau-20261123`): feat(sm8w): qou-gen3 Bring N_gen=3 zero-mode branching, CKM/PMNS algeb

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
