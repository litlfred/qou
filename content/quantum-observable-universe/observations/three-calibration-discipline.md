**Proposition (Three-calibration discipline).**
*The QOU framework admits categorically exactly three external calibration inputs. These are the three real degrees of freedom of the first cohomology of Bring's curve, $H^1 = 2W$:*

| DOF of $H^1(\text{Bring}) = 2W$ | Canonical observable | What it fixes | Numerical proxy (source) |
| ------------------------------- | -------------- | ------------- | ------ |
| $W$-plane **scale** ($h^0$)     | $m_e$ (leptonic mass scale) | the dimensional unit (scale) | $m_e$, CODATA (electron mass) |
| $W$-plane **modulus** ($h^2$)   | $\mathfrak{D}_\beta$ (neutron $\beta$-decay width) | $q_0$ via $m_\mu/m_e = \mathrm{Vol}(4_1)/\hbar_q^2$ | $\mathfrak{Q}_\beta = \hbar/\mathfrak{D}_\beta$; modulus pinned most precisely by $m_\mu/m_e$ (CODATA muon mass) |
| **orthogonal class** (meson sector, $h^3$) | $\mathfrak{D}_\pi$ (pion decay width) | the $\mathrm{Vol}(\mathrm{Hopf})=0$ meson scale (independent of $m_e, q_0$) | $m_\pi$, PDG (charged-pion mass) |

These three degrees of freedom belong to the single first cohomology $H^1(\text{Bring}) = 2W$. They are not three distinct degrees $H^0/H^1/H^2$. The Hodge structure of shape $2W$ has $2+1=3$ real DOF (the rank-2 $W$-plane's scale and modulus, plus one orthogonal class). This matches the three calibrations ([calibration-cohomology-alignment](../mass-theory/calibration-cohomology-alignment.md), Lean witness `QOU.Mass.calibrations_eq_cohomology`).

The three canonical inputs are weak-sector observables: a leptonic mass scale and two decay widths $(m_e, \mathfrak{D}_\beta, \mathfrak{D}_\pi)$. They enter at successive orders $h^0, h^2, h^3$. We read them off their most precise proxies: the masses $m_e, m_\pi$ and the $Q$-value $\mathfrak{Q}_\beta = \hbar/\mathfrak{D}_\beta$. The electron mass $m_e$ sets the unit. Since $q_0$ is dimensionless, we pin it relative to that unit using the ratio $m_\mu/m_e$ through the figure-eight identity $m_\mu/m_e = \mathrm{Vol}(4_1)/\hbar_q^2$ with $\hbar_q = 1 - q_0^{-1}$. Inverted for $q_0 \approx 1.10998$, this provides the most precise anchor for CAL-2 ($\mathfrak{D}_\beta$). The pion mass $m_\pi$ is the proxy for the orthogonal meson scale ($\mathfrak{D}_\pi$). The value $\mathfrak{Q}_\beta$ is the measured proxy for CAL-2, not a fourth input.

*For every confined hadronic state $X$, the mass functional defined by the algebraic-side chain ([categorical action](#def:categorical-action), [Frobenius pairing](#def:frobenius-pairing), [mass identity](#def:mass-identity), [mass-endomorphism tower](#prop:mass-endomorphism-tower), [Jones–Markov trace](#thm:jones-markov-trace)) factors as*

$$
  \mathfrak{m}(X) \;=\;
  m_e^{\,a(X)}\;m_\pi^{\,c(X)}\;Q_X(q_0),
  \qquad
  Q_X(q) \in \mathbb{Q}(q),
$$

*with non-negative integer exponents $a(X), c(X)$ determined by the (co)homological grading of the observable $X$. Concretely: $a$ counts mass-scale insertions ($H^0$ — the $W$-plane scale), $c$ counts meson-sector insertions (the orthogonal $m_\pi$ class; $c = 0$ in the baryon sector), and $q_0$ is fixed by the lepton ratio $m_\mu/m_e$ (the $H^1$ $W$-plane modulus, CAL-2 = $\mathfrak{D}_\beta$). The parameter $\mathfrak{Q}_\beta$ is the CAL-2 proxy. It is the bar-odd ($\sinh$) partner of the bar-even ($\cosh$) meson scale $m_\pi$ under the bar-involution $q \mapsto q^{-1}$ ([substrate cohomology calibration story](../mass-theory/substrate-cohomology-calibration-story.md)). It represents the experimental face of the modulus CAL-2 pins. It is not a separate dimensional mass-formula factor.*

## Discussion

This proposition formalizes the calibration discipline.

1. **Three calibration inputs.** The QOU framework reads three experimental values ($m_e$, the lepton ratio $m_\mu/m_e$, and $m_\pi$). It assigns them to three distinct (co)homological data of the substrate. Every other physical prediction is the product of these three with a $\mathbb{Q}(q_0)$-valued algebraic expression.
2. **(Co)homological alignment.** The three calibrations correspond exactly to the three real degrees of freedom of the Bring Hodge structure $H^1 = 2W$ ([calibration-cohomology-alignment](../mass-theory/calibration-cohomology-alignment.md)). The rank-2 $W$-Hodge plane carries a scale (pinned by $m_e$) and a modulus (pinned by $q_0$ via $m_\mu/m_e$). The meson sector contributes a third, orthogonal scale (pinned by $m_\pi$).
3. **Overdetermination.** The canonical $H^1$ modulus is pinned by the lepton ratio $m_\mu/m_e$ through the figure-eight volume identity

   $$
     \frac{m_\mu}{m_e} \;=\; \frac{\mathrm{Vol}(4_1)}{\hbar_q^2},
     \qquad \hbar_q = 1 - q_0^{-1},
     \qquad \mathrm{Vol}(4_1) = 2\Lambda(\pi/3) \approx 2.0299.
   $$

   Inverted for $q_0$, CAL-1 and CAL-2 coordinatize the single modulus $q_0$ one-to-one. The modulus is overdetermined. It can be fixed by $\alpha_{\mathrm{EM}}^{-1}$ or by tritium $t_{1/2}$, which agree on $q_0$ to within 0.3% ([substrate-consistency window](#prop:substrate-consistency-window)). In the Physical-Observations chapter, one may anchor $q_0$ on the proton ratio $m_p/m_e$ for higher precision. This is a substitution within the same overdetermined $H^1$ datum. It does not introduce a new calibration.
4. **Audit consequence.** Any predicted mass, binding energy, or Q-value not of the form $m_e^a m_\pi^c \cdot \text{rational}(q_0)$ violates this discipline. It must either introduce a fourth calibration or report a $\tau$-image quantity from the Archimedean side.

## Audit hook

This proposition serves as the calibration-discipline hook for audits. Task P1.5 in the [math-framework workplan](../../../docs/audits/-math-framework-workplan.md) sweeps the paper for discipline violations. Task P0.1 sweeps proof blocks for Archimedean-side derivation inputs. The $\mathbb{Q}(q_0)$-rationality clause forbids such inputs in algebraic-side derivations.

A fourth dimensional input constitutes a hard audit failure. The three calibrations are categorical. They sit in distinct cohomological degrees and cannot be replaced without violating the (co)homological alignment.
