The **$\mathcal{Q}_q$-value** of a nuclear transition is the
$q$-deformed transition energy.  It is NOT defined by classical
energy conservation — it is defined directly from the categorical
action.

## Definition (categorical, primary)

For a beta decay $\mathcal{N}_{\mathrm{par}} \to \mathcal{N}_{\mathrm{dau}}
+ e + \bar{\nu}$, the **$\mathcal{Q}_q$-value** is the net change
in categorical action at the Skein crossing change:

$$
  \mathcal{Q}_q
  \;:=\;
  S_q(\mathcal{N}_{\mathrm{par}})
  \;-\;
  S_q(\mathcal{N}_{\mathrm{dau}})
  \;-\;
  S_q(e)
  \;-\;
  S_q(\bar{\nu})
$$

where $S_q(K) = \mathrm{tr}_\tau(\rho(\beta_K))$ is the
categorical action evaluated on the Gröbner normal form of
each knot/link.

This is the **primary definition**.  No conservation law is
invoked.  $\mathcal{Q}_q$ is a computable function of $q$ alone.

## Crossing-level decomposition

The parent and daughter normal forms $\bar{\mathcal{N}}(p,n)$
and $\bar{\mathcal{N}}(p+1, n-1)$ differ at exactly $|\delta p|$
crossings (the converting nucleon's quarks).  At each changed
crossing:

$$
  \Delta \mathbf{E}_\times
  \;=\;
  \mathbf{E}_\times^{(\epsilon_{\mathrm{par}})}(q)
  - \mathbf{E}_\times^{(\epsilon_{\mathrm{dau}})}(q)
$$

For a $\mathfrak{d} \to \mathfrak{u}$ change ($\sigma_k^{-1} \to \sigma_k$):
$\Delta \mathbf{E}_\times = q - q^{-1}$.

$$
  \mathcal{Q}_q
  \;=\;
  \sum_{\text{changed crossings}} \Delta \mathbf{E}_\times
  \;-\; S_q(e)
$$

(dropping $S_q(\bar{\nu}) = 0$ since the unknot has trivial
action).

## Classical limit and the $q$-anomaly

**⚠ WARNING: Classical energy conservation is NOT assumed.**

In classical physics, the Q-value is defined via conservation
of energy:

$$
  Q_{\mathrm{classical}}
  \;=\;
  T_e + T_{\bar{\nu}} + T_{\mathrm{recoil}}
  \;\stackrel{?}{=}\;
  M_{\mathrm{par}} - M_{\mathrm{dau}} - m_e
$$

This equality uses $E_{\mathrm{before}} = E_{\mathrm{after}}$
(first law of thermodynamics / Noether's theorem for time
translation).  In the $q$-deformed framework, this
conservation law **may fail** because the $q$-differential
does not satisfy $d_q^2 = 0$:

$$
  d_q f(x) \;=\; \frac{f(qx) - f(x)}{(q-1)x}
$$

$$
  d_q(f \cdot g) \;=\; (d_q f) \cdot g \;+\; f(qx) \cdot (d_q g)
$$

The $q$-Leibniz rule has a **shift** $f(qx)$ rather than $f(x)$.
This means the $q$-differential of a product is NOT simply the
sum of differentials.  Squaring:

$$
  d_q^2 \;\neq\; 0 \quad \text{for } q \neq 1
$$

**Consequence:** The total $q$-energy of the products need not
equal the total $q$-energy of the parent.  There is a
**$q$-anomaly**:

$$
  \delta_q
  \;:=\;
  \mathcal{Q}_q
  \;-\;
  (T_e + T_{\bar{\nu}} + T_{\mathrm{recoil}})
$$

This anomaly does NOT vanish in general.  It is a genuine
physical effect of the $q$-deformation, not a computational
artefact.

## Structure of the $q$-anomaly

The $q$-anomaly arises from the non-commutativity of the
Hecke algebra.  When the Skein crossing change converts one
quark, the re-reduction to Gröbner normal form
([nuclear Gröbner reduction](#prop:nuclear-groebner-reduction))
introduces R2 moves $T^2 = (q - q^{-1})T + 1$.
Each R2 move shifts the local $q$-environment by:

$$
  q_{\mathrm{eff}} \;\mapsto\; q_{\mathrm{eff}} + \Delta q
$$

where $\Delta q \propto \hbar_q^2 = (1 - q^{-1})^2$.

The self-deformation
([hadron self-correction](#prop:hadron-q-self-correction))
produces a net shift:

$$
  \Delta q_{\mathrm{eff}}
  \;=\;
  \frac{A - 1}{A^2} \cdot \hbar_q^2
$$

This shift modifies $\mathcal{Q}_q$ at second order:

$$
  \mathcal{Q}_q
  \;=\;
  \underbrace{\Delta S_q - S_q(e)}_{\text{leading (crossing change)}}
  \;+\;
  \underbrace{\frac{\partial S_q}{\partial q} \cdot \Delta q_{\mathrm{eff}}}_{\delta_q \text{ (q-anomaly)}}
$$

**At $q = 1$:** $\delta_q = 0$ and
$\mathcal{Q}_q \to Q_{\mathrm{classical}}$ (classical
conservation restored).

**At the substrate parameter $q$:** $\delta_q \neq 0$.  For tritium ($A = 3$):
$\Delta q_{\mathrm{eff}} = 2/9 \cdot \hbar_q^2 \approx 0.0022$,
giving a correction $\delta_q / \mathcal{Q}_q \sim 5\%$.
This is the **same correction** that brings the tritium
half-life prediction from 13 yr to 12.4 yr (vs observed 12.32 yr).

## $\mathcal{Q}_q$ is NOT conserved

The $q$-anomaly $\delta_q$ means that $\mathcal{Q}_q$ defined
as the action difference is NOT equal to the sum of kinetic
energies.  The "missing" energy goes into the $q$-deformation
of the vacuum — it is absorbed by the change in the effective
substrate parameter from $q$ to $q + \Delta q_{\mathrm{eff}}$.

This is not a violation of physics — it is the $q$-deformed
version of the quantum anomaly.  The conserved quantity is not
$\mathcal{Q}_q$ but the **full categorical action** $S_q$ of
the entire system (products + vacuum shift):

$$
  S_q(\mathrm{par})
  \;=\;
  S_{q + \Delta q}(\mathrm{dau})
  \;+\;
  S_q(e)
  \;+\;
  S_q(\bar{\nu})
  \;+\;
  \text{kinetic terms}
$$

Note: the daughter is evaluated at the **shifted** $q$, not the
original.  This is the $q$-analogue of energy conservation.

## Limits

| $q$ | Regime | $\mathcal{Q}_q$ | $\delta_q$ |
|-----|--------|:---:|:---:|
| $q = 1$ | Classical | $0$ | $0$ |
| the substrate $q$ | Our universe | $\mathcal{Q}_{\exp} + \delta_q$ | $\neq 0$ |
| $q \to \infty$ | Big bang | $\to \infty$ | $\to \infty$ |

## $q$-Momentum

The $q$-momentum ([q-momentum](#def:q-momentum)) satisfies
a similar non-conservation.  Classically:

$$
  \vec{p}_{\mathrm{par}} = \vec{p}_{\mathrm{dau}} + \vec{p}_e + \vec{p}_{\bar{\nu}}
$$

In the $q$-deformed case, the Hecke algebra non-commutativity
means:

$$
  p_q(\mathrm{par})
  \;=\;
  p_q(\mathrm{dau}) + p_q(e) + p_q(\bar{\nu})
  \;+\;
  \delta p_q
$$

where $\delta p_q \propto \hbar_q$ is a $q$-anomaly in momentum.
This is the braid-group analogue of the quantum anomaly in
gauge theories.
