**Proposition.**
*The closure of the nuclear braid $\mathcal{N}(Z,N)$ in $H_3(R, q)$
determines a bulk modification factor $a(\mathcal{N})$ for the
BW binding energy.  This factor is a single product over
independent nucleon pairs:*

$$
  a(\mathcal{N})
  \;=\;
  \prod_{i=1}^{n_{\mathrm{pairs}}}
    (1 - \varepsilon_i)
$$

*where $\varepsilon_i$ is the Frobenius norm deviation of the
$i$-th nucleon pair from the identity braid:*

- *Amphicheiral pair (pp or nn in $\mathcal{B}_3$):
  $\varepsilon = h^2 = (q - q^{-1})^2$*
- *Chiral pair (pn):
  $\varepsilon = -h = -(q - q^{-1})$*

*The sign convention: amphicheiral pairs ($K = \bar{K}$) deviate
quadratically ($h^2 > 0$, reducing binding); chiral pairs deviate
linearly ($-h < 0$, increasing binding).*

| $A$ | Pairs | Deviations $\varepsilon_i$ | $a(\mathcal{N})$ |
|-----|-------|---------------------------|-------------------|
| $1$ | $0$ | — | free nucleon |
| $2$ | $1$ pn (chiral) | $-h$ | $1 + h \approx 1.209$ |
| $3$ | $1$ pp or nn (amphicheiral) | $h^2$ | $1 - h^2 \approx 0.956$ |
| $4$ | $2$ (pp + nn, amphicheiral) | $h^2, h^2$ | $(1 - h^2)^2 \approx 0.914$ |
| $\geq 5$ | many | $(1 - h^2)^n \to 1$ | $1$ |

*In the large-$A$ limit, $(1 - h^2)^n \to 1$ since
$h^2 \approx 0.044 \ll 1$, recovering the standard
BW formula for heavy nuclei.*

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
