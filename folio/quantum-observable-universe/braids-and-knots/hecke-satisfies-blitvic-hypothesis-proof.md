*Proof.* Reduce an arbitrary joint moment of centred generators
to a pair-partition sum by induction on word length.

**Setup.** Let $\tilde\sigma_i := \sigma_i - z \cdot 1$ where
$z = q^3/(q^2+1) = \mathrm{tr}_M(\sigma_i)$ (**convention D**; under the
excised convention C the shift $\sigma_i - z\cdot 1$ was not centred at all,
leaving $\mathrm{tr}_M(\tilde\sigma_i) = 0.1134$ rather than $0$), so that
$\mathrm{tr}_M(\tilde\sigma_i) = 0$. The argument uses only joint
$\mathrm{tr}_M$-moments of the $\tilde\sigma_i$; no adjoint structure
is required. (Note that
$\mathrm{tr}_M(\sigma_i^{-1}) = z - (q - q^{-1}) \neq z$
([Markov axioms](#rem:markov-axioms-primitive)), so $\tilde\sigma_i$
is not fixed by the bar-involution $\sigma_i \mapsto \sigma_i^{-1}$;
Blitvić's hypothesis is a moment condition and does not need it.)

**Odd length vanishes.** For $k$ odd, every reduction of
$\tilde\sigma_{i_1} \tilde\sigma_{i_2} \cdots \tilde\sigma_{i_k}$
via the Hecke relation leaves at least one unmatched single
$\tilde\sigma_i$ factor; by Markov property applied at that factor,
$\mathrm{tr}_M(x \cdot \tilde\sigma_i) = \mathrm{tr}_M(x \cdot \sigma_i) -
z \mathrm{tr}_M(x) = z \mathrm{tr}_M(x) - z \mathrm{tr}_M(x) = 0$.
The entire word vanishes under $\mathrm{tr}_M$.

**Even length reduces to pair-partitions.** For $k$ even, proceed
by induction on the number of generator types appearing. The base
case $k = 2$ is the variance computation:
$$
  \mathrm{tr}_M(\tilde\sigma_i \tilde\sigma_j)
  \;=\;
  \mathrm{tr}_M(\sigma_i \sigma_j) - z\,\mathrm{tr}_M(\sigma_i) -
  z\,\mathrm{tr}_M(\sigma_j) + z^2.
$$
For $i \neq j$ with $|i - j| \geq 2$, far-commutativity gives
$\sigma_i \sigma_j = \sigma_j \sigma_i$ and the trace property
yields $\mathrm{tr}_M(\sigma_i \sigma_j) = z^2$; the centred moment
is $z^2 - z^2 - z^2 + z^2 = 0$.

For $i = j$, apply the Hecke quadratic relation:
$\sigma_i^2 = (q - q^{-1}) \sigma_i + 1$, so
$\mathrm{tr}_M(\sigma_i^2) = (q - q^{-1}) z + 1$. The centred moment
is
$$
  \mathrm{tr}_M(\tilde\sigma_i^2)
  \;=\;
  (q - q^{-1}) z + 1 - 2 z^2 + z^2
  \;=\;
  (q - q^{-1}) z + 1 - z^2,
$$
which is positive for every real $q > 0$ under convention D.

The general matching is therefore
$\mathrm{tr}_M(\tilde\sigma_i \tilde\sigma_j) =
\bigl[(q - q^{-1}) z + 1 - z^2\bigr] \cdot \delta_{i = j}$,
which is the case $k = 2$ of the pair-partition formula.

**Inductive step.** For general $k$, apply the Hecke quadratic
relation iteratively to reduce any repeated generator
$\sigma_i^2$ to a lower-degree word. This produces a tree of
reductions whose leaves are square-free generator products; each
leaf evaluates under $\mathrm{tr}_M$ via Wenzl's product
factorisation
([Markov locality of single Hecke crossings](#prop:trace-locality-meets-gs-non-locality)).
The factorisation pairs each $\tilde\sigma_i$ with another
$\tilde\sigma_j$ of the same index (Kronecker $\delta_{i=j}$) — any
unmatched generator gives zero by Markov property as above.

The induction shows the joint moment is a sum, indexed by
pair-partitions $\pi$ of $\{1, \ldots, k\}$, of products of
length-2 moments times a crossing-count weight from the braid
relations. Explicitly:
$$
  \mathrm{tr}_M\bigl(\tilde\sigma_{i_1} \cdots \tilde\sigma_{i_k}\bigr)
  \;=\;
  \sum_{\pi \in P_2(k)}
    q^{\mathrm{cr}(\pi)} \cdot
    \prod_{\{a, b\} \in \pi}
      \bigl((q - q^{-1}) z + 1 - z^2\bigr) \cdot
      \delta_{i_a = i_b},
$$
where $\mathrm{cr}(\pi)$ is the number of crossings of $\pi$. This
matches Blitvić's $(q, t)$-Gaussian moment formula
[`blitvic2012`, eq. (1.2)] at parameter $(q, t = 1)$. $\square$
