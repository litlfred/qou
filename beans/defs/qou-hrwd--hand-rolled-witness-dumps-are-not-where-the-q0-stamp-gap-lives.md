---
# qou-hrwd
title: Hand-rolled witness dumps are a real class (280 producers) but NOT where the q0Anchor gap lives — the canonical serializer misses 1,158
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-29T16:30:00Z
updated_at: 2026-10-04T15:20:42Z
parent: qou-5vkl
---

Raised by the `qou-p77d` sibling (#5996) as a coordination comment on
#6017:

> "two producers write their witness through a hand-rolled
> `json.dump(witness, f, indent=2)` instead of `WitnessBuilder` … They
> stamp provenance by calling `_WB.stamp_staleness_metadata` directly, so
> they *look* stamped, but they bypass the canonical serializer … If you
> are auditing for unstamped or oddly-stamped witnesses, hand-rolled dumps
> are a class worth grepping for."

Good tip, and the class is real — but **measured, it is not the
discriminator for stamping**, and using it as the audit lens would find
about a tenth of the gap.

## Measured on `main`

    hand-rolled json.dump(witness, ...) producers   283
      ...that ALSO use WitnessBuilder.save            3
      ...hand-rolled ONLY                           280

    witnesses by producer style, q0Anchor present?

      canonical (WitnessBuilder.save)   891 yes / 1,158 NO   -> 56.5 % missing
      hand-rolled only                   80 yes /   159 NO   -> 66.5 % missing
      other / unresolved                160 yes /   271 NO   -> 62.9 % missing

**The class is 280, not 2** — the sibling named the two they happened to
hit. So the grep is worth having.

**But hand-rolled is only ~10 points worse than canonical**, and the
canonical bucket holds **1,158** of the 1,588 missing stamps — 7× the
entire hand-rolled bucket. An audit keyed on `json.dump(witness` would
surface 159 of 1,588, i.e. **10 %**, and would report the other 90 % as
clean because they went through the approved serializer.

## What this means

- **Do not use the serializer style as a stamping proxy.** Going through
  `WitnessBuilder.save` does not imply a `q0Anchor`; `save()` stamps what
  the producer passes it, and most producers pass nothing.
- The refill ratchet's 1,627 unstamped witnesses are therefore *mostly a
  canonical-path population*, which is the opposite of where a
  "bypasses the serializer" framing would send you looking.
- The hand-rolled class is still worth draining on its own merits
  (consistency, `mpf` serialization — the sibling hit
  `TypeError: Object of type mpf is not JSON serializable` in exactly
  such a producer). It is just a different problem from the stamp gap.

## Not done here

No producer was changed. #6017 fixes the two witnesses that took the two
q0 gates red; this is a corpus-wide observation surfaced on that PR and
recorded so the tip is not lost — and so the tempting inference from it
is not made.
