---
doc_id: arxiv-0811.2435v1
doc_title: "Stability structures, motivic"
section_id: sec-022-an-integral-identity
section_title: "An integral identity"
section_number: null
pages: 69-73
source_pdf: 0811.2435v1.pdf
source_sha256: 615b04eca83bcade
doc_brief: "Stability structures, motivic — 43 sections: Introduction; Counting problems for 3-dimensiona; Non-commutative varieties with pol"
---
In this section we are going to discuss the identity which wil l be crucial in
the proof of the main theorem of Section 6.
Let k be a ﬁeld of characteristic zero, and V1,V 2,V 3 be ﬁnite-dimensional
k-vector spaces.
Conjecture 4 Let W be a formal series on the product V1×V2×V3 of
three vector spaces, depending in a constructible way on ﬁni tely many extra
parameters, such thatW (0, 0, 0) = 0 andW has degree zero with respect to the
diagonal action of the multiplicative group Gm with the weights (1,−1, 0). We
denote by ˆW the Gm-equivariant extension of W to the formal neighborhood
ˆV1 of V1×{ 0}×{ 0}⊂ V1×V2×V3. Then we have the following formula
(where we denote the direct image by the integral):
∫
v1∈V1
(1−MF (v1,0,0)(ˆW )) = LdimV1(1−MF (0,0,0)(W|(0,0,V3))) ,
69
where in the RHS we consider the motivic Milnor ﬁber at (0, 0, 0) of the
restriction of W to the subspace (0, 0,V 3).
Using the obvious equality
∫
V1
1 = LdimV1 we can rewrite the identity as
∫
v1∈V1
MF (v1,0,0)(ˆW ) = LdimV1·MF (0,0,0)(W|(0,0,V3)) .
Let us discuss the l-adic version of the Conjecture. For simplicity we
assume that the vector spaces do not depend on extra paramete rs. Then we
have a morphism of formal schemes π : ˆV1→Spf (k[[w]]) such that w↦→ˆW
as well as an embedding iV1 : V1→ ˆW−1(0). For any morphism π : X→
Spf (k[[w]]) of formal schemes to we denote by Rψπ the functor of nearby
cycles. It acts from the bounded derived category of l-adic constructible
sheaves onX to the bounded derived category of l-adic constructible sheaves
onX0 =π−1(0) endowed with the action of the inertia group (hence they c an
be informally thought of as l-adic constructible sheaves onX0×Spec(k)k((w))).
Proposition 9 The complex RΓ c(i∗
V1Rψπ(Ql)) is isomorphic (as a complex
of Gal(
k((w))/k((w)))-modules) to the complex RΓ c(V1, Ql)⊗j∗Rψbπ(Ql),
where j : Spec(k)→ V3,j (0) = 0 is the natural embedding and ˆπ is the
morphism of the formal completion of 0∈{ 0}×{ 0}× V3 to Spf (k[[w]])
given by the restriction W|{ 0}×{0}×V3.
Proof. We will give a sketch of the proof based on the non-archimedea n
model for the Milnor ﬁber described in Section 4.3.
Let us consider the k((t))-analytic space (in the sense of Berkovich) as-
sociated with the scheme ( V1×V2×V3)×Spec(k)Spec(k((t))). Let us choose
suﬃciently small positive numbers ε1,ε 2,ε 3,ε 4 (we will specify them later)
and deﬁne an analytic subspace Y =Yε1,ε2,ε3,ε4 by the following inequalities:
|v1|≤ 1 +ε1, |v2|,|v3|≤ ε2, ε4≤|W (v1,v 2,v 3)|≤ ε3 .
Notice that the seriesW (v1,v 2,v 3) is convergent onY because of homogeneity
property. We introduce another analytic space Y′ = Y′
ε1,ε2,ε3,ε4⊂ Yε1,ε2,ε3,ε4
by changing the inequality |v1|≤ 1 + ε1 to the equality |v1| = 1 + ε1 (all
other inequalities remain unchanged). There is a natural pr ojection prY→A
(resp. its restriction prY ′→A) of Y (resp. of Y′) to the annulus A ={w|ε4≤
|w|≤ ε3}. Let us now consider the complex
Cone((prY→A)∗(Ql)→ (prY ′→A)∗(Ql))[−1].
70
This is a lisse sheaf on the annulus, i.e. a continuous l-adic representation of
the fundamental group of the k((t))-analytic space A. There is a tautological
embedding k((w))→ Oan(A). It induces the homomorphism of proﬁnite
groups π1(A)→ Gal(k((w))/k((w))). Then one can show that the complex
Cone((prY→A)∗(Ql)→ (prY ′→A)∗(Ql))[−1]≃
≃ (prY→A)∗(Cone(Ql→ (iY ′֒→Y )∗Ql))
on A is quasi-isomorphic to the pull-back of the complex RΓ c(i∗
V1Rψπ(Ql))
of Gal(
k((w))/k((w)))-modules.
We decompose the space Y into a disjoint union Y0⊔Y1 where for Y0
we have|v1||v2| = 0 while for Y1 we have|v1||v2|⁄= 0. Similarly, we have a
decomposition Y′ =Y′
0⊔Y′
1. We claim that the complex
(prY0→A)∗(Cone(Ql→ (iY ′
0֒→Y0)∗Ql))
is quasi-isomorphic to the pull-back of the complex RΓ c(V1, Ql)⊗j∗Rψbπ(Ql)
of Gal( k((w))/k((w)))-modules. Notice that W|Y0 depends on v3 only. Fur-
thermore, Y0 and Y′
0 can be decomposed as the products
Y0 =Y3×Z0, Y′
0 =Y3×Z′
0 ,
where
Z0 :={(v1,v 2)∈Van
1 ×Van
2 | v1 = 0 or v2 = 0,|v1|≤ 1 +ε1,|v2|≤ ε2} ,
Z′
0 :={(v1,v 2)∈Van
1 ×Van
2 | v2 = 0,|v1| = 1 + ε1} ,
Y3 :={v3∈Van
3 || v3|≤ ε2, ε4≤|W (0, 0,v 3)|≤ ε3} .
Here we denote by Van
i ,i = 1, 2, 3 the k((t))-analytic space associated with
the scheme Vi×Spec(k)Spec(k((t)),i = 1, 2, 3. Notice that Z0 is the bouquet
of two (non-archimedean) balls. It follows that the inclusi on of the ball
Z′′
0 ={(v1, 0)||v1|≤ 1 +ε1}
into Z0 induces isomorphisms of the Berkovich ´ etale cohomology gr oups of
thel-adic sheaves on the analytic spaces. Therefore the cohomol ogy groups of
the pair ( Z0,Z′
0) coincide with the cohomology groups of the pair ( Z′′
0,Z′
0).
The latter are equal to RΓ c(Van
1 , Ql) (which corresponds to the image of
LdimV1 in K0(Gal(k((t))/k((t)))−mod)).
71
We have an obvious morphism of complexes of sheaves on Y :
f :Cone(Ql→ (iY ′֒→Y )∗Ql)→Cone((iY0֒→Y )∗Ql→ (iY ′
0֒→Y )∗Ql) .
In order to prove the Proposition we have to prove that the ( prY→A)∗f is
a quasi-isomorphism, i.e. ( prY→A)∗(Cone(f )) is zero. The compactness of
spaces Y,Y ′,Y 0,Y ′
0 implies that
(prY→A)∗(Cone(f ))≃ (prY1→A)!(Cone(Ql→ (iY ′
1→Y1)∗Ql)) .
The (partially deﬁned) actions of the group Gm on Y1 and Y′
1 are free,
and the value of W does not change under the action. More precisely, one
can deﬁne easily analytic “spaces of orbits” ~Y1⊃~Y′
1 of Gm acting on Y1 and
Y′
1 respectively. The projections
Y1→~Y1, Y′
1→~Y′
1
are proper maps, and the map W factors through them. Hence it is enough
to check that
(prY1→ eY1)∗(Cone(Ql→ (iY ′
1֒→Y1)∗Ql))≃ 0 .
This follows from the fact that every orbit in Y1 is a closed annulus, its
intersection with Y′
1 is a circle, and the inclusion of a circle into an annulus
induces an isomorphism of ´ etale cohomology groups.
This concludes the sketch of the proof. ■
Remark 18 1) In the proof we did not specify the values of εi,i = 1, 2, 3, 4.
We can take ε4 =O(ε3) (e.g. take ε4 = 1
2ε3),ε2 =o(1) andε3 =O(εN
2 ),ε 1 =
O(εM
3 ) for some integers N,M > 0.
2) In the proof we used the comparison of the cohomology of the sheaf
of nearby cycles with the ´ etale cohomology of subvarieties of k((t))-analytic
spaces (see [54]).
We strongly believe that the analog of the Proposition holds at the level
of motivic rings in the case char k = 0.
72
