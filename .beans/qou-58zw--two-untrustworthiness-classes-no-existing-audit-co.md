---
# qou-58zw
title: 'Two untrustworthiness classes no existing audit covers: tolerance-below-arithmetic-floor, and producers that SHRANK'
status: todo
type: task
priority: normal
created_at: 2026-08-30T18:12:32Z
updated_at: 2026-08-30T18:13:14Z
---

Found 2026-08-30 answering "which probes are on float or not trustworthy". The
corpus has seven audits for this area and they are good; these two classes fall
between all of them.

## Class 1 — a tolerance BELOW the arithmetic's own floor

`computations/fr_pullback_borromean_h3a_test.py:549,554`:

    computed=float(plancherel_dev), expected=0.0, tolerance=1e-40
    computed=float(stratum_mass_dev), expected=0.0, tolerance=1e-40

`float()` resolves to ~1e-16. **The tolerance is 24 orders of magnitude below
what the arithmetic can represent.** So the assertion has exactly two possible
meanings, and neither is the one it advertises: either the cast value is
*exactly* 0.0 and the test is trivially true while measuring nothing, or it is
nonzero at ~1e-16 and the assertion must fail. It cannot ever mean "agreement
verified to 1e-40". It reads, in a witness, as a 1e-40 verification.

**Why nothing catches it.** `witness_raw_float64_audit` sees the `float()` and
flags the field. `always_vacuous_assertion_scan` looks for
`computed == expected`. Neither compares the TOLERANCE against the RESOLUTION
of the type the value is carried in — which is the actual defect, and is
mechanically checkable: flag any assertion whose `tolerance` is below ~1e-16
while its `computed` is produced by `float(...)`.

Same file, `:566`:

    computed=float(best_bor), expected=float(best_bor), tolerance=1e-12

`computed == expected` by construction; cannot fail. Its own `source` string
admits it — *"(self-consistent run)"*. `always_vacuous_assertion_scan` SHOULD
catch this shape and did not report this file; worth checking why.

## Class 2 — the producer SHRANK

`computations/probes/delta_lambda_bar_involution_probe.py` (fixed today so it
runs at all: two defects, `qou-cds2`). Its committed witness and what the
current source produces:

    keys only in the committed witness : 19
      /data/gap_decomposition/*   (formula, observed_gap, predicted_gap, miss_pct, ...)
      /data/option_E_comparison/* (verdict: "RULED OUT — wrong sign by 140x, cos=-0.51")
    keys only in a fresh run           :  2   (q0Anchor, q0Value)

`delta_star` also differs materially — `(5,1)`: -15.6949 committed vs -10.3397
fresh; `(3,2,1)` and `(4,1,1)` go to exactly 0.0.

So the committed witness records **analysis whose producing code no longer
exists**. `ghost_value_sweep` catches a producer that CHANGED (194 candidates);
nothing catches one that got SMALLER. The check is cheap: compare the key set a
producer emits against the key set its committed witness holds, and flag any
committed key the current source cannot generate.

I did NOT overwrite that witness. Doing so deletes 19 keys of recorded results
to replace them with values whose change I cannot explain.

## Bonus, from the same sweep — the float64 auditor leaks float64

`computations/audits/float64_leak_audit.py` FAILS ITS OWN ASSERTION and emits
3 raw float64 fields into its own witness (`.assertions[0].computed`,
`.expected`, `.tolerance`).

## Where the 11 `i8_violation` scripts stand

These CARRY a substrate-pure banner (they claim to be float-free) and violate
it — a claim contradicted by the code, which is the sharpest available form of
"not trustworthy". 32 violations over 11 files, worst first:

    9  fr_pullback_borromean_h3a_test.py
    4  canonical_tr_m_via_branching.py
    4  probes/markov_reduction_h3_to_h4_verify.py
    3  chi_at_q_inv_via_native_mpfr.py
    3  chi_cd_mpfr.py
    2  canonical_mass_table_extended.py
    2  normalization_reconciliation_phase5l2.py
    2  probes/he3_pairknot_composite_lp_probe.py
    1  constit_factor_residual_phase5k.py
    1  delta_lambda_categorical_verification.py
    1  substrate/whipple_rotation_involution_probe.py

**And the worst offender's witness has never been committed.** It writes
`fr-pullback-borromean-h3a-test.witness.json`; no such file exists anywhere in
the tree. Run here, it is long-compute — >10 min without reaching the end (H_12
⁴He). So the numbers behind those 1e-40 assertions have never existed, which is
worse than stale and is not what the "9 violations" count conveys on its own.
