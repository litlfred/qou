The Iwahori–Hecke algebra $H_n(R, q)$ is the unital associative algebra
with generators $\sigma_0, \ldots, \sigma_{n-2}$ modulo the three
defining relations: the quadratic relation (R1), the far-commutation
relation (R2), and the braid cubic relation (R3). Its full type-theoretic
realization decomposes into four constructions — a free $R$-module on
$B_n$, a multiplication structure, the quotient by the three relations,
and the per-block Wedderburn decomposition (the $q$-deformed Schur–Weyl
splitting $\sum_\lambda y_\lambda = 1$).

The Lean class scaffold (`HeckeGen n`, `HeckeWord n`, `HeckeRelations n q`,
`HeckeWedderburn n q`) encodes the abstract generators, formal signed
words, the defining relations, and the Plancherel completeness as class
hypotheses. Downstream Lean theorems take `[HeckeRelations n q]` and
`[HeckeWedderburn n q]` as hypotheses; the per-$n$ instances plug in when
the relation-quotient and Murphy seminormal-form infrastructure land.
