**Corollary.** *Let $R$ be a field of characteristic $0$ and $q \in R$ with $[k]_q \neq 0$ for $1 \le k \le n$. Let $E_r^{p,q'}$ be the spectral sequence of the Hochschild complex of $H_n(R, q)$ filtered by Coxeter length, in the bigrading $q' = k - p$ with $k$ the cochain degree ([length-filtration spectral sequence](#prop:gb-spectral-sequence)). Then*

$$
  E_\infty^{p, q'} = 0 \qquad \text{for all } p \ge 0,\ q' > 0 .
$$

*This holds for every $n$. In particular it holds for every real $q > 1$ and every $n$.*

*Proof.* The hypothesis on $[k]_q$ makes $H_n(R, q)$ semisimple \cite{dipper-james1986}. A semisimple algebra over a field of characteristic $0$ is separable, so $HH^k(H_n, H_n) = 0$ for $k \ge 1$ \cite{weibel1994} ([limit page for semisimple $H_n$](#prop:spectral-sequence-collapse)). The spectral sequence converges with $E_\infty^{p,q'} \cong \mathrm{gr}^p HH^{p+q'}$. For $p \ge 0$ and $q' > 0$ the total degree $p + q'$ is at least $1$, so $E_\infty^{p,q'} = 0$. For real $q > 1$, $[k]_q = (q^k - q^{-k})/(q - q^{-1}) > 0$. $\qquad\blacksquare$

*At $n = 3$ the exact computation gives $E_\infty$ in cochain degree $0$ only, at filtration degrees $0, -2, -3$; those classes have $q' = -p \ge 0$ and $p \le 0$, consistent with the corollary.*
