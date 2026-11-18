---
# qou-rj7d
title: 'The 60-dps record of a SHORT decimal: 734 confirmed fields the float64-padding ratchet cannot see, including CAL-1 m_e'
status: in-progress
type: bug
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-13T08:40:07Z
updated_at: 2026-11-18T07:38:33Z
parent: qou-9nnz
---

Found 2026-09-13 while draining `bar_pairing_binding_observable` (raw-float64
ratchet).  Rendering its `AME_MeV` through `_precision.fmt` produced

    2.22456619999999999999999999999999999999999999999999734095406

for a datum whose value is `2.2245662` — eight significant figures.  Sixty
digits published, eight of them real.

## The class

`codata_constants._ame_binding_mev` builds the constant inside
`mp.workdps(max(50, mp.dps))`, and the module is imported before
`set_compute_dps()` has run in most producers, so the constant IS the 50-dps
binary approximation of an exact decimal.  `fmt` renders at `OUTPUT_DPS = 60`
(or a producer prints at 70), and the ten to twenty digits past the 50-dps ulp
are mpmath truncation tail.

This is not the binary64-padding class.  It is one working-precision up.

## Why the existing ratchet cannot see it

`witness_float64_padding_audit.py`'s discriminator is, in its own words,
relative distance to the nearest binary64: ~1e-17 for a genuine
high-precision value, ~1e-50 for a binary64 expansion.  A 50-dps value sits
**~1e-17** from the nearest double — it is a *genuine* high-precision value by
that test — so every field below passes it.  Detector-blindness taxonomy class;
the discriminator is sound and simply answers a different question.

## Measured

Scan of **3,745** committed `computations/**/*.witness.json`.  Two passes,
because the first one over-claimed and the correction is the interesting part.

**Pass 1 (heuristic, DO NOT quote): 1,489 fields / 144 witnesses** — "within
1e-45 relative of some <= 15-significant-figure decimal".  That threshold also
catches a genuinely computed quantity that lands near a short decimal:
`pn-alpha-lp-dual`'s `y_star_str[0] = 1.000000000000000000000000000000000000000000000309399`
has a tail of 3.1e-46 and is an SDP residual, not padding.

**Pass 2 (exact, quote this): 734 fields / 94 witnesses CONFIRMED.**  The test
reconstructs the suspect character-for-character —

    mp.nstr(mpf(short_decimal) built at B dps, printed at O dps) == recorded

over `B in {50, 53, 60, 70}`, `O in {60, 65, 67, 70}`.  A match is not a
heuristic: the recorded digits are exactly what you get by taking a short
decimal into an mpf at a lower working precision and printing it at a higher
one.  There is no information in the tail.

A further **745 fields / 59 witnesses are UNCONFIRMED** and are NOT claimed.
That bucket is mixed: some are the same class at a build precision not in the
four tried (`q-values-derived`'s 476 `Q_pred_MeV` / `Q_AME_MeV` fields look
exactly like it — `0.271805739276899999...998869113528` against the datum
`0.2718057392769` — but do not reconstruct from {50,53,60,70}), and some are
genuine near-integer solver output.  Settling it means widening the build-dps
sweep, not reasoning about it.

### Top confirmed carriers

|  n | witness |
|---:|---|
| 108 | `sweeps/paper-six-term-isotope-sweep` |
| 105 | `k-star-variance-phase5d-5b` |
| 104 | `delta-lambda-full-variance-phase5e-1` |
|  35 | `binding-a3plus-full-theta-assembly` |
|  28 | `atom-mass-full-hecke` |
|  28 | `fr-pullback-cosh-h` |
|  24 | `fr-pullback-k1-k2` |
|  18 | `binding-a3plus-joint-ji-combiner` |
|  18 | `option-e-multi-isotope-delta-lambda-probe-v3` |
|  14 | `binding-depth-stratified-knot-weighted` |
|  14 | `delta-lambda-empirical-tabulation` |

### The quantities, and this is why it is not cosmetic

- **`m_e_MeV` — CAL-1 itself**, the calibration input that fixes the MeV scale,
  published as
  `0.5109989506900000000000000000000000000000000000000005654434719000544678`
  in at least five witnesses (`k-star-variance-phase5d-5b`,
  `binding-a3plus-full-theta-assembly`, `binding-a3plus-joint-ji-combiner`,
  `binding-a3plus-arccosh-growth-split`, `fr-pullback-k3-test`,
  `binding-depth-stratified-knot-weighted`).  The datum is `0.51099895069`.
- **`M_codata`** = `938.272089429999999999999999999999999999999999999999459224910`
  and `939.565000000000000000000000000000000000000000000000383167549`.
- **The AME binding energies** — `2.2245662`, `8.4817962`, `7.71804132` — which
  are the MEASURED side of every binding residual the corpus reports.
- One `assertions[0].computed` field
  (`binding-depth-stratified-knot-weighted`), i.e. an assertion decided against
  a padded target.

`delta-lambda-empirical-tabulation` carries **both** `938.27208816` and
`938.27208943` in adjacent fields, each padded to 60 — two different proton
masses side by side, both reading as exact to fifty places.

## What this is NOT

- **Not a wrong number.**  Every one of these agrees with its datum to ~1e-51.
  The defect is the claim about how well the quantity is known, which is the
  same defect the padding ratchet exists for, one precision level up.
- **Not the source-literal class.**  PR #7271 (`qou-gqt5`) built an AST detector
  for a bare Python literal spelling more digits than its parse can keep.  That
  is the SOURCE side; this is the RECORD side, and the two do not overlap: a
  producer here writes the string correctly from an `mpf`, and the `mpf` is the
  thing that was built short.

## Disposition — ASK, do not sweep

Under the 2026-09-07 ASK-THE-OWNER directive this is measurement, not a
mandate.  A fix is per-producer (record the datum, e.g.
`mp.nstr(x, 50, strip_zeros=True)`, rather than `fmt(x)`, for a field that IS an
input constant) and 94 witnesses is a sweep.  Three options for the owner:

1. **Nothing.**  The numbers are right; only the digit count overstates.  The
   cost is that CAL-1 and the AME comparison targets keep reading as
   fifty-digit quantities in every witness a reader opens.
2. **Fix at `codata_constants`** — build the constants at `COMPUTE_DPS` rather
   than 50, so the tail moves out past `OUTPUT_DPS` and `fmt` is honest again.
   One file, 300+ consumers, and it MOVES NUMBERS at the 1e-51 level in every
   witness that reads them — invisible physically, but it re-runs the corpus.
3. **Fix at the record** — a `fmt_datum()` helper in `_precision` for
   input-constant fields, applied producer by producer as each is touched.
   Cheapest per step, slowest to finish, and it needs a rule for which fields
   are "data" rather than "computed".

**Recommendation (my judgement, not a finding): option 3, plus a detector.**
The detector is the part with standalone value — pass 2's exact reconstruction
is cheap, has no false positives by construction, and would keep the count from
growing while the disposition is decided.  Option 2 is the principled fix but
re-running the corpus to move a 1e-51 tail is a large action for an invisible
gain, and it should be the owner's call rather than a consequence of this bean.

Probe (scratch, not committed): the two-pass script is reproducible from the
description above; the exact test is ~40 lines.
