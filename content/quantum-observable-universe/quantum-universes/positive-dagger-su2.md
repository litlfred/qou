We verify [positive-definiteness of the dagger](#prop:positive-definite-dagger)
concretely in $\mathbf{Rep}(\mathrm{SU}(2))$, continuing the running example
from [SU(2) as a quantum universe](#ex:quantum-universe-su2).

**The dagger involution.** On $\mathbf{Rep}(\mathrm{SU}(2))$, the dagger
sends a morphism $f \colon V \to W$ of representations to its conjugate
transpose:

$$
f^\dagger = \bar{f}^{T} \colon W \to V.
$$

This is well-defined because $\mathrm{SU}(2)$ acts by unitary matrices:
if $f$ intertwines the $\mathrm{SU}(2)$-action, so does
$\bar{f}^{T}$.

**Positive-definiteness on $V = \mathbb{C}^2$.** The fundamental
representation $V = \mathbb{C}^2$ carries the standard Hermitian inner
product $\langle v, w \rangle = v^\dagger w$. The $\mathrm{SU}(2)$-action
preserves this inner product by definition: for $g \in \mathrm{SU}(2)$,

$$
\langle gv, gw \rangle = (gv)^\dagger (gw) = v^\dagger g^\dagger g  w
= v^\dagger w = \langle v, w \rangle.
$$

Now take any endomorphism $f \colon V \to V$ in
$\mathbf{Rep}(\mathrm{SU}(2))$. The composite $f^\dagger f$ satisfies:

$$
\langle f^\dagger f  v, v \rangle
= \langle f  v, f  v \rangle
= \| f v \|^2 \geq 0
$$

for all $v \in V$. Hence $f^\dagger f$ has real non-negative eigenvalues,
and $\langle f^\dagger f  v, v \rangle = 0$ only when $f v = 0$.

**Concretely, Schur's lemma pins $f$ down.** Writing $f$ as a
$2 \times 2$ matrix, irreducibility of the fundamental representation
forces $f = \lambda  \mathrm{id}$ for some $\lambda \in \mathbb{C}$,
so that:

$$
f^\dagger f = \bar{\lambda} \lambda  \mathrm{id}
= |\lambda|^2  \mathrm{id},
$$

which is manifestly non-negative — and for a reducible
$V = V_1 \oplus V_2$ the same bound applies block-diagonally on each
irreducible summand.

**Interpretation.** Positive-definiteness of the dagger means
$\mathbf{Rep}(\mathrm{SU}(2))$ is a $C^*$-tensor category: every
endomorphism has a well-defined "squared norm" $f^\dagger f \geq 0$.
This is the categorical shadow of the fact that $\mathrm{SU}(2)$ is
a *compact* group — compactness ensures the existence of a
positive-definite invariant inner product on every finite-dimensional
representation.

**Prerequisites:** complex numbers, Hermitian inner products,
eigenvalues.
