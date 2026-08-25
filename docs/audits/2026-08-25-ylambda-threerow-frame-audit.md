# The ≥3-row stratum is a structural zero under convention D — which consumers still reason about it

**Date:** 2026-08-25 · **Bean:** `qou-4dq1` (sweep), instance-level `qou-58w3`, `qou-prjo`
**Tool:** [`computations/audits/ylambda_threerow_frame_audit.py`](../../computations/audits/ylambda_threerow_frame_audit.py)

## The fact this rests on — established, not re-derived

Under the canonical trace convention **D** (`z = q³/(q²+1)`, owner ruling 2026-08-15)
the Wenzl level relation collapses to `Q^r = Q²`, i.e. **`r = 2`**.
`schur_principal_mpmath` is then the SU(2) two-row specialisation `s_λ(1, Q)`, so
`y_λ = 0` for every partition with three or more rows.

Both halves are Lean-proved sorry-free on `main` — `wenzlLevel_conventionD` and
`schurPrincipal_eq_zero_iff` (all `n`, all `r`) — and
[`two_row_support_recount.py`](../../computations/deltalambda/two_row_support_recount.py)
measures what the truncation removes. Nothing here re-derives them.

Measured at the proton pin, 40 dps:

| n | partitions | ℓ(λ) ≥ 3 | max\|y_λ\| on that stratum | noise floor | structural zero | genuinely negative y_λ |
|---|---|---|---|---|---|---|
| 6 | 11 | 7 | 1.387e-42 | 1.153e-33 | yes | 0 |
| 9 | 30 | 25 | 3.343e-43 | 2.212e-34 | yes | 0 |
| 12 | 77 | 70 | 6.555e-44 | 3.966e-35 | yes | 0 |

`Q^r = 1.5179532498183459375 = Q²`, `r = 2.0`.

## Why a sweep

Code written before the 2026-08-09 ruling can carry a premise the ruling
falsifies, and it does **not** fail loudly when it does. Three failure shapes,
all observed:

1. **Round-off reported as a measurement.** A filter on `y < 0` picks up the
   ~1e-42 residue in the zeroed entries.
   [`mu3_door_budget_probe`](../../computations/deltalambda/mu3_door_budget_probe.py)
   printed *"the negative-weight blocks supply ~1/7617139225999999870250124307207290880000
   of what the door needs"* from a `Σ|y_neg|` of `1.04e-42` (fixed, PR #4673).
2. **A sum or ratio over an empty set.** Any quantity of the form
   `(something over ℓ ≥ 3) / (something else over ℓ ≥ 3)` is noise ÷ noise.
3. **A C-frame narrative running over D-frame arithmetic.** The prose describes
   `r = 2.5995` while the code returns `r = 2`, and the two never meet.

## Confirmed instance: `threerow_qcross_trend_probe.py`

This is shape (3) in its strongest form, and it prints a false arithmetic claim.

The probe's docstring, its `_D_wenzl`, its `U_STAR`, and its line-223 symbolic
identity all describe **convention C**:

```
Q^r = u³/D(u),  D(u) = −u⁶−u⁴+u³+u²+1,  u* = 1.13068544546204…,  r(q₀) = 2.5995
```

The code calls `_wenzl_constants`, which on `main` returns **convention D**.
Measured side by side at q₀:

```
Q^r from the corpus (LIVE)              1.517953249818345896   = Q²  ⇒ r = 2.0
Q^r = u³/D(u)  (the probe's own text)   1.720251751213844854        ⇒ r = 2.5995
```

The consequences are visible in its own output:

- `level r(0.98q*) = 2.0 (real);  r(1.45) = 2.0  ← COMPLEX ⇒ OFF-BRANCH` — it
  prints `2.0` and labels it complex. Under D, `Q^r = Q²` is entire; there is no
  pole, so `q*` does not exist and the "real-level branch" is all of `q > 0`.
- The level-integer ladder `q_k (r(q_k) = k)` prints `r = 2.0` at **every** rung
  from `q_2` to `q_10`.
- `⇒ q₀ ∈ (q_2, q_3);  r(q₀)=2.0 ∉ ℤ` — **`2.0 ∉ ℤ` is false.** Under C,
  `r = 2.5995 ∉ ℤ` was the real and interesting claim; under D it inverts.
- Its headline object `G_n(q) = Σ_{ℓ(λ)≥3} y_λ Δ_λ` is identically zero, so the
  "is `q_cross(n)` a structured sequence in `n`?" question has no content. The
  measured crossing list is **identical for every n from 3 to 21** —
  `1.000007 1.000032 1.000178 1.000188 1.001887 1.009783 1.092527 1.103019 1.107539 1.222267` —
  with one spurious extra root at n = 11 and n = 18. An n-dependent object does
  not produce an n-independent answer; a bisect-on-sign-change over round-off does.

**Scope, stated:** this is a scope-(a) finding about *this probe*. It does not
refute the general-`r` mathematics the probe describes — the `Q^r = u³/D(u)`
family is a legitimate object — it says the probe is *not computing it*, because
its arithmetic is pinned to `r = 2` while its narrative is pinned to `r = 2.5995`.
Either the narrative is corrected to D (and the object becomes trivial), or the
arithmetic is explicitly re-pinned to the general-`r` family and the probe declares
itself an off-canon comparison. It cannot stay as it is.

## Triage: 158 consumers, 27 flagged

The tool has two layers because a source-only detector cannot decide this.

**Layer 1 — source triage.** High recall, explicitly *not* a verdict. Its own top
hit is a **false positive by construction**: `mu3_door_budget_probe` scores 28 on
negative-weight vocabulary precisely because it now *documents* the trap and
carries the fix. A file that discusses the defect scores like a file that has it.
(The audit also flagged *itself* on the first run, for quoting `2.5995` and
`1.7202` in its own docstring; it now excludes its own path, and says why.)

Tags: `HARD-CODES C's LEVEL` is the strongest single signal;
`declares a C-vs-D comparison` means reasoning about the annihilated stratum is
**correct by design** (both tags together are expected — see
`binding_sum_C_vs_D_per_isotope_probe`); `has a noise floor` is not a clearance
but rules out the `mu3_door_budget` error.

**Layer 2 — numeric confirmation.** `--measure` evaluates the stratum directly.
A value cannot be stale, mislabelled, or re-spelled and still be nonzero. This is
the layer that decides.

`--selftest` fails unless the known instance is detected *and* the stratum
measures as a structural zero, so a future narrowing cannot quietly report a clean
tree.

## A trap the selftest caught, in the audit itself

The first version tested `sum|y| == 0`. It **failed**, reporting `1.27e-42`.

The vanishing is a polynomial identity, but in finite precision it is *reached by
cancellation*, so the computed stratum sits near 1e-42 rather than at a clean
zero — and the value depends on how `q` is spelled: `mpf("1.1099785827513808")`
gives exactly `0.0` where the full-precision `Q_MP` gives `1.27e-42`. Both are the
same structural zero. **An equality test answers a question about the arithmetic,
not about the mathematics.** Compare against a noise floor tied to the working
precision — which is exactly the fix `mu3_door_budget_probe` needed, arriving one
layer up in the tool written to find it.

## Not done

The remaining 26 flagged files are **candidates**, not findings. Each needs
`--measure` pointed at its specific object plus a read of whether it is a declared
comparison. Highest-value by signal, excluding the confirmed instance and the
declared comparisons: `threerow_4he_completion_probe`,
`delta_lambda_closure_tl_support_probe`, `threerow_crossing_a_dependence_probe`,
`threerow_sign_crossing_probe`, `mu3_frechet_perblock_probe`,
`ylambda_sign_content_threshold_probe`.

Known instance already beaned by a sibling and not re-declared here:
`qou-58w3` (`he4-two-row-dominance` pins a convention-C 866/1000 that D makes
exactly 1).
