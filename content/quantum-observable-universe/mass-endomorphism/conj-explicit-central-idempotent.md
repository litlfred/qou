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
[`prop:explicit-central-idempotent`](#prop:explicit-central-idempotent). That proposition is proved in Lean *conditionally* on them, with the class carrying them as an explicit instance hypothesis. Naming the conjecture as its own block is what lets the proposition's `uses[]` record the dependency, so the conditional cone is auditable from the manifest and not only from the Lean signature.

## Status

Open. The carrier is the class `QOU.BraidKnot.ExplicitCentralIdempotent.ExplicitCentralIdempotentConjecture`, whose field states cross-check 2 — the one downstream Lean consumes — quantified over every partition of every $n$, so it is a claim about the whole construction and not about one $\lambda$. **No instance of the class exists anywhere in the corpus**, which is the correct representation of an unproved primary conjecture: an instance would assert the statement, not prove it.

The `J_k` diagonal action that the interpolation argument rests on is itself established — [`prop:jucys-murphy-central-elements-qou`](#prop:jucys-murphy-central-elements-qou) gives pairwise commutation and the eigenvalue $J_k \cdot v_T = c_T(k;q) \cdot v_T$ on the Hoefsmit seminormal basis ([`prop:hoefsmit-seminormal-form`](#prop:hoefsmit-seminormal-form)). What is missing is the step from that diagonal action to the four identities, which is the interpolation argument proper.

## Scope of the Lean carrier

The class encodes cross-check 2 only. Cross-checks 1, 3 and 4 appear in the statement above and in the proposition's docstring but are **not** fields of the class, so a future instance would discharge idempotency alone. That is a deliberate under-encoding — the downstream theorem needs only idempotency — and it means the class is a faithful carrier for what is *consumed*, not for the full conjecture as stated here. Extending it is the natural next step once any of the other three acquires a downstream consumer.
