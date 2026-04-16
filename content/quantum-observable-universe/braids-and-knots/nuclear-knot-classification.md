**Proposition.**
*The closure of the nuclear braid $\mathcal{N}(Z,N)$ in $H_3(q)$
falls into one of four knot types, each determining the binding
scale through its geometric invariant:*

| $A$ | Knot type | Chirality | Bulk factor | Value |
|-----|-----------|-----------|-------------|-------|
| $1$ | unknot $0_1$ | — | $0$ (free) | $0$ |
| $2$ | satellite (Hopf) | 1 chiral pn | $1 + h$ | $\approx 1.209$ |
| $3$ | figure-eight $4_1$ | 1 amphicheiral | $1 - h^2$ | $\approx 0.956$ |
| $4$ | Borromean $\mathcal{B}_3$ | 2 amphicheiral | $(1 - h^2)^2$ | $\approx 0.914$ |
| $\geq 5$ | Borromean (generic) | $\to 1$ | $1$ | $1$ |

*The bulk factor is the Frobenius norm deviation from the identity
braid, determined by the amphicheiral property:*

- **Amphicheiral** knots ($K = \bar{K}$, e.g.\ $4_1$): the Frobenius
  self-pairing is real, giving deviation $h^2 = (q - q^{-1})^2$ per
  nucleon pair.  Factor: $(1 - h^2)^{n_{\mathrm{pairs}}}$.
- **Chiral** knots (e.g.\ satellite pn): deviation $h$ (first order).
  Factor: $1 + h$ for positive chirality.
- **Large-$A$ limit**: $(1 - h^2)^{n} \to 1$ as $n \to \infty$,
  recovering the standard BW formula.

*Proof.*
The nuclear braid $\mathcal{N}(Z,N)$ is built by interleaving $Z$
proton NFs and $N$ neutron NFs with typed crossings (pp, nn, pn).
Each nucleon NF is the Borromean braid $\mathcal{B}_3$ dressed with
quark crossings.

For $A = 3$: the three nucleon NFs compose to give a braid whose
NF has alternating $\sigma_0, \sigma_1$ signs and dominant $L_+$
(Hopf link) content.  This is the NF signature of the figure-eight
knot $4_1 = \sigma_0\sigma_1^{-1}\sigma_0^{-1}\sigma_1$, verified
by comparing eigenvalue structure.

For $A \geq 4$: the composition of four or more nucleon NFs
produces identity-dominated NF with small Hopf corrections — the
signature of the Borromean link, confirmed by the Frobenius
positivity $G \cdot x \geq 0$ at all six basis channels.

The binding scale follows from the topological mass formula
([topological mass formula](#prop:topological-mass-formula)):
$\mathfrak{m}(K) = \mathrm{Vol}(K)/\hbar_q^2$.  The volume
determines the energy scale at which the nuclear braid binds.

The figure-eight volume $\mathrm{Vol}(4_1) = 2.030$ is the SAME
volume that defines the substrate parameter $q_0$ through
$\hbar_q^2 = \mathrm{Vol}(4_1)/(m_\mu/m_e)$.  So $A = 3$ nuclei
bind at the scale set by the substrate itself.  $\square$
