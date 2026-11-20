---
# qou-pgr1
title: Precision-gate residue — the 20 dps sites are all safe; qou-wlaf's blind spot is 72% closable
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-25T18:40:00Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-9nnz
---

Follow-on to `qou-j6gb` (PR #5763), which closed both trunk reds and named this
residue but did not work it.

## The 20 position-risky import-time dps sites are ALL SAFE — none needs an edit

`mpf_import_time_dps_audit` reports 20 sites / 11 files, 0 proven-lossy, gate
green. `qou-j6gb` recorded them as "baselined backlog needing per-site
judgement". Judged, all 20:

* **15** — a dps-raise precedes them at module scope, frequently as an IMPORT
  SIDE EFFECT (`q_parameter` sets `mp.dps = max(dps, 50)` at import; likewise
  `codata_constants`). Safe, but *implicitly* — an import reorder would break
  them silently. This is the "mirror hazard" `_precision.py` documents.
* **5** — inside **lambda / def bodies** (`one_loop_cusp…` x3, `q_parameter`
  L210 and L215). These do not execute at module scope at all; they run when
  called. The audit walks `ast.walk` over module statements and cannot tell a
  deferred body from an immediate one.
* **`gram_matrix_seminormal_n:231`** — no raise precedes it, and it is still
  harmless: measured, `float(mp.mpf(s))` is **bit-identical** at dps 15 and 50,
  and the value is `float()`-ed immediately regardless.
* **`borromean_binding_recompute:172` x3** — see below.

### The borromean site, and why the method matters more than the verdict

I got this one wrong twice.

**First error.** A regex triage reported "SAFE — dps raised at L107". L107 is
`mp.mp.dps = dps` *inside `def _params()`*, not at module scope. Matching a
line inside a function body and calling it a module-scope raise is not evidence
of anything; that verdict was worthless and I had already written it down.

**Then the opposite error was available.** Re-measured, `E0_MeV` differs by
**4 ulps** between dps 15 and 50 (`4.185981357642159` vs `4.18598135764216`),
and `_params` does NOT appear in the `__main__` block's call list. Both facts
point at a real defect, and stopping there would have produced a confident
wrong bug report.

**What settled it was running the thing.** `recompute()` calls `_params()`
internally, and `recompute` is invoked before L172, so `mp.dps` is 50 by the
time L172 executes — confirmed by instrumenting an actual run. Safe by CALL
CHAIN.

That is the general finding, and it is worth more than the 20 verdicts: these
sites are not *unresolved*, they are **not statically resolvable**. A module-
scope AST walk cannot see a raise that happens three frames deep inside a
function the `__main__` block calls. So the honest disposition is to leave all
20 baselined with this rationale recorded, NOT to edit 11 files and not to
re-litigate them next pass.

## qou-wlaf: the blind spot #5775 named is 72% closable

PR #5775 measured the dependency-staleness class (106-witness upper bound; of
those, exactly one — gram-norm itself — is settleable from stored data, the
other 105 needing producer re-runs). **That measurement is theirs and is not
re-done here.** What they flagged as their own gap: witnesses recording no
`scriptFile` are invisible to the method, because there is nothing to walk an
import cone from.

Measured, repo-wide, in
[`witness_provenance_attribution_audit.py`](../computations/witness_provenance_attribution_audit.py):

    witnesses scanned            2,966
      record a producer          2,610
      record NONE (blind spot)     356
        VERIFIED                   256   <- producer source names the witness
        stem-only (a guess)          9
        no producer stem at all     91
      => invisible set  356 -> 100

**Verification is the whole contribution.** A stem match alone is a guess;
requiring the producer's own source to name the witness file turns it into
evidence, and the two buckets are reported separately so the reader can see how
much is which. 256 witnesses become eligible for the cone walk that decides
staleness.

**Attribution is NOT staleness.** It makes a witness eligible for the walk;
it says nothing about whether any number moved. Do not quote 256 as a count of
stale witnesses.

### My counts differ from #5775's, and theirs are probably the older method

They report 3088 witnesses / 490 without provenance; I get 2966 / 356. The gap
is method, not disagreement: their post-mortem says the first pass "read a
nested `witness.scriptFile` while provenance in these files is top-level". This
audit reads **both** shapes and three key names, so it finds provenance in
witnesses that would otherwise land in `missing` — which is exactly why my
`missing` is smaller. Their fix may already have closed part of it. Not
asserting their number is wrong; stating which method produced mine.

Per their caution ("any re-run should self-test before its count is trusted"),
the script **refuses to report** until it has confirmed on the real corpus that
it reads provenance in both shapes, that the corpus does not read as empty, and
that a known-attributable witness verifies. A false zero here reads exactly
like a clean tree.


## Correction from `qou-82ur`: my item 3 is a treadmill step, not a fix

`qou-82ur` landed on main while this branch was open. A sibling independently
found the same three stale audit witnesses, refreshed `q0-anchor-consistency`
in `1d201bd24a`, and reached the conclusion I had missed:

> this artifact is **stale the moment any producer emits a witness**. It was 9
> days stale when the bean opened, and it went stale again **in under 20
> minutes** here. So "regenerate the audit witness" is a **treadmill, not a
> fix**, and the count in a committed audit witness should never be quoted
> without re-running.

That is right and it applies to item 3 as I wrote it. Refreshing the three
brings the committed state current for the merged tree with a correct
environment — worth doing once, and the merge required it anyway — but it is
NOT a fix and the counts in it must not be quoted without re-running.

**The durable item is the absent enforcement**: nothing regenerates these on a
push, because CI is `workflow_dispatch`-only. Same missing-enforcement
conclusion `qou-mnrd` reached from the other side. Out of scope here; recorded
so the next agent does not mistake another refresh for progress.

**It applies to my own item-4 numbers too.** The attribution audit's
356/256 became 357/257 across a single main merge. Re-run it; do not cite it.

## Duplication, visible rather than silent

`qou-ntz0` on main records a sibling drain of the same five float64 witnesses
that `qou-j6gb` / PR #5763 drained. Their note says the merge correctly took
#5763's version, because it evaluates `F_q(1)` at the exact classical Young
form rather than an `eps=1e-30` offset, verified the ninths to 22 digits, and
separated the pin question. Closed by them; no action. Recorded because two
agents drained the same mechanical item concurrently, which the one-owner rule
exists to prevent.

## Merge, 2026-08-25

Merged `origin/main` at `da5a308d75`. Two conflicts, both in GENERATED audit
witnesses (`q0-anchor-consistency-audit`, `witness-raw-float64-audit`) —
resolved by regenerating from the merged tree with the repo's own tooling,
never hand-merged.

One trap in that: staging main's copy of a generated file does NOT get it
regenerated by the subsequent gate run, so the committed carve-out silently
read `ephemeral: None` with main's stale counts. Caught by checking the field
rather than trusting the gate's exit code, and fixed by running the producing
audit directly. `precision-gates.sh` exits 0 on the merged tree.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-08-25 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8384, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.
