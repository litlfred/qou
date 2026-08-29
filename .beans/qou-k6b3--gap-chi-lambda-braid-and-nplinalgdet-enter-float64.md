---
# qou-k6b3
title: 'GAP: chi_lambda_braid and np.linalg.det enter float64 — blocks 2 producers from the proton migration'
status: todo
type: task
priority: normal
created_at: 2026-08-29T09:40:22Z
updated_at: 2026-08-29T09:40:59Z
---

Parent: qou-cds3. Surfaced by the proton migration (PR #5992), which had to
DEFER two producers because of it.

## What is wrong

Two producers compute in float64 and it is not a display cast:

  * computations/chi_lambda_he4_full_partition_table.py:159-160
      chi = pn.chi_lambda_braid(shape, BETA_HE4, q0_f64)
    enters the **f64 Rust kernel**, so every one of the 77 chi values in
    chi-lambda-he4-full-partition-table.witness.json is float64.

  * computations/gram_matrix_seminormal_n.py:190,195
      sigma_k_dets = [float(np.linalg.det(M)) for M in sigma_k_at_q]
      w0_det = float(np.linalg.det(w0_at_q))
    numpy determinants are float64 by construction. Consumed by
    gram_matrix_seminormal_h6.py -> option-e-phase1-gram-h6.witness.json,
    and by any other consumer of that shared module.

## How it surfaced — worth keeping, the mechanism is general

Migrating those two producers to the proton pin turned the raw-float64
ratchet RED:

    chi-lambda-he4-full-partition-table   194 -> 196
    option-e-phase1-gram-h6               130 -> 131

**The migration did not add float64.** Those fields were always float64. At
the MUON pin they evaluated to exactly 1.0, -1.0 and 1.0 — which the ratchet's
integral-valued carve-out does not count — and at the PROTON pin they are
1.000000000000009, -0.9999999999999999 and 0.9999999999999998, which it does.
An anchor change moved three pre-existing float64 results across the
integrality boundary and thereby made them visible.

Generalisation: **the ratchet's integral carve-out hides float64 error
whenever the true value is an integer.** Determinants of ±1, characters that
should be exact counts, any quantity whose exact value is whole — the error is
there at the muon pin too, it just lands on the nose. Do not read a clean
ratchet on such a field as evidence the arithmetic is exact.

## The fix the corpus already names

f64_into_mpmath_audit.py's own test cases state it:

    ("a wrapper call omitting precision= gets the f64 default",
     "c = chi_lambda_braid(shape, word)", "F64_ENGINE_ENTRY"),
    ("passing precision= is the fix, so it is NOT flagged",
     "c = chi_lambda_braid(shape, word, precision='mpfr_50dps')", None),

and computations/hecke/hecke_characters.py:610 provides
`chi_lambda_braid_mpf(shape, signed_word, q_value=None, dps=None)` returning
an mpmath.mpf directly. For the determinants, an mpmath det over the exact
seminormal matrices replaces np.linalg.det.

## Why it was NOT done in PR #5992

It changes the COMPUTE PATH, so every value in both witnesses moves — not just
the three at the boundary. That is a larger and scientifically different change
than an anchor re-pin, and mixing it into the migration diff would make the
migration unreviewable. gram_matrix_seminormal_n.py is also SHARED, so the
determinant fix reaches consumers beyond the H6 producer and needs its own
blast-radius check.

## What unblocks when this lands

chi_lambda_he4_full_partition_table and gram_matrix_seminormal_h6 can then
migrate to physical_proton, completing the direct-reader set (18 of 20 landed
in #5992).

Downstream care: chi_lambda_he4_full_partition_table sorts and takes ratios on
`abs_chi` (lines 185-192) and prints with `:>+18.6f`, so an mpf conversion must
keep a sortable numeric internally and serialize with `_precision.fmt` at write
time rather than casting at the point of use.
