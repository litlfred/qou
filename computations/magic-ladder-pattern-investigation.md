# Magic-ladder pattern investigation — empirical report

Driven by the question: *can a partition-combinatorics statistic of
self-conjugate Young diagrams distinguish magic $n \in \{2, 8, 20,
28, 50, 82, 126\}$ from non-magic $n$?*

**TL;DR — no.** Every metric tested gives values for magic $n$ that
are not unique compared to nearby non-magic $n$. This rules out a
pure-partition-combinatorics origin of the magic ladder and leaves
the categorical / homological-condensation framework as the
required source of the magic-ladder selection rule.

## Setup

Computed by [`magic_vs_nonmagic_self_conjugates.py`](magic_vs_nonmagic_self_conjugates.py)
across $n \in \{1, 3, 4, 5, 6, 7\} \cup \{2, 8, 20, 28, 50, 82, 126\}
\cup \{9, 10, 11, 12, 14, 15, 16, 18, 24, 30, 36, 40, 60, 100\}$.
Full report in `magic_vs_nonmagic_report.json`.

## Metrics tested (all *fail* to distinguish magic)

| Metric | Magic $n$ values | Non-magic $n$ values | Verdict |
|---|---|---|---|
| $q(n) = \#\{\lambda = \lambda'\}$ | $0, 2, 7, 16, 98, 881, 10422$ | $0, 1, 2, 3, 4, 5, 6, 8, 11, 16, 18, 33, 46, 209, 2574$ | overlapping ranges |
| Max Durfee $\max d$ | $0, 2, 4, 4, 6, 8, 10$ | $0, 1, 2, 3, 4, 6, 10$ | overlapping |
| Min Durfee $\min d$ | $0, 2, 2, 2, 2, 2, 2$ | $0, 1, 2$ | parity-determined |
| Max hook length | $0, 7, 19, 27, 49, 81, 125$ | $1, 3, 11, 23, 35, 39, 59, 99$ | $\sim n - 1$ for even $n$ |
| Canonical first row | $0, 3, 5, 6, 8, 10, 12$ | $1, 2, 3, 4, 5, 6, 7, 8, 10$ | $\sim \sqrt{n}$ for all |
| Canonical aspect $w/h$ | $1.0$ at every magic $n \geq 8$ | $1.0$ at every non-magic $n \geq 12$ | not a discriminator |
| Is triangular | $\{28\}$ only | $\{1, 3, 6, 10, 15, 36\}$ | $\{28\}$ alone insufficient |
| Is perfect square | none | $\{1, 4, 9, 16, 36, 100\}$ | not magic |
| Has staircase self-conj | $\{28\}$ only | $\{1, 3, 6, 10, 15, 36\}$ | mirrors triangular |
| Has square self-conj | none | $\{1, 4, 9, 16, 36, 100\}$ | mirrors perfect-square |

## Specific observations

- **$n = 28$ is the only magic that is triangular** (it carries the
  staircase $[7, 6, 5, 4, 3, 2, 1]$ as a self-conjugate). Other
  triangular numbers $\{1, 3, 6, 10, 15, 36\}$ are non-magic.
- **No magic $n \geq 8$ is a perfect square.** Conversely
  $\{16, 36, 100\}$ are perfect squares (with $k \times k$ self-conj
  $[k]^k$) and are non-magic.
- The canonical (most-square-like) self-conjugate has $w \approx h
  \approx \sqrt{n}$ for *all* $n \geq 8$ regardless of magic
  status — by design of the bijection.
- Max-Durfee is forced by $\max d = $ largest even integer with
  $d^2 \leq n$ for even $n$ (parity of $d$ matches parity of $n$
  for distinct-odd decompositions). This is a generic formula, not
  magic-specific.
- $q(n)$ and decomposition-length histograms grow monotonically in
  $n$ with no anomaly at the magic ladder.

## What the negative result means

The Frobenius-coordinate bijection
$$
\bigl\{ \text{self-conj } \lambda \vdash n \bigr\}
\;\leftrightarrow\;
\bigl\{ \text{partitions of } n \text{ into distinct odd parts} \bigr\}
$$
makes self-conjugacy a *generic* property of $n \geq 1$ (excepting
$n = 2$). The partition function for distinct odd parts is well-
behaved and admits no "magic-ladder anomaly."

This forces the magic-ladder selection rule to come from an
**external dynamical condition**, not a partition statistic. The
candidate dynamical inputs in the QOU framework:

1. **BB-stratum complete-intersection**
   ([conj:homological-shell-condensation](../../content/quantum-observable-universe/lifting-and-descent/homological-shell-condensation.md))
   — the additional algebraic-geometry condition on the Hecke
   stratum that is *not* implied by self-conjugacy.
2. **Yekutieli MC-equation** — solvability of the Maurer–Cartan
   equation in the pronilpotent DGLA of jet-tower deformations,
   conjecturally restrictive on the isotropic-oscillator ladder.
3. **LP/SDP active-basis collapse** — the dominant LR-fusion module
   being self-conjugate *and* uniquely shadow-priced in
   [`prop:operator-selection-lp`](../../content/quantum-observable-universe/particle-interactions/operator-selection-lp.md).
4. **Spin-orbit reordering** — physically, magic numbers come from
   the Mayer–Jensen 3D-oscillator-plus-spin-orbit shell-filling
   ordering. The categorical framework would need to encode this
   ordering via the Yekutieli jet prolongations.

## Conclusion

The negative result is **valuable**: it eliminates pure-partition-
combinatorics as a candidate explanation and pins the magic-ladder
selection on the spectral-sequence / BB-stratification side of the
framework. The
[homological-condensation conjecture](../../content/quantum-observable-universe/lifting-and-descent/homological-shell-condensation.md)
is therefore doing the *real* work, and the
[diagrammatic LR-fusion conjecture](../../content/quantum-observable-universe/observations/diagrammatic-double-magic-lr-fusion.md)
should be read as the *necessary* part of the criterion (constituent
self-conjugacy + content additivity force $\kappa_{\lambda_A} = 0$),
with the *sufficient* part requiring the homological condensation.

Future investigation directions:

- Compute LP/SDP shadow-price vectors at $q_0$ for each non-magic
  $n$ in $\{12, 16, 24, 36\}$ and compare with magic $n$ — look for
  a difference in active-basis structure (degeneracy, slack pattern).
- Compute Yekutieli jet-prolongation obstruction classes
  $J^k(\Phi_n)$ explicitly at low $n$ to test whether they vanish
  *only* on the magic ladder.
