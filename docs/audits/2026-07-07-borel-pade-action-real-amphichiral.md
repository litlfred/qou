# The f-map's resurgence action is REAL (4₁ amphichiral) — correcting #3478

**Date:** 2026-07-07 · **Axis:** z→c_k f-map keystone (Borel–Padé instanton action)
· **Tier:** structural-exact (Vol recovery, sign structure) + numerical (action value, order-limited)
· **Discipline:** no fit, no c_k value, no wiring, no tier change. This **corrects a
prior over-read** ([#3478](https://github.com/litlfred/qou/pull/3478)) per the
flip-flop / critical-distance rules.

## The decisive experiment

The f-map is the resurgence connection ([#3474](https://github.com/litlfred/qou/pull/3474));
its content is the **instanton action A** (the Stokes datum). #3478 estimated A from
only 6 Ohtsuki orders (dps 100) and read it as *complex/oscillating, |A|≈0.5*. This
run ([`qbeta_borel_pade_action.py`](scripts/qbeta_borel_pade_action.py), 6/6) sharpens
it: the 4₁ Ohtsuki ladder to **order 11 at dps 220** (Vol recovered to rel `6×10⁻²⁹`).

## Finding: the action is REAL-positive, ≈ 0.69

- **κ_k are all positive and monotone growing** (`0.554, 0.731, 2.655, 13.1, 84.6,
  677, 6444, 71114, 895302, 1.2×10⁷, 2.6×10⁸`). A single **real-positive** Borel
  singularity gives `b_k = κ_k/k! ~ C/A^k` — all one sign. A complex-conjugate pair
  `|A|e^{±iθ}` would give `κ_k ~ (k!/|A|^k)·2cos(kθ+φ)` — **sign-oscillating**. No
  oscillation through 11 orders ⇒ **real-positive dominant singularity**.
- Large-order ratio `A_k = k·κ_{k-1}/κ_k`: `…, 0.750, 0.735, 0.725, 0.715, …`
  (smoothly decreasing); Richardson (k=6..10) ⇒ **A ≈ 0.69**. Closest framework
  candidates `2/e ≈ 0.736` (rel 5.7%), `Vol/π ≈ 0.646` (rel 7%) — **none clean;
  not identified** (still order-limited).
- **Borel–Padé nearest-pole is Froissart-unstable** (jumps `0.71 → 0.049 →
  0.049+0.12j` across M=3,4,5) — the naive pole-picker grabs spurious
  pole–zero doublets. Reported as a cross-check; the **ratio method is the robust
  estimator** here, not Padé.

## Why REAL is *expected* — 4₁ is amphichiral

The figure-eight knot is **amphichiral**, so its Chern–Simons invariant `CS(4₁) = 0`,
hence the complex volume `𝔙(4₁) = Vol + i·CS = Vol` is **genuinely real**. So the
real action is not merely "no fit noise" — it is **forced by the knot's
amphichirality**. #3478's "complex `𝔙 = Vol ± iCS`" read was doubly wrong for 4₁:
it was low-order fit noise *and* it contradicted `CS(4₁)=0`.

This closes a loop with the even channel: the pion = **half-figure-eight** (also
amphichiral-derived), so the even channel is correspondingly **real** — consistent
with `e_k ∈ ℚ(√3)` (all real). **A genuinely complex action / complex 𝔙 would
require a CHIRAL knot (`CS ≠ 0`)** — which the figure-eight sector is not. If the
odd-channel scalar S needs complex structure, it must enter through a chiral knot
elsewhere, not the (amphichiral) figure-eight/pion.

## What this does and does not settle

- **Settles:** the 4₁/pion-sector resurgence action is real-positive (≈0.69),
  forced by amphichirality. Corrects the #3478 complex read.
- **Does not settle:** the exact value of A (order-limited; `2/e`/`Vol/π` are
  ~6–7% guesses, not identifications), nor the odd-channel S (still CAL-2 =
  Subgoal-2). The next step to pin A is the **exact saddle-point expansion** of the
  Kashaev sum to ~20 orders (rationals over ℚ(√-3)), rather than the numerical fit.

## Bottom line

The f-map's Stokes action for the figure-eight/pion sector is **real ≈ 0.69**,
consistent with `CS(4₁)=0`. The complex-volume story survives only for **chiral**
knots. This is a correction of my own #3478 preliminary — the cleaner computation
overturned the low-order read, exactly as the discipline intends.

## Cross-references

- Probe: [`qbeta_borel_pade_action.py`](scripts/qbeta_borel_pade_action.py)
- Prior (corrected): [#3478 resurgence action](2026-07-07-fmap-resurgence-action-and-pion-knot.md)
- f-map = resurgence: [#3474 c_3-even / S rigidity](2026-07-07-c3-even-solved-s-complex-volume-rigidity.md)
- Pion knot: [`pion-half-figure-eight.md`](../../content/quantum-observable-universe/braids-and-knots/pion-half-figure-eight.md)
