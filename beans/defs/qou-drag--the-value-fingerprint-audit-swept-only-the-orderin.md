---
# qou-drag
title: The value-fingerprint audit swept only the ordering axis; the colour ruling of 2026-08-15 was invisible to it
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-14T20:16:14Z
updated_at: 2026-10-04T15:25:01Z
parent: qou-5vkl
---

## The gap

`intra_ordering_value_fingerprint_audit` matches committed numbers against
fingerprints **computed live** — which is the right design, and why a re-pin
moves them rather than silently invalidating the scan. But `fingerprints()`
swept `PINS x ATOMS x (grouped, borromean)` and always took `pn_convention`'s
default, so it could see the 2026-09-05 ordering ruling and **not** the
2026-08-15 colour ruling.

Found while tracing the ⁴He pin under `qou-uujo`, which turned up a lineage of
at least five states where the audit covered two.

## What was added, and what it is NOT

`pn_convention="strict_averaged"` is a live flag on `atom_braid_word_3A`, so
the colour axis costs no transcription: 20 fingerprints -> **32**
(5 atoms x 2 pins x 2 orderings x 2 conventions, with a lone nucleon's two
conventions coinciding and folding to one entry, since it has no p-n
interface). Bucketing now treats a value as superseded on **either** axis —
before, a value in the canonical ordering but the colour-BLIND convention read
as clean — and every hit is labelled `grouped` / `colour-blind` / both.

**Convention C is deliberately out of scope and cannot be added here.** It is a
property of the TRACE, not the word: `Z_MARKOV` is a module constant at
`mass_at_3A_proper:121` with no flag, so no live fingerprint exists for it.
Covering it would mean transcribing literals, which is the one thing this
audit's design forbids. A convention-C detector needs a different mechanism and
must not be bolted on here — noted so the next person does not try.

## Measured, before and after

    fingerprints   20  ->  32
    witness files  29  ->  33
    candidates     28  ->  30
    ACTIONABLE     11  ->  11      <- unchanged
    reflections    15  ->  17
    deliberate      1  ->   3

## The result is a NEGATIVE one, and it is worth having

The colour axis found exactly **two** carriers of colour-blind values:
`colour-weighting-trace-magnitude` and `colour-weighting-across-mixed-nuclei`
— the two probes whose SUBJECT is the colour comparison, holding both frames
side by side because the gap is the measurement. The second is explicitly the
sibling of the first (`qou-fv0s`), extending it from the deuteron to T / 3He /
4He "because the linear coefficient `tr(A B)` is word-specific and does not
transfer". Both are now registered in `DELIBERATE` with that reason.

So: **no producer that owns its value carries a stray colour-blind trace.**
ACTIONABLE is unchanged at 11. The corpus is clean on this axis, which was not
knowable before — the detector could not have told a clean corpus from an
unwatched one.

The +4 files and +2 reflections are real detections the previous version could
not make; they are simply all accounted for.
