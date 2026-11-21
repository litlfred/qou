**Definition (algebraic primality).**
*Fix a substrate parameter $q > 1$. For each strand count $n \geq 1$, the confinement SDP selects a canonical state $\psi_n(q)$. Say that $n$ is **algebraically prime at $q$** if $\psi_n(q)$ is not contained in the closed span of any non-trivial tensor product*

$$
  \overline{\mathrm{span}}\bigl\{\,
    \psi_{n_1}(q) \otimes \cdots \otimes \psi_{n_k}(q)
  \,\bigr\}.
$$

*This product is indexed by a decomposition $n = n_1 + \cdots + n_k$ with $k \geq 2$ and every $n_i \geq 1$.*

By convention, $n = 0$ is not prime. This predicate serves as a purely algebraic surrogate for a magic strand count. An algebraically prime configuration does not factor into a product of smaller closed configurations.

The definition relies on a recursive decomposition argument. Testing primality at $n$ checks all decompositions into smaller parts. The recursion bottoms out at $n = 1$. The $n=1$ state is algebraically prime vacuously, because no decomposition into $k \geq 2$ positive parts sums to $1$.
