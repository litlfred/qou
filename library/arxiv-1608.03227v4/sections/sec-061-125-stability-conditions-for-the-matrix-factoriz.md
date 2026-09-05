---
doc_id: arxiv-1608.03227v4
doc_title: "January 30, 2018"
section_id: sec-061-125-stability-conditions-for-the-matrix-factoriz
section_title: "Stability conditions for the matrix factorizations."
section_number: 12.5
pages: 69-71
source_pdf: 1608.03227v4.pdf
source_sha256: c71128e9a6c35343
doc_brief: "January 30, 2018 — For each braid β ∈ Brn we construct a 2-periodic complex Sβ of quasi-coherent C∗ × C∗ - equivariant sheaves on the non-commutative nested Hilbert scheme Hilb f ree 1,n ."
---
V 0⊂V = Cn
the subset of vectors with a non-zero last coordinate. Let us deﬁ ne Xℓ,f r as the subvariety of Xℓ×V
consisting of collections ( X,g 1,Y 1,,...,g ℓ,Y ℓ,u ) such that
C⟨Ad−1
gi (X),Y i⟩g−1
i (u) = V, g −1(u)∈V 0, i = 1,...,ℓ − 1,
The map that forgets framing fgt : Xℓ,f r→ Xℓ is deﬁned as restriction of the projection Xℓ×V → Xℓ
on the open subset Xℓ,f r⊂ Xℓ×V . It is dominant over the open that we call the stable locus Xℓ,st. There
a unique G×Bℓ-equivariant structure on Xℓ,f r,i that makes map fgt G×Bℓ-equivariant.
The framed space comes equipped with the natural convolution alge bra structure:
F ⋆G :=π13∗(CEn(2) (π∗
12(F )⊗π∗
23(G))T (2)
),
where πij : X3,f r→ X2,f r are the natural projection maps. There is a natural pull back map
fgt : MF sc
B2 (X2,W )→ MFsc
B2 (X2,f r,W )
and the key to what follows in the next sections is the Lemma below:
Lemma 12.2. The pull-back map fgt∗ is the homomorpism of the convolution algebras.
Proof. Let us denote by C the matrix factorization
π∗
12(F )⊗π∗
23(G)∈ MFsc
B2 (X3,f r,π ∗
13(W )).
Then what we need to show is that for any Zarisky open set U⊂ X2,f r the matrix factorizations of C[U ]-
modules fgt ∗(CEn(2) (C)T (2)
) and CE n(2) (fgt∗(C))T (2)
) are homotopic.
69
It is more convenient to restate the above homotopic relation in a slig htly more geometric terms. Let us
denote by X3,f r,1 the subvariety of X3×V that is deﬁned by the stability condition:
C⟨Ad−1
g1 (X),Y 1⟩g−1
1 (u) = V, g −1
1 (u)∈V 0
Both spaces X3,f r,1 and X3,f r project onto X2,f r and to distinguish these projections we denote the projec-
tion from the ﬁrst space by π13 and from the second by πf r
13 . Thus the statement of the lemma is equivalent
to the homotopy equivalence of the C[U ] matrix factorizations
(12.54) CE n(2) (C|π−1
13 (U))T (2)
∼ CEn(2) (C|πf r,−1
13 (U))T (2)
.
From the previous discussion of the equations for the support of Cσǫ1
i1 ,...,σ
ǫl
il
we see that
X crit
3 ×V∩ X3,f r,1 = X crit
3 ×V∩ X3,f r.
Finally since Z = X3,f r,1\ X3,f r is the closed subvariety the equation (12.54) follows from the gener al lemma
that follows the proof: we use X = X3,f r,1 and Z ′ = X crit
3 ×V in the lemma. ✷
Typically the stable locus is a open subset of some more natural bigge r space and we are interesting in
comparing the matrix factorizations on the big space with the ones o n the stable locus. The lemma below
shows that the category does not change as we pass to the stable locus as long the unstable locus does not
intersect the critical locus of the potential. The lemma is shown in mor e general case and we do not refer to
a stability a condition.
Lemma 12.3. SupposeX is a quasi-aﬃne variety and F = (M,D )∈ MF(X,W ),W∈ C[X]. The elements
of C[X] act on MF(X,W ) by multiplication. Let us assume that the elements of the ide al I = (f1,...,f m)⊂
C[X] act by zero homotopies on F and Z ′⊂X is the zero locus of I. Let Z⊂X be a subvariety deﬁned by
J = (g1,...,g n) such that Z∩Z ′ =∅. Then F is homotopic to F| X\Z as matrix factorization over C[X].
Proof. Let us the convention Xf for the open Zarisky subset of X which is a complement of the zero locus of
f . By the conditions of the lemma the open sets Xfi andXgi form a Cech cover of X and we denote by the
ˇCf,g (F ) the Cech resolution of F . The terms of the complex ˇCf,g (F ) are the matrix factorizations F| XS,T
whereS⊂{ 1,...,m } andT⊂{ 1,...,n } andXS,T is the complement to the zero locus of ∏
s∈Sfs
∏
t∈Tgt.
By the conditions of the lemma the matrix factorization F| XS,T is contractible if S ⁄=∅. Thus after
performing all the contractions we are left with ˇCg(F ) which is exactly F| X\Z and the lemma follows. ✷
12.6. T aking theBℓ quotient. Let us deﬁne the closure map: cl : Xℓ−1→ Xℓ by
cl(X,g 1,Y 1,...,g ℓ−1,Y ℓ−1) := (X,g 1,Y 1,...,g ℓ−1,Y ℓ−1,g 1,Y 1).
This map isG×Bℓ−1-equivariant withBℓ−1-action on Xℓ−1 induced by the group homomorphism id 2,...,ℓ−1×
∆ 1,ℓ.
We use the same notation for the maps of the framed and stable spa ces. Let us notice that the preimage of
the map cl applied to Xℓ+1,f r is the cyclicly framed space Xℓ,f c that consists of points (X,g 1,Y 1,...,g ℓ,Y ℓ,v )
satisfying :
C⟨Ad−1
gi (X),Y i⟩g−1(u) = V, g −1(u)∈V 0,i = 1,...,ℓ.
The intersection with the zero-locus of I crit
ℓ we denote by X crit
ℓ,f c .
70
Respectively, we have the pull back map:
cl∗ : MF sc
Bℓ−1(Xℓ,f r,W )→ MFsc
Bℓ−1(Xℓ−1,f c, 0),
and let us denote by Cσǫ1
i1 ,...,σ
ǫℓ
ℓ
the pull-back cl ∗(Cσǫ1
i1 ,...,σ
ǫℓ
ℓ
). We use the same nation for cl ∗(Cσǫ1
i1 ,...,σ
ǫℓ
ℓ
)∈
MFsc
Bℓ−1(Xℓ−1, 0), usually it is clear from the context which category of matrix fact orizations we work with.
Let us denote by MF sc,crit
Bℓ (Xℓ,f c, 0)⊂ MFsc
Bℓ(Xℓ,f c, 0), MF sc,crit
Bℓ (Xℓ, 0)⊂ MFsc
Bℓ(Xℓ, 0) the subcategory
consisting of matrix factorizations with the property that the idea lI crit
ℓ acts by zero homotopy. The element
Cσǫ1
i1 ,...,σ
ǫℓ+1
ℓ+1
is an element of the subcategory MF sc,crit
Bℓ (Xℓ,f c, 0).
Given an element C∈ MFsc,crit
Bℓ (Xℓ, 0) the homology
H∗(CEnℓ (C)) := H even(CEnℓ (C))⊕ Hodd(CEnℓ (C))
is a module over the ring of nℓ invariantsRnℓ
ℓ where Rℓ := C[X crit
ℓ ]. Let us ﬁx a notation for the aﬃne
scheme X crit
ℓ /U ℓ := Spec(Rnℓ
ℓ ). We use notation HU (Xℓ,C ) for H ∗(CEnℓ (C)) considered as Rnℓ
ℓ -module.
There is an natural map fgt : X crit
ℓ,f c→ X crit
ℓ and by applying the respective pull-back map we obtain
HU (Xℓ,f c,C ) := fgt ∗(HU (Xℓ,C ))∈ MFT ℓ(Xℓ,f c/U ℓ, 0).
The complex of sheaves HU (Xℓ,f c,C ) is T ℓ× ˆG-equivariant complex of sheaves on X crit
ℓ,f r/U ℓ and we
deﬁneHB(Xℓ,f c,C ) as a complex of sheaves of T ℓ-invariant sections ofHU (Xℓ,f c,C ). ThusHB(Xℓ,f c,C ) is
a complex of quasi-coherent sheaves on the quotient Xℓ,f c/Bℓ. The complex of sheaves HB(Xℓ,f c,C ) is ˆG-
equivariant hence the complex sheaves HB(Xℓ,f c,C ) ˆG of ˆG-invariant sections ofHB(Xℓ,f c,C ) is a complex
of quasi coherent sheaves on St ℓ.
