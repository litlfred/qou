<!-- FILE_START: infinitesimal-observability.md -->
The QOU observability axiom requires $\mathrm{Hom}(\mathbf{1}, \mathrm{Ad}(A)) = 0$ ([quantum observable universe](#def:quantum-observable-universe)): the trivial representation does not appear in the adjoint of $A$. This rigidity condition guarantees $A$ has no infinitesimal symmetries beyond the identity. Under a surreal lift, this can be relaxed.

**Conjecture.** The $\varepsilon$-relaxed observability axiom is:
$$
  \dim_{\mathbf{No}} \mathrm{Hom}(\mathbf{1}, \mathrm{Ad}(A)) \leq \varepsilon.
$$
The hom-space is non-empty, but every element has $\mathbf{No}$-norm bounded by an infinitesimal $\varepsilon$. A surreal QOU satisfying $\varepsilon$-relaxed observability has a standard-part image satisfying strict observability.

In the archimedean case, $\mathrm{Hom}(\mathbf{1}, \mathrm{Ad}(A))$ is either zero or non-zero. In the surreal case, hom-spaces are $\mathbf{No}$-modules, so "small" becomes "infinitesimal-norm". Take a strict-observability $A$ and add an infinitesimal generator $\xi \in \mathrm{Hom}(\mathbf{1}, \mathrm{Ad}(A))$ with $|\xi| = \varepsilon$. The result is a surreal QOU with $\dim_{\mathbf{No}} \mathrm{Hom}(\mathbf{1}, \mathrm{Ad}(A)) = 1$ but $|\xi| = \varepsilon$. Whether such $\xi$ can be constructed cohomologically is open.

Applying $\mathrm{St}$ kills $\xi$, recovering strict observability. The hard direction is lifting: given an archimedean QOU with strict observability, does a surreal QOU exist above it with a non-trivial $\xi$?

The observability axiom controls what counts as an observable. If $\mathrm{Hom}(\mathbf{1}, \mathrm{Ad}(A)) = 0$, every endomorphism of $A$ is detectable. Under relaxation, infinitesimally many endomorphisms might be almost-detectable—visible at first order in $\varepsilon$ but invisible to archimedean observers. This corresponds to near-symmetries broken at the archimedean scale but restored at the infinitesimal scale.

To prove standard-part recovery, note that $\mathrm{St}(\xi) = 0$ by `standardPart_of_infinitesimal`. For strict generalisation, construct a candidate non-trivial $\xi$ from a class in $\mathrm{HH}^1(A, A) \otimes_{\mathbb{R}} \mathbf{No}$ that becomes infinitesimal under standard-part, and show it is not in the image of any classical Hochschild representative. Falsification requires proving every infinitesimal element of $\mathrm{Hom}_{\mathbf{No}}(\mathbf{1}, \mathrm{Ad}(A))$ comes from a real element scaled by $\varepsilon$.
<!-- FILE_END: infinitesimal-observability.md -->

<!-- FILE_START: vacuum-epsilon.md -->
The Hoefsmit scattering pipeline assigns a geometric energy $\mathrm{Geom}(L)$ to each link $L$ ([Hoefsmit scattering pipeline](#conj:hoefsmit-scattering-pipeline)). Vacuum normalisation requires $\mathrm{Geom}(\unicode{9737}) = 0$ on the unknot. This is a boundary case in the geometric-energy formula and represents a fine-tuned theory (zero vacuum energy). Under a surreal lift, this strict zero can be relaxed.

**Conjecture.** The $\varepsilon$-relaxed vacuum axiom is:
$$
  \mathrm{Geom}(\unicode{9737}) = \varepsilon \in \mathbf{No}.
$$
Every surreal QOU satisfies this relaxation with some positive infinitesimal $\varepsilon$, and the standard-part recovers the strict vacuum: $\mathrm{st}(\varepsilon) = 0$.

If the conjecture holds:
1. The special case for $\unicode{9737}$ is absorbed, giving $\mathrm{Geom}(L) = (\text{generic formula}) + \varepsilon \cdot (\text{number of unknot components})$.
2. The diagonal subtraction in the Möbius energy is exactly the $\varepsilon$-vacuum contribution.
3. Every particle mass $\mathfrak{m}(\mathfrak{H})$ becomes $\mathfrak{m}(\mathfrak{H}) + \varepsilon \cdot c_{\mathfrak{H}}$. The standard-part is zero, leaving archimedean predictions unchanged.
4. When the multiplier of $\varepsilon$ is a surreal-infinite mode count, the product can have a nonzero standard part ($\omega \cdot \varepsilon = 1$). The Casimir force ([Casimir force](#conj:casimir-epsilon-vacuum)) is the $\mathrm{st}$-image of the plate-constrained unknot-count gradient times $\varepsilon$.

This provides cleaner axioms without fine-tuning and unifies the Möbius regularisation with the $\varepsilon$-vacuum subtraction.

To prove the conjecture, recompute geometric energy and particle masses with $\mathrm{Geom}(\unicode{9737}) = \varepsilon$. Apply $\mathrm{St}$ to show archimedean predictions are unchanged. Show the diagonal subtraction in the Möbius energy is exactly the $\varepsilon$-vacuum subtraction. Falsification requires finding a particle mass that changes under standard-part.
<!-- FILE_END: vacuum-epsilon.md -->

<!-- FILE_START: casimir-epsilon-vacuum.md -->
**Conjecture (Casimir force as standard-part of $\varepsilon$-vacuum density gradient).** Assume the [$\varepsilon$-relaxed vacuum axiom](#conj:vacuum-epsilon). Let two parallel conducting plates of area $A$ separated by $d$ constrain the unknot-component count of the vacuum to a surreal-valued density $N_{\unicode{9737}}^{\text{in}}(A, d)$ between the plates and $N_{\unicode{9737}}^{\text{out}}(A, d)$ outside. The standard Casimir force per unit area
$$
  \frac{F_{\text{Cas}}(d)}{A} \approx -\frac{\pi^{2}\hbar c}{240 d^{4}}
$$
is recovered as the standard-part of the surreal-energy gradient
$$
  \frac{F_{\text{Cas}}(d)}{A} = -\mathrm{st}\!\left(\frac{1}{A}\frac{\partial}{\partial d}\bigl[N_{\unicode{9737}}^{\text{in}}(A, d) - N_{\unicode{9737}}^{\text{out}}(A, d)\bigr] \cdot \varepsilon\right).
$$

The functor $\mathrm{st}$ annihilates $X \cdot \varepsilon$ only when $X$ is finite. The unknot-component count between plates is surreal-infinite ($\omega \cdot \varepsilon = 1$). Concretely, we assert
$$
  N_{\unicode{9737}}^{\text{in}}(A, d) - N_{\unicode{9737}}^{\text{out}}(A, d) = -\frac{\pi^{2}}{720}\frac{A}{d^{3}}\hbar^{2}_{q}\hbar c \cdot \varepsilon^{-1} + \text{lower-birthday corrections}.
$$
The $\hbar^{2}_{q}$ factor ensures dimensional consistency with the Hoefsmit normalisation. It cancels the denominator in $\mathrm{Geom}_\varepsilon$, leaving a finite real energy. Taking the gradient recovers the textbook force.

This mechanism resolves the cosmological-constant puzzle in surreal language: vacuum energy is $\infty \cdot 0$ archimedeanly, but a finite surreal in $\mathbf{No}$.

The conditional derivation is rigorous modulo the surreal-arithmetic infrastructure. The Lean formulation in `CasimirEpsilonVacuum.lean` uses instance hypotheses. The conjecture requires proving the existence of $N_{\unicode{9737}}^{\text{in}}(A, d)$ as a categorical object via a Yekutieli-homotopy lift. It requires showing the $A/d^{3} \cdot \varepsilon^{-1}$ scaling and deriving the numerical prefactor $\pi^{2}/720$ from $\zeta(-3)$. Falsification occurs if the categorical mode-count does not match the predicted surreal coefficient.
<!-- FILE_END: casimir-epsilon-vacuum.md -->

<!-- FILE_START: casimir-first-q-correction.md -->
**Conjecture (first substrate correction to the Casimir force is carried by $4_1$).** Assume the plate-constrained mode-count of [Casimir force](#conj:casimir-epsilon-vacuum). Its leading $1/d^{4}$ term is built from disjoint free-photon modes and is independent of substrate deformation. The first contribution carrying substrate-$q$ dependence arises from the interacting sector. Its minimal carrier is the figure-eight knot $4_1$, entering with weight equal to its Markov trace
$$
  J_{4_1}(q) = q^{-2} - q^{-1} + 1 - q + q^{2} = 1 + \tfrac{3}{4}h^{2} + O(h^{4}), \qquad h = q - q^{-1}.
$$

The leading parallel-plate term is assembled from free photon modes (identity braids). Degree-$\leq 1$ closures are non-hyperbolic with vanishing volume. Modes that do not braid transmit no substrate deformation. Substrate corrections enter only where modes braid.

Degree $\geq 2$ is necessary for hyperbolicity. Minimal degree-$\geq 2$ closures (Hopf link, trefoil, $(2,5)$-torus knot) have $\mathrm{Vol} = 0$. The first hyperbolic closure is the figure-eight knot $4_1$, with $\mathrm{Vol}(4_1) \approx 2.0299$.

The figure-eight weight satisfies the exact field identity
$$
  J_{4_1}(q) = 1 + \tfrac{3}{4}h^{2} + \frac{h^{4}}{4(h^{2} + 8 + 4(q + q^{-1}))}.
$$
The coefficient $3/4$ is forced by the identity. The expansion is proved in `FigureEightCasimirWeight.lean`.

The substrate parameter $q_0$ is fixed through $\mathrm{Vol}(4_1)$. The knot defining the one calibrated deformation parameter also carries the vacuum's first substrate correction.

The conjecture requires the interacting-mode mode-sum. The $1/d^6$ power is an expectation, not a derivation. The absolute magnitude is suppressed by $\sim \alpha \lambda_C/d$, below current precision. Falsification requires showing the first non-vanishing substrate correction is not weighted by $J_{4_1}$.
<!-- FILE_END: casimir-first-q-correction.md -->
