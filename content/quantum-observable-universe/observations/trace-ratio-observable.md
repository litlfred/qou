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
