---
# qou-y4gi
title: canonical_trm_reference validates the pin but not the intra-nucleon ordering
status: todo
type: task
created_at: 2026-09-13T11:12:50Z
updated_at: 2026-09-13T11:12:50Z
---


## The gap

`computations/canonical_trm_reference.py` exists so that callers stop
hardcoding |tr_M| — its own docstring calls `tr_m_proton()` "the value 15 files
used to hardcode". It selects its witness by **recorded q₀**, and refuses
rather than falling back:

> "Raises rather than falling back to the other pin: a 78 ppb cross-layer error
> that reads as a successful load is worse than a stack trace."

That guard is good and it works. **It is also the only guard.** The module has
no notion of the intra-nucleon ordering, so a witness at the right pin in the
wrong ordering frame loads silently and cleanly.

## This is not hypothetical — it happened, and it took three commits to notice

Measured 2026-09-13 under `qou-4383`: the module was returning the **grouped**
values for all five atoms, five weeks after the 2026-09-05 ruling
(`qou-hu1f`) made the borromean word canonical. Its input,
`atomic-tr-m-mpfr-50dps-proton.witness.json`, was dated 2026-08-19.

I recommended this module in three separate commits as the durable alternative
to a hardcoded constant, on the stated grounds that it "cannot silently serve
the wrong frame" — while it was doing exactly that. Regenerating the input
fixed the values (`52b154af6e1`); it did not fix the gap.

**Why it went unseen** is worth keeping: the CANONICAL-pin witness was the stale
one (proton, 2026-08-19) and the RETIRED-pin witness was the fresh one (muon,
2026-09-07). Every check that asks "is the recent artifact canonical?" passes,
and the file that matters is the other one.

## The fix

Record the ordering in the witness and assert it on load. Concretely:

1. Have `atomic_tr_m_mpfr_50dps.py` stamp `intra_ordering_frame: "borromean"`
   (the same field `path_b_defect_binding_probe` now carries — see `qou-4383`).
2. Have `_rows_for_pin()` require it, and raise on absent-or-wrong with the
   same voice the pin guard already uses. An undeclared frame must NOT default
   to canonical: every pre-ruling witness is undeclared, so defaulting would
   wave through precisely the population this exists to catch.
3. Backfill the field on the witnesses in `_WITNESSES` only. A corpus-wide
   backfill is a different, larger job (`qou-4383` counts 48 candidate
   witnesses and 55 undeclared `y_lambda` columns).

## Why it is worth doing rather than relying on regeneration

Regenerating a stale witness fixes today's values. It does not stop the next
ruling from doing the same thing again — and the evidence that it recurs is
already in the corpus: `derivation_chain.TR_M_AT_Q0` was corrected from the
convention-C value and went stale again within five days, and
`path_b_defect_binding_probe` records the identical two-step in its own
comments. A loader that checks the frame turns a silent wrong answer into a
stack trace, which is the trade the pin guard already made and justified.

## Related

`qou-4383` (where it surfaced), `qou-72f8` (the `qou_mass` copy of this module
cannot find its witness at all), `qou-hu1f` (the ruling).
