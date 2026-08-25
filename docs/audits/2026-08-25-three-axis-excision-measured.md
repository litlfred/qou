# Three-axis excision — measured surface (2026-08-25)

Owner request: *"excise float64, convention C, non-color-weighted"*. This is the
2026-08-15 ruling's R1 (convention D canonical) and R3 (`bring_color_weighted`
canonical) plus the standing NO-FLOAT64 directive. Milestone `qou-cdx1` already
carries the tranche plan; this doc records what the three surfaces measure
**today**, so the drain is scoped against numbers rather than against the
estimates in older beans.

Method: the repo's own detectors, run on this branch's base. Every count below
is reproducible with the command named beside it.

## Axis A — float64

`computations/witness_raw_float64_audit.py`:

| bucket | count |
|---|---|
| witnesses carrying raw float64 | 1293 |
| total raw float64 fields | 258,420 |
| of which integral-valued (NOT a precision finding) | 224,863 in 839 witnesses |
| f64-integrator carve-out (declared) | 65 in 3 |
| deprecated-f64 carve-out (declared) | 97 in 1 |
| LP-dual carve-out (excused) | 429 in 21 |
| **NEW dirty witnesses (not in baseline)** | **5** |
| REGRESSED (count increased) | 0 |

The headline 258k is not the drain target — 87 % of it is integral-valued floats
reclassified on 2026-08-24, which are exact in binary64. **The actionable finding
is the 5 NEW witnesses**, 96 fields, each of which is a producer that landed
float64 into a witness after the baseline was set:

```
42  computations/deltalambda/deuteron-interface-handle-curvature.witness.json
28  computations/qbeta/birkhoff-barodd-pythagoras-bridge.witness.json
21  computations/qbeta/a3-branching-asymmetry-vs-required.witness.json
 4  computations/deltalambda/yekutieli-trefoil-surface2form-discretization.witness.json
 1  computations/deltalambda/sigma1cubed-seifert-surface-term.witness.json
```

Per the standing rule these are fixed **at the producer** — carry `mpmath.mpf`
from the source, serialize with `_precision.fmt`, re-run. Not baselined, not
hand-edited.

## Axis B — convention C

`scripts/convention-c-producer-audit.py` (AST-verified):

| bucket | sites | files |
|---|---|---|
| probes / exploratory | 12 | 12 |
| live producers | 2 | 2 |
| deliberately C-named comparisons (**not** defects) | 47 | — |
| **ACTIONABLE** | **14** | — |

Plus two classes the `z` migration does not finish, because the defect is a
C-specialised *closed form* rather than the `z` binding:

- **C-specialised closed forms in D files** (2): a half-integer power of `q`
  surviving in a file whose `z` is already D. `h*z+1` and `(q*z+1)/(q^2+1)` are
  rational under D, so a surviving square root is `z_C` showing through.
- **Second tier** (3): closed forms in files whose `z` is still C. The `z` is
  the defect; these are re-derived, never `z`-substituted.

## Axis C — non-colour-weighted p/n convention

Live Python assignment sites (`pn_convention=`, excluding `_deprecated/`):

| value | sites |
|---|---|
| `bring_color_weighted` (canonical) | 13 |
| `chi_lambda_braid` | 9 |
| `strict_averaged` | 7 |

Per-interface factor at the proton-pinned `q0` (50 dps) — the three are **not**
a rename, and the two off-canon values are three orders of magnitude apart from
each other in their distance to canon:

```
chi_lambda_braid  ->  z              = 0.6126880371464652516
strict_averaged   ->  z - h/2        = 0.50815788774864559388
bring_color_wtd   ->  z - h(1/2-d/4) = 0.50822978937673896258
```

So `strict_averaged` is ~1.4e-4 relative from canon while `chi_lambda_braid` is
~20 % away. A file on `chi_lambda_braid` is a materially different computation;
a file on `strict_averaged` is close but still not canon.

Triage of the off-canon files separates **defects** from **labelled comparisons**,
which R3 permits:

| file | value | reading |
|---|---|---|
| `binding_canonical.py` | `strict_averaged` | name says canonical — read first |
| `_habiro_coefficient_extract.py` | `chi_lambda_braid` | |
| `atomic_tr_m_helium4_canonical.py` | `chi_lambda_braid` | name says canonical |
| `closed_form_tau_M_verification_phase5q.py` | `chi_lambda_braid` | |
| `binding_bring_enhancement_compare.py` | `strict_averaged` | labelled comparison — legitimate |
| `binding_combiner_markov_peel_fallback.py` | `strict_averaged` | declared fallback — check label |
| `chi_monotone_transfer.py` | (comment only) | historical note, no live assignment |
| `iterative_knot_builder.py` | (comment only) | already migrated, comment records it |

`closed_form_tau_M.py` and `mass_at_3A_proper.py` carry `strict_averaged` only
inside a `if pn_convention == ...` **dispatch branch** — that is the alternative
being *implemented*, not selected, and is not a defect.
