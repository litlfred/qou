Let $(\mathcal{C}, \otimes, \mathbf{1})$ be a
[rigid monoidal category](#def:rigid-monoidal-category) with fundamental
object $V$ and Frobenius algebra $(A, \mu, \eta, \Delta, \epsilon,
\int_A)$. A *categorical hadron* is a morphism

$$
  h \colon \mathbf{1} \;\longrightarrow\; V^{\otimes n}
$$

for some $n \geq 2$, subject to the constraint that $h$ factors through
the image of the multiplication $\mu$ restricted to simple
constituents — that is, $h$ lies in the span of morphisms of the form

$$
  \mathbf{1} \xrightarrow{\;\eta\;}
  A \xrightarrow{\;\Delta^{(n-1)}\;}
  A^{\otimes n} \xrightarrow{\;\pi_{j_1} \otimes \cdots \otimes \pi_{j_n}\;}
  V_{j_1} \otimes \cdots \otimes V_{j_n}
$$

where each $\pi_{j_i}$ is the projection onto the simple summand
$V_{j_i} \hookrightarrow A$, and the $V_{j_i}$ are simple objects of
$\mathcal{C}$.

The integer $n$ is the *valence* of the hadron. A categorical hadron
of valence $3$ is a *categorical baryon*; valence $2$ is a
*categorical meson*.

This definition is purely categorical: it lives in $\mathcal{C}$
without reference to a base point, coordinates, or a specific gauge
group. The [concrete hadron](#def:hadron) of Chapter 3 is obtained by
composing a categorical hadron with localization to a
[categorical point](#def:categorical-point).
