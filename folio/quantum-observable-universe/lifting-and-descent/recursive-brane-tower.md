Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe over a ring $R$ with $A$ commutative; then every $T(A_n)$ is commutative as well. Set $A_0 = A$ and inductively $A_{n+1} = T(A_n) = \mathrm{Sym}_{A_n}(\Omega^1_{A_n/R})$, the tangent algebra of $A_n$ ([jet prolongation](#prop:jet-prolongation)), whose degree-$\le 1$ part is the [jet object](#def:categorical-jet) $J^1(A_n)$.

The **recursive brane tower** is the sequence
$$
  A_0 \hookrightarrow A_1 \hookrightarrow A_2 \hookrightarrow \cdots
$$
in $\mathbf{C}$, where each embedding is the structure map $\ell_n \colon A_n \hookrightarrow T(A_n) = A_{n+1}$. The augmentation $r_n\colon A_{n+1} \to A_n$, which kills $\Omega^1_{A_n/R}$, satisfies $r_n \circ \ell_n = \mathrm{id}$, so each level is a direct summand of the next.

The *brane relation* makes the structure recursive: each jet object $A_n$ is the base object — the *brane* — of $A_{n+1}$, and the comultiplication $\Delta_n$ on $A_n$ encodes the $n$-th level connection. For $A = \mathcal{O}(G)$ one has $A_n = \mathcal{O}(T^n G)$ and $\Delta_n$ is the comultiplication of the iterated tangent group; a Frobenius form on $A_n$, $n \ge 1$, is not established.
