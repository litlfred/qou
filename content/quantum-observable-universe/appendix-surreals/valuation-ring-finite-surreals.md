The finite surreals form a **convex subring** of $\mathbf{No}$:

$$
  \mathcal{O}
   := \{ x \in \mathbf{No} : \exists n \in \mathbb{N},\,
         -n < x < n \}.
$$

The infinitesimals form the **maximal ideal**:

$$
  \mathfrak{m}
   := \{ x \in \mathcal{O} : \forall n \in \mathbb{N},\,
         -1/n < x < 1/n \}
   = \{ x \in \mathcal{O} : \mathrm{IsInfinitesimal}(x) \}.
$$

## Properties

$\mathcal{O}$ is a **valuation ring** in the algebraic sense:

1. $\mathcal{O}$ is a local ring with maximal ideal $\mathfrak{m}$.
2. The quotient

   $$
     \mathcal{O} / \mathfrak{m} \;\xrightarrow{\sim}\; \mathbb{R}
   $$

   is canonically isomorphic to the real numbers.

3. The projection $\mathcal{O} \twoheadrightarrow \mathcal{O}/\mathfrak{m}
   \cong \mathbb{R}$ is Robinson's **standard-part map**
   ([standard-part functor](#def:standard-part-functor))
   $\mathrm{st} : \mathcal{O} \to \mathbb{R}$.

4. $\mathcal{O}$ is a **set-sized** subring of $\mathbf{No}$ (though
   $\mathbf{No}$ itself is a proper class).

5. $\mathcal{O}$ is convex for the surreal order: if
   $x < z < y$ with $x, y \in \mathcal{O}$ then $z \in \mathcal{O}$.

6. The infinite surreals $\mathbf{No} \setminus \mathcal{O}$ are
   **not** in the domain of $\mathrm{st}$. Any arithmetic involving
   $\omega$, $\omega^2$, $\omega^\omega$ must be restricted to
   $\mathcal{O}$ before applying standard-part.

## Why this matters

The valuation ring is the **set-theoretic rescue** for the surreal
lift:

- Constructions that need a set-sized coefficient ring (categorical
  enrichments, module structures, scheme evaluations) can be
  performed over $\mathcal{O}$ instead of $\mathbf{No}$.
- The archimedean limit is the quotient map
  $\mathcal{O} \twoheadrightarrow \mathcal{O}/\mathfrak{m} \cong \mathbb{R}$.
- The escape-to-infinity problem (where do surreals $> n$ go
  under standard-part?) is **solved by restriction**: the
  standard-part is only defined on $\mathcal{O}$, and there is no
  silent extension to $\mathbf{No} \setminus \mathcal{O}$.

See [functor-of-points for surreals](#def:functor-of-points-surreal)
for how this pairs with Grothendieck's functorial framework to give
a proper-class-free treatment of surreal geometry.

## Relation to Hahn-series substrate

The conjectural Hahn-series substrate
([Hahn substrate](#conj:hahn-substrate)) lives entirely inside
$\mathcal{O}$: every element

$$
  q \;=\; 1 + \varepsilon + \alpha_2 \varepsilon^2 + \cdots
$$

satisfies $|q - 1| < 1$ in the surreal ordering (all
$\alpha_k \varepsilon^k$ are infinitesimal for $k \geq 1$).
So the entire substrate-parameter discussion of the appendix
lives in the valuation ring and projects cleanly to $\mathbb{R}$
via standard-part.
