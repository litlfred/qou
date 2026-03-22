A *hadron* is a composite localized knot: a finite multiset of localized
knots at a common base point, bound by the Hopf-link internal structure.

Formally, let $\mathbb{P}(V)$ be the projective line object
([Definition](#def:projective-line-object)).  A **hadron** at a point
$p \in \mathbb{P}(V)$ is a morphism in $\mathcal{C}$:

$$
  H \;\colon\; \mathbf{1}
  \;\longrightarrow\;
  \mathrm{Sym}^n\!\bigl(\mathcal{K}_p\bigr)
  \;\otimes\;
  \mathcal{L}_{p}^{\mathrm{bind}}
$$

where:

- $\mathcal{K}_p = \bigoplus_{i=1}^{n} K_i$ is the direct sum of $n$
  constituent knot types in the fibre $E_p$,
- $\mathrm{Sym}^n(-)$ denotes the symmetric (bosonic) or antisymmetric
  (fermionic) product according to spin-statistics, and
- $\mathcal{L}_{p}^{\mathrm{bind}}$ is the **binding line bundle**: the
  Hopf link $\mathcal{L}_{\mathrm{Hopf}}$ encoding the strong-force
  internal entanglement that is invisible to the base
  $\mathbb{P}(V)$ but contributes to the total mass via the Skein relation.

The constituent knot types $K_i$ are the *valence quarks* in the QOU
picture.  Their topological identities determine the hadron's mass through
the terminal resolution ([Proposition](#prop:terminal-resolution)):

$$
  m_H \;=\; Q(q) \cdot \mathcal{M}(\mathcal{L}_{\mathrm{Hopf}})
  \;+\; \sum_{i=1}^{n} \mathcal{M}(K_i)
$$

where $Q(q)$ encodes the $q$-deformed Skein polynomial of the binding link.

The **baryon** is the case $n = 3$ with $K_i$ drawn from the trefoil
class; the **meson** is $n = 2$ with a knot–antiknot pair.  In both cases,
$\mathcal{L}_{p}^{\mathrm{bind}} = \mathcal{L}_{\mathrm{Hopf}}$
provides the color-exchange entanglement of the three (or two) chiral
tubes $(\mathfrak{r}, \mathfrak{g}, \mathfrak{b})$ tiling the exceptional
divisor.
