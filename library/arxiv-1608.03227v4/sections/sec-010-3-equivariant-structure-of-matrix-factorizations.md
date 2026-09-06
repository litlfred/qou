---
doc_id: arxiv-1608.03227v4
doc_title: "January 30, 2018"
section_id: sec-010-3-equivariant-structure-of-matrix-factorizations
section_title: "Equivariant structure of matrix factorizations and their push-forwards"
section_number: 3
pages: 12-14
source_pdf: 1608.03227v4.pdf
source_sha256: c71128e9a6c35343
doc_brief: "January 30, 2018 — For each braid β ∈ Brn we construct a 2-periodic complex Sβ of quasi-coherent C∗ × C∗ - equivariant sheaves on the non-commutative nested Hilbert scheme Hilb f ree 1,n ."
---
In this section we discuss the properties of equivariant matrix fact orizations and construct the push
forward of matrix factorizations along the embedding of aﬃne varie ties j :Spec(R)→Spec(S). There is a
more general, more sophisticated construction for push forward of matrix factorization that could be found
in [10] but the functor from [10] is of diﬀerent nature then ours. Ou r construction of the push-forward relies
on the generalizations of the lemmas from the previous section and w e discuss these extensions ﬁrst.
3.1. T echnical lemmas: non-equivariant version. We keep notations consistent with the previous sec-
tion. Let Mod per(Z) be a category of Z2-graded free C[Z] modules with endomorphisms. An object F∈
Modper(Z) is a pair ( M,D ),M =M 0⊕M 1,M i = C[Z]di andD∈ HomC[Z](M 1,M 0)⊕ HomC[Z](M 0,M 1).
The space of morphisms between two elements of Mod per(Z) consists of morphisms of the corresponding
C[Z]-modules that intertwine the endomorphisms.
We denote by Com per(Z) be the category of complexes of Z2-graded modules with endomorphisms. We
denote by Mod per(Z) the abelian category with objects ( M,D ) where M =M 0⊕M 1 is a Z2-graded C[Z]-
module and D∈ HomC[Z](M i,M i+1). The morphisms in Mod per(Z) preserve Z2-grading and intertwine the
endomorphisms. We would like to emphasize that the elements of Mod per(Z) are not matrix factorizations
in general since we do not impose constraint D2 =W and do not require the modules Mi to be free.
An object of Com per(Z) is a collection of objects Fi∈ Modper(Z),Fi = (Mi,D i), Mi = C[Z]ri and
morphisms d+
i : Mi→ Mi−1 which are morphisms of elements of Mod per(Z) and ( d+)2 = 0 as a linear
map Mi→Mi−2. Since d+
i intertwines the endomorphisms Di−1 and Di the kernel ker d+
i ⊂Mi and image
imd+
i ⊂Mi−1 are elements of Mod per(Z) and we use notation H i(F ) for the quotient ker d+
i / imd+
i+1. For
subset of Com per(Z) consisting of complexes F such that Mi = 0 for i /∈ [0,ℓ ] we use notation Com ℓ
per(Z).
Analogously to the previous case we introduce notation Hom k(F•,F•) =⊕i Hom(Fi,Fi−k) respectively
we use notation Hom k
d+ (F•,F•) for the elements of Hom k(F•,F•) that commute with the diﬀerential d+.
The homotopy relations between the elements of Hom k
d+(F•,F•) is deﬁned in the natural way:
f∼g, iﬀ there is h∈ Homk−1(F•,F•), f −g =d+◦h−h◦d+.
The technical lemma that we need later is a generalization of lemmas 2.1 and 2.2, the proof is essentially
identical to the proof of the above mentioned lemmas.
Lemma 3.1. Let (F•,d +
• ),Fi = (Mi,D i) be an element of Comℓ
per(Z) and F∈ C[Z] such that Mi are free
C[Z]-modules and
(1) Elements of Hom<0
d+ (F•,F•) are homotopic to 0
(2) Element F−D2∈ Hom0
d+ (F•,F•) is homotopic to 0
12
Then there are maps d−
ij∈ Hom(Fi,Fj), j >i such that
[(F•,D +d+ +d−)]per∈ MF(Z,F ).
Proof. By assumption of the lemma there exist morphisms of C[Z] modules h(−1)
i ∈ Hom(Fi,Fi+1) such
thatF−D2 =h(−1)
i ◦d+
i+1 +d+
i◦h(−1)
i−1 . Then a new diﬀerential D(−1) :=D +d+ +h(−1) satisﬁes the relation
Ä
D(−1)ä2
−F = (h(−1))2∈ Hom≤−2(C•,C •).
ThusD(−1) provides a base of induction for the proof of existence h(−2i−1)∈ Hom−2i−1(F•,F•),i≥ 0 such
that
(1) [h(−1),d +]+ =F−D2
(2) [h(−2i−1),d +]+ = ∑ i−1
j=0h(−2j−1)h(−2i+2j+1), i> 0
were we used the notation [ a,b ]+ =ab +ba.
Indeed, suppose we constructed h(−2i−1) for all i<j . Deﬁne D(−2j+1) =D +d+ + ∑ j−1
k=0h(−1−2k), then
the inductive assumption implies:
(3.4)
Ä
D(−2j+1)
ä2
−F +D2−R(−2j)∈ Hom<−2j(F•,F•),
R(−2j) =
j−1∑
k=0
h(−2k−1)h(−2j+1+2k)
On the other hand, a direct computation using the inductive assump tions and the fact that F commutes
with all h(2i−1) and d+ implies
(3.5) [d+,R (−2j)] = 0.
In more details, let us introduce notation R(<−2j) := (D(−2j−1))2−F−R(−2j) then
0 = [D(−2j−1), (D(2j−1))2] = [D +d+ +
∑
i
h(−2i−1),F −D2 +R(−2j) +R(<−2j)]
= [d+,R (−2j)] + [d+ +
∑
i
h(−2i−1),R (<−2j)] + [
∑
i
h(−2j−1),R (−2j) +R(−2j−1)].
The ﬁrst term in the last sum is from Hom −2j+1(F•,F•), on the other hand the last two are from Hom <−2j+1(F•,F•)
thus (3.5) follows.
ThusR(−2j) is the morphism of the complex (F•,d +) of degree−2j, that is, an element of Hom −2j(F•,F•).
The assumption of our lemma implies that such morphism is homotopic to zero and the homotopy morphism
h(−2j−1)∈ Hom−2j−1(F•,F•) provides the induction step since [ h(−2j−1),d +]+ =R(−2j).
Thus by setting d−
i = ∑
ih(−2i−1) we obtain the desired extension because of (3.4). ✷
Lemma 3.2. Let (F•,d +
• ) be an element of Comℓ(Z) and F∈ C[Z] that satisfy conditions of the previous
lemma. Suppose there two sets of diﬀerentials d−
ij, ˆd−
ij :Fi→F j, j >i such that
[(F•,D +d+ +d−)]per∈ MF(Z,F ), [(F•,D +d+ + ˆd−)]per∈ MF(Z,F )
then there is Ψ = ∑
i≤0 Ψ i, Ψ i∈ Hom−i(F•,F•), Ψ = Id such
Ψ◦ (D +d+ +d−)◦ Ψ −1 =D +d+ + ˆd−.
Proof of the this lemma is identical to the proof of lemma 2.2 and we omit it.
13
