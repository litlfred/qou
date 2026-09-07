---
# qou-w8rv
title: bar_pairing_binding_observable silently CLOBBERS three canonical chi caches on every run — its cache-key guard reads a field name that does not exist
status: completed
type: task
priority: normal
created_at: 2026-09-06T13:04:07Z
updated_at: 2026-09-07T06:19:57Z
---

## FIXED 2026-09-07 — measured on both legs, and my first fix was itself wrong

Your title is exactly right and the mechanism is confirmed. Recorded here with the
measurements, since the bean carried a title and no body.

### The defect, mechanism first

`bar_pairing_binding_observable.py` extracted the cache key inline:

    cached_q = w.get("q_str", w.get("q_0_50dps_str", w.get("q_inv_50dps_str")))

The canonical q0 caches are written by `chi_at_q0_via_hoefsmit_mpfr.py`, which
spells the field **`q_0_50dps`** — no `_str`. None of the three names exist on
those witnesses, so `cached_q` is `None`, and three things follow:

1. `cached_q == q_str` is `None == <str>` — **the cache never hit**;
2. both diagnostics are guarded by `cached_q is not None`, so **nothing printed**;
3. the miss fell through to recompute-and-persist, **overwriting** the canonical
   witness with this consumer's own payload shape.

A guard added (Copilot review, #1748) to stop a *stale* witness being loaded was
silently destroying the *fresh* one instead.

### Measured, not reasoned

Running the ORIGINAL producer on `deuteron` with the 20 chi witnesses hashed
before and after:

    CLOBBERED: computations/chi-deuteron-h6-at-q0-50dps.witness.json
    diagnostics printed: "computing atom@q0 ... caching to <that file>"
                         and NO "cache miss" line

— the silence is the defect, and it reproduces exactly as the mechanism predicts.

### My first fix was WRONG, and the test caught it

I appended `q_0_50dps` to the shared chain. That fixes the q0 leg and **breaks the
qinv leg**, because a qinv witness carries BOTH values — `q_inv_50dps_str` (the q
it was computed at) and `q_0_50dps` (the anchor, as provenance). The chain then
reads the anchor off a qinv cache. The run said so:

    cache miss: chi-deuteron-h6-at-qinv-50dps.witness.json computed at
                q_str='1.1099...', requested '0.9009...' — recomputing

**An ordered fallback cannot be right when a witness carries both.** The
disambiguator is not an ordering, it is which cache is being read. `_cached_q` is
now keyed on `q_tag`:

    "q0":   ("q_str", "q_0_50dps", "q_0_50dps_str")
    "qinv": ("q_str", "q_inv_50dps_str", "q_inv_50dps")

### Verification

* `--self-test` / `--selftest` (both spellings, per `qou-7u0d`): **8/8**, including
  the regression case — a qinv witness carrying both fields — and both real
  committed witnesses, so it cannot pass on toy data alone.
* Producer re-run on `deuteron`: **all 20 chi witnesses unchanged, zero cache
  misses, every cache hit.**

Taking this unclaimed `todo` because no branch was on it (checked the last 20
`claude/*` for `bar_pairing_binding_observable`) and it is the same class as the
two findings already on my PR: a guard that cannot say it is off. Landed on
litlfred/qou#6971.
