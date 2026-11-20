**Theorem.** *Let $H_n(q)$ be the Iwahori–Hecke algebra over a field $K$ of any characteristic at generic $q$ ($q \neq 0$, not a root of unity), and let*

$$
  e_\lambda \;=\; \sum_{T \in \mathrm{SYT}(\lambda)} \; \prod_{k=1}^{n} \; \prod_{\substack{|d| \le n-1 \\ d \neq c_T(k)}} \frac{J_k - q^{2d}}{q^{2 c_T(k)} - q^{2d}}
$$

*be the Murphy–Lagrange element attached to a partition $\lambda \vdash n$, built from the Jucys–Murphy elements $J_1, \ldots, J_n$, where $c_T(k)$ is the content $j - i$ of the box of $T$ holding $k$ and $q^{2 c_T(k)}$ is its $q$-content. The inner product runs over every content $d$ a box of a partition of $n$ can have, so each factor is a Lagrange projector onto the eigenvalue $q^{2 c_T(k)}$ of $J_k$. Let $x \mapsto \overline{x}$ be the bar involution ($\sigma_i \mapsto \sigma_i^{-1}$, $q \mapsto q^{-1}$, antilinear) and $\#$ the sign twist ($\sigma_i \mapsto -\sigma_i^{-1}$, $q$ fixed). Then the four cross-checks*

1. *sum-to-identity — $\sum_{\lambda \vdash n} e_\lambda = 1$;*
2. *orthogonality — $e_\lambda e_\mu = \delta_{\lambda\mu} \, e_\lambda$, in particular idempotency $e_\lambda^2 = e_\lambda$;*
3. *bar-invariance — $\overline{e_\lambda} = e_\lambda$ for every $\lambda$, self-conjugate or not;*
4. *conjugate pairing — $\#(e_\lambda) = e_{\lambda'}$ for every $\lambda$, so $\#$ fixes $e_\lambda$ exactly when $\lambda = \lambda'$*

*all hold. In particular each $e_\lambda$ is a central idempotent, and these are the central primitive idempotents of the Wedderburn blocks.*

## Proof

The Wedderburn isomorphism $H_n(q) \cong \prod_\lambda M_{f^\lambda}(K)$ sends each Murphy–Lagrange projector to a diagonal matrix unit $E^\lambda_{TT}$, because $J_k$ acts on the seminormal basis vector $v_S$ by $q^{2 c_S(k)}$ and the content vector determines the tableau. Hence $e_\lambda$ maps to the identity of the $\lambda$-block, which gives cross-checks 1 and 2 and centrality. The bar involution sends $J_k$ to $J_k^{-1}$ and $q$ to $q^{-1}$, so it sends each projector to the Lagrange projector in $J_k^{-1}$ with eigenvalues $q^{-2d}$, which picks out the same tableau (cross-check 3). The sign twist also sends $J_k$ to $J_k^{-1}$, but keeps the eigenvalues $q^{2d}$, so it picks out the tableau with negated contents, the transpose (cross-check 4).

## Status

All four cross-checks are proved on the Iwahori–Hecke algebra $H_n(q)$, for every $n$:

- Cross-checks 1 and 2, and centrality. The Wedderburn isomorphism sends each Lagrange projector to a diagonal matrix unit, and the formula above, written in the multiplicative $J_k$, coincides with that projector.
- Cross-check 3. Every map with the bar properties fixes every $e_\lambda$. No bar map is constructed; that needs a field automorphism with $q \mapsto q^{-1}$.
- Cross-check 4. The sign twist is constructed from the universal property and sends $e_\lambda$ to $e_{\lambda'}$.

**Ground field.** No hypothesis on the characteristic is needed. The Wedderburn isomorphism is built by sending each block's matrix units to Lagrange polynomials in the Murphy elements, which needs only that distinct tableaux have distinct content vectors and that $q^{2m} \neq 1$ for $0 < m \le 2n$. In particular the theorem holds over $K = \operatorname{Frac} R[q, q^{-1}]$ for any integral domain $R$, which covers $\mathbb{Q}(q)$ and $\mathbb{F}_p(q)$. Over $R[q, q^{-1}]$ itself $e_\lambda$ is not defined, because the denominators $q^{2m} - 1$ are not units.

**Which involution pairs $\lambda$ with $\lambda'$.** The bar involution does not: it fixes every $e_\lambda$, so an earlier form of cross-check 4, $\overline{e_\lambda} = e_{\lambda'}$, is false already at $n = 2$. The bar involution is the symmetry of the convention-D Markov trace and of non-abelian Stokes path reversal. The sign twist is not a symmetry of that trace: it relates the trace at $q$ to the trace at $-q^{-1}$.

**Formula.** An earlier form took the inner product over the boxes of $\lambda$. Two boxes on one diagonal share a content, so that product can divide by zero (for example $\lambda = (2,2)$). The form above, over all contents $|d| \le n - 1$, is the one in [Explicit central primitive idempotents $e_\lambda$ via Murphy elements](#prop:explicit-central-idempotent).
