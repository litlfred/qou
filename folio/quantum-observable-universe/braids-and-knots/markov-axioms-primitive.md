Let $R$ be a commutative ring and $q \in R^{\times}$ an invertible element with a chosen square root $q^{1/2}$. The Markov trace $\mathrm{tr}_M$ on the Iwahori-Hecke algebra $H_n(R, q)$ is the unique linear functional satisfying:

1. **Normalisation:** $\mathrm{tr}_M(1) = 1$.
2. **Cyclicity:** $\mathrm{tr}_M(xy) = \mathrm{tr}_M(yx)$ for all $x, y$.
3. **Stabilisation by $\sigma_n$:** $\mathrm{tr}_M(x \sigma_n) = z \cdot \mathrm{tr}_M(x)$ for $x \in H_n(R, q)$, where $z = q^3/(q^2+1)$ is the Markov-trace loop value (**convention D**; forced, see below).

Stabilisation by $\sigma_n^{-1}$ — often listed as a fourth axiom — is not an independent condition. Substituting the Hecke quadratic relation $\sigma_n^{-1} = \sigma_n - (q - q^{-1})$ into axiom 3 and using linearity of the trace (with $x \cdot 1 = x$) forces
$$
  \mathrm{tr}_M(x \sigma_n^{-1}) \;=\; z_{-} \cdot \mathrm{tr}_M(x),
  \qquad
  z_{-} \;:=\; z - (q - q^{-1}),
$$
so the negative-crossing loop value $z_{-}$ differs from $z$ whenever $q \neq \pm 1$. No choice of trace parameter makes the two stabilisations scale by mutually inverse factors either: $z \cdot z_{-} = 1$ has the sole solutions $z = q$ and $z = -q^{-1}$, the one-dimensional characters of $H_n(R, q)$, both of which are degenerate. Link invariance of the Jones polynomial is instead restored by the writhe prefactor outside the trace ([Jones–Markov trace](#thm:jones-markov-trace)).

Axioms 1–2 with an unspecified stabilisation parameter admit a **one-parameter
family**; axiom 3 selects one member of it, and which member is *not* free. The
selection is forced by the dimension of the mass fibre:

- The [Feynman eigenbasis decomposition](#lem:feynman-eigenbasis-decomposition) already writes the row cap
  $\ell(\lambda) \leq 2$ into the mass channel's own decomposition: $V$ is the
  fundamental of $\mathrm{SU}_q(2)$, and the summand count $\lfloor n/2 \rfloor + 1$
  is the two-row count and no other. So $y_{(1^3)} = 0$ is a direct restatement of the
  decomposition the mass chapter uses.
- Given $y_{(1^3)} = 0$, the Temperley--Lieb uniqueness theorem
  shows the faithful normalised Markov trace on the two-row quotient is **unique** and equals
  $z = q^3/(q^2+1)$ (**convention D**). The competing root $z = q$ is real but
  degenerate ($y_{(2,1)} = 0$, not faithful on $\mathrm{TL}_3$), which is why the
  faithfulness hypothesis is load-bearing.

So the loop value is a **consequence** of the fibre being two-dimensional rather than an external stipulation.

Convention D has $y_{(1^3)} = 0$, so it **is** the trace whose braid closure is
the Jones polynomial: under D the "Jones–Markov" name is accurate, and under
convention C,
$z = 1/(q^{1/2}+q^{-1/2})$, where the loop value is stipulated rather than
derived, it is not.

 Because $\mathrm{tr}_M$ is compatible with the tower inclusions and evaluates disjoint generators by iterated application of axiom 3, the joint Markov trace of two braids acting on disjoint strand sets is strictly multiplicative:
$$
  \mathrm{tr}_M(K_1 \sqcup K_2) \;=\; \mathrm{tr}_M(K_1) \cdot \mathrm{tr}_M(K_2).
$$
Appending $k$ further strands, each stabilised by one positive crossing, multiplies this value by $z^k$ (one factor of $z$ per application of axiom 3). This derives the inter-knot decoupling theorem from primitive Markov axioms.
