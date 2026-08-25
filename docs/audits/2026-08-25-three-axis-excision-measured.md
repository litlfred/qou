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

## Axis A — drained

Four of the five were real and are fixed at the producer. The fifth was not a
defect.

| witness | fields | what it actually was |
|---|---|---|
| `deuteron-interface-handle-curvature` | 42 | float64 **by allocation** — built via `hecke_characters.build_seminormal_matrices`, which resolves `q` through `float(q)`, then cast to numpy `dtype=complex` |
| `birkhoff-barodd-pythagoras-bridge` | 28 | Python `1j` complex arithmetic — the class the ratchet's own guard misses (`qou-f64j`) |
| `a3-branching-asymmetry-vs-required` | 21 | `math.log` / `math.sqrt` / `math.atanh` on float literals |
| `yekutieli-trefoil-surface2form-discretization` | 4 | `math.sqrt` on float matrix literals |
| `sigma1cubed-seifert-surface-term` | 1 | **false positive** — see below |

All four also hardcoded `Q0 = 1.1099785955573347`, which is the **muon** value
(proton is `...5827513808`); one of them, `birkhoff`, labelled that literal
`# proton-pinned substrate modulus`. All four now take the pin from `q_at()`.

Three findings came out of the rewrites that are worth more than the drain:

1. **A symbol collision in `birkhoff`.** `H_LIT = 0.10997859555733469` was
   commented as "the `h` reading", but it is `q − 1`, not the `h = q − q⁻¹`
   defined on the line directly above it (0.10998 vs 0.20906, a factor of ~1.9).
   Two different quantities named `h` in one file. The longitudinal scan now
   tests **both**, so the negative it reports is stronger: 0 of 6 readings land
   `r*`, where before it was 0 of 4 with the ambiguity unresolved.

2. **A wrong claim in `deuteron`, pre-existing.** The witness carried
   `dFq_scales_as_h_squared: True` with the coefficient quoted in a side comment
   as *"1.77 (measured, constant ratio)"*. The ratio is **not** constant across
   partitions — that same witness's own rows run 0.435 to 1.751, a factor of 4,
   and 1.77 is the `(3,2,1)` block alone. The `h²` claim is nonetheless **true**
   in its correct reading, which is per-λ `h`-dependence rather than constancy
   across λ, so it is now *derived* that way: the fitted exponent of `‖dF_q‖²`
   in `h` is 4 to within 8e-5 for all nine non-singlet blocks. The two facts are
   now separate witness fields instead of one conflated boolean.

3. **A structure the old arithmetic could not see.** The `q → 1` limiting
   coefficients of `‖dF_q‖²/h⁴` read as exact ninths — 4/9, 8/9, 12/9, 16/9
   across the eleven H₆ blocks. Recorded as an *observation*, not a derivation.
   Under binary64 the `q → 1` offset had to be `1e-7` (the seminormal diagonal
   is 0/0 at `q = 1` and both parts are O(ε), so a smaller offset was destroyed
   by cancellation), which capped the limit at ~6 figures: 16/9 read as 1.7506.

Supporting change: [`young_seminormal.seminormal_sigma_symmetric`](../../computations/young_seminormal.py)
— the symmetric-gauge mpmath counterpart of the float64 builder, verified
entry-for-entry against it on (3,1), (2,2), (3,2,1), (4,2). The symmetric gauge
is required rather than incidental: the deuteron probe reports **Frobenius
norms**, which are not gauge-invariant, so the module's existing
non-symmetric `seminormal_sigma` would have silently shifted every magnitude.

### The fifth is a detector false positive

`sigma1cubed-seifert-surface-term`'s single raw float64 is
`elapsed_sec: 0.001` — a **wall-clock timing**, written by the producer as
`round(time.perf_counter() - t0, 3)`. It is not a mathematical quantity and has
no precision content, so there is nothing to carry as `mpf` and nothing to fix.

It is not baselined either. The audit carries three documented carve-outs
(LP-dual, float64-integrator, deprecated-f64), each counted and reported, but
has no notion of a diagnostic/wall-clock field. 31 witnesses in `computations/`
carry an `elapsed_sec`; this is the one whose value did not happen to round to
an integer, which is the only reason it surfaced. So the headline "5 NEW dirty
witnesses" is really **4 defects and 1 false positive**. Tracked as its own bug
rather than fixed here — converting 31 producers, or adding a fourth carve-out,
is a wider decision than this drain.
