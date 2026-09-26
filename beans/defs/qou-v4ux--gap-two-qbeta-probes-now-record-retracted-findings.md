---
# qou-v4ux
title: 'GAP: two qbeta probes now record retracted findings — nucleon-crossing-count-contradiction and nl84-provenance are stale on their own terms'
status: todo
type: task
priority: normal
created_at: 2026-08-30T14:34:40Z
updated_at: 2026-08-30T14:35:02Z
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
`content/quantum-observable-universe/knots-particles-confinement/categorical-neutron-properties.md`,
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
