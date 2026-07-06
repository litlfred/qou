**Definition (algebraic primality).**
Fix a substrate $q > 1$. For each strand count $n \geq 1$ the
confinement SDP selects a canonical state $\psi_n(q)$. Say that $n$ is
**algebraically prime at $q$** if $\psi_n(q)$ is *not* contained in
the closed span of any non-trivial tensor product

$$
  \overline{\mathrm{span}}\bigl\{\,
    \psi_{n_1}(q) \otimes \cdots \otimes \psi_{n_k}(q)
  \,\bigr\},
$$

indexed by a decomposition $n = n_1 + \cdots + n_k$ with $k \geq 2$
and every $n_i \geq 1$.

By convention $n = 0$ (the vacuum) is *not* prime. The predicate is
the framework's purely algebraic surrogate for a **magic** strand
count: a configuration that does not factor through a product of
smaller closed configurations.

The definition is recursive in the decomposition argument — testing
primality at $n$ ranges over all decompositions into smaller parts,
each of which is itself built from canonical states $\psi_{n_i}(q)$.
The recursion bottoms out at $n = 1$, which is algebraically prime
*vacuously* — no decomposition into $k \geq 2$ positive parts can sum
to $1$ ([vacuous primality at $n = 1$](#prop:n-equals-1-vacuous-magic)).

The conjecture that, at the substrate value $q_0$, the algebraically
prime integers coincide with the empirical magic ladder
$\{1, 2, 8, 20, 28, 50, 82, 126\}$ is stated separately; the present
definition fixes only the predicate, not its value at any particular
$q$.
