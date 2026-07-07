<!-- FILE_START: observations-intro.md -->
This chapter collects the physical predictions of the Descartes universe and compares them with experimental data. We assume the knot-to-particle mapping and Skein decomposition ([Chapter 9](#chap:brings-surface)), along with the Gröbner--Shirshov reduction engine and Wedderburn mass formula ([Chapter 10](#chap:particle-interactions)). This chapter is observational. We calibrate the substrate parameter $q_0$ from those constructions. The molecular extension ([Chapter 12](#chap:molecular-construction)) builds on this calibrated $q_0$.

The central result is the substrate consistency window. Multiple independent physical observables (lepton mass ratios, the fine structure constant, proton-to-electron mass ratio, and nuclear binding energies) each determine the substrate parameter $q$. These determinations agree within a narrow interval $q_0 \approx 1.110$. We present particle identification conjectures, CODATA comparisons for fundamental masses, beta decay predictions, and nuclear stability patterns. We also propose experimental tests including crystal resonance, proton radius, and Breit--Wheeler pair creation.

Every numerical prediction uses $\approx$ (not $=$) to indicate that values are derived approximations at $q_0$, not exact identities. We tabulate error terms and percentage deviations from experimental data.

**Notation note.** We use plain italic $m_e$, $m_p$, $m_n$ for the CODATA-measured electron, proton, and neutron masses. We treat these as experimental input. They are distinct from the categorical mass $\mathfrak{m}$, which denotes the QOU-derived mass via the topological mass formula $\mathfrak{m}(K) = \mathrm{Vol}(K)/\hbar_q^{2}$. The role of $m_e$ is an external scaling ruler. It fixes the absolute energy scale. All other masses are predicted as ratios $\mathfrak{m}(K)/\mathfrak{m}(4_1) \cdot m_e$. When a comparison table juxtaposes "QOU prediction" against "CODATA value", both are in MeV. The ratio is dimensionless and substrate-derived.
<!-- FILE_END: observations-intro.md -->

<!-- FILE_START: substrate-consistency-window.md -->
The QOU framework relies on a single free parameter: the substrate parameter $q$. Every observable quantity—masses, couplings, decay rates, and causal structure—is a function of $q$ alone. Independent classes of measurements each restrict $q$ to a narrow range. These ranges overlap, rendering $q$ overdetermined.

**Consistency window.**

$$
  q  \in  [1.109, 1.112].
$$

See [Table 1](#tbl:substrate-consistency-window-table1-data).

Three independent sectors of physics—strong (mass ratios), electromagnetic (fine structure constant), and weak (beta decay)—all point to the same $q$. This is the central empirical result of the QOU: the entire Standard Model parameter space collapses to a single point in the consistency window.

**Derived quantities within the window.**

All entries below are zero-parameter predictions once $q$ is fixed by any one of the preceding determinations.

*Dimensionless ratios.*

See [Table 2](#tbl:substrate-consistency-window-table2-data).

*Mass predictions (MeV/$c^2$; $m_e$ input fixes the dressed quark mass).*

See [Table 3](#tbl:substrate-consistency-window-table3-data).

*Sensitivity amplifications.*

See [Table 4](#tbl:substrate-consistency-window-table4-data).
<!-- FILE_END: substrate-consistency-window.md -->

<!-- FILE_START: substrate-consistency-window-interpretation.md -->
**Significance.**
The overdetermination of $q$ acts as the strongest test of the framework. Three independent measurement classes agree on the identical parameter. The consistency window $[1.109, 1.112]$ remains narrow ($\Delta q / q \approx 0.3\%$) and tightens with observational precision. Any future measurement falling outside this window falsifies the framework.
<!-- FILE_END: substrate-consistency-window-interpretation.md -->

<!-- FILE_START: three-calibration-discipline.md -->
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
<!-- FILE_END: three-calibration-discipline.md -->

