The Borromean braid $\mathcal{B}_3 = (\sigma_0\sigma_1^{-1})^3$ is not
asserted as the confinement operator — it is **selected** by a
**topological** principle. Confinement means *no proper subset of the
three quarks can be isolated*; equivalently, the braid closure is a
**Brunnian** link (every two-component sublink is the unlink), and
$\mathcal{B}_3$ is the crossing-minimal such link.

This selection lives on **braid/link space**, not on the
$6\times 6$ Frobenius Gram matrix
([Frobenius Gram matrix](#prop:frobenius-gram-matrix)): a
*minimum-action* (minimum-eigenvalue) functional on that matrix does
**not** select $\mathcal{B}_3$. Because $\mathrm{NF}(\mathcal{B}_3)$ is
$\approx 99.8\%$ the identity $\gamma$ — the maximum-cost channel — any
cost-*minimising* operator-space program selects instead the
smallest-cost **mesonic** channel $L_\pm$ (a two-strand pairwise object,
not a three-quark confinement). The Gram/Markov-trace data below is a
**consistency check** on the topologically selected $\mathcal{B}_3$, not
its selector.

## Three unconfined quarks are unstable

Consider three quarks with typed crossings but no binding operator.
In $H_3(q)$, the unconfined proton quarks $(\mathfrak{u}, \mathfrak{u}, \mathfrak{d})$
give the product of typed crossing elements:

$$
  \mathrm{NF}(\sigma_0 \cdot (\sigma_0 - \tfrac{1}{2}H_A) \cdot (\sigma_1 - \tfrac{1}{2}H_A))
  =
  -0.105\gamma - 0.011\sigma_0 + 1.000\sigma_1 + 0.105 L_+.
$$

The **demand profile** — channels with negative NF coefficients —
is $\{\gamma = -0.105, \sigma_0 = -0.011\}$.  These negative coefficients
signal instability: the unconfined state requires vacuum energy
($\gamma$) and crossing content ($\sigma_0$) from its environment.
Free quarks have unmet demand and are not self-consistent.

For unconfined neutron quarks $(\mathfrak{u}, \mathfrak{d}, \mathfrak{d})$:

$$
  \mathrm{NF}(\text{unconfined } \mathfrak{n})
  =
  -0.211\gamma + 1.011\sigma_1,
$$

with demand $\{\gamma = -0.211\}$ — a larger vacuum deficit,
reflecting the extra down quark's $-H_A$ shift.

## Candidate operator comparison

We evaluate nine candidate confinement operators by applying
each to the typed crossings and measuring three quantities:

1. **Net constraint**: $|\mathrm{net}(\Phi \cdot \mathrm{crossings}) - \mathrm{net}_{\mathrm{target}}|$
2. **Markov trace**: $\mathrm{tr}_M(\Phi \cdot \mathrm{crossings})$ (categorical action)
3. **Demand channels**: number of negative NF coefficients in the confined state

See [Table 1](#tbl:confinement-operator-selection-table1-data).

**Naive ranking** (minimise demand channels, then $\mathfrak{E}_\times$) selects
$L_+$ — but $L_+$ gives $\mathrm{net} \approx 1.22$, far from the
physical proton mass.  $L_+$ is a pairwise (mesonic) binding; it does
not confine three quarks.  This is precisely the channel an operator-space
cost-minimisation falls into, and precisely what the **Brunnian
constraint excludes**: a two-strand sublink is not Brunnian.

**Topological selection (primary).** Among three-strand braid closures,
$\mathcal{B}_3 = (\sigma_0\sigma_1^{-1})^3$ is the *crossing-minimal
nontrivial Brunnian* link — its closure has three components, all three
pairwise linking numbers vanish, yet every two-component sublink is the
unlink (removing any one quark frees the other two). No braid of fewer
than six crossings is nontrivially Brunnian. This selection uses **no
physical input**.

**Net consistency check.** The topologically selected $\mathcal{B}_3$ is
then confirmed against the physical data: its $|\Delta\mathrm{net}|$ is
closest (target $\approx :val[confinement_B3_net_proton]{precision=4}$)
among the candidates, and it confines (the identity has slightly lower
trace, $0.415$ vs $0.420$, but leaves the quark demand profile
unchanged). See [Table 2](#tbl:confinement-operator-selection-table2-data).
This match is a *consistency check* on the topological selection, not the
selector itself.

## Beta decay emerges from the confined demand

The $\mathcal{B}_3$-confined proton NF has residual demand:

$$
  \mathrm{NF}(\mathfrak{p})
  =
  \underbrace{-0.100}_{\gamma < 0}\gamma
  + 0.036\sigma_0 + 0.998\sigma_1 + 0.099 L_+ + 0.009 L_-
  + \underbrace{-0.043}_{e^- < 0}e^-.
$$

- $\gamma < 0$: vacuum energy deficit — the source of the nucleon's mass
  (filled by the Borromean volume $\mathrm{Vol}(\mathcal{B}_3)$).
- $e^- < 0$: **trefoil demand** — the nucleon demands an electron.
  This is the categorical beta decay channel.

For the neutron, the demand is larger:
$\gamma = -0.202$, $L_+ = -0.010$, $e^- = -0.044$.
The additional $L_+$ deficit (Hopf link demand) and larger $\gamma$
deficit provide the energy that drives $\mathfrak{n} \to \mathfrak{p} + e^- + \bar\nu$.

## Confinement universality

The confined nucleon NF depends only on $q_0$ and the quark types
$(\mathfrak{u}, \mathfrak{u}, \mathfrak{d})$ or
$(\mathfrak{u}, \mathfrak{d}, \mathfrak{d})$.  It is
**independent of the photon polarization** $(\varphi_0, \varphi_1, \varphi_{01})$
that created the quarks via $\gamma\gamma$ pair production.  The strong
interaction ($\mathcal{B}_3$ confinement) washes out the electromagnetic
initial conditions.

**Witness**: `confinement-operator-selection.witness.json`.

**Selection-principle support.** The topological selection is verified by
`computations/probes/b3_brunnian_selection_scope.py` (the closure of
$(\sigma_0\sigma_1^{-1})^3$ is a nontrivial six-crossing Brunnian
three-link — pure braid, all pairwise linking numbers $0$, every
two-sublink the unlink) and
`computations/probes/b3_brunnian_minimality_enumeration.py` (enumerating
all pure three-braids of word length $\le 6$: no nontrivial Brunnian link
below six crossings, and at six crossings the minimal Brunnian links all
carry the Borromean signature). The refutation of the operator-space
*minimum-action* selector is recorded in
`computations/probes/b3_dense_sdp_wedderburn_projector.py` (the dense
Wedderburn-projector SDP collapses to the minimum-eigenvector of the cost
operator, which is the mesonic $L_\pm$, never $\mathcal{B}_3$).
