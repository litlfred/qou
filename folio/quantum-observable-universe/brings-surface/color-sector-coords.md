With notation as in [exceptional divisor](#def:exceptional-divisor), fix the aether parameter $q$ ([aether parameter](#def:substrate-parameter)) and set $\phi \in [0,\pi]$, $\psi \in [0, 2\pi/3]$. Define the **color sector coordinates** — the **red**, **green**, and **blue** sector embeddings — by

```tex
\begin{align*}
  \mathfrak{r}(\phi,\psi)
  &=  O + R\bigl(\sin\phi \bigl(\cos(\psi + q\phi) T_1
         + \sin(\psi + q\phi) T_2\bigr) - \cos\phi N\bigr),\\
  \mathfrak{g}(\phi,\psi)
  &=  \mathfrak{r}\!\bigl(\phi,\psi + \tfrac{2\pi}{3}\bigr),\\
  \mathfrak{b}(\phi,\psi)
  &=  \mathfrak{r}\!\bigl(\phi,\psi + \tfrac{4\pi}{3}\bigr).
\end{align*}
```

The *color twist* $q\phi$ rotates each sector by $q$ full turns as the latitude $\phi$ runs from the south pole ($0$) to the north pole ($\pi$). This encodes the chirality of the aether parameter.

The three sectors tile the exceptional divisor precisely:

$$
  \mathcal{S}_p =  \mathfrak{r}(p) \cup \mathfrak{g}(p) \cup \mathfrak{b}(p).
$$

Adjacent sectors share only their boundary meridians (at $\psi = 0$ and $\psi = 2\pi/3$ in each sector's local coordinate). The union covers $\mathcal{S}_p$ without overlap. The three sectors correspond to the three copies of $S_3 \subset S_5$ in [chirality and trefoil](#rem:chirality-trefoil): $\mathfrak{r}$ constitutes the first, $\mathfrak{g}$ the second, and $\mathfrak{b}$ the third.
