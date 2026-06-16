The two-chain decomposition
([knot operations and $\lambda$](#rem:markov-lambda-knot-operations))
--- an outer chain on partitions (stabilization / Markov II) and
an inner chain on SYTs (generators $\sigma_i$ inside $V_\lambda$) ---
has quantitative error bounds already established elsewhere in
the paper.  This remark matches each chain layer to its
controlling bound and flags a standard CLT framework that
**fails** in this paper's regime.

## Outer chain: $q$-Plancherel CLT (Féray--Méliot)

The outer chain samples $\lambda \vdash n$ under the normalised
Ocneanu weights $\pi_\lambda(q)$, which at generic $q$ are the
$q$-Plancherel measure on the Young lattice.  Fluctuations of
the jet-filtered invariant $a_k(\beta) \to a_\infty(\beta)$
around the dimension-weighted average are controlled by the
Féray--Méliot $q$-Plancherel CLT \cite{feray-meliot2012}:

$$
  \bigl\lvert a_k(\beta) - a_\infty(\beta) \bigr\rvert
  \;=\; O\!\bigl(k^{-1/2}\bigr),
$$

with explicit constants worked out in
[jet convergence](#conj:jet-convergence-classical-limit).
This is the standard Gaussian CLT rate transported to the
$q$-deformed Plancherel measure.

## Inner chain: Perron--Frobenius, not Bożejko--Speicher

The inner chain on $\mathrm{SYT}(\lambda)$ is the natural venue
for a $q$-Gaussian CLT in the sense of Bożejko--Speicher, since
the generators satisfy the $q$-commutation $\sigma_i \sigma_{i+1} \sigma_i =
\sigma_{i+1} \sigma_i \sigma_{i+1}$ with Hecke quadratic $(\sigma_i - q)(\sigma_i + q^{-1})
= 0$.  However, the Bożejko--Speicher noncommutative $q$-Gaussian
**does not apply** at the substrate value $q_0 \approx 1.11 > 1$:
the Touchard pair-partition moments
$T_n(q_0) = \sum_\pi q_0^{\mathrm{cr}(\pi)}$ grow super-exponentially
in $n$, so no well-defined $q$-Gaussian distribution exists.
This failure is documented in the computation layer
(`computations/substrate/hecke_core.py`), which selects the
**Perron--Frobenius dominant eigenvalue** proxy instead:

$$
  \log\bigl\lvert \mathrm{tr}\,\rho^\lambda_q(W_N) \bigr\rvert
  \;\approx\;
  \log d_q(\lambda) \,+\, N \cdot \log\lvert \mu_\lambda \rvert,
$$

where $\mu_\lambda$ is the spectral radius of a typical crossing
$c \sigma + d \cdot I$ in the $\lambda$-irrep.  This estimate is
valid for every $q > 0$ (pure Perron--Frobenius for positive
operators), with the rate controlled by the spectral gap
$\mu_\lambda - \mu_\lambda^{(2)}$ and exponential in $N$.

## Operational layer: geometric rate on physical predictions

The composite of outer and inner chains feeds into the
Wedderburn mass formula, whose empirical error on stable nuclei
satisfies

$$
  \frac{\bigl\lvert M_k(Z, N) - M_{\mathrm{obs}}(Z, N) \bigr\rvert}
       {M_{\mathrm{obs}}(Z, N)}
  \;\leq\; C \cdot r^{-(k-3)},
  \qquad C \approx 0.001,\ r \approx 4
$$

([Hecke convergence bound](#prop:hecke-convergence-bound)).
This geometric rate is faster than either layer in isolation and
reflects cancellation between inner and outer fluctuations in
the trace pairing; one Hecke level $\approx$ one QCD loop order.

## Summary

| Layer | Observable | Controlling bound | Rate |
|:---|:---|:---|:---|
| Outer ($\lambda \vdash n$) | $a_k \to a_\infty$ | Féray--Méliot $q$-Plancherel CLT | $O(k^{-1/2})$ |
| Inner ($\mathrm{SYT}(\lambda)$) | $\log\lvert\mathrm{tr}\,\rho^\lambda_q(W_N)\rvert$ | Perron--Frobenius spectral radius | $O(\mu_\lambda^{-N})$ remainder |
| Operational | $\lvert M_k - M_{\mathrm{obs}}\rvert/M_{\mathrm{obs}}$ | Wedderburn mass-formula error | $C \cdot r^{-(k-3)}$ |

**Caveat.** The natural candidate for an inner-chain CLT --- the
Bożejko--Speicher $q$-Gaussian --- **is not usable at $q_0 > 1$**.
Any approach that invokes a "$q$-Gaussian limit" for braid-word
observables at the physical substrate value is mis-applying the
framework.  The correct substitute is the Perron--Frobenius
dominant-eigenvalue estimate above.
