The proton is a [hadron](#def:hadron). Its three constituents link in a [Borromean configuration](#def:borromean-baryon).

**Constituent quarks as unknots.**
Quarks are unknots $K_{0_1}$ distinguished by their crossing orientation within the Borromean link. The up quark $\mathfrak{u}$ carries positive crossing orientation, while the down quark $\mathfrak{d}$ carries negative crossing orientation. The proton $\mathfrak{p}$ comprises two up quarks and one down quark:

$$
  \mathfrak{p} = [\mathfrak{u}, \mathfrak{u}, \mathfrak{d}]_p \oplus \mathcal{L}_{\mathrm{Bor}},
$$

where $\mathcal{L}_{\mathrm{Bor}}$ is the Borromean link.

**Borromean property.**
The Borromean link requires all three components to remain linked. Removing any single component unlinks the remaining two:

- Remove $\mathfrak{u}_1$: the pair $(\mathfrak{u}_2, \mathfrak{d})$ has linking number zero and separates.
- Remove $\mathfrak{u}_2$: the pair $(\mathfrak{u}_1, \mathfrak{d})$ unlinks.
- Remove $\mathfrak{d}$: the pair $(\mathfrak{u}_1, \mathfrak{u}_2)$ unlinks.

Together, the three components form a non-trivial link. Their pairwise linking numbers vanish, but their Milnor triple linking number $\bar{\mu}(123) = \pm 1$ is non-zero. This provides the topological mechanism for quark confinement. No single quark can be extracted without dissolving the entire structure, yet any two-body subsystem remains topologically trivial.

**Mass from the linking matrix.**
The proton mass decomposes into constituent masses and binding energy:

$$
  \mathfrak{m}_{\mathfrak{p}} = 2\mathfrak{m}(\mathfrak{u}) + \mathfrak{m}(\mathfrak{d}) + \mathfrak{E}_{\mathrm{bind}}.
$$

The binding energy $\mathfrak{E}_{\mathrm{bind}}$ originates from the Borromean linking. Because the individual quark masses $\mathfrak{m}(\mathfrak{u})$ and $\mathfrak{m}(\mathfrak{d})$ are small, the binding energy dominates. The mass of the proton arises overwhelmingly from topological complexity.

We compute the binding energy from the [crossing energy](#ex:crossing-energy-trefoil) of the linking braid word $\beta_{\mathrm{Bor}} \in B_3$. The Borromean link admits the braid representation $\beta_{\mathrm{Bor}} = (\sigma_1^{-1}\sigma_2)^3$. This geometry yields mutual crossings that ensure $\mathfrak{E}_{\mathrm{cross}}(\mathfrak{p}) < 0$. At the substrate parameter $q \approx 1.110$, this computation gives:

$$
  \mathfrak{m}_{\mathfrak{p}}(q) \approx :val[m_p_MeV]{precision=6, witness=computations/codata-masses.witness.json} \text{MeV}.
$$

**Stability of the proton.**
The proton is the lightest baryon and cannot decay into lighter baryons. Topologically, the Borromean link of three unknots is the simplest non-trivial three-component link carrying the correct charge and color quantum numbers. No sequence of Reidemeister moves or Markov stabilizations can simplify it further while preserving the baryon number.
