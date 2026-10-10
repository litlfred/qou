---
# qou-2ht2
title: 'iterative-knot-builder.witness.json is a bare JSON array, not a witness: no envelope, no provenance, float64 volumes'
status: completed
type: task
priority: normal
created_at: 2026-08-21T16:06:47Z
updated_at: 2026-09-04T12:22:26Z
---

Found while triaging the provenance-COMPLETENESS audit (PR #5373, bean
qou-7aum). It is the audit's single `PROV_PARSE_ERROR`, verdict
"root is not an object" — a category the 55 PROV_MISSING did not include and
which nobody had surfaced.

## What it is

`computations/iterative-knot-builder.witness.json` is a **bare JSON array of 5
rows**, with no witness envelope at all:

```json
[ { "Z": 1, "N": 0, "A": 1, "initial_braid_length": 11,
    "volume": 7816850.323077447, "reduced_knot_name": "q-clt-proxy" }, ... ]
```

No `engine`, no `scriptFile`, no `commitSha`, no `assertions`, no
`precisionMetadata`, no `environment`. It carries the `.witness.json` suffix
and is not a witness.

## It is load-bearing, and the workaround is codified

Produced by `computations/iterative_knot_builder.py`; **read** by
`computations/derivation_chain_validator.py`, which special-cases it by name:

```python
# Some witnesses are top-level JSON arrays (e.g. iterative-knot-builder),
# not objects; tolerate them. Prefer scriptFile from the first dict element
```

So the shape defect has a consumer-side workaround naming this exact file
rather than a producer-side fix. It is also already listed in
`computations/raw-float64-baseline.json` — the float64 `volume` values are
baselined, not drained.

## Why it was not fixed in #5373

Two coupled parts, on a load-bearing producer:

1. **Envelope.** Move the producer to `WitnessBuilder` so the payload sits
   under a proper witness. The validator's dict branch (`data.get("scriptFile")`)
   would then be the live path, so the reader is already compatible — but the
   `isinstance(data, list)` tolerance and its comment should be retired in the
   same change, not left as a stale special case.
2. **Precision.** The volumes are raw float64 (`7816850.323077447`). Wrapping
   the payload without fixing that just moves a baselined float64 into a
   freshly-written witness. Per the standing rule the fix is at the producer —
   carry `mpmath.mpf` from source, serialize with `_precision.fmt` — and the
   baseline entry then DRAINS rather than being re-justified.

Doing only (1) would trip the raw-float64 ratchet; doing only (2) leaves the
parse error. Both belong in one change, with the producer re-run.

## Check when fixing

Confirm the recomputed volumes match the committed ones to the precision the
producer can actually justify. `q-clt-proxy` volumes in the 1e6–1e7 range are
extrapolation proxies, not hyperbolic volumes — verify what precision is
meaningful before serializing 50 digits of it.

CLAIMED 2026-09-04 (session cool-johnson). Most of this is ALREADY DONE by prior work: the witness is now a proper dict envelope (engine/assertions/commitSha present), carries NO float64 (volumes drained), and is NOT in raw-float64-baseline. The ONLY remaining piece is the bean's explicit ask: retire the stale isinstance(data,list) tolerance + 'top-level JSON array (e.g. iterative-knot-builder)' comment in derivation_chain_validator.py (lines 408-424). Verified corpus-wide: ZERO bare-array witnesses remain (glob scan of computations/**/*.witness.json), so the branch is dead code. Removing it surfaces any future bare array as computational-only rather than silently tolerating it.

MERGED 2026-09-04 (PR #6623, main HEAD d89535efddb). Dead isinstance(data,list) tolerance retired from derivation_chain_validator.py; behavior-preserving (zero bare-array witnesses corpus-wide). Envelope/float64/baseline were already fixed by prior work.
