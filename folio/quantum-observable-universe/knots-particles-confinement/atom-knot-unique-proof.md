*Proof.*
The Markov trace on $B_n$ factors through the Hecke algebra: it is the
composite of the quotient map $B_n \to H_n(q)$, $\sigma_i \mapsto \sigma_i$,
with the Ocneanu trace on $H_n(q)$
([Jones–Markov trace](#thm:jones-markov-trace)). Two braids with the same
image $T_w$ in $H_n(q)$ therefore have the same Markov trace, and the trace
of a braid is the invariant of its closure. $\square$

**Scope.**
The previous version of this proof concluded that the closures are isotopic,
treating the Hecke quadratic relation $\sigma_i^2 = (q - q^{-1})\sigma_i + 1$
as a Reidemeister II move. It is not one: Reidemeister II is
$\sigma_i \sigma_i^{-1} = 1$, which holds already in $B_n$, while the
quadratic relation identifies braids that are not isotopic. Uniqueness of the
normal form (Diamond Lemma, [hecke normal form](#def:hecke-normal-form)) is a
statement about $H_n(q)$, not about $B_n$.
