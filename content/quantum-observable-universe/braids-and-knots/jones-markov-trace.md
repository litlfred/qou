Let $q \in \mathbb{C}^{\times}$ not be a root of unity. The Iwahori--Hecke algebra $H_n(\mathbb{C}, q)$ admits a unique $\mathbb{C}$-linear functional $\mathrm{tr}_M$ satisfying:
1. Normalisation: $\mathrm{tr}_M(1) = 1$.
2. Trace property: $\mathrm{tr}_M(ab) = \mathrm{tr}_M(ba)$.
3. Markov property, for $x \in H_n(\mathbb{C}, q)$:
$$
  \mathrm{tr}_M(x \sigma_n) = z\,\mathrm{tr}_M(x), \qquad
  z = \frac{q^3}{q^2 + 1} = \mathrm{tr}_M(\sigma_i)
$$
the Markov-trace loop value — **convention D** of the
[trace-convention registry](../../../docs/coordination/trace-convention-registry.md),
pinned in [`rem:markov-axioms-primitive`](markov-axioms-primitive.md). Note
that $q$ not a root of unity already gives $q^2 + 1 \neq 0$, and that $z$ is a
rational function of $q$: no square root is needed.

For each partition $\lambda \vdash n$, the restriction of $\mathrm{tr}_M$ to the irreducible $H_n(\mathbb{C}, q)$-module $S_\lambda$ is a non-zero scalar multiple of the character $\chi_\lambda$. For any braid $\beta$, $\mathrm{tr}_M(\rho_n(\beta))$ computes the Jones polynomial of the closure $\hat{\beta}$ up to framing. This last clause is what fixes $z$: the trace whose closure is the Jones polynomial is the one factoring through $\mathrm{TL}_n$, i.e. $y_{(1^n)} = 0$, and on $\mathrm{H}_3$ the unique non-degenerate such parameter is $z = q^3/(q^2+1)$ ([`MarkovTraceTLUniqueness`](../lean/QOU/BraidsAndKnots/MarkovTraceTLUniqueness.lean)).
