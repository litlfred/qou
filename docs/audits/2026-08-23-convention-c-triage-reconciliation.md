# Two independent convention-C triages, reconciled — the union is 3 live-C producers, not 2

**Date:** 2026-08-23
**Beans:** `qou-z11r` (the triage), `qou-q7lf` (the `hadron_knot_table` crash)
**Reconciles:** [`2026-08-23-convention-c-witness-triage.md`](2026-08-23-convention-c-witness-triage.md) (landed on `main` via #5510) against a second, independent triage run in a takeover session (#5543)
**Second detector:** [`computations/audits/convention_c_witness_triage.py`](../../computations/audits/convention_c_witness_triage.py)

## Why there are two

Two sessions triaged the same 58 committed convention-C witnesses in parallel. The first landed on `main` while the second was mid-run; the second was written against a `main` that did not yet contain it (verified: the doc is **absent** at `b4f9e350e9`, the branch point, and arrived in a later batch of 36 commits).

Under the AGENTS.md measured-research-overlap rule this is the permitted kind of duplication, and it paid the dividend that rule predicts: **each detector found a live convention-C producer the other missed, and the blind spots were different.**

## The disagreement

| | landed triage (#5510) | second triage (#5543) |
|---|---|---|
| `hecke_channel_binding_probe.py` | **LIVE-C** ✓ | missed |
| `signed_crossing_feasibility_probe.py` | **LIVE-C** ✓ | missed |
| `mass-from-q-symbolic.py` | missed (`"producer": null`) | **LIVE-C** ✓ |
| **live-C total** | 2 | 1 (3 after the fix below) |

**The union is 3.** Neither run alone had it.

### Blind spot 1 — producer resolution returned null

The landed triage's JSON twin records, for `computations/mass-from-q-symbolic.witness.json`:

```json
{ "witness": "computations/mass-from-q-symbolic.witness.json",
  "producer": null, "n_fields": 1 }
```

With no producer resolved there is no source to scan, so the file could never be classified live-C regardless of what it contains. The witness was seen; the code behind it never was. (The hyphenated stem `mass-from-q-symbolic.py` is the likely cause — it is not the underscore convention the resolver expects.)

### Blind spot 2 — a case-sensitive character class

The second triage's closed-form pattern was `sqrt\(\s*q\w*\s*\)\s*/\s*\(\s*q\w*\s*\+\s*1\s*\)`. Both probes spell z_C as

```python
z = mp.sqrt(Q0) / (Q0 + 1)          # convention C, in plain sight
```

and `Q0` does not match `q\w*`. The pattern was **correct in shape and wrong in case**, which is the least visible way for a detector to fail: it reports a clean scan of a file it did read. Fixed to `[qQ]\w*`; re-run now returns all three.

That makes **two more entries for the detector-blindness taxonomy** — and both were found not by a better detector but by a second one disagreeing. Neither is a new *spelling*: the two probes use a spelling the landed detector already handles, and `mass-from-q-symbolic` uses one the second detector already handles. The failures were in resolution and in case, one layer below the spelling.

## What only the second run found: `mass-from-q-symbolic.py` is a double defect

Lines 314 and 424:

```python
1.0 / (Q0**0.5 + Q_INV0**0.5)      # = 1/(√q + 1/√q) = z_C
```

1. **Convention C**, live, on a path that serialises the value (`w.add_parameter("z_markov", …)` at 424).
2. **float64.** `**0.5` rather than `mp.sqrt`, with a `1.0` literal numerator — float arithmetic end to end, being written into a witness. Per the 2026-08-18 NO-FLOAT64 directive this is a defect independently of the convention.

Migrating the convention without fixing the arithmetic leaves the second defect on the same line.

## What only the landed run found: a durable refutation is C-conditional

`signed_crossing_feasibility_probe` emits `"verdict": "signed-ILP-pure-chirality-refuted"`, computed with convention-C `z` at a muon-pinned `Q0` and never re-derived under D. The landed triage is right that this must be treated as **C-conditional**, and right that a `z_D` substitution is not a valid repair — `QOU.QBeta.decayLadder_zC_threeRow_ne_zero` makes the swap invalid, so it needs a re-derivation, which is research rather than cleanup.

The second run classified that probe as `unresolved` and would not have caught the refutation's status at all.

## The anchor-witness contamination claim — no instance found

The framing carried into the takeover session was:

> `q-pinning-50-digit.witness.json` … itself carries `derived_50_digit.z_markov = 0.49932…`, i.e. convention C. **Anything reading that field inherits C regardless of its own source.**

First half **true**. Second half has **no instance**:

- `grep '\["z_markov"\]' / '.get("z_markov"'` across live `.py` → **zero reads**.
- Every reader of that block takes `["derived_50_digit"]["q"]`.
- The only reader binding the whole dict, `q_parameter.py:111`, uses `_d["q"]` alone and says so: *"Take ONLY q from the witness."*

The field is **inert** — the anchor advertises a convention it does not supply. That is a provenance defect, not a live contamination path, and not the root cause of the 58. It matters for sequencing: had it been live, nothing downstream could be fixed before it.

**Do not repair it by re-pinning.** AGENTS.md rule 1 — that file is anchor-*defining*; re-pinning redefines what "muon" means corpus-wide (262 `Q0_FLIP`s, measured). Removing an unread field is a smaller operation, but it still touches the anchor file, so it is flagged rather than done.

## Unreconciled

- **z_D witness count: 4 (landed) vs 3 (second run).** Not chased. Likely a scan-scope difference (`_deprecated`, or a wider glob), but that is a guess and is recorded as a guess.
- **The 32 `unresolved` in the second run** share one shape — producer byte-identical to when it emitted C, yet carrying no C spelling. For a self-contained producer both cannot hold, so the C came from a **dependency**: the import-cone drift class. One query, not 32; deliberately not chased here.

## A correction to the takeover session's own reporting

That session reported that `qou-z11r` and `qou-q7lf` "were never created", having measured `beans show` returning not-found for both. That was **true when measured and is now superseded** — both beans exist on `main`, created in the work that landed after the measurement. Its own `qou-9bfp` and `qou-xram` are therefore duplicates and are scrapped in favour of the canonical pair.
