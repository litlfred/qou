The mass integrand
$\alpha_\varrho = (\int_A \otimes \mathrm{id}) \circ \Delta \circ \varrho$
splits along two orthogonal directions in the Hecke algebra, corresponding
to the two Markov moves of the braid group.

| Restriction | Markov move | $H_n(R, q)$ element | Physical invariant |
|---|---|---|---|
| Horizontal | Conjugation (within a fibre) | $\rho(\beta)$ | Charge $Q$, crossing energy $\mathfrak{E}_{\mathrm{cross}}$ |
| Vertical | Stabilisation (along the tower) | $\Phi_{\mathrm{mass}}(\beta)$ | Mass $\mathfrak{m} = \lvert \mathrm{tr}_M(\Phi_{\mathrm{mass}}(\beta)) \rvert$ |
| Mixed | Both simultaneously | $Y(a, z)$ (vertex operator) | Full particle data |

The Frobenius pairing $\langle a, b \rangle_F = \int_A \mu(a \otimes b)$
mediates the duality: it pairs $\mu$ (horizontal) with $\int_A$ (vertical).

**Horizontal restriction (conjugation, within a fibre).**
Restricting to a single level of the brane tower (crossings within
$V^{\otimes n}$ with no tower propagation), the Hecke element
$\rho(\beta) \in H_n(R, q)$ encodes the crossing structure directly.
The crossing energy
([crossing energy](#def:crossing-energy)) reads off the Skein
eigenvalue sum
$\mathfrak{E}_{\mathrm{cross}} = n_+ q - n_- q^{-1}$,
and the Coulomb charge
([Coulomb charge](#def:coulomb-charge)) is the crossing asymmetry
$Q = \tfrac{1}{2}(n_+ - n_-)$.
These are **horizontal** invariants: they depend on the braiding
pattern, not on the depth of the tower.

**Vertical restriction (stabilisation, along the tower).**
The Hecke mass element
$\Phi_{\mathrm{mass}}(\beta) \in H_n(R, q)$
([Hecke mass element](#def:hecke-mass-element)) dresses
$\rho(\beta)$ with the Frobenius--comultiplication operator
$(\int_A \otimes \mathrm{id}) \circ \Delta$, which projects
through the Frobenius form (collapsing tower data) and
comultiplies (probing the tower depth).
Its Markov trace
([mass via Markov trace](#prop:hecke-mass-trace)) gives the
categorical mass $\mathfrak{m} = \lvert \mathrm{tr}_M(\Phi_{\mathrm{mass}}(\beta)) \rvert$,
a **vertical** invariant measuring resistance to
transport through the comultiplication.

**Mixed: the vertex operator as generating function.**
On the mixture (when horizontal crossings and vertical tower
steps act simultaneously), the result is the vertex operator
$Y(a, z)$ ([vertex operator](#def:vertex-operator)), whose modes

$$
  a_m
  =
  \mathrm{tr}_M\!\bigl(\check{R}_{(a)}\, z^m\bigr)
$$

combine horizontal braiding ($\check{R}$, the $R$-matrix) with
vertical insertion ($z^m$, the tower coordinate on
$\mathcal{S}_p$).  The vertex operator is the generating function
that encodes both charge and mass data simultaneously.

**The Frobenius pairing as mediator.**
The duality between horizontal and vertical is mediated by the
Frobenius pairing
([Frobenius pairing](#def:frobenius-pairing)):

$$
  \langle a, b \rangle_F
  =
  \textstyle\int_A \mu(a \otimes b),
$$

which pairs multiplication $\mu$ (horizontal: composing crossings)
with the Frobenius form $\int_A$ (vertical: integrating along the
tower).  This pairing identifies the particle element
$\rho(\beta)$ (charge carrier) with the mass element
$\Phi_{\mathrm{mass}}(\beta)$ (mass carrier) as dual aspects of a
single Hecke algebra element, connected by exactly the
Frobenius--comultiplication map that defines the categorical mass.
