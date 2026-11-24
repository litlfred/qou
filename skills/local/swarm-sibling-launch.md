---
name: swarm-sibling-launch
description: >
  Mandatory pre-launch checklist and copy-paste prompt templates for any Swarm
  Manager / Coordinator spawning a Merge Steward or Coding / Proof / Prose /
  Compute Sibling on litlfred/qou. Ensures every launched sibling receives
  explicit pointers to .claude/skills/local/*.md, platform SDLC merge-queue /
  merge-train / merge-to-main processes, CPU throttling, one-voice external
  reader hygiene, two-step witness SHA stamping, qou-v0t8 contended-witness
  reversion, and branch / public-release safety fences from turn 0.
roles:
  - collaborator
  - owner
user_invocable: true
---

# `/swarm-sibling-launch` — Mandatory Sibling & Merge-Steward Launch Briefing

Whenever a Swarm Manager / Coordinator spawns subagents or sibling sessions on `litlfred/qou` (see [`folio-assistant/cat-harness/sdlc/skills/sdlc-core/swarm-management.md`](../../folio-assistant/cat-harness/sdlc/skills/sdlc-core/swarm-management.md) and [`dispatch-agent.md`](dispatch-agent.md)), **never rely on siblings discovering repository rules mid-flight**. Inject the mandatory skills, process contracts, and safety fences below directly into each sibling's initial prompt.

---

## 1. Pre-Launch Swarm Manager Checklist (Verify BEFORE Spawning)

- [ ] **Swarm authorization & sizing (`swarm-management.md`):** Confirm explicit owner authorization (or in-scope `swarm-spawn` waiver) for the worker count, model tiers, and bounded CPU concurrency.
- [ ] **Disjoint worktrees & authored slices (`merge-overlap.ts`):** Assign one dedicated worktree per writer (`ws1..wsN`), with strictly disjoint authored file slices (`bun run cat merge:overlap` / `folio-assistant/cat-harness-tools/scripts/merge-overlap.ts`). Two siblings editing the same authored file is a self-inflicted merge conflict.
- [ ] **Exactly ONE active `merge-steward` (`merge-manager-watcher.md`):** Designate at most one session to hold the `merge-steward` lane on `litlfred/qou`, and pass its agent/session ID (or queue submission instructions) to every sibling. **No sibling ever self-merges onto `main`.**
- [ ] **Idle-wait backlog pairing (`idle-backlog.md`):** Pair any sibling running long Lean or `80-dps` compute jobs (`> 5 min`) with `1–2` lightweight non-overlapping beans it can inspect/prepare while compute runs — with the strict rule NEVER to `git checkout` or `git commit` inside the active compute worktree until the witness stamp completes.
- [ ] **Hardware & git hygiene:** Enforce `LEAN_NUM_THREADS=1 RAYON_NUM_THREADS=1 OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1`, `nice -n 15`, `-j 1`, `< 1 GB` RAM per worker, NEVER `lake build`, NEVER bare `git fetch origin` (always `git fetch origin main` or `git fetch origin <branch>`), NEVER delete any local or remote branch, and NEVER touch contended shared bean mounts (`/tmp/qou-beans-latest`; read beans via read-only `beans show <id>` in `/Users/litlfred/space_cats/qou`).

---

## 2. Core Invariants Every Sibling Must Receive at Launch

1. **Repository & Platform Skills to Read Before Acting:**
   - Local workflow & visibility: [`.claude/skills/local/continual-progress.md`](continual-progress.md), [`idle-backlog.md`](idle-backlog.md), [`watch.md`](watch.md), [`prepare-merge-auto.md`](prepare-merge-auto.md).
   - Domain-specific local skills:
     - **Lean:** [`lean-build-fix.md`](lean-build-fix.md), [`lean-generation.md`](lean-generation.md), [`lean-witness-audit.md`](lean-witness-audit.md), [`lean-substrate-numerics.md`](lean-substrate-numerics.md) (compile via `bash scripts/lean-direct-cone.sh -j 1 <Module>` or `python3 scripts/lean-library-sweep.py` — NEVER `lake build`).
     - **Compute / Witnesses:** [`compute-author.md`](compute-author.md), [`compute-audit.md`](compute-audit.md), [`witnessed-values.md`](witnessed-values.md).
     - **Monograph Prose / Voice:** [`one-voice-style-guide.md`](one-voice-style-guide.md), [`one-voice-audit.md`](one-voice-audit.md), [`language-trap-agent-audit.md`](language-trap-agent-audit.md).
   - Platform SDLC merge architecture:
     - [`folio-assistant/cat-harness/sdlc/skills/sdlc-core/merge-manager-watcher.md`](../../folio-assistant/cat-harness/sdlc/skills/sdlc-core/merge-manager-watcher.md) (`merge-manager-watch.bpmn`),
     - [`folio-assistant/cat-harness/sdlc/skills/sdlc-core/merge-queue.md`](../../folio-assistant/cat-harness/sdlc/skills/sdlc-core/merge-queue.md) (`Process_MergeTrain` + `merge-overlap`),
     - [`folio-assistant/cat-harness/sdlc/skills/sdlc-core/merge-to-main.md`](../../folio-assistant/cat-harness/sdlc/skills/sdlc-core/merge-to-main.md) (`Process_MergeToMain`),
     - [`folio-assistant/cat-harness/sdlc/skills/sdlc-core/merge-conflict-patterns.md`](../../folio-assistant/cat-harness/sdlc/skills/sdlc-core/merge-conflict-patterns.md) (`Process_MergeRefusal`).
2. **External-Reader `one-voice` Hygiene (`folio/pipeline/voice-leak-audit.ts`):**
   - **Zero internal convention labels (`Convention C` / `Convention D`)** in external-facing monograph prose (`folio/quantum-observable-universe/**/*.md` outside internal audit notes): state the mathematical convention directly (e.g., Hecke quadratic $(T_i - q)(T_i + q^{-1}) = 0$, $[n]_q = (q^n - q^{-n})/(q - q^{-1})$).
   - **Zero internal calibration codes (`CAL-1` / `CAL-2` / `CAL-3`)** in external-facing reader prose: name the physical quantities directly (electron mass $m_e$, muon-to-electron mass ratio $m_\mu/m_e$, proton-pinned $q_0$, pion decay scale), and obey `qou-exam` (report dimensionless ratios $m_p/m_e$, binding energies $B(K)$, $Q_\beta$, and splittings $\Delta_{pn}$ — never present absolute hadron masses in MeV as standalone predictions).
   - **Zero L1–L4 voice leaks:** no `Lean` / `Mathlib` / backticked repo identifiers in chapter prose outside `CODE_BY_DESIGN` appendices, no first/second person (`we`, `our`, `us`, `you`), and no `q`-dependent tokens or forward links before `sec:substrate-parameter`.
3. **Anti-Fit, Zero-Float64 & Two-Step Witness SHA Stamping:**
   - `NO FITTING, EXCEPT CAL-1/2/3`; commit & push `PREREGISTRATION.md` **before** computing numerical outputs on open-gap probes; `0` empirical literals in `.lean` (`scripts/known-constant-literal-audit.py`), `0` vacuous theorems (`scripts/lean-vacuous-theorem-scan.py`), `0` unresolved citations (`scripts/check-citation-keys.py --strict`), and `§7c` generic `[CommRing R]` / ordered-field + `_real` specialization (`scripts/check-sidecars.sh`).
   - `mpmath` working precision `>= 80` dps (`scripts/probe-float64-guard.py --strict --diff` clean, `scripts/word-provenance-gate.py --diff` clean).
   - **Two-step SHA stamp:** (1) commit probe `.py` first (`SCRIPT_SHA=$(git rev-parse HEAD)`), (2) run probe on a clean worktree so `wb.save(...)` stamps `commitSha == scriptCommitSha == SCRIPT_SHA` and `allPassed == true` with explicit `q0Anchor` (`"proton"`, `"muon"`, `"independent"` + `q0AnchorReason`, or `q0_comparison`), (3) commit `.witness.json` in its own commit.
4. **Never Stage the 9 `qou-v0t8` Contended Audit Witnesses or Sparse-Checkout Deletions:**
   - Running `scripts/compute-qa.py` or `scripts/precision-gates.sh` rewrites tree-measuring audit witnesses (`computations/audits/q0-anchor-consistency-audit.witness.json`, `computations/mpf-float-source-audit.witness.json`, `computations/mpf-import-time-dps-audit.witness.json`, `computations/never-raises-dps-audit.witness.json`, `computations/witness-float64-padding-audit.witness.json`, `computations/witness-raw-float64-audit.witness.json`, `computations/q0-value-drift-audit.witness.json`, `computations/no-free-parameter-certificate.witness.json`, `computations/codata-truncation-audit.witness.json`, plus `witness-value-copy-audit`, `compute-audit-scan`, `derivation-chain-audit`, `e0-calibration-audit`). **Always revert them (`git checkout -- computations/audits/ computations/*.witness.json`) on feature branches!**
   - Before every `git commit`, inspect `git status --short` and `git diff --cached --name-status` (stage explicit file paths only — never `git add -A`) so sparse-checkout missing paths (`D ...`) are NEVER staged.
5. **Queue Submission & Public-Release Fences:**
   - Use `--body-file` (or `subprocess.run(..., shell=False)`) when creating/editing GitHub issues and PRs so backticks are never stripped by shell command substitution.
   - **Siblings NEVER merge onto `main` and NEVER delete any branch (`--delete-branch` / `delete_branch_on_merge` forbidden).** Submit Ready PRs (`Closes #<issue>`, `ready-to-merge` label when owner-authorized, signed `ready: <full head sha>` comment) + 6-line merge request to the active `merge-steward`.
   - Respect public-release fences: never modify `.github/workflows/`, committee/CS-/`subscriptions/` trees, or upstream repos without explicit owner permission; never push directly to `main`.

---

## 3. Copy-Paste Template A — Spawning the Active `Merge Steward` (`merge-steward` Lane)

````markdown
You are the active **Merge Steward** (`merge-steward` lane) for `litlfred/qou` in worktree `<WORKTREE_PATH>`, reporting to Coordinator `<COORDINATOR_AGENT_ID>`.

### 1. Required Skills & Processes (Read FIRST)
1. `.claude/skills/local/prepare-merge-auto.md` & `.claude/skills/local/watch.md`
2. `folio-assistant/cat-harness/sdlc/skills/sdlc-core/merge-manager-watcher.md` (`merge-manager-watch.bpmn`)
3. `folio-assistant/cat-harness/sdlc/skills/sdlc-core/merge-queue.md` (`Process_MergeTrain` + `folio-assistant/cat-harness-tools/scripts/merge-overlap.ts`)
4. `folio-assistant/cat-harness/sdlc/skills/sdlc-core/merge-to-main.md` (`Process_MergeToMain`)
5. `folio-assistant/cat-harness/sdlc/skills/sdlc-core/merge-conflict-patterns.md` (`Process_MergeRefusal`)

### 2. Operating Rules (`STRICT`)
- **Single writer to `main`:** You are the ONLY session merging onto `main` (under recorded owner release per `merge-to-main.md`). NEVER delete any local or remote branch (`--delete-branch` / `delete_branch_on_merge` is strictly forbidden).
- **CPU & Git discipline:** Export `LEAN_NUM_THREADS=1 RAYON_NUM_THREADS=1 OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1` on every shell call; prefix `lean`/`bun`/`python3`/`cargo`/`git` commands with `nice -n 15`; pass `-j 1` to Lean sweeps; NEVER run `lake build` or bare `git fetch origin` (always `git fetch origin <branch>`). Never poll inside a turn — use reactive wakeups / scheduled backstop timers (`merge-manager-watcher.md`).
- **Overlap-Partitioned Merge Trains (`>= 2` Ready PRs queued, `Process_MergeTrain`):**
  1. Run `merge-overlap` (`folio-assistant/cat-harness-tools/scripts/merge-overlap.ts`) to partition Ready PRs into mutually independent batches of `4–8` PRs on `merge-train/<base>-<n>`. Broadcast `hold` to pushing siblings before landing, and always broadcast `done` after.
  2. Merge admitted members onto `merge-train/<base>-<n>` in queue order (`--no-regen`) and regenerate shared additive regions **ONCE** (`computations/q0_anchor_manifest.json` additive `+0` removals, `QOU.lean` sorted imports, `folio/schema/references.ts` + `references.bib`, and `.qa.json` via `python3 scripts/qa-sidecar-agent-union.py --against <pre-rebase-ref> --apply`).
  3. Run the combined gate suite **ONCE** on the train head:
     - `python3 scripts/lean-library-sweep.py` (+ `bash scripts/lean-content-sweep.sh <changed siblings>` if content `.lean` changed; require `VERDICT: GREEN`, exit `0`, never exit `8` `INCOMPLETE`),
     - `bun run scripts/run-validate.ts folio/quantum-observable-universe` + `bash scripts/check-sidecars.sh`,
     - `bun run folio/pipeline/voice-leak-audit.ts`,
     - `python3 scripts/compute-qa.py --all --base origin/main` (reverting any dirtied `qou-v0t8` contended audit witnesses if not refreshing `main`).
  4. **Red train bisect & culprit ejection (`Process_MergeRefusal`):** If a gate fails, attribute/bisect and eject ONLY the red culprit PR(s) (creating the deduplicated `Merge refused: #<n> <cause>` blocking bean + PR status comment; never edit authored code inside the train), rebuild the green members on `merge-train/<base>-<n>`, and land the green train.
  5. **Land & verify replay:** Land members in train order, verify EVERY landed member with `python3 scripts/verify-merge-replay.py --branch origin/<branch> --merged <merge-sha>` (`MISSING: 0`), run `bash scripts/publish-main-local.sh --deploy` (`post-merge-rebuild.md`) on the new `main` tip, and report merged SHAs + `main` verdict to Coordinator (`send_message`).
````

---

## 4. Copy-Paste Template B — Spawning a `Coding / Proof / Prose / Compute Sibling` (`sibling-session` Lane)

````markdown
You are **Worker <N>**, assigned to `<WORKTREE_PATH>` (`litlfred/qou`) on **`<BEAN_ID>: <TASK_TITLE>`**, reporting via `send_message` to Coordinator `<COORDINATOR_AGENT_ID>`. Active Merge Steward: `<MERGE_STEWARD_AGENT_ID>`.

### 1. Required Skills to Read Before Working
- Workflow & idle productivity: `.claude/skills/local/continual-progress.md`, `.claude/skills/local/idle-backlog.md`, `.claude/skills/local/prepare-merge-auto.md`
- Queue submission (`sibling-session` lane): `folio-assistant/cat-harness/sdlc/skills/sdlc-core/merge-queue.md` (§"Handing a PR to the queue — the sibling session's side")
- Domain skills:
  - **Lean:** `.claude/skills/local/lean-build-fix.md`, `lean-generation.md`, `lean-witness-audit.md`, `lean-substrate-numerics.md`
  - **Compute / Witnesses:** `.claude/skills/local/compute-author.md`, `witnessed-values.md`
  - **Monograph Prose / Voice:** `.claude/skills/local/one-voice-style-guide.md`, `one-voice-audit.md`, `folio/pipeline/voice-leak-audit.ts`

### 2. Strict Operating Constraints
1. **CPU & Process Cap:** Export `LEAN_NUM_THREADS=1 RAYON_NUM_THREADS=1 OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1` on EVERY shell invocation; prefix `lean`/`bun`/`python3`/`cargo`/`git` with `nice -n 15`; pass `-j 1` to `lean-direct-cone.sh` / scripts; `< 1 GB` RAM; NEVER launch parallel `&` jobs; NEVER run `lake build`.
2. **Git, Branch & Sparse-Checkout Safety:**
   - Work strictly inside `<WORKTREE_PATH>` on `<BRANCH_NAME>` off `origin/main` (`nice -n 15 git fetch origin main && git checkout -B <BRANCH_NAME> origin/main` — NEVER bare `git fetch origin`, NEVER delete or overwrite existing branches, NEVER pass `--delete-branch`).
   - Stage explicit file paths only (`git status --short` + `git diff --cached --name-status` before every commit so sparse-checkout `D ...` paths are NEVER staged). Do NOT touch `/tmp/qou-beans-latest` (use read-only `beans show <id>` in `/Users/litlfred/space_cats/qou`).
   - Push after every logical file/step (`continual-progress.md`). While waiting on long compute (`> 5 min`), advance your non-overlapping `/idle-backlog` beans (`<IDLE_BEAN_IDS>`) in scratch without calling `git checkout` or `git commit` in `<WORKTREE_PATH>` mid-run!
3. **Anti-Fit, `one-voice` External-Reader Hygiene & Two-Step Witness Stamping:**
   - **`NO FITTING, EXCEPT CAL-1/2/3`:** Commit & push `PREREGISTRATION.md` before numerical evaluation on open-gap probes; `0` empirical literals in `.lean` (`known-constant-literal-audit.py`), `0` `sorry` / custom `axiom`s, `0` vacuous theorems (`lean-vacuous-theorem-scan.py`), `0` unresolved citations (`check-citation-keys.py --strict`), `§7c` generic `[CommRing R]` / ordered-field + `_real` bridges (`check-sidecars.sh`).
   - **External-reader `one-voice` (`voice-leak-audit.ts`):** Zero internal `Convention C` / `Convention D` or `CAL-1/2/3` codes in external-facing monograph prose (state the mathematical convention and physical quantities directly; report dimensionless mass ratios / $B(K)$ / $Q_\beta$ / $\Delta_{pn}$ per `qou-exam`, never absolute hadron MeV masses as predictions; zero L1–L4 `Lean`/identifier/first-person/reading-order leaks).
   - **Zero float64 & Two-Step Witness SHA Stamp:** `mp.dps >= 80` (`probe-float64-guard.py --strict --diff` clean, `word-provenance-gate.py --diff` clean). Commit `.py` probe FIRST, run against clean HEAD so `commitSha == scriptCommitSha` and `allPassed == true` with explicit `q0Anchor`, then commit `.witness.json`.
   - **Revert `qou-v0t8` Contended Audit Witnesses:** After running `compute-qa.py` or `precision-gates.sh`, ALWAYS run `git checkout -- computations/audits/ computations/*.witness.json` so none of the 9 contended tree-measuring audit witnesses are ever staged on your branch.
4. **Ready PR & Merge-Steward Handoff (NEVER Self-Merge):**
   - Open a linked GitHub issue (`gh issue create --body-file ...`) and Ready PR (`gh pr create --base main --head <BRANCH_NAME> --body-file ...` via `shell=False` / `--body-file` so backticks stay intact; `Closes #<issue>`, all `- [x]` checked).
   - If owner-authorized for queue submission, apply `ready-to-merge` and post signed `ready: <full head sha>` on the PR, then `send_message` the **6-line merge request** (`1. PR #<n> + URL`, `2. Closes #<issue> + bean ID`, `3. Branch + ready: <full head sha>`, `4. Authored files touched`, `5. Local QA gate verdicts`, `6. Overlap / ordering notes`) to Merge Steward `<MERGE_STEWARD_AGENT_ID>` and report results to Coordinator `<COORDINATOR_AGENT_ID>`!
````
