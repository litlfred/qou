---
# qou-4jut
title: 'c-knot-nonuniversal-pinned-weight.witness.json is STALE at HEAD: re-running moves spread_factor 2.83 -> 59.1 and 4He C_knot 9.31 -> 290.01; scriptHash fcc009c4ce2802cd != sha256(HEAD script) 32fdfcc3ed1c4342'
status: completed
type: task
priority: normal
created_at: 2026-08-11T01:00:14Z
updated_at: 2026-08-15T22:31:55Z
---

RESOLVED. Verified at main 08b6ff7e7d on the reorientation pass:
  sha256(computations/deltalambda/c_knot_nonuniversal_pinned_weight_probe.py)[:16]
    = 3899526a0efb3242
  witness.scriptHash
    = 3899526a0efb3242   -> MATCH
The convention-D refresh landed with PR #4961 (da1b269949); every verdict in the
witness survived and sharpened. Staleness gone.
