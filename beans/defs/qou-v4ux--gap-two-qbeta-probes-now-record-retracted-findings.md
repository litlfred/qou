---
# qou-v4ux
title: 'GAP: two qbeta probes now record retracted findings — nucleon-crossing-count-contradiction and nl84-provenance are stale on their own terms'
status: in-progress
pr: 8277
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-30T14:34:40Z
updated_at: 2026-10-10T10:40:00Z
parent: qou-avtq
---

Surfaced while draining `qou-srvu` slice E; branch
`claude/srvu-drain-e-2026-08-30`.

Both probes are now honestly RED (their assertions were added, so `allPassed`
reflects their real exit code instead of claiming green over nothing). What is
open is whether the probes themselves should be rescoped or retired — a
judgement about the corpus, not about the drain.

## 1. `qbeta_nucleon_crossing_count_contradiction_probe.py` — 3 of 7 fail

The committed witness recorded, alongside `allPassed: true` and zero
assertions:

    THE_CONTRADICTION_neutron_derived_13_implemented_11: true
    corpus_derives_a_thirteen_crossing_neutron: true

Both are now **false**. Commit `272ea9b009` ("QOU: withdraw the nucleon LP
instability") rewrote
`folio/quantum-observable-universe/knots-particles-confinement/categorical-neutron-properties.md`,
which now reads:

> for a total of **11 crossings** (6 from B_3, 3 from quarks, 2 from gluons)
> ... The earlier "$L_+ \to L_-$, 4 gluon crossings, 13 total" was wrong on its
> own terms, independently of anything below.

So the contradiction the probe exists to report has been **resolved in the
corpus** — the corpus now says 11, matching `hecke_core`. The witness has been
carrying a retracted finding as current.

Three of its checks are corpus-greps whose PASS means *"the documented defect
is still present"*. That polarity is worth naming: once the corpus is fixed,
such a check fails on CORRECT behaviour, which is the same shape the `qou-srvu`
bean already flags for `intermediate_knot_detection`.

## 2. `qbeta_nl84_provenance_probe.py` — 1 of 4 fails

Same shape, milder. `neither_the_block_nor_what_it_uses_declares_a_producer`
now computes **false** (the block gained a producer), and its corpus-grep count
moved 50 -> 51. Its headline `N_l_eq_84_is_an_UNSOURCED_FIGURE` therefore fails.

## The decision, and why it is not the drain's to make

Three options, none of them free:

1. **Rescope each probe** so the check asserts the CURRENT corpus state
   (e.g. "the corpus and hecke_core agree at 11") rather than the defect. Turns
   a finding-recorder into a genuine regression guard. Cost: rewriting the
   probe's premise and its prose.
2. **Retire them**, recording the resolution in an audit doc. Cheapest, loses
   the guard.
3. **Leave them red.** Honest and zero-cost, but a permanently-red witness
   trains readers to ignore red.

Recommendation, marked as judgement rather than finding: **(1) for the nucleon
one**, because the 11-vs-13 question is live enough that a guard against
regression is worth having, and **(2) for nl84**, whose subject (an unsourced
figure) is simply no longer unsourced. Default if nobody acts: they stay red,
which is safe but noisy.


## 2026-10-10 — evidence re-check (verification sweep of `qou-avtq`)

**Verdict: OPEN.** Still red, and the defect detectors now fail on corrected corpus behaviour. nl84 fails 2 of 4 checks, not 1. The rescope-or-retire decision is still the owner's. Until it is made, both witnesses record retracted findings.

Evidence: Re-ran both probes (exit 1 each). `qbeta_nucleon_crossing_count_contradiction_probe.py`: 4/7, failing `corpus_derives_a_thirteen_crossing_neutron`, `THE_CONTRADICTION_…`, `the_citation_does_not_say_what_it_is_cited_for`. `qbeta_nl84_provenance_probe.py`: **2/4** (not 1/4 as the bean says), failing `neither_the_block_…declares_a_producer` and `N_l_eq_84_is_an_UNSOURCED_FIGURE`. Its corpus grep count is now 59 (witness 51). Neither probe has been rescoped or retired. Witnesses `computations/qbeta/qbeta-{nucleon-crossing-count-contradiction,nl84-provenance}.witness.json` are allPassed false, computedAt 2026-08-30.

Status: `todo` → `todo` (unchanged: edited today by another session, or held in-progress).
Checked against qou `main` at `77695711d2`. Probes were re-run only where cheap and decisive. A numeric result counts as evidence only where it reproduces and its precision exceeds the gap it decides; convention-C numbers are not evidence about convention-D claims.

## 2026-10-10 — follow-up review (re-check of the `qou-avtq` sweep flags)

**The nl84 "producer added" result is a false positive.** `has_computation()` in `qbeta_nl84_provenance_probe.py:118` is a substring test, and it matches caveat prose in `ilp-solution-count-unwrap.ts`, which has no `computation` field. So N_ℓ = 84 is **still unsourced**, and retiring nl84 on the strength of that check would be wrong.

The nucleon fix is real: the corpus now says 11 crossings.

**Open steps:** fix the detector to test for a `computation` field (code, needs owner OK); rescope-or-retire of the nucleon probe stays the owner's call.

Checked read-only against qou `main` at `aa914b606a`, mpmath 1.3.0. Full write-up: `qou-review/avtq-reopened-beans-2026-10-10.md` (project files). Status unchanged.

## Round 55 Implementation Progress (PR #8277)
- **Status:** `in-progress` (per no-unilateral-closure policy)
- **PR:** https://github.com/litlfred/qou/pull/8277 (head `8f4f568482d5a937ac700b4605cc7c48271faae8`, Commit 1 `0a62bee9d3e501101e220bcafa8c3a9fee1d0d25`)
- **Lean 4 Module & Theorems:** `QOU/AlphaEM/TauLoopWeightMarkovGramAndNucleonCrossingAudit.lean` (`nucleon_crossing_count_11_vs_retracted_13_and_nl84_decomposition`)
- **80-dps Witness:** `computations/probes/round55-tau-loop-markov-nucleon-stokes-monodromy.witness.json` (`scriptHash: 1de39a3b3d7c`, `allPassed: true`, `0` raw `float64`)
