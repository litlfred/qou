Define the **classical limit** as a :refterm[monoidal functor]{#monoidal-functor}

$$
\mathcal{L} : \mathbf{C}_q \longrightarrow \mathbf{C}_1
$$

from the :refterm[braided monoidal category]{#braided-monoidal-category} $\mathbf{C}_q$ (at deformation
parameter $q$) to the :refterm[symmetric monoidal category]{#symmetric-monoidal-category} $\mathbf{C}_1$
(at $q = 1$). The functor $\mathcal{L}$ acts on the substrate
algebra by:

1. **Quantum gap collapse**: $\hbar_q = 1 - q^{-1} \to 0$, so that
 the non-commutativity vanishes.
2. **Differential smoothing**: The Jackson $q$-derivative
 $d_q f(z) = \frac{f(qz) - f(z)}{(q-1)z}$ converges to the
 ordinary derivative $\frac{df}{dz}$.
3. **Braiding trivialization**: The braiding
 $\sigma_{X,Y} : X \otimes Y \to Y \otimes X$ specializes to the
 symmetric swap $\tau_{X,Y}$, since $R(q) \to \mathrm{id}$ as
 $q \to 1$.

The functor $\mathcal{L}$ is exact (preserves short exact sequences)
but **not** full: quantum information is lost in the limit.
