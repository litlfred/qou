The [Yang–Mills surreal bound](#rem:yang-mills-surreal-bound) gives the mass-gap statement at substrate order $\Delta_q \asymp \varepsilon^3$ but explicitly defers the Wightman-axiom portion of the Millennium Prize statement—the regularity programme of recovering a standard renormalised QFT as the standard part of the $q$-deformed substrate. This conjecture supplies the bridge: the Reeb $\mathbb{Z}_2$ acting on the [Frobenius pairing](#def:frobenius-hopf-substrate) furnishes Osterwalder–Schrader reflection positivity in the archimedean realisation. Together with the surreal mass gap, this forms the Osterwalder–Schrader sufficient input for Wightman reconstruction.

**Conjecture (OS reflection positivity from the Reeb $\mathbb{Z}_2$).**
*Let $\theta$ denote the antipodal $\mathbb{Z}_2 \subset U(1)_{\xi}$ inside the Reeb $U(1)$—equivalently, the chart-swap involution $\iota : Z \mapsto Z^{-1}$ on the [contact affine chart](#def:contact-affine-chart) at $\varTheta = \pi$, per [chart-swap $U(1)$ is the Reeb flow](#prop:reeb-u1-chart-swap). Then the [Frobenius pairing](#def:frobenius-hopf-substrate) $\langle\,\cdot\,,\,\cdot\,\rangle_F$ on $A$ satisfies reflection positivity under $\theta$:*

$$
\langle \theta(\phi), \phi \rangle_F \geq 0 \qquad \text{for every state } \phi \in A_+,
$$

*with equality if and only if $\phi$ vanishes on the positive-time half of the Reeb decomposition. Under the [archimedean realization](#def:archimedean-realization-functor) $\tau_{\mathrm{arch}}$, this categorical positivity descends to the Osterwalder–Schrader reflection-positivity axiom of the four Euclidean Wightman correlation functions $\tau_{\mathrm{arch}}\bigl(\langle \phi_1 \cdots \phi_n \rangle_F\bigr)$ on the $\varepsilon \to 0$ standard manifold $\mathbb{R}^4$.*

The Osterwalder–Schrader reflection $\theta_{\mathrm{OS}}$ on Euclidean spacetime is reflection in the $\tau = 0$ hyperplane, i.e., $(x_1, x_2, x_3, \tau) \mapsto (x_1, x_2, x_3, -\tau)$. In the categorical contact-geometric formulation, Euclidean time is the Reeb parameter $t$ along $\xi$ ([categorical Reeb derivation](#def:categorical-reeb)), so $\theta_{\mathrm{OS}}$ acts on the contact affine chart as $\phi_t \mapsto \phi_{-t}$. The categorical realisation of this involution is precisely the antipodal $\mathbb{Z}_2$ subgroup at $\varTheta = \pi$ of the chart-swap $U(1)$ family $\rho_\varTheta : z \mapsto e^{i\varTheta} z$. The [chart-swap–Reeb identification](#prop:reeb-u1-chart-swap) shows this coincides with the Reeb flow $U(1)$. No separate OS reflection needs to be constructed: it is already present in the categorical infrastructure as the $\mathbb{Z}_2$ subgroup of the Reeb circle.

The Frobenius pairing is symmetric by construction: $\Psi = S^2 = \mathrm{id}_A$, so $\langle a, b \rangle_F = \langle b, a \rangle_F$. Under the $\theta$-action on $A$, the antipode $S$ swaps the two factors and inverts the Reeb flow direction. Symmetry of the Frobenius pairing under $\Psi$ implies $\theta$-invariance of the pairing up to the sign captured by the Reeb-half decomposition. The conjecture is the positivity statement: for any state $\phi$ supported on the positive-time Reeb half, $\langle \theta(\phi), \phi \rangle_F$ evaluates to a non-negative scalar in $\mathrm{End}_{\mathbf{C}}(\mathbf{1})$. This positivity refines the symmetry. Symmetry alone gives $\langle \theta(\phi), \phi \rangle_F = \langle \phi, \theta(\phi) \rangle_F$ (so the quantity is real), but does not force the real value to be non-negative. The required structural input is that the antipode-twisted pairing $\langle \theta(\cdot), \cdot \rangle_F$ descends through $\tau_{\mathrm{arch}}$ to a positive-definite inner product on the half-line $L^2(\mathbb{R}_{>0})$.

The Osterwalder–Schrader theorem states that a family of Euclidean correlation functions $\{S_n\}$ on $\mathbb{R}^4$ defines a Wightman QFT on Minkowski space if and only if (OS0) temperedness, (OS1) Euclidean covariance, (OS2) reflection positivity, (OS3) symmetry, and (OS4) cluster decomposition all hold.

In the QOU framework:

| OS axiom | QOU input |
|----------|-----------|
| OS0 (temperedness) | $\tau_{\mathrm{arch}}$ images of partial products $\Phi_n$ are tempered by the [archimedean limit conjecture](#conj:dilogarithm-archimedean-limit) at every $x \in (0, 1)$. |
| OS1 (Euclidean covariance) | $S_5$-action on Bring's coordinate ring is the categorical lift of the $\mathrm{SO}(4) / \mathrm{Spin}(4)$ rotation group, and the [$\mathbb{Z}_2 \hookrightarrow U(1)_{\xi}$](#prop:reeb-u1-chart-swap) hierarchy is the Euclidean time translation. |
| **OS2 (reflection positivity)** | **This conjecture.** |
| OS3 (symmetry / locality) | Categorical permutation symmetry of the Frobenius pairing; $\Psi = S^2 = \mathrm{id}_A$. |
| OS4 (cluster decomposition) | Mass gap $\Delta_q \asymp \varepsilon^3$ from the [surreal bound](#rem:yang-mills-surreal-bound) gives exponential clustering at separation $r$: $|S_n(\cdots) - S_k(\cdots) S_{n-k}(\cdots)| \lesssim e^{-\Delta_q r}$. |

OS0, OS1, OS3 are categorically built-in. OS4 is the [surreal mass-gap statement](#rem:yang-mills-surreal-bound). OS2 is the open input—this conjecture. Granting it, the OS theorem reconstructs a Wightman QFT on $\mathbb{R}^4$ as the standard part of the $q$-deformed substrate, completing the Wightman-axiom portion of the Yang–Mills millennium statement.

The positivity statement involves three open ingredients:

1. **Categorical positivity of the antipode-twisted pairing.** The Frobenius pairing is constructively non-degenerate, but neither the QOU axioms nor the [Frobenius–Hopf substrate definition](#def:frobenius-hopf-substrate) currently impose positivity of $\langle \theta(\cdot), \cdot \rangle_F$. The conjecture claims the substrate, being a $C^*$-Frobenius–Hopf algebra in the archimedean specialisation ($q = q_0 \in \mathbb{R}_{>1}$), inherits positivity from the $C^*$-norm.
2. **Stability under $\tau_{\mathrm{arch}}$.** The archimedean realisation functor must commute with the positivity restriction: $\tau_{\mathrm{arch}}\bigl(\langle\theta(\phi),\phi\rangle_F\bigr) = \bigl\langle\theta_{\mathrm{OS}}\tau_{\mathrm{arch}}(\phi),\, \tau_{\mathrm{arch}}(\phi)\bigr\rangle_{L^2(\mathbb{R}^4)}$. Equivalently, the OS reflection on the standard Euclidean correlation functions is the $\tau_{\mathrm{arch}}$-image of the Reeb antipodal $\mathbb{Z}_2$ action. This follows from the [chart-swap–Reeb identification](#prop:reeb-u1-chart-swap) once $\tau_{\mathrm{arch}}$ preserves the $U(1)_{\xi}$-action on contact charts.
3. **Supporting infrastructure.** A complete proof requires a Frobenius structure on the categorical $C^*$-completion together with the Wightman reconstruction theorem. The conjecture amounts to a single positivity inequality; granting it, the surreal bound completes OS reconstruction.

Ingredients (2) and (3) are technical plumbing once the categorical content is settled. The only genuinely new mathematical input needed is a single positivity axiom on the substrate Frobenius algebra. A Frobenius algebra $(A, \mu, \eta, \Delta, \varepsilon)$ in a $C^*$-tensor category is positive if its evaluation map $\eta : \mathbf{1} \to A$ admits a state-positive lift—i.e., the composition

$$
\mathbf{1} \xrightarrow{\;\eta\;} A \xrightarrow{\;\Delta\;} A \otimes A \xrightarrow{\;\mathrm{id}\,\otimes\,*\;} A \otimes A^*
$$

factors through the positive cone of $A \otimes A^*$. The missing input is exactly this:

> **Axiom (substrate $C^*$-Frobenius positivity).** At the archimedean substrate value $q = q_0 \in \mathbb{R}_{>1}$, the [Frobenius–Hopf substrate](#def:frobenius-hopf-substrate) $A$ admits a $C^*$-completion in which the unit map $\eta : \mathbf{1} \to A$ is positive in the categorical sense above. Equivalently, $(A, \mu, \eta, \Delta, \varepsilon)$ is a *positive* Frobenius algebra in the $C^*$-tensor category $\mathbf{C}$ at $q_0$.

Granting the substrate $C^*$-Frobenius positivity axiom, along with [Chart-swap $U(1)$ equals the Reeb $U(1)$ as subgroups of $\mathrm{Aut}(\mathbb{P}(V))$](#prop:reeb-u1-chart-swap) and [Archimedean realization functor $\mathcal{R}_{\mathrm{top}}$](#def:archimedean-realization-functor), OS axiom (OS2) holds: $\langle\theta(\phi), \phi\rangle_F \geq 0$ for every state $\phi$ in the positive-time Reeb half.

The proof sketch involves three steps:

1. **Categorical reflection = Reeb $\mathbb{Z}_2$.** By [Chart-swap $U(1)$ equals the Reeb $U(1)$ as subgroups of $\mathrm{Aut}(\mathbb{P}(V))$](#prop:reeb-u1-chart-swap), $\theta$ is the antipodal $\mathbb{Z}_2 \subset T_q$ subgroup acting on the contact-affine chart $\mathbb{P}(V)$ via $z \mapsto -z$. On the substrate Hopf algebra $A$, the action $\theta_A : A \to A$ factors through the antipode $S$ via the $T_q$-grading: $\theta_A = S \circ (\mathrm{sign}\,\text{of}\,\xi\text{-grading})$.
2. **Antipode-twisted pairing = state-positive form.** The substrate Frobenius pairing factors through the antipode by $\langle a, b \rangle_F = \varepsilon(\mu(a, S(b)))$. Composing with $\theta_A$: $\langle \theta(\phi), \phi \rangle_F = \varepsilon(\mu(\theta(\phi), S(\phi))) = \varepsilon(\mu(S(\phi^*), S(\phi)))$ where $\phi^*$ is the $C^*$-conjugate. By the substrate positivity axiom, this evaluates to a non-negative element of $\mathrm{End}_{\mathbf{C}}(\mathbf{1}) = k$.
3. **Stability under $\tau_{\mathrm{arch}}$.** $\tau_{\mathrm{arch}}$ sends the categorical $C^*$-norm to the standard $L^2$-norm on $\mathbb{R}^4$ by construction. Positivity is preserved.

The status of OS reflection positivity in the QOU framework is equal to the status of this single $C^*$-Frobenius positivity axiom. The axiom is well-formulated inside unitary fusion categories and unitary $C^*$-Frobenius algebras. Verifying that the QOU substrate $A$ at $q_0 \in \mathbb{R}_{>1}$ satisfies it requires:

- A choice of $C^*$-norm on $A$ compatible with the $q_0$-deformation.
- Verification that one of these candidate norms makes the Frobenius pairing positive in the sense above.
- Compatibility of the chosen norm with the antipode $S$.

This follow-up programme is stated as [Wenzl positivity at $q_0$ implies substrate $C^*$-Frobenius positivity](#conj:wenzl-positivity-implies-substrate-positivity). Closing that bridge conjecture makes the substrate axiom derived from Wenzl's classical result, discharging the OS-reflection-positivity-as-axiom assumption.

The Wightman-axiom portion of the Yang–Mills millennium statement reduces to the structural positivity of the antipode-twisted Frobenius pairing. The reflection involved is the antipodal $\mathbb{Z}_2$ subgroup of the Reeb $U(1)$, made visible by the [chart-swap–Reeb identification](#prop:reeb-u1-chart-swap). The categorical infrastructure already houses every OS ingredient except this positivity.
