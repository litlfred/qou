---
# qou-z8x9
title: script-QA sweeper audits ZERO qou producers — its only root is folio-assistant/computations, which holds no .py
status: todo
type: task
priority: normal
created_at: 2026-08-26T09:19:22Z
updated_at: 2026-08-26T09:19:52Z
---

Found while wiring qou-3xk6. `computations/hecke/hecke_characters.py` changed, so
its `script-qa` sidecar went hash-stale (`2acdad5c6887` -> `834fe83b2cdc`) and
the QA-is-agent-owned rule says refresh it before commit. It cannot be
refreshed: the sweeper audits nothing in this repo.

    folio-assistant/content/pipeline/script-walker.ts

    export const SCRIPT_ROOTS: ScriptRoot[] = [
      { dir: "folio-assistant/computations", exts: [".py"], language: "python" },
    ];

One root, and it is the PLATFORM's computations dir, not qou's. Measured on
this checkout: that directory EXISTS (it holds one witness JSON) and contains
**0 .py files**. qou's ~1800 producers live in `computations/`, which is not a
root at all.

STATE THE CAUSE PRECISELY, because I got it wrong first. `walkRoot` returns
early on `!existsSync(rootAbs)`, so "the root does not exist" is the obvious
diagnosis and it is WRONG here -- the root resolves fine and is simply empty of
`.py`. Same visible effect, different fix. Sending the next agent to re-point a
missing path would not help.

## Why this is worse than a stale sidecar

The sweep does not fail. It exits 0 and prints

    script-sweep: 0 script(s) audited
    findings: 0 critical, 0 major, 0 minor

which is indistinguishable from a clean sweep of everything. Same shape as the
R9 trap recorded on PR #5815: a lost assertion that still reads green. Tried
`script-sweep.ts <path>`, and `--filter hecke_characters`; all three report 0.

## Blast radius, measured

    computations/**/script-qa/   18 dirs, 1798 sidecars
      hash-fresh                  708
      HASH-STALE                 1086   <- 60 %, unrefreshable
      script_path missing           4

A stale sidecar's verdicts describe a version of the file that no longer
exists. `hecke_characters.script-qa.json` was last swept 2026-06-04 and already
records `fail` on does_not_default_to_float, variables_typed and
has_references_to_paper -- against June's file.

## The fix is NOT in this repo

`script-walker.ts` lives in `litlfred/folio-assistant` (moved there by miga).
Adding a `{ dir: "computations", exts: [".py"], language: "python" }` root is
probably all it needs, but it belongs in that repo's PR, not stapled onto a
qou branch. Worth pairing with a guard that makes a 0-target sweep LOUD rather
than green.

Do NOT hand-edit sidecars to clear the staleness. Writing verdicts no checker
produced is exactly the laundering AGENTS.md forbids.
