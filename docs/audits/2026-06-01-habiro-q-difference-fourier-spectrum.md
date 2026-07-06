# Habiro q-difference equation — Fourier/root-of-unity spectrum of tr_M

**Date:** 2026-06-01
**Probe:** [`habiro_q_difference_fourier.py`](../../computations/habiro/habiro_q_difference_fourier.py)
→ `habiro-q-difference-fourier.witness.json`
**Goal arm:** 1ppQ-Q_β (`docs/coordination/1ppq-qbeta.md`)
**Probe claim:** `probe-qbeta-habiro-element-search` — the **modular
bootstrap / q-difference** route (queue candidate #4), made concrete.
**Status:** spectral **characterization** (no closure, no fit). Produces
three exact structural facts about the Markov trace's q-difference form.

---

## Method — Fourier diagonalises the q-difference shift

The open object is the scaling map `f: Δtr_M ↦ Q_β`. The principled route
is Habiro's q-difference equation `(1 − σ_q)·F = δ·(q;q)_∞`, where
`σ_q : q ↦ q·ζ` is a root-of-unity shift. **Fourier transform
diagonalises shift operators** — the modes over the cyclic group `⟨ζ⟩`
are the eigenvectors of `σ_q`.

The repo already carries the **exact finite Habiro expansion** (integer
`a_m`, `habiro-coefficients-atomic.witness.json`):

```
tr_M(u) = (1/D(u)) · Σ_{m=0}^{8} a_m(u) · (u;u)_m ,   u = q^{1/2}
```

The handle: **`(u;u)_m = Π_{k≤m}(1−u^k)` vanishes at any primitive d-th
root of unity with d ≤ m.** So evaluating `tr_M` at `ζ_d = e^{2πi/d}`
keeps only the `m < d` modes — the Witten–Reshetikhin–Turaev / modular-
tensor truncation (`bar_involution.root_of_unity_truncate`). This is the
Fourier transform that turns the q-difference equation into per-mode
algebra.

> **Notation note (a real collision caught here):** the Habiro variable
> is `u = q^{1/2}` (per `habiro_coefficients_atomic.py` line 23), **not**
> the precision-ladder variable `u_ladder = b·ℏ²`. The two are distinct;
> this probe works in the Habiro `u = √q`, where `u ↦ 1/u` is exactly the
> bar involution `q ↦ q⁻¹`. (The numeric sanity reproduces the
> witness-cited `tr_M(p, q₀) = 1.0653` only with the correct `u = √q`.)

## Three exact spectral facts

| d | surviving modes | \|tr_M(p)\| | \|tr_M(n)\| | \|Δtr_M\| |
|---|---|---|---|---|
| 2 | 2 | 0.5000 | 0.5000 | **0.0000** |
| 3 | 3 | 0.6614 | 1.0000 | 1.5612 |
| 4 | 4 | — | — | **POLE** |
| 5 | 5 | 2.2758 | 2.3757 | 1.5429 |
| 6 | 6 | 0.6614 | 1.0000 | 1.5612 |
| 7 | 7 | 0.4148 | 1.1685 | 1.5786 |
| 8 | 8 | 1.5000 | 0.0000 | 1.5000 |

1. **d=2 (bar / charge-conjugation mode): Δtr_M = 0 exactly.** The proton
   and neutron Markov traces are *identical* in the lowest Fourier mode.
   The entire proton–neutron difference lives in the **d ≥ 3** modes.
   This is the spectral statement of why the p/n split is a higher-order
   (subleading) effect.

2. **d=3 ≡ d=6 (period-3 resonance).** The two rows are identical to all
   digits — a clean period-3 structure in the root-of-unity tower. (Note
   d=6 surviving-mode count is larger, yet the value coincides — the new
   modes' contributions cancel at ζ_6.)

3. **ζ_4 = i is a genuine pole.** The Habiro denominator
   `D(u) = 4u¹⁹(u²+1)` vanishes at `u = i` while the numerator does not.
   The Markov trace has a **real singularity at the 4th root of unity** —
   a structural feature of the q-difference equation, not a numerical
   artifact. (The probe detects `D(ζ_d)=0` symbolically and reports POLE
   rather than emitting `nan`.)

## Bar-symmetry sector

With `u = √q`, the bar involution `q ↦ q⁻¹` is `u ↦ 1/u`. Splitting
`Δtr_M` into bar-even `[Δtr_M(u)+Δtr_M(1/u)]/2` and bar-odd parts: both
sectors are non-trivial (even leads at `u¹`, odd at `u⁰` in the Habiro
`u`). Bar-even = charge-conjugation-symmetric = physical. PR #1602 found
the scaling map `f` must be a **cancellation (bar-even) construction**;
this probe locates the symmetry sectors of `Δtr_M` that such an `f` acts
on.

## What this buys the f-search

The q-difference / Fourier route gives `f` a **finite spectral target**:
the 6 non-pole root-of-unity values of `Δtr_M` (d = 2,3,5,6,7,8) plus the
ζ_4 pole structure. Any candidate `f` must reproduce this exact spectrum.
The d=2 vanishing and the period-3 resonance are strong, non-obvious
constraints that the bare eigenphase (PR #1602) and the per-block sum
(PR #1593) did not expose.

## Discipline

Exact symbolic throughout (witness-cited integer `a_m`; exact
root-of-unity evaluation). **No fitted form proposed; no c_k value; no
closure claimed.** Spectral characterization only, tiered per
`canonical-ck-tiered-not-binary`.

## Next step

Solve the q-difference equation `(1−σ_q)F = δ(q;q)_∞` mode-by-mode using
this spectrum as boundary data: the ζ_d values are the Fourier
coefficients, and the recursion among them (the period-3 resonance + the
ζ_4 pole residue) should determine `f` up to the bar-even gauge. This is
the genuine subgoal-2 research target — multi-session, but now with an
exact finite spectral target instead of a value-chasing search.

## Cross-references

- Eigenphase ≠ f (the u¹-cancellation constraint): [`2026-06-01-qbeta-eigenphase-not-f-falsified-at-u1.md`](2026-06-01-qbeta-eigenphase-not-f-falsified-at-u1.md)
- Order audit (per-block √u vs ladder u³): [`2026-05-31-qbeta-c3-order-audit-accidental-coincidence.md`](2026-05-31-qbeta-c3-order-audit-accidental-coincidence.md)
- Habiro derivation gap plan (the exact a_m foundation): [`2026-05-30-qbeta-habiro-derivation-gap-plan.md`](2026-05-30-qbeta-habiro-derivation-gap-plan.md)
- Recursive pair-rules + Habiro PDE: [`2026-05-30-qbeta-recursive-pair-rules-and-habiro-pde.md`](2026-05-30-qbeta-recursive-pair-rules-and-habiro-pde.md)
- Coordination ledger: [`docs/coordination/1ppq-qbeta.md`](../coordination/1ppq-qbeta.md)
