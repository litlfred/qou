---
doc_id: disssubmission
doc_title: "INAUGURAL-DISSERTATION Erlangung der Doktorwürde an der Naturwissenschaftlich-Mathematischen Gesamtfakultät der Ruprecht-Karls-Universität Heidelberg TANNAKIAN CATEGORIES OF PERVER"
section_id: sec-068-51-intersections-of-theta-divisors-97
section_title: "Intersections of theta divisors 97"
section_number: 5.1
pages: 105-107
source_pdf: DissSubmission.pdf
source_sha256: 207fd5e3dc0d278d
doc_brief: "INAUGURAL-DISSERTATION Erlangung der Doktorwürde an der Naturwissenschaftlich-Mathematischen Gesamtfakultät der Ruprecht-Karls-Universität Heidelberg TANNAKIAN CATEGORIES OF PERVERSE SHEAVES — 121 sec"
---
So the orthocomplement from above admits a decompositionV =V+⊕V−
into the eigenspaces
V−ε = Hg−2(Y,Q)−ε and Vε = Hg−2(X,Q)⊥⊆ Hg−2(Y,Q)ε
where now⊥ denotes the orthocomplement inside theε-eigenspace. Since
the restriction morphism in the weak Lefschetz theorem is a morphism of
Hodge structures,V− and V+ are Hodge substructures ofHg−2(Y,Q). To
compute their Hodge numbers one can use the Hirzebruch-Riemann-Roch
theorem together with the following result, where[Θ]∈ H2(X,Q) denotes
the fundamental class of the theta divisor.
LEMMA 5.5. In terms of the restrictionθ = [Θ]|Y∈H2(Y,Q), the Chern
classes of Y are given by
ci(Y) = (−1)i· (i +1)· θi∈ H2i(Y,Q).
In particular, the variety Y is of general type with canonical class KY = 2θ.
Proof.By deﬁnition we haveY = Θ∩Θx for some pointx∈ X(C). The
embeddingY ↪→ Θ gives an adjunction sequence
0−→TY−→TΘ|Y−→OX(Θx)|Y−→0
whereTY andTΘ are the tangent bundles toY resp.Θ (note that this makes
sense also if the theta divisor has isolated singularities, provided thatx is
chosen in such a way thatY does not meet the singularities). By restriction
of the adjunction sequence for the embeddingΘ ↪→ X we also get an exact
sequence
0−→TΘ|Y−→TX|Y−→OX(Θ)|Y−→0.
Since the tangent bundleTX is trivial, it follows from these two adjunction
sequences that the Chern polynomialct(Y) =1+c1(Y)·t +c2(Y)·t2 +···
satisﬁes
1 = ct(Y)· (1+θt)2
since the Chern polynomial is multiplicative in short exact sequences. From
this identity our claim about the Chern classes follows by a comparison of
coefﬁcients. By deﬁnition the canonical sheafωY is the top exterior power
of the cotangent bundleT∗Y , so for the canonical class we get
KY = c1(ωY) = c1(Λg−2(T∗
Y )) = c1(T∗
Y ) = −c1(Y) = 2θ
where in the third equality we have used that by the splitting principle the
ﬁrst Chern class of a bundle coincides with the ﬁrst Chern class of any of
its exterior powers [40, rem. 3.2.3(c)]. In particular, the canonical classKY
is ample and therefore also big in the sense of [71, sect. 2.2], so the smooth
varietyY is of general type. □
With notations as in the above lemma, to compute intersection numbers
between powers of Chern classes we only need to determine the image of
98 Chapter 5 – A family of surfaces
the top powerθg−2 under the degree map degY : Hg−2(Y,Q)−→Q. To
achieve this recall thatY is the intersection of two general translates of the
theta divisor. Since the intersection of cycles corresponds to the cup product
on cohomology, it follows that the fundamental class ofY is the cup product
square[Y] = [Θ]2∈ H4(X,Q). Hence
degY(θg−2) = degX([Θ]g−2· [Y]) = degX([Θ]g) = g!
where the last equality holds by the Poincar´e formula [13, sect. 11.2.1]. As
a direct application we have the following
COROLLARY5.6. For g≥2 the topological Euler characteristic of Y is
given by the formula
χ(Y) = (−1)g· (g−1)·g!.
Proof.By the Gauss-Bonnet theorem [48, p. 416] the topological Euler
characteristic of any compact complex manifold is equal to the degree of its
top Chern class. Henceχ(Y) =degY(cg−2(Y)), and the claim follows from
lemma 5.5 and from the above formula for the degree degY(θg−2). □
To get a feeling for the geometry involved in the above constructions,
let us take a more explicit look at the situation for some small values of the
dimensiong = dim(X) of the underlying ppav.
The case g= 2. Here Y consists of two points which are interchanged
by the involutionσ so that we have the following picture.
s
s
p
q
A
A U
K
Θ
Θx
The fundamental classesp,q of the two interchanged points ofY form a
basis ofH0(Y,Q), and the eigenspace
H0(Y,Q)+ = Q· (p+q) = H0(X,Q)
equals the image of the weak Lefschetz embedding. ThusV+ = 0, and the
Hodge structureV− = Q· (p−q) of weight zero has rank one.
The case g= 3. In this case the morphismY−→Y+ is an ´etale double
covering of smooth projective curves. To any such covering one can attach
its Prym variety [79] [13, ch. 12]. Before we come to the speciﬁc example
