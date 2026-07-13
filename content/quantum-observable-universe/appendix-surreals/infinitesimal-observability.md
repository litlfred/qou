The QOU observability axiom requires $\mathrm{Hom}(\mathbf{1}, \mathrm{Ad}(A)) = 0$ ([quantum observable universe](#def:quantum-observable-universe)): the trivial representation does not appear in the adjoint of $A$. This rigidity condition guarantees $A$ has no infinitesimal symmetries beyond the identity. Under a surreal lift, this can be relaxed.

**Conjecture.** The $\varepsilon$-relaxed observability axiom is:
$$
  \dim_{\mathbf{No}} \mathrm{Hom}(\mathbf{1}, \mathrm{Ad}(A)) \leq \varepsilon.
$$
The hom-space is non-empty, but every element has $\mathbf{No}$-norm bounded by an infinitesimal $\varepsilon$. A surreal QOU satisfying $\varepsilon$-relaxed observability has a standard-part image satisfying strict observability.

In the archimedean case, $\mathrm{Hom}(\mathbf{1}, \mathrm{Ad}(A))$ is either zero or non-zero. In the surreal case, hom-spaces are $\mathbf{No}$-modules, so "small" becomes "infinitesimal-norm". Take a strict-observability $A$ and add an infinitesimal generator $\xi \in \mathrm{Hom}(\mathbf{1}, \mathrm{Ad}(A))$ with $|\xi| = \varepsilon$. The result is a surreal QOU with $\dim_{\mathbf{No}} \mathrm{Hom}(\mathbf{1}, \mathrm{Ad}(A)) = 1$ but $|\xi| = \varepsilon$. Whether such $\xi$ can be constructed cohomologically is open.

Applying $\mathrm{St}$ kills $\xi$, recovering strict observability. The hard direction is lifting: given an archimedean QOU with strict observability, does a surreal QOU exist above it with a non-trivial $\xi$?

The observability axiom controls what counts as an observable. If $\mathrm{Hom}(\mathbf{1}, \mathrm{Ad}(A)) = 0$, every endomorphism of $A$ is detectable. Under relaxation, infinitesimally many endomorphisms might be almost-detectable—visible at first order in $\varepsilon$ but invisible to archimedean observers. This corresponds to near-symmetries broken at the archimedean scale but restored at the infinitesimal scale.

To prove standard-part recovery, note that $\mathrm{St}(\xi) = 0$ because the standard part of an infinitesimal vanishes. For strict generalisation, construct a candidate non-trivial $\xi$ from a class in $\mathrm{HH}^1(A, A) \otimes_{\mathbb{R}} \mathbf{No}$ that becomes infinitesimal under standard-part, and show it is not in the image of any classical Hochschild representative. Falsification requires proving every infinitesimal element of $\mathrm{Hom}_{\mathbf{No}}(\mathbf{1}, \mathrm{Ad}(A))$ comes from a real element scaled by $\varepsilon$.
