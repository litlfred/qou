*Structural; holds over a generic commutative ring $R$.*

**Proposition.** Model a one-dimensional channel by its transmitted datum, a single trace value $\mathrm{tr}_M(\mathcal{F}) \in R$, and define the parallel placement $\mathcal{F}_A \parallel \mathcal{F}_B$ as the channel whose trace is the product

$$
  \mathrm{tr}_M(\mathcal{F}_A \parallel \mathcal{F}_B) \;:=\; \mathrm{tr}_M(\mathcal{F}_A)\,\mathrm{tr}_M(\mathcal{F}_B).
$$

Then parallel placement is associative and commutative, and the vacuum channel (trace $1$) is a two-sided identity. Channels under parallel placement form a commutative monoid.

The product rule is the definition of $\parallel$ here, not a consequence. Its physical motivation is that cladding makes the joint configuration a split link, and the Markov trace is multiplicative over split links; that link-level argument is not part of this statement.
