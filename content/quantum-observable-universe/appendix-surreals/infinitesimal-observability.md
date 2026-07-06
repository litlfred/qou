The QOU observability axiom requires $\mathrm{Hom}(\mathbf{1}, \mathrm{Ad}(A)) = 0$ ([quantum observable universe](#def:quantum-observable-universe) condition (ii)). The trivial representation does not appear in the adjoint of $A$. This rigidity condition guarantees $A$ has no infinitesimal symmetries beyond the identity.

Under a surreal lift, we relax this to allow infinitesimally many symmetries.

## Conjecture

The **$\varepsilon$-relaxed observability axiom** is:

$$
  \dim_{\mathbf{No}} \mathrm{Hom}(\mathbf{1}, \mathrm{Ad}(A))
   \;\leq\; \varepsilon.
$$

We interpret this as: the hom-space is non-empty, but every element has $\mathbf{No}$-norm bounded by an infinitesimal $\varepsilon$.

The conjecture: a surreal QOU satisfying $\varepsilon$-relaxed observability has a standard-part image satisfying strict observability.

## Plausibility

In the archimedean case, $\mathrm{Hom}(\mathbf{1}, \mathrm{Ad}(A))$ is either zero or non-zero. There is no middle ground. In the surreal case, hom-spaces are $\mathbf{No}$-modules. We interpret "small" meaningfully as "infinitesimal-norm".

Consider a strict-observability $A$. We add an infinitesimal generator $\xi \in \mathrm{Hom}(\mathbf{1}, \mathrm{Ad}(A))$ with $|\xi| = \varepsilon$. The resulting structure is a surreal QOU with $\dim_{\mathbf{No}} \mathrm{Hom}(\mathbf{1}, \mathrm{Ad}(A)) = 1$ but $|\xi| = \varepsilon$. The condition is satisfied if we read "$\leq \varepsilon$" as a norm-bound.

Whether we can construct such $\xi$ cohomologically remains open. The natural source is a non-trivial class in $\mathrm{HH}^1(A, A)$ that trivializes in the archimedean limit but persists at infinitesimal order.

## Standard-part recovery

Applying $\mathrm{St}$ kills the infinitesimal $\xi$ because $\mathrm{st}(\varepsilon) = 0$. The archimedean image has $\mathrm{Hom}(\mathbf{1}, \mathrm{Ad}(A)) = 0$. We recover strict observability. This establishes the easy direction.

The hard direction is lifting: given an archimedean QOU with strict observability, does there exist a surreal QOU above it with relaxed observability and a non-trivial $\xi$? If so, the relaxation is a strict generalisation. If not, the relaxation is a tautology.

## Significance

The observability axiom controls what counts as an observable. If $\mathrm{Hom}(\mathbf{1}, \mathrm{Ad}(A)) = 0$, the fibre functor $\tau$ detects every endomorphism of $A$. Under the relaxation, infinitesimally many endomorphisms might be almost-detectable. They remain visible at first order in $\varepsilon$ but invisible to standard-part archimedean observers.

This corresponds to near-symmetries. These symmetries break spontaneously at the archimedean scale but restore at the infinitesimal scale. The analog in particle physics is approximate isospin or chiral symmetry, exact in idealized limits but broken by small parameters at physical scales.

## Proof strategy

We use the same architecture as [infinitesimal-frobenius](#conj:infinitesimal-frobenius).

**Standard-part recovery (provable now)**:

1. We are given an $\varepsilon$-relaxed observability witness $\xi \in \mathrm{Hom}_{\mathbf{No}}(\mathbf{1}, \mathrm{Ad}(A))$ with $|\xi| \leq \varepsilon$.
2. We have $\mathrm{St}(\xi) = 0$ by `standardPart_of_infinitesimal`. The standard-part of the hom-space contains no non-zero elements: $\mathrm{Hom}_{\mathbb{R}}(\mathbf{1}, \mathrm{Ad}(\mathrm{St}(A))) = 0$.
3. Strict observability holds for the standard-part image.

**Strict generalisation (open)**:

4. We construct a candidate non-trivial $\xi$. We source a class in $\mathrm{HH}^1(A, A) \otimes_{\mathbb{R}} \mathbf{No}$ that becomes infinitesimal under standard-part.
5. We show that $\xi$ is not in the image of any classical strict Hochschild representative. This establishes strict generalisation.

**Required infrastructure**:
- `standardPart_of_infinitesimal` (proved).
- Surreal-coefficient Hochschild cohomology (does not exist in mathlib).
- A specific cohomological computation distinguishing $\mathrm{HH}^1_{\mathbb{R}} \otimes \mathbf{No}$ from $\mathrm{HH}^1_{\mathbf{No}}$.

**Falsification path**: Prove that every infinitesimal element of $\mathrm{Hom}_{\mathbf{No}}(\mathbf{1}, \mathrm{Ad}(A))$ comes from a real element scaled by $\varepsilon$. If $\eta$ must vanish for $\xi$ to satisfy the original observability constraint, the relaxation is empty.

**Provability assessment**: Identical to [infinitesimal-frobenius](#conj:infinitesimal-frobenius). One side is trivial. The other requires deformation theory.
