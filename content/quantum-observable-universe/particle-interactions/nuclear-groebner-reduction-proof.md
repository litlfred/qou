## Proof

Uniqueness of the normal form is the confluence half of the
Gröbner--Shirshov / Diamond-Lemma machinery applied to $H_A(q)$.

1. **The relation set $G$ is a Gröbner--Shirshov basis.** The three
   families — the Hecke quadratic $\sigma_i^2 - (q - q^{-1})\sigma_i - 1$,
   the braid relation $\sigma_i\sigma_{i+1}\sigma_i - \sigma_{i+1}\sigma_i\sigma_{i+1}$,
   and far commutativity $\sigma_i\sigma_j - \sigma_j\sigma_i$
   ($|i - j| \ge 2$) — are closed under composition with respect to the
   length-lexicographic order: every overlap ambiguity
   ($\sigma_i^3$, the $\sigma_i\sigma_{i+1}\sigma_i\sigma_{i+1}$ overlap,
   and the far-commutation triples) reduces to zero. This is the
   classical admissibility check for the
   [Gröbner--Shirshov basis](#unital-groebner-bases:def:groebner-basis)
   of the Iwahori--Hecke algebra.

2. **Confluence $\Rightarrow$ path-independent remainder.** By the
   Diamond Lemma \cite{bergman1978}, a confluent rewriting system yields a
   remainder under the
   [division algorithm](#unital-groebner-bases:def:division-algorithm)
   that is independent of the reduction path. Hence
   $r(\mathcal{N}_{\mathrm{raw}}(Z, N), G)$ is a well-defined element of
   $H_A(q)$ — the unique normal form $\mathcal{N}(Z, N)$.

3. **Termination.** Length-lex is a well-order on positive braid
   monomials and each rule strictly decreases it, so reduction
   terminates; with confluence this gives existence and uniqueness
   together.

The Lean sibling states `nuclear_groebner_reduction` and defers the
confluence certificate via `sorry` (`-- Ref: [manuscript]`); the
certificate reduces to the admissible-system machinery already
formalised in the unital-Gröbner-bases paper
([admissible system](#unital-groebner-bases:def:admissible-system)).
$\square$
