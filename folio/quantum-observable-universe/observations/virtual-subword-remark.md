**Observables.** Equivalently, $f$ is a class function: $f(ywy^{-1}) = f(w)$. Every Markov trace and every irreducible character $\chi_\lambda$ of $H_n(q)$ is an observable in this sense.

Equality in normal form implies conjugacy, and the converse fails. Observables see only $\approx$.

Two kinds are virtual for every set of observables:

1. *Pair creation*: $x = y\,y^{-1}$.
2. *Emission and reabsorption*: a loop $y\,w\,y^{-1}$ around a word $w$ satisfies $f(y\,w\,y^{-1}) = f(w)$ for every observable $f$.

A virtual subword is part of the word but changes no observable. Nothing in this definition calls it a particle, so it carries no propagator.

**Entanglement across a cut.** Every crossing of $w$ is counted in exactly one of $c_A(w)$ and $s_A(w)$, so

$$
  \mathrm{wr}(w) = c_A(w) + s_A(w).
$$

For a pure braid, $c_A(w)$ is twice the linking number between the two groups of strands.

**Trivial-block shift.** In the one-dimensional trivial block of $H_n(q)$, where $\sigma_i \mapsto q$ and $\sigma_i^{-1} \mapsto q^{-1}$, every word evaluates to

$$
  q^{\mathrm{wr}(w)} = q^{c_A(w)} \cdot q^{s_A(w)}.
$$

The shift therefore splits into an entangled part and a self-twist part. A shift $q^{\pm 2}$ comes from either an entangled pair or a self-twist, and the block alone cannot tell which.

**Pairwise entanglement is not enough.** On three strands take $V = \sigma_0 \sigma_1^{-1}$. The word $V^3$ is pure, and every one-versus-two cut has $c_A(V^3) = 0$. Yet $V^3 \neq 1$, since its image under the reduced Burau representation at $t = 2$ is not the identity. Its closure is the Borromean rings. The entanglement of $V^3$ is three-party: it is detected by the Milnor invariant $\bar\mu_{123}$ and not by any pairwise linking number. A complete definition of entanglement therefore needs the Milnor hierarchy. Pairwise linking is its first level, which corresponds to a Bell-type pair, while $\bar\mu_{123}$ corresponds to a GHZ-type triple.

**Connected part.** On a pair this is $\phi_F(\{a,b\}) = F(\{a,b\}) - F(\{a\}) - F(\{b\}) + F(\varnothing)$. Suppose $T$ splits into disjoint nonempty parts $T_1$ and $T_2$ with $F(U) = F(U \cap T_1) + F(U \cap T_2)$ for every $U \subseteq T$. Then $\phi_F(T) = 0$. So $\phi_F(T) \neq 0$ means that the strands of $T$ do not split into two non-interacting groups, and it certifies $|T|$-party entanglement relative to $F$. Both statements are proved in the formalisation without extra hypotheses.

The natural choice of $F$ comes from a knot invariant that turns split union into a product. For the Jones polynomial, $G(L) = \delta\, V_L(t)$ with $\delta = -(t^{1/2} + t^{-1/2})$ satisfies $G(L_1 \sqcup L_2) = G(L_1)\, G(L_2)$ and $G(\text{unknot}) = \delta$. Take $F(T) = \log G(L_T) - |T| \log \delta$ for nonempty $T$, where $L_T$ is the closure of the sub-braid on the strands of $T$, and set $F(\varnothing) = 0$. Then $F$ vanishes on every unlink and is additive on split sublinks. The case $|T| = 2$ is the pairwise (Bell) level, and the case $|T| = 3$ with every pair contribution zero is the three-party (GHZ) level. The connected part has the same Möbius form as the connected three-body term of the binding sum. Whether the two are the same object is not established here.

For $V^3$ every sublink with at most two components is an unlink, so all single and pair contributions vanish and

$$
  \phi_F(\{1,2,3\}) = \log \frac{V_{\mathrm{Bor}}(t)}{\delta^2}
  = \log\!\left(1 - \frac{(t-1)^4 (t^2+t+1)}{t^2 (t+1)^2}\right)
  = -\tfrac{3}{4} (\log t)^4 + O\big((\log t)^6\big).
$$

This is exact over $\mathbb{Z}[t^{\pm 1/2}]$. It vanishes at $t = 1$, so the classical limit cannot see the three-party entanglement, and it is nonzero for every $t > 0$ with $t \neq 1$.
