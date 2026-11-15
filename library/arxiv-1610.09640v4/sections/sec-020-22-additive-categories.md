---
doc_id: arxiv-1610.09640v4
doc_title: "Derived Categories"
section_id: sec-020-22-additive-categories
section_title: "Additive Categories"
section_number: 2.2
pages: 33-34
source_pdf: 1610.09640v4.pdf
source_sha256: db5e7a5c5e85f95f
toc_source: outline
doc_brief: "Derived Categories — This is the fourth (and last) prepublication version of a book on derived categories, that will be published by Cambridge University Press."
---
Deﬁnition 2.2.1. An additive category is a linear category M satisfying these two
conditions:
(i) M has a zero object 0.
(ii) M has ﬁnite coproducts.
This material will be published by Cambridge University Press as Derived Categories by Amnon
Yekutieli. This prepublication version is free to view and download for personal use only. Not for
redistribution, resale or use in derivative works. c⃝Amnon Yekutieli, 2019.
33
Derived Categories
|
Amnon Yekutieli
|
14 Apr 2019
Observe that HomM(M, N)̸ = ∅for every M, N ∈M, since this is an abelian
group. For the zero object 0 ∈M we have HomM(M, 0) = HomM(0, M) = 0, the
zero abelian group. We denote the unique arrows 0 →M and M →0 also by 0.
So the numeral 0 has a lot of meanings; but they are always (hopefully) clear from
the context. The coproduct in a linear category M is usually denoted by L, and is
called the direct sum; cf. Example 1.4.2.
Example 2.2.2. Let A be a central K-ring. The category Mod A is a K-linear
additive category. The full subcategory F ⊆Mod A on the free modules is also
additive.
Proposition 2.2.3. Let M be a linear category. Let {Mi}i∈I be a ﬁnite collection
of objects of M, and assume the coproduct M = L
i∈I Mi exists, with embeddings
ei : Mi →M.
(1) For each i let pi : M →Mi be the unique morphism such that pi◦ei = idMi,
and pi ◦ej = 0 for j̸ = i. Then (M, {pi}i∈I) is a product of the collection
{Mi}i∈I.
(2) P
i∈I ei ◦pi = idM.
Exercise 2.2.4. Prove this proposition.
Part (1) of Proposition 2.2.3 directly implies:
Corollary 2.2.5. An additive category has ﬁnite products.
Deﬁnition 2.2.6. Let M be an additive category, and let N be a full subcategory
of M. We say that N is a full additive subcategory of M if N contains the zero object,
and is closed under ﬁnite direct sums.
Exercise 2.2.7. In the situation of Deﬁnition 2.2.6, show that the category N is
itself additive.
Example 2.2.8. Consider the linear category M from Example 2.1.4, built from a
ring A. It does not have a zero object (unless the ring A is the zero ring), so it is
not additive.
A more puzzling question is this: Does M have ﬁnite direct sums? This turns
out to be equivalent to whether or not A ∼= A ⊕A as right A-modules. One can
show that when A is nonzero and commutative, or nonzero and noetherian, then
A̸ ∼= A ⊕A in Mod Aop. On the other hand, if we take a ﬁeld K, and a countable
rank K-module N, then A := EndK(N) will satisfy A ∼= A ⊕A.
Proposition 2.2.9. Let M be a linear category, and N ∈M. The following condi-
tions are equivalent:
(i) The ring EndM(N) is trivial.
(ii) N is a zero object of M.
Proof.
(ii) ⇒(i): Since the set EndM(N) is a singleton, it must be the trivial ring.
(i) ⇒(ii): If the ring EndM(N) is trivial, then all left and right modules over it
must be trivial. Now use Proposition 2.1.2(2).
□
