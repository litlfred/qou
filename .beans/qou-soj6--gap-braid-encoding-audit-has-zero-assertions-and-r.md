---
# qou-soj6
title: 'GAP: braid_encoding_audit has ZERO assertions and reports allPassed=true'
status: todo
type: task
priority: normal
created_at: 2026-08-30T15:12:00Z
updated_at: 2026-08-30T15:12:48Z
---

`computations/audits/braid_encoding_audit.py` runs to **exit 0** and writes a
witness with **zero assertions** and **`allPassed: true`** — measured on both the
committed witness and a fresh run. **It cannot fail.** Whatever it audits, it
reports nothing about, and any consumer reading `allPassed` gets a green light.

This is pre-existing and not caused by the missing input — the committed witness
also has 0 assertions — but the missing input compounds it. The audit loads
`atomic-braid-mass-table.witness.json` (deleted 2026-05-19, commit
`7f30a57924d`, owner directive) behind an `.exists()` guard and substitutes

    s3 = ... if s3_path.exists() else {"data": {"rows": []}}

so `s3_rows` is `{}`. Every downstream read is then a `.get(...)` that returns
`None`:

    line 426:  raw = s3_rows.get(key, {}).get("term1_atomic_total")
    line 436:  "strategy_3_tr_M_missing": s3_rows.get("p", {}).get(...)
    line 448:  "strategy_3_tr_M_missing": s3_rows.get("n", {}).get(...)

**So it is an audit with no assertions, running on an empty dataset, reporting
green.** That is the `qou-srvu` vacuous-green shape in its strongest form.

## What is NOT claimed here

That its non-assertion output is wrong. The fresh run and the committed witness
differ **only in provenance** (`scriptCommitSha`, `pyhecke_native_build`,
`engineVersion` mpmath 1.3.0 → 1.4.1) — **no number moved**. Its data is
reproducible; it simply makes no checkable claim.

## The fix is a design question, not a mechanical one

The obvious move — assert the upstream is present — would make it **permanently
red**, since the input was deliberately deleted and cannot come back. So the
real options are:

1. give it assertions over the inputs it *does* have (option-b proton chain,
   Markov-trace assembly), and drop the Strategy-3 arm;
2. retire it with the other legacy consumers (`qou-s1yn`);
3. leave it, and have the vacuous-green ratchet flag it as a known exemption.

Not decided here. Recommendation (judgement): **1** — the audit has two other
live upstreams, so it can be made falsifiable without resurrecting anything.

Found while triaging the six remaining consumers of the removed witness.
