---
doc_id: arxiv-1610.09640v4
doc_title: "Derived Categories | Amnon Yekutieli | 14 Apr 2019 DERIVED CATEGORIES AMNON YEKUTIELI"
section_id: sec-022-26-projective-objects
section_title: "Projective Objects"
section_number: 2.6
pages: 46-47
source_pdf: 1610.09640v4.pdf
source_sha256: db5e7a5c5e85f95f
doc_brief: "Derived Categories | Amnon Yekutieli | 14 Apr 2019 DERIVED CATEGORIES AMNON YEKUTIELI — This is the fourth (and last) prepublication version of a book on derived categories, that will be published by"
---
A splitting of an epimorphismψ: M→M′′in M is a morphismα: M′′→M
s.t. ψ◦α= idM′′. A splitting of a monomorphismφ: M′→M is a morphism
β:M→M′s.t. β◦φ= idM′. A splitting of a short exact sequence
(2.6.1) 0→M′φ
− →M
ψ
− →M′′→0
is a splitting of the epimorphismψ, or equivalently a splitting of the monomorphism
φ. The short exact sequence is said to besplit if it has some splitting.
Exercise 2.6.2.Show how to get from a splitting ofφto a splitting ofψ, and vice
versa. Show how any of those gives rise to an isomorphismM∼=M′⊕M′′.
Deﬁnition 2.6.3.An objectP∈M is called aprojective objectif for every mor-
phism γ: P →N and every epimorphism ψ: M↠ N, there exists a morphism
˜γ:P→N such thatψ◦˜γ=γ.
46
Derived Categories | Amnon Yekutieli | 14 Apr 2019
This is described in the following commutative diagram inM :
P
γ

˜γ
{{
M ψ
// //N
Proposition 2.6.4. The following conditions are equivalent forP∈M :
(i) P is projective.
(ii) The additive functorHomM(P,−) : M→Ab is exact.
(iii) Every short exact sequence(2.6.1) with M′′=P is split.
Proof. Exercise. □
Deﬁnition 2.6.5.We say M has enough projectivesif everyM ∈M admits an
epimorphism P→M from a projective objectP.
Exercise 2.6.6. Let A be a ring.
(1) Prove that anA-module P is projective iﬀ it is a direct summand of a free
module; i.e.P⊕P′∼=Q for some moduleP′and free moduleQ.
(2) Prove that the categoryModA has enough projectives.
Exercise 2.6.7. Let M be the category of ﬁnite abelian groups. Prove that the
only projective object in M is 0. So M does not have enough projectives. (Hint:
use Proposition 2.6.4.)
Example 2.6.8. Consider the schemeX := P1
K, the projective line over a ﬁeldK,
with structure sheafOX. The categoryCohOX of coherentOX-modules is abelian
(it is a full abelian subcategory ofModOX, cf. Example 2.3.19). One can show
that the only projective object ofCohOX is 0, but this is quite involved.
Let us only indicate why the sheafOX is not a projective object of CohOX.
Denote byt0,t 1 the homogeneous coordinates ofX. These belong toΓ(X,OX(1)),
so each determines a homomorphism of sheavestj :OX(i)→OX(i + 1). We get a
sequence
(2.6.9) 0→OX(−2)
[t0 t1 ]
−−−−→OX(−1)⊕2
−t1
t0

−−−−→OX→0
in CohOX, which is known to be exact. It is also known thatΓ(X,OX) =K and
Γ(X,OX(−1)) = 0. Therefore the sequence (2.6.9) is not split.
