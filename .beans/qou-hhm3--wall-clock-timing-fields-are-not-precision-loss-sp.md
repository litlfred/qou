---
# qou-hhm3
title: 'Wall-clock timing fields are not precision loss: split elapsed_sec out of the raw-float64 ratchet (same argument as qou-xt5l integral floats)'
status: todo
type: task
priority: normal
created_at: 2026-08-25T16:41:59Z
updated_at: 2026-08-25T18:03:16Z
---

## Found 2026-08-25 draining the 5 NEW raw-float64 witnesses on main

`computations/deltalambda/sigma1cubed-seifert-surface-term.witness.json` is one
of the five. It has **exactly one** raw float64 in the whole file:

    /elapsed_sec = 0.001            <- round(time.perf_counter() - t0, 3)

The producer already computes in mpf throughout (`set_compute_dps()`, mpf
constants). Every mathematical quantity in that witness is clean. The only
finding is a wall-clock timer.

## Why this is an over-flag, not a defect

`witness_raw_float64_audit` asks one question: **did a value lose digits a double
cannot hold?** A wall-clock duration answers **no** -- there is no higher-precision
source it was truncated from. `time.perf_counter()` returns a float; there is no
mpf original.

This is the identical argument `qou-xt5l` (completed) made for integral floats,
and it was accepted there: "an integral float answers no, because integers are
exact in binary64. It counted them anyway, so a JSON serialisation detail was
indistinguishable from a dropped digit."

AGENTS.md independently classes these fields as volatile and says to MASK them
when comparing witnesses -- "`timestamp`, `elapsed_seconds`, `measured_at`,
`start_time_monotonic` ... all change every run" -- so the corpus already treats
them as non-data in the one place it reasons about them.

## Scope

24 witnesses under `computations/` carry `elapsed_sec`. It is in NO schema
(`qou-probe/v1` does not declare it); it is an ad-hoc convention.

## Proposed fix (NOT applied here -- it changes a BLOCKING gate)

Follow the qou-xt5l shape: a separate carve-out reported on its own line, not a
silent skip, so the count stays visible:

    volatile-timing carve-out : N field(s) in M witness(es)
      [NOT a precision finding -- no mpf source; see qou-hhm3]

Two cautions taken from qou-xt5l's own writeup:

1. **Declare, do not infer.** qou-xt5l needed `witness-integer-fields.json`
   because inferring integer intent from values would have been wrong ~99% of the
   time. Timing fields are a much smaller and more clearly-named set
   (`elapsed_sec`, `elapsed_seconds`, `wall_sec`, `runtime_sec`), but the name
   list should still be explicit in the audit rather than pattern-matched on
   `*_sec`, which would catch physical quantities measured in seconds
   (a lifetime, a decay time) where precision very much does matter.
2. **A carve-out is a form of widening.** AGENTS.md: "DO NOT MAKE A RED RUN GREEN
   BY WIDENING A BASELINE." This is not a baseline addition and not a
   `--rebaseline`, but it does make the gate flag less, so it needs its own PR
   with a self-test asserting a genuine finding in the same witness still fires.

## Deliberately NOT done: deleting the field

The tempting local fix is to drop `elapsed_sec` from the producer, which would
clear the finding in one line. Rejected: that treats a measurement artifact as a
defect and deletes diagnostic data to make a gate green. The field is not wrong;
the audit's classification of it is. Fixing it producer-side would also leave the
other 23 inconsistent.

## Does not unblock the gate on its own

The other remaining NEW witness, `deuteron-interface-handle-curvature` (42
fields), is a REAL float64 finding blocked on bean `qou-8xb1`
(`hecke_characters.build_seminormal_matrices` is f64-bound at the input). So the
raw-float64 ratchet stays red on main until qou-8xb1 lands, whatever happens
here.


## UPDATE 2026-08-25 — #5763 fixed the instance and handed this class fix over, with the scope understated 3.5x

#5763 drained `sigma1cubed` by serializing `elapsed_sec` as a string, and its argument
answers my objection to touching it: the field is in qou-substrate's
`_EPHEMERAL_META_FIELDS`, which strips **by name**, so a str-for-float swap is inert to the
mask and no diagnostic value is lost. That is a better route than either of the two I
weighed, and the instance is closed.

It explicitly leaves the CLASS fix here:

  > "The class fix -- teaching the audit to skip those names -- is left for you: exactly 4
  >  witnesses corpus-wide carry `elapsed_sec` and all 4 are raw floats, but widening a gate
  >  to turn a red green is the move AGENTS.md bans, so it isn't mine to take."

**The "exactly 4" is wrong, and the real scope matters for testing the carve-out.** Measured
on this tree (main + 3 probe ports, none touching `elapsed_sec`):

    distinct witness files carrying elapsed_sec at all      24
      ... where SOME elapsed_sec value is a float           14   (3 of them under _deprecated/ => 11 live)
      ... where ALL elapsed_sec values are floats           13

    occurrences by JSON type (nesting counted, 106 total):
      str 53   float 34   null 16   int 3

So it is 24 files / 14-with-floats, not 4 -- and the field already appears as **four
different JSON types**, including 16 nulls. Anyone implementing the skip against a
believed-4 sample would not exercise the null or int cases at all.

The 14 with float values:

    _deprecated/atom-sdp-gluon-search              a_operator/A-operator-extract-general
    _deprecated/habiro-coefficients-atomic-fast    atom-nf-symbolic-D
    _deprecated/validate-isotope-nf-stability      atomic-tr-m-helium4
    delta-lambda-q-sweep-2row                      deltalambda/he4-binding-k-stage2
    deltalambda/he4-stage2-ranking-seminormal-xcheck
    deltalambda/sigma1cubed-seifert-surface-term   optimised-magic-verifier
    option-e-probe1-derive-1plusq-over-2           per-irrep-pole-atom-crystal
    tr-m-jones-markov-cross-check

I have not established where "4" came from; possibly the subset that is BOTH float AND
currently on the ratchet's dirty list, which is a different question from how many the
carve-out must handle. Re-measure before implementing rather than taking either number on
trust -- including mine.

**The AGENTS.md concern #5763 raises is right and unchanged:** a carve-out makes a blocking
gate flag less, so it needs its own PR with a self-test proving a genuine float64 finding in
the same witness still fires. Note this is NOT the `--rebaseline`/baseline-widening move the
directive bans (no baseline file is touched); it is a reclassification, the same shape
`qou-xt5l` already landed for integral floats. But it deserves the same scrutiny.
