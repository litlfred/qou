Let $K$ be a real-closed field extending $\mathbb{R}$ (typically $K = \mathbf{No}$, Conway's surreal numbers). Every element $x \in \mathbf{No}$ has a canonical birthday $b(x) \in \mathrm{Ord}$. This is the least ordinal stage at which $x$ is constructed in Conway's recursive $\{L \mid R\}$ presentation. Equivalently, $b(x)$ is the length of the sign-sequence representation for $x$:

$$
  b(0) = 0, \qquad b(n) = n \text{ for } n \in \mathbb{N}, \qquad b(\omega) = \omega, \qquad b(1/2) = 2, \qquad b(\pi) = \omega, \qquad b(\varepsilon) = \omega.
$$

The birthday function refines the archimedean norm. Distinct reals $x, y \in \mathbb{R} \subset \mathbf{No}$ have $b(x), b(y) \leq \omega$. The elements $\varepsilon$, $\omega$, and $\omega^2$ have progressively larger birthdays.

Let $\mathbf{C}$ be a $K$-linear category. A birthday grading on $\mathbf{C}$ is an ordinal-indexed filtration of each hom-space:

$$
  \mathrm{Hom}_{\mathbf{C}}(X, Y)_{\leq \alpha} = \bigl\{ f \in \mathrm{Hom}_{\mathbf{C}}(X, Y) : \text{every coefficient of } f \text{ has birthday} \leq \alpha \bigr\}.
$$

This filtration satisfies three properties:
1. **Exhaustiveness**: $\bigcup_\alpha \mathrm{Hom}_{\mathbf{C}}(X, Y)_{\leq \alpha} = \mathrm{Hom}_{\mathbf{C}}(X, Y)$.
2. **Composition**: If $f \in \mathrm{Hom}(X,Y)_{\leq \alpha}$ and $g \in \mathrm{Hom}(Y,Z)_{\leq \beta}$, then $g \circ f \in \mathrm{Hom}(X,Z)_{\leq \alpha \oplus \beta}$ (where $\oplus$ is the natural sum of ordinals).
3. **Monoidality**: If $\mathbf{C}$ is monoidal, $f \otimes g \in \mathrm{Hom}(X \otimes X', Y \otimes Y')_{\leq \alpha \oplus \beta}$.
