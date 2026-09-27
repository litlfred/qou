---
# qou-306p
title: Four QA checkers are unconditional n/a stubs — 8949 sidecar entries with zero information, two of them named proof-build-green / proof-no-axiom-growth; and they dilute the published M5 by 30-47 pp
status: todo
type: task
created_at: 2026-09-27T10:33:43Z
updated_at: 2026-09-27T10:33:43Z
parent: qou-2z9j
---

Measured 2026-09-27 on `main`-derived branch + platform pin `37a36ce`.

## Four checkers whose entire body is `return { result: "n/a", hits: [] }`

Found by parsing every `export function check*` in
`cat-harness/content/pipeline/qa-checkers*.ts` and keeping those with exactly
one `return`, which returns `n/a`:

| criterion | checker, `qa-checkers-extended.ts` | self-documenting? |
|---|---|---|
| `detangler-no-xchapter-fwd` | `checkDetanglerNoXChapterFwd` `:1847` | yes — `// TODO … n/a until wired` |
| `detangler-archimedean-wall` | `checkDetanglerArchimedeanWall` `:1856` | yes — same |
| `proof-no-axiom-growth` | `checkProofNoAxiomGrowth` `:2783` | **no comment at all** |
| `proof-build-green` | `checkProofBuildGreen` `:2789` | **no comment at all** |

Every parameter is underscore-prefixed and unread. These are not axis-gated and
not data-starved — they cannot return anything but `n/a` at any commit, under
any config, with any artefact present.

## They carry 8949 sidecar entries and zero information

Counting **every** entry (all revisions, not just the last) across qou's
`content/**/*.qa.json`:

| criterion | entries | results | `reviewed_at` range |
|---|---:|---|---|
| `detangler-archimedean-wall` | 3579 | **100.0 % n/a** | 2026-07-13 .. 2026-09-26 |
| `detangler-no-xchapter-fwd` | 3579 | **100.0 % n/a** | 2026-07-13 .. 2026-09-26 |
| `proof-build-green` | 1037 | **100.0 % n/a** | 2026-07-13 .. 2026-09-15 |
| `proof-no-axiom-growth` | 754 | **100.0 % n/a** | 2026-07-13 .. 2026-09-15 |

Two of the four sit in the **`proof`** domain with names that read as
verification. `proof-build-green` is the one to worry about: an agent citing it,
or a reader seeing it pass-or-n/a in a sidecar, would reasonably take it as
evidence the block's Lean builds. It has never looked at a Lean file.

`proof-no-axiom-growth` is worse in kind, if not in blast radius — it is the
sidecar face of AGENTS.md §"Axiomatization is NOT a Proof", the anti-laundering
discipline, and it has never evaluated a single declaration.

**Contrast with a criterion that genuinely is artefact-driven:**
`proof-lean-compiles` reads `docs/audits/lean-compile-diagnostics.json` and
reports **131 pass / 1078 n/a** — real verdicts, from a cached artefact, in the
same domain and the same sweep.

## 🛑 This refutes bean `3t8p`'s diagnosis, and demonstrably rather than by argument

`3t8p` (`todo`, 2026-07-06) reads: *"3 CI-only Lean criteria n/a on path
(214/118/191). Need proof-objects.json+axiom-report.txt from full lake build.
Run in lean_ci.yml."* Its update then establishes that a local `lake build QOU`
fails on a `proofwidgets` JS target, and concludes the three are *"genuinely
CI-only"*.

**`proof-objects.json` is present in this repo** — 114 311 bytes, dated Sep 4 —
and `proof-build-green` is still 1037/1037 `n/a`. The artefact whose absence the
bean blames **exists and is ignored**, because the checker performs no file
access. So the remedy is inert: a CI `lake build` producing those two files
would not move one verdict.

`3t8p` also conflates two different things — its third criterion,
`proof-lean-compiles`, IS artefact-driven and does work (131 pass, above). One of
its three is real and two are stubs, and it treats all three as one cause.

## Blast radius: one live qou consumer, and it publishes a diluted number

`computations/ab_methodology_metrics.py:101`

```python
M5_CRITS = ("proof-no-bare-sorries", "proof-no-axiom-growth")
...
if r["crit"] in M5_CRITS:
    c["m5"].append(r["result"] in PASS)          # :198
```

There is no `n/a` filter — `"n/a" in PASS` is `False`, exactly as `"fail"` is.
So metric **M5** ("axiom/`sorry` growth per cohort", per
`docs/workplans/2026-06-11-ab-methodology-metrics-scope.md:39`) averages a real
criterion against one that contributes 0 % by construction.

Re-running the producer's own first-verdict + cohort logic on today's tree:

| cohort | M5 as published | `proof-no-bare-sorries` ALONE | the stub | understated by |
|---|---:|---:|---:|---:|
| 2026-06 | 52.0000 % (n=275) | **99.3056 %** (n=144) | 0 % (n=131) | **47.3 pp** |
| 2026-07 | 70.0000 % (n=60) | **100 %** (n=42) | 0 % (n=18) | **30.0 pp** |
| 2026-08 | 61.5333 % (n=1487) | **98.5991 %** (n=928) | 0 % (n=559) | **37.1 pp** |
| 2026-09 | 68.3453 % (n=139) | **100 %** (n=95) | 0 % (n=44) | **31.7 pp** |

**The cohort TREND is the artefact, not just the level.** Published M5 runs
52 → 70 → 61.5 → 68.3, which reads as noisy improvement; that series tracks the
stub's share of each denominator (47.6 %, 30.0 %, 37.6 %, 31.7 %) almost
exactly. The real series is 99.3 → 100 → 98.6 → 100 — flat and at ceiling. Any
reading of M5 as a methodology signal is reading the stub's coverage.

Fresh figures, so they differ slightly from the committed
`ab-methodology-metrics.witness.json` (produced Sep 4); the 0 % column is 0 % at
any commit, so the conclusion does not depend on which tree is measured.

## What was NOT done, and the decision that is owed

Nothing changed. The M5 fix has a genuine choice in it — exclude the stub from
`M5_CRITS`, or report M5 as `insufficient` the way the same producer already
reports M1/M2, or keep it and document the dilution — and choosing among those
decides what the metric means. §🟥 ASK THE OWNER puts that with the owner;
regenerating a witness in someone else's arc is named as not exempt. Measured,
reported, waiting.

The upstream half (implement or retire the four checkers) is a
`folio-assistant` change, not a qou one.

## Why this is the same failure class as this milestone's item 1

`qou-2z9j` item 1 says of the clobbering gate: *"until fixed, every other count
is untrustworthy."* This is that one level up — not a count that is wrong, but a
criterion that cannot count, reporting `n/a` 8949 times in a way indistinguishable
from a checker that ran and correctly declined. The 2274-vs-1303 split on
`detangler-archimedean-wall` is the tell: 2274 carry the harness's honest note
*"block has no .lean sibling"*, and **1303 carry no note at all** — blocks that
DO have a `.lean` and get `n/a` because nothing looked.
