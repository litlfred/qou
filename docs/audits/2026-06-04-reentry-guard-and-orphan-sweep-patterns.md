# Two reusable cleanup patterns from the 2026-06-04 session

Durable record of two patterns that came up multiple times this session
and will recur. Written so the next agent can apply them without
rediscovering.

## Pattern 1 — NEGATIVE-finding re-entry guard (AST registry)

**When to use.** A non-canonical form has been DISPROVED (e.g.
falsified bijection, withdrawn empirical fit, owner directive "no X in
production") and explicitly PURGED, but the codebase has memory:
sibling branches and refactors keep re-introducing the same form. A
text grep is too loose (catches comments) and too narrow (misses
aliases, attribute access, `def`s, etc.).

**The pattern.** A small Python audit script under
`computations/audits/` that:

1. **Maintains a provenance-backed registry** of banned symbols /
   modules / prefixes — each entry carries `reason`, `purged_by` (PR
   number / commit SHA), and `canonical_replacement`. Reviewing the
   registry IS the documentation of the purge.
2. **Parses source via `ast`, not regex.** Comments are not in the AST
   at all (the parser strips them); docstrings are present as
   `ast.Expr(value=ast.Constant(...))` but the visitor never flags
   `Constant` / `Expr` node types, so neither appears as a re-entry.
   Only real `import` / `def` / `class` / `Name` / `Attribute` / `arg`
   / `keyword` references trigger. This eliminates the "honest
   historical mention is flagged as a re-entry" false-positive class
   that grep has (Copilot review #1877).
3. **Covers ALL the re-introduction vectors.** Not just `from x import
   <banned>`. The session converged on **9 vectors** through review
   feedback:

   | vector | AST node | example |
   |---|---|---|
   | `import-module` | `ast.Import` + `_module_banned` and `_symbol_banned` on `alias.name` | `import lambda_scale_family_a` |
   | `import-alias` | `ast.Import`/`ast.ImportFrom` + `alias.asname` | `import x as lambda_scale_family_a` |
   | `import-symbol` | `ast.ImportFrom` + check on `alias.name` (against both registries) | `from substrate import lambda_yekutieli_extended_borromean` |
   | `import-from-module` | `ast.ImportFrom` + `_module_banned(node.module)` | `from lambda_yekutieli_extended_borromean import x` |
   | `def` | `ast.FunctionDef` / `ast.AsyncFunctionDef` / `ast.ClassDef` | `def lambda_scale_X(...)` |
   | `name-use` | `ast.Name` | `x = lambda_scale_family_a(Q)` |
   | `attribute-use` | `ast.Attribute` (check `node.attr`) | `mod.lambda_scale_family_a(...)` |
   | `keyword-arg-use` | `ast.keyword` (check `node.arg`, skip `**kwargs`) | `foo(lambda_scale_family_a=v)` |
   | `param-def` | `ast.arg` (check `node.arg`) | `def f(lambda_scale_X=None)` |

   The naive first version covered 3 (import, def, name-use) and Copilot
   + Gemini reviews surfaced the remaining 6. Start with all 9 from the
   beginning.
4. **`--strict` fails CI on detection AND on parse errors.** A
   non-parseable production script is a blind spot — fix the script,
   don't allowlist the file. The session fixed two such pre-broken
   scripts (`casimir_mode_indexed_derivation.py` `\u` in docstring →
   raw-string prefix; `pm_qm_pythagorean_identity.py` mis-indented
   import) and added a `no_unparseable_production_scripts` strict
   assertion.
5. **Excludes `_deprecated/`, `__pycache__/`, `probes/`** by walking
   `path.relative_to(root).parts` and skipping any directory in an
   exclusion set. Filename-prefix filters (`p.name.startswith("_")`)
   ARE NOT ENOUGH — they skip `_bridge.py` but not files INSIDE
   `_deprecated/`. This same trap caught the fitted-labelled audit and
   was fixed in PR #1828.
6. **Registered as a strict CI step** in `.github/workflows/witness-pipeline.yml`
   under the `validate` job, alongside the existing
   `fitted_labelled_canonical_audit`.

**Canonical implementation:** [`computations/audits/noncanonical_reentry_audit.py`](../../computations/audits/noncanonical_reentry_audit.py),
landed in PR #1819 + hardened in #1819's review rounds.

**Verification recipe.** Run a negative test BEFORE pushing: inject a
test file with one example of each vector, run `--strict`, confirm exit
1 with all vectors flagged. The session's negative test was 8 lines
producing 9 violations (line 6 fires twice: `param-def` + `name-use`).

## Pattern 2 — reorg-orphan sweep (cherry-equivalence guard)

**When to use.** A subdir refactor moved scripts out of a flat
directory into thematic subdirs (`hecke/`, `qbeta/`, `audits/`, …).
Per-script sidecars / aggregates / witness JSONs may have been **left
behind at the pre-reorg flat path**, becoming orphaned: their stored
`source_hash` no longer matches any script at the expected location, so
the staleness checker flags them as perpetually-stale noise.

The 2026-06-02 reorg orphaned **333 script-qa sidecars** at
`computations/script-qa/` (PR #1845), plus **150
moved-subdir scripts** that needed correct-path aggregate regeneration
(PR #1862).

**The pattern (delete OR relocate, three steps).**

1. **Detect.** For each artifact at the old flat path, check whether
   the producer/script exists at the expected location. Use a strict
   exclusion set (`_deprecated`, `__pycache__`, `script-qa`, …) and
   walk relative parts (NOT filename prefix). Classify:
   - `legit` — producer still at flat path; keep as-is
   - `MOVED` — producer in a subdir; the orphan sidecar is the wrong path
   - `GONE` — producer deleted; sidecar is pure cruft
2. **Cherry-equivalence safety check.** Before any destructive bulk
   action: `git log --cherry-pick --right-only --no-merges
   main...<branch> --oneline | wc -l` — if 0, the branch's commits are
   patch-equivalent to main (work preserved). This same check enables
   confident bulk delete and safe branch cleanup.
3. **Sweep.** For pure-deletion (GONE) and wrong-path (MOVED whose data
   is regenerable from an authoritative criterion store): bulk
   `git rm`, single mechanical commit. For relocation: a fresh
   regeneration tool (e.g. `bun run script-sweep.ts --filter <path>
   --only <criterion>`) at the correct path. **Confirm no CI gate
   requires the artifact's existence** before deletion (check workflow
   yml for any missing-sidecar / coverage gate).

**Three pitfalls the session hit.**

- **Sibling collision.** If another agent owns a campaign touching the
  same store, defer or coordinate. Check the active siblings via
  `git diff --name-only $(git merge-base sibling main)..sibling` for
  overlap before bulk-writing. (PR #1862 caught this against
  `qa-staleness-per-entry-srchash` — turned out to be no collision, but
  the check was right.)
- **Selective revert of timestamp-only churn.** Tools that re-run on
  many entries may bump `last_run_at` / `reviewed_sha` for every
  touched file, even when the substantive content is unchanged. Use a
  selective **per-file** diff (`git diff <file> | grep -E "^[+-]" |
  grep -vE "^(\+\+\+|---)" | grep -vcE
  "last_run_at|generated_at|reviewed_sha"`) — invoked once per touched
  file, not on the whole tree — and `git checkout --` the files with 0
  substantive lines. Keeps PRs reviewable. (Gemini review #1877.)
- **JSON key reorder ≠ value reattribution.** Removing then
  regenerating a JSON entry can re-append it at the end of an object;
  line-based diffs misalign keys against values and read as
  "criterion X is now under criterion Y." JSON is keyed, not
  positional, so values are correct — but the alarming diff is
  legitimately confusing. Restore canonical key order before pushing
  (read main's order, sort accordingly). PR #1854 hit this and fixed
  it after Copilot review.

**Canonical PRs:** #1843 (single-script relocate), #1845 (333-orphan
sweep), #1862 (350+ subdir regen).

## When neither pattern applies

The orphan-witness audit (`computations/*.witness.json`)
returned **0 real orphans / 6 documented legacy items** when applied to
witness JSONs. That null result is itself useful: the pattern is not
universal — it specifically afflicts sidecars/aggregates whose source
file moved AND that aren't kept in sync by their own pipeline. Witnesses
are pinned by `scriptFile` declarations that get resolved relative to
the witness dir, so the witness pipeline already handles relocation.
Apply the pattern where the artifact's existence depends on a directory
convention; skip where the artifact carries its own relocation pointer.
