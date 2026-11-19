**Definition.**
*Let $K_0(\mathrm{Var}_k)$ be the **Grothendieck ring of varieties**
over the base field $k$ — the free abelian group on isomorphism
classes $[X]$ of $k$-varieties modulo the scissor relations
$[X] = [Z] + [X \setminus Z]$ for closed $Z \subseteq X$, with
product $[X] \cdot [Y] = [X \times Y]$. Let $\mathbb{L} = [\mathbb{A}^1_k]
\in K_0(\mathrm{Var}_k)$ denote the **Lefschetz motive**, and write
$\mathcal{M} := K_0(\mathrm{Var}_k)[\mathbb{L}^{-1}]$ for its
localization. The **motivic mass measure** of the QOU brane is the
Kontsevich--Denef--Loeser motivic measure*

$$
  \mu \;:\; \mathcal{B}(\mathcal{L}(X))
  \;\longrightarrow\;
  \widehat{\mathcal{M}}
$$

*on cylindrical (Borel) subsets of the
[arc space](#def:arc-space) $\mathcal{L}(X)$ of a brane variety $X$,
valued in the dimension-completion $\widehat{\mathcal{M}}$ of
$\mathcal{M}$. Volumes of measurable subsets are computed by*

$$
  \mu(A)
  \;=\;
  [\pi_n(A)] \;\mathbb{L}^{-(n+1)\dim X}
  \qquad
  (\pi_n \colon \mathcal{L}(X) \to \mathcal{L}_n(X)),
$$

*independently of $n$ once $A$ is stable at level $n$.*

*For a braid $\beta \in H_n(R, q)$ whose Gröbner--Shirshov reduction ([three-parameter Wedderburn formula](#thm:wedderburn-mass-formula)) blows up $X$ along its crossing loci, the **topological mass** of the reduced state is*

$$
  \mathfrak{m}_{\mathrm{mot}}(\beta)
  \;:=\;
  \int_{\mathcal{L}(X)} d\mu
  \;\in\;\widehat{\mathcal{M}}.
$$
