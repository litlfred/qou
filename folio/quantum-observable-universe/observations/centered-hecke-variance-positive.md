*Let $q > 0$. Let $z = q^3/(q^2+1)$ and $\tilde\sigma_i := \sigma_i - z \cdot 1$. The variance*
$$
  \mathrm{Var}(\sigma_i) \;:=\; \mathrm{tr}_M(\tilde\sigma_i^2)
  \;=\;
  (q - q^{-1}) z + 1 - z^2
  \;=\;
  \frac{q^4 + q^2 + 1}{(q^2+1)^2}
$$
*is strictly positive for every $q > 0$, attains its minimum $3/4$ at $q = 1$ and only there, and tends to $1$ at both ends. At $q_0$ it is $0.75270211325196540159$.*

At $z = q^3/(q^2+1)$ the variance is a **Wenzl weight**. The closed form above equals
$$
  y_{(3)} + y_{(2,1)}
  \;=\; \frac{[4]_q}{[2]_q^3} + \frac{1}{[2]_q^2},
$$
identically in $q$, which is the isospin-triplet weight $\mu_+$. So $\mathrm{Var}(\sigma_i) = \mu_+$, and its value at $q_0$ is the same $0.7527$ that sits $22.85\,\%$ above the interface ceiling $z = 0.61268803714646525160$. It is also the magnitude of the extreme eigenvalues of the Markov–Gram form on the bilinear pairing at $q_0$, $\pm 0.75270211$.

See [Table: Centred Hecke variance at $q_0$](#tbl:centered-hecke-variance-positive-table-data). The variance is well-separated from zero.

**Positivity on the Temperley–Lieb quotient.** Algebraically, $(q^4+q^2+1)/(q^2+1)^2 > 0$ holds on all of $q > 0$ without any auxiliary threshold inequality. Moreover, at $z = q^3/(q^2+1)$, $\mathrm{tr}_M$ factors through the Temperley–Lieb algebra $\mathrm{TL}_n(q)$ with loop parameter $[2]_q = q + q^{-1} \geq 2$, defining a positive tracial state for every real $q > 0$ by Jones's theorem ([Markov-trace GNS embedding $H_\infty(q)/\mathcal{N} \hookrightarrow L(\mathcal{H})$](#prop:algebraic-gns-embedding)). Consequently, $\mathrm{Var}(\sigma_i)$ is the variance of a positive tracial state for every $q > 0$.
