*Lean sibling: archimedean specialisation over $\mathbb{R}$ (CLAUDE.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data.*

**Multi-link Jones values at $q = 1$ — Lean infrastructure for the $c_5 / c_6$ candidate investigation.**

The $Q_\beta$ precision ladder
([`prop:q-beta-categorical-precision-ladder`](#prop:q-beta-categorical-precision-ladder))
closed $c_1, c_2$ from Kashiwara ($b, b^2$), $c_3$ from
$J_{\mathrm{Hopf}}(q{=}1) = -2$ at the 3-fold Markov closure, $c_4$
from the mixed Kashiwara-plus-Hopf-half $b^2 + 1/2$. The simple
alternating Kashiwara $\times$ Jones pattern at odd $k = 3$ suggests trying
multi-link Jones values for $c_5, c_7, \ldots$ — Borromean rings,
double-Hopf, etc.

**Empirically this fails**: at $q_0$ at 50 dps via
[`probe_q_beta_c5_c6_multilink.py`](../../folio-assistant/computations/probe_q_beta_c5_c6_multilink.py),

| coefficient | empirical | closest simple multi-link Jones candidate |
|:---:|---:|---:|
| $c_5$ | $\approx -395.4$ | $-J_{\mathrm{Borromean}} = +8$ (50$\times$ off in scale and sign) |
| $c_6$ | $\approx -45{,}485$ | $J_{\mathrm{Hopf}} \cdot J_{\mathrm{Borromean}} = 16$ (3000$\times$ off) |

## What this block provides

This is **infrastructure, not closure**. The Lean module
`QOU.BraidKnot.multi_link_jones_q1_extension` exports:

1. **Three new `Link` constructors** (in
   [`rem:braid-link-types`](#rem:braid-link-types)'s extended `Link`
   inductive): `trefoil`, `borromean`, `doubleHopf`.

2. **Three new `jonesAtOne` cases**, each proved by `rfl`:

   | constructor | $J_L(q{=}1)$ | source |
   |---|---:|---|
   | `trefoil` | $+1$ | Jones 1985, $T(2,3)$ 1-component unnormalised |
   | `borromean` | $-8$ | Jones 1985 / Habiro 2002, 3-component Brunnian |
   | `doubleHopf` | $+4$ | $J_{\mathrm{Hopf}}^2$ by disjoint-union multiplicativity |

3. **Two combination values**: `jonesHopfTimesBorromean = 16`,
   `jonesBorromeanFlipped = 8`. Both candidates carry **explicit
   docstrings noting the empirical mismatch** — they are not
   closures.

4. **A `MultiLinkJonesAtOne` class** with fields `c5_candidate`,
   `c6_candidate` for downstream consumers to plug in any specific
   candidate values they want to test. The default instance uses the
   probe's "best simple integer" candidates ($c_5 = +8$, $c_6 = 16$),
   **explicitly flagged as exploratory placeholders, not closure
   values**.

## Why the simple multi-link pattern fails

Three structural hypotheses for the 50–3000$\times$ mismatch:

1. **Precision-ladder normalisation revision**: the $b^k$ factor
   multiplying $c_k$ beyond $k = 4$ may carry an extra
   Wedderburn-weight or coupling-constant prefactor not captured by
   the $(b \cdot \hbar_q^2)^k$ expansion ansatz.

2. **Sum-over-Wedderburn-blocks**: multi-link contributions enter via
   a non-trivial sum over $\lambda \vdash n$ rather than as a direct
   scalar multiple of a single Jones value. The $y_\lambda$
   normalisation in the Wenzl bridge could redistribute weight in a
   way that magnifies single-Jones values into the empirical $c_5,
   c_6$ scale.

3. **New categorical input at $k \geq 5$**: a higher-rank irrep
   coupling, a Mostow rigidity gap correction, or a non-trivial
   Habiro residue contribution may enter only at orders $k \geq 5$.

## Concrete next probe

Test whether the **per-Wedderburn-block contribution at $k = 5, 6$**
matches empirical when properly weighted by the $q$-deformed
dimensions $\dim_q(V_\lambda)$. This requires extending the
Wenzl-bridge $y_\lambda$ infrastructure to $\varepsilon^{10},
\varepsilon^{12}$ evaluations of the $\tau_M$ expansion on
$V_{(2,1)}, V_{(3)}, V_{(1,1,1)}$ separately.
