Let $\mathcal{C}_q$ be the Skein-Collatz map of the [$q$-Collatz conjecture](#conj:q-collatz) on $\mathbb{Z}[q^{\pm 1}]$, let $P_0, P_1, \dots$ be a domain-stable orbit, and let $\mathrm{ev}_1 \colon \mathbb{Z}[q^{\pm 1}] \to \mathbb{Z}$ be evaluation at $q = 1$. Write $T(n) = n/2$ for even $n$ and $T(n) = (3n+1)/2$ for odd $n$ (the Syracuse map on $\mathbb{Z}$).

1. $\mathrm{ev}_1(P_{j+1}) = T\bigl(\mathrm{ev}_1(P_j)\bigr)$ for every $j$, and step $j$ is odd exactly when $\mathrm{ev}_1(P_j)$ is odd. So the parity sequence of the $q$-orbit is the classical parity sequence of $P_0(1)$.
2. If the step types repeat with period $K \geq 1$ from index $N$ on, then $P_{N+K} = P_N$.
3. If the Syracuse orbit of $P_0(1)$ is eventually periodic, then the $q$-orbit reaches one of the three cycles $\{0\}$, $\{-q^{-2}\}$, $\{q^{-1},\, 1 + q^{-1}\}$ of the [cycle classification](#prop:collatz-no-cycles).
4. Consequently, if no Syracuse orbit on $\mathbb{Z}$ diverges, every domain-stable orbit of $\mathcal{C}_q$ reaches one of these three cycles.
