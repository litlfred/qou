---
# qou-306p
title: Four QA checkers are unconditional n/a stubs — 8949 sidecar entries with zero information, two of them named proof-build-green / proof-no-axiom-growth; and they dilute the published M5 by 30-47 pp
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-27T10:33:43Z
updated_at: 2026-10-04T15:19:21Z
parent: qou-5vkl
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

## Owner decision 2026-09-27: **option 2** — M5 publishes no number. Landed.

Asked with four options (drop the stub from `M5_CRITS`, report `insufficient`,
document the dilution, or no-op); the owner chose **2**, which was also the
recommendation. Implemented in `computations/ab_methodology_metrics.py`.

### What changed

A **stub registry**, `STUB_CRITERIA`, naming each criterion whose platform
checker is an unconditional `n/a` — currently `proof-no-axiom-growth` and
`proof-build-green`, each with its checker, file and line. `M5_STUBS` is the
intersection with `M5_CRITS`, and when it is non-empty:

- every cohort's `M5_pass_pct` is `null` rather than a diluted rate;
- a new `M5_n` publishes the population, so a reader can see there **is** data
  and that it is deliberately not aggregated (this parallels `M1_n` / `M2_n`,
  which M5 previously lacked);
- `data.insufficient.M5` records `reported: null`, the reason, the stub's
  identity, what would unblock it, and both beans;
- `caveats[0]` names it, so a reader who never opens `insufficient` still sees it;
- the console prints `insuf` in the M5 column.

**The registry is deliberately wider than M5.** `proof-build-green` is in it
although no metric currently aggregates that criterion — so the next metric that
does gets this treatment without anyone remembering to add it.

**`first_verdicts_by_criterion` carries COUNTS, never rates** (`proof-no-bare-sorries`
1209, `proof-no-axiom-growth` 752). A per-criterion pass rate there would be M5
republished under another name, which is the thing this record exists to prevent.

### Why not simply drop the stub from `M5_CRITS` (option 1)

That silently redefines M5 as a one-criterion metric while its own scope doc
(`2026-06-11-ab-methodology-metrics-scope.md:39`) defines it as the pair — and
the number would jump 30-47 pp with nothing marking the change. Recorded as a
comment at the registry so the next agent does not "simplify" it back.

### 🛑 The `insufficient` key this bean said to reuse DID NOT EXIST

The producer's own comment (line ~130) ends *"M1 and M2 are therefore NOT
COMPUTABLE from resolvable data and are reported as such rather than as a
number; see `insufficient` in the witness."* Measured: the committed witness's
`data` keys were `adoption_dates, caveats, cohort_table, criteria_counts,
n_blocks, n_first_verdicts` — **no `insufficient`**, and `caveats` did not
mention M1/M2 either. So the mechanism option 2 was framed as reusing was
itself a dangling pointer, a third instance of this session's class.

Corrected rather than propagated. The comment now says what is true: M1/M2 are
reported **where the residual sample survives**, with `M1_n` / `M2_n` carrying
that sample size — a **thin-sample caveat, which is weaker and different from
not-computable**, and the note says not to widen it without measuring. The key
exists now and covers **M5 only**.

**M1/M2 were deliberately NOT nulled.** The owner chose option 2 for M5; nulling
M1/M2 would be a second, unasked decision about two more metrics.

### Verification

**My edit changes nothing but M5 — measured, not asserted.** The pre-edit script
from `git show HEAD:` was run against today's tree and its M1/M2/M4/`n_blocks`
are **byte-identical** to the edited script's, cohort by cohort:

| cohort | blocks | M1 pass% (n) | M2 (n) | M4 | M5 before | M5 after |
|---|---:|---|---|---:|---:|---|
| 2026-06 | 145 | 40 (15) | — (0) | 1 | 52 | **insuf** |
| 2026-07 | 66 | 100 (1) | 0.85 (3) | 1 | 70 | **insuf** |
| 2026-08 | 3225 | 12.5 (16) | — (0) | 1 | 61.533 | **insuf** |
| 2026-09 | 141 | — (0) | — (0) | 1 | 68.345 | **insuf** |

Those four M5 values also reproduce my independent hand-replication of the
cohort logic exactly, which is the cross-check that the measurement in the
entry above was right.

**🛑 M1 moved against the COMMITTED witness, and that is corpus drift, not this
change.** The committed witness (produced Sep 4) had 2026-06 M1 = 75 % (n=8) and
three cohorts; today the same code gives 40 % (n=15) and four. The pre-edit
baseline run is what separates the two causes — without it this commit would
look like it moved M1 by 35 pp.

**Environment.** The witness's `environment` block records `mpmath 1.4.1`; this
container had 1.3.0, and the guard refused to let a weaker record be committed
silently. Installed 1.4.1 and re-ran, so provenance is preserved rather than
downgraded. Note `pip` reports a conflict — `sympy 1.14.0` wants `mpmath<1.4` —
which is **irrelevant to this producer**: neither it, `witness_base` nor
`_precision` imports sympy (grepped). Flagging it because the next producer run
in this container may hit it.

**`scripts/precision-gates.sh --changed`: exit 0**, no blocking red. The
producer is pure integer / `Fraction` arithmetic serialized through
`_precision.fmt` and this change adds no float path — the one new numeric
quantity, `M5_n`, is a `len()`.

**The gate run dirtied 13 sibling witnesses and NONE of the movement is mine**
— measured, because the script says to read them rather than assume: `grep -c
ab.methodology` over all four substantively-moved audits returns **0**. What
moved is other arcs' drain progress on `main` (`mpf-mixed-arithmetic` candidates
7 -> 5, `import-time-dps` findings 21 -> 20, `witness-provenance` computed
92 -> 107, `witness-value-copy` indexed literals -2). The script's own warning
is why they are not committed: this branch is **21 behind `origin/main`**, so
committing a drain-only ratchet from here walks it **backwards**. Nine were
auto-reverted by the script (ephemeral-only); the remaining four were reverted
by hand, leaving exactly the two intended files.

**No self-staleness introduced**: the producer's fresh `sha256[:12]` is
`cf11f11b7cfd` and the regenerated witness records `cf11f11b7cfd`.

### Status

Stays **todo**. What the owner chose is done; the open items are unchanged and
are not qou's:

1. **The four stub checkers** — implement or retire, upstream
   (`folio-assistant-89wq`). Until then `proof-build-green` and
   `proof-no-axiom-growth` still write `n/a` into every new sidecar.
2. **`3t8p`'s remedy** is still inert and that bean still says `todo` — correctly,
   since its criteria remain unscored; only the *route* changed.
3. The two `detangler` stubs have no qou consumer and need nothing here.

## Generalisation swept 2026-09-27 (post-merge): M5 was the ONLY diluted aggregate in the Python surface

With the M5 fix on `main` (`18e1ba553e`), the obvious follow-on question is whether
any **other** qou consumer aggregates QA criteria verdicts without filtering
`n/a` — the same defect one file over. Measured rather than assumed.

### Surface searched, and the result

Every `.py` under `computations/`, `scripts/` and `content/` that reads
`.qa.json` **and** mentions `result`/`verdict` — **17 files**. Classified by
what each does with a verdict:

| class | count | verdict |
|---|---:|---|
| aggregates a **pass rate** over criteria | **1** | `ab_methodology_metrics.py` — M5, now fixed |
| counts **failures only** | 1 | `lean-qa-progress-table.py` — **immune by construction** |
| acts **per entry**, no aggregation | 15 | not susceptible |

**Counting failures is the shape that cannot have this bug.** A stub returns
`n/a`, which is not `fail`, so it contributes nothing to a failure count — the
progress table is correct as written and needs no filter. That is worth stating
because the naive reading ("it reads verdicts, so check it") would have flagged
it.

**One consumer already handles `n/a` explicitly and correctly**:
`scripts/qa-evidence-provenance-gate.py:153` — `is_live = result not in ("n/a",
"pass")`. So the corpus was not uniformly blind to this; M5 was the outlier.

All four files carrying a single pass-comparison
(`reaudit-proof-deterministic.py`, `expire-unhashed-agent-verdicts.py`,
`qa-evidence-provenance-gate.py`, `reaudit_verdict.py`) were checked for
aggregate operations — `sum(` / `mean` / `/ len(` / `pct` / `percent` — and all
four return **zero**. They are per-entry tools, not metrics.

### 🛑 What was NOT swept, and what would separate "found none" from "there are none"

Two surfaces are untouched, and the negative above is scoped to exclude them:

1. **The TypeScript side.** 18 files under `content/pipeline/` read `.qa.json`
   or `criteria` and carry aggregate operations (`definition-clarity-audit.ts`
   62, `lean-vacuity-axiom-audit.ts` 78, `trace-convention-audit.ts` 44). **Most
   are verdict PRODUCERS, not consumers** — they count their own findings, which
   is why they mention `pass`/`n/a` at all — so a raw count of aggregate ops is
   not evidence of the defect. Separating producer from consumer needs per-file
   reading, which is a larger job than this follow-on and is not claimed here.
2. **The derived `proof-objects.json` route** — closed cheaply: `grep -rln
   proof-objects` over `computations/`, `scripts/` and `content/` returns
   **zero** consumers, so nothing aggregates through it.

So: **decisive for Python, open for TypeScript.** What would settle the TS side
is classifying each of the 18 as producer or consumer and checking the
consumers' rate arithmetic — worth doing if anyone touches that surface, not
worth a sweep on its own.

### Status

`qou-306p` stays **todo**: the owner's decision is implemented and merged, but
the four checkers are still stubs and that fix is upstream
(`folio-assistant-89wq`). This entry closes the qou-side blast-radius question
and leaves the TS surface explicitly unmeasured rather than implicitly clean.

- **Round 93 (`litlfred/qou#8421`)**: Advanced in `feat/round93-strip-kindratio-kohnokz-resolvent-affinenorm-43c1` (Commit 1 `53341df5af4d7e77e4fbee34d9b0bead3b0b6187`, Commit 2 `2f40c0d2d071ec6bb42d20002fb53171245df01c`, probe sha256 `3d8255f15bbdfc2d9c41114f8ac21a1bec3996e0b1546ef080914210757c628c`).
