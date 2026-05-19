The Borromean braid $\mathcal{B}_3 = (\sigma_0\sigma_1^{-1})^3$ is not
asserted as the confinement operator — it is **selected** by the
minimum-action principle
([knot operator selection](#prop:knot-operator-selection))
acting on the $6 \times 6$ Gram matrix
([Frobenius Gram matrix](#prop:frobenius-gram-matrix)).

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

| Candidate $\Phi$ | $\mathrm{net}(\mathfrak{p})$ | $|\Delta\mathrm{net}|$ | $\mathrm{tr}_M$ | Demand |
|:---|---:|---:|---:|:---:|
| $\mathcal{B}_3 = (\sigma_0\sigma_1^{-1})^3$ | $:val[confinement_B3_net_proton]{precision=4}$ | $0.000$ | $0.420$ | $2$ |
| $L_+ = \sigma_0\sigma_1$ | $:val[confinement_Lplus_net_proton]{precision=4}$ | $0.221$ | $0.558$ | $0$ |
| $e^- = \sigma_0\sigma_1\sigma_0$ | $+1.244$ | $0.245$ | $0.369$ | $0$ |
| $\mathbf{1}$ (identity) | $:val[confinement_id_net_proton]{precision=4}$ | $0.010$ | $0.415$ | $2$ |
| $(\sigma_0\sigma_1)^2$ | $+1.291$ | $0.292$ | $0.724$ | $0$ |
| $\sigma_0\sigma_1^{-1}$ | $+1.009$ | $0.010$ | $0.507$ | $2$ |

**Naive ranking** (minimise demand channels, then $\mathbf{E}_\times$) selects
$L_+$ — but $L_+$ gives $\mathrm{net} \approx 1.22$, far from the
physical proton mass.  $L_+$ is a pairwise (mesonic) binding; it does
not confine three quarks.

**Net-constrained ranking** ($|\Delta\mathrm{net}|$ closest to target
$\approx :val[confinement_B3_net_proton]{precision=4}$) uniquely selects $\mathcal{B}_3$:

| Rank | Operator | $|\Delta\mathrm{net}|$ | $\mathrm{tr}_M$ |
|:---:|:---|---:|---:|
| 1 | $\mathcal{B}_3$ | $0.000$ | $0.420$ |
| 2 | $\mathbf{1}$ (identity) | $0.010$ | $0.415$ |
| 3 | $\sigma_0\sigma_1^{-1}$ | $0.010$ | $0.507$ |

The identity has slightly lower trace ($0.415$ vs $0.420$) but
fails to confine: unconfined quarks retain their demand profile
unchanged.  $\mathcal{B}_3$ is the **unique operator that matches the
physical net AND provides topological confinement** (Borromean =
no subset of quarks can be isolated).

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
