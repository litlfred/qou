---
description: Full pre-merge workflow — rebase onto upstream, integrate new content, one-voice review, 100% Lean, then request a Copilot review
---

Prepare the current branch's PR for merge. Execute the steps **in order**,
with the exception of requesting external reviews (Step 6), which may be
started in parallel with the Lean build (Step 4) to save time.

**Workflow precondition** (per AGENTS.md §Branch + PR workflow,
STRICT, supersedes default "no auto-PR" guidance for this repo):
you should already be on a feature branch with a PR open. If
you're on `main` or a stale branch with uncommitted work, STOP —
go back and create the branch + PR first, then return here.
Commit early + commit often; small structured commits cherry-pick
cleanly; bulk commits are reserved for integration-watcher sweeps.

## 1. Rebase onto upstream HEAD, resolve conflicts

- `git fetch origin` and identify the upstream default branch (typically `main`).
- Rebase the current branch onto `origin/main`.
- If conflicts arise, resolve them (never discard the user's work; ask when
  a resolution is non-obvious). Re-run validation after each conflict fix.
- Continue until the rebase completes cleanly.

### 1·a Witness-drift conflicts — auto-resolve, do NOT prompt

`computations/*.witness.json` files are **machine-generated**
by the validators that run during the witness-pipeline CI. Conflicts on
these files during rebase are almost always **drift** caused by both branches
re-running the same validator at different times — the underlying *content*
is identical modulo `computedAt` / `commitSha` / `scriptCommitSha` /
`scriptHash` / `durationMs` / `engineVersion` fields and a `files_scanned`
counter that bumps when new Python files land on either branch.

**Standardised auto-resolution** (do this without asking the user):

```bash
# Loop until the rebase finishes; each iteration regenerates the four
# self-emitting audit witnesses, re-stages ONLY the regenerated four
# (not all witness JSON), and continues the rebase.  Each validator's
# exit code is checked so a script failure halts the loop instead of
# proceeding silently with a stale or partial witness.
# 30-iteration cap as a safety guard.
# NOTE (2026-06-02 reorg): e0-calibration + fitted-labelled-canonical
# witnesses moved with their scripts into computations/audits/.
WITNESS_REGEN_TARGETS=(
  "computations/compute-audit-scan.witness.json"
  "computations/derivation-chain-audit.witness.json"
  "computations/cross-check-trM-1ppb.witness.json"
  "computations/audits/e0-calibration-audit.witness.json"
  "computations/audits/fitted-labelled-canonical-audit.witness.json"
)
cnt=0
loop_break=""
while git status 2>/dev/null | grep -q "rebase in progress"; do
  cnt=$((cnt+1)); [ $cnt -gt 30 ] && { echo "STUCK"; break; }
  # Bail out to manual handling on any non-witness-json conflict.
  # Use `cut -c 4-` (rather than `awk '{print $2}'`) so paths with
  # spaces are preserved correctly.
  while IFS= read -r f; do
    case "$f" in
      computations/*.witness.json) : ;;
      *) echo "MANUAL: $f"; loop_break=1; break ;;
    esac
  done < <(git status --short | grep "^UU" | cut -c 4-)
  [ -n "$loop_break" ] && break
  # NOTE: the two audit/ scripts moved to computations/audits/
  # (2026-06-02). Path resolved per-script below.
  for s in compute_audit_scan derivation_chain_validator \
           cross_check_trM_1ppb audits/e0_calibration_audit \
           audits/fitted_labelled_canonical_audit; do
    args=()
    case "$s" in cross_check_trM_1ppb|audits/e0_calibration_audit) args=(--strict);; esac
    # QOU_Q0_ANCHOR=ideal: the derivation JSONs / L1 cross-check are
    # muon-q₀ canonical (AGENTS.md §q₀ anchor convention); without the
    # env the runtime proton pin makes c-q-q0 (and the L1 gate) fail
    # spuriously at rel_diff ≈ 1e-7 (diagnosed 2026-07-19).
    if ! QOU_Q0_ANCHOR=ideal python3 "computations/${s}.py" "${args[@]}" \
           >/dev/null 2>&1; then
      echo "FAIL: ${s}.py exited non-zero — halting auto-resolve"
      loop_break=1; break
    fi
  done
  [ -n "$loop_break" ] && break
  # Stage only the four witnesses we just regenerated, not every
  # *.witness.json (over-broad globs can sweep in unrelated drift).
  git add "${WITNESS_REGEN_TARGETS[@]}" 2>/dev/null
  out=$(GIT_EDITOR=true git rebase --continue 2>&1 | tail -3)
  echo "$out" | grep -q "Successfully rebased" && { echo "OK ($cnt)"; break; }
done
```

The four scripts cover the four witnesses that **always drift** under rebase
(`compute-audit-scan`, `derivation-chain-audit`, `cross-check-trM-1ppb`,
`e0-calibration-audit`). The loop stops if any **non-witness** conflict
appears (real conflict requiring human judgment), if any validator exits
non-zero (real failure requiring investigation), or after 30 iterations as
a safety guard.

After the rebase finishes, also re-run the validators **once more** to
catch the post-merge drift introduced by upstream's witness scans and any
new Python files this branch added (which bump `files_scanned`).  Each
validator's exit code is checked; the post-rebase commit is created only
if all four succeed:

```bash
set -e
# QOU_Q0_ANCHOR=ideal — muon-q₀ canonical layer; see comment in the loop above.
QOU_Q0_ANCHOR=ideal python3 computations/compute_audit_scan.py >/dev/null 2>&1
QOU_Q0_ANCHOR=ideal python3 computations/derivation_chain_validator.py >/dev/null 2>&1
QOU_Q0_ANCHOR=ideal python3 computations/cross_check_trM_1ppb.py --strict >/dev/null 2>&1
QOU_Q0_ANCHOR=ideal python3 computations/audits/e0_calibration_audit.py --strict >/dev/null 2>&1
QOU_Q0_ANCHOR=ideal python3 computations/audits/fitted_labelled_canonical_audit.py >/dev/null 2>&1
set +e
git add "${WITNESS_REGEN_TARGETS[@]}" 2>/dev/null
git diff --cached --quiet || git commit -m "fix(witness-pipeline): post-rebase drift refresh"
```

This is the standard workflow per the witness-pipeline CI's "drift detector"
step — fields outside the filtered set (`computedAt|durationMs|commitSha|
scriptCommitSha|scriptHash|engineVersion|engine|engine_version`) are
substantive and require a fresh witness committed alongside the script
changes. **CI will fail without this refresh** if the new Python files this
branch added bumped `files_scanned` or if any audit witness gained new
inventory entries.

## 1a. Migrate any legacy `lean.ref` shapes pulled in from upstream

- **The `bun run migrate-lean-refs` alias no longer exists in qou** — it fails
  with `Script not found "migrate-lean-refs"`. The pipeline moved to
  `litlfred/folio-assistant` (`content/pipeline/migrate-lean-refs.ts`) and miga
  pruned the qou aliases; AGENTS.md §0b has said so since 2026-06-23, and adds
  that the migration is **corpus-complete** (0 legacy `decl:` shapes remain), so
  running it is historical rather than routine.
- What is still worth doing after every rebase is the *verification* below,
  which needs no script: it is what would catch a legacy shape arriving from
  upstream. If it ever reports a non-zero count, run the migration from a
  folio-assistant checkout per that repo's docs.
- This catches blocks that landed on `origin/main` while the branch was
  in flight and still use the legacy `lean: { decl: "...", file? }`
  shape (Zod will hard-fail validation on those).
- If the script writes any files, stage and amend them into the rebase
  result before continuing (`git add` + `git commit --amend --no-edit`
  on the topmost integration commit, or as a follow-up commit if the
  rebase was non-trivial).
- **Verify** no legacy shape is present (both counts must be 0):

  ```bash
  # 1. No legacy `lean: { decl: ... }` shape remains
  grep -rln 'lean:\s*{[^}]*decl:' content/*/*.ts 2>/dev/null \
    | grep -v schema/ | grep -v pipeline/ | wc -l
  # Expected: 0

  # 2. Every `lean.ref` URI uses a registered package prefix.
  #
  # NOTE the `lean:\s*{` anchor. This pattern used to be a bare `ref:\s*"…:`,
  # which matches EVERY `ref:` field in a content block, not just `lean.ref`.
  # `simulator: { ref: "sim:…" }` is schema-valid — `sim:` is a registered
  # namespace (folio-assistant/schemas/constraints.ts) — so the old pattern
  # reported four "unregistered package prefixes" on a clean corpus. Combined
  # with the "if any check is non-zero, do not proceed" rule below, that made
  # this gate unpassable: no qou branch could ever reach Step 2.
  python3 -c "
  import re, glob
  pkgs = re.findall(r'name:\s*\"(\w+)\"', open('folio-assistant/schemas/lean-packages.ts').read())
  bad = []
  for f in glob.glob('content/*/*/*.ts'):
      txt = open(f).read()
      for m in re.finditer(r'lean:\s*{\s*ref:\s*\"([^:\"]+):', txt):
          if m.group(1) not in pkgs: bad.append(f'{f} → {m.group(1)}')
  print(f'Unregistered lean.ref package prefixes: {len(bad)}')
  for b in bad: print(f'  {b}')
  "
  # Expected: 0
  ```

- If any check is non-zero, **do not proceed to Step 2**. Either run
  the migration with `--write`, register the missing package in
  `folio-assistant/schemas/lean-packages.ts` + root `lakefile.toml`, or
  fix the offending block before continuing.

## 2. Integrate new content from upstream

- Pull in any new content blocks, glossary updates, or references that
  landed on `origin/main` during the branch's lifetime.
- Re-run `content-validation` to confirm cross-refs, `uses[]`, and
  `interprets` still resolve after integration.
- Run the `remark-audit` skill to catch any newly dangling remarks.

## 2a. Reuse and simplify pass (audit against newly-merged content)

After main has been pulled in cleanly, audit the branch's own
content against everything new that just arrived from upstream.
Ask three concrete questions for every block, proof, and
computation the branch added or modified:

1. **Can I use anything?** Did `origin/main` introduce a definition,
   lemma, theorem, glossary entry, simulator, or computational
   witness that this branch is now duplicating, paraphrasing, or
   reinventing? If yes, replace the local stand-in with a `uses[]`
   cross-reference (or a one-line `\cite{}` to the new block) and
   delete the duplicate. Run `local/critical-path-analysis` to
   surface the dependency overlaps and `local/ontologist` to align
   terminology.
2. **Can I simplify the proof?** Walk through every Lean proof and
   every narrative `**Proof.**` block this branch authored or
   touched. If a newly-merged result discharges a hypothesis,
   collapses a case split, supplies a tactic that replaces a long
   `calc`/`refine` chain, or makes a `sorry` provable — apply it.
   Route through `local/proof-simplifier` for narrative proofs and
   `local/lean-build-fix` plus `local/lean-completeness-audit` for
   Lean.
3. **Can I simplify the exposition?** Re-read this branch's
   narrative additions with the merged-in context in mind. If a
   paragraph re-derives something main now defines upstream,
   replace it with a forward-reference. If a remark interprets a
   concept main has already glossed, drop the duplicate
   interpretation. Route through `local/scientific-accuracy` (for
   claim audit) and `local/readability-editing` (for prose
   tightening).
4. **Can I simplify the computation?** Inspect every script under
   `computations/` and every fenced ``` ```python ```
   block this branch added. If main shipped a faster routine, a
   prebuilt witness, a SnapPy/SymPy primitive, or a cached
   computation that supersedes a hand-rolled loop, swap it in and
   regenerate the witness JSON.

The reuse pass is **not optional** — duplicating content that main
already carries is the most common source of post-merge review
churn. Running this audit now (rather than waiting for Copilot to
surface the duplicates in step 6) saves a full review cycle.

## 3. One-voice review

- Invoke the `one-voice-audit` skill across every `.md` file touched
  on this branch (mechanical sweep: status leaks, emoji, Unicode
  crashes, first-person work tone). When rewriting, consult
  `one-voice-style-guide` for the author voice profile.
  Fix voice / style inconsistencies before proceeding.

## 4. 100% Lean — build + resolutions

- Run **`lake build QOU UGB Fred2005`** from the repo root. Name the three
  library targets; do **not** run a bare `lake build` there.

  A bare `lake build` at the root **builds nothing and exits 0**
  — "Build completed successfully (0 jobs)", having examined not one Lean file.
  The root package aggregates the three paper packages and declares no library
  of its own, so its default target set is empty. `defaultTargets` cannot fix
  it (it names targets of the root package only; `["QOU", …]` and
  `["qou/QOU", …]` are both rejected), and neither can a root aggregator module,
  because each paper's library is declared with globs (`["QOU", "QOU.+"]`) and a
  glob library is built by naming the library target and no other way. The root
  `lakefile.toml` carries the same note.

  This step said "the standardized root Lake workspace builds every paper
  package in one pass" and named the bare command. It did not, and it reported
  success while doing so — the same defect shape as the three gates in
  folio-assistant PR #88: *a gate that can report success without examining
  anything is not a gate.*

- **Warm the root workspace's Mathlib cache first: `lake exe cache get`.**

  The root workspace has its *own* `.lake/packages/mathlib`, separate from each
  paper's. A sandbox that has been building per-paper (`cd content/<paper>/lean
  && lake build`) has a warm cache in the **paper's** checkout and a cold one at
  the root, so the first `lake build QOU UGB Fred2005` there starts compiling
  Mathlib **from source** — observed going through
  `Mathlib/Algebra/Order/AbsoluteValue/Basic.lean` and friends, which is hours,
  not minutes, and silently: the output looks like ordinary build progress.

  Both lakefiles pin the same rev (`f897ebcf…`), so the cache applies. Check
  free disk before doing it — the root copy is a second full Mathlib build tree
  — and see AGENTS.md's RESTORE → build → SEED note.
- If the build fails, route to `lean-build-fix` and resolve.
- Run `lean-completeness-audit`: every `sorry` must carry a `-- Ref:`
  citation, every `definition` block must have its `.lean` sibling,
  and every provable block kind (`theorem`/`lemma`/`proposition`/
  `corollary`) must have a Lean statement.
- Run `proof-simplifier` on any proofs that changed on this branch.
- The Lean build must be green and the audit must report 100%
  coverage before continuing.

## 4b. Precision gates (BLOCKING)

- Run [`scripts/precision-gates.sh`](../../scripts/precision-gates.sh). It runs
  the whole NO-FLOAT64 family in one pass — the raw-float64 and float64-padding
  ratchets, the three source-level gates (`mpf(<float>)`, `mp.dps` no-op,
  module-const), the q₀ anchor-flip and drift gates — and exits 1 on any
  blocking red. The no-free-parameter certificate runs as advisory only (red by
  design on `A_omega = 3`; see the workflow's own note).
- **This step exists because the CI copy does not run.** The same gates are
  strict in `.github/workflows/witness-staleness.yml`, but that workflow is
  `workflow_dispatch:` only under the 2026-06-30 Actions-billing directive, so
  a push triggers nothing. Three dirty witnesses reached `main` that way
  (bean `qou-mnrd`). Do not treat "CI will catch it" as true here.
- If the run is red on witnesses **this branch introduced**, fix at the
  producer before pushing (`mpmath.mpf` from source, serialize with
  `_precision.fmt`). Never add a file to a baseline, never `--rebaseline`, and
  never hand-edit a number to go green.
- If the run is red on witnesses **inherited from `main`**, that is not this
  branch's regression. Say so explicitly in the PR with the file list, and do
  not silence it — draining another arc's witnesses is that arc's work.
- If the run reports **stale committed audit witnesses**, check whether a
  *count* moved (substantive — commit the regenerated witness and name the
  count) or only `computedAt`/`commitSha`/`durationMs`/`scriptHash` (drift —
  revert it).

## 5. Final rebase pass

- After all fixes above, rebase once more onto the current `origin/main`
  HEAD (upstream may have moved). Resolve any new conflicts. The branch
  tip must fast-forward onto `origin/main`.
- Push with `git push --force-with-lease -u origin <branch>`.

## 6. Request external reviews (can run in parallel with 4)

- Find the open PR for the current branch in `litlfred/qou` using
  `mcp__github__list_pull_requests`. If none exists, tell the user
  and stop.
- Request a Copilot review using `mcp__github__request_copilot_review`.
  **Copilot is the only live external reviewer.**
- **Do NOT post `/gemini review`.** Gemini Code Assist is **sunset** —
  the consumer GitHub integration has ceased all code-review activity
  and answers every request with a `[!CAUTION]` sunset notice. Posting
  it and waiting is the documented way to stall a session
  (PR #4456, 2026-08-07). If an old `gemini-code-assist[bot]` sunset
  comment is already on the PR, record "Gemini: sunset" and move on.
- Subscribe to PR activity with `mcp__github__subscribe_pr_activity`
  so CI failures and review comments are delivered to this session.
- Report the PR URL and confirm the Copilot review request posted.

Note: You do not need to wait for `lake build` (Step 4) to finish before
doing this step. You can fire off the review requests while the build runs.

## 7. Merging

- After all review comments are disposed of, resolve conflicts so that a merge can be performed.
- Ask the user if they are ready to proceed with the merge (provide PR # and URL).  If confirmed, perform merge.
- **Merge method: see AGENTS.md §"Branch + PR workflow" rule 8 — that
  rule is authoritative and explicitly supersedes this skill doc.**
  The default is **`merge_method: "rebase"`** (rebase-and-merge), which
  applies the branch's structured commits to `main` as a linear
  sequence. Do not restate the policy here; read rule 8.
  - `rebase` (**default**) — keeps every commit, no merge commit
  - `merge` — only for a sub-merge of already-merged sibling branches,
    where the merge commit is a useful boundary marker
  - `squash` — **never** without explicit per-PR permission
    ("squash this one" / "squash OK"). Treat it as destructive: do not
    infer it from "merge", "ship", "land", or any generic verb.

## Failure handling

If any step 1–5 fails and cannot be resolved automatically, **stop**
and report the blocker to the user. If you already requested the Copilot
review in parallel, warn the user that the reviewer might be
looking at a broken branch, and proceed to fix the issues so you can push
a green build as quickly as possible.
