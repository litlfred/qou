Simple objects are the irreducible building blocks of a rigid :refterm[monoidal category]{#monoidal-category} $\mathbf{C}$. An object $X$ is simple if every monomorphism into $X$ is zero or an isomorphism.

The faithful, exact functor $\tau$ reflects simplicity: $X$ is simple if and only if $\tau(X)$ is a simple module. The fundamental object $V$ is distinguished by two properties:

1. **Categorical dimension $2$**: $\tau(V)$ is a rank-$2$ free module.
2. **Tensor generation**: Every simple object appears as a direct summand of some tensor power $V^{\otimes n}$.
