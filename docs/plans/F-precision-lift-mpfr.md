# Plan F — Precision lift to MPFR @ 50 dps end-to-end

**Status:** design pass. No code changes yet.
**Target:** witness
[`computations/low-isotope-mass-table.witness.json`](../../computations/low-isotope-mass-table.witness.json)
currently reports `precision: "f64_numeric_fallback"`. The master
proposition (`prop:alpha-k-derivation-procedure`) specifies "evaluated
to ≥ 50 decimal digits via MPFR".  This plan migrates every step
(1a–6) of the categorical pipeline to mpmath / `rug::Float` at 50 dps.

## Pipeline inventory — what is f64 today

The mass-derivation pipeline runs through these stages.  For each, we
record the implementation file, the numeric type used today, and what
needs to change.

| Step | What | File | Today | Target |
|------|------|------|-------|--------|
| 1a | Substrate `q_0` | `computations/substrate/q_parameter.py` | `float` | `mpf` (50 dps decimal string source) |
| 1b | Hoefsmit seminormal `ρ_λ(σ_i)` | `tools/hecke-engine/src/seminormal.rs` (f64) **and** `seminormal_mpfr.rs` (rug::Float, 167-bit) | mixed | drive everything through `seminormal_mpfr` |
| 2  | `χ_λ(β)` characters | `tools/hecke-engine/src/seminormal.rs::chi_lambda_braid` (f64) **and** `seminormal_mpfr::chi_lambda_braid_mpfr` | mixed | exclusive MPFR path via `pyhecke_native.chi_lambda_braid_mpfr` |
| 3  | `y_λ` Jones–Markov solve | `computations/y_lambda_jones_markov_witness.py` (f64) **and** `y_lambda_mpfr_witness.py` (mpmath, 50 dps; n ≤ 11 only) | mixed | extend mpmath solver to n=12; fall back to symbolic Wenzl bridge for n ≥ 13 |
| 4  | `tr_M(T_w)` Markov trace | `computations/markov/markov_trace_canonical.py` (sympy, exact) | symbolic exact | OK — already exact rational in q.  Must evaluate with `q = mpf(q_0_str, 50)` |
| 5  | Census-knot volumes (²H/³H/³He shortcut) | `low_isotope_binding_sweep.py` constants `VOL_6_2`, `VOL_8_11`, `VOL_BORROMEAN`, `VOL_7_2_1` | `float` literals from SnapPy | Plan G retires these.  Until then: pass through as `mpf` with reported uncertainty |
| 6  | Mass-excess assembly `Δ = Z·Δ_H + N·Δ_n − B` and `M = A·u + Δ` | `computations/low_isotope_mass_table.py` | `float` (CODATA constants) | `mpf` constants pinned at 50 dps from CODATA-2022 source |

## Where the f64 residual actually lives — ranking by dominance

Evidence from the witness JSON: `M_max_abs_ppm ≈ 2081 ppm`, dominated
by ⁶Li/⁷Li/¹⁰Be partial-shell rows (strategies that aren't even
calling the Hecke kernel).  For the four census rows (²H/³H/³He/⁴He)
the residuals are 0.001 ppm – 81 ppm — and **none** of the residual
comes from f64 rounding:

| Origin | Ballpark contribution to ppm error |
|--------|------------------------------------|
| f64 rounding in `χ_λ` and `y_λ` | < 0.01 ppb (verified by `y_lambda_mpfr_witness.py` at 50 dps agreeing with f64 to 14 sig figs) |
| `VOL_6_2 = 4.40083` truncation (5 sig figs) | ≈ 1 ppm on ²H |
| `VOL_BORROMEAN = 8·G_Catalan` Catalan constant truncation | < 0.01 ppm |
| ρ hand-pick (`m_e` vs `2m_e`) — Plan H | dominates for ³He (81 ppm) |
| Vol-shortcut substituting tr_M (Plan G) | dominates for ²H/³H/³He |
| Partial-shell linear interpolation | 1000 ppm for ⁶Li, ⁷Li |

**Conclusion.**  The f64 fallback is *not* the bottleneck for the
1 ppb goal.  Plan F is pure-hygiene infrastructure that lets the
witness *report* 50 dps precision; the actual physics gain is from
Plans G and H.  Therefore Plan F is intentionally lower-priority,
but it is a prerequisite for a publishable witness.

## Migration order (priority)

1. **q_parameter.py source-of-truth (½ d).**  Add an mpmath-backed
   `Q_MPF_50DPS` constant alongside `Q`, sourced from the same
   decimal string as in `tools/hecke-engine/Cargo.toml`/build script.
   Add a regression test that the f64 cast matches `Q` exactly.
2. **Witness emitter contract (½ d).**  Define a
   `precision: "mpfr_50dps"` schema field with mandatory companion
   `precision_dps: 50`, `precision_bits: 167`, and a per-row
   `_dps_str` field (decimal string at full 50 dps) shadowing the
   primary f64 field.  Document this in the witness schema.
3. **Step 4 (tr_M evaluation) — 1 d.**  `markov_trace_canonical.py`
   already returns a sympy expression; substitute `q -> mpf(q_str)`
   at evaluation time using `sp.lambdify(..., modules=[mpmath])`.
   Adds a `tr_M_at_q0_mpf` helper that returns an `mpmath.mpf`.
4. **Step 3 (y_λ solve) — already done at n ≤ 11; 2 d to extend
   to n = 12.**  The TODO in `y_lambda_mpfr_witness.py` flags the
   bottleneck (462×462 MPFR matmul for partition (4,4,4)).  Two
   options: (a) parallelise over partitions in `seminormal_mpfr`
   via `rayon`; (b) switch n=12 to the symbolic Wenzl bridge in
   `y_lambda_wenzl_bridge_extended.py` (already supports n=12).
   **Recommend (b)** — costs ½ d, defers the MPFR bottleneck.
5. **Step 6 (mass assembly) — 1 d.**  Convert `low_isotope_mass_table.py`
   to `mpf` arithmetic.  CODATA constants (`U_MEV`, `M_P_MEV`,
   `M_N_MEV`, `M_E_MEV`) become `mpf` from decimal strings (CODATA
   gives 11 sig figs, well within 50 dps).  Output JSON gains
   `_dps_str` shadows.
6. **Step 1b/2 (Hoefsmit kernel) — 0 d new code, 1 d wiring.**
   `seminormal_mpfr.rs` and `chi_lambda_braid_mpfr` are written.
   Replace every f64 call site in `low_isotope_binding_sweep.py`
   and downstream with the MPFR variant.
7. **End-to-end harness — 1 d.**  Add a script
   `low_isotope_mass_table_mpfr.py` that runs the entire chain at
   50 dps and emits a witness with `precision: "mpfr_50dps"`.
   Cross-check against the f64 witness: every numeric field must
   agree to ≥ 14 sig figs.
8. **CI gate — ½ d.**  Add a step to the relevant workflow that
   runs the MPFR witness emitter and diffs against a committed
   golden 50 dps witness.

## Effort estimate

| Phase | Person-days |
|-------|-------------|
| q_parameter + schema | 1 |
| tr_M evaluation | 1 |
| y_λ extension to n=12 (Wenzl-bridge route) | 0.5 |
| Mass assembly (Step 6) | 1 |
| Hoefsmit wiring (Step 1b/2) | 1 |
| End-to-end harness + golden witness | 1 |
| CI gate | 0.5 |
| **Total** | **6 days** |

## Smoke test / exit criterion

A new artifact
[`computations/low-isotope-mass-table-mpfr.witness.json`](../../computations/low-isotope-mass-table-mpfr.witness.json)
exists with:

- `precision: "mpfr_50dps"`, `precision_bits: 167`,
  `precision_dps: 50`.
- For every row, fields `q_0`, `B_pred_MeV`, `delta_pred_MeV`,
  `M_pred_MeV` shadowed by `_dps_str` decimal strings of length
  ≥ 50 + sign + decimal-point.
- The f64 cast of every `_dps_str` agrees with the existing
  f64 witness to 14 sig figs (regression).
- CI runs the harness on every push to main.

## First concrete step

Create
`computations/q_parameter_mpf.py` (or extend
`q_parameter.py`) with:

```python
Q_STR_50DPS = "1.10997859555418050000000000000000000000000000000000"
Q_MPF_50DPS = mpmath.mpf(Q_STR_50DPS)
```

Then add a one-line regression test asserting
`float(Q_MPF_50DPS) == Q`.  This is the foundation every other
step depends on, and it surfaces the source-of-truth question
("what is q_0 at 50 dps?") before anything else can be lifted.

## Out of scope

- Lifting Step 5 (volumes) is **Plan G's job**.  This plan only
  threads `mpf`-typed values through the existing volume shortcut.
- ρ hand-pick is **Plan H's job**.  This plan keeps the existing
  `m_e`/`2m_e` choice.

## Risk register

- **R1.** `seminormal_mpfr` is 10–30× slower than the f64 path.
  At n ≥ 12 this can blow up CI time.  Mitigation: precompute
  golden witness offline; CI only verifies, does not regenerate.
- **R2.** mpmath linear-solve (`mp.lu_solve`) at p_n × p_n with
  p_12 = 77 may hit a numerical edge case.  Mitigation: fall
  back to Wenzl-bridge symbolic at n ≥ 12.
- **R3.** Some downstream consumers may silently truncate
  `_dps_str` shadows on read.  Mitigation: schema lint that
  flags any `_dps_str` field shorter than 50 chars after the
  decimal point.
