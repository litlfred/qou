We define the **classical limit** as a :refterm[monoidal functor]{#monoidal-functor}

$$
\mathcal{L} : \mathbf{C}_q \longrightarrow \mathbf{C}_1
$$

from the :refterm[braided monoidal category]{#braided-monoidal-category} $\mathbf{C}_q$ (at deformation parameter $q$) to the :refterm[symmetric monoidal category]{#symmetric-monoidal-category} $\mathbf{C}_1$ (at $q = 1$). The functor $\mathcal{L}$ acts on the substrate algebra via three mechanisms:

1. **Quantum gap collapse**: The parameter $\hbar_q = 1 - q^{-1}$ goes to $0$. This eliminates non-commutativity.
2. **Differential smoothing**: The Jackson $q$-derivative $d_q f(z) = \frac{f(qz) - f(z)}{(q-1)z}$ converges to the ordinary derivative $\frac{df}{dz}$.
3. **Braiding trivialization**: The braiding $\sigma_{X,Y} : X \otimes Y \to Y \otimes X$ specializes to the symmetric swap $\tau_{X,Y}$. This occurs because $R(q) \to \mathrm{id}$ as $q \to 1$.

The functor $\mathcal{L}$ is exact, preserving short exact sequences. It is **not** full. The limit loses quantum information.
