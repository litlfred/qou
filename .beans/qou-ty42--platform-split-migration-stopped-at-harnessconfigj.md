---
# qou-ty42
title: 'PLATFORM SPLIT: migration stopped at harness.config.json — the pin stays at df28d02 (owner ruling)'
status: todo
type: task
priority: normal
created_at: 2026-09-20T14:33:42Z
updated_at: 2026-09-20T14:34:07Z
---

**Owner ruling, 2026-09-20: stop here.** The migration is deliberately
incomplete. Everything below is what remains, so a later agent knows the state
is a DECISION rather than an abandonment — and does not "finish" it unasked.

## Where it got to

`litlfred/qou#7446` (branch `claude/platform-bump-prep`), on top of `#7445`:

| # | change | status |
|---|---|---|
| 1 | `harness.json` declaring the folio graph at `content/` | **done**, merged as `0e1b226d` |
| 2 | `setup-folio-assistant.sh` detects the platform layout | **done**, #7446 |
| 3 | `folio.config.json` → `harness.config.json`; `typedoc.json` entry 4 | **done**, #7446 |
| 4 | decouple `.github/workflows/build.yml` from `publish.yml@main` | **NOT DONE** |
| 5 | bump `.folio-assistant-pin` `df28d02` → platform main | **NOT DONE — owner's call** |
| — | delete `folio.config.json` | **NOT DONE**, and must not be, see below |

## Why stopping here is a coherent place to stop

qou now works against **either** platform layout. `setup-folio-assistant.sh`
probes for `cat-harness/schemas/types.ts` and points the in-repo symlink at
whichever root holds the platform, so the pre-split clone the pin still names
and a current split clone both resolve. The bibliography bridges are guarded on
the same probe. Nothing in #7446 requires the pin to move.

## What remains, and what each one costs

### Step 4 — `build.yml` calls the platform at `@main`

`qou/.github/workflows/build.yml:10`:

    uses: litlfred/folio-assistant/.github/workflows/publish.yml@main

`.folio-assistant-pin` exists precisely so the platform cannot move under qou
without a reviewable commit. This line **bypasses it**: qou's published build
tracks the platform's default branch whatever the pin says. The workflow is
`workflow_dispatch`-only (owner directive 2026-06-30, billing), so it is not
firing today — which is why this has cost nothing so far, and why it will
surprise whoever dispatches it next.

Fix is one of: pin a SHA in the `uses:` line (simplest, but now TWO pins to
keep in step), or read the pin file (Actions cannot interpolate a file into
`uses:`, so this needs a generated line or a wrapper job), or vendor
`publish.yml` into qou.

### Step 5 — the pin bump

**This is the owner's call and was declined on 2026-09-20.** If it is ever
taken, `.folio-assistant-pin`'s own header states the rule: quote the
before/after `run-validate` counts, measured **at the same corpus commit**.

Measured at the time of the ruling, so a later agent does not re-derive it:

    platform main (b680b431), corpus = branch head WITH harness.config.json
      run-validate content/quantum-observable-universe  ->  2 issue(s)

    the pin's own recorded baseline (df28d02)            ->  3 issue(s)

**Do not quote `3 → 2` as the bump's effect.** Those two numbers are at
different corpus commits: one of the three was `Render/AST validation not
performed … undetermined (no harness.config.json)`, which #7446 fixes, not the
platform. A true before/after needs a second clone at `df28d02` run against
TODAY's corpus. Bean `vbase` records a round of argument that an ill-defined
baseline already cost here.

The 2 remaining are pre-existing and unrelated: the reference registry is off
outside `--strict` by design (`qou-cite`), and one lemma has no Lean
declaration.

### `folio.config.json` — leave it

It is inert: the platform stopped reading that name on 2026-09-18 and it is not
a fallback. It stays because the pin still names a **pre-split** platform, and
deleting it would strand that checkout with no config at all. **Delete it only
after the pin moves**, never before.

## One thing found on the way that is not part of this

qou has **no caller of `export-bibtex`** by any route, so `references.bib` is
not regenerated from here. Pre-existing, unrelated to the split, and not
addressed by #7446. Worth its own bean if anyone wants the .bib current.

## Done when

- [x] qou resolves against either platform layout
- [x] the folio declares where its content is, and what it is
- [x] the remaining steps are written down rather than half-applied
- [ ] **owner:** whether Step 4 (`build.yml@main`) is worth doing on a
      workflow that is dispatch-only today
- [ ] **owner:** the pin bump, with a same-corpus before/after
