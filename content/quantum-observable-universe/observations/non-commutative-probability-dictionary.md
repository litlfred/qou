The Hecke-algebra GNS data
([algebraic GNS embedding](#prop:algebraic-gns-embedding))
forms a non-commutative probability space in Voiculescu's sense
[`biane1998`]: a unital $*$-algebra equipped with a tracial state.
Under this reading, every QOU-internal computation involving the
Markov trace has a probabilistic translation.

**The dictionary.**

See [Table](#tbl:non-commutative-probability-dictionary-table-data).

**Three structural facts that follow.**

1. **Knot theory is the moment theory of QOU's non-commutative
   probability space.** Every closed-braid knot invariant
   ($J_K(q)$, colored Jones, HOMFLY, Khovanov categorifications) is
   a specific joint moment of transfer matrices under $\mathrm{tr}_M$.
   Knot tables are joint-moment tables; the Kashaev volume conjecture
   is a free-entropy-style log-asymptotic of moments.

2. **Wedderburn idempotents are events.** The central projectors
   $e_\lambda$ satisfy $1 = \sum_\lambda e_\lambda$ and
   $e_\lambda^2 = e_\lambda$, $e_\lambda e_\mu = 0$ for $\lambda \neq \mu$
   — they partition the unit into a non-commutative analogue of
   measurable events. The Plancherel measure $\tilde w_\lambda =
   \mathrm{tr}_M(e_\lambda)$ assigns probability mass to each event:
   $\mathrm{tr}_M(x) = \sum_\lambda \tilde w_\lambda \cdot \chi_\lambda(x)$
   is the **law of total probability** in this space.

3. **Jucys–Murphy elements are commuting random variables.** The
   elements
   $J_k = \sigma_{k-1} \sigma_{k-2} \cdots \sigma_1 \sigma_1 \cdots \sigma_{k-2} \sigma_{k-1}$
   commute pairwise and generate the maximal abelian subalgebra
   (Gelfand–Tsetlin). Biane proved that in the large-$n$ limit at
   $q = 1$, suitably normalised $J_k$'s become *free random
   variables* with semicircle distribution
   [`biane1998`]; the q-deformed version (Féray–Méliot 2010, q-CLT
   below) replaces semicircle with the q-Gaussian
   [`marsh2006`].

**This reading is not metaphor.** It is the precise statement that
the Hecke algebra under the Markov trace is a non-commutative
$(W^*, \mathrm{tr})$ probability space in the sense of Voiculescu,
and every theorem about such spaces applies directly to QOU. The
q-CLT below
(q-CLT for Hecke transfer matrices)
makes this explicit by stating the central limit theorem in the
QOU setting.

**Imported tools.** Through this dictionary, QOU inherits the
analytic machinery of free probability and asymptotic representation
theory: Voiculescu's R-/S-transforms, Speicher's free cumulants
(non-crossing partitions), free entropy, Biane's asymptotic
representation theory of $S_\infty$, Jones–Wenzl subfactor planar
algebra. Random matrix theory's large-$N$ universality results apply
to QOU expectations under the q-Plancherel limit; Kashaev's volume
conjecture reads as a free-entropy / log-moment-asymptotic identity.
