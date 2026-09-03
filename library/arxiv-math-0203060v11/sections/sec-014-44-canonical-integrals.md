---
doc_id: arxiv-math-0203060v11
doc_title: "ON FUSION CATEGORIES"
section_id: sec-014-44-canonical-integrals
section_title: "Canonical integrals"
section_number: 4.4
pages: 16-18
source_pdf: 0203060v11.pdf
source_sha256: fa7e21ceab3e9933
doc_brief: "ON FUSION CATEGORIES — Using a variety of methods developed in the literature (in pa rtic- ular, the theory of weak Hopf algebras), we prove a number of g eneral results about fusion categories in"
---
grals on a weak Hopf algebra A called the canonical integrals. Namely, we have the
following proposition, a particular case of which was proved in [BNSz].
Proposition 4.9. Let A be a ﬁnite-dimensional weak Hopf algebra and let {qi}
be primitive central idempotents in At. Then χi(h) := Tr(Lh ◦S2|AS(qi)), where
ON FUSION CATEGORIES 17
Lh ∈ Endk(A) is given by Lh(x) = hx, h,x ∈A, deﬁnes a left integral in A∗ such
that
χi(qj) = Tr(S2|qjAS(qi)) and(18)
χi(gh) = χ(hS2(g)),(19)
for all g,h ∈A.
Proof. The identities (18) and (19) follow immediately from the deﬁnition of χ,
since A is regular and S2 ◦Lg =LS2(g) ◦S2 for all g ∈A.
Next, for all φ ∈A∗ we deﬁne Rφ ∈ Endk(A) by Rφ(x) = x↼φ, x ∈A∗. Then
Rφ(xS(qi)) = Rφ(x)S(qi) so that AS(qi) is Rφ-invariant. A direct computation
shows that L(h↼φ) =Rφ(1) ◦Lh ◦RS−1(φ(2)) for all h ∈A, φ∈A∗, and hence,
(φ ⊗χi)(∆(h)) = Tr( L(h↼φ) ◦S2|AS(qi))
= Tr( Rφ(1) ◦Lh ◦RS−1(φ(2)) ◦S2|AS(qi))
= Tr( Rεt(φ) ◦Lh ◦S2|AS(qi)),
therefore, (id ⊗χi)∆( h) = (εt ⊗χ)∆( h) for all h ∈ A, i.e., χi is a left integral in
A∗. □
4.5. Suﬃcient conditions for semisimplicity . The next proposition is a reﬁne-
ment of [N, Proposition 6.4] and is analogous to the Larson-Radford theorem [LR1]
for usual Hopf algebras which says that if A is a ﬁnite dimensional Hopf algebra
with Tr(S2|A) ⁄= 0 then A is semisimple and cosemisimple.
Proposition 4.10. Let A be a ﬁnite dimensional weak Hopf algebra. If for every
primitive idempotent p inAt ∩Z(A) there exist idempotents qp, q′
p inpAt such that
(20) Tr(S2|qpAS(q′
p)) ⁄= 0,
then A is semisimple.
Proof. Let ℓ and λ be a dual pair of non-degenerate left integrals in A and A∗ re-
spectively. Then (ℓ(2) ⇀λ )⊗qpS−1(ℓ(1))S(q′
p) is the dual bases tensor for qpAS(q′
p),
cf. [N]. Therefore,
0 ⁄= Tr( S2|qpAS(q′p))
= ⟨ℓ(2) ⇀λ, qpS(ℓ(1))S(q′
p) ⟩
= ⟨λ, qpεs(q′
pℓ) ⟩.
Therefore, yp :=εs(q′
pℓ) ⁄= 0. Next, we compute
ypℓ = S(ℓ(1))S(q′
p)ℓ(2)ℓ
= S(ℓ(1))S(q′
p)εt(ℓ(2))ℓ
= S(ℓ(1))εt(ℓ(2))S(q′
p)ℓ =S(ℓ)yp.
Let ξp be an element in A∗
t (here and below we write A∗
t := (A∗)t, A∗
s := (A∗)s)
such that ξp ⇀ 1 = yp. Then from the previous computation we have
(21) ypℓ = (α⇀ℓ )yp,
whereα is a distinguished group-like element of A∗. Arguing as in [N, Proposition
6.4] one gets
(22) ξp =S(ξp)α,
18 PA VEL ETINGOF, DMITRI NIKSHYCH, AND VIKTOR OSTRIK
whence α is trivial, i.e., α ∈ A∗
min. This means that one can choose ℓ in such a
way that α = ǫ, i.e., ℓ = S(ℓ). Hence, yp ∈ As ∩Z(A) is a non-zero multiple of
p. We conclude that y := εs(ℓ) = ∑
p yp is an invertible central element of A.
Hence, ℓ′ =y−1ℓ is a normalized right integral in A. By Maschke’s theorem, A is
semisimple. □
Let q qnd q′ be idempotents in At, and let ρ =ǫ ↼q and ρ′ =ǫ ↼q′. Then ρ
and ρ′ are idempotents in A∗
t .
Lemma 4.11. The space ρA∗S(ρ′) may be identiﬁed, in an S2-invariant way, with
the dual space of qAS(q′).
Proof. It is easy to check that for all h ∈ A and φ ∈ A∗ one has ⟨φ, qhS(q′) ⟩ =
⟨ρφS(ρ′), h⟩, whence the statement follows. □
The next three corollaries reﬁne [N, Corollaries 6.5 - 6.7].
Corollary 4.12. Let A be a ﬁnite dimensional weak Hopf algebra. If for every
primitive idempotent π in A∗
t ∩A∗
s there exist idempotents ρπ, ρ′
π in πA∗
t such that
(23) Tr(S2|ρπA∗S(ρ′π )) ⁄= 0,
then A is semisimple.
Proof. This immediately follows from Proposition 4.10 and Lemma 4.11, since the
latter implies Tr(S2|ρπA∗S(ρ′π )) = Tr(S2|qpAS(q′p)). □
Corollary 4.13. Let A be a connected ﬁnite dimensional weak Hopf algebra. If
there exist idempotents q, q′ in At such that Tr (S2|qAS(q′)) ⁄= 0 then A is semi-
simple.
Corollary 4.14. Let A be a biconnected ﬁnite dimensional weak Hopf algebra. If
there exist idempotents q, q′ in At such that Tr (S2|qAS(q′)) ⁄= 0 then A and A∗ are
semisimple.
