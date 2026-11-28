**Status: heuristic surreal comparison, not a complexity lower bound.** Writing the heuristic of [the Reeb--surreal conjecture](#conj:p-vs-np-qou) in Conway $\omega$-order notation \cite{conway1976}, for any standard-real $\delta_n > 0$,

$$
2^n \cdot \delta_n^2 \cdot \varepsilon^{-1} > 2^n \cdot \varepsilon^3 \qquad \text{in } \mathbb{R}(\varepsilon) \subset \mathbf{No},
$$

equivalently $\ordw(2^n \delta_n^2 \varepsilon^{-1}) = 1 > -3 = \ordw(2^n \varepsilon^3)$, because the standard-real factor $2^n > 0$ has $\ordw(2^n) = 0$ on both sides.

**Why this does not separate $\mathbf{P}$ from $\mathbf{NP}$.** Because $\ordw(2^n) = \ordw(n^k) = 0$ for every fixed $n$, the $\omega$-adic order in $\mathbb{R}(\varepsilon)$ is blind to the difference between polynomial $n^k$ and exponential $2^n$ growth in the standard-real variable $n$. The inequality compares $\varepsilon^{-1}$ with $\varepsilon^3$ at fixed $n$ and therefore cannot distinguish a polynomial-time algorithm from an exponential-time search.
