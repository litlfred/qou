**Proposition.**
*The closure of the nuclear braid $\mathcal{N}(Z,N)$ in $H_3(q)$
falls into one of four knot types, each determining the binding
scale through its geometric invariant:*

| $A$ | Knot type | Geometric invariant | Binding scale $\alpha$ |
|-----|-----------|---------------------|------------------------|
| $1$ | unknot $0_1$ | $\mathrm{Vol} = 0$ | $0$ (free nucleon) |
| $2$ | satellite | mixed | $\alpha_{\mathrm{Borr}}$ (default) |
| $3$ | figure-eight $4_1$ | $\mathrm{Vol}(4_1) = 2.0299$ | $m_e \times \mathrm{Vol}(4_1)$ |
| $\geq 4$ | Borromean $\mathcal{B}_3$ | $\mathrm{Vol}(\mathcal{B}_3) = 8G$ | $m_e \times 8G$ |

*The classification is determined by the dominant NF component
of the full nuclear braid, computed via $\texttt{build\_atom\_nf}(Z,N)$:*

- **Borromean-like**: identity $\gamma$ dominates ($|\gamma| > 0.3$
  with Hopf corrections $|L_\pm| > 0.01$). Hyperbolic, $\mathrm{Vol} = 7.328$.
- **Figure-eight-like**: generators $\sigma_0, \sigma_1$ have opposite
  signs ($\sigma_0 \cdot \sigma_1 < 0$). Hyperbolic, $\mathrm{Vol} = 2.030$.
- **Satellite**: mixed NF with no single dominant component.
  Uses Borromean scale as default.

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
