# The o(dim) is dominated by TRACE-ORTHOGONALITY, not the commutator norm (qou-o6ov)

**Date:** 2026-08-31
**Directive (owner):** next.
**Scope:** scope-(a); no MeV, no fit, nothing wired.
**Probe:** [`magnus_single_window_frobenius_localization_probe.py --A 3`](../../computations/deltalambda/magnus_single_window_frobenius_localization_probe.py) (CS-slack section)
**Follows:** #6339 (localized to `‖[ρ,A_a]‖_F`), #6349 (norm route dead — local commutator
`Θ(√dim)`), #6352 (the commutator cancellation is distributed).

## The question this settles

The chain is `|t| = |tr([ρ,A_a]·A_{a+1})| ≤ ‖[ρ,A_a]‖_F·‖A_{a+1}‖_F` (Cauchy–Schwarz on the
trace pairing). The open sub-question after #6352: is the measured `o(dim)` **all** in the
commutator norm `‖[ρ,A_a]‖_F` (CS tight), or is there **extra** cancellation in the trace step
(CS loose)? The discriminator is the **CS slack**
`slack = ‖[ρ,A_a]‖_F·‖A_{a+1}‖_F / |t| ≥ 1`.

## Measured (A=3, exact mpf, interior windows, per b)

The slack **grows sharply with b** in *every* window:

| window | b=1 | b=2 | b=3 | high b |
|---|---|---|---|---|
| (0,1) | 2.7 | 8.9 | 242 | 100s–1000s |
| (1,2) | 3.8 | 8.6 | 34 | up to ~4000 |
| (2,3) | 2.5 | 4.8 | 11 | 50–220 |
| (5,6) | 2.5 | 4.8 | 11 | 60–110 |

(Exact high-b magnitudes are **noisy** — max-dim-partition-per-b sampling, and `|t|` can be
near-zero for particular partitions — so read the robust signal: slack rises from **single
digits at b=1–2 to 10²–10³ at high b**, monotone in trend, in all 7 windows.)

## Interpretation: the germ direction is being vacated

`slack = ‖X‖_F‖Y‖_F / |⟨X,Y⟩_F| = 1/|cos θ|` for `X = [ρ,A_a]`, `Y = A_{a+1}ᵀ` in the
Frobenius inner product. So **slack → large means `cos θ → 0`**: as the diagram fattens
(`b` grows), the word-commutator `[ρ,A_a]` becomes **nearly trace-orthogonal to the germ
`A_{a+1}`**. The trace `tr([ρ,A_a]·A_{a+1})` is the *component of `[ρ,A_a]` along the fixed
local germ direction*, and that component vanishes far faster than `[ρ,A_a]`'s norm.

**So the dominant driver of the `o(dim)` at high `b` is trace-orthogonality, not norm decay.**
The commutator norm `‖[ρ,A_a]‖_F/√dim` does decrease with `b` (#6339), but only modestly and
possibly to a plateau; the *large* effect is that `[ρ,A_a]` and `A_{a+1}` become nearly
orthogonal.

## What this does to the proof target

The whole arc's target restates cleanly as an **overlap / orthogonality** statement, not a
norm bound:
```
⟨ ⁅ρ_λ, A_a⁆ , A_{a+1} ⟩_Frobenius / dim_λ  →  0   as  b(λ) → ∞,
```
i.e. the word-commutator's projection onto the fixed 3-strand germ direction vanishes. This is
the precise form of the sign/phase cancellation the earlier probes pointed to — and it is a
*matrix-element* decay (an equidistribution-flavoured statement about how the braid word
spreads `A_a` away from the local germ subspace), which is exactly the kind of object the
cumulant / connected-diagram machinery computes.

## Honest limits

- **A=3 only, interior windows, dim ≤ 200, max-partition-per-b.** The slack magnitudes are
  noisy; the robust claim is the *qualitative growth* (single digits → 10²–10³), uniform across
  all 7 windows.
- **Not proved.** This is a measurement of *where* the cancellation lives (dominantly the trace
  overlap), not a proof that it vanishes.
- **Both effects are real.** The commutator-norm decay (#6339) and the distributed telescoping
  cancellation (#6352) still hold; this shows a *third*, larger effect on top — the trace
  orthogonality — dominates at high `b`.

## Bottom line

The `o(dim)` is **not** primarily a norm effect: the CS slack grows from ~3 to 10²–10³ with
`b`, so `[ρ,A_a]` becomes nearly **trace-orthogonal** to the germ `A_{a+1}`. The clean proof
target is therefore the normalized overlap
`⟨⁅ρ_λ,A_a⁆, A_{a+1}⟩_F / dim_λ → 0` — a matrix-element / equidistribution statement, the
sharpest form yet of the sign-tracking cancellation that the norm route (#6349) provably cannot
reach. Still open, but now stated as the right kind of object.
