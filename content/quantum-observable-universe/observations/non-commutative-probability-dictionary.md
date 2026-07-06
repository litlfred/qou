The Hecke-algebra GNS data ([algebraic GNS embedding](#prop:algebraic-gns-embedding))
forms a non-commutative probability space in Voiculescu's sense [`biane1998`]:
a unital $*$-algebra equipped with a tracial state. Every computation involving
the Markov trace admits a precise probabilistic translation.

**The dictionary.**

See [Table](#tbl:non-commutative-probability-dictionary-table-data).

**Three structural consequences.**

1. **Knot theory evaluates non-commutative moments.** Every closed-braid knot
   invariant (Jones, colored Jones, HOMFLY, Khovanov categorifications) evaluates
   a joint moment of transfer matrices under $\mathrm{tr}_M$. Knot tables
   function as joint-moment tables. The Kashaev volume conjecture operates as
   a free-entropy log-asymptotic of these moments.
2. **Wedderburn idempotents define events.** The central projectors $e_\lambda$
   satisfy $1 = \sum_\lambda e_\lambda$, $e_\lambda^2 = e_\lambda$, and
   $e_\lambda e_\mu = 0$ for $\lambda \neq \mu$. They partition the unit,
   forming non-commutative measurable events. The Plancherel measure
   $\tilde w_\lambda = \mathrm{tr}_M(e_\lambda)$ assigns probability mass to
   each event. The decomposition
   $\mathrm{tr}_M(x) = \sum_\lambda \tilde w_\lambda \cdot \chi_\lambda(x)$
   acts as the law of total probability.
3. **Jucys--Murphy elements are commuting random variables.** The elements
   $J_k = \sigma_{k-1} \sigma_{k-2} \cdots \sigma_1 \sigma_1 \cdots \sigma_{k-2} \sigma_{k-1}$
   commute pairwise, generating the maximal abelian subalgebra (Gelfand--Tsetlin).
   Biane showed that in the large-$n$ limit at $q = 1$, suitably normalized $J_k$
   converge to free random variables with semicircle distributions [`biane1998`].
   The $q$-deformed version (Féray--Méliot) replaces the semicircle with a
   $q$-Gaussian [`marsh2006`].

**Formal equivalence.** The Hecke algebra under the Markov trace formally
constitutes a $(W^*, \mathrm{tr})$ probability space. Theorems governing such
spaces apply directly. The subsequent $q$-CLT for Hecke transfer matrices
makes this explicit.

**Imported tools.** This mapping incorporates the analytic machinery of free
probability and asymptotic representation theory. We utilize Voiculescu's
R-/S-transforms, Speicher's free cumulants (non-crossing partitions), free
entropy, Biane's asymptotic representation theory of $S_\infty$, and the
Jones--Wenzl subfactor planar algebra. Random matrix theory's large-$N$
universality governs expectations under the $q$-Plancherel limit.
