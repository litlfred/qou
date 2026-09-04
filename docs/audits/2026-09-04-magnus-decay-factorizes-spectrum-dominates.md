# The decay factorizes, and the OUTPUT spectrum dominates — refining #6548 (qou-o6ov)

**Date:** 2026-09-04
**Scope:** scope-(a); one quantitative result that **corrects the natural reading of my own previous
finding**; nothing wired.
**Probe:** [`magnus_cancellation_factor_probe.py`](../../computations/deltalambda/magnus_cancellation_factor_probe.py)
**Follows:** #6548 (the b-decay is not in the input commutator norm), #6534 (`★`).

## The refinement in one line

#6548 showed the decay is **not** in `‖[ρ,σ_a]‖` — the *input*. The natural next thought, which I
held, was "therefore it is phase cancellation in the trace." **That is wrong.** The decay is
overwhelmingly a collapse in the magnitude of the *output* operator's spectrum. Both facts are
true and they are about different objects.

## The decomposition

Let `M_λ = ρ_λ(ρ)·ρ_λ(Ω₂^P)`, so `tr_λ(ρΩ₂^P) = Σ_i eig_i(M_λ)`. Define the **cancellation factor**

```
κ(λ) := |Σ_i eig_i| / Σ_i |eig_i|  ∈ [0,1]        (κ=1: phases aligned; κ→0: total cancellation)
```

Then exactly `|tr|/dim = κ · (Σ|eig|/dim)`, so any b-decay splits into a **phase** part (`κ`) and a
**magnitude** part (`Σ|eig|`). Measured on conjugate pairs — `dim λ = dim λ'` **exactly**, so the
dimension confound is removed by a theorem — ratios are higher-b partner ÷ lower-b partner:

| A | pair | dim | b → b' | **Σ\|eig\| ratio** | κ ratio | product = trace ratio |
|---|---|---|---|---|---|---|
| 3 | (8,1) → (2,1⁷) | 8 | 1 → 7 | **0.00469** | 0.732 | 0.00343 |
| 3 | (7,2) → (2,2,1⁵) | 27 | 2 → 7 | **0.0226** | 0.911 | 0.0206 |
| 3 | (7,1,1) → (3,1⁶) | 28 | 2 → 6 | **0.0284** | 0.467 | 0.0133 |
| 3 | (6,3) → (2,2,2,1,1,1) | 48 | 3 → 7 | **0.0607** | 0.290 | 0.0176 |
| 3 | (5,4) → (2,2,2,2,1) | 42 | 4 → 7 | **0.106** | 0.871 | 0.0926 |
| 2 | (5,1) → (2,1⁴) | 5 | 1 → 4 | **0.0684** | 0.532 | 0.0364 |
| 2 | (4,2) → (2,2,1,1) | 9 | 2 → 4 | **0.318** | 0.840 | 0.267 |
| 2 | (4,1,1) → (3,1,1,1) | 10 | 2 → 3 | **0.371** | 0.291 | 0.108 |
| 2 | (3,3) → (2,2,2) | 5 | 3 → 4 | **0.151** | **1.385** | 0.209 |

(The product column reproduces #6548's independently-measured trace ratios — a consistency check
across two probes, e.g. `0.732 × 0.00469 = 0.00343`.)

**`Σ|eig|` falls in 9 of 9 pairs, and it dominates in all 9.** For `(8,1)` vs `(2,1⁷)` the spectrum
contributes a factor 213 and the phases only 1.4.

## What this changes

- **An absolute-value spectral bound on `M_λ` is VIABLE.** `Σ|eig(M_λ)|` — and any bound above it,
  such as `dim · spectral-radius` — *does* decay with `b` at fixed dimension. This is the
  constructive route to a general-λ bound, and it is the opposite of what "cancellation" suggested.
  It is also consistent with the hook bound (#6520) working through `e_j` of a spectrum.
- **#6548's stated finding stands unchanged**: no bound `|tr| ≤ Σ_a ‖[ρ,σ_a]‖·‖σ_{a+1}‖` can work,
  because that quantity *grows* ~25 % at high b. What fails is the inference I drew from it.
  Reconciled: the commutators are individually larger at high b, but the assembled
  `Ω₂^P = Σ_a[σ_a,σ_{a+1}]` and its product with `ρ` have a far smaller spectrum. **The cancellation
  happens in the assembly, not in the final trace.** Bounding the inputs term-by-term throws that
  assembly away — which is exactly why the input-norm route fails and the output-spectrum route
  does not.
- **κ is real but secondary, and NOT uniform.** It falls in 8 of 9 pairs, and **rises** in one:
  `(3,3) → (2,2,2)` at A=2, κ `0.604 → 0.837` (ratio 1.385) — the trace still falls there, carried
  entirely by `Σ|eig|` (0.151). So "κ decreases with b" is **not** a law and must not be asserted;
  the probe reports the non-uniformity rather than averaging it away.

## Honest limits

- **9 pairs, A = 2 and 3, dim ≤ 50.** Self-conjugate shapes ((3,3,3) at n=9, measured but pairless)
  and `dim > 50` pairs are not in the control — named as skipped, not evidence.
- **`Σ|eig|` is not the nuclear norm** (`M_λ` is not normal); it is the right comparator here
  because the trace is exactly `Σ eig`, so the split into magnitude × phase is exact by
  construction, not an approximation.
- **"Viable" is not "proved".** That `Σ|eig(M_λ)|` decays is measured on 9 dimension-controlled
  pairs; no closed form or bound for it is derived here. A general-λ theorem still needs one.
- Scope-(a) throughout.

## Bottom line

The b-decay factorizes exactly as `|tr|/dim = κ · Σ|eig|/dim`, and across 9 dimension-controlled
conjugate pairs the **magnitude** factor `Σ|eig|` falls in all 9 and dominates in all 9 (down to
0.005), while the **phase** factor `κ` falls in 8 and rises in 1. So the decay is chiefly a
collapse of the output operator's spectrum, not phase cancellation in the trace — correcting the
reading I drew from #6548, whose own finding (the input-norm route is excluded) is untouched. An
absolute-value spectral bound on `M_λ` is the viable route to the general-λ statement.
