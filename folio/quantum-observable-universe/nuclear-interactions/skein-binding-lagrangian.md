*Let $L = Z\mathfrak{p} \oplus N\mathfrak{n}$ be a multi-nucleon Hopf link with $Z$ protons, $N$ neutrons, and $A = Z + N$. The **canonical binding Lagrangian** is the categorical action $\mathfrak{S}_q$ evaluated on $L$:*
$$
  \mathcal{L}_{\mathrm{bind}}[L]
  = 
  \mathcal{L}_{\mathrm{qCLT}}
  - \mathcal{L}_{\mathrm{Coulomb}}.
$$
*Each term arises from the exact evaluation of the topological trace on the link components, without empirical liquid-drop parameters:*

1. ***Strong Binding (q-CLT/JSJ volume term).** The strong force contribution evaluates strictly from the Hecke channel traces. As established in [q-CLT mass scaling](../mass-theory/q-clt-jsj-mass-scaling.md), the Jaco–Shalen–Johannson decomposition yields an additive scaling for the strong binding:*
   $$
     \mathcal{L}_{\mathrm{qCLT}}
     = \alpha \sum_i \ln\lvert V_i\rvert,
   $$
   *where $\alpha = \mathfrak{m}_e / (q_0(q_0-1))$ is the rigid substrate scale (built from CAL-1 $\mathfrak{m}_e$ and CAL-2 $q_0$), and $V_i$ are the two-nucleon sub-braid Markov traces for each bond type. This carries no empirical parameter beyond that calibration scale, and is **intended** to replace the empirical Bethe-Weizsäcker volume, surface, asymmetry, and pairing terms — but that replacement is **not a completed closure**: the per-isotope binding magnitude ($\Delta_\lambda$) is open, so its empirical accuracy against AME is not established here.*

2. ***Coulomb repulsion (imported, not derived).** The term is the standard uniform-sphere Coulomb energy*
   $$
     \mathcal{L}_{\mathrm{Coulomb}} = E_C(Z, A)
     = \frac{3}{5}\,\frac{Z(Z-1)\,\alpha_{\mathrm{EM}}\,\hbar c}{R},
     \qquad R = \bar\lambda_\pi\,A^{1/3},
   $$
   *with $\bar\lambda_\pi = \hbar c/\mathfrak{m}_\pi$ the CAL-3 length. It is not obtained from the categorical action. No braid element and no invariant pair coupling between two nucleon blocks produces a pair term proportional to $Q_AQ_B$ ([the Coulomb-charge definition](#def:coulomb-charge)), and a bond graph of bounded degree, such as the nearest-neighbour bonds of the strong term above, cannot carry a term growing like $Z(Z-1)$ when the energy per bond does not grow with $Z$. A Coulomb pair term needs the electroweak mixing angle of [the Weinberg-angle conjecture](#conj:weinberg-angle-categorical) together with a mass scale that removes the $Z$ exchange at nuclear distance, and neither is derived. The status of each input:*

   | input | status |
   |---|---|
   | $Z(Z-1)$ | derived: the number of ordered pairs of $Z$ unit charges |
   | $\alpha_{\mathrm{EM}}$ | conditional: the tree value $1/(q_0[9]_q[10]_q)$ is a derived trace ratio; the correction to it is open and no form is chosen |
   | $\hbar c$ | unit conversion |
   | coefficient $1$ on $\bar\lambda_\pi$ | a selection; nothing derives it |
   | $A^{1/3}$ | an assumed packing law, not derived |
   | $\tfrac{3}{5}$ | imported uniform-ball self-energy; the braid supplies no charge density |

   *No continuous parameter is tuned, but three of the six inputs are selected or imported, so this is a standard-physics estimate with one conditional framework input; the Coulomb coefficient itself is not derived. Comparison only: on the mirror pair $^3\mathrm{H}$/$^3\mathrm{He}$ it gives $\Delta E_C \approx 0.847$ MeV against the $0.764$ MeV the measured masses require ($+10.9\%$). Solving for the exponent against measured radii gives $0.43$ at $^3\mathrm{H}$ and $0.53$ at $^3\mathrm{He}$ in place of $1/3$, and the alternatives to $3/5$ bracket the observed value ($3/5 \to 0.849$, $1/2 \to 0.707$ MeV).*

**Archimedean specialisation.** What follows sits on the archimedean side of the substrate wall. It invokes real- or complex-analytic constructs—real-valued physical observables, real-analytic bounds, transcendental constants, or numerical evaluation at the substrate parameter $q_0$. Any generic categorical/$q$-deformation identities it relies upon remain valid over an abstract coefficient ring; only their archimedean realisation is specialised here.
