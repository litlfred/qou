The crystal-limit character $\chi^\lambda_{\mathrm{crystal}}(\sigma)$
on a single Hecke generator $\sigma$ is, by
[crystal-graph realisation](#conj:crystal-graph-realization),
the trace of the signed-permutation action

$$
  \sigma_i : T \;\longmapsto\; \mathrm{sign}(\rho_T(i)) \cdot T,
  \qquad \rho_T(i) := c(T(i+1)) - c(T(i))
$$

on the standard-Young-tableaux basis $\mathrm{SYT}(\lambda)$, where
$c(\cdot)$ is the cell content
([content scaling](#prop:content-scaling-correspondence)).
The Hecke involutivity at $q = 0$ — equivalently, reading off the
relation $\sigma_i^{-1} = \sigma_i$ on the crystal sub-quotient from
the Hecke skein convention $(\sigma_i - q)(\sigma_i + q^{-1}) = 0$
specialised at $q = 0$ — gives

$$
  \sigma_i^{-1} : T \;\longmapsto\; \mathrm{sign}(\rho_T(i)) \cdot T
  \;=\; \sigma_i \cdot T
$$

acting on the same SYT eigenline.  The crystal-limit generators
therefore act *diagonally* on the SYT basis with eigenvalues
that are individually invariant under $\sigma_i \leftrightarrow
\sigma_i^{-1}$.  For any fixed $T \in \mathrm{SYT}(\lambda)$, the
eigenvalue product along a braid word

$$
  \mu^\lambda_T(\beta) \;:=\; \prod_{\ell \,\in\, \beta} \mathrm{eigval}_T(\ell)
$$

is therefore equal under $\beta \to \beta'$.  Note that
$\mu^\lambda_T$ is *not* the character $\chi^\lambda$ — it is the
eigenvalue product *on the line through $T$*; the character is the
trace

$$
  \chi^\lambda_{\mathrm{crystal}}(\beta) \;=\; \sum_{T \in \mathrm{SYT}(\lambda)}
      \mu^\lambda_T(\beta).
$$

The trace is *not* multiplicative in $\beta$, but it is a sum of
sign-flip-invariant per-eigenline contributions, so

$$
  \chi^\lambda_{\mathrm{crystal}}(\beta_A)
    \;=\; \sum_{T \in \mathrm{SYT}(\lambda)} \mu^\lambda_T(\beta_A)
    \;=\; \sum_{T \in \mathrm{SYT}(\lambda)} \mu^\lambda_T(\beta_A')
    \;=\; \chi^\lambda_{\mathrm{crystal}}(\beta_A')
$$

per partition.  Summing against the (sign-independent) Plancherel
weight $w_\lambda(q = 1) = (f^\lambda)^2 / (3A)!$ yields the claim.
$\qquad\blacksquare$
