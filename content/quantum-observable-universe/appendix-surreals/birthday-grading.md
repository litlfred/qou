Let $K$ be a real-closed field extending $\mathbb{R}$ (typically
$K = \mathbf{No}$, Conway's surreal numbers). Every element
$x \in \mathbf{No}$ has a canonical **birthday**
$b(x) \in \mathrm{Ord}$ — the least ordinal stage at which $x$ is
constructed in Conway's recursive $\{L \mid R\}$ presentation
[@conway1976]. Equivalently, $b(x)$ is the length of $x$'s
sign-sequence representation [@gonshor1986]:

$$
  b(0) = 0, \qquad
  b(n) = n \text{ for } n \in \mathbb{N}, \qquad
  b(\omega) = \omega, \qquad
  b(1/2) = 2, \qquad
  b(\pi) = \omega, \qquad
  b(\varepsilon) = \omega.
$$

The birthday function refines the archimedean norm: if $x, y \in
\mathbb{R} \subset \mathbf{No}$ are distinct reals then $b(x), b(y)
\leq \omega$, but $\varepsilon$, $\omega$, and $\omega^2$ have
progressively larger birthdays.

## Definition

Let $\mathbf{C}$ be a $K$-linear category (enriched over $K$-modules).
A **birthday grading** on $\mathbf{C}$ is an ordinal-indexed
filtration of each hom-space

$$
  \mathrm{Hom}_{\mathbf{C}}(X, Y)_{\leq \alpha}
  \;=\; \bigl\{ f \in \mathrm{Hom}_{\mathbf{C}}(X, Y) :
         \text{every coefficient of } f \text{ has birthday} \leq \alpha \bigr\}
$$

indexed by ordinals $\alpha$, such that:

1. **Exhaustiveness**:
   $\bigcup_\alpha \mathrm{Hom}_{\mathbf{C}}(X, Y)_{\leq \alpha}
    = \mathrm{Hom}_{\mathbf{C}}(X, Y)$.
2. **Compatibility with composition**:
   $f \in \mathrm{Hom}(X,Y)_{\leq \alpha}$ and
   $g \in \mathrm{Hom}(Y,Z)_{\leq \beta}$
   implies
   $g \circ f \in \mathrm{Hom}(X,Z)_{\leq \alpha \oplus \beta}$
   (natural-sum of ordinals).
3. **Compatibility with tensor** (if $\mathbf{C}$ is monoidal):
   $f \otimes g \in \mathrm{Hom}(X \otimes X', Y \otimes Y')_{\leq
   \alpha \oplus \beta}$.

## Archimedean sub-category

The sub-category with all hom-spaces in birthday $\leq \omega$ is
exactly the **archimedean-coefficient sub-category** — morphisms
whose coefficients are real numbers. For $\mathbf{C} =
\mathrm{Rep}_{\mathbf{No}}(\mathrm{SU}_q(2))$ with $q \in \mathbb{R}
\subset \mathbf{No}$, this recovers $\mathrm{Rep}_{\mathbb{R}}(\mathrm{SU}_q(2))$
up to the caveat that $\mathbf{No}$'s arithmetic *restricted to
birthday $\leq \omega$* coincides with $\mathbb{R}$'s arithmetic
only on the archimedean part.

## Example: substrate parameter at $q = 1 + \varepsilon$

Set $q = 1 + \varepsilon$ for infinitesimal $\varepsilon \in
\mathbf{No}$ with $b(\varepsilon) = \omega$ (its sign sequence
$(+, -, -, -, \ldots)$ has length $1 + \omega = \omega$). Then:

- $c_q = 1/(q - 1) = 1/\varepsilon = \omega$ has birthday $\omega$.
- $\hbar_q = (q-1)/q = \varepsilon(1 + \varepsilon)^{-1}$ has
  birthday $\omega$.
- $d_H(q) = (2q-1)^2/q^3 = (1 + 2\varepsilon)^2(1 + \varepsilon)^{-3}$
  has birthday $\omega$.

In general, expressions rational in $q$ at $q = 1 + \varepsilon$
live in the birthday-$\leq \omega$ stratum, embedded in the
Laurent-series field $\mathbb{R}(\!(\varepsilon)\!)$. The
finite-vs-infinitesimal distinction within this stratum is
determined by the standard-part map, **not** by birthday alone:
limit reals like $\pi$ also have birthday $\omega$.

## Role in the appendix

The birthday grading gives a coarse "how transfinite" depth gauge.
Statements with all hom-coefficients of birthday $< \omega$
involve only dyadic rationals; birthday-$\leq \omega$ statements
include limit reals and first-order infinitesimals; birthday
$> \omega$ statements use named infinities like $\omega$ itself
or transseries terms like $\log \omega$.

The appendix's relaxed axioms
([infinitesimal Frobenius](#conj:infinitesimal-frobenius)) all
allow corrections of the form $\mathrm{id} + O(\varepsilon)$,
which live at birthday $\leq \omega$ but are distinguished from
classical $\mathrm{id}$ by having non-zero standard-part of the
$\varepsilon$-coefficient.
