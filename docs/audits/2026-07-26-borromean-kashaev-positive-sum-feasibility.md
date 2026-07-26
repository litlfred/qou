# Borromean volume conjecture: positive-sum feasibility — the 4₁ squeeze architecture transfers

**Date**: 2026-07-26 · **Bean**: qou-z1wh (milestone qou-jpwy) · **Status**: feasibility CONFIRMED; attack program scoped, not started.

## Question

Can the E-brick infrastructure that machine-proved the 4₁ volume conjecture in-repo
(`FigureEightVolumeSqueeze.lean`, milestone qou-cpfn — positive Riemann sums of
`log(2 sin)` squeezed against the Clausen primitive) also machine-prove the
**Borromean** instance `(2π/N)·log⟨𝓑₃⟩_N → Vol(𝓑₃) = 8·Cl₂(π/2) = 8G`?
The Borromean instance is literature-proven (van der Veen, Whitehead chains,
arXiv:math/0611181) and load-bearing for the binding-scale `8G` and the `F_Bor`
anchor (see `docs/coordination/binding-scale-is-hyperbolic-volume.md`).

## Finding — YES: the Kashaev-point Habiro sum is positive, and its rate hits 8G

Starting from the **corpus-verified** Habiro formula (transcribed + 4-anchor-verified
in [`computations/habiro_borromean_colored_jones.py`](../../computations/habiro_borromean_colored_jones.py), bean n920):

$$
  J_{B,n}(q) = \sum_{l=0}^{n-1} (-1)^l \{n\}^2
    \frac{\bigl(\prod_{j=1}^{l}\{n+j\}\{n-j\}\bigr)^3}
         {\bigl(\prod_{j=l+1}^{2l+1}\{j\}\bigr)^2},
  \qquad \{j\} = q^{j/2} - q^{-j/2}.
$$

At the Kashaev point $q = e^{2\pi i/N}$, $n = N$ (exact sign analysis, no numerics):

1. $\{N\} = 0$, so terms with $2l+1 < N$ **vanish** and terms with $2l+1 \ge N$
   survive with the exact cancellation $\{N\}^2/\{N\}^2 = 1$ (identical factors —
   algebraic, no limit).
2. $\{N+j\}\{N-j\} = 4\sin^2(\pi j/N) > 0$ — the cubed numerator is
   $\mathrm{kashaevProd}(N,l)^3$.
3. The leftover squared denominator contributes $(-1)^l\cdot(\text{positive})$,
   cancelling Habiro's $(-1)^l$.

$$
  \Rightarrow\quad \langle\mathcal{B}_3\rangle_N \;=\; \sum_{l \ge (N-1)/2} P_l,
  \qquad P_l \;=\; \frac{\mathrm{kashaevProd}(N,l)^3}
    {\prod_{j=l+1,\,j\ne N}^{2l+1} \bigl(2\sin(\pi j'/N)\bigr)^2} \;>\; 0,
$$

with $j' = j$ or $j-N$ (mirror). A **positive sum whose log-terms are 1D Riemann
sums of the same `log(2 sin)` integrand** — exactly the 4₁ situation.

Numeric confirmation ([`borromean_kashaev_positive_sum_probe.py`](../../computations/borromean_kashaev_positive_sum_probe.py),
witness `borromean-kashaev-positive-sum-probe.witness.json`, all assertions pass):

| N | (2π/N)·log Σ | argmax l/N |
|---|---|---|
| 101 | 7.67316 | 0.7426 |
| 501 | 7.42733 | 0.7485 |
| 1001 | 7.38408 | 0.7493 |
| 3001 | 7.34997 | 0.7498 |

→ `8G = 7.32772…` from above with ~1/N corrections; saddle at $x = l/N \to 3/4$
(the $\pi/2$ Catalan angle, as expected).

## Attack program (scoped bricks, 4₁-analogous)

- **B1 — Cl₂ duplication** `Cl₂(2θ) = 2Cl₂(θ) − 2Cl₂(π−θ)`: provable now from the
  in-repo integral representation (`clausen` + FTC bricks) via
  `log(2 sin 2u) = log(2 sin u) + log(2 sin(π/2 − u + …))` substitution — closes a
  gap the Clausen filler explicitly lists as missing. Needed to evaluate the
  continuum functional at $x = 3/4$ as $8\,Cl₂(π/2)$.
- **B2 — the positive-sum carrier**: define `borromeanKashaev N := Σ_l P_l` in Lean
  (real positive form above) with the Habiro/GL2011 citation, mirroring how
  `FigureEightVolume.lean` defines `kashaev` by its explicit sum (same epistemic
  status: the identification with the diagrammatic invariant is the cited input).
- **B3 — window/mirror deviation**: `log P_l = 3·log kashaevProd(N,l) −
  [window sum over (l, 2l+1] mirrored at N]` — the existing E4/E5 sum-vs-integral
  machinery (`abs_deviation_le`, falling/mirror bricks) plus one new windowed
  variant.
- **B4 — extremum at 3/4**: maximize `Φ(x) = −3·clausen(2πx) + clausen-window(x)`
  via `hasDerivAt_clausen` (E3-analogue); value `Φ(3/4) = 8·Cl₂(π/2)` via B1.
- **B5 — squeeze**: E1-analogue (`log Σ ≤ log N + log max`) + B3 + B4, as in E5d.

Estimated effort: comparable to the full 4₁ program (E1–E5d), dominated by B3's
mirror bookkeeping. All bricks elementary — no Borel resummation, no stationary
phase.

## Honest scope

- The probe is float64 asymptotics — a **rate** check, not a precision claim.
- Nothing here discharges anything yet: this document authorizes-by-feasibility
  the brick program; the (a)/(b) refutation discipline and anti-laundering rules
  apply unchanged.
- The 8₁₁ (³H) instance remains **open in the literature and out of reach of this
  architecture** (oscillatory multi-dimensional Kashaev sum — no positivity).
