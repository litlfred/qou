Interactive periodic table visualizing the knot-theoretic nuclear
shell structure predicted by the topological mass formula and
Borromean binding conditions.  Elements are arranged by nuclear shell
rows (stability pairs) and proton sub-shell filling order
(Mayer--Jensen).  Controls allow switching between nuclear sub-shell,
electron block, and fill-order column modes.

Each element tile displays the knot-particle identification per the
GB-NF / confinement source of truth
([confined-particle](#def:confined-particle)) at $q_0$, all at shell
level $\ell = 1$ except the neutrino at $\ell = 0$:
**protons** as Borromean baryons $B_3(\mathrm{uud})$ (3-strand
flavored Borromean rings),
**neutrons** as $B_3(\mathrm{udd})$,
**electrons** as the word $\sigma_0\sigma_1\sigma_0 \in B_3$, whose closure is the Hopf link (the simulator still draws the backup reading, the trefoil $3_1$, closure of $\sigma_1^3$ in $B_2$),
and **neutrinos** as unknots $0_1$ (vacuum drag).
The fermion--boson decomposition classifies all entries via
[fermions are knots, bosons are links](#prop:fermion-boson-knot-link):
in the $T(2,n)$ family, fermions are single-component odd-$n$ torus knots and bosons are
even-$n$ 2-component links. That rule does not decide the electron's statistics, which remain open.
Building-block data including Jones polynomials and hyperbolic
volumes is in
([building-block knots](#rem:building-block-knots)).

**Views:**

1. **Default**: knot-centric layout with electron block coloring
2. **Magic numbers**: shell closures from linking number constraints
3. **Binding energy**: $B/A$ gradient (topological mass formula)
4. **Alpha clusters**: $k_\alpha$ sub-link count (Borromean decomposition)
5. **Transfer matrix**: Skein polynomial degree bound $A^2 - 1$
6. **Shell eigenvalues**: $\lambda_+^n$ at outermost electron shell
