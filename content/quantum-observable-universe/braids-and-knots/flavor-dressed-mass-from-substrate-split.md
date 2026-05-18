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
$O(\Delta m / M_N)^2$ correction) reads*

$$
  \mu_{\mathfrak{d}} - \mu_{\mathfrak{u}}
  \;\approx\;
  M_N \cdot \hbar_q^2 \cdot h_q \cdot [2]_q
  \cdot
  \frac{1}{z_{\mathrm{mkv}} \cdot \sqrt{q}}
  \;\;\;\;\text{(at } q = q_0 \text{).}
$$

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

## Numerical value at $q_0$

At $q = q_0 \approx 1.10998$ and using the CODATA nucleon-mass
average $M_N = (m_p + m_n)/2 \approx 938.92\,\text{MeV}$:

$$
  \mu_{\mathfrak{d}} - \mu_{\mathfrak{u}}
  \;\approx\;
  938.92 \cdot \frac{(0.110)^2 \cdot (1 - 0.658)}{3}
  \cdot
  \frac{2.005}{2.012}
  \;\approx\;
  1.288\,\text{MeV}.
$$

This matches the value previously assigned to
$\mu_{\mathfrak{d}} - \mu_{\mathfrak{u}}$ via CODATA
$m_n - m_p \approx 1.293\,\text{MeV}$ (residual $-0.4\%$,
attributable to the dropped $O((\Delta m / M_N)^2)$ term).

## Calibration discipline

The CODATA value $m_n - m_p = 1.29333251\,\text{MeV}$ is **no longer
an input** of the production formula under
[`prop:flavor-split-substrate`](../observations/flavor-split-substrate.md).
This proposition makes $\mu_{\mathfrak{d}} - \mu_{\mathfrak{u}}$ a
derived output of the substrate parameter $q_0$ plus $M_N$, removing
the $u$–$d$ splitting from the calibration count.

The remaining calibration inputs at the production-formula boundary
are $m_e$ and $q_0$ (with $Q_\beta$ as the third input until the
$Q_\beta$ substrate derivation lands; see
[`docs/audits/2026-05-17-1ppb-workplan-v4.md`](https://github.com/litlfred/qou/blob/main/docs/audits/2026-05-17-1ppb-workplan-v4.md) for the open status).

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

so $\bar\mu \approx M_N / 3 \approx 312.7\,\text{MeV}$.  Combined
with the substrate splitting, this gives
$\mu_{\mathfrak{u}} \approx 311.10\,\text{MeV}$ and
$\mu_{\mathfrak{d}} \approx 312.39\,\text{MeV}$; see the companion
remark [`rem:dressed-quark-numerology-at-q0`](dressed-quark-numerology-at-q0.md)
for the full numerology.
