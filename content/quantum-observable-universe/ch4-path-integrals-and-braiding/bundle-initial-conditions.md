A **bundle initial condition** (or *big bang state*) over the projective
line $\mathbb{P}(V)$ is a formal sum of localized hadrons at
base points:

$$
  \mathcal{S}_0 \;=\; \sum_{i \in I} (p_i,\, H_i)
$$

where each $(p_i, H_i)$ is a localized hadron
([Definition](#def:localized-hadron)).  The index set $I$ may be
infinite, and multiple hadrons may share the same base point
(bosonic and fermionic statistics are determined by the Skein
algebra, not by a support constraint).

Equivalently, $\mathcal{S}_0$ is a section of the free commutative monoid on the
hadron sheaf $\mathcal{H}$:

$$
  \mathcal{S}_0 \;\in\;
  \Gamma\!\bigl(\mathbb{P}(V),\;
  \mathrm{Free}_{\mathrm{CMon}}(\mathcal{H})\bigr).
$$

This is the **position-only** specification: at the initial moment the
positions $\{p_i\}$ on $\mathbb{P}(V)$ are known exactly, while the
momenta are entirely undetermined (the "big bang" complementarity).  The
categorical content is that $\mathcal{S}_0$ specifies the *fibre data* of the
bundle — which hadron sits in which fibre — without any information about
the horizontal transport connecting neighbouring fibres.

For the equivalence relation on bundle initial conditions, see
[Definition](#def:bundle-isotopy-equivalence).
