Each generator $\sigma_i$ of $H_n(q)$ has two eigenlines: the line on which it acts by $q$, with projector $P_+ = (\sigma_i + q^{-1})/[2]_q$, and the line on which it acts by $-q^{-1}$, with projector $P_- = (q - \sigma_i)/[2]_q$. The Hecke relation fixes only $q - q^{-1}$, so it does not single out either line. Relabelling the root $q \mapsto -q^{-1}$ exchanges $P_+$ and $P_-$ and leaves the generator unchanged.

Convention D, the trace selected in [the Markov-trace selection](#prop:markov-trace-frobenius-selection), does single out a line. It does so in three ways.

1. **At $n = 3$ it kills the block on which every generator acts by $-q^{-1}$.** That block is $(1^3)$, which carries weight $y_{(1^3)} = 0$ ([the antisymmetriser lemma](#prop:convention-d-kills-antisymmetriser)). The block on which every generator acts by $q$ is $(3)$, and it keeps the weight $y_{(3)} = (q^4+1)/(q^2+1)^2$.
2. **Its parameter depends on the root label.** $z_D(q) = q^3/(q^2+1)$, while $z_D(-q^{-1}) = -1/(q^3+q)$.
3. **At every level $n$ it weighs the two lines in the ratio $[3]_q : 1$.** For any Markov trace, $\tau(P_+) = (z + q^{-1})/[2]_q$ and $\tau(P_-) = (q - z)/[2]_q$, and neither depends on $n$. At $z = z_D$:

$$
\frac{\tau(P_+)}{\tau(P_-)} \;=\; [3]_q \;=\; q^2 + 1 + q^{-2}.
$$

This is the ratio of the quantum dimensions of $\mathrm{Sym}^2 V$ and $\Lambda^2 V$ for the $\mathrm{SU}_q(2)$ fundamental $V$. It equals $3$ at $q = 1$ and is unchanged under $q \mapsto q^{-1}$. The bias therefore comes from convention D itself, not from $|q| > 1$.

The favoured line is the one on which the generator acts by $q$. For $q > 1$ that is the line on which a positive crossing acts with eigenvalue of modulus greater than $1$.

**What this does not say.** These are observations about a ruled trace convention. Nothing here identifies either eigenline with a physical chirality, or the favoured line with the left-handed weak coupling. That identification is not made.

The bias is also not exclusive. The algebra $P_- H_n P_-$ (call it the corner over $P_-$) contains a copy of $\mathfrak{sl}_2$ for every $n \geq 4$. Convention D gives that copy zero weight at $n = 4$ only. From $n = 5$ on, both corners carry $\mathfrak{sl}_2$-carrying blocks that convention D keeps, and the weighted share of the two corners tends to $[3]_q : 1$.
