---
# qou-wdh9
title: 'GAP: the validate gate cannot RUN in a stock container — bun fails to resolve unist-util-visit-parents, so qou-mwmn and qou-mln9 are uncheckable'
status: todo
type: task
priority: normal
created_at: 2026-09-13T11:26:51Z
updated_at: 2026-09-13T11:26:51Z
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
