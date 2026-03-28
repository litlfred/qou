**(1) Constituent-composite agreement.**
The hadron $H \hookrightarrow V^{\otimes 2(j_1 + \cdots + j_n)}$
embeds into a tensor power of $V$ via the PawLei basis
([knot factorization](#rem:knot-factorization)).  The braid word
$\beta_H \in B_N$ (where $N = 2(j_1 + \cdots + j_n)$) acts on
$V^{\otimes N}$ through the Hecke algebra $H_N(q)$.

At the **constituent level**, the crossings between $K_i$ and
$K_j$ are grouped by generator index, and the Markov trace factors
as $\prod \hat{V}_i^{\mathrm{const}}$
([Markov trace product](#thm:markov-trace-product)).

At the **composite level**, the same braid word $\beta_H$ has a
unique Hecke reduction in $H_N(q)$, and the Markov trace yields
$P_{K_H}(q) = \mathrm{tr}_M(\rho(\beta_H))$.

These are equal because the Markov trace product formula is an
**exact algebraic identity** in $H_N(q)$: the product
$\prod \hat{V}_i$ and the direct trace $\mathrm{tr}_M(\rho(\beta_H))$
evaluate the same element of $H_N(q)$.  The factorization is not
an approximation --- it is a rewriting of the trace using the
Markov property.

**(2) Path independence on $\mathcal{S}_p$.**
All braiding takes place within the exceptional divisor
([vertex operators factor through $\mathcal{S}_p$](#prop:vertex-is-exceptional-divisor)).
Two braiding operations $T_1, T_2$ that produce isotopy-equivalent
configurations have braid words $\beta_1, \beta_2$ whose closures
$\hat{\beta}_1, \hat{\beta}_2$ are ambient-isotopic.  By the
link invariance of the Markov trace
([Jones--Markov trace](#thm:jones-markov-trace), property 3),
$\mathrm{tr}_M(\rho(\beta_1)) = \mathrm{tr}_M(\rho(\beta_2))$.
Hence $\hat{V}(T_1) = \hat{V}(T_2)$ and $\mathcal{T}(T_1)
= \mathcal{T}(T_2)$.

The specific sequence of crossings within $\mathcal{S}_p$ does not matter:
all that matters is the isotopy class of the resulting link.  This
is the content of "what happens in the exceptional divisor stays in
the exceptional divisor" --- the blow-down map $\pi$ collapses
$\mathcal{S}_p$ to $p$, erasing the internal history.

**(3) Well-definedness.**
Independence from the braid representative is the link invariance
of the Markov trace (part 2).  Independence from the PawLei
embedding follows from the $q$-Schur--Weyl duality: any two
embeddings $\iota, \iota'$ of $V_{j_i}$ into $V^{\otimes 2j_i}$
differ by an element of the Hecke algebra centralizer, which
commutes with the Markov trace.  Independence from the order of
crossing evaluation follows from the right-to-left peeling argument
in the Markov trace product
([Markov trace product](#thm:markov-trace-product)): the
generators are peeled in decreasing order, and the result is
independent of the order in which crossings at a fixed generator
were originally applied.  $\square$
