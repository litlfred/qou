These notes accompany [Three-calibration discipline ($m_e$, $m_\mu$, $m_\pi$) aligned to (co)homological data](#def:three-calibration-discipline): the cohomological alignment of the three inputs, how their proxies are read off, and what the discipline rules out.

## Cohomological alignment

It is conjectured that these three degrees of freedom belong to the single first cohomology $H^1(\text{Bring}) = 2W$, not to three distinct degrees $H^0/H^1/H^2$. On that reading the Hodge structure of shape $2W$ has $2+1=3$ real degrees of freedom (the rank-2 $W$-plane's scale and modulus, plus one orthogonal class), matching the three calibrations ([The three calibrations are the three cohomological data of H¹(Bring)](#conj:calibration-cohomology-alignment)).

The three canonical inputs are weak-sector observables: a leptonic mass scale and two bar-parity channels $(m_e, P_{\mathrm{skew}}^{\beta}, P_{\mathrm{avg}}^{\pi})$. They enter at successive orders $h^0, h^2, h^3$. We read them off their most precise proxies: the masses $m_e, m_\pi$ and the $Q$-value $\mathfrak{Q}_\beta = P_{\mathrm{skew}}^{\beta}$. The electron mass $m_e$ sets the unit. Since $q_0$ is dimensionless, we pin it relative to that unit using the ratio $m_\mu/m_e$ through the figure-eight identity $m_\mu/m_e = \mathrm{Vol}(4_1)/\hbar_q^2$ with $\hbar_q = 1 - q_0^{-1}$. Inverted for $q_0 \approx 1.10998$, this provides the most precise anchor for CAL-2 ($P_{\mathrm{skew}}^{\beta}$). The pion mass $m_\pi$ is the proxy for the orthogonal meson scale ($P_{\mathrm{avg}}^{\pi}$). The value $\mathfrak{Q}_\beta$ is the measured proxy for CAL-2, not a fourth input.

## Discussion

This proposition formalizes the calibration discipline.

1. **Three calibration inputs.** The QOU framework reads three experimental values ($m_e$, the lepton ratio $m_\mu/m_e$, and $m_\pi$). It assigns them to three distinct (co)homological data of the substrate. Every other physical prediction is the product of these three with a $\mathbb{Q}(q_0)$-valued algebraic expression.
2. **(Co)homological alignment.** The three calibrations correspond exactly to the three real degrees of freedom of the Bring Hodge structure $H^1 = 2W$ ([calibration-cohomology-alignment](../mass-theory/calibration-cohomology-alignment.md)). The rank-2 $W$-Hodge plane carries a scale (pinned by $m_e$) and a modulus (pinned by $q_0$ via $m_\mu/m_e$). The meson sector contributes a third, orthogonal scale (pinned by $m_\pi$).
3. **Overdetermination.** The canonical $H^1$ modulus is pinned by the lepton ratio $m_\mu/m_e$ through the figure-eight volume identity

   $$
     \frac{m_\mu}{m_e} \;=\; \frac{\mathrm{Vol}(4_1)}{\hbar_q^2},
     \qquad \hbar_q = 1 - q_0^{-1},
     \qquad \mathrm{Vol}(4_1) = 2\,\mathrm{Cl}_2(\pi/3) = 6\,\Lambda(\pi/3) \approx 2.0299.
   $$

   Inverted for $q_0$, CAL-1 and CAL-2 coordinatize the single modulus $q_0$ one-to-one. The modulus is overdetermined. It can be fixed by $\alpha_{\mathrm{EM}}^{-1}$ or by tritium $t_{1/2}$, which agree on $q_0$ to within 0.3% ([substrate-consistency window](#prop:substrate-consistency-window)). In the observations chapter, one may anchor $q_0$ on the proton ratio $m_p/m_e$ for higher precision. This is a substitution within the same overdetermined $H^1$ datum. It does not introduce a new calibration.
4. **Consequence.** Any predicted mass, binding energy, or Q-value not of the form $m_e^a m_\pi^c \cdot \text{rational}(q_0)$ violates this discipline. It must either introduce a fourth calibration or report a $\tau$-image quantity from the Archimedean side.

## What the discipline rules out

Every derivation in the paper is checked against this proposition, and every proof block against the $\mathbb{Q}(q_0)$-rationality clause, which forbids Archimedean-side derivation inputs on the algebraic side.

A fourth dimensional input is a hard failure. The three calibrations are categorical. They sit in distinct cohomological degrees and cannot be replaced without violating the (co)homological alignment.
