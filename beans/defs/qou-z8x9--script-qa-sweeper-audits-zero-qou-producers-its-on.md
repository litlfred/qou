---
# qou-z8x9
title: script-QA sweeper audits ZERO qou producers — its only root is folio-assistant/computations, which holds no .py
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-26T09:19:22Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-5vkl
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


## FIXED 2026-08-26 — litlfred/folio-assistant#136

0 -> 3814 scripts audited on qou, and 3814 is exactly
`find computations -name '*.py' | wc -l`.

## MY ROOT CAUSE ABOVE WAS WRONG — TWICE, IN OPPOSITE DIRECTIONS

Read this before the section above, because that section is the error.

I first said "the root does not exist". I then RETRACTED that and wrote "it
resolves, it is empty of .py", and told the next agent that re-pointing a
missing path would not help. Measured at runtime, the FIRST version was
closer and the retraction was the mistake:

    __filename        : /home/user/folio-assistant/content/pipeline/script-sweep.ts
    REPO_ROOT         : /home/user/folio-assistant
    joined SCRIPT_ROOT: /home/user/folio-assistant/folio-assistant/computations
    existsSync        : false                              <-- DOUBLED path

I had checked `qou/folio-assistant/computations` (= /home/user/folio-assistant
/computations, exists, 0 .py) -- NOT the path the code actually builds. Same
visible symptom, different mechanism, and I asserted the wrong one while
writing a warning about asserting the wrong one.

The lesson holds and I failed it: `existsSync` on a path YOU construct is not
evidence about the path the CODE constructs. Print the joined path from inside
the process. That took one 6-line probe and settled it.

## The actual defect

ONE CONSTANT DOING TWO JOBS. `REPO_ROOT` was the PLATFORM root, while
SCRIPT_ROOTS entries were written CONTENT-relative. Both roots are real and
needed: criterion sources are platform-relative (`source_file`), audited
scripts are content-relative (`script_path`). Split into PLATFORM_ROOT and
CONTENT_ROOT, with CONTENT_ROOT from the EXISTING `findContentRepoRoot()`
helper -- whose docstring already names this class, "the caller reported a
clean run over nothing". The walker was never migrated onto it.

## The durable half

A zero-target sweep now prints both roots, an exists/MISSING verdict per root,
and exits 1. That is what let this hide: auditing nothing and finding nothing
printed the same thing. A `--filter` matching nothing is distinguished and is
not called a misconfiguration.

## Still open, and NOT this bean

The newly-visible backlog -- 106 critical / 2571 major / 8829 minor -- is
content-repo work. Nothing was written (every run used --dry-run). 568 of 3814
are under `_deprecated/` and the top-15 output cap means the full severity
split is UNMEASURED; do not quote a breakdown off that sample.

- **Round 96 PR (`litlfred/qou#8510`)**: Formalized `ScriptSweeperRootDiscrepancyLedger`, `canonicalScriptSweeperRootDiscrepancyLedger`, `script_sweeper_two_square_composition`, and `round_ninety_six_joint_certificate` in `QOU.Foundations.AnchorRefillArrivalPartitionUnifiedIterativeTableOrphanAuditEnvironmentVersionCensusNoncommutativeTacticSiteAuditScriptSweeperRootDiscrepancy` with 80-dps witness (`HEAD = 9861bd624187df98849a08e324f09311a00ff969`).

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8510, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.
