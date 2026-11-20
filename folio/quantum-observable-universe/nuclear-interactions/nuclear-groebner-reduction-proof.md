## Proof

Uniqueness of the normal form relies on the confluence half of the Gröbner--Shirshov (Diamond Lemma) machinery applied to $H_A(q)$.

1. **The relation set $G$ is a Gröbner--Shirshov basis.** The defining relations of $H_A(q)$ — the Hecke quadratic $\sigma_i^2 - (q - q^{-1})\sigma_i - 1$, the braid relation, and far commutativity — are not closed under composition once $A \geq 4$. The overlap of the braid relation $\sigma_3\sigma_2\sigma_3 \to \sigma_2\sigma_3\sigma_2$ with far commutativity $\sigma_3\sigma_1 \to \sigma_1\sigma_3$ over the word $\sigma_3\sigma_2\sigma_3\sigma_1$ has composition $\sigma_2\sigma_3\sigma_2\sigma_1 - \sigma_3\sigma_2\sigma_1\sigma_3$, and both of its words are irreducible for those three families ([Hecke normal form](#def:hecke-normal-form)). That composition is, up to sign, the Bokut--Shiao relation at $(i, j) = (3, 1)$. Adjoining the whole Bokut--Shiao family \cite{bokut2001} closes the system: every composition of the completed set $G$ reduces to zero, so $G$ is a [Gröbner--Shirshov basis](#unital-groebner-bases:def:groebner-basis) of the Iwahori--Hecke algebra for the length-lexicographic order.

2. **Confluence ensures a path-independent remainder.** Every element of $G$ has leading coefficient $1$. By the Diamond Lemma \cite{bergman1978}, the rewriting system of a Gröbner--Shirshov basis with unit leading coefficients is confluent, so the remainder under the [division algorithm](#unital-groebner-bases:def:division-algorithm) is independent of the reduction path. Thus $r(\mathcal{N}_{\mathrm{raw}}(Z, N), G)$ specifies a unique normal form $\mathcal{N}(Z, N)$ in $H_A(q)$.

3. **Termination.** Length-lexicographic order well-orders the monomials. Each reduction step removes its leading monomial and introduces only smaller ones, so every reduction sequence terminates. Combined with confluence, this establishes both existence and uniqueness.

<<<<<<< HEAD
The Lean formalisation of the three steps lives in the unital-Gröbner-bases development. The failure of the three defining families at $A = 4$ is machine-checked (`NotAGSBasis.hecke_not_gs_basis_four`), and the completed system is proved to be a Gröbner--Shirshov basis for every $A$ (`heckeCompleted_isGrobnerShirshovBasis`, for real $q > 0$, $q \neq 1$). Termination is proved (`reduction_well_founded`). The local-confluence half of the Diamond Lemma is still taken as an axiom (`local_confluence`, citing \cite{bergman1978}). The block's own Lean sibling states only the existence of a reduced form (`nuclear_groebner_reduction`).
=======
A complete confluence certificate is not supplied here; it is deferred \cite{leitner2026} and reduces to the admissible-system machinery of the unital-Gröbner-bases paper ([admissible system](#unital-groebner-bases:def:admissible-system)).
>>>>>>> origin/main
$\square$
