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
[Explicit central primitive idempotents $e_\lambda$ via Murphy elements](#prop:explicit-central-idempotent). That proposition is proved *conditionally* on them.

## Open interpolation step

The conjecture remains open. The hypothesis used downstream is cross-check 2, quantified over every partition of every $n$, so it is a claim about the whole construction and not about one $\lambda$. **No proof of it is known.**

The diagonal action of the $J_k$ that the interpolation argument rests on is itself established — [Elementary symmetric polynomials in Jucys–Murphy elements are central in $H_n(q)$ with closed-form spectrum on each Wedderburn block](#prop:jucys-murphy-central-elements-qou) gives pairwise commutation and the eigenvalue $J_k \cdot v_T = c_T(k;q) \cdot v_T$ on the Hoefsmit seminormal basis ([Hoefsmit seminormal matrices as $R$-matrix evaluations in $H_n(q)$](#prop:hoefsmit-seminormal-form)). What is missing is the step from that diagonal action to the four identities, which is the interpolation argument proper.

## Scope of the conditional hypothesis

The hypothesis consists of the **interpolation-theoretic inputs**, not the cross-checks
themselves: an index type $\mathrm{Tab}(\lambda)$ of standard tableaux, a
projector $\pi_T$ for each, and three properties —

- $\pi_T^2 = \pi_T$ (Lagrange interpolation at a simple joint eigenvalue),
- $\pi_T \pi_{T'} = 0$ for $T \neq T'$ (distinct tableaux carry distinct joint
  eigenvalue tuples),
- $e_\lambda = \sum_T \pi_T$.

Cross-check 2 is then **derived**: $e_\lambda^2 = \sum_T \sum_{T'} \pi_T
\pi_{T'} = \sum_T \pi_T^2 = \sum_T \pi_T = e_\lambda$.


Cross-checks 1, 3 and 4 (sum-to-identity, self-adjointness, bar-pairing) are
stated above but are not part of the hypothesis — nothing downstream uses them
yet. Orthogonality enters at the projector level, because idempotency needs
it. The hypothesis is **unproved**: the conjecture is open.
