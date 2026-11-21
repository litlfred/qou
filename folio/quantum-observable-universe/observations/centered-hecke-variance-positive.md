*Let $q > 0$. Let $z = q^3/(q^2+1)$ (**convention D**) and $\tilde\sigma_i := \sigma_i - z \cdot 1$. The variance*
$$
  \mathrm{Var}(\sigma_i) \;:=\; \mathrm{tr}_M(\tilde\sigma_i^2)
  \;=\;
  (q - q^{-1}) z + 1 - z^2
  \;=\;
  \frac{q^4 + q^2 + 1}{(q^2+1)^2}
$$
*is strictly positive for every $q > 0$, attains its minimum $3/4$ at $q = 1$ and only there, and tends to $1$ at both ends. At $q_0$ it is $0.75270211325196540159$.*

Under convention D the variance is a **Wenzl weight**. The closed form above equals
$$
  y_{(3)} + y_{(2,1)}
  \;=\; \frac{[4]_q}{[2]_q^3} + \frac{1}{[2]_q^2},
$$
identically in $q$, which is the isospin-triplet weight $\mu_+$. So $\mathrm{Var}(\sigma_i) = \mu_+$, and its value at $q_0$ is the same $0.7527$ that sits $22.85\,\%$ above the interface ceiling $z = 0.61268803714646525160$. It is also the magnitude of the extreme eigenvalues of the Markov–Gram form on the bilinear pairing at $q_0$, $\pm 0.75270211$.

See [Table: Centred Hecke variance at $q_0$](#tbl:centered-hecke-variance-positive-table-data). The variance is well-separated from zero.

**Scope: algebraic, not yet probabilistic.** Under convention D the hypothesis $q^{1/2}+q^{-1/2} > 2$ is algebraically unnecessary — positivity holds on all of $q > 0$ — and that is the whole of what the statement above claims. That hypothesis carried a second job in the convention-C setting: it was the paper's citation of Wenzl's positivity threshold, the condition under which $\mathrm{tr}_M$ is a positive functional and $\mathrm{Var}(\sigma_i)$ may be read as the variance of a tracial state rather than as a number. The threshold is calibrated to convention C, and its convention-D analogue is **not** derived here. Read the statement above as the algebraic identity it is; the probabilistic reading, and the $q$-CLT consequence drawn in the interpretation below, inherit whatever the D threshold turns out to be.

**Positivity on the Temperley–Lieb quotient.** Under Convention D, $\mathrm{tr}_M$ factors through the Temperley–Lieb algebra $\mathrm{TL}_n(q)$ with loop parameter $[2]_q = q + q^{-1} \geq 2$, which defines a positive tracial state for every real $q > 0$ by Jones's theorem ([Markov-trace GNS embedding $H_\infty(q)/\mathcal{N} \hookrightarrow L(\mathcal{H})$](#prop:algebraic-gns-embedding)). Consequently, $\mathrm{Var}(\sigma_i)$ is the variance of a genuine tracial state for every $q > 0$.
