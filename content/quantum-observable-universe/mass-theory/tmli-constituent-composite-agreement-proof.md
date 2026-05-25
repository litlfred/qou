**Proof.**
The hadron $\mathfrak{H} \hookrightarrow V^{\otimes 2(j_1 + \cdots + j_n)}$
embeds into a tensor power of $V$ via the PawLei basis
([knot factorization](#rem:knot-factorization)).  The braid word
$\beta_{\mathfrak{H}} \in B_N$ (where $N = 2(j_1 + \cdots + j_n)$) acts on
$V^{\otimes N}$ through the Iwahori--Hecke algebra $H_N(q)$.

At the **constituent level**, the crossings between $K_i$ and
$K_j$ are grouped by generator index, and the Markov trace factors
as $\prod \hat{V}_i^{\mathrm{const}}$
([Markov trace product](#thm:markov-trace-product)).

At the **composite level**, the same braid word $\beta_{\mathfrak{H}}$ has a
unique Hecke reduction in $H_N(q)$, and the Markov trace yields
$P_{K_{\mathfrak{H}}}(q) = \mathrm{tr}_M(\rho(\beta_{\mathfrak{H}}))$.

These are equal because the Markov trace product formula is an
**exact algebraic identity** in $H_N(q)$: the product
$\prod \hat{V}_i$ and the direct trace $\mathrm{tr}_M(\rho(\beta_{\mathfrak{H}}))$
evaluate the same element of $H_N(q)$.  The factorization is not
an approximation --- it is a rewriting of the trace using the
Markov property.  $\square$
