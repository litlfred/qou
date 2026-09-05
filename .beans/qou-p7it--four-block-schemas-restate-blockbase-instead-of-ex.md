---
# qou-p7it
title: 'Four block schemas restate BlockBase instead of extending it; five qou manifest fields silently dropped (PR #6501 / folio-assistant#164)'
status: completed
type: bug
priority: normal
created_at: 2026-09-03T20:35:52Z
updated_at: 2026-09-05T09:00:15Z
---

## Two defects, one shared cause

`scripts/run-validate.ts` reported **6** `Unknown field` warnings on the qou
corpus. A Zod object is non-strict, so each key was **stripped and the parse
succeeded** — no error, nothing downstream, nothing told the author.

**Five are invented names** (qou-side, PR #6501): `is_mathematics: true` on
three `mass-theory` propositions, and `probe: "audit/positron-correction-probe"`
+ `consumers: []` on `prop:positron-correction`. Measured before touching
anything: all five are **write-only** — no reader anywhere in `content/`,
`computations/` or the pipeline, and no other block uses the names, so they were
never a convention that had drifted. Each was written once and lost.

- `is_mathematics` moved to `meta` (the declared `Record<string, unknown>`
  escape hatch on `BlockBase`), deliberately not deleted and not guessed at.
- `probe` named a probe that **does not exist** — the only positron compute is
  the deprecated `computations/_deprecated/positron_lifted_sdp.py` — so it could
  not become `computation.script`, which resolves against a real file. Recorded
  as an `authorNote` so the intent survives. `consumers: []` dropped.

**One is a schema gap** (folio-assistant#164): `prose`, `equation`, `diagram`
and `table` each *restate* their field set rather than extending
`BlockBase` / `BlockBaseSchema`. Live victim today: `prose:knot-periodic-table`
declares a `computation` and has it dropped.

Measured a week after the 2026-08-24 grant that added `authorNotes` to those
four by hand: `defines` still absent from **all four**, `cites` / `simulator` /
`computation` from three. **`defines` is the sharp one** — AGENTS.md §4c
*requires* every glossary term in `defines[]` and `defterm-declared` reads that
array, so on those kinds a term could not be declared at all, indistinguishably
from an authoring choice.

Fixed structurally: the four now extend `Omit<BlockBase, "label">` (TS cannot
loosen a required property through `extends`), plus a new guard
`scripts/tests/block-base-fields.test.ts` that fails when any block schema falls
behind the base — derived by unwrapping `BlockSchema`'s union, so a kind added
later is covered without editing the test, and round-tripping a parse as well as
inspecting shapes.

## TRAPs recorded

- **A CI-availability fact does not cross a repo boundary.** I carried qou's
  "Actions are `workflow_dispatch`-only" into folio-assistant, which has **real
  CI** (6 checks); my first push failed it. Verified qou's half directly
  afterwards: `get_check_runs` on #6453 and #6501 both return `total_count: 0`.
- **`bun install` had never been run in the fa workspace**, so `tsc` reported 5
  module-resolution errors that I recorded as "the pre-existing baseline". With
  45 packages installed, my file's error was the **only** one in the repo.
- **A "precise" type can be false precision.** The union unwrap was cast as
  `z.ZodEffects<z.ZodDiscriminatedUnion<"kind", z.ZodObject<z.ZodRawShape>[]>>`,
  which *looks* tighter than a structural assertion and is not:
  `ZodDiscriminatedUnionOption<"kind">` needs `{ kind: ZodTypeAny } &
  ZodRawShape`. The spelling was a compile error proving nothing extra at
  runtime.
- **CI tests the MERGE REF, not the branch head.** The first CI log showed only
  my error although `content/pipeline/q-usage-audit.ts` had a genuine TS2552 at
  my base — main had already fixed it.
- **A source-text walker must follow the construct the source uses.**
  `schema-ts-zod-parity.test.ts` follows `interface X extends Y` but not
  `type X = Omit<Y, ...>`, so 6 of its tests failed on a tree where the drift
  they exist to catch had just been *repaired*. Taught it to resolve `Omit<>`.
- **Local test counts are not repo counts.** I reported "1219 pass / 23 fail ->
  1227 / 15" as if repo-wide; those failures are Lean tactic-ladder suites CI
  skips, and CI reports 1352 pass / 0 fail.
- **The validator you ran is the validator in the clone.** AGENTS.md §4d's own
  figures were taken against a fa checkout at `e1030e8`, already behind main —
  which is how it came to advise agents *not* to put an author note on those
  four kinds, a field that has worked since 2026-08-24. §4d corrected, with the
  superseded text kept and marked.

## Verification (re-measured after main took 55 commits)

`ff30b80913` merged onto `main` @ `2a7dfce761`, fa at `d013481`: clean merge,
validate **exit 0**, `Unknown field` **0**. The 3 residual issues are
pre-existing and outside this diff (no reference registry configured;
`lem:piece-a-corner-removal-obligation` has no Lean decl;
`em-coupling-projection-table1-data` cross-refs an undefined
`def:local-substrate-q`).

folio-assistant#164: **6/6 check runs success** on `d013481`, and fa `main` is
still exactly its base `e7f5f55`, so that CI ran on the current merge ref.

## Status

Both open and `mergeable_state: clean`, waiting only on merge permission.


## Coordination note (not a claim on this bean) — 2026-09-05

Leaving this bean to its owner; recording one measurement it depends on.

**The folio-assistant half has LANDED.** `a117daa` (2026-09-03, *"Four block
kinds restated BlockBase instead of extending it"*) is confirmed an ancestor of
folio-assistant `origin/main`, along with `affcec4`. Verified by parse rather
than grep: `ProseSchema`/`EquationSchema`/`DiagramSchema`/`TableSchema` each
retain `authorNotes`, `defines`, `cites` and `computation` on `safeParse`.

**The qou half has landed too**: 0 top-level `is_mathematics`/`probe`/
`consumers` remain in `content/` (the 7 residual grep hits are `consumers:`
nested inside `computation:`, which is declared and correct).

So if this bean's scope is exactly *"the four schemas + the five invented
fields"*, both halves are now in the product and it is closeable on evidence —
but that is its owner's call, not mine.

`qou-3v8h` and `qou-eu0r` are closed with the full evidence. This session's
change was to **AGENTS.md 4d only**: the box led with the retracted claim and
closed by telling agents not to use a field that works.
