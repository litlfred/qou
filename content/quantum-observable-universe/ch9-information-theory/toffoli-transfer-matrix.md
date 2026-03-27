**Proposition.**
*Let $M(q)$ be the $8 \times 8$ matrix whose $(m, k)$-entry
$P_{m,k}(q)$ is the topological amplitude from the $3$-strand
nuclear braid with input type assignment $k \in \{0,1\}^3$
to output type assignment $m \in \{0,1\}^3$, constructed from
the Hecke crossing coefficients
([transfer matrix product](#prop:skein-polynomial-transfer-matrix))
with the Toffoli constraint: strands $1, 2$ (controls) keep
their types, and strand $3$ (target) flips iff both controls
are $1$.*

*Then:*

1. **(Diagonal.)** $P_{k,k}(q) = \mathrm{tr}_{\mathrm{Markov}}
   \bigl(\overline{\mathcal{N}(k)}\bigr)$ is the Skein
   polynomial of the $3$-strand nuclear braid with type
   assignment $k$.*

2. **(Destructive interference.)** $P_{m,k}(q) = 0$ for all
   off-diagonal entries except $(m, k) = (7, 6)$ and
   $(m, k) = (6, 7)$.  Every phase-flip pathway with fewer
   than two controls active interferes to zero.*

3. **(The q-AND.)**

$$
  P_{7,6}(q)
  \;=\;
  \frac{
    (q - 1)\,(q^{3/2} + q^{1/2} - 1)\,(q^{3/2} + q + 1)
  }{
    2\,(q + 1)^2
  }
$$

4. **(Antisymmetry.)** $P_{6,7}(q) = -P_{7,6}(q)$.*

5. **(Classical limit.)** $P_{7,6}(q) \to 0$ as $q \to 1$.
   The q-AND amplitude carries the factor $(q - 1)$ and
   vanishes identically at the classical limit.*

6. **(Toffoli block.)**

$$
  P_{7,7}(q) = \frac{q + q^{1/2} - 1}{q + 1}
$$

*This entry vanishes at $q = 1/\varphi^2$
([golden ratio degeneration](#rem:golden-ratio-degeneration)):
the all-proton diagonal amplitude has a zero at the golden
ratio threshold.*

*Proof.*
On $3$ strands, the chain reduction
([transfer matrix product](#prop:skein-polynomial-transfer-matrix))
produces two generators $\sigma_0, \sigma_1$ with traced volumes
$\hat{V}_0(q), \hat{V}_1(q)$.

**Diagonal entries.**  For each type assignment
$k = (k_1, k_2, k_3) \in \{0,1\}^3$, the ordering
$[k_1, k_2, k_3]$ determines the crossing coefficients at
each pair.  The Markov trace is
$P_{k,k} = \hat{V}_0^{(k)} \cdot \hat{V}_1^{(k)}$.

**Off-diagonal entries.**  The Toffoli gate maps
$|k_1 k_2 k_3\rangle \to |k_1 k_2 (k_3 \oplus k_1 k_2)\rangle$.
The $1$-jet transition amplitude at converting generator
$\sigma_i$ is:

$$
  \Delta_i(q) = \hat{V}_i^{(\mathrm{par})}(q) - \hat{V}_i^{(\mathrm{dau})}(q)
$$

where "parent" is the input ordering and "daughter" is the
output ordering (one type flipped at strand $3$).  The full
transition amplitude is:

$$
  P_{m,k}(q) = \sum_{i=0}^{1}
  \biggl[\prod_{j \neq i} \hat{V}_j^{(\mathrm{par})}(q)\biggr]
  \cdot \Delta_i(q)
$$

**Why only $(7,6)$ and $(6,7)$ are non-zero.**
The transition requires strand $3$ to change type ($0 \to 1$
or $1 \to 0$), which changes a crossing from mixed to
$\mathfrak{p}\mathfrak{p}$ (or vice versa).

When either control is $0$ (neutron), the crossing of that
control with the target is already mixed in both parent and
daughter orderings.  Only the other crossing (between the
control and target) could change — but if the other control
is also $0$, the crossing of controls is
$\mathfrak{n}\mathfrak{n}$ in both orderings.  In all cases,
$\Delta_i = 0$ at every generator when fewer than two controls
are active.

When both controls are $1$: the crossing of each control with
the target changes from mixed $(c, d) = ((1 + q^2)/2, -qs/2)$
to $\mathfrak{p}\mathfrak{p}$ $(c, d) = (1, 0)$.  This
produces $\Delta_0 \neq 0$ (strand $0$ crosses strand $2$,
whose type changes) while $\Delta_1 = 0$ (strand $1$ only
crosses strand $2$ at generator $\sigma_1$, and
$\hat{V}_1 = z$ for both orderings since the single crossing
at $\sigma_1$ depends on strands $1$ and $2$ where strand $1$
is fixed as proton).

The factored form follows by direct computation of the
chain reduction with the paper's crossing coefficients.

**Antisymmetry.**  The reverse transition ($1 \to 0$ flip)
uses daughter-minus-parent instead of parent-minus-daughter
at the converting generator.  Since the non-converting
context $\prod_{j \neq i} \hat{V}_j$ is the same (it uses
the parent ordering in both directions by convention),
$P_{6,7} = -P_{7,6}$.

**Classical limit.**  At $q = 1$: $s = 0$, so
$T_{pp} = T_{nn} = T_{\mathrm{mix}}$.  All crossing types
coincide, hence $\Delta_i = 0$ for every transition.  The
factor $(q - 1)$ in the numerator confirms this.

**Golden ratio zero of $P_{7,7}$.**  The numerator
$q + q^{1/2} - 1$ vanishes when $q^{1/2} = (\sqrt{5} - 1)/2
= 1/\varphi$, i.e., $q = 1/\varphi^2 = (3 - \sqrt{5})/2$.
$\square$

**Explicit values at $q = 1.110$:**

| Entry | Symbolic | Numerical |
|:-----:|----------|:---------:|
| $P_{6,6}$ | $\frac{q^4 + q^{7/2} + 2q^{3/2} + q^{1/2} - 1}{2(q+1)^2}$ | $0.6010$ |
| $P_{7,6}$ | q-AND (above) | $+0.0495$ |
| $P_{6,7}$ | $-P_{7,6}$ | $-0.0495$ |
| $P_{7,7}$ | $\frac{q + q^{1/2} - 1}{q + 1}$ | $0.5515$ |
