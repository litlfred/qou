---
# qou-36i2
title: canonical-mass-table-extended stores the PRE-RULING grouped word in braid_word_canonical, and qou-mass prefers it BY DESIGN
status: todo
type: bug
priority: normal
created_at: 2026-09-07T06:18:30Z
updated_at: 2026-09-07T06:19:09Z
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
