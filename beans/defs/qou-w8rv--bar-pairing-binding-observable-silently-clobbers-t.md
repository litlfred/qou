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

---

## Earlier independent pass, 2026-09-06 (session `rag-document-ingestion-options-orasrw`)

Reached the same defect and the same mechanism a day earlier, on a branch that had not yet seen the fix above. **The code fix in that pass was the ordered fallback the section above names as its own regression** — it is superseded, and `_cached_q(w, q_tag)` is the right shape. What survives is the measurement, which the section above does not carry: the per-producer field census, the enumeration of the four clobbered files, and the downstream consumers of the fields the clobber destroys.

## FIXED 2026-09-06. And the title undercounts: it is FOUR caches, not three.

Probe: `computations/probes/chi_cache_guard_reads_a_field_that_exists_probe.py`
(7/7). Fix in `computations/bar_pairing_binding_observable.py`.

### The defect

Four producers write files matching `chi-<atom>(-free)-h<n>-at-<tag>-50dps`,
and each spells the q value differently:

| producer | q field | files on disk |
|---|---|---|
| `bar_pairing_binding_observable.py` (the consumer) | `q_str` | 2 |
| `chi_at_q_inv_via_native_mpfr.py` | `q_inv_50dps_str` | 4 |
| `chi_at_q0_via_hoefsmit_mpfr.py` | **`q_0_50dps`** | 4 |
| *(unstamped — no `producer`/`scriptFile`)* | — | 6 |

`_load_or_compute_chi`'s cache-key guard read

```python
cached_q = w.get("q_str", w.get("q_0_50dps_str", w.get("q_inv_50dps_str")))
```

Two real names and `q_0_50dps_str`, **which no producer writes**. So on every
cache from the Hoefsmit producer `cached_q` was `None`, the hit condition
`cached_q == q_str` could never hold, and the file was recomputed and
overwritten with the consumer's schema.

The guard itself was right to exist — a Copilot review added it on PR #1748 so
a q re-pin could not silently load a stale witness. It was reading the wrong
names.

### Measured, 2026-09-06, over all 16 on-disk caches

The old guard returned `None` on **exactly 4** files and on no others:

```
chi-deuteron-h6-at-q0-50dps.witness.json
chi-tritium-h9-at-q0-50dps.witness.json
chi-helium-3-h9-at-q0-50dps.witness.json
chi-helium-4-h12-at-q0-50dps.witness.json
```

All four `producer: chi_at_q0_via_hoefsmit_mpfr.py` — **the four canonical
at-q0 caches, and the four just regenerated under `qou-92u9`.** The other
twelve carried a recognised field and hit correctly. The title says three;
four is right.

### What the clobber destroys

The consumer's write drops **`tr_M_at_q0`** and **`q_0_50dps`**, which are
read by, at minimum:

- `aK_via_lp_dual_hecke_basis.py:119` — `load_tr_M()` opens
  `chi-{atom}-h{n}-at-q0-50dps.witness.json` → `d["tr_M_at_q0"]`
- `s5so3_geometric_wlambda_a4_helium_probe.py:68` — opens
  `chi-helium-4-h12-at-q0-50dps.witness.json` → `d["q_0_50dps"]`
- `probe_chirality_delta_lambda_the3_diagnostic.py:59` — opens the tritium
  and ³He h9 caches → `d["q_0_50dps"]`
- `carrier_saturation_mechanism_probe.py`, `li6_h18_amplification_
  discriminator_probe.py` — `w["tr_M_at_q0"]`

`mass_vol_density.py:81` reads `tr_M_at_q0` too but from
`chi-proton-h3-at-q0-50dps`, and `proton` is not in this script's `ISOTOPES`
— **not affected.**

Each of those is a `KeyError` after a clobber, not a wrong number. Loud, but
only at the next consumer's run, long after the data is gone.

### Why it was silent

Both diagnostic branches were guarded on `cached_q is not None` — which is
exactly the case that failed. A miss on a *recognised* schema printed a
"cache miss" line; a miss on an *unrecognised* one printed nothing and
destroyed the file.

### The fix, three parts

1. **Look up every producer's vocabulary** — `q_0_50dps` and `q0Value` added,
   as an explicit loop rather than nested `dict.get` defaults (the old idiom
   also returns `None` for a key *present* with value `None`). Verified: the
   guard now hits **16/16** with **0 recomputes**, proved by replacing the
   compute path with a raising stub, so a hit is established by nothing having
   been recomputed rather than by a return value.
2. **Make the unrecognised-schema case loud** — it prints the file's actual
   top-level keys.
3. **Refuse to overwrite another producer's file.** If the cache genuinely
   disagrees on q *and* names a different `producer`, raise and say which
   script to re-run. Overwriting a canonical at-q0 witness with this script's
   schema is never the right repair. Checked *before* the diagnostics so the
   "recomputing" messages only print on paths that really do recompute.
   Scoped: a mismatch on a file this script owns still recomputes normally.

### Residual gap, asserted rather than left open

The refusal is keyed on `w["producer"]`, so it **cannot protect an unstamped
file**. Six of sixteen are unstamped — and all six are `free-*`, the kind this
script owns exclusively, so the hole is real but unoccupied. The probe asserts
`no_canonical_atom_cache_is_unstamped` (0 of 8), so a future unstamped
canonical cache trips it instead of quietly reinstating the bug.

### Why this blocked the sweep

The 22-producer refresh sweep after the chi regeneration halted at 1/22 on
this. Running it would have recomputed and overwritten the four caches the
regeneration had just produced — undoing the owner-ruled `qou-92u9` work
inside the pass meant to consolidate it. The remaining 21 producers are now
unblocked.