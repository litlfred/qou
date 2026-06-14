Noble gases are atoms whose curls are full — every sub-Hopf
link is closed.  **Metals are the opposite**: atoms whose
outermost sub-Hopf link has **unfilled linking sites**, and
whose crossing energy at those sites is low enough that
neighbouring atoms can share them.

**Statement.**
Let $\mathcal{A}(p,n)$ be a stable atom with electron cloud
$\mathcal{E} = p \cdot T_{2,3}$ partitioned into sub-Hopf
links $S_1 \sqcup \cdots \sqcup S_k \sqcup R$, where each
$S_i$ is closed and $R$ is the **residual sub-link** — the
outermost incomplete shell.  Then $\mathcal{A}$ exhibits
metallic character if and only if:

1. **Incompleteness**: $|R| < 2n_{k+1}^2$, so the outermost
   sub-link has unfilled linking sites.

2. **Low crossing energy**: the crossing energy
   ([crossing energy](#def:crossing-energy)) to attach or
   detach a trefoil from $R$ satisfies
   $\mathfrak{E}_{\mathrm{cross}}(R) \ll \mathfrak{E}_{\mathrm{cross}}(S_k)$ —
   the outermost curls are loosely wound compared to the
   inner closed shells.

3. **Site availability**: $R$ has at least one **open linking
   site** — a position in the trefoil chain where Hopf
   linking to an adjacent atom's residual sub-link is
   topologically permitted without disrupting the closed
   inner shells $S_i$.

**Metallic bonding as shared linking sites.**

In a metallic lattice, neighbouring atoms' residual sub-links
$R_a$ and $R_b$ share open linking sites.  The outermost
trefoils are not bound to any single nucleus — they Hopf-link
to whichever neighbouring residual sub-link offers the lowest
crossing energy.  This is the knot-theoretic picture of
**electron delocalisation**:

$$
  R_a \oplus R_b
   \leadsto 
  \text{shared sub-link } R_{ab}
  = 
  R_a \cup R_b \text{ with merged linking sites.}
$$

The delocalised trefoils form a **lattice-spanning sub-Hopf
chain** — a topological analogue of the conduction band.
Each trefoil can slide along the chain by a sequence of
Reidemeister II moves (crossing exchanges with neighbours)
without changing the total linking number.

**Strategy.**
The proof translates the phenomenological properties of metals into structural conditions on the sub-Hopf links. We correlate macroscopic conductivity with Reidemeister-II mobility of outermost knots, and formalize shared bonding via merged linking sites between residual sub-links. The energetic inequalities naturally follow from knot-theoretic crossing energies, culminating in the $\lambda(R)$ index.

**Classification by residual size.**

The number of electrons in the residual sub-link $|R|$ and
the next shell capacity $2n_{k+1}^2$ determine the
metallic properties:

| $\lvert R\rvert$ vs. capacity | Character | Examples |
|--------------------:|-----------|----------|
| $\lvert R\rvert = 1$ | Strong metal (alkalis) | Li, Na, K |
| $\lvert R\rvert = 2$ | Strong metal (alkaline earths) | Mg, Ca, Sr |
| $\lvert R\rvert \approx \tfrac{1}{2} \cdot 2n^2$ | Transition metal | Fe, Cu, Ni |
| $\lvert R\rvert = 2n^2 - 1$ | Weak nonmetal (halogens) | F, Cl, Br |
| $\lvert R\rvert = 2n^2$ | Noble gas (no residual) | He, Ne, Ar |

**Alkali metals** ($|R| = 1$) have a single trefoil in the
residual — one loose curl.  The crossing energy to detach it
is minimal, explaining why alkali metals have the lowest
ionization energies and highest reactivity in each period.

**Transition metals** have partially filled $d$-sub-links
($\ell = 2$, Seifert genus 2).  The $d$-sub-link has 10
linking sites; with $|R_d|$ between 1 and 9, the atom has
multiple open sites of similar crossing energy.  This produces:

- **Variable oxidation states**: different numbers of trefoils
  can be shared or detached, each costing similar energy.
- **Catalytic activity**: open $d$-sites can temporarily
  Hopf-link to substrate trefoils (bond activation), then
  release them — a topological picture of catalytic cycles.
- **Magnetic behaviour**: unpaired trefoils (those without a
  Hopf partner within $R_d$) carry uncompensated writhe,
  which manifests as a net magnetic moment.

**Conductivity as Reidemeister transport.**

Electrical conductivity corresponds to the **mobility of
delocalised trefoils** along the lattice-spanning sub-Hopf
chain.  Applying an external field biases the Reidemeister II
crossing exchanges in one direction, producing a net drift
of trefoils — i.e., electric current.

The resistance arises from **pinning sites**: locations where
the lattice chain has a local energy barrier for the crossing
exchange, caused by:

- Lattice defects (missing or extra nuclei disrupting the
  chain topology).
- Thermal fluctuations (random Reidemeister I moves that
  temporarily add or remove crossings).
- Phonons (periodic compressions of the chain that modulate
  the crossing energies).

At low temperature, the crossing exchanges proceed with
minimal disruption — explaining why metallic resistance
decreases with temperature.

**Contrast with noble gases.**

The [noble gas characterization](#prop:noble-gas-characterization)
shows that noble gases have $R = \varnothing$: no residual
sub-link, no open linking sites, no possibility of
delocalisation.  Metals and noble gases are thus the two
extremes of a single topological invariant — the
**residual linking number** $\lambda(R)$:

$$
  \lambda(R) = 0 \Longleftrightarrow \text{noble gas},
  \qquad
  \lambda(R) > 0 \Longleftrightarrow \text{non-inert}.
$$

Metallic character is strongest when $\lambda(R)$ is small
relative to the shell capacity (few electrons, many open
sites), and weakest when $\lambda(R)$ approaches the closure
threshold $2n^2$ (nearly full curls — approaching noble gas
behaviour).


**Remark on Mathematical Novelty:** Replacing qualitative atomic structure models with a rigid residual-linking-number lambda(R) classification introduces a highly novel knot-theoretic metric for metallic versus noble traits, formalizing Reidemeister-transport conductivity as a core algebraic topological property.
