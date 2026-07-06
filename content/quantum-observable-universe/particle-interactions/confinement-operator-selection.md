**Proposition.**
*Among three-strand braid closures, the Borromean braid $\mathcal{B}_3 = (\sigma_0\sigma_1^{-1})^3$ is selected as the confinement operator by the topological principle of crossing-minimal Brunnian nontriviality. Its closure is the crossing-minimal nontrivial Brunnian three-link (every two-component sublink is the unlink). The Frobenius Gram and Markov-trace data act as a consistency check on this topologically selected operator, rather than its selector.*

We do not assert the Borromean braid $\mathcal{B}_3 = (\sigma_0\sigma_1^{-1})^3$ as the confinement operator out of convenience; a **topological** principle selects it. Confinement requires that no proper subset of the three quarks can be isolated. Equivalently, the braid closure must be a **Brunnian** link, and $\mathcal{B}_3$ provides the crossing-minimal such link.

This selection occurs on **braid/link space**, not on the $6\times 6$ Frobenius Gram matrix ([Frobenius Gram matrix](#prop:frobenius-gram-matrix)). A *minimum-action* (minimum-eigenvalue) functional on that matrix does **not** select $\mathcal{B}_3$. Because $\mathrm{NF}(\mathcal{B}_3)$ is $\approx 99.8\%$ the identity $\gamma$ (the maximum-cost channel), any cost-*minimising* operator-space program instead selects the smallest-cost **mesonic** channel $L_\pm$ (a two-strand pairwise object, not a three-quark confinement). The Gram and Markov-trace data below serve strictly as a **consistency check** on the topologically selected $\mathcal{B}_3$.

## Three unconfined quarks are unstable

Consider three quarks with typed crossings but no binding operator. In $H_3(q)$, the unconfined proton quarks $(\mathfrak{u}, \mathfrak{u}, \mathfrak{d})$ yield the product of typed crossing elements:

$$
  \mathrm{NF}(\sigma_0 \cdot (\sigma_0 - \tfrac{1}{2}H_A) \cdot (\sigma_1 - \tfrac{1}{2}H_A))
  =
  -0.105\gamma - 0.011\sigma_0 + 1.000\sigma_1 + 0.105 L_+.
$$

The **demand profile** (channels with negative NF coefficients) is $\{\gamma = -0.105, \sigma_0 = -0.011\}$. These negative coefficients signal instability. The unconfined state requires vacuum energy ($\gamma$) and crossing content ($\sigma_0$) from its environment. Free quarks have unmet demand and are not self-consistent.

For unconfined neutron quarks $(\mathfrak{u}, \mathfrak{d}, \mathfrak{d})$:

$$
  \mathrm{NF}(\text{unconfined } \mathfrak{n})
  =
  -0.211\gamma + 1.011\sigma_1,
$$

with demand $\{\gamma = -0.211\}$. This larger vacuum deficit reflects the extra down quark's $-H_A$ shift.

## Candidate operator comparison

We evaluate nine candidate confinement operators by applying each to the typed crossings and measuring three quantities:

1. **Net constraint**: $|\mathrm{net}(\Phi \cdot \mathrm{crossings}) - \mathrm{net}_{\mathrm{target}}|$
2. **Markov trace**: $\mathrm{tr}_M(\Phi \cdot \mathrm{crossings})$ (categorical action)
3. **Demand channels**: number of negative NF coefficients in the confined state

See [Table 1](#tbl:confinement-operator-selection-table1-data).

**Naive ranking.** Minimising demand channels and then $\mathfrak{E}_\times$ selects $L_+$. However, $L_+$ gives $\mathrm{net} \approx 1.22$, far from the physical proton mass. $L_+$ represents a pairwise (mesonic) binding; it does not confine three quarks. An operator-space cost-minimisation naturally falls into this channel, which is precisely what the **Brunnian constraint excludes**: a two-strand sublink is not Brunnian.

**Topological selection (primary).** Among three-strand braid closures, $\mathcal{B}_3 = (\sigma_0\sigma_1^{-1})^3$ is the *crossing-minimal nontrivial Brunnian* link. Its closure has three components, all three pairwise linking numbers vanish, yet every two-component sublink is the unlink (removing any one quark frees the other two). No braid of fewer than six crossings is nontrivially Brunnian. This selection relies on **no physical input**.

**Net consistency check.** We then confirm the topologically selected $\mathcal{B}_3$ against the physical data. Its $|\Delta\mathrm{net}|$ is closest (target $\approx :val[confinement_B3_net_proton]{precision=4}$) among the candidates, and it successfully confines. The identity has slightly lower trace ($0.415$ vs $0.420$), but it leaves the quark demand profile unchanged. See [Table 2](#tbl:confinement-operator-selection-table2-data). This match acts as a *consistency check* on the topological selection.

**Witness**: `confinement-operator-selection.witness.json`.

**Selection-principle support.** We derive the topological selection rigorously: the closure of $(\sigma_0\sigma_1^{-1})^3$ is a nontrivial six-crossing Brunnian three-link (pure braid, all pairwise linking numbers $0$, every two-sublink the unlink). Enumeration of all pure three-braids of word length $\le 6$ confirms no nontrivial Brunnian link exists below six crossings. At six crossings, the minimal Brunnian links all carry the Borromean signature. We refute the operator-space *minimum-action* selector analytically: the dense Wedderburn-projector SDP collapses to the minimum-eigenvector of the cost operator, which invariably yields the mesonic $L_\pm$, never $\mathcal{B}_3$.
