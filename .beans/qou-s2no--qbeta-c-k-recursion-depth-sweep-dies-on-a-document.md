---
# qou-s2no
title: qbeta_c_k_recursion_depth_sweep dies on a documented upstream contract it does not read
status: in-progress
type: bug
priority: normal
created_at: 2026-08-30T14:26:08Z
updated_at: 2026-08-30T14:26:08Z
---

Found while working `qou-0hnz`; diagnosed before filing. Related to `qou-5wuz`
(same witness, different defect: that one is about it recording no `q0Anchor`).

## Not what it looks like

`computations/qbeta/qbeta_c_k_recursion_depth_sweep.py` cannot run:

```
File ".../qbeta_c_k_recursion_depth_sweep.py", line 94, in load_c_k
    return {int(k.split("_")[1]): mp.mpf(v) for k, v in raw.items()}
TypeError: cannot create mpf from None
```

The obvious reading is "the upstream is corrupt". It is not. **The upstream is
correct and the nulls are deliberate.**
`computations/qbeta/qbeta-decay-sdp-extended-ck.witness.json` records

    c_k_extracted_50dps          9 entries, ALL null
    c_k_extracted_float          9 entries, ALL null
    c_k_unresolved_raw_quotient  9 entries, NONE null
    c_k_resolution.last_resolved_rung   None
    c_k_resolution.n_unresolved         9
    c_k_resolution.why_unresolved_rungs_are_null   <prose explaining exactly this>

and its producer says so at the write site: *"Unresolved rungs are now null; the
raw quotient is preserved separately under an unmistakable key so the record is
complete without being consumable."* `_settle_resolution` marked every rung
unresolved (the residual never drops by the required ~1/u factor), so the
producer refuses to publish values that would be misread as extractions.

## The actual defect

`load_c_k` reads `c_k_extracted_50dps` and calls `mp.mpf(v)` with no None check,
so a deliberate, documented "not extractable" state surfaces as an opaque
mpmath TypeError 60 lines away from the thing that explains it.

## Todo

- [x] Make `load_c_k` honour the contract: skip nulls, and if nothing is
      resolvable fail with a message naming the upstream's own explanation.
- [x] Do NOT invent values or read `c_k_unresolved_raw_quotient` as a
      substitute — the upstream deliberately made it non-consumable. Not done,
      and the docstring says why so the next reader is not tempted.


## Summary of Changes

`load_c_k` now filters nulls and, when nothing is resolvable, raises a
`SystemExit` that names the upstream's own explanation instead of letting
mpmath throw. Verified by calling it directly under a write guard:

```
no resolvable c_k in qbeta-decay-sdp-extended-ck.witness.json: all 9 rungs are
null (last_resolved_rung=None, n_unresolved=9). That witness is not broken --
it deliberately nulls rungs whose residual never drops by the required ~1/u
factor. Its own field c_k_resolution.why_unresolved_rungs_are_null states why.
This sweep needs at least one RESOLVED rung, so re-run
qbeta_decay_sdp_extended_ck.py once the extraction resolves; do not substitute
c_k_unresolved_raw_quotient.
```

**The producer still cannot run**, and that is correct: there is genuinely no
resolved rung to sweep over. What changed is that it now says so, pointing at
the field that explains it, rather than dying on a TypeError that reads like
upstream corruption. Whether the extraction *should* resolve is a separate
question about `_settle_resolution`'s ~1/u threshold, not about this consumer.

No witness regenerated — this producer writes one only on a successful run.
