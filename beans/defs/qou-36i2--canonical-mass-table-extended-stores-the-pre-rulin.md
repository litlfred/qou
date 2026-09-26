---
# qou-36i2
title: canonical-mass-table-extended stores the PRE-RULING grouped word in braid_word_canonical, and qou-mass prefers it BY DESIGN
status: todo
type: bug
priority: normal
created_at: 2026-09-07T06:18:30Z
updated_at: 2026-09-14T19:53:35Z
---

Found while draining `qou-wpp2` (the vendor mirror ratchet). The mirror drain
was correct and landed, and it does NOT make the shipped package canonical.
This is why.

## Measured

`computations/canonical-mass-table-extended.witness.json`, `computedAt`
**2026-08-28T18:31:52Z** — a week BEFORE the 2026-09-05 ordering ruling
(`qou-hu1f`) — stores `braid_word_canonical` for all **9 rows** in the
**grouped** ordering:

    Z=1 N=0  len=11  monotone=True  gens=[0,0,0,0,0,0,0,1,1,1,1]
    Z=0 N=1  len=11  monotone=True  gens=[0,0,0,0,0,0,0,1,1,1,1]
    Z=1 N=1  len=23  monotone=True  gens=[0,0,0,0,0,0,0,1,1,1,1,2]
    Z=1 N=2  len=35  monotone=True  gens=[0,0,0,0,0,0,0,1,1,1,1,2]

A monotone generator sequence IS the grouped word; the ruling's word is
non-monotone by construction. So the field named `braid_word_canonical` does
not hold the canonical word.

## Why it decides the answer, rather than merely being stale

`qou_mass.api.canonical_braid` and `compute_tr_M` BOTH read this shard
**first**, and the docstring says the preference is deliberate:

> The shard is still tried first, and deliberately: it is the recorded
> artifact, so preferring it keeps answers reproducible against a published
> witness rather than varying with the installed dependency set. The live path
> is the fallback, not the default.

That reasoning is sound and it is exactly what makes this bite: a pre-ruling
shard preferred by design overrides a correctly-fixed live path. Measured on
the freshly-synced package:

    canonical_braid(1,0).generators = (0,0,0,0,0,0,0,1,1,1,1)   <- grouped
    compute_tr_M(1,0) = 1.14575969245730086968...               <- superseded
                        (canonical is 0.62932840220292...)

## This is a THIRD carrier, and the first two are already fixed

  1. the code (`compute_tau_M_nucleon_H3`)  -- fixed by `qou-y2o7` option B
  2. the vendored `_internal/` mirror       -- fixed by the `qou-wpp2` drain
  3. **this witness**                        -- NOT fixed, and it is the one
     the shipped API prefers

## Why every detector so far is blind to it

`self_built_braid_word_audit.py` (PR #6960) keys on Python call sites and
cannot see a braid word **stored in a witness JSON and read at runtime**. That
is a scope limit rather than a bug in it — its population is code, this is
data — but it means the corpus currently has no detector for a superseded word
sitting in a witness field. A value-keyed scan over `braid_word*` fields for
monotonicity would be the analogue, and would have found this in one pass.

## Not fixed here

Regenerating the shard means running its producer, which is a real compute on
a contended witness that `main` regenerates on its own cadence — and two
other beans (`qou-xwet` clobbering + positional `B_2H_AME_MeV` pinning,
`qou-3wqg` raw-float64 red and truncated to 5 of 7 rows) already say this file
needs producer work. Those should land together; regenerating it from a
vendor-drain branch would collide with both.

Note the row count is now **9**, so `qou-3wqg`'s '5 of 7 rows' figure is
itself stale — re-measure before quoting it.

## MEASURED: it is 6 files, not 1 (2026-09-07)

Built the data-side selector this bean names as missing —
`computations/audits/witness_braid_word_ordering_audit.py`, on branch
`claude/witness-braid-word-audit-2026-09-07`. The class is not a single
instance.

    stored word fields: 3355 in 96 witness files
    of atom length (12A-1): 128
    and atom-SHAPED (2 <= generator span <= 3A-1): 29
    ATOM-LENGTH AND MONOTONE (the superseded order): 28, in 8 files

Six distinct sources after deduplicating two qou-mass mirrors, and only the
first was known:

| file | fields | |
|---|---|---|
| `canonical-mass-table-extended.witness.json` | 9 | this bean |
| `low-isotope-mass-table.witness.json` | 5 | **NEW** |
| `deltalambda/he4-magnus-omega2-sign.witness.json` | 1 | **NEW** |
| `deltalambda/triton-magnus-omega2-sign.witness.json` | 1 | **NEW** |
| `markov/markov-trace-axiomatic-multi-atom.witness.json` | 1 | **NEW**, 1-indexed |
| `markov/markov-trace-recursive.witness.json` | 1 | **NEW**, 1-indexed |

`low-isotope-mass-table` is the table behind `/dashboard-low`, and it already
carries two other beans (`qou-5h7z` pre-convention, `qou-7e1t` clobbering) — so
that file now has three independent reasons to be regenerated, which is an
argument for doing them in one pass rather than three.

The two 1-indexed hits matter for anyone writing a follow-up scan: the corpus
writes the same grouped word as both `[0]*7+[1]*4` and `[1]*7+[2]*4`, so a
grep for the 0-indexed literal finds under half the carriers.

### The discriminator, and what it cost

An atom word has exactly `12A-1` letters (verified A=1 -> 11, A=2 -> 23,
A=3 -> 35 against this bean's own shard) and lives on 3A strands, so its
generators span 2..3A-1 values. Both facts are about strand count, not
ordering, so neither can hide a grouped word. Monotone then means grouped,
because the ruling's word is non-monotone by construction.

Both parts were bought by false positives the audit produced before they
existed — `joint-tower-sdp-rust` storing an index list `[1,2,...,11]`, and
`hecke-agtb-lineage-schedule` storing **23 words of 14 letters** at n=17, which
the `e[0]` rule flattened into one monotone atom-length sequence. A letter is
now required to be exactly two slots with a non-integer second. 10/10 selftest,
including both.

## CLOSED end to end — #7007 + #7016 (2026-09-07)

The shipped package now answers canonically:

    canonical_braid(1,0) = (0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0)   borromean
    tr_M(p) = 0.629328402202921918165345   (was 1.145759692457300869...)
    tr_M(n) = 0.475133517155682212506090   (was 0.987743688115809571...)

matching qou-y2o7's canonical column to TWENTY digits. The producer never
needed changing — `atom_canonical_crossings` already emitted the borromean
word; only the 2026-08-28 artifact was stale.

Corpus-level, by the #6995 audit: **28 flagged fields in 8 files -> 5 in 5**.

## Correcting a claim I made in #7016's first body

I called `low-isotope-mass-table` "/dashboard-low's source table". **It is
not.** `mass_binding_dashboard.py` references neither that witness nor
`canonical-mass-table-extended` — it computes live. I asserted it first and
checked afterwards, by running the dashboard and then grepping it.

So neither #7007 nor #7016 changes any dashboard output. Measured, the real
loaders of the low-isotope witness are three:

    computations/low_isotope_sign_flip_diagnostic.py:77
    computations/multi_layer_gap_decomposition.py:61
    computations/m_qclt_approx.py            (nucleon masses, not the word)

The defensible claim is the narrower one: a recorded artifact consumed by three
diagnostics, two migrations behind. Worth carrying forward because the same
mistake is easy here — several beans describe this file in terms of the
dashboard, and the dependency does not exist in code.

## 2026-09-14 — the headline defect is FIXED, and this bean never recorded it. Class drained 28 -> 3.

Re-ran this bean's own detector (`computations/audits/witness_braid_word_ordering_audit.py`,
which DID land on main as `fe830d7abe`) on `main` `2b8206e504`.

### The class drained, against a GROWING denominator

    field                        bean (2026-09-07)   today
    stored word fields                       3355     3480
    of atom length (12A-1)                    128      178
    and atom-SHAPED                            29       34
    ATOM-LENGTH AND MONOTONE                   28        3   <- the flagged class

So the corpus grew on every other row and the flagged count still fell **28 -> 3**,
**8 files -> 3**, **6 distinct sources -> 2** (one of the three is a `qou-mass`
mirror of another).

Gone since this bean was written: `canonical-mass-table-extended` (9),
`low-isotope-mass-table` (5), `deltalambda/he4-magnus-omega2-sign` (1),
`deltalambda/triton-magnus-omega2-sign` (1).

### This bean's own subject was fixed 25 MINUTES after it was filed

`canonical-mass-table-extended.witness.json` now carries **zero**
`braid_word_canonical` fields — the field is gone, not corrected — and its
`computedAt` is **2026-09-07T06:43:25Z** against this bean's `created_at`
**06:18:30Z**. The bean was never updated, so its body has read as a live defect
for a week while stating *'Not fixed here'*.

### The central alarm is refuted — verified against the shipped API

The bean's sharpest claim is that `qou_mass.api` prefers the shard *by design*,
so *'a pre-ruling shard preferred by design overrides a correctly-fixed live
path'*. Measured on the freshly-synced package today:

    canonical_braid(1,0).generators = (0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0)
    monotone (= grouped, superseded)? False
    compute_tr_M(1,0) = 0.629328402202921918165345746778485927600219400634

**`0.62932840220292…` is this bean's own stated CANONICAL value**, not its
superseded `1.14575969245730086968`. The shard no longer carries the field, so
the documented shard-first preference now falls through to the corrected live
path. The shipped-API defect is closed.

### The residual 3, adjudicated

All three are the same test vector plus its mirror:

    markov/markov-trace-axiomatic-multi-atom.witness.json  /atoms/proton/word
    markov/markov-trace-recursive.witness.json             /test_cases[5]/word
    qou-mass/src/qou_mass/markov-trace-recursive.witness.json   (mirror of the above)

`test_cases[5]` is **named** `σ_1^7 σ_2^4 (proton)` and carries
`tr_M_symbolic_full` — a closed form in `q`. Its job is *'given word W, does the
recursion reproduce the symbolic trace?'*, and that is **convention-neutral**:
the symbolic result is exact for whatever word is fed. `computedAt`
2026-09-05T17:10, the same day as the ruling.

**Verdict: the computation is sound; the LABEL is stale.** Calling the grouped
word '(proton)' asserts an identification the 2026-09-05 ruling retired. That is
a naming defect of the same shape as `qou-khue`'s missing `prediction_route`
field — a reader meets a superseded identification with nothing saying so.

### Left open deliberately

**Not closed.** Two reasons. The label call is a change inside someone else's
test harness and is neither a precision increase nor corpus-fixed (the corpus
fixes that the word is superseded, not what the test case should be called), so
it waits under ASK-THE-OWNER. And this bean now carries the census for the
class, which is the useful thing to keep open.

**Also still true and unaddressed:** the detector is on main but **wired into no
gate** — `grep` finds no reference from `scripts/` or `.github/`. A one-shot
audit nobody runs is how 28 became invisible in the first place. Wiring it is a
gate change and also waits.
