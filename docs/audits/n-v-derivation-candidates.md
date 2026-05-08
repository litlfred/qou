# N_v topological invariant — derivation candidates

**Status**: open paper-side research. Numerical exploration of
candidate closed-forms.

## Setup

Per [`hadron-half-life-verification.md`](../../content/quantum-observable-universe/observations/hadron-half-life-verification.md):

```
v (weak scale) = N_v · m_e / 3        — N_v is the open input
G_F = 1/(√2 v²)                       — derived
```

CODATA: `v = 246.220 GeV`, `m_e = 0.510999 MeV` ⇒ `N_v_target = 1.4455 × 10⁶`.

The categorical predictions need `N_v` to close the Layer-3 decay
rates. Closed-form structural derivation is the open problem.

## Strategy 1 — pure brane-tower count

`v / m_e ≈ q^L` with `L = log_q(v/m_e) = 125.41` "Hecke generations".

This is **circular**: we cannot derive `v` from `q + m_e` alone if `L`
is itself read off from the experimental ratio.

**Verdict**: not a derivation. Useful only as a unit-conversion check.

## Strategy 2 — factor·q^L closure with structural prefactor

Search for `N_v = factor · q^L` with `factor` a categorical constant
(`|S_5|`, `[k]_q`, `h^k`, etc.) and `L` integer (= a structural
generation depth, not a fitted parameter).

| candidate `factor` | nearest `L` | predicted `v` (GeV) | err vs CODATA |
|---|---:|---:|---:|
| `120 = \|S_5\|` (Bring autom group) | **90** | **244.79** | **−0.581%** |
| `h³ = (q-q⁻¹)³` | 181 | 247.78 | +0.631% |
| `h² = (q-q⁻¹)²` | 166 | 247.78 | +0.634% |
| `h = q-q⁻¹` | 151 | 247.79 | +0.636% |
| `1` (pure q-power) | 136 | 247.79 | +0.638% |
| `5²·h = 25 h` | 120 | 243.93 | −0.931% |
| `2g+2 = 10` (Bring genus 4) | 114 | 249.55 | +1.354% |

**Best closure**: `N_v = 120 · q_0^90` with err = **−0.581%**.

### Categorical interpretation of the best closure

- **120 = |S_5| = 5!** is the order of the automorphism group of
  Bring's surface (genus-4 quintic curve), the geometric substrate
  of QOU per `chi-minus-six-chain.md` and `descartes-yekutieli.md`.
- **L = 90** is the Hecke-tower depth at which the EW scale emerges.
  - `90 = 2·3²·5` (factorisation suggestive but not categorically named)
  - `90 = 5·18` (5 levels of Bring × 18 sub-stratum?)
  - `90 = 6·15 = 6·(3·5)` (6 generations × 15-nucleon shell?)

The remaining 0.58% gap may correspond to a sub-leading correction
of order `h²/8 ≈ 0.0055` or `(q-1)/2 ≈ 0.055` exponent shift; both
candidates fit numerically but neither has paper-side justification.

### Why not a CHEAP fit

The closure `factor · q^L` with `factor ∈ {1, 5, 24, 120, 240}`
(small categorical constants) and `L ∈ {1..200}` integer is a
SEARCH SPACE OF ~1000 PAIRS. The expected Bonferroni-corrected
chance of one of them hitting within ±1% is non-trivial. So a
0.58% match on `120 · q^90` is **suggestive but not conclusive**.

To upgrade to a derivation:

1. **Categorical justification for `factor = 120`** — the `|S_5|`
   action on the Hecke algebra at the EW scale. Specifically: at
   what Wedderburn block does `S_5` act non-trivially? Could be
   `λ = (3,2)` or `λ = (2,2,1)` for n = 5.

2. **Categorical justification for `L = 90`** — the GB filtration
   grade or jet order at which the EW scale braid stabilises.
   Concrete test: compute the Coxeter-length distribution of the
   "weak-scale braid" (whatever that is) and check if the median
   or 90th percentile lands at 90.

3. **Sub-leading correction** to close the 0.58% gap — should be
   derivable from the same categorical structure.

## Strategy 3 — Self-consistency fixed point

`N_v` should be the unique fixed point of an equation involving
`q`, `m_e`, `μ_0`, and the EW-scale binding closure. No specific
proposal yet; would require explicit categorical EW-scale
construction in the paper.

## Strategy 4 — Wenzl-bridge level

`N_v` may equal a critical level `k` of the SU(2)_k Reshetikhin-Turaev
TQFT where the EW gauge group emerges. Specifically: at what level
does the SU(2) RT-TQFT have a finite-dimensional Hilbert space with
exactly the right number of states to host the W±/Z⁰ flavour
structure? Speculative; requires paper-side EW-RT-TQFT mapping.

## Status summary

- Strategy 1: circular, not a derivation.
- **Strategy 2 (`120 · q^90`): −0.581% match, suggestive**, awaiting
  paper-side categorical justification of `120` and `90`.
- Strategy 3: no concrete proposal.
- Strategy 4: requires paper-side EW-RT-TQFT mapping.

The compute side cannot close this without paper-side input on
which categorical invariant `(factor, L)` actually corresponds to.
