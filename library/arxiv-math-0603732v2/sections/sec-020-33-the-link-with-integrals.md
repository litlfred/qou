---
doc_id: arxiv-math-0603732v2
doc_title: "DUALISING COMPLEXES AND TWISTED HOCHSCHILD (CO)HOMOLOGY FOR NOETHERIAN HOPF ALGEBRAS"
section_id: sec-020-33-the-link-with-integrals
section_title: "The link with integrals"
section_number: 3.3
pages: 11-12
source_pdf: 0603732v2.pdf
source_sha256: 3464a2ddc2e54f3a
doc_brief: "DUALISING COMPLEXES AND TWISTED HOCHSCHILD (CO)HOMOLOGY FOR NOETHERIAN HOPF ALGEBRAS — W e show that many noetherian Hopf algebras A have a rigid du- alising complex R with R ∼= ν A1[d]."
---
is due to Feng and Tsygan [FT, Corollary (2.5)] (see also [HK1, Propo sition 2.3]):
Proposition. [FT] Let A be a Hopf algebra and let M be an A-bimodule. Then,
for all i ≥ 0, there are vector space isomorphisms
Hi(A, M) ∼= TorAe
i (A, M) ∼= TorA
i (M ′, k).
Consequently, tHdim A ≤ gldim A.
Proof. By [We, Lemma 9.1.3], Hi(A, M) ∼= TorAe
i (A, M). To see the second iso-
morphism we use the fact that A ⊗Ae M ∼= M ′ ⊗A k and that the functor ( −)′ : Ae-
Mod → Aop-Mod preserves projectives and is exact. Finally, tHdim A ≤ gldim A
follows from the isomorphisms. □
The second observation is a version of Poincar´ e duality for AS-reg ular Hopf
algebras, which, as we shall note in Section 6, is suﬃcient to retrieve some classical
results:
12 K.A. BROWN AND J.J. ZHANG
Lemma. Let A be an augmented AS-regular algebra of global dimension d. Then
for any right A-module N ,
TorA
d−i(N, k) ∼= Exti
Aop(∫ l, N)
for all i.
Proof. The isomorphism follows from Ischebeck’s spectral sequence (3.2.1 ), taking
M = k, together with the Artin-Schelter condition (AS2). □
Noting (3.2.1), and combining the above proposition and lemma, we imme diately
deduce the following partial Poincar´ e duality for the Hochschild hom ology of AS-
regular Hopf algebras.
Corollary . Let A be an AS-regular Hopf algebra of global dimension d. Let M be
an A-bimodule. Then, for every integer i,
Hd−i(A, M) ∼= Exti
Aop(
∫ l, (M )′).
As a consequence, if σ is an algebra automorphism of A, then, for every i,
Hd−i(A, σA) ∼= Exti
Aop(
∫ l
, (σA)′).
Remark. When S is bijective, this corollary can be deduced from Van den Bergh’s
general Poincar´ e duality result Proposition 5.1 – see Corollary 5.2. H owever it is
unknown at present whether S is bijective in general, so it seems worth recording
this corollary.
