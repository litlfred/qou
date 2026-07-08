<!-- FILE_START: surreal-blowup-calculus.md -->
Fix an infinitesimal $\varepsilon = 1/\omega \in \mathbf{No}$. Equivalently, $\omega = 1/\varepsilon$ is the first infinite ordinal regarded as a surreal.

See [Table](#tbl:surreal-blowup-calculus-table-data) for named surreals. Every name corresponds to a unique element under Conway's recursive construction.

A blow-up of a divergent expression evaluates the expression at a named infinite surreal, then takes the standard part of a renormalised version:
1. Write the divergent expression $X$ as a function of a parameter that becomes a named surreal: $X = X(\Lambda)$ with $\Lambda \to \omega$.
2. Identify a counterterm $C(\Lambda)$ such that $X(\Lambda) - C(\Lambda)$ is a finite surreal.
3. Define the renormalised value: $X_{\mathrm{ren}} := \mathrm{st}(X(\omega) - C(\omega)) \in \mathbb{R}$.

The field $\mathbf{No}$ makes every step literal. The cutoff $\Lambda$ is a specific element. The counterterm is a specific surreal-valued function. The standard part is a specific real number.
<!-- FILE_END: surreal-blowup-calculus.md -->

<!-- FILE_START: surreal-blowup-examples.md -->
Physics frequently uses an unspecified $\infty$ to denote an unrenormalised divergence ($\Lambda \to \infty$, $1/\varepsilon$, $\delta(0)$). These require a specific element in an extended number system. The blow-up calculus ([surreal blow-up calculus](#def:surreal-blowup-calculus)) makes each device literal in $\mathbf{No}$.

**Möbius energy diagonal.** The diagonal-regularised Möbius energy ([Möbius energy proof](#prf:mobius-energy)) computes
$$
  E(\varrho) = \iint_{S^1 \times S^1} \!\!\left(\frac{1}{|\varrho(s) - \varrho(t)|^2} - \frac{1}{D(\varrho(s), \varrho(t))^2}\right) \!ds\, dt.
$$
In the surreal lift, the inner integrand at $s = t$ evaluates to $1/0^2 = \omega^2$. The arc-length subtraction $1/D^2$ matches this $\omega^2$. The difference is a finite surreal, and its standard part is the renormalised energy.

**$c_q$ at $q = 1$.** The speed of light $c_q = 1/(q-1)$ at $q = 1 + \varepsilon$ is exactly $\omega \in \mathbf{No}$. The classical-limit divergence "$c_q \to \infty$ as $q \to 1$" becomes the literal identity $c_q\big|_{q = 1 + \varepsilon} = \omega$.

**Vacuum normalisation.** The empty-link Markov trace evaluates to $\mathrm{tr}_M(1) = 1/(\sqrt{q} + 1/\sqrt{q})$. At $q = 1 + \varepsilon$, this is $1/2 + O(\varepsilon)$. In the unnormalised convention $\mathrm{tr}_M(1) = 1$, normalisation factors become $1/0$. The named-surreal calculus makes these distinctions explicit.

The blow-up calculus respects the birthday grading. The counterterm $C(\omega)$ has the same birthday as $X(\omega)$. Their difference lives at a strictly lower birthday. The standard part collapses it to $\mathbb{R}$. This provides a birthday-graded refinement of BPHZ subtraction, where each subtraction reduces the birthday by a controlled ordinal amount.

The QOU mass formula contains no divergences. The blow-up calculus serves three secondary purposes:
1. **Möbius energy comparison**: We turn the informal classical $\infty$ into a named $\omega^2$.
2. **Classical-limit $q \to 1$**: We make "$c_q \to \infty$" literal.
3. **Future renormalisation work**: We provide a setting for Yang--Mills or Sobolev-completion arguments requiring regularisation.
<!-- FILE_END: surreal-blowup-examples.md -->

<!-- FILE_START: mobius-surreal-renormalization.md -->
The [Möbius energy](#prop:mobius-energy) is a renormalized quadratic interaction: $\iint |\varrho(s)-\varrho(t)|^{-2}$ and $\iint D(s,t)^{-2}$ each diverge on the diagonal, and the divergences cancel. Under the surreal lift, this renormalization becomes a difference of two infinite surreals.

Excise a diagonal band of width $\varepsilon = 1/\omega$ and set
$$
  I_1 = \iint_{|s-t|>1/\omega}\!\frac{|\varrho'(s)|\,|\varrho'(t)|}{|\varrho(s)-\varrho(t)|^2}, \qquad I_2 = \iint_{|s-t|>1/\omega}\!\frac{|\varrho'(s)|\,|\varrho'(t)|}{D(s,t)^2}.
$$
Both are infinite surreals of $\operatorname{ord}_\omega = +1$; each diverges like $c\,\omega$. Because $|\varrho(s)-\varrho(t)| = D(s,t) + O(|s-t|^3)$ near the diagonal, $I_1$ and $I_2$ share the same leading coefficient $c$. The $\omega^{+1}$ parts cancel, $I_1 - I_2$ is finite, and
$$
  E(\varrho) = \operatorname{std}\!\bigl(I_1 - I_2\bigr).
$$
The analytic Hadamard finite part becomes the standard part of a difference of two infinite surreals of equal leading $\omega$-order. The finiteness bound reduces to an algebraic leading-coefficient match $[\omega^{+1}]I_1 = [\omega^{+1}]I_2$.

This applies generally. For the Frostman/Riesz $s$-energy $I_s = \iint |x-y|^{-s}$, the Hausdorff dimension is the $\operatorname{ord}_\omega$ boundary at which $I_s$ flips from infinite to finite.

This provides surreal language for a classical renormalization. It adds no archimedean obligation: $E(\varrho)$ is the same real number. However, while $\mathbf{No}$ carries no Lebesgue measure, Hausdorff dimension (an exponent) and renormalized energies (a difference of infinite surreals) are surreal-native.
<!-- FILE_END: mobius-surreal-renormalization.md -->

<!-- FILE_START: bigbang-heatdeath.md -->
The QOU framework is parameter-time-symmetric: the substrate $q \in \mathbb{R}_{>0}$ controls all dimensionful constants but does not evolve. A cosmological reading would identify $q$-flow with cosmic time $t$, with two endpoints:
- **Big Bang**: $q \to 1^+$ ($c_q \to \infty$, all states causally connected).
- **Heat death**: $q \to \infty$ ($\hbar_q \to 1$, quantum scale saturates classical scale).

Both endpoints are singular limits in the archimedean sense. Standard physics treats these as unattainable.

**Conjecture.** The Big Bang and heat-death endpoints are the standard-part of evaluation at specific named surreals.

Let $\mathbf{QOU}_{1 + \varepsilon}$ be the surreal QOU at $q = 1 + \varepsilon$. We define
$$
  \mathbf{BigBang}_{1 + \varepsilon} := \mathrm{St}_{\mathrm{QOU}}(\mathbf{QOU}_{1 + \varepsilon}).
$$
1. **Big Bang as named-surreal evaluation**: There is a functor $\mathbf{BigBang} := \mathbf{BigBang}_{1 + \varepsilon}\big|_{\varepsilon \to 0^+}$. This is evaluation at a specific transfinite surreal $\varepsilon^\omega$, composed with $\mathrm{St}$.
2. **Heat death as evaluation at $q = \omega$**: $\mathbf{HeatDeath} := \mathrm{St}_{\mathrm{QOU}}(\mathbf{QOU}_{q = \omega})$.
3. **Both functors are well-defined**: The QOU mass formula and $\mathcal{Q}$-value derivations are rational in $q$, evaluating at any non-zero, non-pole element of $\mathbf{No}$. $\mathbf{BigBang}$ yields massless particles and equivalent knots. $\mathbf{HeatDeath}$ yields classical/quantum identification.
4. **Approximation by intermediate $\varepsilon$**: $\mathbf{QOU}_{1 + \varepsilon}$ for finite real $\varepsilon$ approximates $\mathbf{BigBang}$ to leading order.

If true, cosmological endpoints become objects in the category of archimedean QOUs. The Big Bang singularity is resolved into the standard-part of a surreal QOU. Observables near either endpoint are computed by perturbation in $\varepsilon$. Cosmological-time evolution $t \mapsto \mathbf{QOU}_{q(t)}$ becomes a functor from surreal times to archimedean QOUs.

The mathematical kernel is provable in Lean: $\mathrm{QOU}_q$ is rational in $q$, evaluation at non-pole $q \in \mathbf{No}$ is well-defined, and the standard-part produces well-defined archimedean QOUs. The interpretation requires a cosmological framework not developed in the main paper. Falsification requires showing structure constants have poles at $q = \omega$ or $q = 1$ in $\mathbf{No}$, which is false for rational formulas.
<!-- FILE_END: bigbang-heatdeath.md -->

<!-- FILE_START: cosmological-cone-visualization.md -->
Visualize the substrate-parameter axis $q \in \mathbb{R}_{>0}$ as the radial coordinate of a schematic cone with two endpoints:

| endpoint | $q$ | structure constants | geometric reading |
|---|---|---|---|
| Big Bang | $q \to 1^+$ | $c_q \to \infty$, $\hbar_q \to 0$ | "apex": causally connected |
| heat death | $q \to \infty$ | $c_q \to 0$, $\hbar_q \to 1$ | "asymptotic base": scales saturate |

At every interior $q$, each cross-section carries a copy of the Reeb bundle $\mathcal{R}_p \cong S^3$ over the exceptional divisor $\mathcal{S}_p$, with the three color sectors threaded under the color twist $q\phi$. As $q$ varies, the embedding deforms continuously.

Light speed $c_q$ diverges at the Big Bang ($q \to 1^+$), and $\hbar_q$ saturates to $1$ at heat death ($q \to \infty$).

The cone is a schematic mnemonic. It does not introduce a physical metric on the parameter axis, commit to a cosmological-time reading of $q$, or promote the endpoint functors from conjecture to theorem. It provides a unifying picture for the substrate parameter, exceptional divisor, Reeb bundle, and color sectors.
<!-- FILE_END: cosmological-cone-visualization.md -->

