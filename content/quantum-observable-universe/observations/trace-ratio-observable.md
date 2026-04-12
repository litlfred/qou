The Markov trace of the nuclear braid is a link invariant that
grows exponentially with $A$
([Markov trace factorization](#thm:markov-trace-factorization)).
The physical observable — the transition matrix element
$|\mathcal{M}_q|^2$ — is the **ratio** of parent and daughter
traces, where the exponential growth cancels.

**Proposition.**
The beta-decay matrix element squared is proportional to the
ratio of Markov-traced generator volumes at the affected
generators:

$$
  |\mathcal{M}_q|^2
   \propto 
  \prod_{i=0}^{p}
  \left|
    \frac{\hat{V}_i^{\mathrm{par}}}{\hat{V}_i^{\mathrm{dau}}}
  \right|^2
$$

where $\hat{V}_i = z \cdot a_i + b_i$ is the Markov-traced
generator volume at $\sigma_i$, and the product runs only over
generators $i \leq p$ (those affected by the conversion of
nucleon $p$ from neutron to proton).  Generators $i > p$ cancel
exactly between parent and daughter.

**Proof.**
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

For generators $i > p$: the crossings from nucleon $i$ to
nucleons $j > i$ are identical in parent and daughter (neither
nucleon $i$ nor any $j > i$ changed type).  Therefore
$\hat{V}_i^{\mathrm{par}} = \hat{V}_i^{\mathrm{dau}}$ and
the ratio is $1$.  Only generators $i = 0, \ldots, p$ contribute.

The transition matrix element is the Skein amplitude at the
beta-decay vertex, which is proportional to the trace ratio:

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

where $\mathrm{skein\_amp} = q^{1/2} - q^{-1/2}$.  $\square$
