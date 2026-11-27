---
doc_id: arxiv-1507.06276v2
doc_title: "UNIVERSAL K-MATRIX FOR QUANTUM SYMMETRIC PAIRS"
section_id: sec-030-71-a-pseudo-longest-element-of-w
section_title: "A pseudo longest element of W"
section_number: 7.1
pages: 37-38
source_pdf: 1507.06276v2.pdf
source_sha256: f552aa5de7125b23
toc_source: outline
doc_brief: "UNIVERSAL K-MATRIX FOR QUANTUM SYMMETRIC PAIRS — Let g be a symmetrizable Kac-Moody algebra and let Uq(g) de- note the corresponding quantized enveloping algebra."
---
τ0 ∈ Aut(A) such that the longest element w0 ∈W satisﬁes
w0(αi) = −ατ0(i) for all i ∈I.(7.1)
Moreover, in this case the Lusztig automorphism Tw0 ofUq(g) corresponding to w0
can be explicitly calculated. Indeed, by [Jan96, Proposition 8.20] or [K ol14, Lemma
3.4] one has
(7.2)
Tw0(Ei) = −Fτ0(i)Kτ0(i), T w0(Fi) = −K −1
τ0(i)Eτ0(i), T w0(Ki) = K −1
τ0(i),
T −1
w0 (Ei) = −K −1
τ0(i)Fτ0(i), T −1
w0 (Fi) = −Eτ0(i)Kτ0(i), T −1
w0 (Ki) = K −1
τ0(i).
In the Kac-Moody case we mimic the inverse of the Lusztig automorp hism corre-
sponding to the longest element of the Weyl group as follows. Let tw : Uq(g) →
Uq(g) denote the algebra automorphism deﬁned by
tw(Ei) = −K −1
i Fi, tw(Fi) = −EiKi, tw(Kh) = K−h
for all i ∈I, h ∈Q∨
ext.
Lemma 7.1. For all i ∈I one has tw ◦Ti =Ti ◦ tw on Uq(g).
Proof. Forh ∈ Q∨
ext one has Ti ◦ tw(Kh) = K−si(h) = tw ◦Ti(Kh). It remains to
check that
Ti ◦ tw(Ej) = tw ◦Ti(Ej) and Ti ◦ tw(Fj ) = tw ◦Ti(Fj)(7.3)
for all j ∈I. For j =i relation (7.3) holds because T −1
i |Uqi (sl2)i = tw|Uqi (sl2)i . For
j ⁄=i relation (7.3) is veriﬁed by a direct calculation using the formulas
Ti(Ej) =
−aij∑
k=0
(−1)kq−k
i E(−aij −k)
i EjE(k)
i ,
Ti(Fj) =
−aij∑
k=0
(−1)kqk
iF (k)
i FjF (−aij −k)
i .
which hold by [Lus94, 37.1.3]. □
To mimic the Lusztig action of the longest element in the Kac-Moody ca se we
additionally need an automorphism τ0 ∈ Aut(A,X ). Recall our setting and as-
sumptions from Section 5.4. For the construction of the universal K-matrix we
need to make minor additional assumptions on the parameters c ∈ C and s ∈ S .
Assumption (τ0): We are given an additional involutive element τ0 ∈ Aut(A,X )
with the following properties:
(1) τ ◦τ0 =τ0 ◦τ .
(2) The parameters c ∈ C and s ∈ S satisfy the relations
cτ0τ (i) =ci, s τ0(i) =si for all i ∈I \X.(7.4)
(3) The function s :I → K described by (5.1) and (5.2) satisﬁes the relation
s(τ (i)) = s(τ0(i)) for all i ∈I.(7.5)
38 MARTINA BALAGOVI ´C AND STEF AN KOLB
Remark 7.2. Assume that g is of ﬁnite type. In this case we always choose τ0 to
be the diagram automorphism determined by Equation (7.1). Then Property (1) is
automatically satisﬁed as follows by inspection from the li st of Satake diagrams in
[Ara62]. Moreover, by deﬁnition of the parameter set S one can have si ⁄= 0 only
if τ ′(i) = i for all τ ′ ∈ Aut(A). Hence Property (2) reduces to cτ0τ (i) = ci in the
ﬁnite case. By (5.1) and (5.2) one can have s(i) ⁄= 1 only if τ (i) = τ0(i). Hence
Property (3) is always satisﬁed in the ﬁnite case.
If τ0 = τ then Property (2) is an empty statement. It is possible that τ = id
and τ0 ⁄= id , see the list in [Ara62]. In this case condition (5.17) implies that
ci equals cτ0(i) up to multiplication by a bar invariant scalar. The new condi tion
cτ0τ (i) =ci forces this scalar to be equal to 1. Finally, only in type D2n is it possible
that τ0 = id and τ ⁄= id . In this case, however, the condition c ∈ C implies that
cτ0τ (i) =ci. These arguments show that the new condition cτ0τ (i) =ci is consistent
with the conditions imposed in Section 5.4 and that it is alwa ys possible to choose
parameters c and s which satisfy all of the assumptions.
The composition
tw ◦τ0 :Uq(g′) →Uq(g′)
deﬁnes an algebra automorphism. By (7.2) the automorphism tw ◦τ0 is a Kac-
Moody analog of the inverse of the Lusztig action on Uq(g) corresponding to the
longest element in the Weyl group in the ﬁnite case. As τ0 ∈ Aut(A,X ) one has
τ0 ◦TwX =TwX ◦τ0. By Lemma 7.1 this implies that
τ0 ◦ tw ◦TwX =TwX ◦τ0 ◦ tw.(7.6)
To obtain an analog of this Lusztig action on modules in Oint we will twist the mod-
ule structure. In the following section we construct a Bc,s-module homomorphism
between twisted versions of modules in Oint. As Bc,s is a subalgebra of Uq(g′) it
suﬃces to consider objects in Oint as Uq(g′)-modules. With this convention, for
any algebra automorphism ϕ : Uq(g′) → Uq(g′) and any M ∈ Ob(Oint) let Mϕ
denote the vector space M with the Uq(g′)-module structure u ⊗m ↦→u •ϕm given
by
u •ϕm =ϕ(u)m for all u ∈Uq(g′), m ∈M .
We will apply this notation in particular in the case where ϕ is one of τ0 ◦τ and
tw ◦τ0, see Theorem 7.5.
Remark 7.3. If the algebra automorphism ϕ :Uq(g′) →Uq(g′) extends to a Hopf
algebra automorphism of Uq(g) then the notation Mϕ for M ∈Ob(Oint) coincides
with the notation in Example 4.7.
