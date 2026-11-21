---
doc_id: ant-v14-n7-s-p05
doc_title: "Motivic Gauss–Bonnet formulas"
section_id: sec-008-8-applications
section_title: "Applications"
section_number: 8
pages: 36-50
source_pdf: ant-v14-n7-s-p05.pdf
source_sha256: 1c8e94ff62a8d920
toc_source: inferred
doc_brief: "Motivic Gauss–Bonnet formulas — 12 sections: Front matter; Introduction; X+ ∈SH(k) is dualizable. In partic"
---
In this section, we apply the motivic Gauss–Bonnet formula of Section 5 and the comparison results of
Section 7 to various speciﬁc SL-oriented cohomology theories, and thereby make computations of the
motivic Euler characteristic χ(X/B) in different contexts.
8A. Motivic cohomology and cohomology of the Milnor K-theory sheaves. We work over the base-
scheme B = Spec k, with k a perfect ﬁeld. In SH(k) we have the motivic cohomology spectrum HZ
representing Voevodsky’s motivic cohomology (see, e.g., [Levine 2008, §6.2] for a construction valid in
arbitrary characteristic). By [Voevodsky 2002], there is a natural isomorphism
HZa,b(X) ≃CHb(X, 2b −a)
for X ∈SmB, where CHb(X, 2b −a) is Bloch’s higher Chow group [1986].
HZ admits a localization sequence: for i : Z →X a closed immersion of codimension d in Smk, there
is a canonical isomorphism
HZa,b
Z (X) ≃HZa−2d,b−d(Z).
See for example [Bloch 1994]. In particular, for p : V →X a rank r vector bundle over X ∈Smk, we
have the isomorphism
HZ2r,r
0V (V ) ≃HZ0,0(X)
which gives us Thom classes ϑHZ
V
∈HZ2r,r
0V (V ) corresponding to the unit 1HZ
X ∈HZ0,0(X). Thus HZ is a
GL-oriented motivic spectrum.
Let X be a smooth projective k-scheme of dimension n over k. For a class x ∈HZ2n,n(X), the
isomorphism HZ2n,n(X) ≃CHn(X, 0) = CHn(X) allows one to represent x as the class of a 0-cycle
˜x = P
i ni pi, with the pi closed points of X. One has the degree degk(pi) := [k(pi) : k] and extending by
linearity gives the degree degk(˜x), which one shows passes to rational equivalence to deﬁne a degree map
degk : HZ2n,n(X) →CH0(Spec k) = Z.
As a GL-oriented theory, HZ has Chern classes for vector bundles: cr(V ) ∈HZ2r,r(X) for V →X a
vector bundle over some X ∈Smk and r ≥0.
Theorem 8.1. Let X ∈Smk be projective of dimension dX. Then
uHZ(χ(X/k)) = degk(cdX(TX/k)).
Proof. One has well-deﬁned pushforward maps on CH∗(−, ∗) for projective morphisms (see, e.g., [Bloch
1986, Proposition 1.3]). Via the isomorphism HZa,b(X) ≃CHb(X, 2b −a) [Voevodsky 2002], this
gives pushforward maps ˆf∗on HZ∗,∗for f : Y →X a projective morphism in SmB (see [Bloch 1986]
for details), making (X, Z) 7→HZ∗,∗
Z (X) a GL-oriented cohomology theory on Smk. In addition, for
πX : X →Spec k in Smk projective of dimension n, the map ˆπX∗: HZ2n,n(X) →CH0(Spec k) = Z is
degk, and for i : Y →X a closed immersion, the map ˆi∗is given by the localization theorem, which
Motivic Gauss–Bonnet formulas
1837
readily implies that ˆi∗= i∗. By our comparison Theorem 7.1, which here really reduces to the theorem of
Panin and Smirnov, it follows that ˆf∗= f∗for all projective f.
Finally, one has cdX = s∗s∗(1HZ
X ) = eHZ(V ) [Fulton 1984, Corollary 6.3], so applying the motivic
Gauss–Bonnet Theorem 5.3 gives the statement.
□
One can obtain the same result by using the cohomology of the Milnor K-theory sheaves as a bigraded
cohomology theory. The homotopy t-structure on SH(k) has heart the abelian category of homotopy
modules 5*(k) (see [Morel 2004, §5.2; 2012] for details); we let H0 : SH(k) →5*(k) be the associated
functor. The fact that HZn,n(Spec F) ≃KM
n (F) for F a ﬁeld [Nesterenko and Suslin 1989; Totaro 1992]
says that H0HZ is canonically isomorphic to the homotopy module (KM
n )n, which is in fact a cycle module
in the sense of Rost [1996]. This gives us the isomorphism
H0HZa,b(X) ≃Ha(X, KM
b ).
The isomorphism Hn(X, KM
n ) ≃CHn(X) (a special case of Rost’s formula [1996, Corollary 6.5] for the
Chow groups of a cycle module) gives us as above Thom classes ϑKM
∗(V ) ∈H0HZ2r,r
0V (V ), giving H0HZ
a GL-orientation. As for HZ∗,∗, one has explicitly deﬁned pushforward maps on H∗(−, KM
∗) which give
H0HZ∗,∗the structure of a GL-oriented cohomology theory on Smk and for which the pushforward map
for the zero-section of a vector bundle is given by the Thom isomorphism. Since the pushforward on
Hn(X, KM
n ) agrees with the classical pushforward on CHn, we deduce the following using the same proof
as for Theorem 8.1.
Theorem 8.2. Let X ∈Smk be projective of dimension dX. Then
uH0HZ(χ(X/k)) = degk(cdX(TX/k)) in CH0(Spec k) = Z.
8B. Algebraic K-theory. We now let B be any regular separated base-scheme of ﬁnite Krull dimension.
Algebraic K-theory on SmB is represented by the motivic commutative ring spectrum KGL ∈SH(B); see
[Voevodsky 1998, §6.2]. Just as for HZ, the purity theorem
KGLa,b
Z (X) ≃KGLa−2c,b−c(Z)
for i : Z →X a closed immersion of codimension d in SmB (a consequence of Quillen’s localization
sequence for algebraic K-theory [1973, §7, Proposition 3.2]) gives Thom class ϑKGL(V ) ∈KGL2r,r
0V (V )
for V →X a rank r vector bundle over X ∈SmB, and makes KGL a GL-oriented motivic spectrum.
Explicitly, KGL represents Quillen K-theory on SmB via KGLa,b ≃K2b−a and the Thom class for a
rank r vector bundle p : V →X is represented by the Koszul complex KosV (p∗V ∨, can). Here
can : p∗V ∨→OV
is the dual of the tautological section OV →p∗V and KosV (p∗V ∨, can) is the complex whose terms are
given by
KosV (p∗V ∨, can)−r = 3r p∗V ∨
1838
Marc Levine and Arpon Raksit
and whose differential 3r p∗V ∨→3r−1 p∗V ∨is given with respect to a local framing of V ∨by
d(ei1 ∧· · · ∧eir) =
r
X
j=1
(−1) j−1can(ei j) · ei1 ∧· · · ∧b
ei j ∧· · · ∧eir.
This complex is a locally free resolution of s∗(OX), where s : X →V is the zero-section. Thus, by the identi-
ﬁcation of KGL2r,r
0V (V ) with the Grothendieck group of the triangulated category of perfect complexes on V
with support contained in 0V , KosV (p∗V ∨, can) gives rise to a class [KosV (p∗V ∨, can)] ∈KGL2r,r
0V (V )
which maps to 1X under the purity isomorphism KGL2r,r
0V (V ) ≃KGL0,0(X), so that we indeed have
[KosV (p∗V ∨, can)] = ϑKGL(V ).
Just as for motivic cohomology, one has explicit pushforward maps in K-theory given by Quillen’s
localization and devissage theorems identifying, for X ∈SmB and Z ⊆X a closed subscheme, the K-theory
with support KZ(X) with the K-theory of the abelian category of coherent sheaves CohZ on Z, denoted
G(Z). For a projective morphism f : Y →X, one has the pushforward map ˆf∗: G(Y) →G(X) deﬁned
by using a suitable subcategory of CohY on which f∗is exact. On K0, this recovers the usual formula
ˆf∗([F]) =
dim Y
X
j=0
(−1) j[R j f∗(F)]
for F ∈CohY. Via the isomorphisms KGLa,b
Z (X) ≃G2b−a(Z), this gives pushforward maps ˆf∗for
KGL∗,∗, deﬁning a GL-oriented cohomology theory on SmB.
For s : X →V the zero-section of a vector bundle, ˆs∗agrees with the pushforward s∗using the Thom
isomorphism/localization theorem, hence by our comparison theorem (again really the theorem of Panin
and Smirnov), we have ˆf∗= f∗for all projective f.
Theorem 8.3. Let πX : X →B be a smooth projective morphism with B a regular separated scheme of
ﬁnite Krull dimension. Then
uKGL(χ(X/B)) =
dimB X
X
j=0
dimB X
X
i=0
(−1)i+ j[R jπX∗i
X/B] ∈K0(B) = KGL0,0(B).
Proof. Let p : TX/B →X denote the relative tangent bundle and let s : X →TX/B denote the zero-section.
We have
eKGL(TX/B) = s∗(th(TX/B)) = s∗(KosTX/B(p∗T ∨
X/B, can)).
Since T ∨
X/B = X/B, and s∗(can) is the zero-map, it follows that, in K0(X),
s∗(KosTX/B(p∗T ∨
X/B, can)) =
dimB X
X
i=0
(−1)i[i
X/B],
and thus
πX∗(eKGL(TX/B)) =
dimB X
X
j=0
dimB X
X
i=0
(−1)i+ j[R jπX∗i
X/B].
Motivic Gauss–Bonnet formulas
1839
We conclude by applying the motivic Gauss–Bonnet theorem.
□
8C. Milnor–Witt cohomology and Chow–Witt groups. In this case, we again work over a perfect base-
ﬁeld k. The Milnor–Witt sheaves KMW
∗
constructed by Morel [2004, §6; 2012, Chapter 3] give rise to an
SL-oriented theory as follows. Morel describes an isomorphism of KMW
0
with the sheaﬁﬁcation GW of
the Grothendieck–Witt rings;1 the map of sheaves of abelian groups Gm →GW× sending a unit u to the
one-dimensional form ⟨u⟩allows one to deﬁne, for L →X a line bundle, a twisted version
KMW
∗
(L) := KMW
∗
×Gm L×
as a Nisnevich sheaf on X ∈Smk (see [Morel 2012, p. 118] or [Calmès and Fasel 2014, §1.2]). One may
use the Rost–Schmid complex for KMW
∗
(L) [Morel 2012, Chapter 5] to compute H∗
Z(X, KMW
∗
(L)) for
Z ⊆X a closed subset, which gives a purity theorem: for i : Z →X a codimension d closed immersion
in Smk and L →X a line bundle, there is a canonical isomorphism
H∗
Z(X, KMW
∗
(L)) ≃H∗−d(Z, KMW
∗−d(i∗L ⊗det Ni)),
(8.3.1)
where Ni →Z is the normal bundle of i. Applying this to the zero-section of a rank r vector bundle
p : V →X gives the isomorphism
H0(X, GW) ≃Hr
0V (V, KMW
r
(p∗det−1 V ));
(8.3.2)
in particular, given an isomorphism φ : det V →OX, we obtain a Thom class
θV,φ ∈Hr
0V (V, KMW
r
)
corresponding to the unit section 1X ∈H0(X, GW).
On the other hand, Morel’s computation [2004, Theorem 6.4.1, Remark 6.4.2; 2012, Theorem 6.40] of
the zeroth graded homotopy sheaf of the sphere spectrum gives an identiﬁcation
H0(1k) ≃(KMW
n
)n∈Z
in 5*(k), which then gives the natural isomorphism
H0(1k)a+b,b
Z
(X) ≃Ha
Z(X, KMW
b
).
This is moreover compatible with twisting by a line bundle p : L →X, on the H0(1k) side using the
Thom space construction
H0(1k)∗,∗
Z (X; L) := H0(1k)∗+2,∗+1
Z
(L)
1Morel [2012, Lemma 3.10] deﬁned an isomorphism GW(F) →KMW(F), F a ﬁeld. Morel [2012, §3.2] deﬁned KMW
∗
as
an unramiﬁed sheaf and it follows from [Ojanguren and Panin 1999, Theorem A] that GW is an unramiﬁed sheaf. From this it is
not difﬁcult to show that the isomorphism GW(F) →KMW(F) for ﬁelds extends to an isomorphism of sheaves.
1840
Marc Levine and Arpon Raksit
and on the Milnor–Witt cohomology side using the twisted Milnor–Witt sheaves. To see this, note that
the “untwisted” isomorphism gives us an isomorphism
H0(1k)a+b+2,b+1
Z
(Th(L)) ≃H0(1k)a+b+2,b+1
0L∩p−1(Z) (L) ≃Ha+1
0L∩p−1(Z)(X, KMW
b+1),
so it sufﬁces to identify the right-hand side with Ha
Z(X, KMW
b
(L)). For Y ∈Smk and line bundle M →Y, the
Rost–Schmid complex for KMW
m
(M) consists in degree a of sums of terms of twisted Milnor–Witt groups
of the form KMW
m−a(k(y); 3a(my/m2
y)∨⊗M), for y a codimension a point of Y and my ⊂OY,y the maximal
ideal. To compute cohomology with supports in W ⊆Y, one restricts to those y ∈W. If we now take Y = L
and M the trivial bundle, with supports in p−1(Z) ∩0L and m = b + 1, and compare with Y = X, with
supports in Z with m = b, the term for y ∈Z, of codimension a+1 on L is KMW
b−a(k(y); 3a(my/m2
y)∨⊗L)
while the term for y ∈Z, of codimension a on X is KMW
b−a(k(y); 3a(my/m2
y)∨), where my is the maximal
ideal in OX,y in both cases. This gives the desired identiﬁcation
Ha+1
0L∩p−1(Z)(X, KMW
b+1) ≃Ha
Z(X, KMW
b
(L)).
The purity isomorphism (8.3.1) is a special case of this construction.
The Thom class θV,φ ∈Hr
0V (V, KMW
r
) gives the Thom class
θV,φ ∈H0(1k)2r,r
0V (V ),
making H0(1k) an SL-oriented theory; see, e.g, [Levine 2017b, §3.2]. The resulting canonical Thom class
thV ∈H0(1k)2r,r
0V (V ; det−1 V ) = Hr
0V (V, KMW
r
(det−1 V ))
agrees with the image of 1X ∈H0(X, GW) under the Rost–Schmid isomorphism (8.3.2).
Let πX : X →Spec k be smooth and projective over k of dimension d. Using the Rost–Schmid
complex for the twisted homotopy module one has generators for Hd(X, KMW
d
(ωX/k)) as formal sums
˜x = P
i αi · pi, with αi ∈GW(k(pi)) and pi ∈X closed points. Since k is perfect, the ﬁnite extension
k(pi)/k is separable and one can deﬁne
g
degk(˜x) :=
X
i
Trk(pi)/kαi ∈GW(k)
where Trk(pi)/k : GW(k(pi)) →GW(k) is the transfer induced by the usual trace map Trk(pi)/k : k(pi) →k;
see, for example, [Calmès and Fasel 2014, Lemma 2.3]. It is shown in [Calmès and Fasel 2014, §3] that
this descends to a map
g
degk : H2d,d
0
(X; ωX/k) = Hd(X, KMW
d
(ωX/k)) →H0,0
0 (Spec k) = GW(k).
See also [Hoyois 2014, Lemma 5.10], which identiﬁes this map with one induced by the Scharlau trace.
The methods of this paper give a new proof of the result given in [Levine 2017b, Lemma 1.5]:
Theorem 8.4. Let k be a perfect ﬁeld of characteristic different from two. For πX : X →Spec k smooth
and projective over k, we have
χ(X/k) = g
degk(eH0(1k)(TX/k)).
Motivic Gauss–Bonnet formulas
1841
Proof. Under Morel’s isomorphism EndSH(k)(1X) ≃GW(k) [2004, Theorem 6.4.1, Remark 6.4.2; 2012,
Theorem 6.40] and the isomorphism H0(Spec k, KMW
0
) ≃GW(k), the unit map uH0(1k) : 1k →H0(1k)
induces the identity map on π0,0. Using this, the proof of the claim is essentially the same as the other
Gauss–Bonnet theorems we have discussed, but with a bit of extra work since we are no longer in the
GL-oriented case.
Fasel [2008] has deﬁned pushforward maps
ˆf∗: Ha
W(X, KMW
b
(ωX/k ⊗f ∗L)) →Ha−d
Z
(Y, KMW
b−d(L))
for each projective morphism f : X →Y in Smk of relative dimension d, line bundle L →Y, and closed
subsets Z ⊆Y, W ⊆X with f (W) ⊆Z. In the case of the structure map πX : X →Spec k, the pushforward
eπX∗: Hd(X, KMW
d
(ωX/k)) →H0(Spec k, KMW
0
) = GW(k) is the map g
degk.
For s : X →V the zero-section of a vector bundle, ˆs∗is the Thom isomorphism s∗. Thus, if we pass
to the η-inverted theory, H0(1X)η := H0(1k)[η−1], our comparison Theorem 7.1 says that ˆfη∗= fη∗for
all projective morphisms f in Smk. We have KMW
∗
[η−1] ≃W, the sheaf of Witt rings, and the map
KMW
0
= GW →KMW
∗
[η−1] ≃W is the canonical map q : GW →W realizing W as the quotient of GW
by the subgroup generated by the hyperbolic form. Thus, applying our motivic Gauss–Bonnet theorem
gives the identity
q(χ(X/k)) = q(g
degk(eH0(1k)(TX/k))) in W(k).
To lift this to an equality in GW(k) and thereby complete the proof, we use that the map
(rnk, q) : GW →Z × W
is injective, together with the fact that we can recover the rank by applying H0 to the unit map 1k →HZ
and using Theorem 8.2.
□
8D. Hermitian K-theory and Witt theory. We again let our base-scheme B be a regular noetherian
separated base-scheme of ﬁnite Krull dimension, but now assume that 2 invertible on B. Our goal in
this subsection is to explain how the description of the “rank” of χ(X/B) given by Theorem 8.3 can be
reﬁned to give a formula for χ(X/k) itself in terms of Hodge cohomology by using hermitian K-theory.
By work of Panin and Walter [2018], Schlichting [2010], and Schlichting and Tripathi [2015], hermitian
K-theory KO[∗]
∗(−) is represented by a motivic commutative ring spectrum BO ∈SH(B) (we use the
notation of [Ananyevskiy 2016b]). Panin and Walter gave BO an SL-orientation. BO-theory also represents
particular cases of Schlichting’s Grothendieck–Witt groups [2010], via functorial isomorphisms
BO2r,r(X; L) ≃KO[r]
0 (X, L) := GW(Dperf(X), L[r], can),
where L →X is a line bundle and GW(Dperf(X), L[r], can) is the Grothendieck–Witt group of L[r]-valued
symmetric bilinear forms on Dperf(X); we recall a version of the deﬁnition here.
1842
Marc Levine and Arpon Raksit
Deﬁnition 8.5. Let L →X be a line bundle and let r ∈Z. An L[r]-valued symmetric bilinear form on
C ∈Dperf(X) is a map
φ : C ⊗L C →L[r]
in Dperf(X) which satisﬁes the following conditions.
(i) φ is nondegenerate: the induced map C →RHom(C, L[n]) is an isomorphism in Dperf(X).
(ii) φ is symmetric: φ ◦τ = φ, where τ : C ⊗L C →C ⊗L C is the commutativity isomorphism.
(Note that we are assuming nondegeneracy in the deﬁnition but leaving this out of the terminology for the
sake of brevity.)
Similar to the case of algebraic K-theory discussed in Section 8B, for a rank r vector bundle p : V →X,
the Thom class θBO
V
∈BO2r,r(V ; p∗det−1 V ) is given by the Koszul complex Kos(p∗V ∨, s∨
can), where
the symmetric bilinear form
φV : Kos(p∗V ∨, s∨
can) ⊗Kos(p∗V ∨, s∨
can) →p∗det−1 V [r] = 3rV ∨[r]
is given by the usual exterior product
−∧−: 3iV ∨⊗3r−iV ∨→3rV ∨.
Moreover, there are isomorphisms for i < 0
BO2r−i,r(X; L) ≃Wr−i(Dperf(X), L[r], can)
where Wr−i(Dperf(X), L[r], can) is Balmer’s triangulated Witt group. In the case B = Spec k for k a ﬁeld
of characteristic different from two, Ananyevskiy [2016b, Theorem 6.5] showed that this isomorphism
induces an isomorphism of η-inverted hermitian K-theory with Witt-theory,
BO[η−1]∗,∗≃W∗[η, η−1],
where one gives η bidegree (−1, −1) and an element αηn with α ∈Wm has bidegree (m −n, −n); the
same proof works over out general base B (with assumptions as at the beginning of this subsection).
For f : Y →X a proper map of relative dimension d f in SmB and L a line bundle on X, we follow
[Calmès and Hornbostel 2011] in deﬁning a pushforward map
ˆf∗: BO2r,r(Y, ωY/B ⊗f ∗L) →BO2r−2d f ,r−d f (X, ωX/B ⊗L)
by Grothendieck–Serre duality. In [op. cit.], this is worked out for the η-inverted theory BOη when the
base is a ﬁeld; however, the same construction works for BO over the general base-scheme B and goes
as follows. For r ≥0, given an L[r]-valued symmetric bilinear form φ : C ⊗L C →ωY/B ⊗f ∗L[r], we
have the corresponding isomorphism
˜φ : C →RHom(C, ωY/B ⊗f ∗L[r]) ≃RHom(C, ωY/X ⊗f ∗(ωX/B ⊗L[r])).
Motivic Gauss–Bonnet formulas
1843
Grothendieck–Serre duality gives the isomorphism
R f∗RHom(C, ωY/X ⊗f ∗(ωX/B ⊗L[r]))
ψ
∼
−→RHom(R f∗C, ωX/B ⊗L[r −d f ]).
Composing these, we obtain the isomorphism
ψ ◦˜φ : R f∗C →RHom(R f∗C, ωX/B ⊗L[r −d f ]),
corresponding to the (nondegenerate) bilinear form
R f∗(φ) : R f∗C ⊗L R f∗C →ωX/B ⊗L[r −d f ],
which one can show is symmetric. We explicitly deﬁne the above pushforward map by setting ˆf∗(C, φ) :=
(R f∗C, R f∗(φ)).
Applying this in the situation that f = πX : X →B is a smooth and proper B-scheme of relative
dimension dX, we may obtain the formula
ˆπX∗(eBO(TX/B)) =
 dimB X
M
i, j=0
RiπX∗ j
X/B[ j −i], Tr

,
where
Tr :
 dimk X
M
i, j=0
RiπX∗ j
X/B[ j −i]

⊗
 dimk X
M
i, j=0
RiπX∗ j
X/B[ j −i]

→OB
is the symmetric bilinear form in Dperf(B) determined by the pairings
(RiπX∗ j
X/B) ⊗(RdX−iπX∗dX−j
X/B )
∪
−→RdXπX∗dX
X/B
Tr
−→OB.
Indeed, if s : X →TX/B denotes the zero-section, we have
eBO(TX/B) = s∗(Kos(TX/B), φ) =
 dX
M
j=0
 j
X/B[ j], s∗φ

with s∗φ determined by the product maps
 j
X/B[ j] ⊗dX−j
X/B [dX −j] →ωX/B[dX],
and therefore ˆπX∗(eBO(TX/B)) is Ldimk X
i, j=0 RiπX∗ j
X/B[ j −i] with the symmetric bilinear form Tr as
described above.
Passing to the η-inverted theory BOη, our comparison Theorem 7.1 gives
q ◦ˆπX∗= q ◦πX∗
as maps BO2dX,dX
η
(X, ωX/B) →BOη(B). We check that the conditions of the comparison theorem
hold just as we did for algebraic K-theory. Firstly, as mentioned above, the SL-orientation for BO
deﬁned by Panin-Walter can be described as follows: the Thom class for an oriented vector bundle
1844
Marc Levine and Arpon Raksit
(p : V →X, ρ : OX −→
∼
det V ) is given by the Koszul complex Kos(p∗V ∨, s∨
can) equipped with the
symmetric bilinear form φV deﬁned by the product in the exterior algebra followed by the isomorphism
p∗ρ∨: p∗det−1 V →OV . On the other hand, the Calmès-Hornbostel pushforward for the zero-section
s : X →V of a rank r vector bundle p : V →X with isomorphism ρ : OX −→
∼
det V is as described
above, sending a symmetric bilinear form ψ : C ⊗L C →ωX/B ⊗s∗L[n] to the symmetric bilinear form
Rs∗(ψ) : Rs∗C ⊗L Rs∗C →ωV/B ⊗L[n +r].
Since s is ﬁnite, Rs∗C ≃C, which in Dperf(V ) is canonically isomorphic to p∗C ⊗OV Kos(p∗V ∨, s∨
can).
We may thus view Rs∗(ψ) instead as a map
[p∗C ⊗OV Kos(p∗V ∨, s∨
can)] ⊗L [p∗C ⊗OV Kos(p∗V ∨, s∨
can)] →ωV/B ⊗L[n +r];
tracing through its deﬁnition, one ﬁnds that this map is given by the composition
[p∗C ⊗OV Kos(p∗V ∨, s∨
can)] ⊗L [p∗C ⊗OV Kos(p∗V ∨, s∨
can)]
−→
∼
[p∗C ⊗L p∗C] ⊗[Kos(p∗V ∨, s∨
can) ⊗Kos(p∗V ∨, s∨
can)]
p∗ψ⊗φV
−−−−→ωX/B ⊗L[n] ⊗p∗det−1 V [r] −→
∼
ωV/B ⊗L[n +r].
As this is exactly p∗(C, φ) ⊗thV,ρ, we see that the Calmès-Hornbostel pushforward for s is the same as
that deﬁned by the Panin-Walter SL-orientation on BOη, which veriﬁes the hypothesis in our Theorem 7.1.
Having veriﬁed this, we can prove our main result.
Theorem 8.6. Let B be a regular noetherian separated scheme of ﬁnite Krull dimension with 2 invertible
in 0(B, OB). Let X be a smooth projective B-scheme. Then:
(1) We have
uBOη(χ(X/B)) =
 dimk X
M
i, j=0
RiπX∗ j
X/B[ j −i], Tr

in BO0,0
η (B) ≃W(Dperf(B)) ≃W(B).
(2) Let f : GW(B) →K0(B) denote the forgetful map discarding the symmetric bilinear form. Suppose
that the map
( f, q) : GW(B) →K0(B) × W(B)
is injective (this is the case if for example B is the spectrum of a local ring). Then
uBO(χ(X/B)) =
 dimB X
M
i, j=0
Hi(X,  j
X/B)[ j −i], Tr

in GW(Dperf(B)) ≃GW(B).
Motivic Gauss–Bonnet formulas
1845
(3) Suppose B is in Smk for k a perfect ﬁeld. Then the image
^
χ(X/B) of χ(X/B) in π0,0(1B)(B) ≃
H0(B, GW) is given by
^
χ(X/B) =
 dimB X
M
i, j=0
RiπX∗ j
X/B[ j −i], Tr

∈H0(B, GW).
In particular, if B = Spec k, then
χ(X/k) =
 dimB X
M
i, j=0
Hi(X,  j
X/k)[ j −i], Tr

∈GW(k).
Proof. The ﬁrst statement follows from our comparison Theorem 7.1, as detailed above, together with the
motivic Gauss–Bonnet Theorem 5.3. Statement (2) follows from (1) and our result for algebraic K-theory,
Theorem 8.3. Finally, (3) follows from (2), after we check that the unit map uBO induces the identity map
on GW(k) via
GW(k)
(Morel)
∼
−−−→10,0
k (Spec k) uBO
∼
−→BO0,0(Spec k) ≃KO[0]
0 (k) = GW(k),
where the ﬁrst isomorphism arises from Morel’s theorem [2004, Theorem 6.4.1, Remark 6.4.2; 2012,
Theorem 6.40] identifying 10,0
k (Spec k) with GW(k). The one-dimensional forms ⟨λ⟩∈GW(k), λ ∈k×,
generate GW(k), and via Morel’s isomorphism ⟨λ⟩maps to the automorphism of 1k induced by the
automorphism φλ : P1
k →P1
k, φλ((x0 : x1)) = (x0 : λ · x1). By [Ananyevskiy 2016b, Corollary 6.2],
the image of φλ under the unit map uBO is also ⟨λ⟩, after the canonical identiﬁcation BO0,0(Spec k) ≃
KO[0]
0 (k) ≃GW(k).
□
Corollary 8.7. Let k be a perfect ﬁeld of characteristic different from two. Let H ∈GW(k) denote the
class of the hyperbolic form x2 −y2. Let X be a smooth and projective k-scheme.
(1) Suppose X has odd dimension 2n −1. Let
m :=
X
i+ j<2n−1
(−1)i+ j dimk Hi(X,  j
X/k) −
X
0≤i< j
i+ j=2n−1
dimk Hi(X,  j
X/k).
Then χ(X/k) = m · H ∈GW(k).
(2) Assume X has even dimension 2n. Let
m :=
X
i+ j<2n
(−1)i+ j dimk Hi(X,  j
X/k) +
X
0≤i< j
i+ j=2n
dimk Hi(X,  j
X/k)
and let Q be the symmetric bilinear form
Hn(X, n
X/k) × Hn(X, n
X/k)
∪
−→H2n(X, 2n
X/k)
Tr
−→k.
Then χ(X/k) = m · H + Q ∈GW(k).
1846
Marc Levine and Arpon Raksit
Proof. For V a ﬁnite-dimensional k-vector space and n ∈Z, we have the symmetric bilinear form in Dperf(k)
hn : (V [n] ⊕V ∨[−n]) ⊗(V [n] ⊕V ∨[−n]) →k
whose restriction to V [n] ⊗V ∨[−n] is the canonical pairing of V [n] with V ∨[−n] ≃V [n]∨, and (−1)n
times this pairing on V ∨[−n] ⊗V [n]. The corresponding class of hn in GW(k) is (−1)n times the
class of h0, as (V [n] ⊕V ∨[−n], hn) is the image of the class of V [n] in K0(k) under the hyperbolic
map H : K0(−) →KO[0]
0 (−) (see, e.g., [Walter 2003, Theorem 2.6]), and [V [n]] = (−1)n[V [0]] in
K0(Dperf(k)) ≃K0(k).
With this in mind, we may deduce the claim from the formula
χ(X/k) =
 dimB X
M
i, j=0
Hi(X,  j
X/k)[ j −i], Tr

of Theorem 8.6. Indeed, in the case dim X = 2n −1, the symmetric bilinear form Tr is the sum of the
“hyperbolic” forms as above on
Hi(X,  j
X/k)[ j −i] ⊕H2n−1−i(X, 2n−1−j
X/k
)[i −j]
for i + j < 2n −1, or 0 ≤i < j and i + j = 2n −1; and the argument in the even-dimensional case is the
same, except that one has the remaining factor coming from the symmetric pairing on Hn(X, n
X/k). □
The next result was obtained independently by Abelson [1976, Theorem 1] and Kharlamov [1974,
Theorem A] using an argument of Milnor’s relying on the Lefschetz ﬁxed point theorem.
Corollary 8.8. Let k be a ﬁeld equipped with an embedding σ : k ,→R. Let X be a smooth projective
k-scheme of even dimension 2n. Then
|χtop(X(R))| ≤dimk Hn(X, n
X/k).
Proof.
We know that χtop(X(R)) is the signature of σ∗(χ(X/k)) ∈GW(R); see [Levine 2017b,
Remarks 1.11]. The description of χ(X/k) given by Corollary 8.7 gives the desired inequality
|sig σ∗(χ(X/k))| ≤dimk Hn(X, X/k).
□
Remark 8.9. Let k be a perfect ﬁeld of characteristic different from two. The formula for the Euler
characteristic given in Theorem 8.6 shows that the invariant χ(X/k) is “motivic” in the following sense.
Let X and Y be smooth projective k-schemes of respective even dimensions 2n and 2m and let α : X 99K Y
be a correspondence with k-coefﬁcients of degree n, that is, an element α ∈CHm+n(X × Y)k. The
correspondence α induces the map of k-vector spaces α∗: Hm(Y, m
Y/k) →Hn(X, n
X/k). Suppose that α∗
is an isomorphism and is compatible with the trace pairings on Hm(Y, m
Y/k) and Hn(X, n
X/k) appearing
in Corollary 8.7. Then χ(X/k) = χ(Y/k) in the Witt ring W(k).
Motivic Gauss–Bonnet formulas
1847
For instance, supposing k has characteristic zero, if the motives of X and Y (for homological equivalence
with respect to de Rham cohomology) have a Künneth decomposition
h(X) ≃
2n
M
i=0
hi(X)⟨i⟩,
h(Y) ≃
2m
M
i=0
hi(Y)⟨i⟩
and α induces an isomorphism α∗: hm(Y)⟨m⟩→hn(X)⟨n⟩, compatible with the respective intersection
products
hm(Y)⟨m⟩⊗hm(Y)⟨m⟩→h2m(Y)⟨2m⟩πY∗
−→h0(k) ≃Q,
hn(X)⟨n⟩⊗hn(X)⟨n⟩→h2n(X)⟨2n⟩πX∗
−→h0(k) ≃Q,
then χ(Y/k) = χ(X/k) in W(k).
Presumably, merely having an isomorphism of motives hn(X)⟨n⟩≃hm(Y)⟨m⟩would not sufﬁce to
yield χ(Y/k) = χ(X/k) in W(k), but we do not have an example.
8E. Descent for the motivic Euler characteristic. Let k be a perfect ﬁeld of characteristic different from
two. With the explicit formula for χ(X/k) given by Theorem 8.6, we may ﬁnd χ(X/k) for forms X
of some k-scheme X0 by the usual twisting construction; this works for all manners of descent but we
conﬁne ourselves to the case of Galois descent here.
Let X0, X be smooth projective k-schemes of even dimension 2n. Let K be a ﬁnite Galois extension
ﬁeld of k with Galois group G. Let X K := X ×k K, X0K := X0×k K, and suppose we have an isomorphism
φ : X×k K →X0×k K. This gives us the cocycle {ψσ ∈AutK(X0×k K)}σ∈G, where ψσ :=φσ ◦φ−1. Letting
b0 : Hn(X0, n
X0/k) × Hn(X0, n
X0/k) →k,
b : Hn(X, n
X/k) × Hn(X, n
X/k) →k
denote the respective symmetric bilinear forms Tr(x ∪y), the isomorphism φ induces an isometry
φ∗: (Hn(X0K, n
X0K /K), b0K) →(Hn(X K, n
X K /K), bK),
and the cocycle {ψσ}σ∈G determines a cocycle {(ψ∗
σ)−1 ∈O(b0)(K)}σ∈G. Twisting by the latter cocycle
allows one to recovers b from b0; explicitly, this works as follows.
Firstly, as usual, one recovers the k-vector space Hn(X,n
X/k) from the K-vector space Hn(X0K,n
X0K /K)
as the G-invariants for the map x 7→ψ∗−1
σ
(xσ). Secondly, letting A ∈GL(Hn(X0K, n
X0K /K)) be a
change of basis matrix comparing the k-forms Hn(X0, n
X0/k) ⊂Hn(X0K, n
X0K /K) and Hn(X, n
X/k) ⊂
Hn(X0K, n
X0K /K), we recover b (up to k-isometry) as
b(x, y) = b0(Ax, Ay) =: bA
0 (x, y).
Having performed this twist at the level of symmetric bilinear forms, we may now pass Grothendieck–
Witt classes to describe the Euler characteristic of X: namely, Corollary 8.7(2) gives
χ(X0/k) = [b0 + m · H],
χ(X/k) = [bA
0 + m · H]
in GW(k).
1848
Marc Levine and Arpon Raksit
Remark 8.10. In the case of a smooth projective surface S with pg(S) = 0, over a characteristic zero
ﬁeld k, the twisting construction reduces to a computation involving CH1(S¯k)/∼num as a Gal(k)-module;
here ¯k is the algebraic closure of k and ∼num is numerical equivalence. Indeed, the assumption pg(S) = 0
implies that the cycle class map in Hodge cohomology
cycHdg : CH1(S¯k) →H1(S¯k, 1
S/¯k)
induces an isomorphism
CH1(S¯k)/∼num ⊗Z ¯k −→
∼
H1(S¯k, 1
S/¯k) ≃H1(S, 1
S/k) ⊗k ¯k
and the cycle class map cycHdg transforms the intersection product on CH1(S¯k)/∼num to the quadratic
form b0 on H1(S¯k, 1
S/¯k), induced by cup product and the trace map. Thus, our quadratic form b on
H1(S, 1
S/k) is equivalent to the one gotten by twisting the ¯k-linear extension of the intersection product
on CH1(S¯k)/∼num by the natural Galois action.
Analogous comments hold for a “geometrically singular” variety, by which we mean a smooth projective
k-scheme X of dimension 2n such that Hn(X ¯k, n
X ¯k/¯k) is spanned by cycle classes, where we replace
CH1/∼num with CHn/∼num. For example, one could take a K3 surface with Picard rank 20 over ¯k or a
cubic fourfold X with H2(X ¯k, 2
X ¯k/k) ≃¯k21 spanned by algebraic cycles.
Examples 8.11. (1) As a simple example, take S to be a quadric surface in P3
k deﬁned by a degree two
homogeneous form q(X0, . . . , X3); we may assume that q is a diagonal form,
q(X0, . . . , X3) = a0X2
0 +
3
X
i=1
ai X2
i
= a0(X0 +
p
−a1/a0X1)(X0 −√−a1X1) + a2(X2 −
p
−a3/a2X3)(X2 +
p
−a3/a2X3).
This trivializes CH1(S) over K := k(√−a0a1, √−a2a3), namely CH1(S) = Zℓ1 ⊕Zℓ2 with ℓ1
deﬁned by (X0 −√−a1X1) = (X2 −√−a3/a2X3) = 0 and with ℓ2 deﬁned by (X0 −√−a1X1) =
(X2 + √−a3/a2X3) = 0. Embedding Gal(K/k) ⊂Gal(k(√−a0a1)/k) × Gal(k(√−a2a3)/k) =
⟨σ1⟩×⟨σ2⟩, the Galois action is given by σ1(ℓ1, ℓ2) = σ2(ℓ1, ℓ2) = (ℓ2, ℓ1). A Galois-invariant basis
is thus given by ((ℓ1 + ℓ2), √a0a1a2a3(ℓ1 −ℓ2)), and the intersection form in this basis has matrix
2
0
0 −2a0a1a2a3

.
In other words, χ(S/k) = ⟨2⟩+ ⟨−2a0a1a2a3⟩.
(2) Suppose S is the blowup of P2
k along a 0-dimensional closed subscheme Z ⊂P2
k, with Z étale over
k. Let ℓdenote the class of a line in CH1(P2). Writing Z ¯k = {p1, . . . , pr}, we have CH1(S¯k) ≃
Z · ℓ⊕
 Lr
i=1 Z · pr

, with the evident Galois action and with intersection form the diagonal matrix
(1, −1, . . . , −1). It is then easy to show that the twisted quadratic form χ(S/k) is ⟨1⟩−TrZ/k(⟨1⟩).
Motivic Gauss–Bonnet formulas
1849
These last two examples have been computed by different methods before: (1) is a special case of
[Levine 2017b, Corollary 13.2] and (2) is a special case of [Levine 2017b, Proposition 1.10]. Here is a
more interesting example.
Example 8.12. Let π : S →C be a conic bundle over a smooth projective curve C, all deﬁned over k;
we assume for simplicity that k ⊂C. Let Z ⊂C be the degeneracy locus of π: that is, Z is the reduced
proper closed subscheme of C over which π is not smooth. For each geometric point z of Z, the ﬁber
π−1(z) is isomorphic to two distinct lines in P2: π−1(z) = ℓz ∪ℓ′
z. There is a “double section” D ⊂S
with D →C a ﬁnite degree two morphism, and with D · ℓz = 1 = D · ℓ′
z for all z ∈Z(¯k).
Over ¯k, the bundle S is isomorphic to the blow-up of a P1-bundle S ¯k →C ¯k along a ﬁnite set Z′ ⊂S ¯k
with Z′ −→
∼
Z ¯k via π.
Suppose Z ¯k = {z1, . . . zr}. If we ﬁx a closed point c0 ∈C \ Z of degree d over k, we have the following
basis for CH1(S¯k)Q/∼num:
ℓz1 −ℓ′
z1, . . . , ℓzr −ℓ′
zr, D, π−1(c0).
We have the ﬁnite degree two extension p : ˜Z →Z, where for each z ∈Z, p−1(z) corresponds to the pair
of lines ℓz, ℓ′
z. Let L := k({z1, . . . , zr}) ⊃k and let G := Aut(L/k). Writing k( ˜Z) = k(Z)(
√
δ) for some
δ ∈O×
Z , we have a basis of CH1(SL)Q/∼num given by
v1, . . . , vr, D, π−1(c0),
with vi :=
√
d(ℓzi −ℓ′
zi). The intersection form on ⟨v1, . . . , vr⟩is the diagonal matrix
(−4δ(z1), . . . , −4δ(zr)),
the subspaces ⟨v1, . . . , vr⟩and ⟨D, π−1(c0)⟩are perpendicular and ⟨D, π−1(c0)⟩is hyperbolic. Moreover,
the automorphism group Aut(L/k) acts on ⟨v1, . . . , vr⟩just as it does on ⟨z1, . . . , zr⟩. From this it follows
that the twisted intersection form b is given by
b = H −Trk(Z)/k(⟨δ⟩),
and hence
χ(S/k) = m · H −Trk(Z)/k(⟨δ⟩)
with
m = 2 −dimk H0(S, 1
S/k) −dimk H1(S, OX) = dimQ H0(San, Q) −dimQ H1(San, Q) + 1,
where San is the complex manifold associated to SC.
As a particular example, we may take S to be a cubic surface V ⊂P3
k with a line ℓ. Projection from ℓ
realizes V as a conic bundle π : V →P1
k, with degeneracy locus Z ⊂P1
k a reduced closed subscheme of
degree 5 over k. The above implies that the symmetric bilinear form bV is given by
bV = H −TrZ/k(⟨δ⟩)
and computes χ(S/k) = 2H −TrZ/k(⟨δ⟩).
1850
Marc Levine and Arpon Raksit
Remark 8.13. Bayer-Fluckiger and Serre [2019] considered the ﬁnite k-scheme W representing the 27
lines on a cubic surface V and computed the trace form TrW/k(⟨1⟩) in [Bayer-Fluckiger and Serre 2019,
Theorem 5, Interpretation 7.3]. They identiﬁed their form q6,V with the trace form on H1(V, V/k) and
showed that
TrW/k(⟨1⟩) = λ2bV + (⟨−1⟩−⟨2⟩)bV + 7 −⟨−2⟩.
