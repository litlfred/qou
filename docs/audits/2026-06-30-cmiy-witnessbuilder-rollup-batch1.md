# cmiy WitnessBuilder rollup — batch 1 + migration gotchas

**Date:** 2026-06-30
**Bean:** `cmiy` (canonical-watcher · P30 WitnessBuilder rollup) — stays **open** (multi-batch).
**Symptom audit:** `computations/audits/witness_provenance_audit.py` (I14) — PROV_MISSING witnesses lack `engine`/`scriptFile`/`commitSha`. Baseline this batch: **280 → 279**.

## Batch 1 (this PR)

`meson_vol_density.py` → routed off raw `json.dump` onto the WitnessBuilder
provenance path. Verified: PROV_OK, **all original keys preserved**, **2
assertions preserved**, data values refreshed (see q0 note below). The witness
has **0 consumers** (no content block / script reads it), so the refresh is safe.

Only 1 script this batch — not for lack of candidates (≈30 raw-emit scripts,
279 PROV_MISSING witnesses) but because the migration is **not mechanical**.
Three gotchas surfaced that the next batch must handle per-script:

## Gotcha 1 — `wrap_legacy` DROPS flat `assertions` / `allPassed`

`WitnessBuilder.wrap_legacy(name, payload, …)` routes "reserved" keys
(`_RESERVED_LEGACY_KEYS`) to structured slots and **recomputes them from the
builder**. Since a legacy script builds its `assertions` list *in the payload*
(not via `builder.add_assertion`), wrap_legacy emits `assertions: []` —
**silent data loss**. (Caught here: meson's 2 assertions vanished under
wrap_legacy.)

**Rule:** if the payload contains a flat `assertions`/`allPassed`, do **not**
use `wrap_legacy`. Use `WitnessBuilder.stamp_staleness_metadata(payload,
script_path=__file__, engine=…)` — it adds provenance *in place* and drops
nothing — then set `payload["scriptFile"] = Path(__file__).name` (stamp omits
`scriptFile`) and keep the script's own `json.dump`. wrap_legacy is only safe
for assertion-free payloads.

## Gotcha 2 — regen refreshes STALE data (e.g. q0)

Several committed witnesses were generated with an **older q0**
(`1.1099785955541805…`) and the producer now emits the canonical muon-q₀
(`1.10997859555733471…`). Re-running to add provenance therefore **also
refreshes the numbers** (correct — the committed witness was stale). So a P30
migration is not "provenance-only"; it is a full regen. Only convert scripts
whose witness has no consumers (or update consumers), and run in the canonical
env — `pyhecke_native`-dependent producers will engine-skew in an ad-hoc env
and must wait for a canonical-env batch.

## Gotcha 3 — some raw-emit scripts are pre-existing CRASHES

`magic_A_formula.py` crashes on `main` (multiple `{mpf:.10f}` format prints —
`M_E_MEV`/`VOL_BORROMEAN`/`CATALAN_G` are mpmath `mpf`, not float). Its
committed witness predates the breakage. Such scripts need a **separate
format-bug fix** before they can be migrated; do not fold that into a P30 batch.

## Next-batch recipe

1. Pick a small cluster of **pure-Python, zero-consumer** raw-emit scripts that
   **run cleanly** (`python3 <script>` exit 0).
2. Payload has flat `assertions`? → `stamp_staleness_metadata` + `scriptFile`.
   Else → `wrap_legacy(...).save()`.
3. Verify per script: PROV_OK, original keys ⊆ new keys, assertions preserved,
   non-meta data diffs are only intended refreshes.
4. Re-run `witness_provenance_audit.py`; PROV_MISSING must drop by the batch size.
