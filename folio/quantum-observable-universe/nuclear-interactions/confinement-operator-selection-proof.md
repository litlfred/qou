## Topological selection versus operator-space cost

A topological principle selects the Borromean braid $\mathcal{B}_3 = (\sigma_0\sigma_1^{-1})^3$ as the confinement operator. The model encodes confinement, the requirement that no proper subset of the three quarks can be isolated, as the requirement that the braid closure be a nontrivial three-component Brunnian link. $\mathcal{B}_3$ is a crossing-minimal three-strand braid with this property (shown below).

This selection occurs on braid space, not on the Frobenius Gram matrix. A minimum-action functional on that matrix does not select $\mathcal{B}_3$. Because $\mathrm{NF}(\mathcal{B}_3)$ is $\approx 99.8\%$ the identity $\mathbf{1}$, any cost-minimising operator-space program selects the smallest-cost mesonic channel $L_\pm$. The Gram and Markov-trace data serve strictly as a consistency check.

## Three unconfined quarks are unstable

In $H_3(q)$, the unconfined proton quarks $(\mathfrak{u}, \mathfrak{u}, \mathfrak{d})$ yield the product of typed crossing elements:

$$
  \mathrm{NF}(\sigma_0 \cdot (\sigma_0 - \tfrac{1}{2}h_{\mathrm{A}}) \cdot (\sigma_1 - \tfrac{1}{2}h_{\mathrm{A}}))
  =
  -0.105\,\mathbf{1} - 0.011\sigma_0 + 1.000\sigma_1 + 0.105 L_+.
$$

The demand profile $\{[\mathbf{1}] = -0.105, \sigma_0 = -0.011\}$ (with $[\mathbf{1}]$ the coefficient of the identity word $\mathbf{1}$) signals instability. The unconfined state requires vacuum energy ($\mathbf{1}$) and crossing content ($\sigma_0$) from its environment.

For unconfined neutron quarks $(\mathfrak{u}, \mathfrak{d}, \mathfrak{d})$:

$$
  \mathrm{NF}(\text{unconfined } \mathfrak{n})
  =
  -0.211\,\mathbf{1} + 1.011\sigma_1,
$$

with demand $\{[\mathbf{1}] = -0.211\}$. This larger vacuum deficit reflects the extra down quark's $-h_{\mathrm{A}}$ shift.

## Candidate operator comparison

Evaluate nine candidate confinement operators by applying each to the typed crossings and measuring three quantities:

1. **Net constraint**: $|\mathrm{net}(\Phi \cdot \mathrm{crossings}) - \mathrm{net}_{\mathrm{target}}|$
2. **Markov trace**: $\mathrm{tr}_M(\Phi \cdot \mathrm{crossings})$ (categorical action)
3. **Demand channels**: number of negative NF coefficients in the confined state

**Naive ranking.** Minimising demand channels and then $\mathfrak{E}_\times$ selects $L_+$. $L_+$ represents a pairwise binding. An operator-space cost-minimisation falls into this channel, which the Brunnian requirement excludes.

**Topological selection.** The closure of $\mathcal{B}_3 = (\sigma_0\sigma_1^{-1})^3$ is the Borromean rings: three components, all pairwise linking numbers zero, and every two-component sublink the unlink, so it is a nontrivial Brunnian link \cite{kawauchi1996}. (The braid-level form of this statement is recorded separately as [`conj:brunnian-property-of-borromean`](#conj:brunnian-property-of-borromean), pending formalisation.) No three-strand braid with fewer than six crossings closes to a nontrivial three-component Brunnian link. The closure of such a braid is a three-component link of crossing number at most five. In the Rolfsen table every prime link with three components has at least six crossings \cite{rolfsen}, so the closure is split or composite. A Brunnian link has every proper sublink trivial. A split three-component link that is not the unlink has a nontrivial proper sublink: a knotted component, or a split-off linked pair. A composite three-component link of crossing number at most five is the connected sum of two Hopf links, and its two end components form a Hopf link. In neither case is the link nontrivially Brunnian. This selection uses no physical input; the comparison of $\mathrm{net}$ values with physical data lies outside the proof (see [the interpretation](#rem:confinement-operator-selection-interpretation)).
