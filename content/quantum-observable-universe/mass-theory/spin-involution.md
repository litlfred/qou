**Definition (spin involution on a Frobenius $*$-algebra).**
*Let $(A, \tau, {}^*)$ be a Frobenius $*$-algebra over a commutative ring $R$. A spin involution on $(A, \tau, {}^*)$ is an $R$-linear map $\sigma : A \to A$ satisfying:*

1. *Involution: $\sigma \circ \sigma = \mathrm{id}_A$.*
2. *Anti-multiplicative: $\sigma(a b) = \sigma(b)\, \sigma(a)$ for all $a, b \in A$.*
3. *Trace-invariant: $\tau \circ \sigma = \tau$.*
4. *$*$-compatible: $\sigma(a^*) = \sigma(a)^*$ for all $a$.*

*The $\mathbb{Z}/2$ grading $A = A_+ \oplus A_-$ by $\sigma$-eigenvalue defines the spin grading. The space $A_+$ is the spin-singlet sector and $A_-$ is the spin-doublet sector.*

When applying the $A_\pm$ projections, assume $2 \in R^\times$. Without this hypothesis, the projections $a_\pm := \tfrac{1}{2}(a \pm \sigma(a))$ are ill-defined.

Every $a \in A$ has the canonical decomposition $a = a_+ + a_-$. The isospin third-component evaluates on $\sigma$-eigenvectors as:

$$
  T_3(a) \;=\; \tfrac{1}{2}\,\mathrm{sgn}_\sigma(a)
  \;\in\; \{-\tfrac{1}{2},\, 0,\, +\tfrac{1}{2}\}.
$$

For a general $a \in A$, read $T_3$ off the $A_\pm$-projection $a = a_+ + a_-$. The derived spin grading secures the additive homomorphism properties, the orthogonality of the sectors $A_+ \cap A_- = 0$, and the explicit mapping $2\,T_3 = \mathrm{sgn}_\sigma$.
