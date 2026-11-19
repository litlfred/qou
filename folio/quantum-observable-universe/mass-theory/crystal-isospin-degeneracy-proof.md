**Proof.**
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
The crystal model takes $\sigma_i^{-1}$ to act by the same sign on
the same line:

$$
  \sigma_i^{-1} : T \;\longmapsto\; \mathrm{sign}(\rho_T(i)) \cdot T
  \;=\; \sigma_i \cdot T
$$

acting on the same SYT eigenline.  This is an input of the model
(the `abs(i)` reduction in `term7_alpha5_crystal_derivation.py`),
not a consequence of the Hecke relation.  The relation
$(\sigma_i - q)(\sigma_i + q^{-1}) = 0$ cannot be specialised at
$q = 0$, because $q^{-1}$ is undefined there.  At generic $q$ it
gives $\sigma_i^{-1} = \sigma_i - (q - q^{-1})$, so $\sigma_i$ has
eigenvalues $q, -q^{-1}$ while $\sigma_i^{-1}$ has $q^{-1}, -q$; the
two are not equal on any line.  In the seminormal form $\sigma_i$ is
also not diagonal on the SYT basis: it mixes $T$ with $s_i T$
whenever $i$ and $i+1$ lie in different rows and columns of $T$.  The crystal-limit generators
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
weight $w_\lambda(q = 1) = (f^\lambda)^2 / (3A)!$ yields the claim.  $\square$

**Conditional corollary (legacy disjoint-product convention).**
*Suppose tritium and helium-3 are presented by the simplified
disjoint-product words used by
the canonical formalism*

$$
  \tilde\beta_T = \sigma_1\sigma_2\sigma_1^{-1}\sigma_4\sigma_5^{-1}\sigma_4
              \sigma_7\sigma_8^{-1}\sigma_7,
  \qquad
  \tilde\beta_{{}^3\mathrm{He}} = \sigma_1\sigma_2\sigma_1^{-1}\sigma_4\sigma_5\sigma_4^{-1}
              \sigma_7\sigma_8^{-1}\sigma_7
$$

*(differing only at positions $5$ and $6$ by paired inversion).
Then*

$$
  S_{\mathrm{crystal}}(\tilde\beta_T) \;=\; S_{\mathrm{crystal}}(\tilde\beta_{{}^3\mathrm{He}}),
$$

*matching the witness
[`term7-alpha5-crystal-derivation.witness.json`](../../../computations/term7-alpha5-crystal-derivation.witness.json)
which records both values to fifty decimal digits as
$0.0020612874779541296$.*

**Caveat — this corollary is *not* a statement about physical
${}^3\mathrm{H}$ vs.\ ${}^3\mathrm{He}$.** Under the canonical
$\bowtie_K$-coupled convention
the canonical formalism,
${}^3\mathrm{H}$ has interface types $(pn{=}\bowtie_K,\;nn{=}\sigma^{-1})$
while ${}^3\mathrm{He}$ has $(pp{=}\sigma,\;pn{=}\bowtie_K)$ — the
words differ in *interface type*, not just generator signs, so the
sign-flip proposition does not apply directly.  The legacy
disjoint-product witness for the Term-7 $\alpha_5$ crystal derivation
artificially erases this isospin asymmetry.
