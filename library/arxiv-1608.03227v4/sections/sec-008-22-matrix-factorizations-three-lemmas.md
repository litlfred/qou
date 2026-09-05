---
doc_id: arxiv-1608.03227v4
doc_title: "January 30, 2018"
section_id: sec-008-22-matrix-factorizations-three-lemmas
section_title: "Matrix factorizations: three lemmas"
section_number: 2.2
pages: 8-11
source_pdf: 1608.03227v4.pdf
source_sha256: c71128e9a6c35343
doc_brief: "January 30, 2018 — For each braid β ∈ Brn we construct a 2-periodic complex Sβ of quasi-coherent C∗ × C∗ - equivariant sheaves on the non-commutative nested Hilbert scheme Hilb f ree 1,n ."
---
and remind some basic facts about them. In particular we prove thr ee lemmas that we will use in the main
body of the paper. These lemmas essentially contain all facts about matrix factorizations that are used
here. For more thorough review of the theory of matrix factoriza tion the reader could consult the beautiful
original paper [11] or later surveys in [8].
Given an aﬃne variety Z and a function F on it we deﬁne [11] the homotopy category MF( Z,F ) of
matrix factorizations whose objects are complexes of C[Z]-modules M =Modd⊕Meven equipped with the
diﬀerential
D∈ HomC[Z](Modd,M even)⊕ HomC[Z](Meven,M odd)
such that D2 =F . Thus MF(Z,F ) is a triangulated category as explained in subsection 3.1 of [37].
IfZ is a variety with G-action and F is a G-invariant function then we deﬁne the category of strongly
equivariant matrix factorizations MF str
G (Z,F ) as the category of matrix factorizations with extra condition
thatD is a G-equivariant matrix. Unfortunately, this deﬁnition is too restrictiv e and we use a slightly more
sophisticated deﬁnition for the category of equivariant matrix fac torization. We postpone the details of our
8
deﬁnition till the next section where we deﬁne matrix factorizations that are equivariant up to homotopy.
However, the naive equivariant matrix factorization as above are o bjects in our category.
Let us discuss some speciﬁc types of matrix factorizations that will be used in our paper. Suppose
C• = [C0→ C1→···→ Cn] is the complex of C[Z]-modules. Then we construct a matrix factorization
[C•]per∈ MF(Z, 0) by setting M =Codd⊕Ceven, Ceven :=⊕i∈2ZCi,C odd =⊕i∈1+2ZCi and the diﬀerential
is induced from the complex C•.
Another type of matrix factorization appearing in our work is obtain ed by ”doubling” the diﬀerential d+
of an ordinary complex ( C•,d +). Indeed, let us denote by MF ℓ(Z,F ) the set of the following complexes:
C• =⊕ℓ
i=0Ci, d +
i :Ci→Ci−1, d −
i :Ci→C>i, (
∑
i
d−
i +d+
i )2 =F· Id.
The complex C• with only the positive diﬀerentials d+
i is called the positive part of the complex. There is
a folding map MF ℓ(Z,F )→ MF(Z,F ) that associates to ( C•,d ±
• ) a two-periodic complex [ C•,d ±
• ]per. The
matrix factorizations of the above type occur very naturally in a ge ometric setting as explained in the lemma
below. The notations for the morphisms are as follows: Hom k(C•,C •) =⊕m Hom(Cm,C m−k) is notations
for the maps of C[Z]-modules and Hom k
d+(C•,C •) is the subspace of maps from Hom k(C•,C •) that commute
with the diﬀerential d+.
Lemma 2.1. Let (C•,d +
• ) be the complex
C0
d+
1
←−−C1
d+
2
←−−...
d+
ℓ
←−−Cℓ
of C[Z] modules and F∈ C[Z] such that
(1) Elements of Hom<0
d+ (C•,C •) are homotopic to 0
(2) The element F∈ Hom0
d+ (C•,C •) is homotopic to 0.
Then the complex (C•,d +
• ) can be extended to (C•,d ±
• )∈ MFℓ(Z,F ).
Proof. By assumption of the lemma, the endomorphism F· Id of ( C•,d +
• ) is homotopic to 0. This means
that there exist morphisms of C[Z] modules h(−1)
i :Ci→Ci+1 such that F =h(−1)
i ◦d+
i+1 +d+
i ◦h(−1)
i−1 . Then
a new diﬀerential D(−1) :=d+ +h(−1) satisﬁes the relation
Ä
D(−1)ä2
−F = (h(−1))2∈ Hom≤−2(C•,C •).
ThusD(−1) provides a base of induction for the proof of existence h(−2i−1)∈ Hom−2i−1(C•,C •),i≥ 0 such
that
(1) [h(−1),d +]+ =F
(2) [h(−2i−1),d +]+ = ∑ i−1
j=0h(−2j−1)h(−2i+2j+1), i> 0
were we used the notation [ a,b ]+ =ab +ba.
Indeed, suppose we constructed h(−2i−1) for all i<j . Deﬁne D(−2j+1) =d+ + ∑ j−1
k=0h(−1−2k), then the
inductive assumption implies:
(2.1)
Ä
D(−2j+1)ä2
−F−R(−2j)∈ Hom<−2j(C•,C •), R (−2j) =
j−1∑
k=0
h(−2k−1)h(−2j+1+2k)
9
On the other hand, a direct computation using the inductive assump tions and the fact that F commutes
with all h(2i−1) and d+ implies
(2.2) [d+,R (−2j)] = 0.
In more details, let us introduce notation R(<−2j) := (D(−2j−1))2−F−R(−2j) then
0 = [D(−2j−1), (D(2j−1))2] = [d+ +
∑
i
h(−2i−1),F +R(−2j) +R(<−2j)]
= [d+,R (−2j)] + [d+ +
∑
i
h(−2i−1),R (<−2j)] + [
∑
i
h(−2j−1),R (−2j) +R(−2j−1)].
The ﬁrst term in the last sum is from Hom −2j+1(C•,C •), on the other hand the last two are from Hom <−2j+1(C•,C •)
thus (2.2) follows.
ThusR(−2j) is the morphism of the complex (C•,d +) of degree−2j, that is, an element of Hom −2j
d+ (C•,C •).
The assumption of our lemma implies that such morphism is homotopic to zero and the homotopy morphism
h(−2j−1)∈ Hom−2j−1(C•,C •) provides the induction step since [ h(−2j−1),d +]+ =R(−2j).
Thus by setting d−
i = ∑
ih(−2i−1) we obtain the desired extension because of (2.1). ✷
The extension described in Lemma 2.1 is unique up to a natural equivale nce relation. First, let us ﬁx
notations: the space of morphisms Hom d±(A,B ),A,B ∈ MFℓ(Z,F ) consists of C[Z]-module homomorphism
that (super-)commute with the diﬀerentials d±
• . This space is Z-graded with Hom i
d±(A,B ) consisting of
morphisms hk :Ak→Ak+i.
Lemma 2.2. LetA = (C•,d ±
• ),B = (C•, ˜d±
• )∈ MFℓ(Z,F ) such that
(1) ( ˜C, ˜d+
• ) = (C•,d +
• )
(2) Elements of Hom<0
d+ (C•,C •) are homotopic to 0
(3) The element F∈ Hom0
d+ (C•,C •) is homotopic to 0.
Then there is Ψ = ∑
i≤0 Ψ i, Ψ i∈ Homi(A,B ) such that Ψ 0 = Id and
Ψ◦ (d+ +d−)◦ Ψ −1 = ( ˜d+ + ˜d−).
Proof. For brevity let us denote by C+ the complex (C•,d +
• ), respectively we use notation Hom d+(C+,C +)
for the morphisms that respect the diﬀerential d+ and Hom(C,C ) for the morphisms of complexes simply
as modules. In particular in these notations we have
D =d+ +d−, ˜D =d+ + ˜d−∈ Hom1(C,C )⊕ Hom≤−1(C,C ).
We claim that there is sequence of morphisms Ψ (k)∈ Hom≤0(C,C ), k = 0, 1, 2,... such that
(1) Ψ (k)
0 = Id,
(2) D(k)− ˜D∈ Hom−k−1(C,C ),
where D(k) = Ψ (k)◦D◦ (Ψ (k))−1.
Indeed, for k = 0 we can set Ψ (0) = Id. For the step of induction we assume the existence of Ψ (k−1), then
the leading term ∆ = ( D(k−1)− ˜D)−k∈ Hom−k(C,C ) is actually an element of Hom −k
d+ (C+,C +) as could
be seen from degree −k + 1 part of the equation
(D(k−1))2−D2 = 0.
10
On the other hand the second assumption of the Lemma implies that a ll elements of Hom −k
d+ (C+,C +)
are homotopic to 0 and hence there is h∈ Hom −k−1(C,C ) such that [ h,d +] = ∆. Hence the element
Ψ (k) := (1 + h)◦ Ψ (k−1) satisﬁes the condition of our induction statement.
Finally, since the complex C is bounded see that the morphism Ψ (ℓ) has the desired properties and our
proof is complete. ✷
The last lemma is very elementary but it is responsible for appearance of the Hilbert scheme of points on
the plane in our construction of the knot homology.
Lemma 2.3. LetZ be smooth and aﬃne. The elements of the ideal Icrit generated by the partial derivatives
of the potential F act by zero homotopies on the elements of MF(Z,F )
Proof. Let z be a local coordinate on Z and D is the diﬀerential from some matrix factorization with the
potential F . Then we have
∂F
∂z = ∂D
∂z ◦D +D◦ ∂D
∂z .
Hence ∂D
∂z is the map that provides a homotopy of ∂F
∂z to 0. ✷
