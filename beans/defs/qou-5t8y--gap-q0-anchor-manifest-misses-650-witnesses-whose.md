---
# qou-5t8y
title: 'GAP: q0_anchor_manifest misses 650 witnesses whose producer filename is SUFFIXED (_probe/_derivation/_test) — _producer_stem matches the witness stem exactly, so fbor-normalisation-barsymmetry.witness.json never finds fbor_normalisation_barsymmetry_probe.py. Fix must re-key the manifest on the PRODUCER filename (q_parameter matches Path(sys.argv[0]).stem), and needs a disambiguation policy: a prefix match is ambiguous (stem ''foo'' would match ''foo_bar_probe.py'').'
status: todo
type: task
priority: normal
created_at: 2026-08-23T14:46:06Z
updated_at: 2026-08-23T14:46:48Z
---

## Measured (PR #5550, 2026-08-23)

Over every committed `computations/**/*.witness.json`:

| | count |
|---|---|
| witness stem == producer filename (found today) | 1744 |
| **suffixed producer exists, MISSED** | **650** |
| no matching producer at all | 643 |

Worked example: `fbor-normalisation-barsymmetry.witness.json` is produced by
`fbor_normalisation_barsymmetry_probe.py`. `_producer_stem` tries only
`fbor_normalisation_barsymmetry` / `fbor-normalisation-barsymmetry`, so the
producer is never found and cannot enter the manifest.

## Why this is not a one-line fix

1. **A prefix match is ambiguous.** Stem `foo` matches `foo_bar_probe.py` even
   when `foo` and `foo_bar` are different computations. Needs a policy —
   an explicit suffix allow-list (`_probe`, `_derivation`, `_test`, …), a
   uniqueness requirement, or a producer-declared witness name.
2. **The manifest key must equal `Path(sys.argv[0]).stem`.** `q_parameter`
   auto-selects by the *running script's* filename stem, so the fix has to
   re-key the manifest on the **producer filename**, not the witness stem.
   Today the two coincide only because the lookup demands it.

## Relation to the other two blind spots (both fixed in #5550)

1. `_producer_stem` was root-only ⇒ 700 live witnesses invisible. Fixed;
   `ideal_muon` 3 → 111.
2. `build()` stamps only when already manifest-declared, and the manifest is
   built from serialized q₀ ⇒ a self-reinforcing loop. Fixed producer-side for
   the three witnesses of `qou-khmj`.
3. **This one.** Independent of both, and the reason those three still do not
   appear in the manifest even though they now stamp correctly.

## Severity — bounded, one-directional

`q_parameter` resolves an unlisted stem to **proton** (standing default, owner
directive 2026-08-07). So a suffixed producer that wants proton is correct by
accident; one that wants muon is silently given proton **and cannot be listed
as muon at all**. Same shape as blind spot 1, which hid 108 such producers.
