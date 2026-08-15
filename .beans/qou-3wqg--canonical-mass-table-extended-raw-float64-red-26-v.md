---
# qou-3wqg
title: 'canonical-mass-table-extended: raw-float64 red (26 vs baseline 24) AND the committed witness is truncated to 5 of 7 rows'
status: todo
type: bug
created_at: 2026-08-15T23:00:29Z
updated_at: 2026-08-15T23:00:29Z
---


## Two defects, and the second is the one nobody was looking at

`scripts/precision-gates.sh` is red on `raw-float64` with **two** REGRESSED
witnesses. One is `rho-k-co-casimir-extended` (3 → 4, documented on `qou-mnrd`,
needs a ≥ 24 GiB host). The other is this one, and it had not been attributed:

    canonical-mass-table-extended.witness.json    24 -> 26

Bisected rather than assumed. My first guess was the most recent commit to touch
it, `204c5c4e3` ("regenerate with pyhecke_native") — **wrong**, the count was 26
both before and after it. It goes back to:

    1af7d4b7a   24 raw float64
    708ce844c   26 raw float64      fix(ctype): d_for_ctype broke its own
                                    type contract, on averaged_weighted [qou-gscs]

`708ce844c` restructured the table (row 0 went from the deuteron to the proton),
row 4 gained `err_*` fields it previously lacked, and two rows lost
`B_AME_MeV`. Net +2, and the baseline was never updated.

### The second defect: the committed witness is TRUNCATED

Regenerating gives **7 rows where the committed file has 5**, and 1524 leaves
against 588. The producer's own ORDERING INVARIANT comment documents indices
0–7, naming index 5 as ⁴He and index 6 as ⁵Li — **neither of which is in the
committed witness**. So the published table stops at ³He while claiming a
layout that runs to ⁶Li.

`content/values/registry.ts` reads `data.rows.2.B_AME_MeV` (the deuteron), which
survives at index 2 either way — so the truncation is invisible to the one
consumer that pins an index. Same shape as `atom-level-wedderburn-tower`
(`results: {}`) on bean `qou-j6gb`: a truncated witness that no gate flags,
because shrinkage only trips the shape guard when something REGENERATES it.

### DO NOT fix this by stringifying — I nearly did

The tempting fix is to serialize `err_MeV` / `err_pct` / `err_ppb` / `err_ppm`
as strings. It works: 26 → 8 raw float64, comfortably under the baseline, and
`atlas_render_canonical_table._fmt_number` already coerces strings so only one
raw-arithmetic site (`err_ppm * 1000.0`, line 135) needs a `float()`.

**It is also exactly what the audit forbids** — *"Carry mpmath.mpf from the
source and serialize with `_precision.fmt`; do NOT stringify the float."* I
implemented it, then checked whether the values actually carry more than a float
before committing:

    prediction_MeV_50dps = "2.2488207948647343"     18 chars — a FLOAT
    err_MeV              = "0.024254594864734358"

The field is named `50dps` and holds float64. Stringifying would have moved 20
fields out of the ratchet's count while preserving exactly zero extra digits —
a green gate and no more precision than before. Reverted.

### Where the precision is actually lost

Two places, both upstream of the serialization:

    canonical_mass_table_extended.py:80-85
        (1, 1): float(AME_B_DEUTERON_MEV_VALIDATION),   # and T, ³He, ⁴He, ⁶Li

`AME_B_DEUTERON_MEV_VALIDATION` is an **mpf** in `codata_constants`; the
producer casts it to float on the way into `B_AME_MEV`. And:

    lookup_b_pred_existing(...) -> tuple[float | None, str | None]

`pred` is a float by declared type, sourced from `mass-table-ppb.witness.json`.
So `err = pred - ref` cannot carry more than float64 no matter what the
serialization does.

**A real fix is therefore: drop the `float()` casts on the AME constants, carry
`pred` as mpf through `lookup_b_pred_existing` and its upstream witness, then
serialize with `fmt`.** That is a multi-file change through another arc's
prediction path, not a producer tweak — which is why it is a bean and not a
commit.

### Suggested order

  1. Decide whether the 5-row truncation is intended. If not, regenerating
     restores ⁴He and ⁵Li — but on its own that takes the ratchet from 26 to a
     larger number, because more rows means more `err_*` fields.
  2. Then the precision port above, which removes them properly.
  3. Only then update the baseline, downward.

Doing (1) before (2) leaves the gate redder than it is now, which is probably
why it has sat.
