The proton is a [hadron](#def:hadron) — a stable knot composite — whose
three constituents are linked in a
[Borromean configuration](#def:borromean-baryon).

**Constituent quarks as unknots.**
In the knot-particle correspondence, quarks are unknots $K_{0_1}$
distinguished by crossing orientation within the Borromean link:
the up quark $\mathfrak{u}$ has positive crossing orientation
and the down quark $\mathfrak{d}$ has negative crossing orientation.
The proton $\mathfrak{p}$ consists of two up quarks and one down quark:

$$
  \mathfrak{p}
  = 
  [\mathfrak{u}, \mathfrak{u}, \mathfrak{d}]_p
   \oplus  \mathcal{L}_{\mathrm{Bor}},
$$

where $\mathcal{L}_{\mathrm{Bor}}$ is the Borromean link.

**Borromean property.**
The Borromean link has the defining property: *remove any one
component and the remaining two are unlinked*.  Concretely:

- Remove $\mathfrak{u}_1$: the pair
  $(\mathfrak{u}_2, \mathfrak{d})$ has linking number zero and falls
  apart.
- Remove $\mathfrak{u}_2$: the pair
  $(\mathfrak{u}_1, \mathfrak{d})$ likewise unlinks.
- Remove $\mathfrak{d}$: the pair
  $(\mathfrak{u}_1, \mathfrak{u}_2)$ unlinks.

Yet all three together form a non-trivial link with pairwise linking
numbers all zero but a non-vanishing Milnor triple linking number
$\bar{\mu}(123) = \pm 1$.  This is the topological origin of quark
confinement: no single quark can be extracted because the Borromean
link is topologically stable, while any two-body subsystem is
topologically trivial.

**Mass from the linking matrix.**
The proton mass decomposes as

$$
  \mathfrak{m}_{\mathfrak{p}}
  = 
  2\mathfrak{m}(\mathfrak{u})
  + \mathfrak{m}(\mathfrak{d})
  + \mathfrak{E}_{\mathrm{bind}},
$$

where $\mathfrak{E}_{\mathrm{bind}}$ is the binding energy from the
Borromean linking.  The individual quark masses
$\mathfrak{m}(\mathfrak{u})$ and $\mathfrak{m}(\mathfrak{d})$ are
small (a few MeV each in QCD terms), so the binding energy dominates:
the proton mass is overwhelmingly due to the topological complexity
of the Borromean linking, not the constituent masses.

The binding energy is computed from the
[crossing energy](#ex:crossing-energy-trefoil) of the linking braid
word $\beta_{\mathrm{Bor}} \in B_3$.  The Borromean link has braid
representation $\beta_{\mathrm{Bor}} = (\sigma_1^{-1}\sigma_2)^3$,
contributing mutual crossings that make
$\mathfrak{E}_{\mathrm{cross}}(\mathfrak{p}) < 0$.  At the substrate
parameter $q \approx 1.110$, the full computation yields

$$
  \mathfrak{m}_{\mathfrak{p}}(q)  \approx  :val[m_p_MeV]{precision=6, witness=computations/codata-masses.witness.json}  \text{MeV},
$$

matching the experimental proton mass to high precision.

**Why the proton is stable.**
The proton is the lightest baryon and cannot decay into lighter
baryons.  Topologically, this corresponds to the fact that the
Borromean link of three unknots is the simplest non-trivial
three-component link with the correct charge and color quantum
numbers.  No topological simplification (Reidemeister moves,
Markov stabilization) can reduce it further while preserving
baryon number.
