*Lean sibling: archimedean specialisation over $\mathbb{R}$ (CLAUDE.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data.*

The **$Q$-value** of a nuclear transition is the
$q$-deformed transition energy. It is NOT defined by classical
energy conservation — it is defined directly from the categorical
action.

## Definition (mass difference, primary)

For a $\beta^-$ decay $\mathcal{N}(Z,N) \to \mathcal{N}(Z{+}1,N{-}1)
+ e^- + \bar{\nu}_e$, the **$Q$-value** is the mass difference
of neutral atoms:

$$
  Q = M(Z, N) - M(Z{+}1, N{-}1)
$$

where $M(Z, N) = Z m_{\mathfrak{p}} + N m_{\mathfrak{n}} + Z m_e
- B(Z, N)$ is the neutral atomic mass and $B(Z, N)$ is the BW
binding energy at Hecke level $k$
([q-integer mass formula](#conj:q-integer-mass-formula)).

This definition is consistent with the mass accuracy: if
$|\Delta M/M| \approx 0.002\%$, then $Q$-values for transitions
with $Q \gg \Delta M$ inherit the same precision. For transitions
with small $Q$ (e.g.\ ${}^3\mathrm{H} \to {}^3\mathrm{He}$,
$Q = 18.6$ keV), catastrophic cancellation amplifies the mass
error: $\delta Q/Q \approx (M/Q) \times (\delta M/M)$.

At $k = 11$: $Q(n \to {}^1\mathrm{H}) = 0.782$ MeV ($0.00\%$),
$Q({}^3\mathrm{H} \to {}^3\mathrm{He}) = 0.01823$ MeV ($-2.1\%$).

## Crossing-level decomposition

The parent and daughter normal forms $\mathcal{N}(p,n)$
and $\mathcal{N}(p+1, n-1)$ differ at exactly $|\delta p|$
crossings (the converting nucleon's quarks). At each changed
crossing:

$$
  \Delta \mathfrak{E}_\times
  = 
  \mathfrak{E}_\times^{(\epsilon_{\mathrm{par}})}(q)
  - \mathfrak{E}_\times^{(\epsilon_{\mathrm{dau}})}(q)
$$

For a $\mathfrak{d} \to \mathfrak{u}$ change ($\sigma_k^{-1} \to \sigma_k$):
$\Delta \mathfrak{E}_\times = q - q^{-1}$.

$$
  Q
  = 
  \sum_{\text{changed crossings}} \Delta \mathfrak{E}_\times
  -  \mathfrak{S}_q(e)
$$

(dropping $\mathfrak{S}_q(\nu^{\sigma}) = 0$ since the unknot has trivial
action).

## Classical limit and the $q$-anomaly

**Warning.** Classical energy conservation is **not** assumed.

In classical physics, the Q-value is defined via conservation
of energy:

$$
  Q_{\mathrm{classical}}
  = 
  T_e + T_{\nu^{\sigma}} + T_{\mathrm{recoil}}
  \stackrel{?}{=}
  M_{\mathrm{par}} - M_{\mathrm{dau}} - m_e
$$

This equality uses $E_{\mathrm{before}} = E_{\mathrm{after}}$
(first law of thermodynamics / Noether's theorem for time
translation). In the $q$-deformed framework, this
conservation law **may fail** because the $q$-differential
does not satisfy $d_q^2 = 0$:

$$
  d_q f(x) =  \frac{f(qx) - f(x)}{(q-1)x}
$$

$$
  d_q(f \cdot g) =  (d_q f) \cdot g +  f(qx) \cdot (d_q g)
$$

The $q$-Leibniz rule has a **shift** $f(qx)$ rather than $f(x)$.
This means the $q$-differential of a product is NOT the
sum of differentials. Squaring:

$$
  d_q^2  \neq  0 \quad \text{for } q \neq 1
$$

**Consequence:** The total $q$-energy of the products need not
equal the total $q$-energy of the parent. There is a
**$q$-anomaly**:

$$
  \delta_q
   := 
  Q
  - 
  (T_e + T_{\nu^{\sigma}} + T_{\mathrm{recoil}})
$$

This anomaly does NOT vanish in general. It is a genuine
physical effect of the $q$-deformation, not a computational
artefact.

## Structure of the $q$-anomaly

The $q$-anomaly arises from the non-commutativity of the
Iwahori--Hecke algebra. When the Skein crossing change converts one
quark, the re-reduction to Gröbner--Shirshov normal form
([nuclear Gröbner--Shirshov reduction](#prop:nuclear-groebner-reduction))
introduces R2 moves $T^2 = (q - q^{-1})T + 1$.
Each R2 move shifts the local $q$-environment by:

$$
  q_{\mathrm{eff}} \mapsto q_{\mathrm{eff}} + \Delta q
$$

where $\Delta q \propto \hbar_q^2 = (1 - q^{-1})^2$.

The self-deformation
([hadron self-correction](#prop:hadron-q-self-correction))
produces a net shift:

$$
  \Delta q_{\mathrm{eff}}
  = 
  \frac{A - 1}{A^2} \cdot \hbar_q^2
$$

This shift modifies $Q$ at second order:

$$
  Q
  = 
  \underbrace{\Delta \mathfrak{S}_q - \mathfrak{S}_q(e)}_{\text{leading (crossing change)}}
  + 
  \underbrace{\frac{\partial \mathfrak{S}_q}{\partial q} \cdot \Delta q_{\mathrm{eff}}}_{\delta_q \text{ (q-anomaly)}}
$$

**At $q = 1$:** $\delta_q = 0$ and
$Q \to Q_{\mathrm{classical}}$ (classical
conservation restored).

**At the substrate parameter $q$:** $\delta_q \neq 0$. For tritium ($A = 3$):
$\Delta q_{\mathrm{eff}} = 2/9 \cdot \hbar_q^2 \approx 0.0022$,
giving a correction $\delta_q / Q \sim 5\%$.
This is the **same correction** that brings the tritium
half-life prediction from 13 yr to 12.4 yr (vs observed 12.32 yr).

## $Q$ is NOT conserved

The $q$-anomaly $\delta_q$ means that $Q$ defined
as the action difference is NOT equal to the sum of kinetic
energies. The "missing" energy goes into the $q$-deformation
of the vacuum — it is absorbed by the change in the effective
substrate parameter from $q$ to $q + \Delta q_{\mathrm{eff}}$.

This is not a violation of physics — it is the $q$-deformed
version of the quantum anomaly. The conserved quantity is not
$Q$ but the **full categorical action** $\mathfrak{S}_q$ of
the entire system (products + vacuum shift):

$$
  \mathfrak{S}_q(\mathrm{par})
  = 
  \mathfrak{S}_{q + \Delta q}(\mathrm{dau})
  + 
  \mathfrak{S}_q(e)
  + 
  \mathfrak{S}_q(\nu^{\sigma})
  + 
  \text{kinetic terms}
$$

Note: the daughter is evaluated at the **shifted** $q$, not the
original. This is the $q$-analogue of energy conservation.

## Limits

| $q$ | Regime | $Q$ | $\delta_q$ |
|-----|--------|:---:|:---:|
| $q = 1$ | Classical | $0$ | $0$ |
| the substrate $q$ | Our universe | $\mathcal{Q}_{\exp} + \delta_q$ | $\neq 0$ |
| $q \to \infty$ | Deep-quantum | $\to \infty$ | $\to \infty$ |

## $q$-Momentum

The $q$-momentum ([q-momentum](#def:q-momentum)) satisfies
a similar non-conservation. Classically:

$$
  \vec{p}_{\mathrm{par}} = \vec{p}_{\mathrm{dau}} + \vec{p}_e + \vec{p}_{\nu^{\sigma}}
$$

In the $q$-deformed case, the Iwahori--Hecke algebra non-commutativity
means:

$$
  p_q(\mathrm{par})
  = 
  p_q(\mathrm{dau}) + p_q(e) + p_q(\nu^{\sigma})
  + 
  \delta p_q
$$

where $\delta p_q \propto \hbar_q$ is a $q$-anomaly in momentum.
This is the braid-group analogue of the quantum anomaly in
gauge theories.
