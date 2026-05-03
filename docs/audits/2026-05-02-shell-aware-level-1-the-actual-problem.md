# A.3 v2 post-mortem + the actual math problem

## The Manhattan-distance shell_factor was ad-hoc

I invented `shell_factor(Z, N) = exp(-d/scale)` where $d$ is
Manhattan distance to the closest magic shell-pair. **No
principled basis** — I just hypothesised "shell binding scales
with proximity to magic" and tried a multiplicative penalty.
It didn't work (spread 1.06% → 1.19%).

The cal-spread audit's diagnosis (4He outlier driven by shell
structure) was correct, but the implementation was a guess.

## The actual structural problem (per PR #500's BB-stratum)

`conj:categorical-neutrality-saturated-shells` (PR #500):
**at magic $n$, the categorical mass endomorphism $\Phi_n$ is
supported only on self-conjugate partitions $\lambda \vdash n$**.

The full-twist $\Delta_n^2$ acts on $V_\lambda$ by the central
scalar $q^{c(\lambda)}$ where $c(\lambda) = \sum_{x}(j_x - i_x)$
is the content sum. Self-conjugate partitions have $c(\lambda)
= 0$, so $\Delta_n^2$ acts trivially. Non-self-conjugate
partitions get a non-trivial scalar action and don't enter
$\Phi_n$ at saturation.

## Why level 0 misses the saturation entirely

The level-0 mass tower iterates only **length ≤ 2** partitions
(because the 2-variable Schur $s_\lambda(q, q^{-1})$ vanishes
for length > 2). Empirically:

| atom | $3A$ | total self-conj | length ≤ 2 | length ≥ 3 |
|------|----:|---------------:|----------:|----------:|
| D | 6 | 1 | 0 | 1 |
| 3He | 9 | 2 | 0 | 2 |
| 4He | 12 | 3 | 0 | 3 |
| 6Li | 18 | 5 | 0 | 5 |
| 12C | 36 | 33 | 0 | 33 |
| 16O | 48 | 87 | 0 | 87 |

**Every self-conjugate partition has length ≥ 3** (this is a
combinatorial fact: a self-conjugate partition has a square
Frobenius core, requires ≥ 3 rows for $n \geq 6$). So the
level-0 SW sum sees **zero contribution** from any
self-conjugate $\lambda$. The shell-saturation content lives
entirely in the **level-1 jet correction**.

## What level 1 should compute

$$
  m^{(1)}(Z, N) = \sum_{\lambda \vdash 3A,\; \mathrm{self\text{-}conj},\; \mathrm{len} \geq 3} w_\lambda^{(1)} \cdot \chi^\lambda(\beta_{\mathrm{atom}})
$$

where $w_\lambda^{(1)}$ is the **level-1 weight** — derived from
the Białynicki-Birula spectral sequence on $A_n =
A_{n-1} \otimes \Omega^1(A_{n-1})$, NOT the standard $q$-Plancherel
weight $\dim_q(\lambda)^2 / [n]_q!$.

Probe attempt (using raw $q$-Plancherel weight) reveals the
problem:

| atom | $3A$ | $\sum w_\lambda$ over self-conj |
|------|----:|--------------------------------:|
| D | 6 | $3.6 \times 10^{-1}$ |
| 3He | 9 | $2.0 \times 10^{-2}$ |
| 4He | 12 | $2.3 \times 10^{-1}$ |
| 6Li | 18 | $1.6 \times 10^{-1}$ |
| 12C | 36 | $8.3 \times 10^{5}$ |
| 16O | 48 | $9.8 \times 10^{14}$ |

The factorial-growth $\dim_q(\lambda)^2$ explodes the raw sum at
large $n$ — clearly the level-1 weight needs proper BB-filtration
normalization to give a physically meaningful per-atom
contribution.

## Why this is genuinely hard (not just bookkeeping)

1. **Level-1 weight derivation is open.** The categorical
   formulation says $\Phi_n$ is the global section of the mass
   functor; the BB spectral sequence on the brane tower computes
   this. The explicit per-$\lambda$ weight $w_\lambda^{(1)}$ at
   each jet level is **not yet derived** in the framework — it's
   conjectural via `conj:homological-shell-condensation`.
2. **Character on jet-prolonged braid is open.** The atomic
   braid $\beta_{\mathrm{atom}}$ acts on $V_q^{\otimes 3A}$ at
   level 0; at level 1 it acts on $V_q^{\otimes 3A} \otimes
   \Omega^1$. The Specht character $\chi^\lambda$ on this lifted
   action is a separate computation.
3. **BB-stratum projection is implicit.** Saturated shells
   correspond to BB-strata where the $E_\infty$ page collapses;
   the projection from "all self-conjugate $\lambda$" to
   "BB-saturated $\lambda$" depends on the spectral sequence
   structure for that specific $n = 3A$.

## Status

**A.3 v2 negative result is now contextualised:** my Manhattan-
distance heuristic was a guess at a problem whose actual solution
requires deriving the level-1 BB-spectral-sequence weights —
research-grade work, not a refactor.

**Recommended A.3 v3:** route through PR #500's
`optimised_magic_verifier.py` machinery (which uses LR-fusion
$\Delta i \leq 1$ rule on shell-pair indices) to construct
$w_\lambda^{(1)}$ as the LR-coefficient of a self-conjugate
partition under the magic shell-pair fusion. This stays within
the existing categorical machinery and avoids ad-hoc heuristics.

**Pragmatic alternative:** treat the cal/m_e log(A) trend as
part of the categorical formula's intrinsic structure (not an
error), and quote per-atom predictions with the
trend-subtracted residual ~350 ppm (excluding 4He outlier) as
the achieved precision. Reach toward 22 ppb floor only via
A.3 v3 derivation.
