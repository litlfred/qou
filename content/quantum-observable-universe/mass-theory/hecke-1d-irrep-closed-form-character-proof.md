A 1-dimensional irrep $V_\lambda$ of $H_n(q)$ is determined by the
generator-image scalar $\rho_\lambda(\sigma_i) = \lambda_\sigma$,
which by the Iwahori-Hecke relation
$(\sigma_i - q)(\sigma_i + q^{-1}) = 0$ must satisfy
$\lambda_\sigma \in \{+q,\, -q^{-1}\}$.  The two choices give the
trivial and sign 1-d irreps respectively (per
`prop:hecke-branching-trace-decomposition`).

For a typed braid $\beta = c_1 c_2 \cdots c_L$ with crossings
$c_\ell \in \{\sigma_i,\, \sigma_i^{-1},\, \sigma_i - h/2\}$, the
1-d action is multiplicative:

$$
  \rho_\lambda(\beta) \;=\; \prod_{\ell=1}^{L} \rho_\lambda(c_\ell),
$$

with the three crossing types contributing:

$$
\begin{aligned}
  \rho_\lambda(\sigma_i)              &= \lambda_\sigma, \\
  \rho_\lambda(\sigma_i^{-1})         &= \lambda_\sigma^{-1}, \\
  \rho_\lambda(\sigma_i - \tfrac{h}{2}\mathbf{1})
                                       &= \lambda_\sigma - \tfrac{h}{2}.
\end{aligned}
$$

Hence

$$
  \rho_\lambda(\beta)
   \;=\;
   \lambda_\sigma^{w(\beta)} \cdot
   \bigl(\lambda_\sigma - \tfrac{h}{2}\bigr)^{m(\beta)} .
$$

The $q$-character $\chi^\lambda_q(\beta) = \mathrm{tr}_{V_\lambda} \rho_\lambda(\beta) = \rho_\lambda(\beta)$
(trace on 1-d space).  Substituting $\lambda_\sigma = +q$ and using
$q - h/2 = q - (q - q^{-1})/2 = (q + q^{-1})/2 = [2]_q/2$:

$$
  \chi^{(n)}_q(\beta) \;=\; q^{w(\beta)} \cdot \bigl(\tfrac{[2]_q}{2}\bigr)^{m(\beta)}.
$$

Similarly $\lambda_\sigma = -q^{-1}$ gives $-q^{-1} - h/2 = -[2]_q/2$, so

$$
  \chi^{(1^n)}_q(\beta) \;=\; (-q^{-1})^{w(\beta)} \cdot \bigl(-\tfrac{[2]_q}{2}\bigr)^{m(\beta)}.
$$

The formulas hold for every $n$ because the 1-d Hecke irreps' generator
eigenvalues $\pm q^{\pm 1}$ are *substrate-derived* — they come from the
Hecke quadratic relation, not from any $n$-specific representation
combinatorics. $\blacksquare$
