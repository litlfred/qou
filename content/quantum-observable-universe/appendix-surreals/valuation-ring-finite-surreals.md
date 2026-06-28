The [standard-part functor](#def:standard-part-functor)
$\mathrm{st} : \mathbf{No}_{\mathrm{fin}} \to \mathbb{R}$ admits a
clean ring-theoretic reading: **it is the quotient map of a
valuation ring.**

## Valuation ring structure

The **finite surreals** form a convex subring of $\mathbf{No}$:

$$
  \mathcal{O}
   := \{ x \in \mathbf{No} : \exists n \in \mathbb{N},\,
         -n < x < n \}
   = \{ x \in \mathbf{No} : \mathrm{IsFinite}(x) \}.
$$

The **infinitesimals** form its unique maximal ideal:

$$
  \mathfrak{m}
   := \{ x \in \mathcal{O} : \mathrm{IsInfinitesimal}(x) \}.
$$

The quotient

$$
  \mathcal{O} / \mathfrak{m} \;\xrightarrow{\sim}\; \mathbb{R}
$$

is canonically isomorphic to the real numbers, and the projection
$\mathcal{O} \twoheadrightarrow \mathcal{O}/\mathfrak{m}$ is exactly
$\mathrm{st}$.
