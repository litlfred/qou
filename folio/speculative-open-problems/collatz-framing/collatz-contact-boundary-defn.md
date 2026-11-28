For a domain-stable element $P \in \mathbb{Z}[q^{\pm 1}]$ whose forward $\mathcal{C}_q$-orbit takes odd steps at indices $i_1 < i_2 < \cdots$, define the **orbit $[2]_q$-contact average** (when the limit exists) by

$$
\langle v_{[2]} \rangle(P) := \lim_{M \to \infty} \frac{1}{M} \sum_{m=1}^{M} v_{[2]}\!\bigl(\mathcal{C}_q(P_{i_m})\bigr),
$$

where $v_{[2]}(R) = \max\{k \ge 0 : [2]_q^k \mid R\}$ is the $[2]_q$-adic valuation, and define at real $q > 0$ the formal locus $\mathcal{H}_{\mathrm{Col}}(q) = \{P : \langle v_{[2]} \rangle(P) = \log [3]_q / \log [2]_q\}$.

**Convention and bound.** Because the odd branch $\mathcal{C}_q(P) = ([3]_q P + 1)/[2]_q$ already performs one division by $[2]_q$, $v_{[2]}(\mathcal{C}_q(P))$ counts additional even steps *after* that built-in division. On the fundamental cycle $q^{-1} \mapsto 1 + q^{-1} = q^{-1}[2]_q \mapsto q^{-1}$ of [the $q$-Collatz conjecture](#conj:q-collatz), each odd step is followed by one even step, so $\langle v_{[2]} \rangle = 1$, and degree accounting shows $\limsup \langle v_{[2]} \rangle \le 1$ on every domain-stable orbit with infinitely many odd steps ([chapter introduction](#sec:collatz-intro)). Thus $\langle v_{[2]} \rangle(P)$ does not separate convergent from divergent orbits.
