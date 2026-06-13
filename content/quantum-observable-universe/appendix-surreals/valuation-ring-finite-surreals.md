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

## Why this framing matters

The appendix's functorial constructions (point-evaluation of
schemes, categorical enrichments, surreal-coefficient sheaves)
all need a **set-sized** coefficient ring to avoid proper-class
pathologies. The valuation ring $\mathcal{O}$ is set-sized; the
ambient $\mathbf{No}$ is a proper class. By restricting to
$\mathcal{O}$ before any point-evaluation, we stay inside
standard set-theoretic foundations.

The infinite surreals $\mathbf{No} \setminus \mathcal{O}$ are **not
in the domain of $\mathrm{st}$**. Any arithmetic involving
$\omega, \omega^2, \omega^\omega$ must be restricted to
$\mathcal{O}$ before projecting. This is not a loss: it is
exactly the archimedean-observability boundary already implicit
in the main paper's treatment of physical observables.

## Connection to points-and-topology framework

The main paper develops the points-and-topology framework for
QOU in its categorical-foundations chapters. This remark
specialises that framework to the surreal setting:

- Main paper: points of a categorical structure live in an
  $R$-algebra for some coefficient ring $R$.
- Surreal appendix: the natural choice is $R = \mathcal{O}$
  (finite surreals), with the archimedean quotient recovering
  $R = \mathbb{R}$.

No new framework is introduced here; this remark records that
the Robinson standard-part construction fits the same
categorical framework already in use.
