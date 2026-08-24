---
# qou-nmza
title: 'DRAIN: 71 sites call the f64 Rust engine where an exact MPFR sibling exists'
status: todo
type: task
priority: normal
created_at: 2026-08-24T13:16:05Z
updated_at: 2026-08-24T13:16:47Z
---

Opened by the `F64_ENGINE_ENTRY` tier added to
`computations/f64_into_mpmath_audit.py` (2026-08-24). Sibling of `qou-840k`.

## The class

`pyhecke_native` exposes five f64 entry points that each have an exact MPFR
sibling:

    chi_lambda_all_partitions_f64  -> chi_lambda_all_partitions_mpfr
    chi_lambda_braid               -> chi_lambda_braid_mpfr
    chi_lambdas_braid              -> chi_lambdas_braid_mpfr
    chi_q_atomic                   -> chi_q_atomic_mpfr
    chi_q_atomic_all_partitions    -> chi_q_atomic_all_partitions_mpfr

**71 site(s) in 46 file(s)** reach the f64 one, over two hops:

1. **Direct** — `pyhecke_native.chi_lambda_braid(...)`.
2. **Wrapper** — `hecke_characters.chi_lambda_braid(...)` with no
   `precision=`. That keyword selects the path and DEFAULTS to f64; 20 of 30
   wrapper sites omit it.

`_iter_rows` / `--tier F64_ENGINE_ENTRY` gives the live list. Do not re-derive
it by grep — see the two failed censuses below.

## What makes a site actionable (it is NOT "calls the f64 entry")

The f64 entry is ~10-30x faster and is frequently the right choice. Measured
against MPFR at 50 dps, proton q0:

    H3  sigma_1        rel diff 2.917e-16
    H3  borromean-ish  rel diff 7.746e-16
    H6  deuteron-ish   rel diff 7.362e-16

~15-16 real digits. So the defect is **calling it and then serialising the
result at more digits than that**. Triage each site by what it does with the
value, not by the call:

- writes a witness at 30/50 dps  -> **fix**
- feeds a downstream mpmath chain -> **fix**
- a fast scan / ranking / plot    -> **leave, and say so in a comment**

Worked example: `fr-pullback-k1-k2.witness.json` carries **697** numbers at
>=18 significant digits, every one from the f64 path.

## The half-fix that will look like a fix

`precision="mpfr_50dps"` alone is NOT sufficient. The wrapper preserves the
boundary only when `q_value` is a **string**; a float is put through
`format(float(q_value), ...)` first, which the wrapper's own comment calls
"implicit acceptance of f64 boundary loss". Pass `Q_50_DIGIT_STR`, not `Q`.

Cost: the MPFR path is ~10-30x slower (its docstring's figure). Long-running
producers need the compute-audit long-compute logging discipline
(`python3 -u ... 2>&1 | tee /tmp/<script>.log`) rather than a silent re-run.

## Do not re-measure by grep — two censuses were wrong first

Both were mine, in opposite directions:

* **120 sites / 64 files** — regex over call names, which counted **string
  literals**. `closed_form_tau_M.py` declares `PnConvention =
  Literal["chi_lambda_braid", ...]`: convention names, not calls.
* **51 sites / 39 files** — the AST detector before the wrapper hop existed,
  blind to every caller going through `hecke_characters`.

Guard cases for both are in the audit's self-tests (36/36).

## Also corrected

`qou-840k`'s "49 of 116 F64_CAST files use no f64 engine" is **43**, not 49 —
the engine regex behind it had `pyhecke.gram` but not `pyhecke_native`. Six
modules routing through the Rust engine were counted as engine-free. And the
framing was too generous regardless: "f64 engine" exempts a module only when
**no exact sibling exists**. Where one does, it is not an f64 pipeline by
design, it is the wrong entry point.
