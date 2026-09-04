# The b(λ)-decay is cancellation, not size — the conjugate-pair control (qou-o6ov)

**Date:** 2026-09-04
**Directive (owner):** "A=3 completion decides the size-vs-cancellation question."
**Scope:** scope-(a); one resolved question + one retracted reading of my own; nothing wired.
**Probes:** [`magnus_conjugate_pair_cancellation_probe.py`](../../computations/deltalambda/magnus_conjugate_pair_cancellation_probe.py) (the control),
[`magnus_curvature_commutator_identity_probe.py`](../../computations/deltalambda/magnus_curvature_commutator_identity_probe.py) (`--min-b` / `--max-dim` targeting)
**Follows:** #6534, which established `(★)` and left this open.

## The question

`(★)` (#6534, Lean-verified): `tr_λ(ρ·Ω₂^P) = (4/[2]_q²)·Σ_a tr_λ([ρ,σ_a]·σ_{a+1})`, for every λ.
That says *what* the decay object is, not *why* it decays with `b(λ) = n − λ₁`. Two candidates:

- **SIZE** — `[ρ,σ_a]` is itself smaller in high-`b` irreps ⇒ a norm bound
  `|tr| ≤ Σ_a ‖[ρ,σ_a]‖·‖σ_{a+1}‖` would capture the decay.
- **CANCELLATION** — `[ρ,σ_a]` is *not* smaller; the decay is signed cancellation in the pairing
  against `σ_{a+1}` ⇒ **no** norm bound can capture it, and a spectral route (as the hook bound
  #6520 took) is forced.

## Why the raw b-scan could not decide it — and misled me

`dim λ` varies wildly with `b`, so both `|tr|/dim` and the normalised norm mix a `b`-effect with a
`dim`-effect. Worse, **the normalised norm is U-shaped in `b`**: it falls to a minimum near mid-`b`
and rises again. At A=3 it runs `0.76 → 0.28 → 0.087 → 0.054` (min) `→ 0.11 → 0.24, 0.36, 0.36 →
0.955`. The first A=3 run was truncated at `b ≤ 4` — entirely inside the falling half — and so read
as "the norm falls with `b`", the opposite of the A=2 reading (`0.93 → 0.60 → 1.11 → 1.39`), which
had reached the rising half. **The two sizes never actually disagreed; one of them was half-measured.**
I recorded that as a live contradiction in #6534 and declined to claim either way, which was right,
but the "contradiction" itself was an artifact.

The targeting fix is cheap and worth keeping: **the high-`b` tail is not expensive, merely last in
enumeration order.** Since `dim λ = dim λ'`, the `b = 6…8` shapes at `n = 9` have dims 1–48, while
the costly `dim`-216 blocks sit at mid-`b`. `--min-b 6 --max-dim 50` returns the decisive tail in
about a minute, against hours for the full sweep.

## The control — conjugate pairs

`dim λ = dim λ'` **exactly**, while `b(λ') = n − (number of parts of λ)`. A conjugate pair is
therefore two irreps of *identical dimension* at very different `b` — the clean A/B test, with the
dimension confound removed by a theorem rather than by normalisation.

Measured (exact mpf, dps 140), ratios are higher-`b` partner ÷ lower-`b` partner:

| A | pair | dim | b → b' | trace ratio | **norm ratio** |
|---|---|---|---|---|---|
| 2 | (5,1) → (2,1⁴) | 5 | 1 → 4 | 0.0364 | **1.309** |
| 2 | (4,2) → (2,2,1,1) | 9 | 2 → 4 | 0.2672 | **1.194** |
| 2 | (4,1,1) → (3,1,1,1) | 10 | 2 → 3 | 0.1081 | **1.125** |
| 2 | (3,3) → (2,2,2) | 5 | 3 → 4 | 0.2096 | **1.243** |
| 3 | (8,1) → (2,1⁷) | 8 | 1 → 7 | **0.00343** | **1.265** |
| 3 | (7,2) → (2,2,1⁵) | 27 | 2 → 7 | 0.0206 | **1.263** |
| 3 | (7,1,1) → (3,1⁶) | 28 | 2 → 6 | 0.0133 | **1.227** |
| 3 | (6,3) → (2,2,2,1,1,1) | 48 | 3 → 7 | 0.0176 | **1.287** |
| 3 | (5,4) → (2,2,2,2,1) | 42 | 4 → 7 | 0.0926 | **1.290** |

**9 of 9 pairs: norm ratio ≥ 1 (1.13–1.31, tightly clustered near 1.25) while the trace ratio is
0.003–0.27.** At identical dimension the high-`b` partner's commutators are roughly **25 % larger**
and its trace is **4× to 290× smaller**. The sharpest single instance is `(8,1)` vs `(2,1⁷)`: same
dimension 8, norm `0.755 → 0.955`, `|tr|/dim` `33.65 → 0.115`.

## Answer

**CANCELLATION.** The `b(λ)`-decay is not a size effect. Consequences:

- **No norm bound can produce it.** `|tr| ≤ Σ_a ‖[ρ,σ_a]‖·‖σ_{a+1}‖` runs the wrong way on every
  conjugate pair measured — the bound *grows* by ~25 % exactly where the quantity falls by 1–2
  orders of magnitude. This is a **scope-(a) negative**: the norm route, alone and as-is, cannot
  reproduce the decay. It is not a proved exclusion of every norm-flavoured argument (a bound using
  the *signed* structure, or norms of a different object, is untouched).
- **The spectral route is the one that works, and now for a reason.** The hook bound (#6520) went
  through `e_j` of the Burau moduli rather than a norm; that was the route taken, and this says it
  was the route *available*. A general-λ bound should be spectral in the same sense.
- **`(★)` is unaffected** — it is a theorem, verified sorry-free. Only the interpretation moved.

## What I got wrong, and where it reached

In #6534 I first wrote the A=2-only reading into the Lean docstring as settled ("no norm bound can
produce it"). Commit `50ef169ae1` retracted that to "open, no claim either way" on seeing the
partial A=3 data. **The original claim was right and the retraction was over-cautious** — but both
were made on inadequate evidence, and only the conjugate-pair control settles it. The docstring now
states the resolved answer *with the control that establishes it*, not with the raw scan that
cannot. Sites touched: `MagnusCurvatureCommutator.lean` docstring, bean `qou-o6ov`, and this audit.

## Honest limits

- **9 pairs at A = 2, 3, dim ≤ 50.** The self-conjugate shapes ((3,3,3) at n=9) and the
  `dim > 50` pairs are not measured — not evidence either way, and named as skipped in the output.
- **The trivial/sign pair is excluded**, both traces being exactly 0 (scalars commute), so it
  carries no ratio.
- **`~1.25` is an observation, not a law.** Nine points, two sizes; no claim that the norm ratio
  has a limit or a closed form.
- The negative is **scope-(a)** as stated above, deliberately not scope-(b).

## Bottom line

At identical dimension, high-`b` irreps have *larger* commutators `[ρ,σ_a]` and *far smaller*
curvature traces — 9 of 9 conjugate pairs, norm ratio 1.13–1.31 against trace ratio 0.003–0.27. The
`b(λ)`-decay is cancellation in the pairing against `σ_{a+1}`, not a size effect; no plain norm
bound can reproduce it, and the spectral route the hook bound already takes is the one available
for the general λ. The apparent A=2/A=3 contradiction was a half-measured U-shape, now closed.
