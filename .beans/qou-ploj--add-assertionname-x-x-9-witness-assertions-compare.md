---
# qou-ploj
title: 'add_assertion(name, X, X): 9 witness assertions compare a value to itself and can never fail'
status: in-progress
type: task
priority: normal
created_at: 2026-08-25T19:47:06Z
updated_at: 2026-08-25T21:28:54Z
---

FOUND 2026-08-25 while draining the two state-2 records of
`docs/audits/2026-08-25-ylambda-threerow-frame-audit.md`. Tool:
`computations/audits/self_fulfilling_assertion_audit.py` (`--selftest` included).
Two instances are FIXED in that PR; **9 MEASURED hits remain**.

## The defect

`WitnessBuilder.add_assertion(name, computed, expected)` marks an assertion `passed`
when `computed == expected`. Nothing stops the two arguments being the SAME
EXPRESSION. When they are, the assertion is `x == x`: tautologically true, unable to
fail, and it renders as `"passed": true`, which the QA pipeline reads as evidence.

This is the compute-side twin of a rule AGENTS.md already states for Lean, under
§"No trivial trues, no tautologies, no laundering": *"Tautological conclusions are
banned: `X = X` ... any proposition that is provable without using any hypothesis
about the mathematical objects in question."* The same sentence applies verbatim to a
witness assertion. Nothing was checking for it on the compute side.

## The worked case that exposed it

`threerow_sign_crossing_probe` carried, under a comment calling them **"the headline
falsifiable fact"**:

```python
w.add_assertion("D_sign_qlo", iso_rows["D"]["sign_qlo"], iso_rows["D"]["sign_qlo"])
w.add_assertion("D_sign_q0",  iso_rows["D"]["sign_q0"],  iso_rows["D"]["sign_q0"])
```

Between conventions C and D the deuteron object went from `F(q0) = -0.19496...` to
identically zero and the asserted sign went `+1 -> 0`, `-1 -> 0`:

| assertion | committed (C) | re-run (D) |
|---|---|---|
| `D_sign_qlo` | `1/1 True` | `0/0 True` |
| `D_sign_q0` | `-1/-1 True` | `0/0 True` |

The measurement inverted; the check passed both times. **A sign is a MEASUREMENT, not
a check** — it belongs in `add_data`.

## Scale, measured

3199 files, 3530 `add_assertion` calls. **9 MEASURED**, 17 LITERAL.

MEASURED — both slots derived from the computation. Dangerous: looks like a check,
tracks whatever the code does, cannot report a regression.

```
computations/deltalambda/b4_nonsaturating_mstar_diagnostic.py   L235 derived_lead_found
computations/deltalambda/mu3_abs_choice_robustness_probe.py     L122 verdict_robust_to_abs
computations/deltalambda/mu3_door_budget_probe.py               L195 ceiling_below_P_both_isotopes
computations/deltalambda/mu3_frechet_perblock_probe.py          L235 frechet_violator_found
computations/deltalambda/threerow_crossing_a_dependence_probe.py L302/303 <dynamic> sign_q0/sign_qlo
computations/deltalambda/threerow_isospin_parity_probe.py       L266 isospin_pattern_survives_fixed_n_control
computations/su2_spinor_multiplicity_resolution.py              L368 global_canonical_spin_selector_exists
                                                                L386 intermediate_H4_spin_simple_on_all_m2_spaces
```

LITERAL — same constant in both slots (`0`, `1`, `True`, `'pass'`), e.g.
`no_h4_fit_performed`. Documentary flags the author asserted, not measurements. Still
misleading beside real checks, but they do not silently track a drifting quantity.
Listed by the tool; **do not bulk-convert them without reading each one** — some are
deliberate provenance statements and the right fix is `add_parameter`, not deletion.

## Why several of these are load-bearing

`mu3_abs_choice_robustness_probe::verdict_robust_to_abs` is the fifth C-frame instance
identified in that audit's layer-3 dating, and its verdict is exactly the kind that
gets quoted downstream. `mu3_door_budget_probe` and `mu3_frechet_perblock_probe` are
both in the mu3-door cone. `threerow_crossing_a_dependence_probe` is UNIT-2, which
`qou-qdtk` shows is receiving a C-frame "correction" about crossings above a `q*` that
does not exist under D. `threerow_isospin_parity_probe` is `qou-iav7`.

So this bean and `qou-iav7` overlap on one file, and `qou-qdtk` on another. Whoever
takes them should read all three rather than fixing file-by-file.

## The fix, per hit

Supply an INDEPENDENT expected value, or demote to `add_data` / `add_parameter` —
recording is not checking. Worked example in the PR: the two sign assertions became
`add_data`, and a real assertion took their place —
`three_row_object_is_structural_zero`, `max|F| < 1e-30`, a tolerance chosen once and
justified against the C-era O(1) magnitudes and f64 noise, never fitted. On the
committed C data that assertion FAILS, which is the point.

## Consider gating

The tool exits 1 on any MEASURED hit and has a `--selftest` that fails if the known
instance stops being detected or if a genuine two-sided assertion is flagged. Wiring
it into `scripts/precision-gates.sh` or `check-sidecars.sh` would stop the class
recurring, but that is a policy call, not mine to make.


## DRAINED 2026-08-25 — 13 -> 0 MEASURED, and one probe had NOTHING BUT tautologies

All 9 remaining call sites fixed. The audit now reports `MEASURED: 0`, exit 0.
`--selftest` OK.

**Uniform disposition: demote to `add_data`.** In every case the quantity is a
recorded finding with no independent expectation — "did we find a violator?", "is the
verdict robust?", "does the pattern survive the control?" — so inventing an `expected`
would have fabricated an expectation the author never had. Two of the sites say so in
their own trailing comments: `# RAW, not a target` and `# report RAW (not a target)`,
in `su2_spinor_multiplicity_resolution`. The author knew it was not a check and used
`add_assertion` anyway, because that is the prominent slot and there is no equally
visible "record a finding" equivalent. That is the API shape driving the misuse.

**`threerow-crossing-a-dependence` had NO other assertions.** Its six (3 isotopes x 2
endpoints, from a 2-site loop) were its entire assertion set, under the comment
*"Falsifiable assertions: the SIGNS at the two physical endpoints, per isotope."*
Removing them leaves the witness with **zero** assertions. That is honest — it was
checking nothing before — but it means this witness has never verified anything, and
whoever wants a real gate there has to write the first one.

**One site is patched but NOT executed**: `threerow_isospin_parity_probe` cannot be run
to completion (see `qou-iav7` — ETA 1248 s on the ⁴He leg alone). The edit is
AST-verified well-formed and `add_data(key, value)` matches the signature, but no run
confirms it. Stated rather than glossed.

**A mistake worth recording.** My first patch of `su2_spinor_multiplicity_resolution`
broke it: the original `add_assertion` calls carried `tolerance=0, source="..."` on
lines below the ones I had read, and `add_data(key, value)` takes neither. It raised
`TypeError` on run. Caught only because I ran all seven probes rather than trusting the
AST edit — the source text is now preserved in a companion `_source` data key. An
AST-level edit that type-checks can still be wrong about the callee's signature.

LITERAL (17) deliberately untouched — several are intentional provenance statements
(`no_h4_fit_performed`) where the right move is `add_parameter`, not deletion.
