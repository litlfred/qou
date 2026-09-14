---
doc_id: arxiv-2012.12159v3
doc_title: "A FUNK PERSPECTIVE ON BILLIARDS, PROJECTIVE GEOMETRY AND MAHLER VOLUME"
section_id: sec-011-32-the-volume-in-funk-geometry
section_title: "The volume in Funk geometry"
section_number: 3.2
pages: 11-13
source_pdf: 2012.12159v3.pdf
source_sha256: 473ec6959e82cd98
doc_brief: "A FUNK PERSPECTIVE ON BILLIARDS, PROJECTIVE GEOMETRY AND MAHLER VOLUME — We explore connections furnished by the Funk metric, a relative of the Hilbert metric, between projective geometry, billiards"
---
a smooth measure ~µ on int(K). Given x∈ int(K), choose a density dx =αx⊗νx∈
Dens(TxP) = Dens(x∗⊗V/x) = Dens(V∗/x⊥)⊗Dens((x⊥)∗). Then ν∗
x∈ Dens(x⊥)
is deﬁned by havingν∗
x⊗νx the symplectic (Liouville) volume onx⊥⊕(x⊥)∗. Choose
ξ∈ V∗/x⊥ with αx(ξ) = 1, and consider the intersection in V∗ of the cone K∨
with the aﬃne subspace x⊥ +ξ. We evaluate c(x) = ν∗
x(K∨∩ (x⊥ +ξ)) and set
~µx := c(x)dx∈ Dens(TxP). It is easily veriﬁed that the choice of αx,νx does not
matter. Thus ~µ is well-deﬁned in int(K).
Lemma 3.8. 1
ωn
~µ is the Holmes-Thompson volume of the projective co-nomadic
Finsler structure inside K.
Proof. Immediate from the construction. □
Next we construct a measure on P× P∨, which is analogous to the symplectic
volume onV⊕V∗. The group of projective automorphisms PGL(V ) acts on P∨ by
g(ξ) :=g−∗ξ. It holds that
Dens(Tx,ξ(P× P∨)) = Dens(x∗⊗V/x⊕ξ∗⊗V∗/ξ)
= Dens∗(x)n+1⊗ Dens∗(ξ)n+1⊗ Dens(V⊕V∗)
= Dens∗(x)n+1⊗ Dens∗(ξ)n+1 = Dens∗(x⊕ξ)n+1,
where all equalities are equviariant for the stablizer of ( x,ξ ) in PGL(V ).
Denote the incidence manifoldZ ={(x,ξ ) :x⊥ξ}⊂ P× P∨. We thus arrive at
Proposition 3.9. There is a one-dimensional space of projective-invariant mea-
sures on P× P∨\Z , with canonic normalization. Using the standard Euclidean
structure on Rn+1 to identify P and P∨ locally with the unit sphere, it is given by
dµ(x,ξ ) =|⟨x,ξ⟩|−(n+1)dσxdσξ
whereσx,σξ are the standard rotationally-invariant measures on each sphere.
Lemma 3.10. For a measurable set A⊂ int(K), it holds that ~µ(A) =µ(A×K∨).
12 A Funk perspective on billiards, projective geometry and Mahler volume
Proof. We have
µ(A×K∨) =
∫
A
dx
∫
K∨
dξ
|⟨x,ξ⟩|n+1.
Next we use the Euclidean structure for all choices in the deﬁnition of~µ. Assume
x =en+1, so TxP =T∗
x P =e⊥
n+1. Choose dx =dx, αx =x, so that ξ =x, and νx,
ν∗
x are both the Euclidean volume. So it remains to check that
∫
K∨∩Sn
dξ
|ξn+1|n+1 =|K∨∩ (en+1 +e⊥
n+1)|.
As the jacobian of the map
Sn→en+1 +e⊥
n+1, ξ ↦→ξ/ξn+1 (2)
is 1/|ξn+1|n+1, the claim follows. □
Corollary 3.11. The Holmes-Thompson volume of the Funk metric in the interior
of L, denoted volF
L, is a projective invariant of L, that is independent of a choice
of a hyperplane at inﬁnity. Furthermore, if K⊂ int(L) is convex, there is a duality
of Funk volumes: volF
L(K) = volF
K∨(L∨).
Proof. The ﬁrst part follows from Proposition 3.4 and the paragraph after Deﬁnition
3.1. The second is immediate from Lemmas 3.8 and 3.10. □
Let volH
K denote the Holmes-Thompson volume of the Hilbert metric in int( K).
Corollary 3.12. GivenK⊂ int(L) in RPn, volH
L (K)≤ 1
2n
(2n
n
)
volH
K∨(L∨). Equal-
ity is uniquely attained when L is a simplex, and K is an ellipsoid.
Proof. Choose an aﬃne chart and assume 0 ∈ int(K). By the Rogers-Shephard
inequality and the duality of volumes,
volH
L (K) = 1
ωn
∫
K
|1
2(Lz−Lz)|dz≤ 1
2nωn
(2n
n
)∫
K
|Lz|dz = 1
2n
(2n
n
)
volF
L(K)
= 1
2n
(2n
n
)
volF
Ko(Lo).
On the other hand by the Brunn-Minkowski inequality,
volF
Ko(Lo) = 1
ωn
∫
Lo
|(Ko)z|dz≤ 1
ωn
∫
Lo
|1
2((Ko)z− (Ko)z)|dz = volH
Ko(Lo).
The Rogers-Shephard inequality becomes an equality when L is a simplex, while
the Brunn-Minkowski inequality above gives equality for symmetric bodies, that is
(Ko)z must have antipodal symmetry (with respect to some point) for everyz∈Lo.
A projective center of a convex body in RPn is a center of antipodal symmetry
for the body in some aﬃne chart containing K. The sets ( Ko)z are projectively
equivalent to K, and we ﬁnd that the set Lo ⊂ int(K∨) parametrizes diﬀerent
choices of hyperplanes η⊥ at inﬁnity, for which K⊂ RPn\η⊥ has antipodal sym-
metry with some center point. But that implies that every η∈ Lo is a projective
center for K∨⊂ P∨. By [18, Theorem 9-3.], we conclude that K∨, and therefore
K, must be a convex quadric, that is an ellipsoid. □
13 A Funk perspective on billiards, projective geometry and Mahler volume
