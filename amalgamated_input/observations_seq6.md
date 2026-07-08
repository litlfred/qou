<!-- FILE_START: mass-predictions-derivations-intro.md -->
This sub-section details specific mass derivations. We cover nucleon Borromean topology and the pair-skein mass formula. We analyze the flavor-split substrate and dressed-quark numerology at $q_0$. We derive the deuteron binding energy. The terminal-resolution closure anchors the categorical chain to the Archimedean evaluation. Finally, we examine the $W$-boson mass discrepancy, which forms a key open audit target.
<!-- FILE_END: mass-predictions-derivations-intro.md -->

<!-- FILE_START: nucleon-borromean-topology.md -->
*The proton and neutron are Borromean configurations ($6_2^3$) of three quark vortices. They are internally bound by Hopf links $\mathcal{L}_{\mathrm{Hopf}}$. Since $\mathrm{Vol}(\mathcal{L}_{\mathrm{Hopf}}) = 0$, the mass contribution arises entirely from the Skein functional.*
<!-- FILE_END: nucleon-borromean-topology.md -->

<!-- FILE_START: pair-skein-mass-formula.md -->
The Borromean braid of a nucleon with quarks $(q_1, q_2, q_3)$ contributes a pair Skein mass at each color-exchange crossing:

$$
  \mathcal{S}_{ab}(q)
  =
  \frac{q\mu_a +  q^{-1}\mu_b}
       {q^{1/2} + q^{-1/2}}.
$$

The total nucleon mass is:

$$
  m_N
  =
  \mathcal{S}_{q_1 q_2}(q)
  + \mathcal{S}_{q_1 q_3}(q)
  + \mathcal{S}_{q_2 q_3}(q).
$$
<!-- FILE_END: pair-skein-mass-formula.md -->

<!-- FILE_START: flavor-split-substrate.md -->
*The proton–neutron mass splitting requires no calibration to the $u$--$d$ mass difference:*

$$
  \frac{m_n - m_p}{M_N}
  \;\approx\;
  \frac{(q - 1)^2 \, (1 - q^{-4})}{3},
$$

*where $M_N = (m_p + m_n)/2$. Equivalently:*

$$
  \frac{m_n - m_p}{\mu_{\text{avg}}}
  \;\approx\;
  \hbar_q^2 \cdot h_q \cdot [2]_q,
$$

*At $q = q_0 \approx 1.10998$, this matches the CODATA value to within $-0.10\%$.*

This form depends only on $q_0$ and $M_N$. A companion proposition ([`prop:flavor-dressed-mass-from-substrate-split`](../braids-and-knots/flavor-dressed-mass-from-substrate-split.md)) recovers the dressed-mass difference $\mu_{\mathfrak{d}} - \mu_{\mathfrak{u}} \approx 1.288\,\text{MeV}$ as a derived consequence.

The factored form admits a categorical reading:

| Factor               | Categorical meaning                                                                   |
| -------------------- | ------------------------------------------------------------------------------------- |
| $\hbar_q^2$          | Two quanta of substrate Planck action                                                 |
| $h_q$                | One Hecke crossing                                                                   |
| $[2]_q$              | Doublet quantum integer                                                              |

The flavor swap $\mathfrak{u} \leftrightarrow \mathfrak{d}$ acts via the Hecke generator $\sigma$.

**Canonical evaluation.**

| Quantity                       | Substrate formula                 | Substrate value        | CODATA target          | Residual  |
| ------------------------------ | --------------------------------- | ---------------------- | ---------------------- | --------- |
| $(m_n - m_p)/M_N$              | $(q-1)^2 (1 - q^{-4}) / 3$        | $1.376 \times 10^{-3}$ | $1.377 \times 10^{-3}$ | $-0.10\%$ |
| $(m_n - m_p)/\mu_{\text{avg}}$ | $\hbar_q^2 \cdot h_q \cdot [2]_q$ | $4.127 \times 10^{-3}$ | $4.148 \times 10^{-3}$ | $-0.49\%$ |
| $m_n - m_p$                    | $M_N \cdot (q-1)^2(1-q^{-4})/3$   | $1.287\,\text{MeV}$    | $1.293\,\text{MeV}$    | $-0.52\%$ |
<!-- FILE_END: flavor-split-substrate.md -->

<!-- FILE_START: flavor-split-substrate-interpretation.md -->
**Remark (Bring-surface origin).**

The closed form emerges from per-sheet Picard–Lefschetz integration on the Bring color-tube cubic. The $1/3$ factor reflects the permutation average over three flavor placements.

**Remark (limitation).**

The $-0.10\%$ residual exceeds the formal precision of $q_0$. The substrate ansatz is approximate at the subleading order.
<!-- FILE_END: flavor-split-substrate-interpretation.md -->

<!-- FILE_START: dressed-quark-numerology-at-q0.md -->
**Remark (dressed-quark numerology at $q_0$).**

At $q_0 \approx 1.10998$, combining [`prop:flavor-dressed-mass-from-substrate-split`](../braids-and-knots/flavor-dressed-mass-from-substrate-split.md) with $\bar\mu \approx M_N / 3$ yields:

$$
  \mu_{\mathfrak{u}} \;\approx\; 311.10\,\text{MeV},
  \qquad
  \mu_{\mathfrak{d}} \;\approx\; 312.39\,\text{MeV},
  \qquad
  \mu_{\mathfrak{d}} - \mu_{\mathfrak{u}} \;\approx\; 1.286\,\text{MeV}.
$$

These values are now derived from $M_N$ and $q_0$. The CODATA value $m_n - m_p \approx 1.293\,\text{MeV}$ is a prediction at $-0.53\%$ residual.

## Origin of $\bar\mu \approx M_N / 3$ and the Skein cross-term shift

The sum of nucleon masses contains three copies of the average quark dressing:

$$
  m_p + m_n
  \;=\;
  3(\mu_{\mathfrak{u}} + \mu_{\mathfrak{d}})
  \;+\;
  \text{(Skein cross-terms)}.
$$

Ignoring cross-terms yields a naive estimate $\bar\mu^{\mathrm{naive}} \approx 312.97\,\text{MeV}$. Borromean Skein cross-terms shift this down by $\delta \approx 1.23\,\text{MeV}$ per quark:

$$
  \bar\mu^{\mathrm{Skein-corrected}}
  \;\approx\;
  311.75\,\text{MeV}.
$$

## Distance from the substrate bound

[`thm:flavor-mass-splitting-bound`](../braids-and-knots/flavor-mass-splitting-bound.md) gives an upper bound of $\approx 3.88\,\text{MeV}$. The realised value $1.286\,\text{MeV}$ is about $33\%$ of the bound. 

## Heavier flavors

The substrate flavor-split derivation is specific to the nucleon doublet topology. Extensions to heavier flavors remain unconstrained.
<!-- FILE_END: dressed-quark-numerology-at-q0.md -->

<!-- FILE_START: m-tau-knot-prediction.md -->
The CAL-2 critique ([`rem:epistemic-status-of-calibrations`](#rem:epistemic-status-of-calibrations)) identifies a structural pattern in the muon-mass identity. Does $m_\tau/m_e$ admit an analogous reading $m_\tau/m_e = \mathrm{Vol}(K_\tau)/\hbar_q^{k_\tau}$?

**Refuted.** A direct search evaluated 25 hyperbolic knots. No candidate matches within $1\%$ of the CODATA value $3477.23$. We retain this as a falsifiable observation without proposing a new calibration.
<!-- FILE_END: m-tau-knot-prediction.md -->

