The Gröbner--Shirshov basis theory gives a stronger result than uniqueness: the energy of the nuclear braid word is a topological invariant, computed with no path dependence. The invariance holds for a fixed word; it does not say that the word selected for a nucleus is independent of the order in which it was assembled.

**Theorem.**
Define the energy functional on $H_A(q)$ by

$$
  E(\xi) =  \sum_{w \in B} |c_w(q)| \cdot \ell(w)
$$

where $\xi$ is the normal form and $\ell(w)$ is the word length. Then:

1. **Only Hecke reductions change energy.** The Yang--Baxter relation, far commutativity and the other Bokut--Shiao rules preserve coefficients and lengths. The Hecke relation is the unique energy-changing generator.
2. **Energy is path-independent.** Along any reduction path $\xi_0 \to \xi_1 \to \cdots \to \xi_m$ the step changes sum to $E(\xi_m) - E(\xi_0)$. By confluence every path ends at the same normal form, so the total change depends only on $\xi_0$.
3. **Energy change of one Hecke step.** Let $h = q - q^{-1}$. Applied to an isolated monomial $c\,w$ with $w = u\,\sigma_i\sigma_i\,v$ of length $\ell$, the replacement of $\sigma_i^2$ by $h\,\sigma_i + 1$ changes the energy by

$$
  |c|\,\bigl(|h|\,(\ell - 1) - 2\bigr).
$$

The sign is not fixed: for $|h|\,(\ell - 1) < 2$ the step lowers the energy.

**Archimedean specialisation.** The absolute values in $E$ are taken over $\mathbb{R}$, so the functional sits on the archimedean side of the substrate wall. Near the substrate value, $h \approx 0.21$, so a Hecke step on a short word lowers the energy.
