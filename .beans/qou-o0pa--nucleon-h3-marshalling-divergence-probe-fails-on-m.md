---
# qou-o0pa
title: 'nucleon_h3_marshalling_divergence_probe fails on main: the grouped pin is inverted AND its two arms now confound d-dropping with ordering'
status: todo
type: bug
priority: normal
created_at: 2026-09-07T08:35:25Z
updated_at: 2026-09-07T08:35:58Z
---

Found while adding a deliberate/actionable split to
`audits/self_built_braid_word_audit.py`. I attempted the fix, it half-worked,
and the half that failed is the interesting part — so this is reported, not
repaired.

## 1. The pin is inverted (certain)

`nucleon_h3_marshalling_divergence_probe.py` pins its marshalled arm with
`intra_order="grouped"` (added 2026-09-06, bean `qou-y2o7`), reasoning that the
borromean default "would swing `marshalled` to 0.629/0.475 against a
1.146/0.988 target".

**That target no longer exists.** `habiro/habiro-coefficients-atomic.witness.json`
was regenerated to the canonical ordering in **`a4909014a5`** — the SAME
option-B commit the pin was reacting to. Measured against the live target:

    p  grouped    1.14575969245730087    rel 0.821
    p  borromean  0.629328402202921918   rel 6.37e-51
    n  grouped    0.987743688115809572   rel 1.08
    n  borromean  0.475133517155682213   rel 2.39e-50

So the pin makes the probe compare GROUPED against a CANONICAL target, and it
**fails its own assertions on `main`** ("3 assertions, FAILURES"). Reproduced
with `origin/main`'s own copy of the probe — this is not branch-local.

## 2. Removing the pin is NOT sufficient — the arms are confounded

I removed it. The marshalled arm then matches to **1e-51**, and the probe
**still fails**, because the *other* arm now diverges:

    d-preserving  1.14575969245730087   rel vs habiro = 0.821

The d-preserving arm traces `chain`, built at line 140 as
`[(c,d,0) for ... g0] + [(c,d,1) for ... g1]` — GROUPED — through the
monotone-only `T.chi_all_lambda`. So after unpinning, one arm is canonical and
the other grouped.

**That is worse than it looks.** The probe's subject is whether dropping `d`
changes the trace, which requires both arms to share a word and differ only in
`d`. Grouped-vs-borromean across the two arms confounds `d`-dropping with
ordering, so neither the pinned nor the unpinned state measures what the probe
claims to.

A real fix rebuilds `chain` in borromean order so both arms share it — a
substantive change to what the probe computes, on a sibling's regression guard,
which is why I reverted rather than shipping it.

## A wrong claim I nearly shipped

My unpinning commit carried a comment saying `chain` is "unrelated to the intra
ORDER". That is false — the chain IS that arm's ordering, and it is exactly why
the probe still failed. Caught by running it rather than by reading the diff.

## Detector status

`self_built_braid_word_audit` reports this site **ACTIONABLE 1**, which is
correct: it is an undeclared grouped word whose guard is broken, not a
deliberate historical choice. I deliberately did NOT mark it deliberate — the
marker would have silenced a real defect.
