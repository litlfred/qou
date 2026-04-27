A **bundle initial condition** over the projective line $\mathbb{P}(V)$
at a reference point in an affine chart is a formal sum of localized
hadrons and photons at base points:

$$
  \mathcal{S}_0 =  \sum_{i \in I} (p_i, H_i)
$$

where each $(p_i, H_i)$ is a localized hadron
([Definition](#def:localized-hadron)) or a photon
($H_i = \mathbf{1}_{B_4}$, 4-strand identity in $B_4$ — knot-trivial
under Markov closure but carries 4 internal polarisation×chirality
components on the exceptional divisor; see
[confined-particle](#def:confined-particle) registry).
The index set $I$ may be infinite, and multiple constituents may share
the same base point (bosonic and fermionic statistics are determined by
the Skein algebra, not by a support constraint).

Equivalently, $\mathcal{S}_0$ is a section of the free commutative monoid on the
hadron sheaf $\mathcal{H}$:

$$
  \mathcal{S}_0  \in 
  \Gamma\!\bigl(\mathbb{P}(V),
  \mathrm{Free}_{\mathrm{CMon}}(\mathcal{H})\bigr).
$$

This is a **position-only** specification: the positions $\{p_i\}$ on
$\mathbb{P}(V)$ are known exactly, while the momenta are entirely
undetermined.  The categorical content is that $\mathcal{S}_0$ specifies
the *fibre data* of the bundle — which constituent sits in which fibre —
without any information about the horizontal transport connecting
neighbouring fibres.

The subsequent configurations $\mathcal{S}_1, \mathcal{S}_2, \ldots$
represent the forward light cone from $\mathcal{S}_0$: each step applies
one iteration of the Reeb flow
([information-theoretic time](#def:information-theoretic-time)),
adding horizontal transport and accumulating interaction relations.
The backward sequence $\mathcal{S}_{-1}, \mathcal{S}_{-2}, \ldots$
represents the past light cone (reversing computation).  Whether the
sequence extends infinitely in either direction, or terminates, is
**not assumed** — it depends on the dynamics within the given affine
chart.

For the equivalence relation on bundle initial conditions, see
[Definition](#def:bundle-isotopy-equivalence).
