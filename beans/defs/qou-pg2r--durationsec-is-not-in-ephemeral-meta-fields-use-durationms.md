---
# qou-pg2r
title: durationSec is NOT in _EPHEMERAL_META_FIELDS — serializing seconds makes wall-clock substantive witness content
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-15T21:11:00Z
updated_at: 2026-10-04T15:12:26Z
parent: qou-5vkl
---

## The trap

`_EPHEMERAL_META_FIELDS`
(`tools/qou-substrate/python/qou_substrate/witness.py:1291`) contains
**`durationMs`** and **not** `durationSec`.

A producer that records its wall-clock as `durationSec` — especially
serialized as a *string* to dodge the raw-float64 ratchet — makes that field
**substantive witness content**. Every subsequent re-run then reports drift on
a meaningless timing number, so a genuinely-unchanged recomputation looks
stale.

The two spellings look interchangeable. Only one is masked.

## Evidence

Corpus agrees strongly with `durationMs`: **55 uses vs 2**.

Discovered when `main` and PR #5123 **independently** drained the same float64
duration leak in the #5107 probe — `main` as `durationMs`, the branch as
`durationSec`. Main's form is the correct one; the branch commit was dropped as
superseded on rebase. The branch's *own new* probe had copied the bad form and
was fixed in #5123.

Proof the fix works: consecutive no-op re-runs of the corrected probe now
differ **only** in `computedAt` / `commitSha` / `durationMs` — all masked.

## What to do

1. Grep `computations/` for `durationSec` and confirm the current count (do not
   trust the 2 above — it is a measurement from 2026-08-15, and per the
   repo's own "importer counts are measured, not maintained" note, a
   hand-carried number decays).
2. Convert each to `durationMs`, carried as an integer of milliseconds.
3. Re-run each producer and confirm consecutive no-op runs differ only in
   masked fields.
4. Consider whether `durationSec` should simply be **added** to
   `_EPHEMERAL_META_FIELDS` as a belt-and-braces measure — cheaper than
   policing every future producer, though converting to the canonical spelling
   is still preferable.

## Provenance

Surfaced by the `/prepare-merge-auto` pipeline for PR #5123 (bean
`qou-kc21im`), during a convergent-fix conflict resolution.

---

## 2026-08-15 (later) — the field name in this bean is wrong, and it matters

Worked the item. Both the count *and the field name* above are wrong, and the
name being wrong is not cosmetic: it would have made the recommended fix a
**silent no-op**.

### There is no `durationSec` in this corpus

Measured with exact-key greps (`grep -rl '"<key>"' --include=*.json .`):

| key | JSON files |
|---|---|
| `durationSec` | **0** |
| `durationSeconds` | 3 |
| `duration_sec` | 2 |
| `durationMs` | 2423 |
| `elapsed_seconds` | 61 *(already masked)* |
| `elapsed_sec` | 20 *(already masked)* |

So "**55 uses vs 2**" decayed exactly as this bean predicted it would — the
real ratio is 2423 vs 5, split across **two** seconds spellings, neither of
which is the one named here.

The misspelling is traceable. `computations/qbeta/qbeta_kc21_parity_convention_immunity_probe.py:480`
explains the trap in prose — *"A `durationSec` is therefore compared as
SUBSTANTIVE content"* — and this bean took the shorthand from that comment
rather than from an emitted key. The probe itself is correct; it emits
`durationMs`.

**Why the name is load-bearing:** `_strip_ephemeral_fields` masks by
**exact dict-key match**, applied recursively at any depth
(`if k not in _EPHEMERAL_META_FIELDS`). Not prefix, not suffix, not
normalized. Adding the string `"durationSec"` would therefore have matched
nothing at all, closed the bean, and left the actual keys unmasked.

### Deeper finding: the affected witnesses never reach the mask

The three `durationSeconds` witnesses are produced by
`qbeta_nz_even_series_fourone_probe.py`, `qbeta_sdeformed_leading_bound_probe.py`
and `sdeformed_channel_signflip_probe.py` — **all three write with plain
`json.dump` / `Path.write_text`**, never `WitnessBuilder.save()`.
`_witnesses_substantively_equal` is called in only three places
(`witness.py:1267`, `computations/audits/e0_calibration_audit.py:303`,
`computations/cross_check_trM_1ppb.py:447`), none of which these probes touch.

So even **correctly spelled**, the mask changes the behaviour of zero existing
witnesses. Their re-run churn has a different cause — they overwrite
unconditionally, with no preserve-if-unchanged path to consult a mask at all.
Renaming their field to `durationMs` would **not** stop that churn either;
only routing them through `WitnessBuilder` would.

That reframes the fix: masking is **future-proofing** for any producer that
does use `WitnessBuilder`, not a repair of a live drift. Worth doing — it is
one line and it removes a real trap — but it should not be described as fixing
the three probes.

### What was done

Chose the mask fix with the **corrected spellings**: added `durationSeconds`
and `duration_sec` to `_EPHEMERAL_META_FIELDS`, mirrored the names into
`test_ephemeral_mask_contains_required_fields`, and recorded the
no-`durationSec` finding in the comment block so the next reader measures
before adding a third spelling. Both mirrors
(`qou-mass/src/qou_mass/_internal/witness_base.py`,
`computations/substrate/witness_base.py`) are re-export shims over the
canonical set, so the one edit propagates; `test_ephemeral_mask_sync` passes.

Deliberately **not** done — steps 2 and 3 above (convert producers to
`durationMs` + re-run):

- For the three probes it would fix nothing the mask does not already cover,
  since they bypass the mask.
- It would rewrite three witnesses purely to change a timing field's spelling,
  which is the re-run this bean's own discipline warns against.

`duration_sec` is worth calling out separately: in
`computations/m-tau-complex-volume-search.witness.json` it is serialized as
the **string** `"1.728"` — precisely the "seconds-as-a-string dodges the
raw-float64 ratchet" workaround the kc21 comment describes. It is now masked,
so the dodge no longer costs a false drift.

### Still open

Routing the three plain-`json.dump` probes through `WitnessBuilder` so they
gain the preserve-if-unchanged path. That is the fix that would actually end
their churn, and it is a different (larger) change than this bean's title
suggests.


--------

## 2026-08-16 — the "Still open" item, restated so it is findable

A backlog item arrived phrased as a fresh task — *"Route the three
plain-json.dump probes through WitnessBuilder"* — and it is **already this
bean's `## Still open` paragraph**, so it is recorded here rather than
filed as a second bean. Restating it under its own heading because a work
item buried at the bottom of a bean titled about `durationSec` masking is
not findable by anyone grepping for `json.dump` or `WitnessBuilder`.

### The item

    computations/probes/qbeta_nz_even_series_fourone_probe.py
    computations/probes/qbeta_sdeformed_leading_bound_probe.py
    computations/probes/sdeformed_channel_signflip_probe.py

(all three confirmed present under `computations/probes/` at merge
`36080a4e21`)

write with plain `json.dump` / `Path.write_text` and never call
`WitnessBuilder.save()`. They therefore never reach
`_witnesses_substantively_equal` and **overwrite unconditionally**. Routing
them through `WitnessBuilder` — so they gain the preserve-if-unchanged path
— is the fix that actually ends their re-run churn.

### What the mask fix did and did not do

Settled above and restated so it is not re-litigated: adding
`durationSeconds` / `duration_sec` to `_EPHEMERAL_META_FIELDS` was
**future-proofing** for producers that *do* use `WitnessBuilder`. It changes
the behaviour of **zero** existing witnesses, because these three bypass the
mask entirely. Worth having; not a repair of these probes.

### Cross-reference — `qou-pin5` is the general case

`qou-pin5` measured **436 producers** writing witnesses via raw `json.dump`,
of which **14 pinned witnesses are one rerun away** from losing their
`q0Anchor`. These three probes are three of those 436, seen from the
churn side rather than the pin-loss side. **Same root cause, one fix.**

Do not work this item and `qou-pin5` independently — whoever routes these
three through `WitnessBuilder` should say whether the same move generalises
to the other 433, and `qou-pin5` now carries a pointer back here.

*(Routed 2026-08-16 by an agent that could not reach the `beans` CLI.)*



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-08-16 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.
