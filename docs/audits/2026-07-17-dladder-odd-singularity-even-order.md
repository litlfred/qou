# D-ladder parity resummation: the even/odd Gevrey split softens; ρ_odd unresolved

> **⚠ CONVENTION-C CONDITIONAL — scope note added 2026-09-06 (bean `qou-h6o3`).**
> This document's conclusions depend on the `c_k` precision ladder / `Q_β`, which
> AGENTS.md records as **convention-C-frame throughout and NOT re-derived** under
> the owner ruling of 2026-08-15 making convention D (`z = q³/(q²+1)`) canonical.
> Treat every `c_k`-dependent statement below as **C-conditional** until the
> ladder is re-derived (bean `qou-cds1`). The numbers here are correct *for C*
> and are kept as recorded — they need **scoping, not correction**. This note was
> applied mechanically to the 45 documents in this arc that reference the ladder;
> it asserts dependence on the ladder, not that any particular conclusion changes
> under D.


**Date:** 2026-07-17 · **Axis:** Q_β odd channel (c₃ S-carrier) resummation ·
**Tier:** numerical (scope-(a) measurement — self-correcting) · **Discipline:**
no c_k wired, no fit to QOU data, no tier change. Follow-through on #3861
(bar-odd half fixed-order Borel–Leroy at s≈0.068; bar-even half "drifts").

## What was tested

Two questions on the exact ℚ(√3) D-ladder to k=31
([`qbeta_dladder_parity_odd_singularity_even_order_probe.py`](../../computations/qbeta/qbeta_dladder_parity_odd_singularity_even_order_probe.py)):

1. **Odd half (S-carrier):** apply the fixed-order Borel–Leroy transform at
   s≈0.068 to the odd subseries and *locate* its Borel-plane singularity ρ_odd
   (dlog-Padé), then test ρ_odd against parameter-free candidates.
2. **Even half:** decide whether its "drift" is a single *higher* Gevrey order
   (slow estimator) or genuinely index-less — via the sliding-window local
   Gevrey exponent γ.

## Result — both are honest negatives / refinements

**Part 1 — ρ_odd unresolved.** The odd Borel–Leroy singularity comes out
ρ_odd ≈ 0.0160, with the nearest parameter-free candidate (Vol(4₁)/2π) **95 %
off** — i.e. **no clean constant** at k=31. ρ_odd is an unresolved *location*, not
a resummed S-value. (Consistent with the corpus finding that a clean odd-channel
action needs genuine Écalle acceleration, not a fixed-order Borel–Leroy dlog-Padé
at 16 terms.)

**Part 2 — the parity split softens toward a single order.** At k=31 **both**
parities' local Gevrey exponent are still *decreasing monotonically toward a
common small value*: even-k γ ≈ 0.085, odd-k γ ≈ 0.078 (gap **0.007**), both
trending down through the sequence (even: 0.47→0.33→0.18→…→0.093→0.085). Neither
is converged. This does **not** support "even is a distinctly higher fixed order"
(it is heading *toward* the odd value, not plateauing above it), nor "even is
index-less" (it decreases smoothly). The honest reading: **a single small Gevrey
order (~0.07–0.09) for the whole ladder**, with #3861's even/odd asymmetry looking
like a finite-k estimator-window artifact rather than two genuinely different
orders. **No single order is claimed** — only that the two-order reading is not
supported at k=31.

## Consequence

Neither result advances a resummed c₃/S value (the anti-laundering line holds);
both *narrow* the picture: (i) the odd-channel Borel singularity is not a
low-height multiple of Vol(4₁)/2π at attainable precision, and (ii) the
resummation order is (within finite-k reach) a **single** mild q-Gevrey index,
not a parity-graded pair — simplifying the Écalle-acceleration target to one
order. This corrects the #3861 two-order reading rather than confirming it.

## Honest scope (anti-laundering)

Scope-(a) measurement throughout. ρ_odd is a singularity *location*, not an
S-value; the Gevrey-order finding is a *refinement*, not a closure. No c_k wired;
no fit; no tier change. The genuine odd-channel resummation remains the Écalle /
Φ_b state-integral target (now against a single order).

## Cross-references

- Parity-split origin (#3861): the merged D-ladder parity Borel–Leroy result
- 2-adic parity grading + q-Gevrey class: [`2026-07-13-dladder-coupled-recurrence-and-2adic-parity-grading.md`](2026-07-13-dladder-coupled-recurrence-and-2adic-parity-grading.md)
- Exact-rung machinery: `qbeta_ck_sseries_exact_rational.py`, `qbeta_dladder_generating_function_structure_probe.py`
