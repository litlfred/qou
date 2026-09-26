---
# qou-ujil
title: 'qou-x631 route 7 eliminated: the margin is at the CLT scale k^{3/2}, so concentration arguments cannot work'
status: completed
type: task
priority: normal
created_at: 2026-09-06T13:21:05Z
updated_at: 2026-09-26T11:03:19Z
---


Follows `qou-cze8` (route 6: p = 3 is special). That reduced the conjecture to the
single-cumulant statement `Cov_Planch(f^λ, R₄) ≤ 0`, i.e. `E_Q[Σ₃] ≤ 0` under
`Q ∝ (f^λ)³`. This measures the **margin**, and the answer constrains proof
strategy more than the sign does.

**Not progress toward a proof.** A seventh route eliminated, and evidence for
which of the remaining ones can work.

## The margin scales as k^{3/2}, not k

    E_Q[Σ₃] / k^{3/2}  =  −0.277 ± 0.02,   10 ≤ k ≤ 42

stable, oscillating, **not drifting**. The `/k` normalisation is ruled out
directly: `E_Q[Σ₃]/k` at k = 12, 24, 42 is −0.79, −1.34, −1.86 — it grows by a
factor ~2.4, so k is the wrong scale.

`k^{3/2}` is not an arbitrary fit. By **Kerov's CLT**, under Plancherel measure
`Σ₃` is asymptotically Gaussian with mean 0 and standard deviation `√3·k^{3/2}`.
So the f-biasing shifts `Σ₃` by

    E_Q[Σ₃]  ≈  −0.16 · sd_Planch(Σ₃)

— an **O(1) effect measured in standard deviations**, not a large-deviation one.

## Route 7, eliminated: concentration / limit-shape arguments

The first idea anyone reaches for is *"Plancherel concentrates on the
Vershik–Kerov–Logan–Shepp shape; evaluate there."* The scaling shows why that
cannot work. At the limit shape `Σ₃` contributes **zero** —
`E_Planch[Σ₃] = 0` exactly (`qou-cze8`, exact fact B) — so the entire signal is
the *correlation* between the `f^λ` bias and the Gaussian fluctuation mode.

Any argument that replaces λ by the limit shape, uses concentration of measure to
discard atypical λ, or bounds via large deviations, **discards exactly the term
being computed and proves 0 ≤ 0**.

## And it is evidence *for* route `qou-t5m1`

A proof must operate at the CLT scale and produce a correlation coefficient.
That is precisely what the Śniady genus expansion on the `(f^λ)³`-biased measure
is built to do. Of the phase-3 routes, this measurement says t5m1 is aimed at the
right object; `qou-0ml9` (RSK) is not excluded, and its Lean dependency landed in
`qou-t181`.

## A coincidence, quarantined

Mean of the last eight values (k = 28…42) is **0.27727**; `√3/(2π)` = **0.27566**.
Agreement 0.6 %.

**Recorded as a target to check a future derivation against, never as a criterion
to search on.** The sequence still oscillates by ±0.02 and drifts slightly upward
over the measured range, so the data does not establish that a limit exists, let
alone its value. If an argument independently produces a constant, compare it
here — do not fit to it.

## Arithmetic

`f^λ` by hook length in Python integers; `E_Q[Σ₃] = 3·cov(k)/M(k)` formed as an
exact `Fraction` before any float. At k = 42, `(f^λ)³` exceeds 10⁶⁰ and both
`cov(k)` and `M(k)` are exact integers of that size — a double would have
destroyed the ratio. The four `float64-ok` annotations cover display and two
comparisons whose slack (0.02 against a 0.06 spread; a factor 1.7 against a true
factor 2.4) is far outside double precision.
