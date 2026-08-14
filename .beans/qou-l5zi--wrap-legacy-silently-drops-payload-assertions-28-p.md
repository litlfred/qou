---
# qou-l5zi
title: wrap_legacy silently drops payload assertions -> 28 producers emit allPassed:true vacuously
status: completed
type: task
priority: high
created_at: 2026-08-14T19:10:00Z
updated_at: 2026-08-14T20:03:32Z
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
| witnesses corpus-wide with `allPassed: true` and zero assertions | 389 of 2083 |

### ⚠ CORRECTION — the 389 is NOT this bug's blast radius

The first version of this bean led with "389 of 2083 (19 %)" as the damage.
**That was an overstatement**, and re-running all 28 producers against the fix
settles it: the corpus count moved **389 → 389**. So the 389 are overwhelmingly
producers that legitimately register no assertions, not victims of the drop.

The real committed blast radius, measured after the fix landed:

| | |
|---|---|
| witnesses that recovered assertions | **6** (+17 assertions) |
| `allPassed` verdicts that FLIPPED true → false | **0** |

```
 0 ->  6   delta-q-decoration
 0 ->  3   rho-k-h3a-counit-canonical-integral
 0 ->  2   qbeta/qbeta-h4-gram-barchannel-split
 0 ->  2   rho-k-counit-defect-form
 0 ->  2   rho-k-counit-isotope-systematics
 0 ->  2   rho-k-counit-vortex-writhe
```

**No committed producer was hiding a genuine failure.** The evidence was
invisible; the verdicts were right. The one case where the drop *did* mask a
real failure was this session's own new probe
(`ak_lp_dual_quotient_probe`) — its headline check was `false` and the first
witness it wrote claimed `allPassed: true`. That is what makes the bug real; it
is not what the committed corpus was suffering from.

Mechanism proven end-to-end on `rho_k_counit_vortex_writhe_probe.py`: the
source built 2 assertions and the committed witness carried
`assertions: 0, allPassed: true`. It now carries both (and still passes).

## Why it matters more than a formatting bug

Same failure shape as `qou-9d6h` (D3), where
`deuteron_tower_fusion_frame_probe` wrote `allPassed: False` and then exited 0,
so the cascade filed it as `ok`. Here it is worse in kind: the witness itself
asserts success. Anything gating on `allPassed` — dashboards, the integration
watchers, a reader skimming a witness — reads a value that was never computed.

Worth keeping the severity honest, though: *in kind* worse, **not** in measured
damage. See the correction above — 0 committed verdicts were wrong.

## The fix — adopted, not raised

`wrap_legacy` now ADOPTS payload assertions instead of skipping them
(`_assertion_from_mapping`), so all 28 producers are correct with **zero
producer edits**.

Adoption beat the raise-and-enumerate plan this bean originally proposed:
the producer's verdict was never wrong, it was discarded, so converting it is a
faithful reading of what the caller asked for — and it avoids a flag day where
28 producers are broken until each is hand-edited.

Rules, pinned by `tools/qou-substrate/tests/test_wrap_legacy_assertions.py`
(13 tests):

* `{"name", "passed"}` (11 sites) — no numeric pair; the producer's predicate
  IS the check, so it becomes `passed_override`.
* An explicit `passed` **always beats** a derivable `computed`/`expected`
  comparison. Adoption must not silently re-decide a stated verdict — that
  would be a different bug from the one being fixed.
* No `passed` — derived the normal way from computed/expected/tolerance.
* Extra keys (`detail`, `manifold`, `particle`) ride along in `extra`, so
  adoption is lossless, and cannot shadow a schema key.
* No `assertions` key, or an empty list — unchanged, still vacuously true.

## Still open

The ~383 other vacuous-true witnesses are a **separate question**, not this
bug. Worth a look on its own terms: a witness with `allPassed: true` and no
assertions is asserting nothing, whoever wrote it. Whether that is fine
(genuinely check-free producers) or a second gap needs its own pass — do not
inherit the 389 figure into it as though it were established damage.
