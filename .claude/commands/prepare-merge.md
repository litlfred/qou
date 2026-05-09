---
description: Full pre-merge workflow — rebase onto upstream, integrate new content, one-voice review, 100% Lean, then request Gemini + Copilot reviews
---

Prepare the current branch's PR for merge. Execute the steps **in order** —
do not request external reviews until every earlier step has succeeded.

## 1. Rebase onto upstream HEAD, resolve conflicts

- `git fetch origin` and identify the upstream default branch (typically `main`).
- Rebase the current branch onto `origin/main`.
- If conflicts arise, resolve them (never discard the user's work; ask when
  a resolution is non-obvious). Re-run validation after each conflict fix.
- Continue until the rebase completes cleanly.

### 1·a Witness-drift conflicts — auto-resolve, do NOT prompt

`folio-assistant/computations/*.witness.json` files are **machine-generated**
by the validators that run during the witness-pipeline CI. Conflicts on
these files during rebase are almost always **drift** caused by both branches
re-running the same validator at different times — the underlying *content*
is identical modulo `computedAt` / `commitSha` / `scriptCommitSha` /
`scriptHash` / `durationMs` / `engineVersion` fields and a `files_scanned`
counter that bumps when new Python files land on either branch.

**Standardised auto-resolution** (do this without asking the user):

```bash
# Loop until the rebase finishes; each iteration regenerates the four
# self-emitting audit witnesses, re-stages them, and continues the rebase.
# 30-iteration cap as a safety guard.
cnt=0
while git status 2>/dev/null | grep -q "rebase in progress"; do
  cnt=$((cnt+1)); [ $cnt -gt 30 ] && { echo "STUCK"; break; }
  # Bail out to manual handling on any non-witness-json conflict.
  conflicts=$(git status --short | grep "^UU" | awk '{print $2}')
  for f in $conflicts; do
    case "$f" in
      folio-assistant/computations/*.witness.json) : ;;
      *) echo "MANUAL: $f"; break 2 ;;
    esac
  done
  python3 folio-assistant/computations/compute_audit_scan.py >/dev/null 2>&1
  python3 folio-assistant/computations/derivation_chain_validator.py >/dev/null 2>&1
  python3 folio-assistant/computations/cross_check_trM_1ppb.py --strict >/dev/null 2>&1
  python3 folio-assistant/computations/e0_calibration_audit.py --strict >/dev/null 2>&1
  git add folio-assistant/computations/*.witness.json 2>/dev/null
  out=$(GIT_EDITOR=true git rebase --continue 2>&1 | tail -3)
  echo "$out" | grep -q "Successfully rebased" && { echo "OK ($cnt)"; break; }
done
```

The four scripts cover the four witnesses that **always drift** under rebase
(`compute-audit-scan`, `derivation-chain-audit`, `cross-check-trM-1ppb`,
`e0-calibration-audit`). The loop stops if any **non-witness** conflict
appears (real conflict requiring human judgment) or after 30 iterations as
a safety guard.

After the rebase finishes, also re-run the validators **once more** to
catch the post-merge drift introduced by upstream's witness scans and any
new Python files this branch added (which bump `files_scanned`):

```bash
python3 folio-assistant/computations/compute_audit_scan.py >/dev/null 2>&1
python3 folio-assistant/computations/derivation_chain_validator.py >/dev/null 2>&1
python3 folio-assistant/computations/cross_check_trM_1ppb.py --strict >/dev/null 2>&1
python3 folio-assistant/computations/e0_calibration_audit.py --strict >/dev/null 2>&1
git add folio-assistant/computations/*.witness.json 2>/dev/null
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

- After every rebase / merge, **run the lean-ref migration script**:
  `cd content && bun run migrate-lean-refs`. The script is idempotent
  (no-op when there is nothing to migrate) — running it unconditionally
  is the standardized post-rebase workflow described in
  CLAUDE.md §0b.
- This catches blocks that landed on `origin/main` while the branch was
  in flight and still use the legacy `lean: { decl: "...", file? }`
  shape (Zod will hard-fail validation on those).
- If the script writes any files, stage and amend them into the rebase
  result before continuing (`git add` + `git commit --amend --no-edit`
  on the topmost integration commit, or as a follow-up commit if the
  rebase was non-trivial).
- **Verify** the migration is complete (all three counts must be 0):

  ```bash
  # 1. Dry-run reports nothing left to migrate
  cd content && bun run migrate-lean-refs:dry | tail -3
  # Expected: "Migrated 0 lean refs across 0 files."

  # 2. No legacy `lean: { decl: ... }` shape remains
  grep -rln 'lean:\s*{[^}]*decl:' content/*/*.ts 2>/dev/null \
    | grep -v schema/ | grep -v pipeline/ | wc -l
  # Expected: 0

  # 3. Every `lean.ref` URI uses a registered package prefix
  python3 -c "
  import re, glob, json
  pkgs = re.findall(r'name:\s*\"(\w+)\"', open('folio-assistant/schemas/lean-packages.ts').read())
  bad = []
  for f in glob.glob('content/*/*/*.ts'):
      txt = open(f).read()
      for m in re.finditer(r'ref:\s*\"([^:\"]+):', txt):
          if m.group(1) not in pkgs: bad.append(f'{f} → {m.group(1)}')
  print(f'Unregistered package prefixes: {len(bad)}')
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
   `folio-assistant/computations/` and every fenced ``` ```python ```
   block this branch added. If main shipped a faster routine, a
   prebuilt witness, a SnapPy/SymPy primitive, or a cached
   computation that supersedes a hand-rolled loop, swap it in and
   regenerate the witness JSON.

The reuse pass is **not optional** — duplicating content that main
already carries is the most common source of post-merge review
churn. Running this audit now (rather than waiting for Gemini /
Copilot to surface the duplicates in step 6) saves a full review
cycle.

## 3. One-voice review

- Invoke the `one-voice-audit` skill across every `.md` file touched
  on this branch (mechanical sweep: status leaks, emoji, Unicode
  crashes, first-person work tone). When rewriting, consult
  `one-voice-style-guide` for the author voice profile.
  Fix voice / style inconsistencies before proceeding.

## 4. 100% Lean — build + resolutions

- Run `lake build` from the **repo root** (the standardized root Lake
  workspace builds every paper package — `qou`, `ugb`, `fred2005` —
  in one pass; see CLAUDE.md §0).
- If the build fails, route to `lean-build-fix` and resolve.
- Run `lean-completeness-audit`: every `sorry` must carry a `-- Ref:`
  citation, every `definition` block must have its `.lean` sibling,
  and every provable block kind (`theorem`/`lemma`/`proposition`/
  `corollary`) must have a Lean statement.
- Run `proof-simplifier` on any proofs that changed on this branch.
- The Lean build must be green and the audit must report 100%
  coverage before continuing.

## 5. Final rebase pass

- After all fixes above, rebase once more onto the current `origin/main`
  HEAD (upstream may have moved). Resolve any new conflicts. The branch
  tip must fast-forward onto `origin/main`.
- Push with `git push --force-with-lease -u origin <branch>`.

## 6. Request external reviews (only after 1–5 succeed)

- Find the open PR for the current branch in `litlfred/qou` using
  `mcp__github__list_pull_requests`. If none exists, tell the user
  and stop.
- Post a `/gemini review` comment on the PR using
  `mcp__github__add_issue_comment`.
- Request a Copilot review using `mcp__github__request_copilot_review`.
- Subscribe to PR activity with `mcp__github__subscribe_pr_activity`
  so CI failures and review comments are delivered to this session.
- Report the PR URL and confirm both review requests posted.

## Failure handling

If any step 1–5 fails and cannot be resolved automatically, **stop**
and report the blocker to the user. Do not request Gemini or Copilot
review on a branch that does not rebase cleanly, fails Lean build,
or has voice inconsistencies — it wastes reviewer attention.
