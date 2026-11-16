Let $G$ be a group, standing for the braid group $B_n$ or its image in the Hecke algebra $H_n(q)$, and let $R$ be a ring of values.

**Observables.** A function $f \colon G \to R$ is an *observable* when $f(xy) = f(yx)$ for all $x, y \in G$. Equivalently, $f$ is a class function: $f(ywy^{-1}) = f(w)$. Every Markov trace and every irreducible character $\chi_\lambda$ of $H_n(q)$ is an observable in this sense.

Two equivalences on words are in play. Words $a, b$ are *conjugate*, $a \approx b$, when $b = y a y^{-1}$ for some $y$. Words are *equal in normal form*, $a \equiv b$, when they reduce to the same Gröbner–Shirshov normal form. Equality in normal form implies conjugacy, and the converse fails. Observables see only $\approx$.

**Virtual subword.** Fix a set $\mathcal{O}$ of observables. A subword $x$ placed between $u$ and $v$ is *virtual* for $\mathcal{O}$ when

$$
  f(u\,x\,v) = f(u\,v) \quad \text{for every } f \in \mathcal{O}.
$$

Two kinds are virtual for every set of observables:

1. *Pair creation*: $x = y\,y^{-1}$.
2. *Emission and reabsorption*: a loop $y\,w\,y^{-1}$ around a word $w$ satisfies $f(y\,w\,y^{-1}) = f(w)$ for every observable $f$.

A virtual subword is part of the word but changes no observable. Nothing in this definition calls it a particle, so it carries no propagator.

**Entanglement across a cut.** Let $w$ be a word on $n$ strands and $A \subset \{1, \dots, n\}$. Write $c_A(w)$ for the signed number of crossings between a strand in $A$ and a strand outside $A$, and $s_A(w)$ for the signed number of the remaining crossings. Every crossing is one or the other, so

$$
  \mathrm{wr}(w) = c_A(w) + s_A(w).
$$

The word is *entangled across* $A \mid A^{c}$ when $c_A(w) \neq 0$. For a pure braid, $c_A(w)$ is twice the linking number between the two groups of strands. A *prior entangled pair* is a pure subword that is entangled across the cut separating its two partners.

**Trivial-block shift.** In the one-dimensional trivial block of $H_n(q)$, where $\sigma_i \mapsto q$ and $\sigma_i^{-1} \mapsto q^{-1}$, every word evaluates to

$$
  q^{\mathrm{wr}(w)} = q^{c_A(w)} \cdot q^{s_A(w)}.
$$

The shift therefore splits into an entangled part and a self-twist part. A shift $q^{\pm 2}$ comes from either an entangled pair or a self-twist, and the block alone cannot tell which.

**Pairwise entanglement is not enough.** On three strands take $V = \sigma_0 \sigma_1^{-1}$. The word $V^3$ is pure, and every one-versus-two cut has $c_A(V^3) = 0$. Yet $V^3 \neq 1$, since its image under the reduced Burau representation at $t = 2$ is not the identity. Its closure is the Borromean rings. The entanglement of $V^3$ is three-party: it is detected by the Milnor invariant $\bar\mu_{123}$ and not by any pairwise linking number. A complete definition of entanglement therefore needs the Milnor hierarchy. Pairwise linking is its first level, which corresponds to a Bell-type pair, while $\bar\mu_{123}$ corresponds to a GHZ-type triple.
