---
doc_id: arxiv-2011.12932v2
doc_title: "MODULAR CATEGORIES AND TQFTS BEYOND SEMISIMPLICITY"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-2
source_pdf: 2011.12932v2.pdf
source_sha256: 23709542c5652a29
doc_brief: "MODULAR CATEGORIES AND TQFTS BEYOND SEMISIMPLICITY — Vladimir Turaev discovered in the early years of quantum topol- ogythatthenotionofmodularcategorywasanappropriatestructureforbuild- ing"
---
After the work of Vaughan Jones [30] and Edward Witten [61, 62], Vladimir Tu-
raev played a key role in the foundation of quantum topology. Together with Nikolai
Reshetikhin [54], they were the ﬁrst to obtain a mathematically rigorous construc-
tion of Witten’s invariants of 3-dimensional manifolds. Turaev showed that the rel-
evant algebraic structure underlying their approach was that of amodular category,
a notion he himself identiﬁed and introduced for this purpose [58]. Starting from
a modular category, one can build a Topological Quantum Field Theory (TQFT
for short) and, in particular, invariants of links in 3-manifolds, and representations
of mapping class groups of surfaces. The famous Witten–Reshetikhin–Turaev in-
variants can be derived from a family of modular categories arising as semisimple
quotients of representation categories of the restricted quantum group of sl2 at
roots of unity. Around the same time, equivalent modular categories were obtained
from the Kauﬀman bracket skein theory [8]. On the one hand, the quantum group
construction generalizes to other families of modular categories, corresponding to
arbitrary simple Lie algebrasg. On the other hand, the skein construction produces
families of modular categories associated with the structure of Hecke algebras of
type A [10] and of Birman–Murakami–Wenzl algebras of type B,C, and D [4]. The
abundance of examples shows the relevance of Turaev’s deﬁnition. However, in all
these instances, only simple representations, which cover just a small part of the
corresponding representation theory, are used.
Already within the ﬁrst decade since the birth of quantum topology, construc-
tions of invariants and mapping class group representations beyond the scope of
semisimple modular categories emerged, thanks to the work of Mark Hennings [29]
and Volodymyr Lyubashenko [41]. More recently, the algebraic theory ofmodiﬁed
traces, whose germs can be found in an early collaboration of Nathan Geer and
Bertrand Patureau with Turaev [26], served as a huge propeller for a new wave
of non-semisimple quantum constructions. Through this technology, TQFTs and
HQFTs1 were built for the ﬁrst time out of non necessarily semisimple generaliza-
tions of modular categories. Our purpose here is to review the original construction,
and to relate it to the latest achievements in the ﬁeld.
1Acronym for Homotopy Quantum Field Theory, a notion introduced by Turaev.
1
arXiv:2011.12932v2  [math.GT]  22 May 2021
2 C. BLANCHET AND M. DE RENZI
2. Historical over view
Deﬁnition of TQFT.A popular axiomatization of the notion of TQFT was pro-
posed by Micheal Atiyah [3], who was inspired by a similar deﬁnition of Graeme
Segal [55] for the concept of a Conformal Field Theory (CFT for short). Paraphras-
ing Atiyah, a TQFT in dimension 3 can be deﬁned as a symmetric monoidal functor
from a category of 3-dimensional cobordisms to the category of vector spaces. In
this deﬁnition, cobordism categories are naturally equipped with the symmetric
monoidal structure induced by disjoint union. In other words, a TQFTV asso-
ciates with every closed oriented surfaceΣ a vector spaceV (Σ) called the state
space of Σ, and it associates with every cobordismM from Σ to Σ′ a linear map
V (M) : V (Σ)→ V (Σ′). At the same time, a TQFT translates the topological
operations of gluing and disjoint union into the algebraic operations of composition
and tensor product, respectively. The use of an indeﬁnite article in this deﬁnition,
when we talk abouta category of cobordisms, as opposed tothe category of cobor-
disms, is due to the fact that cobordisms are typically allowed to carry additional
structure, which may vary according to the diﬀerent constructions we might want to
consider. All the resulting notions are gathered under the umbrella term “TQFT”.
