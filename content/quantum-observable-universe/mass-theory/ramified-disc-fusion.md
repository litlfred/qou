**Proposition.**
*Let $\mathcal{R}_p \xrightarrow{\pi_H} \mathcal{S}_p$ be the Reeb
bundle ([Reeb bundle](#def:reeb-bundle)), and let $D \subset \mathcal{S}_p$
be a small open disc around a foundry point (a boundary point of
the latitude range $\phi \in \{0, \pi\}$).  Let
$\widetilde{D} \subset \mathcal{R}_p$ denote the preimage
$\pi_H^{-1}(D)$ together with the three colour-tube sections
$\mathfrak{r}, \mathfrak{g}, \mathfrak{b}$ restricted to $D$
([color-sector coordinates](#def:color-sector-coords)).  Then:*

1. **Fusion.** *$\widetilde{D}$ is a single connected topological
   disc with degree-$3$ ramification at the centre $\pi_H^{-1}(p)$.
   Away from that centre, $\widetilde{D}$ is the disjoint union of
   the three sector traces; at the centre the three sectors
   coalesce.*

2. **Monodromy.** *The monodromy of the branched cover
   $\widetilde{D} \to D$ around $\partial D$ is the cyclic group
   $C_3 = \langle (rgb) \rangle$.  The full Galois group of the
   regular closure is the symmetric group $S_3$ acting on the
   sheets $\{r,g,b\}$.*

3. **Comparison with the Lagrange resolvents.** *The $S_3$
   monodromy on $\widetilde{D}$ agrees with the $S_3$ action on
   the Lagrange resolvents $(w_1, w_2, w_3)$ given by
   [Lagrange resolvent transform](#prop:lagrange-resolvent-transform):
   the cyclic generator $(rgb)$ corresponds to the cyclic permutation
   $w_k \mapsto \zeta w_k$ ($\zeta$ a primitive cube root of unity)
   diagonalising the $C_5$ representation on the spectral fibre,
   and the transpositions correspond to the parity reflections
   exchanging conjugate pairs.*

**Sketch of proof.**

For (1): the three color-sector embeddings
$\mathfrak{r}(\phi,\psi),\mathfrak{g}(\phi,\psi),\mathfrak{b}(\phi,\psi)$
tile the exceptional divisor with shared meridian boundaries at
$\psi = 0, 2\pi/3, 4\pi/3$ (each sector covers an angular sector
of width $2\pi/3$).  At the foundry boundary $\phi \to 0$ or
$\phi \to \pi$ the latitude factor $\sin\phi \to 0$ collapses the
three sectors onto their common axis $\pm N$, identifying the
three meridian seams into a single triple point.  The resulting
quotient topology is the cone over the three angular slices —
i.e. a disc with degree-$3$ ramification at the apex.

For (2): a loop around $\partial D$ in the base lifts to three
disjoint paths on the unramified part of $\widetilde{D}$; each
path connects a sector to its cyclic successor under the $C_3$
action embedded in the symmetric group $S_3$.  Going around
$\partial D$ once therefore implements the cyclic permutation
$(rgb)$.  Adjoining the cover's transpositions (orientation
reversals on $D$ — equivalently, the involution that exchanges
the $\pm N$ poles in the color parametrisation) yields the
full $S_3$.

For (3): the Lagrange resolvents $w_1, w_2, w_3$ are obtained
from the colour-tube coordinates $c_r, c_g, c_b$ by the cube-root
DFT $w_k = c_r + \zeta^k c_g + \zeta^{2k} c_b$, hence the cyclic
permutation $(c_r, c_g, c_b) \mapsto (c_g, c_b, c_r)$ corresponds
to $w_k \mapsto \zeta^{-k} w_k$.  Identifying $(rgb)$ on the
ramified disc with the cyclic Galois generator on the resolvents
therefore matches the geometric monodromy of (1)–(2) with the
algebraic $S_3$ action of
[$\rho$ as $S_3$ holonomy on Lagrange resolvents](#rem:rho-s3-holonomy-exposition). $\square$

**Why this matters.**  The proposition closes the geometric
chain "internal Reeb flow $\to$ boundary observable" in a precise
sense: the $S_3$ Galois action that appears in the algebraic
braid-group representation $\rho \colon B_3 \to \mathrm{SU}(2)$ is
not posited — it is read off as the monodromy of the
ramified-disc cover at the foundry boundary, which in turn is
the topological shadow of the Reeb-flow trajectories on the
interior.  Combined with
[six canonical knot operators](#prop:six-canonical-knot-operators),
this gives the explicit dictionary
$\text{Reeb trajectory} \longmapsto \text{boundary Galois permutation}$
that the motivating discussion proposed.
