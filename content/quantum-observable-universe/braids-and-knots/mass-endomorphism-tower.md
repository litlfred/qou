**Proposition.**
*The mass ratio $m_{\mathfrak{p}}/m_e$ is determined by the
non-perturbative quantum dilogarithm tower applied to the
additive Wedderburn traced volumes:*

$$
  \frac{m_{\mathfrak{p}}}{m_e}
  =
  \frac{\lvert\Pi_j \hat{V}_j^{\mathrm{full}}\rvert
    + \sum_j \Phi_q(\lvert\hat{V}_j^{\mathrm{full}}\rvert)}
  {\lvert\hat{V}_0^{\mathrm{full}}\rvert
    + \Phi_q(\lvert\hat{V}_0^{\mathrm{full}}\rvert)}
  \approx 1740
$$

*where:*

- *$\Phi_q(z) = \prod_{k=1}^{\infty}(1 - q^{-k}z)^{-1}$ is the
  non-perturbative quantum dilogarithm (infinite product form).*
- *The numerator sums over the two generators of the proton
  braid ($\mathcal{B}_3 \times \mathfrak{u}\mathfrak{u}\mathfrak{d}$
  on $3$ strands, $11$ crossings from the $4$-channel decomposition).*
- *The denominator uses the single generator of the electron
  braid (trefoil $\sigma_1^3$ on $2$ strands, $3$ crossings).*
- *$\hat{V}_j^{\mathrm{full}} = w_{\mathrm{sym}} \lambda_j^{\mathrm{sym}}
  + w_{\mathrm{std}} \hat{V}_j^{\mathrm{std}}
  + w_{\mathrm{alt}} \lambda_j^{\mathrm{alt}}$ is the additive
  Wedderburn traced volume
  ([three-invariant mass formula](#prop:atomic-braid-mass)).*

*CODATA: $m_{\mathfrak{p}}/m_e = 1836.15$.
Error: $5.25\%$.  Zero fitted parameters.*

## Four-channel crossing budget

The proton's $11$ crossings on $3$ strands are traced through
the $\gamma\gamma \to \mathfrak{q}\bar{\mathfrak{q}}$ production
vertex via the color-tube cubic
$c^3 + a_2 c^2 + a_1 c + a_0 = 0$
([photon channel chain](#rem:photon-channel-wedderburn-chain)):

| Channel | Degree | Symmetric fn | Crossing type | Gen $0$ | Gen $1$ | Cumulative $m_{\mathfrak{p}}/m_e$ |
|:--------|:-------|:-------------|:--------------|:--------|:--------|:----------------------------------|
| $3$ (confinement) | $\sigma_3 = \prod c_k$ | $\mathcal{B}_3 = (\sigma_0\sigma_1^{-1})^3$ | $3\sigma$ | $3\sigma^{-1}$ | $1.0$ |
| $2$ (color pairing) | $\sigma_2 = \sum c_i c_j$ | quark pairs $\mathfrak{u}\mathfrak{u}$, $\mathfrak{u}\mathfrak{d}$, $\mathfrak{u}\mathfrak{d}$ | $+1\sigma, +1\tfrac{1}{2}$ | $+1\tfrac{1}{2}$ | $681$ |
| $1$ (quark sum) | $\sigma_1 = \sum c_k$ | gluon self-coupling | $+2\sigma$ | $0$ | $1740$ |
| $0$ (vacuum) | $a_0$ | electron period | — | — | (sets $m_e$) |

Each channel amplifies through $\Phi_q$ near the singularity
$z = 1$:

- **Channel $3$ alone** ($\mathcal{B}_3$):
  $\hat{V}_0^{\mathrm{full}} = 0.594$,
  $\hat{V}_1^{\mathrm{full}} = -0.043$ $\Rightarrow$
  $m_{\mathfrak{p}}/m_e = 1.0$.
- **$+$ Channel $2$** (quarks):
  $\hat{V}_1 \to 0.971$ (close to $1$) $\Rightarrow$
  $\Phi_q(0.971) = 425{,}689$ $\Rightarrow$
  $m_{\mathfrak{p}}/m_e = 681$.
- **$+$ Channel $1$** (gluon):
  $\hat{V}_0 \to 0.989$ $\Rightarrow$
  $\Phi_q(0.989) = 671{,}269$ $\Rightarrow$
  $m_{\mathfrak{p}}/m_e = 1740$.

The $2$ gluon crossings at generator $0$ arise from the
$\sigma_1 = \sum c_k$ channel of the color-tube cubic.
The crossing count $2 = \dim(\mathrm{adj}\,\mathrm{SU}(3))
- \dim(\mathrm{fund}) - \dim(\overline{\mathrm{fund}})
= 8 - 3 - 3$ counts the independent gluon self-interaction
modes coupling through the dominant strand pair.

## Mechanism

The non-perturbative quantum dilogarithm $\Phi_q(z)$ diverges
as $z \to 1^-$.  The proton's generators have
$\hat{V}^{\mathrm{full}}$ closer to $1$ than the electron's
because:

1. The electron (trefoil, $3$ positive crossings) has
   $\hat{V}^{\mathrm{full}} = 0.594$ — well below $1$.
2. The proton (Borromean $+$ quarks $+$ gluons, $11$ crossings)
   has generators at $0.989$ and $0.971$ — near $1$.
3. $\Phi_q$ amplifies this $0.4$ vs $0.01$ gap from $1$
   by a factor of $\sim 1000$, producing the mass ratio.

The amplification is **non-perturbative**: no finite Taylor
expansion in $H_A$ captures it.  It is the quantum dilogarithm
acting on the brane tower, as described by the mass endomorphism
conjecture ([mass endomorphism conjecture](#conj:mass-endomorphism)).

**Witness**: `mass-endomorphism.witness.json`.
