---
# qou-uujo
title: 'orbit_reduction_crosscheck is RED on main: its 4He smoke pin 0.05534833 predates the ordering ruling and its witness (2026-05-30) still claims allPassed'
status: todo
type: task
created_at: 2026-09-14T18:38:47Z
updated_at: 2026-09-14T18:38:47Z
---

## Measured, on a CLEAN tree

Found while draining `atom_orbit_reduction` under `qou-t29k`. Verified by
stashing my own edits and re-running, so this is not from that work:

    N1 ³He |orbit|-guard: via=0.0585962536544363 direct=0.0585962536544363
                          Δ=0.0e+00  [✓]
    N2 ⁴He value smoke:   tr_M=0.011237417659767421
                          (pin 0.0553483351637685668, Δ=4.4e-02)  [✗]
    TIER 1.B ORBIT-REDUCTION CROSS-CHECK: FAIL

The committed witness says **`allPassed: True`, `computedAt` 2026-05-30** —
more than three months old and long before the 2026-09-05 intra-ordering ruling
(`qou-hu1f`).

## Why it fails, and why it is NOT the qou-t29k defect

`tr_M_via_orbit_representative` goes through `atom_braid_orbit_representative`,
which **delegates to the production `atom_braid_word_3A`** — so this path was
always canonical and moved on 2026-09-05 when that builder's default did. The
value it now returns, `0.011237417659767421`, is exactly the canonical ⁴He
constant `0.011237417659767421564199549374410…`, which I confirmed
independently the same session by regenerating the ⁴He binding cache.

So the CODE is right and the PIN is stale. Note the pin is not the grouped
value either: grouped ⁴He is `0.160974145442407…`, and `0.0553483351637685668`
is neither — it is from some earlier state again, so re-pinning wants the
provenance of that number checked rather than just overwriting it with today's.

## Deliberately not fixed here

Re-pinning a smoke test is a one-line change and I did not make it, because the
right value depends on what `N2` is for. Its own source calls it "⁴He value
smoke @50dps vs post-re-pin canonical" — if the point is "this equals the
canonical ⁴He trace", the pin should be the canonical constant and the
tolerance 1e-40 like its sibling `N1`, not 1e-6. That is a decision about the
test, not a number to swap. Also left the witness at its committed state rather
than regenerating a FAIL into the repo: I was not otherwise editing this file,
and flipping someone else's witness in a drive-by is a bigger statement than
recording the finding.

## Third of its kind

After `qou-g5oz` (`qbeta_level_k_binding_operator_probe`, red since the ruling,
witness two days pre-ruling claiming all-pass) and the pre-existing crash in
`canonical_ordering_dof_probe` Part 6 (`TypeError: cannot create mpf from None`,
also reproduced on a clean tree; Part 6 is already tracked as blocked by
`qou-xy5f`). The pattern worth naming: **the ordering ruling left a tail of
probes whose witnesses still claim all-pass**, and nothing re-ran them. Each was
found by working an unrelated site next to it, not by a sweep.
