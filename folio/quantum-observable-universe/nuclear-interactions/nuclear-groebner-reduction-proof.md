## Proof

Uniqueness of the normal form relies on the confluence half of the Gröbner--Shirshov (Diamond Lemma) machinery applied to $H_A(q)$.

1. **The relation set $G$ is a Gröbner--Shirshov basis.** The three families — the Hecke quadratic $\sigma_i^2 - (q - q^{-1})\sigma_i - 1$, the braid relation $\sigma_i\sigma_{i+1}\sigma_i - \sigma_{i+1}\sigma_i\sigma_{i+1}$, and far commutativity $\sigma_i\sigma_j - \sigma_j\sigma_i$ ($|i - j| \ge 2$) — are closed under composition with respect to the length-lexicographic order. Every overlap ambiguity ($\sigma_i^3$, the $\sigma_i\sigma_{i+1}\sigma_i\sigma_{i+1}$ overlap, and far-commutation triples) reduces to zero. This verifies classical admissibility for the [Gröbner--Shirshov basis](#unital-groebner-bases:def:groebner-basis) of the Iwahori--Hecke algebra.

2. **Confluence ensures a path-independent remainder.** By the Diamond Lemma \cite{bergman1978}, a confluent rewriting system yields a remainder under the [division algorithm](#unital-groebner-bases:def:division-algorithm) independent of the reduction path. Thus, $r(\mathcal{N}_{\mathrm{raw}}(Z, N), G)$ specifies a unique normal form $\mathcal{N}(Z, N)$ in $H_A(q)$.

3. **Termination.** Length-lexicographic order well-orders positive braid monomials. Each rule strictly decreases this order, guaranteeing termination. Combined with confluence — which reduces directly to the general [admissible system](#unital-groebner-bases:def:admissible-system) criterion — this establishes both existence and uniqueness.
$\square$
