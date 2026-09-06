---
doc_id: arxiv-1608.03227v4
doc_title: "January 30, 2018"
section_id: sec-031-62-computational-aspects-of-push-forward
section_title: "Computational aspects of push-forward"
section_number: 6.2
pages: 32-33
source_pdf: 1608.03227v4.pdf
source_sha256: c71128e9a6c35343
doc_brief: "January 30, 2018 — For each braid β ∈ Brn we construct a 2-periodic complex Sβ of quasi-coherent C∗ × C∗ - equivariant sheaves on the non-commutative nested Hilbert scheme Hilb f ree 1,n ."
---
F = (M,D,d l,d r) we make a choice of the extension ˜D of the diﬀerential D from sub-variety X ◦
2 (Pk)
to X ◦
2 (Gn). However in our case we have a canonical choice of the extension b ecause we could use the
projection map Lie( Gn)→ Lie(Pk) to construct such an extension and use the remark 3.3, the deta ils are
provided below. Morally, we would like to interpret ik as a section of some map and it is possible if we
enlarge our space slightly.
In this subsection we use notation adj( A) for the adjoint of matrix A. Let us introduce space X ◦
2 (Gn)♭ :=
gn× Lie(Gn)× n2
n. There is a natural embedding
jn : X ◦
2 (Gn)→ X ◦
2 (Gn)♭
induced by the embedding Gn→ gln. If we deﬁne
W ♭(X,g,Y 1,Y 2) = Tr(X(Y1 det−gY2adj(g))), det = det(g)
then we have j∗
n(W· det) = W ♭ and the map
j∗
n : MF sc
B2n
(X ◦
2 (Gn)♭,W ♭)→ MFsc
B2n
(X ◦
2 (Gn)♭,W ′),
where W ′ =W· det, is well deﬁned.
Similarly, we deﬁne X ◦
2 (Pk)♭ and X
◦
2(Pk)♭. The natural map
jk
n : X ◦
2 (Pk)→ X ◦
2 (Pk)♭
induces the pull back map
jk∗
n : MF sc
B2 (X ◦
2 (Pk)♭,W ♭)→ MFsc
B2(X ◦
2 (Pk),W ′).
Since W ′ and W diﬀer by the non-vanishing factor det, there is an embedding of cat egories det :
MFsc
B2(X ◦
2 ,W )→ MFsc
B2 (X ◦
2,W ′):
det : [M0
D0
−−→M1
D1
−−→M1]↦→[M0
D0·det
−−−−→M1
D1
−−→M0].
We the inverse functor we denote by det −1 and we use the same notation for the functors between the
categories related to the parabolic versions of the categories.
There is no natural map between X ◦
2 (Gn) and X ◦
2 (Pk) but there is a natural linear projection ρk :
X ◦
2 (Gn)♭→ X ◦
2 (Pk)♭ and there is a pull back map
ρ∗
k : MF sc(X ◦
2 (Pk)♭,W ♭)→ MFsc(X ◦
2 (Gn)♭,ρ ∗
k(W ♭)).
There is also a natural inclusion map ik : X ◦
2 (Pk)♭→ X ◦
2 (Gn)♭ which is a section of the projection ρk:
ρk◦ik =id. Hence there is F ′∈ MFsc
B2n
(X ◦
2 (Pk)♭,W ♭) such that jk∗
n (F ′) = det(F ) and we deﬁne
˜F = ( ˜M, ˜D, ˜∂l, ˜∂) := det −1◦j∗
n◦ρ∗
k(F ′)∈ MFsc(X ◦
2 (Gn),j ∗
n◦ρ∗
k(W ♭)· det−1).
By construction we have ˜F| X ◦
2 (Pk) =F . Thus the matrix factorization ˜F provides the ﬁrst step of the
construction of the push forward ik∗(F ) from section 3.7. By completing the second step of the construct ion
from the section 3.7 we obtain the matrix factorization:
ik∗(F ) = ( ˜M,d K + ˜D +d−,∂ l,∂ r),
where dK : ˜M⊗ Λ •V → ˜M⊗ Λ •−1V is the Koszul diﬀerential for the deﬁning ideal of X ◦
2 (Pk)⊂ X ◦
2 (Gn)
and d− = ∑
i<jd−
ij, d−
ij : ˜M⊗ Λ iV → ˜M⊗ Λ jV is the complementary diﬀerential: ( dk + ˜D +d−)2 =W
32
Note that because of our choice of extension ˜F the diﬀerentials d−
ij vanish unless j =i + 1, we give more
details below. Deﬁne a linear operator operator Π k
+ : gn→ pk which is a natural projection. Respectively,
we have Π k
−−(A) = A− Π k
+(A). The diﬀerence δkW :=W−j∗
n◦ρk∗
n (W ♭)· det−1 could be written as sum
of two terms:
δkW1 := Tr(Π k
−−(X)· Π k
++(Y1− Adg12 (Y2))),
δkW2 := Tr(Π k
+(X)· Π k
−(Adg12 (Y2)−ρk(g12)(Y2)adj(ρk(g12)) det(g12)−1),
where we use convention Id = Π k
− + Π k
++.
Since δkW1∈ (Π k
−−(X)) and δkW2∈ (Π k
−−(g12)) we have
ik∗(F )♯ = ˜F⊗ [Π k
−−(X), Π k
++(Y1− Adg12 (Y2))]⊗ KδkW2 (Π k
−−(g12)).
That is the diﬀerentials d−
ij are the negative diﬀerentials of the Koszul matrix factorization an d hence have
above mentioned property.
