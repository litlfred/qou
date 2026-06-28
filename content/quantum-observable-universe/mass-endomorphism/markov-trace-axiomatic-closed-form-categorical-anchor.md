## Categorical interpretation

This proposition is the **direct categorical-mass anchor** for the
proton: the formula $\operatorname{tr}_M(\sigma_1^7\sigma_2^4)(q)$
is the Frobenius integral on $H_3(q)$ evaluated on the canonical
atomic-braid representative of the proton's GB-filtration normal
form ([`prop:atomic-mass-gb-nf`](#prop:atomic-mass-gb-nf)). The
axiomatic derivation makes the construction independent of any
representation-theoretic parameterisation; in particular, it
bypasses [``](https://github.com/litlfred/qou/pull/546)'s
seminormal `IndexError` failure on $\sigma_2$ acting on shape $(3)$.

The contrast with the Plancherel-trace closed form is
notable: that form was *anti-self-reciprocal* under $q \leftrightarrow 1/q$
([`prop:markov-trace-antipode-polynomial-symmetry`](#prop:markov-trace-antipode-polynomial-symmetry)),
whereas this Markov-trace closed form is **not** anti-self-reciprocal —
the two traces are genuinely different categorical objects, both
finite linear combinations of irreducible characters but with
different weights ($w_\lambda$ Plancherel vs $y_\lambda$ Jones-Markov,
[`prop:mass-coefficient-shadow-price`](#prop:mass-coefficient-shadow-price)).
