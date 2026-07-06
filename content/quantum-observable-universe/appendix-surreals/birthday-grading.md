The birthday grading provides a coarse "how transfinite" depth gauge for morphisms in surreal-enriched categories. It stratifies formal parameters into nested levels of infinitesimal and transfinite resolution. Statements with all hom-coefficients of birthday $< \omega$ involve only dyadic rationals. Birthday-$\leq \omega$ statements include limit reals and first-order infinitesimals. Birthday $> \omega$ statements use named infinities like $\omega$ itself or transseries terms like $\log \omega$.

Let $K$ be a real-closed field extending $\mathbb{R}$ (typically $K = \mathbf{No}$, Conway's surreal numbers). Every element $x \in \mathbf{No}$ has a canonical **birthday** $b(x) \in \mathrm{Ord}$. This is the least ordinal stage at which $x$ is constructed in Conway's recursive $\{L \mid R\}$ presentation [@conway1976]. Equivalently, $b(x)$ is the length of the sign-sequence representation for $x$ [@gonshor1986]:

$$
  b(0) = 0, \qquad
  b(n) = n \text{ for } n \in \mathbb{N}, \qquad
  b(\omega) = \omega, \qquad
  b(1/2) = 2, \qquad
  b(\pi) = \omega, \qquad
  b(\varepsilon) = \omega.
$$

The birthday function refines the archimedean norm. Distinct reals $x, y \in \mathbb{R} \subset \mathbf{No}$ have $b(x), b(y) \leq \omega$. The elements $\varepsilon$, $\omega$, and $\omega^2$ have progressively larger birthdays.

## Example: Substrate Parameter at $q = 1 + \varepsilon$

Consider $q = 1 + \varepsilon$ for an infinitesimal $\varepsilon \in \mathbf{No}$ with $b(\varepsilon) = \omega$. Its sign sequence $(+, -, -, -, \ldots)$ has length $1 + \omega = \omega$. The associated parameters resolve as follows:

- $c_q = 1/(q - 1) = 1/\varepsilon = \omega$ has birthday $\omega$.
- $\hbar_q = (q-1)/q = \varepsilon(1 + \varepsilon)^{-1}$ has birthday $\omega$.
- $d_H(q) = (2q-1)^2/q^3 = (1 + 2\varepsilon)^2(1 + \varepsilon)^{-3}$ has birthday $\omega$.

Expressions rational in $q$ evaluated at $q = 1 + \varepsilon$ remain in the birthday-$\leq \omega$ stratum. They embed into the Laurent-series field $\mathbb{R}(\!(\varepsilon)\!)$. The standard-part map determines the distinction between finite and infinitesimal within this stratum. The birthday alone does not distinguish them, as limit reals like $\pi$ also have birthday $\omega$.

## Definition

Let $\mathbf{C}$ be a $K$-linear category (enriched over $K$-modules). A **birthday grading** on $\mathbf{C}$ is an ordinal-indexed filtration of each hom-space:

$$
  \mathrm{Hom}_{\mathbf{C}}(X, Y)_{\leq \alpha}
  \;=\; \bigl\{ f \in \mathrm{Hom}_{\mathbf{C}}(X, Y) :
         \text{every coefficient of } f \text{ has birthday} \leq \alpha \bigr\}.
$$

This filtration satisfies three properties:

1. **Exhaustiveness**: $\bigcup_\alpha \mathrm{Hom}_{\mathbf{C}}(X, Y)_{\leq \alpha} = \mathrm{Hom}_{\mathbf{C}}(X, Y)$.
2. **Composition**: If $f \in \mathrm{Hom}(X,Y)_{\leq \alpha}$ and $g \in \mathrm{Hom}(Y,Z)_{\leq \beta}$, then $g \circ f \in \mathrm{Hom}(X,Z)_{\leq \alpha \oplus \beta}$ (where $\oplus$ is the natural sum of ordinals).
3. **Monoidality**: If $\mathbf{C}$ is monoidal, $f \otimes g \in \mathrm{Hom}(X \otimes X', Y \otimes Y')_{\leq \alpha \oplus \beta}$.

## Archimedean Sub-category

The sub-category defined by $b(f) \leq \omega$ forms the **archimedean-coefficient sub-category**. Its morphisms have coefficients that are real numbers or bounded infinitesimals. For $\mathbf{C} = \mathrm{Rep}_{\mathbf{No}}(\mathrm{SU}_q(2))$ with $q \in \mathbb{R} \subset \mathbf{No}$, this recovers $\mathrm{Rep}_{\mathbb{R}}(\mathrm{SU}_q(2))$. The arithmetic of $\mathbf{No}$ restricted to birthday $\leq \omega$ coincides with $\mathbb{R}$ exactly on the archimedean part.

The relaxed axioms in this appendix ([infinitesimal Frobenius](#conj:infinitesimal-frobenius)) allow corrections of the form $\mathrm{id} + O(\varepsilon)$. These corrections live at birthday $\leq \omega$ but are distinguished from the classical $\mathrm{id}$ by having a non-zero standard part for the $\varepsilon$-coefficient.
