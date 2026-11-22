[Positive-definiteness](#prop:positive-definite-dagger) is checked here in $\mathbf{Rep}(\mathrm{SU}(2))$.

**The dagger involution.** On $\mathbf{Rep}(\mathrm{SU}(2))$, the dagger sends $f \colon V \to W$ to its conjugate transpose $f^\dagger = \bar{f}^{T} \colon W \to V$.

**Positive-definiteness on $V = \mathbb{C}^2$.** The fundamental representation $V = \mathbb{C}^2$ carries the standard Hermitian inner product $\langle v, w \rangle = v^\dagger w$. The $\mathrm{SU}(2)$-action preserves this inner product.

For any endomorphism $f \colon V \to V$, the composite $f^\dagger f$ satisfies:

$$
\langle f^\dagger f  v, v \rangle = \| f v \|^2 \geq 0.
$$

Thus $f^\dagger f$ has real non-negative eigenvalues. By Schur's lemma, $f = \lambda \mathrm{id}$, forcing $f^\dagger f = |\lambda|^2 \mathrm{id}$. 

**Interpretation.** Positive-definiteness makes $\mathbf{Rep}(\mathrm{SU}(2))$ a $C^*$-tensor category. This is the categorical shadow of the compactness of $\mathrm{SU}(2)$.
