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

- **🛑 If the root cache was RESTORED from `lake-cache/*`, do NOT run this step
  at all — it will DESTROY the cache.** This is not the cold-cache case above;
  it is worse, and it looks like the opposite.

  Measured 2026-08-15 on PR #5106 (bean `qou-r13s`), running the very command
  this section prescribes:

  | | before | during (10 min) | after kill |
  |---|---|---|---|
  | root `mathlib` oleans | **6990** | — | **334** |
  | oleans written | — | 536 | — |
  | …under `mathlib`/`aesop`/`batteries` | — | **520** | — |
  | …under `QOU`/`UGB`/`Fred2005` | — | **0** | — |

  Oleans restored by `tar` carry no `.trace` files, so **Lake treats them as
  stale, rebuilds them from source, and evicts them as it goes** (AGENTS.md
  records the mechanism for the *seeding* direction as bean `02kc`; it fires
  identically on an ordinary consumer build of named library targets). Ten
  minutes produced zero paper-library progress and cost the session its cache;
  recovery is a fresh 1.6 GB fetch + extract.

  **A high olean count is not a validity check for the cache — the traces
  are.** 6990 reads as fully populated, which is exactly why the run above
  proceeded. Check for traces, not oleans:

  ```bash
  # oleans present but traces sparse ⇒ RESTORED; do not `lake build` at the root
  o=$(find .lake/packages/mathlib -name '*.olean' | wc -l)
  t=$(find .lake/packages/mathlib -name '*.trace' | wc -l)
  echo "oleans=$o traces=$t"; [ "$o" -gt 100 ] && [ "$t" -lt "$((o / 10))" ] \
    && echo "RESTORED CACHE — use lean-direct, NOT lake build"
  ```

  **Treat that as a strong hint, not a proof, and know its calibration.**
  Measured on the tree that produced this section: the restored root reports
  `oleans=6991 traces=333` (ratio 0.048, trips the check) — and those 333
  traces are themselves debris from the aborted rebuild, so a *pristine*
  restore sits nearer zero. The control available here, a genuinely
  lake-built `QOU` library tree, reports `oleans=951 traces=310` (ratio 0.33)
  and clears the 0.1 threshold by 3.3×. That margin is real but modest, and
  the control is a **paper library, not a lake-built Mathlib** — no built
  Mathlib tree existed in this sandbox to calibrate against. If you have one,
  measure it and tighten this threshold. Until then: when the check trips,
  believe it; when it does not, you still have not proved the cache is built.

  On a restored cache the gate is **`lean`-direct against the real import
  cone**, per AGENTS.md §"QA is agent-owned; CI is a backup" — which is the
  sanctioned verification path anyway, not a fallback. It verified the changed
  file on #5106 in **2.4 s** against the same cone the aborted `lake build`
  was 50 minutes into not reaching:

  ```bash
  LP="$PWD/folio/quantum-observable-universe/lean/.lake/build/lib/lean"
  for p in mathlib batteries aesop Qq proofwidgets importGraph plausible \
           LeanSearchClient; do
    LP="$LP:$PWD/.lake/packages/$p/.lake/build/lib/lean"
  done
  # -DautoImplicit=false is NOT optional — see the note below.
  LEAN_PATH="$LP" lean -DautoImplicit=false -s 65536 path/to/Changed.lean
  ```

  Then `#print axioms` on the new declarations to confirm no `sorryAx`. Say in
  the PR that this is what you ran and why.

- **🛑 A BARE `lean` DOES NOT APPLY THE LAKEFILE'S `[leanOptions]`, so it is a
  strictly WEAKER check than Lake — always pass `-DautoImplicit=false`.**
  `autoImplicit` defaults to **true** in `lean` and is set **false** in both the
  root and paper lakefiles. With it on, Lean silently auto-binds an unbound
  identifier as an implicit argument instead of erroring, so a file Lake rejects
  can pass `lean`-direct. Measured 2026-09-05 on
  `QOU/MassTheory/AtomWordShadow.lean`, same file, same `LEAN_PATH`:

  ```
  lean                        ->  exit 0,  0 errors
  lean -DautoImplicit=false   ->  exit 1,  6 errors      (lake agrees: 20)
  ```

  That file was **red on `main`** and three sweeps called it clean. Also pass
  `-s 65536`, mirroring the paper lakefile's `moreLeanArgs`: one generated module
  overflows the default elaboration stack and aborts as a bare `exit 134` with no
  source error. The sweep scripts below now pass both.

- **🛑 AND `lean`-direct against a restored cache verifies against a SNAPSHOT,
  and `exit 0` from it is a claim about that snapshot — not about the library
  source your file names.** This is the gate's own blind spot and it has been
  realised: `descartesWtrace` recorded `lean`-direct `exit 0` and **landed on
  `main` red**, because the cache was built 2026-08-30 while `794c34897d7`
  (2026-09-03) retyped `SeminormalRep.wtrace`'s genericity hypothesis and ported
  only the seven consumers *inside* the package (#6751). The library half of that
  change was done correctly; a content-block sibling was simply not in it.

  **So when your branch touches any `.lean`, run the matching sweep instead of
  bare `lean`-direct.** Both build a shadow tree, rebuild from source only the
  modules whose own olean predates their own last source commit, and compile
  against that. Neither invokes `lake`, so the restored cache cannot be evicted;
  Mathlib is never rebuilt.

  ```bash
  # content-block .lean siblings (content/**/*.lean outside a package tree)
  scripts/lean-content-sweep.sh [file.lean ...]     # no args = all 261

  # library modules (content/*/lean/QOU/**) — the DIRTY CLOSURE, which is what
  # a source-change count misses: a NEW file inherits its dependencies'
  # staleness without ever appearing in one.
  scripts/lean-library-sweep.py
  ```

  Measured 2026-09-05, whole corpus: 261 content blocks and 74 dirty library
  modules, **0 red** — content sweep ~50 min, library sweep 122 s. Pass
  `SHADOW=<dir>` / `--shadow <dir>` to reuse the ~2.3 GB shadow across runs; the
  copy is the slow part.

  **Two things the sweeps do not settle, so do not write them into a PR:**

  * **The result is container-scoped.** The dirty closure is computed against
    *this* container's olean tree. A container restored from an older cache has
    a larger closure and needs its own run. Two sessions measured the same
    dependency as stale and as current, and both were right.
  * **Sibling packages (UGB, Fred2005) are not swept** by either script.

  Bean `qou-56qy`.

- **If the root cache is cold and `cache get` will not fetch, build per-paper
  instead.** Measured in a sandbox with 9.2 GB free: the per-paper Mathlib build
  tree is 3.3 GB, so the root workspace wants a second one, and `lake exe cache
  get` there stalled — 4 seconds of CPU in 20 minutes, sitting on the network.

  Per-paper builds are an equally valid gate, not a lesser one. They compile the
  same sources against the same pinned Mathlib rev; only the `.lake` tree holding
  the oleans differs. Run all three, and say in the PR that this is what you did:

  ```bash
  (cd folio/quantum-observable-universe/lean && lake build)
  (cd folio/unital-groebner-bases/lean      && lake build)
  (cd folio/fred2005-formal-groups/lean     && lake build)
  ```

  What is *not* acceptable is the bare root `lake build`, which compiles nothing
  at all — that is the defect this section documents. Dropping to per-paper is
  the remedy for a cold cache, not a way around the gate.
- If the build fails, route to `lean-build-fix` and resolve.
- Run `lean-completeness-audit`: every `sorry` must carry a `-- Ref:`
  citation, every `definition` block must have its `.lean` sibling,
  and every provable block kind (`theorem`/`lemma`/`proposition`/
  `corollary`) must have a Lean statement.
- Run `proof-simplifier` on any proofs that changed on this branch.
- The Lean build must be green and the audit must report 100%
  coverage before continuing.
- **Say in the PR which verification you ran, in these words**, so a reader can
  tell a snapshot-conditional green from a source-verified one:
  - *"`scripts/lean-library-sweep.py`: N/N dirty modules rebuilt from source,
    exit 0"* — source-verified.
  - *"`lean`-direct against the restored cache, exit 0"* — snapshot-conditional;
    say so, and say why the sweep was not run.

  Never write "CI green" (no run exists — auto-triggers are disabled repo-wide),
  and never write "verified" unqualified over a bare `lean`-direct run on a
  branch that touches `.lean`.

## 4a. Mirror-drift gate (BLOCKING on growth)

```sh
python3 scripts/mirror-drift-audit.py --baseline
```

> **🛑 The command this section used to name did not exist (corrected 2026-09-05).**
> It read `bun run <folio-assistant>/scripts/check-mirror-drift.ts --package qou
> --baseline 35`. Measured: **no such file**, not in this repo and not in the
> `folio-assistant` clone — so for as long as that line stood, this "BLOCKING"
> gate could only ever error out, and a section that names a missing script is
> worse than no section, because it reads as covered.
>
> The one audit that sounds adjacent,
> [`scripts/lean-duplicate-fqn-audit.py`](../../scripts/lean-duplicate-fqn-audit.py),
> does **not** substitute: its own SCOPE note says it walks the library tree only
> and that *"a clean run here is not evidence that a name is unambiguous in the
> corpus."*
>
> The replacement, [`scripts/mirror-drift-audit.py`](../../scripts/mirror-drift-audit.py),
> is the missing half — it reuses that script's parser (so the namespace-stack and
> comment-stripping calibration is not re-litigated) and measures the sibling
> surface. Baseline: [`docs/audits/mirror-drift-baseline.json`](../../docs/audits/mirror-drift-baseline.json).
>
> **Read the baseline before acting on a hit.** Two things it records that the
> table below does not:
> - **A faithful live mirror is NOT a defect.** This gate is on *drift*; a
>   `definition` block is *required* to carry a sibling (§3), so deleting a
>   faithful mirror breaks that requirement. Of 12 live shadows, **7** are
>   actionable.
> - **Do not assume the library is canonical.** Across the 163 substantive drifts,
>   **91 have the library edited more recently and 70 the sibling** — and recency
>   is not canonicality. `QOU.Information.speedOfLight` has the *library* edited
>   later while the *sibling* is the §7c-compliant one (generic base ring,
>   division-free, defining relation discharged as a theorem). Every
>   reconciliation requires reading both sides.

A green Lean build does not mean the checkers looked at the code it compiled.
Content-block `.lean` siblings compile standalone and cannot import one another,
so a sibling needing a library type **restates it**. That is deliberate. What is
not deliberate is the two copies drifting — because a co-located `<block>.lean`
wins **candidate 1** of `lean.ref` resolution, before any Lake-tree candidate,
so every checker aimed at that block audits the sibling's copy and never sees
the declaration `lake build` just compiled.

Measured 2026-08-23 (bean `qou-u87j`), all columns with the current parser:

| | `main` @797db0ebf7 | `qou-u87j` branch | after merging `main` |
|---|---|---|---|
| same-FQN pairs | 141 | 148 | 141 |
| faithful mirrors | 91 | 111 | 106 |
| **drifted** | **43** | **37** | **35** |
| drifted **and** crossing the §7c wall | 7 | **0** | **0** |
| §7c regime-only | 7 | **0** | **0** |

The middle column is the branch *before* it took `main`; the right column is
what is on disk. Pair count drops back to 141 because the merge brought in
`main`'s deletion of 11 content siblings that had shadowed the library —
`main` had been draining this same population from the other end.

Every drifted pair masks a `lean.ref`, in all three columns. `pairs = faithful
+ regime-only + drifted`; the two 7s on `main` are different sets —
`regimeOnly` is same-fields-opposite-wall and is *excluded* from `drifted`,
while `driftedRegime` is the subset of `drifted` that also crosses. Equal by
coincidence, and easy to double-count.

- **`--baseline 35` fires on growth only** (exit 3). A gate that failed on the
  whole backlog would just teach everyone to pass `--warn-only`; this one stops
  the 106 faithful mirrors becoming the next 35.
- **If you touched a mirrored declaration, resync both copies in the same
  change.** The checker names the file and line on each side and prints the
  field-level diff; `--tsv` gives one row per pair.
- **Lower the baseline when you drain some.** It is a ratchet, like the
  float64 ones in §4b — leaving it at 35 after fixing five means the next five
  regressions go unnoticed.
- **The two §7c counters are at 0 and should stay there.** They are the reason
  this gate was built; what is left under `qou-u87j` is plain field drift with
  no wall component. If either goes non-zero, that is a regression, not backlog.
- `--max 0` is the end state once the backlog is gone.

Worked example of why it is not cosmetic — `QOU.CRManifoldData`: the library
copy carries `n_pos : 0 < n` and the two siblings do not; the siblings carry
`contact_nondeg` and `reeb_preserves_contact` and the library does not. Each
side has an anti-vacuity condition the other lacks, so whichever one a reader
or a checker reaches, it is not the one the other half of the corpus means.

### The §7c line in the same output — read it, it is not gated

The checker also reports a **`regime`** count: pairs that agree on every field
name and parent and still sit on **opposite sides of the substrate→archimedean
wall**, judged by the corpus's own `ARCHIMEDEAN_TYPE_RE` on field *types*. On
`main` that is **7 regime-only pairs across 5 files**, plus **10** of the 46
drifted pairs crossing the wall as well — 17 §7c disagreements in total.

**No baseline flag covers this yet**, deliberately: the fix is a wall split, not
a field resync, and folding it into the drift number would make that number move
for two unrelated reasons. Treat the line as a read-and-judge item. If your
change adds one, fix it rather than let it ride.

Why it needs a check of its own: **`check-wall-side` and `check-base-ring` PASS
on every one of these files.** They fire on a file that *mixes* regimes, so a
declaration **wholly** on the wrong side passes both. Passing the wall gate
means "not mixed", not "on the right side of the wall" — bean `qou-6ome`.

Direction is per-case and all three shapes occur:

| shape | example | how to spot it |
|---|---|---|
| the **library** never migrated | `QOU.SubstrateParameter` (`qou-6ome`) | the block defines the categorical form; the siblings already split |
| the **sibling** over-generalised | `QOU.QReebFlow` | the sibling's own docstring records the divergence and leaves it standing |
| the sibling over-generalised **and lost content** | Möbius energy | conditions commented out with "(archimedean; not meaningful over `R_q`)" |

**The block's `.md` adjudicates, not the field diff.** The diff cannot tell you
which side is behind — `QOU.SubstrateParameter` reads as "sibling is missing
three fields" when in fact the siblings are correct and the library never made
the split.

This lives here rather than in `.github/workflows/` for the reason §4b gives:
the CI copy does not run.

### Duplicate declarations — run it in the same breath

```sh
bun run <folio-assistant>/scripts/check-duplicate-decls.ts --package qou --baseline 57
```

Same family of defect — the library disagreeing with itself — and the same kind
of blind spot. Lean's environment is flat, so two modules declaring the same
fully-qualified name **cannot both be imported by anything**. Not a shadowing
warning, not a use-site ambiguity; the import fails:

```
error: import QOU.CategoricalDqSquared failed, environment already contains
       'QOU.q_param' from QOU.BraidKnot.CasimirShared
```

Measured 2026-08-23 (bean `qou-kfcl`) — the earlier text labelled the
right-hand column "main", which it never was:

| | `main` @797db0ebf7 | `qou-kfcl` branch | after merging `main` |
|---|---|---|---|
| declarations scanned | 34 138 | 33 793 | 34 136 |
| **duplicated FQNs** | **66** | **56** | **57** |
| un-importable module pairs | 65 | 61 | 62 |
| modules involved | 72 | 64 | 66 |

The worst was `QOU.R_q` — `RatFunc ℚ` in one module and `LaurentPolynomial ℤ`
in the other, the same name for two different rings. That one is resolved:
`QOU/GroundRingCore.lean` is the canonical minimal module (one Mathlib import),
and no `R_q`, `q_param` or `q_inv_param` appears in the report any more.

**The baseline went 56 → 57, which is a ratchet loosening and needs its
reason.** The merge brought in exactly one new duplicate and nothing was lost:
`QOU.Mathlib.Schensted.wordOfPerm_injective`, a `theorem` declared at both
`QOU/Mathlib/SchenstedPermInjective.lean:42` and
`QOU/Mathlib/SchenstedRSKPairInjective.lean:68`, which arrived with `main`'s
RSK–Burnside work. Set-differenced against the pre-merge list rather than
inferred from the totals — 57 new, 0 gone. Lower it back to 56 when that pair
is resolved.

- **A green Lean build says nothing about this.** `lean-direct-cone.sh --all`
  compiles each module against its own cone, and no *existing* module imports
  both halves of any colliding pair — 2029/2040 modules, `err=0`, on the very
  commit with 64 un-importable pairs. The error is only reachable by writing a
  new module, which is how it was found: it blocked a `qou-u87j` fix.
- **Ratchet, like the drift gate.** Lower `--baseline` as pairs are resolved.
- **Verify before acting** on any individual finding by writing the two-line
  import. Two earlier counts of this population (38, then 80) were wrong;
  the compile has never been.

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

## 4c. Voice-leak ratchet (BLOCKING on growth)

- Run `bun run folio/pipeline/voice-leak-ratchet.ts`. It runs
  [`voice-leak-audit.ts`](../../folio/pipeline/voice-leak-audit.ts) (Lean talk
  in prose, backticked Lean or repository identifiers, first/second person,
  reading-order anachronisms in Part I) and compares the failing-hit count per
  file and per leak kind against
  [`voice-leak-baseline.json`](../../folio/pipeline/voice-leak-baseline.json).
  Exit 1 means this branch **added** a leak.
- **Fix the leak, never the baseline.** Restate the sentence in mathematical
  terms; move Lean declaration names to the block's `.ts` `lean` /
  `authorNotes`; replace a raw-label link text by the target's title. A
  sentence that carries a real scope caveat ("Lean checks this only
  through …") is restated, not deleted.
- **The baseline only drains.** If the run reports counts below baseline, run
  it again with `--shrink` and commit the smaller baseline with the drain. That
  is the only supported edit: `--shrink` lowers counts and drops entries, and
  cannot add or raise one. Never hand-edit the file to go green.
- Owner ruling 2026-11-20 (#8526 comment 7041693067, W14 option 5): a
  draining ratchet rather than a hard gate, so that a PR touching a leaky
  block is not made to fix that block's older leaks.

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
