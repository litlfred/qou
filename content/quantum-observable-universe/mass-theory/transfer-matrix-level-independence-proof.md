**(1) Constituent-composite agreement.**
By
([constituent-composite agreement](#lem:tmli-constituent-composite-agreement)),
the constituent product $\prod \hat{V}_i^{\mathrm{const}}$ equals the
composite Markov trace
$\mathrm{tr}_M(\rho(\beta_{\mathfrak{H}})) = P_{K_{\mathfrak{H}}}(q)$
as exact elements of $H_N(q)$.

**(2) Path independence on $\mathcal{S}_p$.**
All braiding takes place within the exceptional divisor
([vertex operators factor through $\mathcal{S}_p$](#prop:vertex-is-exceptional-divisor)).
Two braiding operations $T_1, T_2$ that produce isotopy-equivalent
configurations have braid words $\beta_1, \beta_2$ whose closures
$\hat{\beta}_1, \hat{\beta}_2$ are ambient-isotopic.  By the
link invariance of the Markov trace
([Jones--Markov trace](#thm:jones-markov-trace), property 3),
$\mathrm{tr}_M(\rho(\beta_1)) = \mathrm{tr}_M(\rho(\beta_2))$.
Hence $\hat{V}(T_1) = \hat{V}(T_2)$ and $\mathcal{T}(T_1) = \mathcal{T}(T_2)$.

The specific sequence of crossings within $\mathcal{S}_p$ does not matter:
all that matters is the isotopy class of the resulting link.  The
blow-down map $\pi$ collapses $\mathcal{S}_p$ to $p$, erasing the
internal history.

**(3) Well-definedness.**
Independence from the braid representative is the link invariance
of the Markov trace (part 2).  Independence from the PawLei
embedding follows from the $q$-Schur--Weyl duality: any two
embeddings $\iota, \iota'$ of $V_{j_i}$ into $V^{\otimes 2j_i}$
differ by an element of the Iwahori--Hecke algebra centralizer, which
commutes with the Markov trace.  Independence from the order of
crossing evaluation follows from the right-to-left peeling argument
in the Markov trace product
([Markov trace product](#thm:markov-trace-product)): the
generators are peeled in decreasing order, and the result is
independent of the order in which crossings at a fixed generator
were originally applied.  $\square$
