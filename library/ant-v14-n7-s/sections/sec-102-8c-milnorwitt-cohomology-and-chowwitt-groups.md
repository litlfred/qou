---
doc_id: ant-v14-n7-s
doc_title: "Algebra & Number Theory Volume 14 No. 7 msp"
section_id: sec-102-8c-milnorwitt-cohomology-and-chowwitt-groups
section_title: "8C. Milnor–Witt cohomology and Chow–Witt groups"
section_number: null
pages: 173-175
source_pdf: ant-v14-n7-s.pdf
source_sha256: ab695eddd565addf
---
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
0 (X;ωX/k)= Hd(X, KMW
d (ωX/k))→ H0,0
0 (Spec k)= GW(k).
See also [Hoyois 2014, Lemma 5.10], which identiﬁes this map with one induced by the Scharlau trace.
The methods of this paper give a new proof of the result given in [Levine 2017b, Lemma 1.5]:
Theorem 8.4. Let k be a perfect ﬁeld of characteristic different from two. ForπX: X→ Spec k smooth
and projective over k, we have
χ( X/k)=~degk(eH0(1k)(TX/k)).
Motivic Gauss–Bonnet formulas 1841
Proof. Under Morel’s isomorphismEndSH(k)(1X)≃ GW(k) [2004, Theorem 6.4.1, Remark 6.4.2; 2012,
Theorem 6.40] and the isomorphism H0(Spec k, KMW
0 )≃ GW(k), the unit map uH0(1k): 1k→ H0(1k)
induces the identity map on π0,0. Using this, the proof of the claim is essentially the same as the other
Gauss–Bonnet theorems we have discussed, but with a bit of extra work since we are no longer in the
GL-oriented case.
Fasel [2008] has deﬁned pushforward maps
ˆf∗: Ha
W(X, KMW
b (ωX/k⊗ f∗L))→ Ha−d
Z (Y, KMW
b−d(L))
for each projective morphism f: X→ Y in Smk of relative dimension d, line bundle L→ Y, and closed
subsets Z⊆ Y, W⊆ X with f(W)⊆ Z. In the case of the structure mapπX: X→ Spec k, the pushforward
~πX∗: Hd(X, KMW
d (ωX/k))→ H0(Spec k, KMW
0 )= GW(k) is the map~degk.
For s: X→ V the zero-section of a vector bundle,ˆs∗ is the Thom isomorphism s∗. Thus, if we pass
to theη-inverted theory, H0(1X)η:= H0(1k)[η−1], our comparison Theorem 7.1 says that ˆfη∗= fη∗ for
all projective morphisms f in Smk. We have KMW
∗ [η−1]≃ W, the sheaf of Witt rings, and the map
KMW
0 = GW→ KMW
∗ [η−1]≃ W is the canonical map q: GW→ W realizing W as the quotient of GW
by the subgroup generated by the hyperbolic form. Thus, applying our motivic Gauss–Bonnet theorem
gives the identity
q(χ( X/k))= q(~degk(eH0(1k)(TX/k))) in W(k).
To lift this to an equality in GW(k) and thereby complete the proof, we use that the map
(rnk, q): GW→ Z× W
is injective, together with the fact that we can recover the rank by applying H0 to the unit map 1k→ HZ
and using Theorem 8.2. □
