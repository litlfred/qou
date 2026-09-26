---
# qou-y4gi
title: canonical_trm_reference validates the pin but not the intra-nucleon ordering
status: completed
type: task
priority: normal
created_at: 2026-09-13T11:12:50Z
updated_at: 2026-09-13T11:54:47Z
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


## DONE 2026-09-13 — `0db2f5c731b`

Implemented as scoped, with one addition the scope did not name: a self-test.

### What landed

1. **The producer stamps, derived not asserted.** `atomic_tr_m_mpfr_50dps.py`
   records `intra_ordering_frame` read from `atom_braid_word_3A`'s own default
   via `inspect.signature` — it calls that function with no override, so the
   default *is* the frame it used. A literal `"borromean"` here would have been
   the same defect one level up: a constant that does not track a ruling. The
   loader derives its notion of canonical the same way.
2. **The loader refuses.** `_require_canonical_ordering` raises on a wrong
   frame and, critically, on an **absent** one.
3. **Both `_WITNESSES` regenerated** so they carry the stamp — including the
   muon-pin file, whose frame I verified rather than assumed. It was already
   canonical. `qou-mass` mirror re-synced, both files byte-identical.

### The self-test, which was not in the plan and should have been

A guard nobody has watched reject is indistinguishable from a no-op — and *this
module shipped for five weeks with a docstring promising a protection it did
not provide*. So `--self-test` now proves all three branches: canonical passes,
a wrong frame raises, an absent frame raises, and the committed witnesses still
load under it (1 must-pass, 2 must-raise, 1 live load; PASS).

### Two standing reds went green, downstream of the same stale witness

    graded-hecke-energy-probe   expected 1.14575969245730087 -> 0.62932840220292192
                                passed  false -> TRUE
    skein-proton-canonical      residual 0.4507326393606963 -> 1.6266846192e-50
                                passed  false -> TRUE

**Checked that neither hardcodes its target** before claiming this — a moving
`expected` is exactly what should make a reader suspicious. Both call
`canonical_trm_reference.tr_m_nucleon()`, so the target moved because the
*reference* moved. The skein one is the stronger evidence: an independent
atlas-vs-Layer-1 cross-check whose residual collapsed to numerical zero, i.e.
two routes that disagreed by 0.45 now agree to 50 digits. That is corroboration
of the regeneration from a direction that had nothing to do with it.

### The design decision worth keeping

**Absent must raise, and must not default to canonical.** Every pre-ruling
witness is undeclared, so a permissive default waves through exactly the
population the guard exists to catch — including the file that motivated it.
The cost is real: a stale witness now stops a caller instead of quietly
misinforming it. That is the same trade the pin guard makes and justifies two
functions down in this file, so the module is at least self-consistent about
what it is willing to break.

### Left open

- The `qou-mass` copy of this module has neither the guard nor a working data
  path — bean `qou-72f8`.
- Corpus-wide backfill of `intra_ordering_frame` is NOT done and was
  deliberately out of scope: only the two files in `_WITNESSES` are stamped.
  `qou-4383` counts 48 candidate witnesses undeclared on this axis.
- The `derivation_chain.TR_M_AT_Q0` migration is now **safe to start**, which
  was the point of doing this first: migrating twelve consumers onto a loader
  that could still serve the wrong frame would only have relocated the problem.
