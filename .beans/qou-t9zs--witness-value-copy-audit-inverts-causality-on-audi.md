---
# qou-t9zs
title: witness_value_copy_audit inverts causality on auditOnly witnesses — 5 of 11 NEW are an audit quoting the source it flagged
status: todo
type: bug
created_at: 2026-09-13T14:22:24Z
updated_at: 2026-09-13T14:22:24Z
---

## The finding

`computations/audits/witness_value_copy_audit.py` reports "this producer typed a
value that lives in a witness — read the witness instead". For a class of its
findings the causality runs the **other way**, and the audit cannot tell.

Measured on the merged tree 2026-09-13: `RATCHET: 210 baselined, 11 NEW`.
**Five of the 11 name `computations/audits/q0-consistency-audit.witness.json`**
as the witness the value was "copied" from. That witness records source
excerpts as evidence:

```json
{"file": "computations/subgoal_1_per_knot_mass_table_probe.py", "line": 62,
 "kind": "stale-trM", "classification": "production-hardcode",
 "text": "(\"D\", 2, 1, 1, mp.mpf(\"4.40083251608\"), M_D_MEV_VALIDATION..."}
```

That is `q0_consistency_audit` **quoting the probe's own source line verbatim**,
because that is what a corpus-scanning audit records. The literal is in the
witness *because it is in the probe*. `witness_value_copy_audit` then sees it in
both and reports the probe as the copier.

## Why it gets worse on its own

Self-reinforcing: every additional hardcode `q0_consistency_audit` finds and
records becomes another false positive here. A gate that grows noise as a
sibling gate does its job will be skipped, which is what
`scripts/precision-gates.sh`'s own header warns about.

## The fix, and why I did not just make it

`auditOnly` is already a first-class field in the witness schema, and
`q0-consistency-audit.witness.json` carries `auditOnly: True`. An audit-only
witness records what it found in the corpus, so **it can never be the origin of
a value a producer should have read instead**. Skipping `auditOnly` witnesses as
copy SOURCES is the principled fix, and `witness_value_copy_audit.py` has no
`auditOnly` handling at all today.

Not done here because of how the baseline is keyed:

```
computations/witness-value-copy-baseline.json -> counts:
  "computations/alpha_em/alpha_em_nonD_index_route_probe.py::1.6625077511098137144": 1
```

`<producer file>::<value>`, **with no record of which witness the value was
found in**. So adding the skip would silently drop baselined entries whose
source was audit-only, and nothing in the baseline could say which. That is
drain-by-exclusion, and it is the third instance of that pattern found in one
day: the `y_lambda` check-D ratchet "drained" 7 entries that were files main had
deleted, and `q0_value_drift_audit` scans `_deprecated/` where every other audit
skips it.

**If the skip is adopted, regenerate the baseline in the same change and say in
the message that the drop is exclusion rather than repair.**

## The other six

Not audit-only, and worth a separate read — several pair a producer with a
witness from an unrelated domain (e.g. `a3_vol_is_pseudovolume…:78` with
`qbeta/dt-d1b-nz-gluing-invariant-entry.witness.json`), which is the signature
of a coincidental value match rather than a copy. Note also that
`4.40083251612` and `4.40083251608` differ in the last two digits and were
matched to different witnesses, so at least some matching is exact rather than
fuzzy.
