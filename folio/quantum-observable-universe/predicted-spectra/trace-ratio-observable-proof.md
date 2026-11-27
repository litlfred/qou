From the factorization theorem:

$$
  \frac{\mathrm{tr}(\mathcal{N}(Z, N))}
       {\mathrm{tr}(\mathcal{N}(p+1, n-1))}
  = 
  \frac{\prod_{i=0}^{A-2} \hat{V}_i^{\mathrm{par}}}
       {\prod_{i=0}^{A-2} \hat{V}_i^{\mathrm{dau}}}
  = 
  \prod_{i=0}^{A-2}
  \frac{\hat{V}_i^{\mathrm{par}}}{\hat{V}_i^{\mathrm{dau}}}.
$$

For generators $i > p$, the crossings from nucleon $i$ to nucleons $j > i$ are identical in parent and daughter because neither nucleon $i$ nor any $j > i$ changed type. Therefore $\hat{V}_i^{\mathrm{par}} = \hat{V}_i^{\mathrm{dau}}$ and the ratio is $1$. Only generators $i \leq p$ contribute.

The transition matrix element is the Skein amplitude at the beta-decay vertex, which is proportional to the trace ratio:

$$
  |\mathcal{M}_q|^2
  = 
  |\mathrm{skein\_amp}|^2
  \cdot
  \left|
    \frac{\mathrm{tr}(\mathcal{N}(Z, N))}
         {\mathrm{tr}(\mathcal{N}(p+1, n-1))}
  \right|^2
$$

where $\mathrm{skein\_amp} = q^{1/2} - q^{-1/2}$. $\square$
