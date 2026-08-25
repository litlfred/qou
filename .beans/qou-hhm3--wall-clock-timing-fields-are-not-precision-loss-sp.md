---
# qou-hhm3
title: 'Wall-clock timing fields are not precision loss: split elapsed_sec out of the raw-float64 ratchet (same argument as qou-xt5l integral floats)'
status: completed
type: task
priority: normal
created_at: 2026-08-25T16:41:59Z
updated_at: 2026-08-25T19:51:32Z
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


## CLOSED 2026-08-25 — carve-out landed, with the self-test this bean asked for

`VOLATILE_TIMING_FIELDS` in `witness_raw_float64_audit.py`, reported on its own
line, never silent. Declared by NAME (eight of them), never by a `*_sec`
pattern -- the caution this bean was filed with, and it earned its keep: the
self-test now proves `half_life_sec`, `lifetime_seconds` and `tau_sec` are
STILL FLAGGED. A suffix rule would have silenced all three, and precision is
the entire point in those.

Self-test 30 -> 36 cases. The requirement this bean set -- "a self-test proving
a genuine float64 finding in the same witness still fires" -- is case
`{"elapsed_sec": 0.001, "some_measured_value": 7.7777777} -> 1`. Also covered: all four
JSON types the field actually occurs as (53 str / 34 float / 16 null / 3 int),
none of which may throw.

MEASURED against main, every headline, so the change is fully accounted:

                              main        with carve-out
  witnesses carrying f64      1288   ->   1278
  total raw float64 fields  258,324  ->  258,236   (-88)
  f64-integrator carve-out     65/3  ->     65/3   unchanged
  deprecated-f64 carve-out     97/1  ->     97/1   unchanged
  LP-dual carve-out           429/21 ->   429/21   unchanged
  integral-valued floats  224,823/836 -> 224,823/836  unchanged
  volatile-timing              --    ->    88/31   NEW
  NEW dirty / REGRESSED         0/0  ->      0/0

## Corrections to this bean's own numbers

**"24 files / 14 with floats" was the `elapsed_sec`-only measure.** With all
eight declared names the carve-out covers **31 witnesses / 88 fields**. Only
four names occur at all: `elapsed_sec` 33 occurrences in 13 files, `wall_sec`
36/7, `elapsed_seconds` 16/6, `wall_seconds` 5/5. The other four are
forward-looking and unexercised by the corpus -- said explicitly in the source
comment so eight names are not read as eight measured cases.

So BOTH earlier figures were narrow: #5763's "exactly 4 witnesses" and my "24".
Mine was closer and still not the number that matters, which is per-name.

**An accounting bug I introduced and caught here:** the first version dropped
the integral count under a timing field, so an integral-valued timer vanished
from both buckets (visible as a 90-vs-88 gap). Fixed to `integral += i`,
matching the LP-dual carve-out; the diff above shows integral-valued unchanged
at 224,823 either way.

## Why this was safe to do now, when it was not before

The ratchet was ALREADY green (NEW 0) before this change, so it cannot be the
banned "make a red green by widening" move -- and no baseline file is touched,
so it is not a `--rebaseline` either. It is a reclassification, exactly the
shape `qou-xt5l` landed. I deferred it on 2026-08-25 while the ratchet was red
for precisely this reason; #5763 draining the five is what made the moment.


## CLOSED BY MAIN, NOT BY ME — and reopened for a measured residue (2026-08-25)

A sibling landed the same carve-out first: `d9df357d69 feat(raw-float64 audit):
carve out runtime-duration fields — 42 in 19 witnesses`. I had claimed this bean
`in-progress` and implemented it in parallel anyway, without re-checking whether
anyone had picked it up in the interim. Second duplication of the day, same root
cause. **Claiming a bean is not the same as holding it.**

**Their implementation is better than mine, and not marginally.** It sources the
names from `qou_substrate.witness._EPHEMERAL_META_FIELDS` — the SAME mask the
witness-comparison path already uses — where I hand-declared a frozenset inside
the audit. Mine was a second list that would silently drift from the first; that
is the exact defect class this corpus keeps re-finding. Theirs also covers
`durationMs`, which mine missed, and carries the same guard case I set as the
requirement (a real finding in the same witness still fires).

Mine was dropped in the merge. No reconciliation needed.

## RESIDUE — this is why the two counts differ, and it is real

    main's carve-out : 42 fields / 19 witnesses
    mine             : 88 fields / 31 witnesses

The gap is **`wall_sec` and `wall_seconds`, which are NOT in
`_EPHEMERAL_META_FIELDS`**. Measured: `wall_sec` 36 occurrences in 7 files,
`wall_seconds` 5 in 5, 48 occurrences total (incl. the prefixed
`free_chi_wall_sec`).

Verified they are genuinely wall-clock, at the producer, not by name:

    whitehead_recurrence_hunt_fast.py:65      f"{time.time() - t0:.3f}"
    binding_canonical.py:296                  "wall_sec": wall
    threerow_isospin_parity_probe.py:213      round(time.time() - t0, 1)
    borromean_sublink_channel_sum_probe.py    f"{time.time() - t_start:.2f}"

Every writer is `time.time()`/`perf_counter()` differencing. They pass every
test main's own comment applies. So today they are BOTH still counted by the
ratchet AND not stripped when witnesses are compared — the second half being
the more annoying one, since it produces spurious diffs on every re-run.

**The fix belongs at the single source** (`_EPHEMERAL_META_FIELDS`), never as a
second list in the audit — that is precisely what makes main's version the
better one. Note it is NOT a two-line change: `tools/qou-substrate/tests/
test_ephemeral_mask_sync.py` guards this set, and AGENTS.md records that this
very test was once green only because the generated `qou-mass/_internal` mirror
was stale. So: add the names, re-run `sync-qou-mass-vendor.py`, and confirm the
sync test is green for the right reason.

Also worth a look while there: `free_chi_wall_sec` is a PREFIXED variant, which
a name-set match cannot catch. Whether the mask should match by suffix is a real
design question and the answer is probably no — a suffix rule is what this bean
argued against for `*_sec` in the first place.

NOT started here deliberately: it is a third scope item on a PR that already
carries two, and I have collided twice today by starting work without
re-checking. Left as a clean pickup with the measurement done.


## RETRACTION 2026-08-25 — my prescription above is WRONG, and the axis has an owner

The section above says the `wall_sec` fix "belongs at the single source
(`_EPHEMERAL_META_FIELDS`)". **That would not work.** Measured on main
(`ac458da7a0`):

    _EPHEMERAL_META_FIELDS  : 9 names
       commitSha, computedAt, durationMs, durationSeconds, duration_sec,
       elapsed_sec, elapsed_seconds, environment, scriptCommitSha

    what the audit CARVES   : 5 names
       durationMs, durationSeconds, duration_sec, elapsed_sec, elapsed_seconds

The audit does not consume the mask whole. `_ephemeral_timing_fields()` filters
it:

    frozenset(n for n in _M if "dur" in n.lower() or "elapsed" in n.lower())

`wall_sec` contains neither substring, so adding it to the mask leaves the
ratchet counting it exactly as before. It would improve witness-comparison
stripping — a real but different benefit — and do nothing for the gate. I told
the owner "the fix belongs at the mask" and that was a code-read I did not
finish.

## The axis is owned, and measured far better than mine

Bean `qou-ywee` / PR #5783 (`raw-float64 ratchet counts wall-clock elapsed_sec`)
covers this: **453 fields across 97 witnesses**, 40 of them dirty ONLY because
of timings. My 48-occurrence `wall_sec` finding is a slice of a family they have
already enumerated: `walltime_sec` 99, `rust_secs` 46, `time_sec` 42,
`compute_time_sec` 38, `wall_sec` 36, `solve_time_s` 33 — ~495 timing-shaped
fields under names the mask does not declare.

**And they explicitly warn against the obvious next step**, with a measurement I
did not have. Broadening the filter to `/time|wall|_sec|elapsed|dur/` matches 84
distinct names, 19 of which are physics or ratios, and would remove **361 REAL
float64 fields** from the gate. The trap they name:

    `_times_` is MULTIPLICATION. `y_times_chi` is the Frobenius pairing
    y_lambda . chi_lambda -- 177 fields, the framework's central object.

A `/time/` substring test excuses every one of them, silently, and the gate
stays green while doing it. They wrote that regex first and the corpus caught
it; those names are now self-test cases that must still count.

So the remaining work is neither "add two names to the mask" nor "broaden the
filter". It is a per-name adjudication of ~495 fields against a corpus where
timing-shaped names and physics names overlap, and it belongs to `qou-ywee`.

## What this bean keeps

Nothing actionable. The carve-out landed via `d9df357d69`; the residue is
`qou-ywee`'s. Closing rather than leaving a wrong prescription live — a stale
instruction in a bean is exactly the failure mode this corpus keeps re-finding,
and this one was mine.
