---
doc_id: arxiv-math-0006057v2
doc_title: "FINITE QUANTUM GROUPOIDS AND THEIR APPLICA TIONS"
section_id: sec-026-20-dmitri-nikshych-and-leonid-v-ainerman
section_title: "DMITRI NIKSHYCH AND LEONID V AINERMAN"
section_number: 20
pages: 20-21
source_pdf: 0006057v2.pdf
source_sha256: c881434fe9f4b04f
doc_brief: "FINITE QUANTUM GROUPOIDS AND THEIR APPLICA TIONS — W e give a survey of the theory of ﬁnite quantum groupoids (wea k Hopf algebras), including foundations of the theory and app lications to ﬁnite"
---
The structure operations of ˆD(H) are obtained by dualizing those of D(H):
(
∑
k
hk ⊗φk)(
∑
l
gl ⊗ψl) =
∑
kl
hkgl ⊗φkψl,
1 ˆD(H) = 1 (2) ⊗ (ε↼ 1(1)),
∆(
∑
k
hk ⊗φk) =
∑
ijk
(hk(2) ⊗ξiφk(1)ξj ) ⊗ (S(fi)hk(1)fj ⊗φk(2)),
ε(
∑
k
hk ⊗φk) =
∑
k
ε(hk)ˆε(φk),
S(
∑
k
hk ⊗φk) =
∑
ijk
fiS−1(hk)S(fj) ⊗ξiS(φ)ξj,
for all ∑
k hk ⊗φk, ∑
l gl ⊗ψl ∈ ˆD(H), where {fi} and {ξj} are dual bases.
Corollary 5.3.4 ([NTV], 6.4) . The Drinfeld double D(H) is factorizable in the
sense of Deﬁnition 5.2.10.
Proof. One can use the explicit form of the R-matrix (40) of D(H) and the de-
scription of the dual ˆD(H) to check that in this case the map F from (33) is
surjective.
5.4. Ribbon quantum groupoids.
Deﬁnition 5.4.1. A ribbon quantum groupoid is a quasitriangular quantum group-
oid with an invertible central element ν ∈H such that
∆( ν) = R21R(ν ⊗ν) and S(ν) = ν.(41)
The element ν is called a ribbon element of H.
For an object V of Rep(H) we deﬁne the twist θV :V →V to be the multipli-
cation by ν :
θV (v) = ν ·v, v ∈V.(42)
Proposition 5.4.2. Let (H, R,ν ) be a ribbon quantum groupoid. The family of
homomorphisms {θV }V deﬁnes a twist in the braided monoidal category Rep (H)
compatible with duality. Conversely, if θV (v) = ν ·v is a twist in Rep (H), then ν
is a ribbon element of H.
Proof. Since ν is an invertible central element of H, the homomorphism θV is an
H-linear isomorphism. The twist identity follows from the properties of ν :
cW,VcV,W (θV ⊗θW )(x) = R21R(ν ·x(1) ⊗ν ·x(2)) = ∆( ν) ·x =θV ⊗W (x),
for all x = x(1) ⊗x(2) ∈ V ⊗W . Clearly, the identity R21R(ν ⊗ν) = ∆( ν) is
equivalent to the twist property. It remains to prove that
(θV ⊗ idV ∗ )bV (z) = (id V ⊗θV ∗ )bV (z),
for all z ∈Ht, i.e., that
∑
i
νz(1) ·γi ⊗z(2) ·gi =
∑
i
z(1) ·γi ⊗νz(2) ·gi,
FINITE QUANTUM GROUPOIDS AND THEIR APPLICA TIONS 21
where ∑
i γi ⊗gi is the canonical element in V ∗ ⊗V . Evaluating the ﬁrst factors
of the above equality on an arbitrary v ∈V , we get the equivalent condition :
∑
i
(νz(1) ·γi)(v)z(2) ·gi =
∑
i
(z(1) ·γi)(v)νz(2) ·gi,
which reduces to z(2)S(νz(1)) ·v = S(z(1))νz(2) ·v. The latter easily follows from
the centrality of ν =S(ν) and properties of Ht.
Proposition 5.4.3. The category Rep (H) is a ribbon category if and only if H is
a ribbon quantum groupoid.
Proof. Follows from Propositions 5.1.2, 5.2.2, and 5.4.2.
For any endomorphism f of the object V , we deﬁne, following [T], I.1.5, its
quantum trace
trq(f ) = dVcV,V ∗(θVf ⊗ idV ∗ )bV(43)
with values in End( Ht) and the quantum dimension of V by dim q(V ) = tr q(idV ).
Corollary 5.4.4 ([NTV], 7.4) . Let (H, R,ν ) be a ribbon quantum groupoid, f be
an endomorphism of an object V in Rep (H). Then
trq(f )(z) = Tr(S(1(1))uνf )z1(2), dimq(V )(z) = Tr(S(1(1))uν)z1(2),(44)
where Tr is the usual trace of endomorphism, and u is the Drinfeld element.
Corollary 5.4.5. Let k be algebraically closed. If the trivial H-module Ht is ir-
reducible (which happens exactly when Ht ∩Z(H) = k, i.e., when H is connected
([N1], 3.11, [BNSz], 2.4), then tr q(f ) and dimq(V ) are scalars:
trq(f ) = (dimHt)−1 Tr(uνf ), dimq(V ) = (dim Ht)−1Tr(uν).(45)
Proof. Any endomorphism of an irreducible module is the multiplication by a scala r,
therefore, we must have Tr (S(1(1))uνf )1(2) = tr q(f )1. Applying the counit to both
sides and using that ε(1) = dim Ht, we get the result.
