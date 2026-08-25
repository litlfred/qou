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

## Axis C — drained

`bring_color_weighted` is canonical (R3). The measured surface separated into
two genuinely different problems, and only one of them was the `pn_convention=`
line the detector points at.

### `binding_canonical.py` — the convention line was the symptom

The file bean `qou-cds4` says to read first, because a file named *canonical*
assigning a non-canonical convention is either a naming defect or a real one. It
was a real one. Its local `_factor_from` had **no branch at all** for the
colour-weighted interface `d = −h(1/2 − δ/4)`. That value sits 7.190163e-05 from
the colour-blind `−h/2`, outside the 1e-6 windows for both `±h` and `±h/2`, so it
missed every branch and fell through to `sp.nsimplify(d_f)` — freezing a `q₀`
float into a rational and destroying the q-dependence the symbolic path exists to
carry. The in-code comment justified `strict_averaged` as *matching the symbolic
path's literal σ − h/2 factor*, which is true but circular: that path could only
produce σ − h/2.

This is the sibling of bean `qou-4e5k`, already fixed in
`atom_nf_symbolic_D._factor_from`, where the same crossing was *swallowed* rather
than missed (a 1e-3 window matched it to `−h/2` silently).

Verified two ways rather than asserted:

| check | before | after |
|---|---|---|
| deuteron closed form | `0.575090871629810…` — the value `qou-4e5k` names as the colour-blind error | `0.575172243917771…` — that bean's bridge/peel value |
| `B(D)`, closed form vs this file's own default transfer path | 0.43546714 vs 0.43540348 — **disagree by 1.5e-4** | 0.43540348 vs 0.43540348 — **agree to 15 figures** |

### The label trap — the class behind two red tests

`test_ctype_consumer_coverage` was **red on main** with two Part-D failures,
both the same defect. `canonical_interface_kinds()` defaults to
`bring_color_weighted` but deliberately labels the p-n interface `"averaged"` —
the label vocabulary cannot carry δ, and the real factor lives in
`closed_form_ratio`. So a consumer that asks for canonical kinds and applies its
own `{positive, negative, averaged}` dispatch gets `z − h/2`, the colour-blind
factor, **while believing it is canonical**. No equality test against
`"averaged_weighted"` can catch it, because that label was never emitted
anywhere; it fails by returning a slightly smaller number.

`probes/binding_closed_form_C_vs_D_probe.py` was doing exactly this — pricing
every p-n interface blind, in a probe whose whole purpose is comparing
conventions. Fixed at the class: `canonical_interface_kinds` gains an **opt-in**
`weighted_labels` flag emitting `"averaged_weighted"`, opt-in precisely so the
label-only consumers that depend on `"averaged"` keep working.

### A stale C-frame number that had already propagated

`signed_crossing_feasibility_probe` migrated its `z` to D earlier, and its
computed `deuteron_pn_bond_count_needed` duly reads `0.78518842…`. The `"note"`
string **one key above it in the same witness dict** still said *"Deuteron needs
0.572 pn bonds"* — the C-frame value, retyped rather than interpolated, so the
migration could not reach it.

It did not stay local. `pauli_young_spin_isospin_delta_lambda_probe` adopted
0.572 as its deuteron cross-check **target** and, being itself still in C,
reproduced it to 0.015 % — a self-consistent C-frame loop reading as
confirmation. Under canonical D the quantity is 0.7852, a 37 % miss.

And the cross-check was never one: `signed_crossing_feasibility_probe` computes
the *same expression* `(B_D/E₀)/L_pn`, so agreement between the two is **by
construction**, not evidence. The field is now named `reference_*` and says so.

## Axis B — drained to its floor, which is not zero

14 → 11 actionable. The three fixed were the one genuine live producer
(`lepton_tower_core.markov_z`, which returned C while its docstring called it
"the canonical Markov parameter" — now delegating to the canonical definition
rather than holding a second copy), the `pauli_young` deuteron block above, and
`probes/probe_alpha.py`.

**The remaining 11 are not a queue.** They split as:

- **9 in the qbeta / decay cone, where a z-swap is FORBIDDEN.**
  `QOU.QBeta.decayLadder_zC_threeRow_ne_zero` (sorry-free) makes the C-frame
  ladder and the mass channel's two-row forcing *mutually exclusive*: if the
  decay channel's decomposition kills the third row its trace parameter is
  `z_D` and the existing ladder is not that trace. So substituting `z_D` into
  these is not a cheap fix, it is an invalid one. They need the S1
  re-derivation (bean `qou-cds1`), which is science, not migration.
- **1 already adjudicated.** `probes/markov_reduction_h3_to_h4_verify.py`
  documents in its own header that it is *deliberately* left in C and float64
  "as the historical record of what the Lean docstring cites", with a live
  both-conventions companion (`markov_reduction_h3_to_h4_conventions.py`,
  worst residuals ~1e-51). The detector's actionable flag is a false negative.
- **1 needing re-derivation, not substitution.**
  `deltalambda/mirror_split_milnor_one_third_probe.py` carries three
  C-specialised closed forms (`sqrt(q0)`, `q0**1.5`) alongside its `z`; the
  audit's own second-tier note says these are the work the `z` migration does
  not finish.

So the honest floor for a *mechanical* convention-C drain is 11, and the
detector's "actionable" count overstates the drainable surface — the same shape
as axis A, where "5 new dirty witnesses" was really 4 defects and 1 false
positive. Both counts are useful as alarms and neither is a work queue.

## Final state

| axis | metric | before | after |
|---|---|---|---|
| A | NEW dirty witnesses | 5 | **1** (the `elapsed_sec` false positive) |
| A | raw float64 fields | 258,420 | **258,325** (−95 = 42+28+21+4) |
| B | actionable convention-C sites | 14 | **11** (floor: 9 Lean-blocked, 2 adjudicated/re-derive) |
| C | `test_ctype_consumer_coverage` | **RED** (2 failures) | **PASS** (6 baselined, 0 unadjudicated) |
| C | off-canon `pn_convention` baseline entries | 8 | **6** |
