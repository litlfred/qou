*Let $q > 0$. Let $z = q^3/(q^2+1)$ (**convention D**) and $\tilde\sigma_i := \sigma_i - z \cdot 1$. The variance*
$$
  \mathrm{Var}(\sigma_i) \;:=\; \mathrm{tr}_M(\tilde\sigma_i^2)
  \;=\;
  (q - q^{-1}) z + 1 - z^2
  \;=\;
  \frac{q^4 + q^2 + 1}{(q^2+1)^2}
$$
*is strictly positive for every $q > 0$, attains its minimum $3/4$ at $q = 1$ and only there, and tends to $1$ at both ends. At $q_0$ it is $0.75270211325196540159$.*

Under convention D the variance is not merely positive — it **is** a Wenzl weight. The closed form above equals
$$
  y_{(3)} + y_{(2,1)}
  \;=\; \frac{[4]_q}{[2]_q^3} + \frac{1}{[2]_q^2},
$$
identically in $q$, which is the isospin-triplet weight $\mu_+$. So $\mathrm{Var}(\sigma_i) = \mu_+$, and its value at $q_0$ is the same $0.7527$ that sits $22.85\,\%$ above the interface ceiling $z = 0.61268803714646525160$. It is also the magnitude of the extreme eigenvalues of the Markov–Gram form on the bilinear pairing at $q_0$, $\pm 0.75270211$.

See [Table: Centred Hecke variance at $q_0$](#tbl:centered-hecke-variance-positive-table-data). The variance is well-separated from zero.

**Corrected 2026-08-09.** This proposition previously read $z = 1/(q^{1/2}+q^{-1/2})$ — **convention C**, excised by the owner ruling of 2026-08-09 — and quoted $\mathrm{Var}(\sigma_i) \approx 0.855$ at $q_0$. That figure is withdrawn. The correction strengthens the result: under C, positivity was conditional on the Wenzl regime $q^{1/2}+q^{-1/2} > 2$ and the bound was $\mathrm{Var} > 3/4$; under D the expression is a ratio of manifestly positive polynomials, so positivity is unconditional on $q > 0$ and $3/4$ is attained rather than merely approached.

**Open (2026-08-09).** The hypothesis $q^{1/2}+q^{-1/2} > 2$ dropped from the statement above is *algebraically* unnecessary, and that is all that is claimed here. It also carried a second job — it was the paper's citation of Wenzl's positivity threshold, the condition under which $\mathrm{tr}_M$ is a positive functional and $\mathrm{Var}(\sigma_i)$ may be read as a variance of a tracial state rather than as a number. That threshold was calibrated to convention C and its convention-D analogue has **not** been re-derived here. Until it is, read the statement above as the algebraic identity it is; the probabilistic reading, and the $q$-CLT consequence drawn in the interpretation below, inherit whatever the D threshold turns out to be.
