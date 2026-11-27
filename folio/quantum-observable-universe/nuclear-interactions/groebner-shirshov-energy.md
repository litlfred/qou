The Gröbner--Shirshov basis theory gives a stronger result than uniqueness: both the Markov trace of a nuclear braid word and the $\ell^1$ word-length norm of its normal form are computed with no reduction-path dependence. The invariance holds for a fixed word; it does not say that the word selected for a nucleus is independent of the order in which it was assembled.

Define the word-length functional on normal-form expansions in $H_A(q)$ by

$$
  E(\xi) = \sum_{w \in B} |c_w(q)| \cdot \ell(w)
$$

where $\xi = \sum_{w \in B} c_w(q)\,w$ is the normal form and $\ell(w)$ is the word length. Then:

1. **Only Hecke reductions change $E$.** The Yang--Baxter relation, far commutativity, and the other Bokut--Shiao rules preserve coefficients and word lengths. The Hecke relation is the unique $E$-changing generator.
2. **Telescoping path independence.** Along any reduction path $\xi_0 \to \xi_1 \to \cdots \to \xi_m$ the step changes sum to $E(\xi_m) - E(\xi_0)$. By confluence every path ends at the same normal form, so the total change depends only on $\xi_0$.
3. **Single-step word-length change.** Let $h = q - q^{-1}$. Applied to an isolated monomial $c\,w$ with $w = u\,\sigma_i\sigma_i\,v$ of length $\ell$, the replacement of $\sigma_i^2$ by $h\,\sigma_i + 1$ changes $E$ by

$$
  \bigl(|c|\,|h|\,(\ell - 1) + |c|\,(\ell - 2)\bigr) - |c|\,\ell \;=\; |c|\,\bigl(|h|\,(\ell - 1) - 2\bigr).
$$

The sign is not fixed: for $|h|\,(\ell - 1) < 2$ the step lowers $E$.
4. **Hecke skein invariance of linear traces.** Over any commutative ring $R$, any $R$-linear functional $\tau \colon H_n(R, q) \to R$ respecting $u\,\sigma_i^2\,v = h\,u\,\sigma_i\,v + u\,v$ satisfies $\tau(u\,\sigma_i^2\,v) = h\,\tau(u\,\sigma_i\,v) + \tau(u\,v)$. Under the normalised Markov rules $\tau(1) = 1$, $\tau(\sigma_i) = z$, and $\tau(\sigma_1\sigma_2) = z^2$, a single square evaluates to $\tau(\sigma_i^2) = h\,z + 1$, and both $\sigma_1^2\sigma_2$ and the cyclically conjugate reduced word $\sigma_1\sigma_2\sigma_1$ evaluate to $\tau(\sigma_1\sigma_2\sigma_1) = z\,(1 + h\,z)$, whereas the normal-form coefficient sums are $1 + h$ and $1$.

**Archimedean specialisation.** The absolute values in $E$ are taken over $\mathbb{R}$, so the word-length functional sits on the archimedean side of the algebraic→archimedean wall, whereas item 4 holds over any commutative ring $R$. Near the aether value, $h \approx 0.21$, so a Hecke step on a short word lowers $E$.

**β decay in the short typed-crossing model.** In $H_3(q)$ take the short-model nucleon normal forms $p = \sigma_1\sigma_2 - (h/2)\,\sigma_1$ and $n = \sigma_1\sigma_2 - h\,\sigma_1 - (h/2)\,\sigma_2 + h^2/2$. Then

$$
  E(p) - E(n) = -|h|,
$$

so for $q > 1$ the daughter proton has the lower word-length norm. The statement is specific to this model. In the 11-letter typed-crossing model the nucleon-only change has the opposite sign at the aether value, and on the common base $(\sigma_1\sigma_2^{-1})^3$ it is zero, so no model-free sign of the β-decay energy change follows from $E$.
