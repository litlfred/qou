---
doc_id: ant-v14-n7-s
doc_title: "Algebra & Number Theory Volume 14 No. 7 msp"
section_id: sec-100-8a-motivic-cohomology-and-cohomology-of-the-miln
section_title: "8A. Motivic cohomology and cohomology of the Milnor K-theory sheaves"
section_number: null
pages: 170-171
source_pdf: ant-v14-n7-s.pdf
source_sha256: ab695eddd565addf
---
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
