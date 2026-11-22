---
doc_id: arxiv-1507.06276v2
doc_title: "UNIVERSAL K-MATRIX FOR QUANTUM SYMMETRIC PAIRS"
section_id: sec-017-44-cylinder-braided-coideal-subalgebras-via-char
section_title: "Cylinder braided coideal subalgebras via characters"
section_number: 4.4
pages: 21-23
source_pdf: 1507.06276v2.pdf
source_sha256: f552aa5de7125b23
toc_source: outline
doc_brief: "UNIVERSAL K-MATRIX FOR QUANTUM SYMMETRIC PAIRS — Let g be a symmetrizable Kac-Moody algebra and let Uq(g) de- note the corresponding quantized enveloping algebra."
---
[DKM03] J. Donin, P. Kulish, and A. Mudrov introduced the notion of a universal
solution of the reﬂection equation which they also called a universal K -matrix. In
contrast to Deﬁnition 4.10, this notion does not refer to a coideal s ubalgebra of a
Hopf algebra. Nevertheless, there is a close relationship between D eﬁnition 4.10
and the notion of a universal K-matrix in [DKM03], and it is the purpose of the
present section to explain this. This material will not be used in later p arts of the
present paper.
As in Section 4.3 let ( H,RH ) be a braided Hopf algebra over a ﬁeld k. We
retain the conventions from Deﬁnition 4.8 and hence the symbol R in [DKM03]
corresponds to RH
21 in our conventions. Let H ∗ = Homk(H,k ) denote the linear
dual space of H. Recall from [RSTS88] that the braided Hopf H algebra is called
factorizable if the linear map
H ∗ →H, f ↦→(f ⊗ id)(RH
12RH
21)
is an isomorphism of vector spaces. This is only possible if H is ﬁnite dimensional.
If H is factorizable then Donin, Kulish, and Mudrov call the element
Kdkm =RH
12RH
21 ∈H ⊗H
22 MARTINA BALAGOVI ´C AND STEF AN KOLB
the universal K-matrix of H. It follows from (4.10) that
(id ⊗∆)(Kdkm) = RH
01RH
02RH
20RH
10RH
12(RH
12)−1
=RH
01RH
10RH
12RH
02RH
20RH
21(RH
12RH
21)−1
= Kdkm
01 RH
12 Kdkm
02 RH
21(RH
12RH
21)−1(4.17)
where we label the tensor legs of H ⊗3 by 0, 1, 2. The above formula is closely
related to formula (4.13) for ∆(K). There are two diﬀerences, however, namely the
occurrence of the additional factor ( RH
12RH
21)−1 and the fact that (4.17) holds in
H ⊗3 while formula (4.13) holds in H ⊗2. Moreover, the element Kdkm makes no
reference to a coideal subalgebra of Uq(g).
To address the ﬁrst diﬀerence, recall from [Kas95, Deﬁnition XIV.6 .1] that the
braided Hopf algebra ( H,RH ) is called a ribbon algebra if there exists a central
elementθH ∈H such that
∆(θH ) = (RH
12RH
21)−1(θH ⊗θH), ε (θH ) = 1, S (θH ) = θH.
If such a ribbon element θH exists then the element
Kdkm,θ = (1 ⊗θ−1
H )Kdkm ∈H ⊗H
satisﬁes the relation
(id ⊗∆)(Kdkm,θ) = Kdkm,θ
01 RH
12 Kdkm,θ
02 RH
21(4.18)
inH ⊗3.
To eliminate the additional tensor factor in (4.17) and (4.18) let
f :H →k
be a character, that is a one-dimensional representation. Deﬁne
Bf = {(f ⊗ id)∆(h) |h ∈H}(4.19)
and observe that Bf is a right coideal subalgebra of H. The element
Kdkm,θ,f = (f ⊗θ−1
H )Kdkm ∈H(4.20)
commutes with all elements of Bf because ∆(h) commutes with Kdkm = RH
12RH
21
for all h ∈H by (4.9). By (4.18) one has
∆(Kdkm,θ,f ) = ( Kdkm,θ,f ⊗ 1)RH (1 ⊗ Kdkm,θ,f )RH
21
which coincides with relation (4.13) in Deﬁnition 4.10. We summarize the a bove
discussion.
Proposition 4.14. Let (H,RH,θH ) be a factorizable ribbon Hopf algebra over a
ﬁeld k and let f : H → k be a character. Then the right coideal subalgebra Bf
deﬁned by (4.19) is cylinder braided with universal K-matrix
Kdkm,θ,f = (f ⊗θ−1
H )(RH
12RH
21) ∈H.
By the above proposition the element Kdkm,θ,f satisﬁes the reﬂection equation
in every tensor product M ⊗N of representations of H. As the ribbon element θH
is central, the element ( f ⊗ 1)(RH
12RH
21) also satisﬁes the reﬂection equation.
