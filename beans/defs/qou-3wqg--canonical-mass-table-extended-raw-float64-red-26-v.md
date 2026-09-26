---
# qou-3wqg
title: 'canonical-mass-table-extended: raw-float64 red (26 vs baseline 24) AND the committed witness is truncated to 5 of 7 rows'
status: completed
type: bug
priority: normal
created_at: 2026-08-15T23:00:29Z
updated_at: 2026-09-08T04:48:11Z
---


## Two defects, and the second is the one nobody was looking at

`scripts/precision-gates.sh` is red on `raw-float64` with **two** REGRESSED
witnesses. One is `rho-k-co-casimir-extended` (3 → 4, documented on `qou-mnrd`,
needs a ≥ 24 GiB host). The other is this one, and it had not been attributed:

    canonical-mass-table-extended.witness.json    24 -> 26

Bisected rather than assumed. My first guess was the most recent commit to touch
it, `204c5c4e3` ("regenerate with pyhecke_native") — **wrong**, the count was 26
both before and after it. It goes back to:

    1af7d4b7a   24 raw float64
    708ce844c   26 raw float64      fix(ctype): d_for_ctype broke its own
                                    type contract, on averaged_weighted [qou-gscs]

`708ce844c` restructured the table (row 0 went from the deuteron to the proton),
row 4 gained `err_*` fields it previously lacked, and two rows lost
`B_AME_MeV`. Net +2, and the baseline was never updated.

### The second defect: the committed witness is TRUNCATED

Regenerating gives **7 rows where the committed file has 5**, and 1524 leaves
against 588. The producer's own ORDERING INVARIANT comment documents indices
0–7, naming index 5 as ⁴He and index 6 as ⁵Li — **neither of which is in the
committed witness**. So the published table stops at ³He while claiming a
layout that runs to ⁶Li.

`content/values/registry.ts` reads `data.rows.2.B_AME_MeV` (the deuteron), which
survives at index 2 either way — so the truncation is invisible to the one
consumer that pins an index. Same shape as `atom-level-wedderburn-tower`
(`results: {}`) on bean `qou-j6gb`: a truncated witness that no gate flags,
because shrinkage only trips the shape guard when something REGENERATES it.

### DO NOT fix this by stringifying — I nearly did

The tempting fix is to serialize `err_MeV` / `err_pct` / `err_ppb` / `err_ppm`
as strings. It works: 26 → 8 raw float64, comfortably under the baseline, and
`atlas_render_canonical_table._fmt_number` already coerces strings so only one
raw-arithmetic site (`err_ppm * 1000.0`, line 135) needs a `float()`.

**It is also exactly what the audit forbids** — *"Carry mpmath.mpf from the
source and serialize with `_precision.fmt`; do NOT stringify the float."* I
implemented it, then checked whether the values actually carry more than a float
before committing:

    prediction_MeV_50dps = "2.2488207948647343"     18 chars — a FLOAT
    err_MeV              = "0.024254594864734358"

The field is named `50dps` and holds float64. Stringifying would have moved 20
fields out of the ratchet's count while preserving exactly zero extra digits —
a green gate and no more precision than before. Reverted.

### Where the precision is actually lost

Two places, both upstream of the serialization:

    canonical_mass_table_extended.py:80-85
        (1, 1): float(AME_B_DEUTERON_MEV_VALIDATION),   # and T, ³He, ⁴He, ⁶Li

`AME_B_DEUTERON_MEV_VALIDATION` is an **mpf** in `codata_constants`; the
producer casts it to float on the way into `B_AME_MEV`. And:

    lookup_b_pred_existing(...) -> tuple[float | None, str | None]

`pred` is a float by declared type, sourced from `mass-table-ppb.witness.json`.
So `err = pred - ref` cannot carry more than float64 no matter what the
serialization does.

**A real fix is therefore: drop the `float()` casts on the AME constants, carry
`pred` as mpf through `lookup_b_pred_existing` and its upstream witness, then
serialize with `fmt`.** That is a multi-file change through another arc's
prediction path, not a producer tweak — which is why it is a bean and not a
commit.

### Suggested order

  1. Decide whether the 5-row truncation is intended. If not, regenerating
     restores ⁴He and ⁵Li — but on its own that takes the ratchet from 26 to a
     larger number, because more rows means more `err_*` fields.
  2. Then the precision port above, which removes them properly.
  3. Only then update the baseline, downward.

Doing (1) before (2) leaves the gate redder than it is now, which is probably
why it has sat.

## Traced the chain to its root: there is no mpf to carry

The bean above says the fix is to "carry `pred` as mpf through
`lookup_b_pred_existing` and its upstream witness". **There is nothing to
carry.** Followed it one hop at a time:

    canonical_mass_table_extended.lookup_b_pred_existing
        -> returns r["B_pred_MeV"] straight out of mass-table-ppb.witness.json,
           no cast of its own

    mass-table-ppb.witness.json
        -> "B_pred_MeV": 2.2488207948647343      a JSON FLOAT, not a string

    computations/mass_table_ppb.py                the root producer
        -> imports NO mpmath at all. No `import mpmath`, no set_compute_dps(),
           no mp.dps anywhere in the file.
        -> `from q_parameter import Q as Q0`      the FLOAT q0, not Q_MP
        -> M_E_MEV from experimental_constants, VOL_BORROMEAN / VOL_7_SQ_1
           from knot_volumes — all float
        -> B = nu * M_E_MEV * vol                 float arithmetic throughout

So `B_pred` is float64 from the root, and `err = pred - ref` cannot be anything
else regardless of what `canonical_mass_table_extended` does. Dropping the
`float()` casts on `AME_B_*_MEV_VALIDATION` there is still correct on its own
terms — those constants really are mpf and really are being truncated — but it
changes nothing about the err fields, because `pred` dominates.

**Revised scope: draining this means porting `mass_table_ppb.py` to mpmath** —
switching it from `q_parameter.Q` to `Q_MP`, and its `M_E_MEV` / `VOL_*`
constants to mpf sources. That changes every published `B_pred_MeV` in a
16-row table which other producers read. A third arc, and a bigger one than the
two above it.

## A gate gap this exposes, worth its own consideration

`mass_table_ppb.py` emits a witness full of physics values and uses **zero
mpmath**. It is therefore invisible to all four precision gates, including the
one added for exactly this family of blind spots:

    mpf_float_source_audit          needs an mpf(<float literal>) to flag
    mpf_import_time_dps_audit       needs an mpf built at module scope
    witness_float64_padding_audit   needs padding, i.e. mpf serialized too wide
    never_raises_dps_audit          needs mp_value_calls > 0 — this file has none

Every one of them keys on the producer *touching mpmath*. A producer that never
touches it at all emits honest float64 and is, by construction, outside all four.
`never_raises_dps_audit` was written for "raises precision nowhere"; the case
below it is "has no precision to raise", and the two are not the same.

Whether that is a defect is a real question rather than an obvious yes — plenty
of producers legitimately work in float64. What makes THIS one worth flagging is
that it feeds a 16-row published mass table which downstream witnesses compare
against AME references at ppb, and it takes the float q0 when an mpf q0 is
available two imports away.

Not proposing a fifth gate on the strength of one example. Recording the
category so the next instance is recognised rather than re-derived.

## PORTED — the whole chain, root first

    mass-table-ppb.witness.json                  119 -> 36 raw float64
    canonical-mass-table-extended.witness.json    26 ->  1   (baseline 24)
    raw-float64 ratchet: 2 REGRESSED -> 1        (only rho-k remains)

Done root-first, because the downstream producer cannot carry precision that
never existed upstream. Three files:

**1. `mass_table_ppb.py` — the actual root.** It imported the FLOAT variant of
every constant and computed `B = nu * m_e * Vol` in Python floats, with no
`import mpmath` in the file at all. The mpf variants already sat beside the
floats, exactly as this module's own comment anticipated ("a `--precision mpfr`
lift only needs to update one place"):

    q_parameter.Q -> Q_MP
    experimental_constants.M_E_MEV -> codata_constants.M_E_MEV   (module, not name)
    knot_volumes.VOL_BORROMEAN / VOL_7_SQ_1 -> the _MPF variants

**2. `canonical_mass_table_extended.py`.** `lookup_b_pred_existing` now lifts
with `mp.mpf(...)` rather than taking the JSON number — lossless, since upstream
emits a 44-digit decimal string. `B_AME_MEV` drops its `float()` wrappers around
the five mpf `AME_B_*` constants, and its four bare literals become
`mp.mpf("...")` strings (binding the decimal, not the binary64). The err fields
serialize with `fmt`.

**3. `atlas_render_canonical_table.py`.** One line: `float(err_ppm)` at the sole
site doing arithmetic before formatting. `_fmt_number` already coerced strings
everywhere else.

### This is the move the audit ALLOWS, and the earlier attempt was not

The reverted attempt stringified `err_*` while `pred` was still a float — 20
fields out of the count, zero digits gained. Now `pred` and `ref` are both mpf
and `fmt` writes out precision that genuinely exists. Same-looking diff, opposite
meaning; the difference is entirely upstream.

### The numbers MOVED, which is the point

    B_pred_MeV (D)   2.2488207948647343
                  -> 2.248820797901308979386776627507060766220092

They differ at the **9th significant digit** — ~1.4e-9 relative. The float
pipeline was not merely imprecise, it was wrong past digit 8. `err_ppb` for the
deuteron moves 10903067.24 -> 10903068.61 for the same reason.

Anyone comparing these predictions against AME at ppb was reading roughly 1.4
ppb of pipeline noise as signal.

### Also fixed in passing: the truncation

`canonical-mass-table-extended` now emits **7 rows where the committed file had
5**, restoring ⁴He and ⁵Li — the two the producer's own ORDERING INVARIANT names
at indices 5 and 6 and the published witness did not contain. Shape guard: 0
collapsed.

## Survey result: "no mpmath" is too blunt to gate on

    runnable witness producers            2355
    ZERO mpmath (no import, no mp values)  578      ~25%
    touch mpmath in some way              1777

578 is a quarter of the corpus, and most are certainly fine — combinatorial
probes, structural audits, anything whose output is counts or flags. A gate on
"emits a witness, uses no mpmath" would fire on all of them.

So the category is real but the discriminator is not "no mpmath" — it is
something like "emits values that are compared against experiment at ppb/ppm",
which is not statically obvious from the source. `mass_table_ppb.py` was worth
finding because it fed a ppb comparison while importing the float q₀ with an mpf
one two lines away; that is a judgement about what the numbers are FOR, not a
property a parser can see.

**Recommendation: do not add a fifth gate.** The four existing ones plus this
survey are enough to find the next instance by hand. A gate with 578 baseline
entries would be a gate nobody reads.


---

## Update (claude/ppb-consumers-recheck @ 4d852e5d4) — raw-float64 half CLOSED

`canonical-mass-table-extended.witness.json` is now at **0** raw float64, down
from the 26 this bean opened on (baseline 24, so it is drained past baseline
rather than merely back to it).

Two changes got it there. The `err_*` and prediction fields moved to
`_precision.fmt` in the mass_table_ppb port; the last remaining leaf was
`paper_hard_floor_ppb: 780.0` — the paper's declared CAL-2 propagation floor,
a stated threshold rather than a computed quantity. It is now the int `780`.
`atlas_render_canonical_table.py:167` already read it through `int(...)`, so no
consumer changes.

The truncation half is also gone: the committed witness carries **7 rows**
(D, T, 3He, 4He, 5Li, 6Li, 7Li), not the 5 this bean found.

## Still open, and it is NOT the same defect this bean opened on

The producer's ORDERING INVARIANT comment names index 5 as 4He and index 6 as
5Li — i.e. a layout that begins with p and n. The regenerated witness puts 4He
at index 3 and 5Li at index 4, because the default `--atoms` set has no nucleon
rows. So the published table and the documented invariant still disagree about
what index means what, and `content/values/registry.ts` pins `data.rows.2.
B_AME_MeV` against that layout. Either the comment or the default atom set is
wrong; deciding which is a content call, not a precision one.

Unrelated observation from the same regeneration, recorded so it is not lost:
the witness records `"precision": "mpfr"` alongside `"dps": 0`. Those come from
different branches of the same `args.precision` — `precision` is forced to
"mpfr" for the `branching` method, while `dps` still reports the f64 value 0.
Each is defensible under its own definition ("effective precision" vs "the dps
handed to the Rust binary"); the PAIRING is what reads as a contradiction.


---

## CLOSED 2026-09-08 — all four items are resolved on `main`, including the one this bean recorded as still open

Verified on `main` `a61496dbc82`, item by item.

| item this bean raised | state |
|---|---|
| raw-float64 red (26 vs baseline 24) | **0** — the witness appears nowhere in `witness-raw-float64-audit`'s dirty list |
| committed witness truncated to 5 rows | **9 rows** (p, n, D, T, ³He, ⁴He, ⁵Li, ⁶Li, ⁷Li) — better than the 7 the bean's own update recorded |
| `"precision": "mpfr"` beside `"dps": 0` | **`mpfr` / `50`** — the pairing contradiction is gone |
| ordering invariant vs emitted layout | **they agree** |

### The fourth item is the one worth spelling out, because this bean called it "Still open"

The bean recorded: *"The producer's ORDERING INVARIANT comment names index 5 as
4He and index 6 as 5Li … The regenerated witness puts 4He at index 3 and 5Li at
index 4, because the default `--atoms` set has no nucleon rows."*

Measured today, `data.rows` is
`[(1,0), (0,1), (1,1), (1,2), (2,1), (2,2), (3,2), (3,3), (3,4)]` — so **⁴He is
at index 5 and ⁵Li at index 6**, exactly what
`canonical_mass_table_extended.py:118-126` documents. The default set *does* now
begin with p and n. Resolved by the same full-coverage fix that closed the
truncation half (`low_isotope_mass_table.py` no longer passes `--atoms`, bean
`qou-xwet`).

### The registry pin was fixed STRUCTURALLY, which is better than the layouts agreeing

The bean flagged that `content/values/registry.ts` pins `data.rows.2.B_AME_MeV`
against a positional layout. That pin is gone; the file now reads *"Addressed by
NUCLIDE, not by position (bean `qou-xwet`)"* and uses `rows_by_nuclide`, keyed by
the `--atoms` label, so a missing row is a missing key and fails loudly.

Its comment also records what the positional pin actually cost, which is the
reusable part: *"from 2026-06-22 to 2026-08-15 `rows.2` was ³He — so this entry
returned 7.71804132 MeV, 3.47× the deuteron's, under the description below.
Nothing caught it; it was restored by a second clobber rather than by a fix."*
Note the mechanism was **not** reordering, which is what the invariant comment
guards against — it was the fixed output filename being overwritten by a
restricted-`--atoms` run, so every index shifted with nothing reordered. A
positional pin cannot see that; a nuclide key can.

### Its own recommendation stands and was not overturned

*"Do not add a fifth gate. … A gate with 578 baseline entries would be a gate
nobody reads."* Nothing here adds one; all four items closed at the producer or
at the consumer.
