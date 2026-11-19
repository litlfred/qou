**Conjecture.** *Let $H_n(q)$ be the Iwahori–Hecke algebra over a commutative ring $R$ at generic $q$, and let*

$$
  e_\lambda \;=\; \sum_{T \in \mathrm{SYT}(\lambda)} \; \prod_{k=1}^{n} \; \prod_{\substack{\square \in \lambda \\ \square \neq T(k)}} \frac{J_k - c(\square; q)}{c(T(k); q) - c(\square; q)}
$$

*be the Murphy–Lagrange element attached to a partition $\lambda \vdash n$, built from the Jucys–Murphy elements $J_1, \ldots, J_n$ and the $q$-contents $c(\square; q) = q^{2(j-i)}$ of the boxes of $\lambda$. Then the four cross-checks*

1. *sum-to-identity — $\sum_{\lambda \vdash n} e_\lambda = 1$;*
2. *orthogonality — $e_\lambda e_\mu = \delta_{\lambda\mu} \, e_\lambda$, in particular idempotency $e_\lambda^2 = e_\lambda$;*
3. *self-adjointness — $\star(e_\lambda) = e_\lambda$ for self-conjugate $\lambda = \lambda'$;*
4. *bar-pairing — $\star(e_\lambda) = e_{\lambda'}$ for a chiral pair $\lambda \neq \lambda'$*

*all follow from Lagrange interpolation in the commuting variables $J_1, \ldots, J_n$.*

## Why this is stated separately

The cross-checks are what makes $e_\lambda$ *the* central primitive idempotent rather than merely an element of $Z(H_n(q))$, and they are the sole unproved input to
[the explicit central idempotent proposition](#prop:explicit-central-idempotent). That proposition holds *conditionally* on them, taking the interpolation hypothesis as an explicit premise.

## Open interpolation step

The conjecture remains open. Its hypothesis states cross-check 2 — quantified over every partition of every $n$, so it is a claim about the whole construction and not about one $\lambda$.

The $J_k$ diagonal action that the interpolation argument rests on is itself established — [the Jucys–Murphy centrality proposition](#prop:jucys-murphy-central-elements-qou) gives pairwise commutation and the eigenvalue $J_k \cdot v_T = c_T(k;q) \cdot v_T$ on the Hoefsmit seminormal basis ([Hoefsmit seminormal form](#prop:hoefsmit-seminormal-form)). What is missing is the step from that diagonal action to the four identities, which is the interpolation argument proper.

## Scope of the interpolation hypothesis

The hypothesis carries the **interpolation-theoretic inputs**, not the cross-checks
themselves: an index type $\mathrm{Tab}(\lambda)$ of standard tableaux, a
projector $\pi_T$ for each, and three properties —

- $\pi_T^2 = \pi_T$ (Lagrange interpolation at a simple joint eigenvalue),
- $\pi_T \pi_{T'} = 0$ for $T \neq T'$ (distinct tableaux carry distinct joint
  eigenvalue tuples),
- $e_\lambda = \sum_T \pi_T$.

Cross-check 2 is then **derived**: $e_\lambda^2 = \sum_T \sum_{T'} \pi_T
\pi_{T'} = \sum_T \pi_T^2 = \sum_T \pi_T = e_\lambda$.

Cross-checks 1, 3 and 4 (sum-to-identity, self-adjointness, bar-pairing) are
stated above as part of the full interpolation conjecture; orthogonality at the projector level directly yields idempotency of $e_\lambda$.
