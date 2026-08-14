---
# qou-l5zi
title: "wrap_legacy silently drops payload assertions -> 28 producers emit allPassed:true vacuously"
status: todo
type: task
priority: high
created_at: 2026-08-14T19:10:00Z
updated_at: 2026-08-14T19:10:00Z
---

## The defect

`WitnessBuilder.wrap_legacy(name, payload, …)` routes reserved keys to
structured slots and **skips** every key in `_RESERVED_LEGACY_KEYS`
(`tools/qou-substrate/python/qou_substrate/witness.py:736`). That set includes
**`assertions` and `allPassed`**, on the reasoning that `build()` recomputes
them from assertions registered via `add_assertion`.

So a producer that writes its checks as a payload literal —

```python
payload = {..., "assertions": [{"name": "x_holds", "passed": False}],
           "allPassed": False}
WitnessBuilder.wrap_legacy("my-probe", payload, script_path=__file__).save()
```

— has them **silently discarded**, and `build()` emits

```json
"assertions": [], "allPassed": true
```

`allPassed` is `true` *vacuously*, because nothing was registered. No warning,
no exception. A probe whose headline check FAILED reports success.

## Measured

| | |
|---|---|
| producers passing `assertions` into a `wrap_legacy` payload | **29** |
| ...of those NOT also calling `add_assertion` (so dropped) | **28** |
| witnesses corpus-wide with `allPassed: true` and zero assertions | **389** of 2083 (19 %) |

The 389 is an upper bound on the damage — some producers legitimately register
no assertions — but the 28 all *intend* to assert.

Proven end-to-end on `rho_k_counit_vortex_writhe_probe.py`: the source builds
2 assertions; `rho-k-counit-vortex-writhe.witness.json` carries
`assertions: 0, allPassed: true`.

Found because it bit this session's own new probe
(`computations/probes/ak_lp_dual_quotient_probe.py`): its headline check
`quotient_recovers_a_K_closed` is **False**, and the first witness it wrote
still said `allPassed: true`. Switching to `add_assertion` produced the honest
`allPassed: false`.

## Why it matters more than a formatting bug

This is the same failure shape as `qou-9d6h` (D3), where
`deuteron_tower_fusion_frame_probe` wrote `allPassed: False` and then exited 0,
so the cascade filed it as `ok`. Here it is worse: the witness itself asserts
success. Anything that gates on `allPassed` — dashboards, the integration
watchers, a reader skimming a witness — is reading a value that was never
computed.

## The fix, per producer

Register through the builder instead of the payload:

```python
builder = WitnessBuilder.wrap_legacy("my-probe", payload, script_path=__file__)
builder.add_assertion("x_holds", computed="0", expected="1", tolerance="0",
                      unit="boolean", source="my_probe")
out = builder.save()
```

Pass `computed`/`expected`/`tolerance` as **strings** — that is the drained
convention (`qou-t0rf`) and keeps the values out of float64.

## Also worth doing (cheap, high leverage)

`wrap_legacy` should not swallow these keys in silence. Either

1. **raise** on a payload carrying `assertions`/`allPassed` (they are never
   what the caller wants — the caller believes they are being emitted), or
2. **adopt** them: convert payload assertion dicts into `Assertion` records
   rather than dropping them.

(1) is the safer change and would have surfaced all 28 at once. Whichever is
chosen, a regression test should pin it, because the current behaviour is
indistinguishable from working for any producer whose checks happen to pass.

## Next step

Fix `wrap_legacy` first (option 1), then let the resulting failures enumerate
the 28 rather than hand-auditing them. Re-run each and record which witnesses
change `allPassed` — those are the ones that were reporting a false green.
