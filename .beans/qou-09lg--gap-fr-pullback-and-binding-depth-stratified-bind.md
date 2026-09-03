---
# qou-09lg
title: 'GAP: fr_pullback_* and binding_depth_stratified_* bind q as a Python float — the f64_into_mpmath half-fix trap is LIVE'
status: todo
type: task
priority: normal
created_at: 2026-08-29T16:17:15Z
updated_at: 2026-08-29T16:17:54Z
---

Parent: qou-k6b3. Surfaced draining the F64_ENGINE_ENTRY PROPAGATES bucket
reported by `computations/f64_into_mpmath_audit.py`.

## The finding

`f64_into_mpmath_audit` carries a HALF-FIX WARNING for the `fr_pullback_*` /
`binding_depth_stratified_*` family, saying `mass_at_3A_proper.dim_q` and
`qfac` return Python FLOATS so swapping the Rust entry to MPFR alone leaves
the result f64-capped. **The warning is LIVE. I nearly recorded it as stale.**

The trap is that it depends on the ARGUMENT, not the function:

    from q_parameter import Q_MP as Q0            # mpf
    dim_q((2,1), Q0)              -> mpf, precision-responsive (dps 30 vs 50 agree to ~30 digits)

    from qou_substrate.constants import Q         # FLOAT 1.1099785827513808
    dim_q((2,1), Q)               -> float 2.010896866707122

`hecke_characters.dim_q` dispatches: `q is None` uses the module-level
`q_int`, which closes over `Q`/`Q_INV`/`HA` — all Python floats; an explicit
`q` uses `_q_int_at`, which is mpmath-clean. So the function is fine and the
BINDING is the defect.

`computations/fr_pullback_cosh_h_test.py:52` does
`from qou_substrate.constants import Q as Q0_PROTON`, then calls
`dim_q(shape, Q0_PROTON)` at :114 and :130 and `qfac(n, Q0_PROTON)` at :104.
All three come back float64.

**Method note for whoever takes this.** I first tested `dim_q` with
`q_parameter.Q_MP`, got an mpf, and was one edit from writing "the audit's
warning is stale" into this repo. The proxy I tested was not the input the
file uses. Test with the module's OWN import line.

## Why it is not a drive-by fix

Rebinding `Q0_PROTON` to an mpf changes every number the file emits, and the
same `from qou_substrate.constants import Q` pattern appears across the
`fr_pullback_*` and `binding_depth_stratified_*` families — the audit lists 8
modules importing `dim_q`/`qfac`. That is a scoped change with 8 consumers to
re-run, not a one-line swap, and doing only the Rust half would be exactly the
half-fix the audit warns against.

## Also settled while here

`computations/all_nuclides_wedderburn_spectral_v2.py` is listed PROPAGATES and
must **NOT** be converted. Its two f64 entries (`chi_lambda_braid` at :363,
`trace_weights_n` at :389) are DELIBERATE cross-checks: mpmath `mine` against
native `ref` at tolerance 1e-9. Converting them would compare mpmath to
mpmath and test nothing. Measured: **no module reads the f64 fields** —
`trace_weights_n_native` and `chi_std_vs_native_hoefsmit` have zero consumers
outside the producer; the two modules that read the witness
(`delta_lambda_feed_analysis.py`, `audits/vacuous_pass_assertion_scan.py`)
read the per-nuclide rows, and the first reads them as floats by design.

So the audit's PROPAGATES bucket is coarse: it keys on "the WITNESS is read by
another module", not "the f64 FIELD is read". Narrowing it to field-level
consumption would move this file out of the actionable set.
