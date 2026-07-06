**Proposition (Color and spacetime are orthogonal factors of the Bring Galois group).**
*Let $K$ be a Bring-embeddable knot, evaluated through the categorical Markov trace $\mathrm{tr}_M$ on the Hecke algebra $H_2(q) \oplus H_3(q)$. The $2+3=5$ irreducible representations constitute the Bring fivefold. Bring's five homogeneous coordinates split as spacetime $(x_0, x_1)$ and color $(x_2, x_3, x_4)$. The substrate Galois group $S_5$ contains the block-diagonal product $S_2 \times S_3$. Then:*

1. *The factorization $S_2 \times S_3 \hookrightarrow S_5$ is faithful.*
2. *The color factor $S_3$ fixes every spacetime coordinate, and the spacetime factor $S_2$ fixes every color coordinate. The two sectors are orthogonal.*
3. *Every additive homomorphism from the connected phase parameter $\mathbb{R}$ to a finite group is trivial.*

## A single trace object

The embeddable strand counts dictate a single trace algebra $H_2(q) \oplus H_3(q)$ carrying $2+3=5$ irreducible representations ([`prop:cohomological-embedding`](#prop:cohomological-embedding)). These match Bring's five homogeneous coordinates, partitioned into a rank-two spacetime block and a rank-three color block ([`brings-qou-4tuple`](../brings-surface/brings-qou-4tuple.md)). We record the color content of an embedded photon as an element of $H_3(q)$, where the generators $\sigma_0, \sigma_1$ serve as the color axes ([`knot-basis-color-content`](../brings-surface/knot-basis-color-content.md)). Color is therefore a grading on the trace algebra itself, rather than a separate object.

The substrate symmetry $S_5$ acts on all five coordinates. Its block-diagonal subgroup $S_2 \times S_3$ permutes spacetime and color separately. The $S_3$ permutes the three color sheets while preserving spacetime ([`color-sector-coords`](../brings-surface/color-sector-coords.md), [`rem:chirality-trefoil`](#rem:chirality-trefoil)). The $S_2$ permutes the two spacetime coordinates while preserving color. Parts (1) and (2) formalize this: the product embeds faithfully, and each factor fixes the opposing sector pointwise. Color and spacetime function as independent coordinates on a single object. They couple only through $S_5$ elements outside $S_2 \times S_3$, which rotate spacetime indices into color indices.

## Discreteness

Part (3) enforces rigidity on the continuous sector. The connected group $\mathbb{R}$ is divisible, so any homomorphism to a finite group $G$ vanishes: for each $x$, $f(x) = f\big(|G| \cdot \tfrac{x}{|G|}\big) = |G| \cdot f(\tfrac{x}{|G|}) = 0$, because $|G| \cdot g = 0$ for every $g \in G$. A continuous winding parameter cannot carry a finite-group (e.g. $\mu_5$) character. Physically, this dictates that the continuous trace phase is not the discrete color charge ([`rem:mass-modulus-em-phase-color-grading`](#rem:mass-modulus-em-phase-color-grading)).

## Lean formalism

These claims are formalized without `sorry` in [`QOU.MassEndomorphism`](color-spacetime-s5-factorization.lean) via `spacetime_color_card`, `colorSpacetimeEmbed_injective`, `color_fixes_spacetime`, `spacetime_fixes_color`, and `winding_hom_to_finite_trivial`. The construction is generic. The embedding and divisibility arguments rely strictly on combinatorial data, requiring no archimedean input.
