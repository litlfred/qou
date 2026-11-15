**Proof.**
The argument decomposes into four steps.  By
([genus from Hecke completeness](#lem:genus-from-hecke-completeness)),
$g = 4$ is the least genus at which the embeddable
torus knots number at least the five irreducibles of
$H_2(q) \oplus H_3(q)$ -- a count, not a spanning statement
([the block-rank remark](#rem:torus-evaluation-block-rank)), so
$g = 4$ is taken as given here.  By
([Chebyshev degree = Seifert genus](#lem:chebyshev-degree-genus)),
the Hecke recurrence $a_{n+1} = s\,a_n + a_{n-1}$ produces
$\deg_u a_p = (p-1)/2 = g(T_{2,p})$ in the variable $u = s^2$,
with leading coefficient $1$.  By
([genus-filtration ideal characterisation](#lem:genus-ideal-characterisation)),
the truncation $\pi_4 \colon \mathbb{Z}[u] \to \mathbb{Z}[u]/(u^5)$
has kernel $\mathfrak{I}_4 = (u^5)$, identified with the Seifert
cycles that have no target in $H_1(\Sigma_4)$.  Finally, by
([Yekutieli leading coefficient](#lem:yekutieli-leading-coefficient)),
the obstruction $\kappa(T_{2,p})$ at level $n = 5$
equals the leading Chebyshev coefficient $c_{(p-1)/2} = 1$, which
is nonzero for $q \neq 1$.  Both characterisations therefore
agree.  $\square$
