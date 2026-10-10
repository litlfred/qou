---
# qou-dg4x
title: 'INFRA: lakefile doc-gen4 block active + over-broad CI sed — FIXED (sentinel-scoped, with guards)'
status: completed
type: task
priority: normal
tags:
    - lean
    - infra
    - ci
    - lakefile
created_at: 2026-08-07T18:40:00Z
updated_at: 2026-08-07T18:55:00Z
---


## Symptom

Every **local** `lake build` in `content/quantum-observable-universe/lean` clones
and builds `doc-gen4` and its ~20 heavy metaprogramming modules. Hit while
building a single leaf file (`QOU.QBeta.FiveTwoCyclotomicBloch`, PR #4658): the
build stopped to `cloning https://github.com/leanprover/doc-gen4`.

This is **exactly the failure the lakefile's own comment warns about**:

> doc-gen4 is CI-only (blueprint.yml uses docgen-action; lean_ci.yml has a
> fallback source browser). Requiring it here forces ~20 heavy metaprogramming
> modules into every local `lake build`, which can hang on resource-constrained
> machines. **Un-comment if you need local docs.**

## Cause

The comment describes the intended state — **commented out** — and is followed by
an orphan `#` line and then the `[[require]]` block **uncommented and active**.
Compare `checkdecls` immediately below, which *is* properly commented out. So the
block was meant to be disabled and currently is not.

`.github/workflows/doc-gen4.yml` confirms the intent: it has an *"Enable doc-gen4
in lakefile.toml"* step that un-comments the block itself before building docs.
Those `sed`s are currently **silent no-ops** — nothing matches `# name = "doc-gen4"`
because the block is already active. **CI works by accident**, local builds pay
the cost.

## ⚠ THE TRAP — do not apply the obvious fix

The naive repair ("just re-comment the doc-gen4 block") **breaks the docs CI**,
because the workflow's first `sed` is file-wide and not doc-gen4-specific:

```sh
sed -i 's/# \[\[require\]\]/[[require]]/' lakefile.toml        # <-- matches EVERY commented require
sed -i 's/# name = "doc-gen4"/name = "doc-gen4"/' lakefile.toml
sed -i 's|# git = "https://github.com/leanprover/doc-gen4"|git = ...|' lakefile.toml
sed -i 's/# rev = "1cd7a11...."/rev = "1cd7a11..."/' lakefile.toml
```

Today the first `sed` already un-comments the **dead `checkdecls` block's**
`# [[require]]` line, while its `# name` / `# git` / `# rev` lines stay commented
(they match none of the later, doc-gen4-specific patterns). That leaves

```toml
[[require]]
# name = "checkdecls"
# git = "https://github.com/PatrickMassot/checkdecls"
# rev = "master"
```

— a `[[require]]` table with **no fields**. Re-commenting doc-gen4 does not
introduce this; it is *already* the case on every docs-CI run. It is presumably
tolerated only because that trailing table is last in the file and/or the docs
workflow is not gating.

## The fix, which must do BOTH

1. Re-comment the doc-gen4 `[[require]]` block **in exactly the form the seds
   expect** — `# [[require]]`, `# name = "doc-gen4"`,
   `# git = "https://github.com/leanprover/doc-gen4"`,
   `# rev = "1cd7a1113090e216703e323e8fdcdf099f0a9c8a"` — and delete the orphan
   `#` line left behind.
2. **Delete the dead `checkdecls` block** (or make the workflow's first `sed`
   doc-gen4-scoped, e.g. an address range). It is unused, its `rev = "master"` is
   unpinned anyway, and while it exists the file-wide `sed` will keep producing a
   fieldless `[[require]]`.

Fixing only (1) leaves the collision; fixing only (2) leaves local builds slow.

## Not done here, deliberately

This is CI-critical config and PR #4658 is about the 5₂ dilogarithm sum rule.
Changing the docs pipeline from that PR is scope creep and the failure mode is
non-obvious enough to deserve its own change with owner eyes on it. **Recorded,
not applied.**

## Verify after fixing

```sh
cd content/quantum-observable-universe/lean
lake build QOU.QBeta.FiveTwoCyclotomicBloch   # must NOT clone doc-gen4
# then dry-run the workflow's seds on a copy and confirm lakefile.toml still parses
```

## Refs

* `content/quantum-observable-universe/lean/lakefile.toml`
* `.github/workflows/doc-gen4.yml` (the "Enable doc-gen4 in lakefile.toml" step)
* found while building for PR #4658 / bean `qou-b7cy`

---

## ✅ FIXED 2026-08-07 — sentinel-scoped sed, with two guards

Both halves done, and **the bug was demonstrated before fixing it** rather than
argued: replaying the old seds over the old `lakefile.toml` produces

```
[[require]]
# name = "checkdecls"
```

— a fieldless `[[require]]`, exactly as predicted. Not theoretical.

**`checkdecls` was NOT deleted.** It is referenced in
`.claude/skills/local/lean-generation.md:258` ("CI validates via
`lake exe checkdecls blueprint/lean_decls`"), so it is documented intent even
though no workflow wires it up yet. Deleting a collaborator's config to work
around our own over-broad `sed` is the wrong repair — the `sed` was the bug.

**lakefile.toml** — doc-gen4 block re-commented, orphan `#` removed, and wrapped
in sentinels:

```toml
# --- BEGIN doc-gen4 (CI-only) ---
# [[require]]
# name = "doc-gen4"
# git = "https://github.com/leanprover/doc-gen4"
# rev = "1cd7a1113090e216703e323e8fdcdf099f0a9c8a"
# --- END doc-gen4 (CI-only) ---
```

**`.github/workflows/doc-gen4.yml`** — the four file-wide seds replaced by one
range-scoped sed that strips `# ` only from `[[require]]`/`name`/`git`/`rev`
lines *between the sentinels*, plus two guards:

1. `grep -q '^name = "doc-gen4"'` — **fail loudly instead of no-opping.** The old
   step silently succeeded whenever the block was already active, which is
   precisely how the lakefile drifted out of sync with its own comment and went
   unnoticed.
2. An `awk` check that every `[[require]]` is followed by a `name =` line, so the
   fieldless-table failure can never recur silently.

**Verified:** dry-running the new sed on the real file enables doc-gen4, leaves
`checkdecls` commented, and leaves no fieldless `[[require]]`. Local
`lake build QOU.QBeta.FiveTwoCyclotomicBloch` still succeeds (707 jobs).

## Deliberately NOT changed: `lake-manifest.json`

The committed manifest still lists `«doc-gen4»` and its transitive deps
(`UnicodeBasic`, `BibtexQuery`, `MD4Lean`), so it is now out of step with a
commented-out `require`. Left alone on purpose:

* the build is unaffected — verified, 707 jobs green;
* the docs workflow runs `lake update doc-gen4` right after enabling, which
  reconciles the lockfile itself;
* regenerating it here would risk churning **unrelated package pins** on a PR
  about the 5₂ sum rule.

If a future change wants the lockfile tidy, do it deliberately and diff the pins.
