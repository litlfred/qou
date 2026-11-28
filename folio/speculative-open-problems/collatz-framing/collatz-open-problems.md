Four open questions surround [the $q$-Collatz conjecture](#conj:q-collatz); none is claimed here:

1. **Power-series characterisation of divergent lifts.** By the Syracuse-lift and bounded-window propositions of the main monograph, [$q$-Collatz](#conj:q-collatz) fails if and only if some domain-stable Laurent polynomial lifts an unbounded Syracuse trajectory \cite{lagarias2010} with unbounded exponent support. Writing $t = 1 + q$, any domain-stable element with odd steps at positions $i_1 < i_2 < \cdots$ expands in $\mathbb{Z}[[t]]$ (where $[3]_q = 1 - t + t^2$ is a unit) as

$$
P = -\sum_{j \geq 1} t^{\,i_j}\,[3]_q^{-j}.
$$

Determining which infinite sequences $(i_j)$ sum to a finite Laurent polynomial in $q$ is open, and whether this question is more tractable than classical Collatz is unknown.

2. **Characterising liftable integers.** For integers $n = P(1)$ admitting a domain-stable lift, $q$-Collatz implies classical convergence, yet liftable integers are sparse: an odd step into $[2]_q^k q^{-1}$ (lifting $2^k$) exists if and only if $[3]_q \mid ([2]_q^{k+1} - q)$, which evaluation at a primitive cube root of unity shows holds precisely for $k \equiv 1 \pmod{6}$ (so $85 = (2^8 - 1)/3$ lifts, whereas $5 = (2^4 - 1)/3$ and $3$ do not, and nonzero constants are not domain-stable).

3. **Dynamics of the mod-$2$ shadow.** Reducing $\mathcal{C}_q$ modulo $2$ produces a total map $\bar{\mathcal{C}}$ on $\mathbb{F}_2[q^{\pm 1}]$ sending $f \mapsto f/(1 + q)$ when $f(1) = 0$ and $f \mapsto ((1 + q + q^2)f + 1)/(1 + q)$ when $f(1) = 1$. A domain-stable $\mathbb{Z}[q^{\pm 1}]$ orbit converges if and only if its mod-$2$ shadow is eventually periodic. Unlike the $\mathbb{F}_2[x]$ analogue with multiplier $1 + x$, whose orbits all converge \cite{hicksmullenyucaszavislak2008}, numerical experiments indicate unbounded-degree orbits for $\bar{\mathcal{C}}$ on $\mathbb{F}_2[q^{\pm 1}]$, so characteristic-$0$ lift constraints are essential.

4. **Constructing a Hecke-algebra lift.** Formulating the third face of [proposed braid faces](#rem:collatz-three-forms) as a mathematical statement requires defining a partial or total lift of $\mathcal{C}_q$ to $H_n(q)$ compatible with the Markov trace.
