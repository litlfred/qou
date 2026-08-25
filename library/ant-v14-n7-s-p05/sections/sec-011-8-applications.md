---
doc_id: ant-v14-n7-s-p05
doc_title: "Motivic Gauss–Bonnet formulas"
section_id: sec-011-8-applications
section_title: "Applications"
section_number: 8
pages: 36-40
source_pdf: ant-v14-n7-s-p05.pdf
source_sha256: 1c8e94ff62a8d920
doc_brief: "Motivic Gauss–Bonnet formulas — 18 sections: Duality and Euler characteristics; TX/B(1X×B X); TX/B(p∗"
---
In this section, we apply the motivic Gauss–Bonnet formula of Section 5 and the comparison results of
Section 7 to various speciﬁc SL-oriented cohomology theories, and thereby make computations of the
motivic Euler characteristicχ( X/B) in different contexts.
8A. Motivic cohomology and cohomology of the Milnor K-theory sheaves. We work over the base-
scheme B= Spec k, with k a perfect ﬁeld. In SH(k) we have the motivic cohomology spectrum HZ
representing V oevodsky’s motivic cohomology (see, e.g., [Levine 2008, §6.2] for a construction valid in
arbitrary characteristic). By [V oevodsky 2002], there is a natural isomorphism
HZa,b(X)≃ CHb(X, 2b− a)
for X∈ SmB, where CHb(X, 2b− a) is Bloch’s higher Chow group [1986].
HZ admits a localization sequence: for i: Z→ X a closed immersion of codimension d in Smk, there
is a canonical isomorphism
HZa,b
Z (X)≃ HZa−2d,b−d(Z).
See for example [Bloch 1994]. In particular, for p: V→ X a rank r vector bundle over X∈ Smk, we
have the isomorphism
HZ2r,r
0V (V)≃ HZ0,0(X)
which gives us Thom classesϑHZ
V ∈ HZ2r,r
0V (V) corresponding to the unit 1HZ
X ∈ HZ0,0(X). Thus HZ is a
GL-oriented motivic spectrum.
Let X be a smooth projective k-scheme of dimension n over k. For a class x∈ HZ2n,n(X), the
isomorphism HZ2n,n(X)≃ CHn(X, 0)= CHn(X) allows one to represent x as the class of a 0-cycle
˜x=∑
i ni pi, with the pi closed points of X. One has the degree degk(pi):=[ k(pi): k] and extending by
linearity gives the degree degk(˜x), which one shows passes to rational equivalence to deﬁne a degree map
degk: HZ2n,n(X)→ CH0(Spec k)= Z.
As a GL-oriented theory, HZ has Chern classes for vector bundles: cr(V)∈ HZ2r,r(X) for V→ X a
vector bundle over some X∈ Smk and r≥ 0.
Theorem 8.1. Let X∈ Smk be projective of dimension dX. Then
uHZ(χ( X/k))= degk(cdX(TX/k)).
Proof. One has well-deﬁned pushforward maps on CH∗(−,∗) for projective morphisms (see, e.g., [Bloch
1986, Proposition 1.3]). Via the isomorphism HZa,b(X)≃ CHb(X, 2b− a) [V oevodsky 2002], this
gives pushforward maps ˆf∗ on HZ∗,∗ for f: Y→ X a projective morphism in SmB (see [Bloch 1986]
for details), making (X, Z)↦→ HZ∗,∗
Z (X) a GL-oriented cohomology theory on Smk. In addition, for
πX: X→ Spec k in Smk projective of dimension n, the map ˆπX∗: HZ2n,n(X)→ CH0(Spec k)= Z is
degk, and for i: Y→ X a closed immersion, the map ˆi∗ is given by the localization theorem, which
Motivic Gauss–Bonnet formulas 1837
readily implies thatˆi∗= i∗. By our comparison Theorem 7.1, which here really reduces to the theorem of
Panin and Smirnov, it follows that ˆf∗= f∗ for all projective f.
Finally, one has cdX= s∗s∗(1HZ
X )= eHZ(V) [Fulton 1984, Corollary 6.3], so applying the motivic
Gauss–Bonnet Theorem 5.3 gives the statement. □
One can obtain the same result by using the cohomology of the Milnor K-theory sheaves as a bigraded
cohomology theory. The homotopy t-structure on SH(k) has heart the abelian category of homotopy
modules5*(k) (see [Morel 2004, §5.2; 2012] for details); we let H0: SH(k)→5*(k) be the associated
functor. The fact that HZn,n(Spec F)≃ KM
n(F) for F a ﬁeld [Nesterenko and Suslin 1989; Totaro 1992]
says that H0HZ is canonically isomorphic to the homotopy module(KM
n)n, which is in fact a cycle module
in the sense of Rost [1996]. This gives us the isomorphism
H0HZa,b(X)≃ Ha(X, KM
b).
The isomorphism H n(X, KM
n)≃ CHn(X) (a special case of Rost’s formula [1996, Corollary 6.5] for the
Chow groups of a cycle module) gives us as above Thom classes ϑKM
∗(V)∈ H0HZ2r,r
0V (V), giving H0HZ
a GL-orientation. As for HZ∗,∗, one has explicitly deﬁned pushforward maps on H∗(−, KM
∗ ) which give
H0HZ∗,∗ the structure of a GL-oriented cohomology theory on Smk and for which the pushforward map
for the zero-section of a vector bundle is given by the Thom isomorphism. Since the pushforward on
Hn(X, KM
n) agrees with the classical pushforward on CHn, we deduce the following using the same proof
as for Theorem 8.1.
Theorem 8.2. Let X∈ Smk be projective of dimension dX. Then
uH0HZ(χ( X/k))= degk(cdX(TX/k)) in CH0(Spec k)= Z.
8B. Algebraic K-theory. We now let B be any regular separated base-scheme of ﬁnite Krull dimension.
Algebraic K-theory on SmB is represented by the motivic commutative ring spectrum KGL∈ SH(B); see
[V oevodsky 1998, §6.2]. Just as for HZ, the purity theorem
KGLa,b
Z (X)≃ KGLa−2c,b−c(Z)
for i: Z→ X a closed immersion of codimension d in SmB (a consequence of Quillen’s localization
sequence for algebraic K-theory [1973, §7, Proposition 3.2]) gives Thom class ϑKGL(V)∈ KGL2r,r
0V (V)
for V→ X a rank r vector bundle over X∈ SmB, and makes KGL a GL-oriented motivic spectrum.
Explicitly, KGL represents Quillen K-theory on SmB via KGLa,b≃ K2b−a and the Thom class for a
rank r vector bundle p: V→ X is represented by the Koszul complex KosV(p∗V∨, can). Here
can: p∗V∨→ OV
is the dual of the tautological section OV→ p∗V and KosV(p∗V∨, can) is the complex whose terms are
given by
KosV(p∗V∨, can)−r=3r p∗V∨
1838 Marc Levine and Arpon Raksit
and whose differential3r p∗V∨→3r−1 p∗V∨ is given with respect to a local framing of V∨ by
d(ei1∧···∧ eir)=
r∑
j=1
(−1) j−1can(ei j)· ei1∧···∧ ˆei j∧···∧ eir.
This complex is a locally free resolution ofs∗(OX), where s: X→ V is the zero-section. Thus, by the identi-
ﬁcation of KGL2r,r
0V (V) with the Grothendieck group of the triangulated category of perfect complexes onV
with support contained in 0V , KosV(p∗V∨, can) gives rise to a class[KosV(p∗V∨, can)]∈ KGL2r,r
0V (V)
which maps to 1X under the purity isomorphism KGL2r,r
0V (V)≃ KGL0,0(X), so that we indeed have
[KosV(p∗V∨, can)]= ϑKGL(V).
Just as for motivic cohomology, one has explicit pushforward maps in K-theory given by Quillen’s
localization and devissage theorems identifying, forX∈ SmB and Z⊆ X a closed subscheme, the K-theory
with support KZ(X) with the K-theory of the abelian category of coherent sheaves CohZ on Z, denoted
G(Z). For a projective morphism f: Y→ X, one has the pushforward map ˆf∗: G(Y)→ G(X) deﬁned
by using a suitable subcategory of Coh Y on which f∗ is exact. On K 0, this recovers the usual formula
ˆf∗([F])=
dim Y∑
j=0
(−1) j[R j f∗(F)]
for F∈ CohY . Via the isomorphisms KGLa,b
Z (X)≃ G2b−a(Z), this gives pushforward maps ˆf∗ for
KGL∗,∗, deﬁning a GL-oriented cohomology theory on Sm B.
For s: X→ V the zero-section of a vector bundle,ˆs∗ agrees with the pushforward s∗ using the Thom
isomorphism/localization theorem, hence by our comparison theorem (again really the theorem of Panin
and Smirnov), we have ˆf∗= f∗ for all projective f.
Theorem 8.3. LetπX: X→ B be a smooth projective morphism with B a regular separated scheme of
ﬁnite Krull dimension. Then
uKGL(χ( X/B))=
dimB X∑
j=0
dimB X∑
i=0
(−1)i+ j[R jπX∗i
X/B]∈ K0(B)= KGL0,0(B).
Proof. Let p: TX/B→ X denote the relative tangent bundle and let s: X→ TX/B denote the zero-section.
We have
eKGL(TX/B)= s∗(th(TX/B))= s∗(KosTX/B(p∗T∨
X/B, can)).
Since T∨
X/B=X/B, and s∗(can) is the zero-map, it follows that, in K 0(X),
s∗(KosTX/B(p∗T∨
X/B, can))=
dimB X∑
i=0
(−1)i[i
X/B],
and thus
πX∗(eKGL(TX/B))=
dimB X∑
j=0
dimB X∑
i=0
(−1)i+ j[R jπX∗i
X/B].
Motivic Gauss–Bonnet formulas 1839
We conclude by applying the motivic Gauss–Bonnet theorem. □
8C. Milnor–Witt cohomology and Chow–Witt groups. In this case, we again work over a perfect base-
ﬁeld k. The Milnor–Witt sheaves KMW
∗ constructed by Morel [2004, §6; 2012, Chapter 3] give rise to an
SL-oriented theory as follows. Morel describes an isomorphism of KMW
0 with the sheaﬁﬁcation GW of
the Grothendieck–Witt rings;1 the map of sheaves of abelian groups Gm→ GW× sending a unit u to the
one-dimensional form⟨u⟩ allows one to deﬁne, for L→ X a line bundle, a twisted version
KMW
∗ (L):= KMW
∗ ×Gm L×
as a Nisnevich sheaf on X∈ Smk (see [Morel 2012, p. 118] or [Calmès and Fasel 2014, §1.2]). One may
use the Rost–Schmid complex for KMW
∗ (L) [Morel 2012, Chapter 5] to compute H∗
Z(X, KMW
∗ (L)) for
Z⊆ X a closed subset, which gives a purity theorem: for i: Z→ X a codimension d closed immersion
in Smk and L→ X a line bundle, there is a canonical isomorphism
H∗
Z(X, KMW
∗ (L))≃ H∗−d(Z, KMW
∗−d(i∗L⊗ det Ni)), (8.3.1)
where Ni→ Z is the normal bundle of i. Applying this to the zero-section of a rank r vector bundle
p: V→ X gives the isomorphism
H0(X, GW)≃ Hr
0V(V, KMW
r (p∗ det−1 V)); (8.3.2)
in particular, given an isomorphismφ: det V→ OX, we obtain a Thom class
θV,φ∈ Hr
0V(V, KMW
r )
corresponding to the unit section 1 X∈ H0(X, GW).
On the other hand, Morel’s computation [2004, Theorem 6.4.1, Remark 6.4.2; 2012, Theorem 6.40] of
the zeroth graded homotopy sheaf of the sphere spectrum gives an identiﬁcation
H0(1k)≃(KMW
n )n∈Z
in5*(k), which then gives the natural isomorphism
H0(1k)a+b,b
Z (X)≃ Ha
Z(X, KMW
b ).
This is moreover compatible with twisting by a line bundle p: L→ X, on the H0(1k) side using the
Thom space construction
H0(1k)∗,∗
Z (X; L):= H0(1k)∗+2,∗+1
Z (L)
1Morel [2012, Lemma 3.10] deﬁned an isomorphism GW(F)→ KMW(F), F a ﬁeld. Morel [2012, §3.2] deﬁned KMW∗ as
an unramiﬁed sheaf and it follows from [Ojanguren and Panin 1999, Theorem A] that GW is an unramiﬁed sheaf. From this it is
not difﬁcult to show that the isomorphism GW(F)→ KMW(F) for ﬁelds extends to an isomorphism of sheaves.
1840 Marc Levine and Arpon Raksit
and on the Milnor–Witt cohomology side using the twisted Milnor–Witt sheaves. To see this, note that
the “untwisted” isomorphism gives us an isomorphism
H0(1k)a+b+2,b+1
Z (Th(L))≃ H0(1k)a+b+2,b+1
0L∩p−1(Z)(L)≃ Ha+1
0L∩p−1(Z)(X, KMW
b+1),
so it sufﬁces to identify the right-hand side withHa
Z(X, KMW
b (L)). For Y∈Smk and line bundle M→Y, the
Rost–Schmid complex for KMW
m (M) consists in degree a of sums of terms of twisted Milnor–Witt groups
of the form KMW
m−a(k(y);3a(my/m2
y)∨⊗ M), for y a codimension a point of Y and my⊂ OY,y the maximal
ideal. To compute cohomology with supports inW⊆ Y, one restricts to those y∈ W. If we now take Y= L
and M the trivial bundle, with supports in p−1(Z)∩ 0L and m= b+ 1, and compare with Y= X, with
supports in Z with m= b, the term for y∈ Z, of codimension a+1 on L is KMW
b−a(k(y);3a(my/m2
y)∨⊗ L)
while the term for y∈ Z, of codimension a on X is KMW
b−a(k(y);3a(my/m2
y)∨), where my is the maximal
ideal in OX,y in both cases. This gives the desired identiﬁcation
Ha+1
0L∩p−1(Z)(X, KMW
b+1)≃ Ha
Z(X, KMW
b (L)).
The purity isomorphism (8.3.1) is a special case of this construction.
The Thom classθV,φ∈ Hr
0V(V, KMW
r ) gives the Thom class
θV,φ∈ H0(1k)2r,r
0V (V),
making H0(1k) an SL-oriented theory; see, e.g, [Levine 2017b, §3.2]. The resulting canonical Thom class
thV∈ H0(1k)2r,r
0V (V; det−1 V)= Hr
0V(V, KMW
r (det−1 V))
agrees with the image of 1 X∈ H0(X, GW) under the Rost–Schmid isomorphism (8.3.2).
Let πX: X→ Spec k be smooth and projective over k of dimension d. Using the Rost–Schmid
complex for the twisted homotopy module one has generators for Hd(X, KMW
d (ωX/k)) as formal sums
˜x=∑
iαi· pi, withαi∈ GW(k(pi)) and pi∈ X closed points. Since k is perfect, the ﬁnite extension
k(pi)/k is separable and one can deﬁne
~degk(˜x):=
∑
i
Trk(pi)/kαi∈ GW(k)
where Trk(pi)/k: GW(k(pi))→ GW(k) is the transfer induced by the usual trace mapTrk(pi)/k: k(pi)→ k;
see, for example, [Calmès and Fasel 2014, Lemma 2.3]. It is shown in [Calmès and Fasel 2014, §3] that
this descends to a map
~degk: H2d,d
