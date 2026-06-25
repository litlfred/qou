*Lean sibling: archimedean specialisation over $\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data.*

A *Hopf diquark* is a pair of quarks
$(\mathfrak{q}_i^a, \mathfrak{q}_j^b)$ in distinct color tubes
$a \neq b$ of the Bring's surface, joined by the Hopf link
$\mathcal{L}_H$:

$$
  D_{ij}^{[ab]}
  = 
  \mathfrak{q}_i^a  \oplus  \mathfrak{q}_j^b,
$$

where $i, j \in \{\mathfrak{u}, \mathfrak{d}, \mathfrak{s}\}$ are
flavor indices and $a, b \in \{r, g, b\}$ are color indices.  The
bracket $[ab]$ denotes antisymmetry: $D_{ij}^{[ab]} = -D_{ij}^{[ba]}$.

**Contrast with the Borromean baryon.**

In the confined phase, quarks are Borromean-linked
([Borromean quark](#conj:borromean-quark)): no two components are
pairwise linked, so no stable two-quark subsystem exists.  The Hopf
diquark violates this: its two components **are** pairwise linked,
with linking number $\pm 1$.  A Hopf diquark cannot exist inside an
intact Borromean baryon — it requires the Borromean topology to be
disrupted.

**Crossing energy.**

The Hopf link $\mathcal{L}_H = T_{2,2}$ has braid word $\sigma_1^2$
with $2$ crossings.  For a diquark of quarks with crossing
orientations $\epsilon_i, \epsilon_j \in \{+1, -1\}$, the Hopf
crossing energy is

$$
  \mathfrak{E}_{\mathrm{cross}}(D_{ij}^{[ab]})
  = 
  \epsilon_i \cdot q^{\epsilon_i}
  + 
  \epsilon_j \cdot q^{\epsilon_j}
  + 
  \mathfrak{E}_{\mathrm{cross}}(\mathcal{L}_H),
$$

where $\mathfrak{E}_{\mathrm{cross}}(\mathcal{L}_H)$ is the
linking contribution.  For an attractive (binding) diquark,
$\mathfrak{E}_{\mathrm{cross}} < 0$ is required.

**Color representation.**

The two quarks each carry a color index; their antisymmetric
combination $[ab]$ transforms in the **color antitriplet**
$\bar{\mathbf{3}}_c$ of $\mathrm{SU}(3)$:

$$
  \bar{\mathbf{3}}_c
  = 
  \epsilon^{abc}\mathfrak{q}^b \otimes \mathfrak{q}^c.
$$

The antisymmetry $D^{[ab]} = -D^{[ba]}$ is automatic from the
Hopf linking: the linking number is $\mathrm{lk}(a, b) = +1$
while $\mathrm{lk}(b, a) = -1$ under component exchange.

**Flavor-antisymmetric channel.**

For the most attractive pairing (largest binding), the flavor
indices must also be antisymmetric: $D_{[ij]}^{[ab]}$ with
$i \neq j$.  The three independent flavor-antisymmetric diquarks
are

$$
  D_{[\mathfrak{u}\mathfrak{d}]},
  \quad
  D_{[\mathfrak{d}\mathfrak{s}]},
  \quad
  D_{[\mathfrak{s}\mathfrak{u}]}.
$$

These are the three Cooper pair species in the CFL condensate.
