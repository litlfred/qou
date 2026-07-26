# Flavor-split α: the positive-weight pair product has a ½ ceiling (Lean-proved exclusion)

**Date:** 2026-07-26 · **Branch:** `claude/even-moment-positivity-proof-qvxk1b` · **Tier:** proved
scope-(b) exclusion (Lean, sorry-free) + exact-`Fraction` α confirmation · **Discipline:** scope-(a)
for the α value; **scope-(b)** for the exclusion (cite the proved invariant); no fit; nothing wired;
L2 unchanged (2/7). **Sharpens:**
[`2026-06-29-flavor-split-partial-derivation.md`](2026-06-29-flavor-split-partial-derivation.md) Part 2a.

## Context

The p–n flavor split is `Δm_pn/M_N = leading·(1 + α·leading)`, with
`leading = (q−1)²(1−q⁻⁴)/3` **proved** (`prop:flavor-split-substrate`) and the second-order
normalization **α ≈ 0.929254** the single open coefficient. The partial-derivation audit established
the *form* (`α·leading²`, second-order) rigorously and bracketed `α ∈ (⅓, 1]` between two
parameter-free readings: the **pair-count** reading (Part 2a, equal split → `(m−1)/(2m) ≤ ½`) and the
**self-energy / geometric** reading (Part 2b, `leading/(1−leading)` → `α = 1`).

## Result — the pair-count reading is excluded for *all* positive weights, not just equal split

Model the split as a multiplicative pair product `1 + split = ∏_k (1 + s_k)` with `Σ_k s_k = leading`
and `s_k > 0`. The second-order coefficient is `α = (Σ_{k<l} s_k s_l)/(Σ_k s_k)²`. Then:

> **`α < ½` for every positive-weight pair product** (Lean:
> [`QOU.FlavorDressing.pairSum_lt_half_sq`](../../content/quantum-observable-universe/lean/QOU/FlavorDressing/PairProductCoefficientBound.lean),
> sorry-free). Proof: the Newton identity `(Σs)² = Σs² + 2·Σ_{k<l}s_k s_l` gives
> `2·Σ_{k<l}s_k s_l = (Σs)² − Σs² < (Σs)²` since `Σs² > 0` for a nonempty positive list.

The equal-split value `(m−1)/(2m)` is the **maximum** of this ratio (it minimizes `Σs²` at fixed
`Σs`); **unequal weighting lowers α toward 0**. Since the measured

    α = 0.929254490280  (proton anchor)  =  0.929254548073  (muon anchor)   [drift 5.8e-8]

exceeds `½` by `0.429`, **no positive-weight multiplicative pair product can produce it** — a
structural exclusion via the proved invariant `α < ½` (scope-(b)).

### What this corrects / sharpens in Part 2a

Part 2a excluded only the *equal-split* count and closed with "the pairs are **not** equally
weighted — the swapped pair must dominate." That direction is a dead end: pair **dominance** (unequal
weighting) drives α *down* toward 0, i.e. **away** from 0.929, not toward it. The correct statement is
the stronger one proved here — the *entire* positive-weight pair-count family is capped at `½`, so the
door Part 2a left ajar ("maybe unequal weighting reaches 0.929") is now shut.

## Consequence for the α-derivation

The `α`-derivation must live on the **self-energy / geometric-series side** (`split =
leading/(1−leading)`, coefficient `1`; overshoots 0.929 by 7.6%), **not** the pair-count side (capped
at `½`; undershoots by ≥ 2×). The open question is thus specifically: *what damps the geometric
self-energy series from `α = 1` down to `α ≈ 0.929`* — a `~7.1%` reduction of the 3-strand spectator
re-coupling, not a pair-multiplicity count. This narrows the search to a one-sided problem.

## State of the α-derivation after this narrowing (forward-derivation wall)

With the pair-count side excluded, the natural forward attempt is to make `α` *fall out* of an
existing categorical object rather than be fitted. Checked, and it does **not**:

- **The corpus interface object consumes δ; it does not derive α.** The p-n interface factor
  `f_pn = z − h·(½ − δ/4)` (`closed_form_tau_M.py`) takes `δ = flavor_split_subleading(q)` as an
  **input**. Reading a coefficient back out of it is circular — no derivation of `α`.
- **The wired production δ uses the wrong shape (a live discrepancy).**
  `flavor_split_subleading(q) = leading·(1 + ℏ_q³)` is labelled in-code *"⚠ POSITED — NOT DERIVED"*
  and supplies only **76%** of the gap (`(C_true−1)/ℏ_q³ = 1.314`). The correct second-order shape is
  `leading²` (Part 1 of the partial-derivation audit), not `ℏ_q³`. So the production p-n split carries
  a known posited-and-insufficient subleading term — independent of whether `α` is ever pinned.
- **What remains is a single-number self-energy target.** Combining the ½-ceiling with the geometric
  self-energy reading, `split = leading/(1 − β·leading)` with `α = β`; the measured `β ≈ 0.929254 =
  1 − 0.0707` must come from the **3-strand spectator re-coupling amplitude**. No forward categorical
  construction for that amplitude exists in the corpus — building it is the open research the prior
  audit named. **Anti-fit note:** `0.0707 ≈ h_q/3` (1.4% off) and `1 − 1/14 = 0.9286` (0.07% off) are
  the documented numerical temptations; neither falls out of any construction, both are **rejected**
  per anti-flip-flop discipline.

The α-derivation is therefore a *sharper* open problem after this narrowing — pinned to one categorical
amplitude — not a closure. This is the honest, expected outcome of the forward attempt.

## Honest scope

A **narrowing**, not a closure. `α ≈ 0.929254` itself remains **underived** (the anti-fit discipline
still forbids matching it to `13/14 = 0.92857` or any clean form). This result does **not** move the
L2 dashboard (Δ_pn / m_n still miss 100× by ~160×); it removes one of the two candidate mechanisms so
future work concentrates on the self-energy normalization. The proved invariant is over positive
reals; a signed/complex-weight product is *not* excluded (and is where a `> ½` coefficient could still
originate — a distinct, still-open mechanism).

## Artifacts

- Lean (sorry-free, lean-direct exit 0): [`QOU/FlavorDressing/PairProductCoefficientBound.lean`](../../content/quantum-observable-universe/lean/QOU/FlavorDressing/PairProductCoefficientBound.lean) — `sq_sum_eq`, `pairSum_lt_half_sq`.
- Probe (exact α + bound sweep, exit 0): [`computations/probes/flavor_split_pair_product_half_ceiling_probe.py`](../../computations/probes/flavor_split_pair_product_half_ceiling_probe.py).

## Cross-references

- Partial derivation (the bracket): [`2026-06-29-flavor-split-partial-derivation.md`](2026-06-29-flavor-split-partial-derivation.md)
- Closed-form coverage: [`2026-06-29-color-weighting-coverage-and-flavor-split-closed-form.md`](2026-06-29-color-weighting-coverage-and-flavor-split-closed-form.md)
- L2 shared-root: [`2026-05-30-l2-100x-status-3-failing-shared-root.md`](2026-05-30-l2-100x-status-3-failing-shared-root.md)
