Two constructions:

1. **Laplace transform.**  By
   ([existence of categorical Laplace transform](#prop:categorical-laplace-exists)),
   $\mathcal{L}[\exp(-t \widehat{\Delta_q})](s)$ is well-defined for
   every $s$ in the domain of the Laplace pairing.  The resulting
   morphism equals $R_q(s)$ by the spectral identity
   $\int_0^\infty e^{-(s + \lambda)t} dt = (s + \lambda)^{-1}$.

2. **Peter--Weyl diagonal.**  Under the Fourier decomposition of
   $\widehat{\Delta_q}$ with eigenvalues $\lambda_j(q)$, define
   $R_q(s) = \bigoplus_j \pi_j / (s + \lambda_j(q))$ on each
   isotypic summand.  This is well-defined whenever $s + \lambda_j(q) \ne 0$
   for every $j$ — i.e. outside the categorical spectrum.  The
   direct sum converges formally in $\mathrm{End}(\bigoplus_j V_j \otimes V_j^\vee)$.

Both constructions yield the same morphism.
