---
# qou-wdh9
title: 'GAP: the validate gate cannot RUN in a stock container — bun fails to resolve unist-util-visit-parents, so qou-mwmn and qou-mln9 are uncheckable'
status: completed
type: task
priority: normal
created_at: 2026-09-13T11:26:51Z
updated_at: 2026-09-13T12:14:51Z
---

## Measured 2026-09-13

`bun run scripts/run-validate.ts content/quantum-observable-universe` **exits 1
without validating anything**:

```
error: Cannot find module 'unist-util-visit-parents/do-not-use-color'
  from '/root/.bun/install/cache/unist-util-visit-parents@6.0.2@@@1/lib/index.js'
Bun v1.3.11 (Linux x64)
```

Three lines of output, no validation performed. **`bun install` does NOT fix
it** — measured: ran it (exit 0), re-ran validate, byte-identical failure.

## Why it matters more than an ordinary tooling nit

Two open beans assert `main` is broken **and neither can be checked**:

- `qou-mwmn` (`todo`) — *"main is currently INVALID: 4 eightfold-way
  unresolved-uses errors"*
- `qou-mln9` (`todo`) — *"main validate gate RED: 20 unresolved-ref errors"*

Both are claims about the validate gate's output. With the gate unable to run in
a stock container, they can be neither confirmed nor cleared, and an agent that
tries will get `exit 1` and may read it as *"validate is red"* — which is the
same word for a completely different thing. **`exit 1` here means the checker
never started**, not that the corpus failed.

## What is NOT established

- Whether this is container-specific or reproduces for the owner. Not tested
  elsewhere.
- Whether it is the pinned platform. `.folio-assistant-pin` is `df28d02` and the
  clone matches it, so this is the intended platform — but the pin note records
  `df28d02` measuring "3 issue(s)" against a 2026-09-07 corpus, i.e. the gate DID
  run then. So either the container or something since has changed.
- Whether other bun entry points are affected. Only `run-validate.ts` was tried.

## Diagnosis, as far as it goes

`unist-util-visit-parents@6` exposes `./do-not-use-color` as a **conditional
subpath export**. Bun is resolving the dependency straight out of its global
install cache rather than a materialised `node_modules` (there is none in either
`qou/` or the `folio-assistant/` clone), and does not honour that subpath there.
So it is a resolver/packaging interaction, not a missing package — the package
is present in the cache.

Next honest step: materialise `node_modules` in the **`folio-assistant/` clone**
(not just `qou/`, which is where `bun install` was run) and retry; if that fixes
it, the fix belongs in `scripts/setup-folio-assistant.sh`.


## RESOLVED 2026-09-13T12:0xZ — the gate runs, and my own "where the fix goes" was WRONG

**The fix.** `bun install` in the **folio-assistant clone** (`/home/user/folio-assistant`),
not in `qou/`. 335 packages, 3.6 s, exit 0. The gate then runs end to end.

```
bun run scripts/run-validate.ts content/quantum-observable-universe
  platform (folio-assistant): df28d02 (/home/user/folio-assistant)
  bibliography: 870 entries, parses
  ℹ [(bibliography)]: no reference registry configured — cites-resolve did not run
  ⚠ [piece-a-corner-removal-obligation]: no Lean declaration yet
✓ Valid — 2 issue(s)                                    exit 0, 3m33s wall
```

Why `bun install` in `qou/` could not have worked: the remark/unified family that
transitively pulls `unist-util-visit-parents@6` is declared in the **platform's**
`package.json` (`remark ^15.0.1`, `remark-directive ^4.0.0`, `remark-html ^16.0.1`,
`remark-math ^6.0.0`, `@unified-latex/unified-latex-util-parse ^1.8.4`) and nowhere
in this repo. With no `node_modules` in the clone, bun resolved straight out of its
global install cache, where it does not honour the `./do-not-use-color` conditional
subpath export.

## 🛑 CORRECTION to this bean's own next-step: the fix does NOT belong in setup-folio-assistant.sh

This bean said *"if that fixes it, the fix belongs in `scripts/setup-folio-assistant.sh`"*.
**It is already there** — lines 261-267 do exactly this `bun install`, documented at
line 32 (`FOLIO_SKIP_INSTALL`). So "add the install step" is a no-op recommendation.

What actually happened, measured rather than assumed:

| observation | value |
|---|---|
| clone `package.json` / `bun.lock` mtime | Sep 13 **08:40** (this container's setup) |
| in-repo symlink `folio-assistant -> ../folio-assistant` | Sep 13 **08:40** — the script's own artifact, so **the script ran** |
| `bun` on PATH | yes, `/root/.bun/bin/bun` 1.3.11 |
| `FOLIO_SKIP_INSTALL` | unset |
| `node_modules` | **absent until 11:55**, when I created it by hand |
| early `exit` before the install block | none (`awk` over lines 1-261: zero hits) |
| `set -e` | no — `set -uo pipefail` only, so a failing command does not abort |

So the script reached its install step with every guard satisfied and left no
`node_modules`. **Why is NOT recoverable**: the step is best-effort
(`(cd "$CLONE_ABS" && bun install) || info "bun install failed — run it manually"`),
it is not a SessionStart hook, and no log survives — `/tmp` holds no `*folio*` log.
Two candidates remain and this measurement does not separate them: the install ran
and failed at 08:40 (network/proxy at provisioning time), or the clone was
materialised by container provisioning through some path that skipped the step.

## The durable defect, which is independent of which candidate is true

**A best-effort install whose failure is invisible three hours later.** The
consequence is not a missing package — it is that the failure resurfaces as

```
error: Cannot find module 'unist-util-visit-parents/do-not-use-color'
  from '/root/.bun/install/cache/unist-util-visit-parents@6.0.2@@@1/lib/index.js'
```

which points at bun's global cache and names neither the platform clone nor setup.
An agent reading it reasonably concludes the *gate* is broken and runs
`bun install` in `qou/` — which is what happened here, and which cannot work.

Candidate fix (**NOT applied — needs owner sign-off**): have the script *verify*
`node_modules` after the attempt and fail loudly, or drop a marker file the gate
can name in its error path. Under AGENTS.md §"ASK THE OWNER BEFORE CHANGING
THINGS" (2026-09-07) this is neither a precision increase nor corpus-derived, so
it waits.

## Downstream: both beans this one blocked are now checkable — and both are GREEN

See `qou-mwmn` and `qou-mln9`. Main measures **✓ Valid — 2 issue(s), 0 errors**.
