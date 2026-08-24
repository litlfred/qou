---
# qou-5t68
title: 'GAP: borromean-binding-recompute.witness.json is 17-23% stale — and the assertion that should catch it passes because both sides are'
status: todo
type: task
priority: normal
created_at: 2026-08-24T10:01:14Z
updated_at: 2026-08-24T10:01:15Z
---

Found while converting `probe_9b_perlambda_brane_tower.py` for the convention-C
excision (`qou-cds1`, PR #5622). The conversion broke an assertion, and chasing
why produced this instead.

## The measurement

`computations/borromean_binding_recompute.py` re-run with **NO source change**:

    isotopes[0].B_can0            committed 2.0898131  ->  fresh 1.6166217   (-23%)
    isotopes[0].B_tower           committed 2.4802963  ->  fresh 2.0630769   (-17%)
    isotopes[0].delta_K_residual  committed 0.8968981  ->  fresh 1.0782792
    isotopes[1].B_can0            committed 3.5638785  ->  fresh 3.1372256
    isotopes[1].B_tower           committed 4.9190261  ->  fresh 4.7419664

26 fields total. The producer is convention **D** and says so explicitly
(`borromean_binding_recompute.py:111` `z = q**3/(q**2+1)`; docstring at :123-124
"y_(1^3) = 0; z = q^3/(q^2+1) ... NOT convention C"). The COMMITTED witness is a
stale convention-C-era artifact.

## Why nothing caught it

`probe_9b_perlambda_brane_tower.py` carries an assertion named exactly for this:

    scalar_baseline_matches_committed_witness
    computed=max_base_dev, expected=0.0, tolerance=1e-6
    source="scalar Jones tower vs borromean-binding-recompute.witness.json
            per-isotope B_tower (q-string precision difference only)"

It PASSES, at **computed = 0.0 exactly**. It passes because probe_9b was ALSO
convention C, so a C-frame scalar tower was being compared against a C-era
committed witness. Two stale things agreeing is not a check.

Converting probe_9b to D flips it: computed 0.0 -> 0.17767, passed True ->
False. The assertion only became informative once one side moved.

## Ordering consequence for the excision

`probe_9b` CANNOT be converted before its upstream is refreshed. The correct
order is:

  1. refresh `borromean-binding-recompute.witness.json` (producer re-run, no
     source change) -- a 17-23% value movement in the BINDING channel;
  2. then convert `probe_9b` to D;
  3. the assertion should return to ~0 against D-vs-D.

Step 1 is deliberately NOT done in the excision PR. A 17-23% movement in
committed binding numbers deserves its own review with its own attribution, not
a footnote in a convention-migration commit. It is also plausibly the binding
channel owner's call rather than mine.

## Generalisation worth checking

Any assertion of the form "my value matches a committed upstream witness" is
only as good as that witness's freshness. If both sides drifted together the
assertion reports success. This one sat at EXACTLY 0.0, which reads as strong
agreement and was actually two stale artifacts matching. Worth sweeping for
other `*_matches_committed_*` assertions on the same pattern.
