A **bundle initial condition** (or *big bang state*) over the projective
line $\mathbb{P}(V)$ is a finite formal sum of localized knots:

$$
  E_0 \;=\; \sum_{i=1}^{N} (p_i,\, K_i)
  \;\in\;
  \mathbb{N}\bigl[\mathrm{Hom}(\mathbf{1},\, A^{\mathrm{co}\,T})
  \times \mathrm{Knot}\bigr]
$$

where each $(p_i, K_i)$ is a localized knot
([Definition](#def:localized-knot)).

Equivalently, $E_0$ is a section of the free commutative monoid on the
knot sheaf $\mathcal{K}$:

$$
  E_0 \;\in\;
  \Gamma\!\bigl(\mathbb{P}(V),\;
  \mathrm{Free}_{\mathrm{CMon}}(\mathcal{K})\bigr).
$$

This is the **position-only** specification: at the initial moment the
positions $\{p_i\}$ on $\mathbb{P}(V)$ are known exactly, while the
momenta are entirely undetermined (the "big bang" complementarity).  The
categorical content is that $E_0$ specifies the *fibre data* of the
bundle — which knot sits in which fibre — without any information about
the horizontal transport connecting neighbouring fibres.

Two bundle initial conditions are **equivalent** if they are related by a
permutation of indices and an ambient isotopy within each fibre:

$$
  (p_1, K_1, \ldots, p_N, K_N) \;\sim\;
  (p_{\sigma(1)}, K_{\sigma(1)}', \ldots, p_{\sigma(N)}, K_{\sigma(N)}')
$$

where $\sigma \in S_N$ and each $K_{\sigma(i)}'$ is ambient-isotopic to
$K_{\sigma(i)}$ in $E_{p_{\sigma(i)}}$.

When several localized knots share a common base point $p$, their
composite forms a hadron ([Definition](#def:hadron)).  Thus a bundle
initial condition decomposes as a disjoint union of hadrons distributed
across $\mathbb{P}(V)$.
