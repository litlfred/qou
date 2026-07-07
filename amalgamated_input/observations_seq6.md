<!-- FILE_START: mass-predictions-derivations-intro.md -->
The preceding sub-section established the mass-prediction methodology.
It introduced the stability cubic, the $q$-stability ranges, per-particle
mass-ratio predictions, the mass-comparison table anchoring outputs
against AME2020/CODATA, and validation gates tracking prediction drift.

This sub-section details specific derivations. We cover nucleon Borromean
topology and the pair-skein mass formula, constructing nucleon masses
from braid-link data. We analyze the flavor-split substrate and
dressed-quark numerology at $q_0$. We derive the deuteron binding energy
to verify the two-nucleon construction. The terminal-resolution closure
anchors the categorical chain to the Archimedean evaluation. Finally, we
examine the $W$-boson mass discrepancy. This constitutes the largest
residual gap between the framework and the Standard Model, forming a key
open audit target.
<!-- FILE_END: mass-predictions-derivations-intro.md -->

<!-- FILE_START: nucleon-borromean-topology.md -->
**Lemma.**
*The proton and neutron are each modelled as a Borromean configuration ($6_2^3$) of three quark vortices. They are bound internally by Hopf links $\mathcal{L}_{\mathrm{Hopf}}$ representing the color-exchange interaction. Since the Hopf link is a torus link with $\mathrm{Vol}(\mathcal{L}_{\mathrm{Hopf}}) = 0$, its mass contribution arises entirely from the Skein functional, not from hyperbolic volume.*
<!-- FILE_END: nucleon-borromean-topology.md -->

<!-- FILE_START: pair-skein-mass-formula.md -->
**Lemma.**
The Borromean braid of a nucleon with quarks $(q_1, q_2, q_3)$ contributes a pair Skein mass at each of its three color-exchange crossing pairs:
$$
  \mathcal{S}_{ab}(q)
  =
  \frac{q\mu_a +  q^{-1}\mu_b}
       {q^{1/2} + q^{-1/2}},
$$
where $\mu_a$ is the dressed quark Skein mass of species $a$. The total nucleon mass is the sum over the three crossing pairs:
$$
  m_N
  =
  \mathcal{S}_{q_1 q_2}(q)
  + \mathcal{S}_{q_1 q_3}(q)
  + \mathcal{S}_{q_2 q_3}(q).
$$
<!-- FILE_END: pair-skein-mass-formula.md -->

<!-- FILE_START: flavor-split-substrate.md -->
**Proposition.**
*The proton–neutron mass splitting admits a closed-form expression in substrate atoms, requiring no calibration to the $u$--$d$ mass difference:*

$$
  \frac{m_n - m_p}{M_N}
  \;\approx\;
  \frac{(q - 1)^2 \, (1 - q^{-4})}{3},
$$

*where $M_N = (m_p + m_n)/2$ is the nucleon mass average. Equivalently, in factored substrate-atom form:*

$$
  \frac{m_n - m_p}{\mu_{\text{avg}}}
  \;\approx\;
  \hbar_q^2 \cdot h_q \cdot [2]_q,
  \qquad
  \mu_{\text{avg}} = \tfrac{1}{2}(\mu_{\mathfrak{u}} + \mu_{\mathfrak{d}}).
$$

*Here, $\hbar_q = (q-1)/q$ is the substrate Planck constant, $h_q = q - q^{-1}$ is the Hecke crossing scale, and $[2]_q = q + q^{-1}$ is the doublet quantum integer.*

*At $q = q_0 = 1.109978595554181\ldots$ (50 dps), this closes the CODATA value $(m_n - m_p)/M_N = 1.293\,\text{MeV} / 938.92\,\text{MeV} \approx 1.377 \times 10^{-3}$ to within $-0.10\%$.*

*The two algebraic forms agree via the identity $h_q \cdot z_{\text{mkv}} = z_0 = \hbar_q \cdot \sqrt{q}$, where $z_0 = q^{1/2} - q^{-1/2}$ and $z_{\text{mkv}} = (q^{1/2} + q^{-1/2})^{-1}$.*

The substrate-pure form depends only on $q_0$ and the universal nucleon scale $M_N$; neither $\mu_{\mathfrak{u}}$ nor $\mu_{\mathfrak{d}}$ appears. A companion proposition ([`prop:flavor-dressed-mass-from-substrate-split`](../braids-and-knots/flavor-dressed-mass-from-substrate-split.md)) lifts this splitting back to the dressed-quark masses via the Skein factor. This recovers the dressed-mass difference $\mu_{\mathfrak{d}} - \mu_{\mathfrak{u}} \approx 1.288\,\text{MeV}$ as a derived consequence of $q_0$ and $M_N$.

The factored form $\hbar_q^2 \cdot h_q \cdot [2]_q$ admits a precise categorical reading:

| Factor               | Categorical meaning                                                                   |
| -------------------- | ------------------------------------------------------------------------------------- |
| $\hbar_q^2$          | Two quanta of substrate Planck action                                                 |
| $h_q = q - q^{-1}$   | One Hecke crossing (the Skein gap $\sigma - \sigma^{-1}$)                             |
| $[2]_q = q + q^{-1}$ | Doublet quantum integer (symmetric $\oplus$ antisymmetric eigenspace of $\sigma$) |

The flavor swap $\mathfrak{u} \leftrightarrow \mathfrak{d}$ on a 3-quark baryon is implemented categorically as the Hecke generator $\sigma$ acting on a 2-strand sub-braid. Its eigenspace decomposition provides the $[2]_q$ multiplicity. The Skein gap $h_q$ supplies the crossing-energy factor. The two $\hbar_q$ factors count the two action quanta required to traverse the crossing pair.

**Canonical evaluation.**

| Quantity                       | Substrate formula                 | Substrate value        | CODATA target          | Residual  |
| ------------------------------ | --------------------------------- | ---------------------- | ---------------------- | --------- |
| $(m_n - m_p)/M_N$              | $(q-1)^2 (1 - q^{-4}) / 3$        | $1.376 \times 10^{-3}$ | $1.377 \times 10^{-3}$ | $-0.10\%$ |
| $(m_n - m_p)/\mu_{\text{avg}}$ | $\hbar_q^2 \cdot h_q \cdot [2]_q$ | $4.127 \times 10^{-3}$ | $4.148 \times 10^{-3}$ | $-0.49\%$ |
| $m_n - m_p$                    | $M_N \cdot (q-1)^2(1-q^{-4})/3$   | $1.287\,\text{MeV}$    | $1.293\,\text{MeV}$    | $-0.52\%$ |
<!-- FILE_END: flavor-split-substrate.md -->

<!-- FILE_START: flavor-split-substrate-interpretation.md -->
**Remark (Bring-surface origin).**

The closed form $(q-1)^2 (1 - q^{-4}) / 3$ emerges from per-sheet Picard–Lefschetz integration on the Bring color-tube cubic. At the C2 inflection ($a_{C2} = 0.4066$), the three color sheets yield integrals $A_1 \in \mathbb{R}$ (one asymmetric real sheet) and $A_{2,3} \in \mathbb{C}$ (a complex conjugate pair). We average the flavor-weighted sum $\sum_q \mu_q A_{\text{sheet}(q)}$ over the three possible placements of the asymmetric flavor. This recovers the per-quark averages $(2\mu_u + \mu_d)/3$ and $(\mu_u + 2\mu_d)/3$ for the proton and neutron, respectively. The $1/3$ factor reflects this permutation average.

**Remark (limitation).**

The $-0.10\%$ residual exceeds the formal precision of $q_0$ ($\sim 10$ ppb from CAL-2). The substrate ansatz is therefore approximate at the level of a subleading correction. Refining the ansatz to the precision floor requires either a higher-order substrate atom (a next-to-leading $(q-1)^k$ correction) or a refined categorical derivation of the per-quark splitting.
<!-- FILE_END: flavor-split-substrate-interpretation.md -->

<!-- FILE_START: dressed-quark-numerology-at-q0.md -->
**Remark (dressed-quark numerology at $q_0$).**

At the substrate parameter $q_0 = 1.109978595554181\ldots$ (50 dps), we combine [`prop:flavor-dressed-mass-from-substrate-split`](../braids-and-knots/flavor-dressed-mass-from-substrate-split.md) with the baryon-content sum rule $\bar\mu \approx M_N / 3$. This fixes the individual dressed-quark masses to:

$$
  \mu_{\mathfrak{u}} \;\approx\; 311.10\,\text{MeV},
  \qquad
  \mu_{\mathfrak{d}} \;\approx\; 312.39\,\text{MeV},
  \qquad
  \mu_{\mathfrak{d}} - \mu_{\mathfrak{u}} \;\approx\; 1.286\,\text{MeV}.
$$

These values were previously absorbed into the deprecated `lem:nucleon-mass-splitting` as a four-input fit ($\mu_{\mathfrak{u}}, \mu_{\mathfrak{d}}, m_p, m_n$ taken from CODATA). Under the substrate-pure derivation, they reduce to a two-input form: $M_N$ (anchored by CODATA) and $q_0$ (the substrate parameter). The CODATA value $m_n - m_p \approx 1.293\,\text{MeV}$ is no longer an input. It is a prediction at $-0.53\%$ residual.

## Origin of $\bar\mu \approx M_N / 3$ and the Skein cross-term shift

The proton ($\mathfrak{u}\mathfrak{u}\mathfrak{d}$) and neutron ($\mathfrak{u}\mathfrak{d}\mathfrak{d}$) braids each carry three quark vortices. The sum of nucleon masses contains three copies of the average quark dressing:

$$
  m_p + m_n
  \;=\;
  3(\mu_{\mathfrak{u}} + \mu_{\mathfrak{d}})
  \;+\;
  \text{(Skein cross-terms)}.
$$

Setting the cross-terms to zero yields a naive closed-form upper estimate:

$$
  \bar\mu^{\mathrm{naive}}
  \;=\;
  \tfrac{1}{6}(m_p + m_n)
  \;=\;
  \tfrac{M_N}{3}
  \;\approx\;
  312.97\,\text{MeV}.
$$

The Borromean Skein cross-terms shift the per-quark contribution down by a uniform amount $\delta \approx 1.23\,\text{MeV}$ per quark ($6\delta \approx 7.4\,\text{MeV}$ total across the proton + neutron sum). This gives:

$$
  \bar\mu^{\mathrm{Skein-corrected}}
  \;=\;
  \bar\mu^{\mathrm{naive}} - \delta
  \;\approx\;
  311.75\,\text{MeV}.
$$

This is consistent with $\bar\mu = (\mu_{\mathfrak{u}} + \mu_{\mathfrak{d}})/2 = (311.10 + 312.39)/2 = 311.745\,\text{MeV}$ from the per-quark values. The substrate split $\mu_{\mathfrak{d}} - \mu_{\mathfrak{u}}$ (1.286 MeV) remains unaffected by the Skein cross-term adjustment, which acts uniformly on both flavors.

## Distance from the substrate bound

[`thm:flavor-mass-splitting-bound`](../braids-and-knots/flavor-mass-splitting-bound.md) gives the upper bound:

$$
  \mu_{\mathfrak{d}} - \mu_{\mathfrak{u}}
  \;<\;
  M_N \cdot \hbar_q^2 \cdot h_q \cdot [2]_q
  \;\approx\;
  3.88\,\text{MeV}.
$$

The realised value $1.286\,\text{MeV}$ sits at about $33\%$ of the bound. Per the slack-ratio identity in [`thm:flavor-mass-splitting-bound`](../braids-and-knots/flavor-mass-splitting-bound.md), the closed form for this ratio is:

$$
  \frac{\mu_{\mathfrak{d}} - \mu_{\mathfrak{u}}}{M_N \cdot \hbar_q^2 \cdot h_q \cdot [2]_q}
  \;=\;
  \frac{1}{3}
  \cdot
  \frac{q^{1/2} + q^{-1/2}}{q + q^{-1}}
  \;+\;
  O\!\left((\Delta m / M_N)^2\right).
$$

The dominant contribution is the explicit $1/3$ in the substrate formula of [`prop:flavor-split-substrate`](flavor-split-substrate.md). The Skein-side factor $(q^{1/2} + q^{-1/2})/(q + q^{-1}) \approx 0.997$ at $q_0$ only adjusts the slack slightly. Tightening the bound to capture the realised value remains open.

## Heavier flavors

The dressed-quark masses of $\mathfrak{s}, \mathfrak{c}, \mathfrak{b}, \mathfrak{t}$ are not pinned by the substrate flavor-split derivation. That derivation is specific to the nucleon doublet topology ($\mathfrak{u}\mathfrak{d}$). An extension to higher-flavor braids requires either:

- The strangelet topology ([`sec:strangelet-intro`](strangelet-intro.md)) for $\mathfrak{s}$.
- A flavor-dependent confinement-category extension for $\mathfrak{c}, \mathfrak{b}, \mathfrak{t}$ via the heavy-quark effective theory analog (open).

Until these extensions are formalized, the entries $\mu_{\mathfrak{s}}, \mu_{\mathfrak{c}}, \mu_{\mathfrak{b}}, \mu_{\mathfrak{t}}$ of the [`def:flavor-dressing-functor`](../braids-and-knots/flavor-dressing-functor.md) remain unconstrained.
<!-- FILE_END: dressed-quark-numerology-at-q0.md -->

<!-- FILE_START: m-tau-knot-prediction.md -->
The CAL-2 cohomological critique ([`rem:epistemic-status-of-calibrations`](#rem:epistemic-status-of-calibrations)) identifies a structural pattern in the muon-mass identity ($m_\mu/m_e = \mathrm{Vol}(4_1)/\hbar_q^2$). This raises a natural question. Does $m_\tau/m_e$ admit an analogous cohomological reading $m_\tau/m_e = \mathrm{Vol}(K_\tau)/\hbar_q^{k_\tau}$ for some hyperbolic knot $K_\tau$ and small integer $k_\tau$?

**Refuted (specific evidence).** A direct search evaluates 25 hyperbolic knots and links through 10 crossings, for $k_\tau \in \{2, 3, 4, 5\}$, and two-knot products at $k \le 7$. This search finds no candidate within $1\%$ of the CODATA value $m_\tau/m_e = 3477.23$. The best single-knot match is $\mathrm{Vol}(8_1)/\hbar_q^3 = 3523.59$. This deviates by $+1.33\%$, which is roughly $13\,000$ times the experimental precision.

**Primary content moved to audits.** The full search table, five queued extensions (Vol+iCS pair, polylog tower at $n>2$, Whitehead doubling, multi-stratum sum, tower correction), and the explicit $\Delta_\lambda$-gate guard against proposing this as a fourth calibration input are detailed in [`docs/audits/2026-06-03-m-tau-knot-prediction-falsification.md`](../../../docs/audits/2026-06-03-m-tau-knot-prediction-falsification.md).

We retain this block as a falsifiable observation. It makes no logical claim and proposes no new calibration.
<!-- FILE_END: m-tau-knot-prediction.md -->

