Out of the many Wedderburn--Artin partitions of the $3A$-strand Hecke algebra $H_{3A}(q)$, the macroscopic Markov trace $\mathrm{tr}_M$ of the canonical atom braid concentrates on a small subset of "active" partitions. For $^4\mathrm{He}$ ($A = 4$, $12$ strands) the per-block fingerprint at $q_0$ is dominated by two-row partitions — $(9,3)$ carries $\approx 29.0\%$ of $|\mathrm{tr}_M|$ and $(8,4)$ carries $\approx 23.6\%$, with the two-row stratum as a whole carrying $\approx 92.7\%$ ([two-row dominance](#prop:he4-two-row-dominance)) — while many of the $77$ partitions of $12$ contribute nothing measurable (the sign block $(1^{12})$ contribution is $\approx 5 \times 10^{-10}$ in absolute terms).

**Conjecture (fusion bound on the active set).**
*The multi-nucleon atom braid of mass number $A$ factors through the sub-algebra $(H_3)^{\otimes A} \hookrightarrow H_{3A}$, with each nucleon in its totally symmetric ground state, the one-row partition $[3]$ of $H_3$. Consequently the topological support of the ground-state nucleus is bounded by the Littlewood--Richardson (induction-product) support of $[3]^{\otimes A}$:*

$$
  \mathrm{supp}\bigl(\mathrm{tr}_M\text{-active set}\bigr)
  \;\subseteq\;
  \bigl\{\, \lambda \vdash 3A \;:\; K_{\lambda,\,(3^A)} > 0 \,\bigr\}
  \;=\;
  \bigl\{\, \lambda \vdash 3A \;:\; \ell(\lambda) \le A \,\bigr\},
$$

*where $K_{\lambda,\,(3^A)}$ is the Kostka multiplicity of $\lambda$ in $[3]^{\otimes A}$ and $\ell(\lambda)$ is the number of rows. Every Wedderburn block with more than $A$ rows carries zero Markov-trace contribution for a ground-state nucleus.*

## The $^4\mathrm{He}$ ($A = 4$) fusion computation

Direct enumeration of the Kostka multiplicities $K_{\lambda,\,(3,3,3,3)}$ gives the decomposition of $[3]^{\otimes 4}$: the two-row components are

$$
  [12] \,\oplus\, 3\,[11,1] \,\oplus\, 6\,[10,2] \,\oplus\, 10\,[9,3]
  \,\oplus\, 11\,[8,4] \,\oplus\, 9\,[7,5] \,\oplus\, 4\,[6,6],
$$

together with the unique minimal-length rectangular component $[4,4,4]$ (multiplicity $1$) and $26$ further components with three or four rows, for $34$ non-vanishing components in total. The remaining $43$ partitions of $12$ — exactly those with five or more rows — have Kostka multiplicity $0$ and lie outside the fusion support.

Comparison with the observed fingerprint:

1. **Support exclusion.** Every partition with $\ell(\lambda) > 4$ is outside the fusion support; consistently, the sign block $(1^{12})$ contribution at $q_0$ is numerically indistinguishable from zero.
2. **Two-row dominance is compatible but not implied.** The fusion multiplicities are largest along the two-row strip ($10$ at $(9,3)$, $11$ at $(8,4)$), matching the empirically dominant blocks, but three-row components such as $(8,3,1)$ also sit inside the support (multiplicity $15$) and do contribute ($\approx 4\%$). The support bound explains which blocks *vanish*; the quantitative concentration onto the two-row stratum requires the Wenzl-weight and character factors of the trace itself.
3. **The $(4,4,4)$ block.** The fusion generates exactly one copy of $(4,4,4)$, identifying it as the unique minimal-length rectangular block inside the active set.

## Active-set truncation from the fusion bound

If the conjecture holds, any partition outside the fusion support of $[3]^{\otimes A}$ carries no topological information for a ground-state nucleus, and $A$-nucleon binding and mass-operator evaluations may be restricted to the fusion support without loss. This is the structural rationale for the active-set truncation used in the large-$A$ trace computations; the restriction from the full support to the empirically dominant two-row-plus-rectangular blocks is a further, quantitative truncation justified per isotope by the fingerprint data rather than by the fusion bound alone.
