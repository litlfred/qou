**Proposition.**
*Let $\mu \colon \mathbf{Flavor} \to \mathbb{R}_{>0}$ be the flavor
dressing functor of [`def:flavor-dressing-functor`](flavor-dressing-functor.md),
let $M_N$ be the nucleon-mass average $(m_p + m_n)/2$, and let
$q = q_0$ be the substrate parameter.  Then the splitting between
the down- and up-quark dressed masses is determined by the substrate
flavor formula:*

$$
  \mu_{\mathfrak{d}} - \mu_{\mathfrak{u}}
  \;=\;
  M_N \cdot \frac{(q - 1)^2 (1 - q^{-4})}{3}
  \cdot
  \frac{q^{1/2} + q^{-1/2}}{q + q^{-1}}
  \;+\;
  O\!\left(\bigl(\Delta m / M_N\bigr)^2\right).
$$

*The leading-order substrate-pure form (dropping the
$O\!\left((\Delta m / M_N)^2\right)$ correction) reads, using the
algebraic identity $(q-1)^2 (1 - q^{-4})/3 = (1/3)\,\hbar_q^2 \cdot h_q \cdot [2]_q$,*

$$
  \mu_{\mathfrak{d}} - \mu_{\mathfrak{u}}
  \;\approx\;
  \frac{M_N}{3} \cdot
  \hbar_q^2 \cdot h_q \cdot
  \frac{[2]_q\,(q^{1/2} + q^{-1/2})}{q + q^{-1}}
  \;=\;
  \frac{M_N}{3} \cdot
  \hbar_q^2 \cdot h_q \cdot
  \frac{1}{z_{\mathrm{mkv}}}
  \;\;\;\;\text{(at } q = q_0 \text{)},
$$

*where $z_{\mathrm{mkv}} = (q^{1/2} + q^{-1/2})^{-1}$.  The
numerical evaluation at $q = q_0$ and the matching CODATA residual
are tabulated in
[`rem:dressed-quark-numerology-at-q0`](../observations/dressed-quark-numerology-at-q0.md)
(Observations chapter; per the manuscript convention numerical
substrate values stay out of geometry / braids chapters and are
collected with the other Physical-Observations numerology there).*

## Derivation

Combine two identities:

1. **Substrate side** ([`prop:flavor-split-substrate`](../observations/flavor-split-substrate.md)):

   $$
     \frac{m_n - m_p}{M_N}
     \;\approx\;
     \frac{(q-1)^2 (1 - q^{-4})}{3}.
   $$

2. **Skein side** (proved via [`lem:pair-skein-mass-formula`](../observations/pair-skein-mass-formula.md)
   applied to the Borromean baryon braids of the proton and neutron):

   $$
     m_n - m_p
     \;=\;
     \frac{q + q^{-1}}{q^{1/2} + q^{-1/2}}
     \cdot
     (\mu_{\mathfrak{d}} - \mu_{\mathfrak{u}}).
   $$

Solving (2) for $\mu_{\mathfrak{d}} - \mu_{\mathfrak{u}}$ and
substituting (1) gives the closed-form expression above.

## Calibration discipline

The CODATA value $m_n - m_p = 1.29333236\,\text{MeV}$ is **no longer
an input** of the production formula under
[`prop:flavor-split-substrate`](../observations/flavor-split-substrate.md).
This proposition makes $\mu_{\mathfrak{d}} - \mu_{\mathfrak{u}}$ a
derived output of the substrate parameter $q_0$ plus the nucleon-mass
scale $M_N = (m_p + m_n)/2$ (CODATA-anchored), removing the $u$–$d$
splitting from the calibration count.  $M_N$ itself is currently a
CODATA input (its substrate derivation is open — see
[`docs/audits/-1ppb-workplan-v4.md`](https://github.com/litlfred/qou/blob/main/docs/audits/-1ppb-workplan-v4.md)),
The calibration boundary for this proposition is $\{m_e, q_0,
M_N\}$.

The remaining calibration inputs at the production-formula boundary
are $m_e$ and $q_0$ (with $\mathfrak{Q}_\beta$ as the third input until the
$\mathfrak{Q}_\beta$ substrate derivation lands; see
[`docs/audits/-1ppb-workplan-v4.md`](https://github.com/litlfred/qou/blob/main/docs/audits/-1ppb-workplan-v4.md) for the open status).

## Individual values

The proposition pins the **difference** $\mu_{\mathfrak{d}} -
\mu_{\mathfrak{u}}$.  The individual values
$\mu_{\mathfrak{u}}, \mu_{\mathfrak{d}}$ require additionally an
average $\bar\mu = (\mu_{\mathfrak{u}} + \mu_{\mathfrak{d}})/2$,
which is pinned by the baryon-content sum-rule
([`prop:neutron-proton-mass-splitting`](../observations/neutron-proton-mass-splitting.md)
of the proton and neutron braids):

$$
  m_p + m_n = 3(\mu_{\mathfrak{u}} + \mu_{\mathfrak{d}})
    + \text{(Skein cross-terms)},
$$

so $\bar\mu \approx M_N / 3 \approx 312.97\,\text{MeV}$.  Combined
with the substrate splitting, this gives
$\mu_{\mathfrak{u}} \approx 311.10\,\text{MeV}$ and
$\mu_{\mathfrak{d}} \approx 312.39\,\text{MeV}$; see the companion
remark [`rem:dressed-quark-numerology-at-q0`](../observations/dressed-quark-numerology-at-q0.md)
for the full numerology.
