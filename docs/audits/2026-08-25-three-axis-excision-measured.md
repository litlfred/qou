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

## Axis A — SUPERSEDED by a sibling, and rightly

**This branch's axis-A work did not land and should not.** While it was open, a
sibling drained the same four float64 witnesses on `main` (`147aeb66c`,
`e1114b1b2`) and migrated the same `pauli_young` stale convention-C hand-copy
(`a97d415bd`). The merge took **theirs** on all ten conflicting files.

That was not a coin toss. Their versions are better on the mathematics, and the
differences are worth recording because they are instructive:

- **`F_q(1)` exactly, not as a limit.** They evaluate at the exact classical
  Young form. This branch used an `ε = 1e-30` offset — a better approximation to
  the limit than the `1e-7` it replaced, but still an approximation. Theirs
  removes the limit entirely.
- **They carried the ninths further.** Both branches independently found
  `lim_{q→1} ‖dF_q‖²/h⁴` to be exact ninths. They verified `4k/9`, `k ∈ {0..4}`
  to **22 digits** and found it **conjugation-symmetric** — `(5,1) ↔ (2,1⁴)`
  both 4/9, `(3,2,1)` alone 16/9. This branch observed the ninths and stopped.
- **Cleaner separation of concerns.** They fixed precision and *kept* the muon
  pin, labelling it `"muon (ideal CAL-2)"`. This branch changed pin and
  precision in one commit, conflating two movements in one diff.
- **A defect this branch could not have hit.** `58db04f28` fixes `fmt()`-padding
  a 17-digit `q0` **literal**, which appends digits wrong from the 18th. This
  branch read `q0` from `q_at()`, which computes rather than pads — verified,
  all 60 serialized digits survive independent recomputation at 110 dps — so the
  bug was structurally absent rather than avoided by care.

Also dropped: this branch's `young_seminormal.seminormal_sigma_symmetric`. Main
added `hecke_characters.build_seminormal_matrices_mp`, the same object placed
better — beside the float64 twin it replaces, where all 64 of that builder's
callers can find it. Keeping both would leave two copies of one dispatch, the
`qou-4e5k` failure mode this document cites three times.

### What axis A is still worth for

Two findings survive as *measurements*, independent of whose code landed:

1. **The "5 NEW dirty witnesses" headline was 4 defects and 1 false positive.**
   `sigma1cubed-seifert-surface-term`'s single raw float64 is
   `elapsed_sec: 0.001` — a wall-clock timing with no precision content and
   nothing to carry as `mpf`. It is neither fixed nor baselined. The audit
   carries three documented carve-outs but has no notion of a diagnostic field;
   31 witnesses in `computations/` hold an `elapsed_sec` and this is the one
   whose value did not round to an integer. Tracked as `qou-ywee`.
2. **The headline 258,420 raw float64 fields is not a drain target.** 224,863 of
   them are integral-valued floats reclassified on 2026-08-24, exact in binary64.

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

### Independently corroborated, from a different direction

A sibling reached the same negative while this branch was open, and measured it
rather than deriving it. Bean `qou-lp5d` records that of 8 assigned B4 sites,
**5 are blocked for one reason**: the probe's own *subject* — the property it
asserts and concludes about — is an analytic feature `z_C` has and `z_D` does
not. Symbolically, with no float anywhere:

| property | `z_C = √q/(q+1)` | `z_D = q³/(q²+1)` |
|---|---|---|
| bar involution `q → 1/q` | **bar-EVEN** | **neither** |
| order of `(z − ½)` at `q = 1` | **2** | 1 |

So substituting `z_D` does not move a value — it *falsifies the probe's own
committed assertions* and desynchronises it from a sorry-free Lean companion.
That is a stronger statement than this branch's route (the Lean
mutual-exclusivity above), and the two agree. Their bean also makes the
structural point this section is arguing: the "B4" label reads as a work item,
so every future drain will pick these up, re-derive the blocker, and put them
back. The audit now carries a **blocked-by-design** bucket for exactly that.

So the honest floor for a *mechanical* convention-C drain is real, and the
detector's "actionable" count overstates the drainable surface — the same shape
as axis A, where "5 new dirty witnesses" was really 4 defects and 1 false
positive. Both counts are useful as alarms and neither is a work queue.

## Final state

| axis | metric | before | after |
|---|---|---|---|
| A | *(superseded — landed on `main` by a sibling, see above)* | — | — |
| B | actionable convention-C sites | 14 | **9** on the merged tree (3 by this branch, the rest by `main`) |
| C | `test_ctype_consumer_coverage` | **RED** (2 failures) | **PASS** (6 baselined, 0 unadjudicated) |
| C | off-canon `pn_convention` baseline entries | 8 | **6** |


## Correction: `Q0_FLIP: 0` is a weaker gate than this branch cited

Raised by the sibling on PR #5765 and confirmed here against the audit's own
source, not taken on trust. `q0_anchor_consistency_audit`'s docstring is
explicit:

> `Q0_OK` — anchor ∈ {muon,proton} **and `q0Value` matches that anchor's pin**

It compares the two recorded **stamp fields to each other** — never against the
constants the producer actually consumed. So a producer that copies
`constants.q_0` out of an *input* witness inherits whatever pin that input
carried, gets stamped from the manifest, and reports `Q0_OK` either way.
`Q0_FLIP: 0` therefore means "no witness contradicts its own stamp", which is
strictly weaker than "computed at the anchor it claims".

**The conclusion it was cited for still holds, because the actual check was a
different one.** For `signed_crossing_feasibility_probe` the pin was established
by reading the *payload* — `constants.q0` is the proton value both before and
after the re-run — against the code's `from q_parameter import Q_MP`. That is a
comparison of the recorded value to the consumed constant, which is exactly what
the audit does not do. What needs correcting is the framing: `Q0_FLIP: 0` was
listed as part of the gate and is better described as a consistency check that
happened to be green.

This is the same failure class as axis A one layer up, and worth stating
together: four producers hardcoded `Q0 = 1.1099785955573347` (the muon value)
while one of them *labelled* that literal `# proton-pinned substrate modulus`.
The stamp and the arithmetic are independently settable, and only one of them is
audited.
