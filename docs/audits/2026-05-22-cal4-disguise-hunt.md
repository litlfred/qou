# CAL-4 disguise hunt — beyond literal `mp.mpf("...")`

**Date:** 2026-05-22
**Branch:** `claude/iw-cal4-disguise-hunt-2026-05-22`
**Predecessor:**
- PR #888 — `LAMBDA_*_FITTED_FROM_CODATA` literal truth-in-naming +
  `fitted_labelled_canonical_audit.py`
- PR #892 — `conj:mobius-limit-from-thimble` curve-fit demotion
- PR #904 — `conj:lambda-scale-bring-bloch-identity` demotion
- PR #923 + #928 — q-dilog basis-exhaustion spikes

**Status:** New audit tool + 3 in-line annotations. Hunt-A (Möbius-pencil disguises) is now CLEAN; Hunt-C surfaces 22 unrelated CODATA-literal **duplications** (separate cleanup track).

## What the existing tooling catches

`fitted_labelled_canonical_audit.py` (PR #888) catches the **literal**
pattern: module-level `mp.mpf("<10+ digit literal>")` definitions
that match CODATA-derived constants. After PR #888 + #892 + #904, all
known **literal** disguises have been truth-in-named.

## What this hunt adds

`cal4_disguise_hunt.py` (this PR) catches three additional patterns:

| Hunt | Pattern | Example |
|---|---|---|
| **A** | Möbius / rational q-pencils used as substrate-derived formulas without an acknowledged CAL-4 banner | `(4-q)/(4q+3)` ansatz (PR #892 demoted to `conj:`) |
| **B** | PSLQ script targeting CODATA-derived value AND claiming "substrate/canonical/derived" in docstring without acknowledgement | `bring_bloch_tier{0..5}_search_m_p.py` (already labelled correctly) |
| **C** | High-precision literals (≥ 10 digits) not in acknowledged `_FITTED_FROM_CODATA` / `_VALIDATION` / `_CODATA` slots and not imported from `codata_constants` | `M_E_MEV = 0.51099895069` redefinitions in 4 scripts |

### Heuristics

Exempt patterns: `# CAL-1/2/3/4`, `# FITTED_FROM_CODATA`, `# acknowledged`, `# noqa: P31/P32`, `_deprecated/`, `codata_constants.py`, file-level docstrings mentioning `post-hoc / empirical / fitted / conj:mobius`.

File-level exemption for Hunt A: if the module's first 80 lines acknowledge the CAL-4 status (via `conj:mobius-limit-from-thimble` / `CAL-4` / `post-hoc` / `empirical` / `fitted` references), in-line references are not flagged.

File-level exemption for Hunt C: if the script imports from `codata_constants`, locally-defined CODATA-matching literals are a duplication issue (separate cleanup), not a CAL-4 disguise.

## Findings

### Hunt A — Möbius-pencil disguises: **0** (after annotations)

Before annotations: 19 false-positive references to `(4-q)/(4q+3)` in audit / probe scripts that already correctly characterize the pencil as post-hoc. After file-level docstring exemption + 3 in-line `noqa: P31` / CAL-4-caveat banners:

| File | Line | Action |
|---|---|---|
| `picard_lefschetz_thimble.py:883` | `limits_to_test` literal | added comment + relabel: `"(4-q)/(4q+3) (post-hoc-fitted, conj:mobius-limit)"` |
| `picard_lefschetz_thimble.py:1051` | `add_caveat` text | rewrote: "post-hoc-fitted integration limit … conj:mobius-limit-from-thimble, CAL-4 ansatz" |
| `alpha_high_precision.py:189` | `(q-1)/(q+1)` PSLQ basis element | added `# noqa: P31 — generic q-rational basis element`. NOT the (4-q)/(4q+3) pencil; was a false-positive for our specific CAL-4. |
| `probe_a_higher_derivatives_and_gb_tracking.py` | file docstring | added CAL-4 caveat acknowledging the (4-q)/(4q+3) comparison context |

Hunt A is now clean. The hunter will catch any **new** Möbius-pencil disguise that lands in production without a banner.

### Hunt B — PSLQ + substrate-claim + CODATA target: **0**

All `bring_bloch_tier{0..5}_search_m_p.py` scripts correctly identify themselves as fitting against `M_P_MEV_VALIDATION` (CODATA closure target). PR #888's truth-in-naming already covered this.

### Hunt C — duplicated CODATA / high-precision literals: **22**

Not strictly CAL-4 disguises, but a **stale-duplication** issue: scripts that re-instantiate values which should be imported from a shared module.

| Category | Count | Pattern |
|---|---:|---|
| `M_E_MEV` redefined | 4 | `M_E_MEV = 0.51099895069` in scripts that don't import `codata_constants` |
| Hyperbolic knot volumes redefined | 12 | `VOL_5_2`, `VOL_6_1`, …, `VOL_8_1`, `VOL_41` across `lambda_scale_rd4_k_p_search.py`, `lambda_scale_rd2_transcendental.py`, `probe_workplan_0b_route_c_bring.py` |
| V̂ values redefined | 5 | `V_HAT_PROTON`, `V_HAT_NEUTRON`, `V_HAT_ELECTRON` in `probe_a_ell_confinement.py` |
| tr_M values redefined | 1 | `TR_M_PROTON_AT_Q0`, `TR_M_NEUTRON_AT_Q0` in `deuteron_delta_i_audit.py` |

These are **backlog items**, not active CAL-4 issues. Cleanup paths:

- **M_E_MEV redefinitions**: replace with `from codata_constants import M_E_MEV`.
- **Hyperbolic knot volumes**: create a shared `_snappy_volumes.py` (or similar) with `VOL_5_2_SNAPPY = ...` (suffix marks them as SnapPy-derived structural constants, not CAL-4-fitted).
- **V̂ values**: derive from `canonical_tower.per_irrep_V_hat` rather than hardcoding.
- **tr_M values**: derive from `chi_lambda_braid` / `closed_form_tau_M` rather than hardcoding.

## Files

- [`computations/cal4_disguise_hunt.py`](../../computations/cal4_disguise_hunt.py) — new audit
- [`computations/cal4-disguise-hunt.witness.json`](../../computations/cal4-disguise-hunt.witness.json) — finding details
- [`computations/picard_lefschetz_thimble.py`](../../computations/picard_lefschetz_thimble.py) lines 883, 1051 — CAL-4 banners
- [`computations/alpha/alpha_high_precision.py`](../../computations/alpha/alpha_high_precision.py) line 189 — `noqa: P31`
- [`computations/probe_a_higher_derivatives_and_gb_tracking.py`](../../computations/probe_a_higher_derivatives_and_gb_tracking.py) docstring — CAL-4 caveat

## Recommended next actions

1. **CI hookup**: add `cal4_disguise_hunt.py --strict` to `witness-pipeline.yml` to catch future Möbius-pencil disguises at PR review time.
2. **Hunt-C backlog**: consolidate the 22 CODATA-literal duplications via a follow-up integration-watcher PR (script-only, mechanical sweep).
