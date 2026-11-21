**Proposition.** The idempotency below is proved unconditionally, for every $n$, at generic $q$ ([The Murphy–Lagrange elements $e_\lambda$ are the central primitive idempotents of $H_n(q)$](#thm:explicit-central-idempotent-cross-checks)).

*Let $H_n(q)$ be the Iwahori–Hecke algebra over a field $K$ at generic $q$ ($q \neq 0$, not a root of unity). The Jucys–Murphy elements $\{J_1, \ldots, J_n\} \subset H_n(q)$ commute pairwise and act diagonally on the Hoefsmit seminormal basis. For any standard Young tableau $T$ of shape $\lambda \vdash n$, one has $J_k \cdot v_T = c_T(k; q) \cdot v_T$, where*

$$
  c_T(k; q) \;=\; q^{\,2(j(k) - i(k))}
$$

*is the $q$-content of the box containing $k$ at row $i(k)$ and column $j(k)$.*

*The central primitive idempotent $e_\lambda \in Z(H_n(q))$ projecting onto the $\lambda$-Wedderburn block carries the explicit formula:*

$$
  \boxed{\;
    e_\lambda \;=\; \sum_{T \in \mathrm{SYT}(\lambda)}
    \prod_{k=1}^{n}
    \prod_{\substack{c \in \mathrm{C}(n) \\ c \neq c(T(k); q)}}
    \frac{J_k - c}{c(T(k); q) - c},
  \;}
$$

*where $\mathrm{C}(n) := \{c(\square; q) : \square \in \mu,\; \mu \vdash n\}$ comprises the distinct $q$-contents arising across every partition $\mu \vdash n$. The inner product excludes the eigenvalue $c(T(k); q)$. Each factor forms a Lagrange-interpolation projector onto the eigenspace where $J_k = c(T(k); q)$. This construction completely specifies $Z(H_n(q))$.*

## Cross-checks

1. **Sum-to-identity.** $\sum_{\lambda \vdash n} e_\lambda = 1 \in H_n(q)$, confirming the completeness of the partition decomposition.
2. **Orthogonality.** $e_\lambda e_\mu = \delta_{\lambda \mu} e_\lambda$ via Lagrange interpolation in commuting variables.
3. **Bar-invariance.** The bar involution ($\sigma_i \mapsto \sigma_i^{-1}$, $q \mapsto q^{-1}$) fixes every $e_\lambda$, self-conjugate or not.
4. **Conjugate pairing.** The sign twist ($\sigma_i \mapsto -\sigma_i^{-1}$) sends $e_\lambda$ to $e_{\lambda'}$. The bar involution does not pair $\lambda$ with $\lambda'$.

## Small $n$ examples

| $n$ | $\lambda$ | conjugation class | $e_\lambda$ structure |
|---|---|---|---|
| $2$ | $(2)$ | chiral pair w/ $(1,1)$ | $\frac{L_2 - q^{-2}}{q^2 - q^{-2}} = \frac{\sigma_1 + q^{-1}}{q + q^{-1}}$ |
| $2$ | $(1,1)$ | chiral pair w/ $(2)$ | $\frac{L_2 - q^{2}}{q^{-2} - q^2} = \frac{q - \sigma_1}{q + q^{-1}}$ |
| $3$ | $(3)$ | chiral pair w/ $(1,1,1)$ | $q$-deformed symmetriser |
| $3$ | $(2,1)$ | self-conjugate | standard 2D representation idempotent |
| $4$ | $(2,2)$ | self-conjugate | bar-fixed; witnesses $\mathrm{Vol}(4_1)$ via depth-2 pairing with $\mathrm{Li}_2^q(\zeta_6)$ |

## Provenance

The Murphy-element diagonalization of $Z(H_n(q))$ originates with Murphy (1981, symmetric group) and Dipper–James (1986, Hecke algebra). The Lagrange-interpolation form offers the cleanest computable expression. It is standard in computer-algebra implementations of Hecke algebras.
