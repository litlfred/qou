---
doc_id: bn
doc_title: "Braid groups and Hodge theory Curtis T. McMullen 25 April, 2009"
section_id: sec-018-6-the-period-map
section_title: "The period map"
section_number: 6
pages: 27-32
source_pdf: bn.pdf
source_sha256: 95ed0908ceb54a1c
doc_brief: "Braid groups and Hodge theory Curtis T. McMullen 25 April, 2009 — This paper gives an account of the unitary representations of the braid group that arise via the Hodge theory of cyclic branched cove"
---
In this section we introduce the period map
fq : T ∗
0,n → H r,s
from the Teichm¨ uller space of n points in the plane to the space Hr,s of
positive lines in Cr,s . This map records, for each conﬁguration B ⊂ C and
for q =ζ −k
d , the line in H 1(X)q ∼
= Cr,s spanned by the holomorphic 1-form
[dx/yk]. It is deﬁned so long as 1 /n<k/d< 1.
We then show:
Theorem 6.1 The period map is a holomorphic local diﬀeomorphism when
qn ⁄= 1. Otherwise it is a submersion, with 1-dimensional ﬁbers.
Corollary 6.2 Providedqn ⁄= 1 , the period map gives M∗
0,n the structure
of a (G,X )-manifold, where G = U(r,s ) and X = Hr,s .
Note: When q = −1, the structure group can be reduced from U( g,g ) to
Sp2g(R) (see §12).
Corollary 6.3 The moduli space M∗
0,n is endowed with a natural K¨ ahler
metric of constant negative curvature for each k/d ∈ (1/n, 2/n), and con-
stant positive curvature for each k/d ∈ (1−1/n, 1).
These metrics are modeled on the symmetric spaces CPn−2 and CHn−2
respectively. (For more on the complex hyperbolic case, see §10 and [Th2].)
Theorem 6.4 When q = ζ −2
n , the period map descends to a holomorphic
local diﬀeomorphism fq : T0,n → CHn−3.
Corollary 6.5 The period map for q = ζ −2
n gives M0,n the structure of a
complex hyperbolic orbifold.
Positive lines. Given (r,s ) with r> 0, we let
Hr,s ∼
= U(r,s )/ U(r−1,s ) × U(1)
denote the space of positive lines in the Hermitian vector sp ace Cr,s . Thus
Hr, 0 ∼
= CPr−1 and H1,s ∼
= CHs. In general, Hr,s carries an invariant Her-
mitian metric of signature ( r − 1,s ). (It should not be confused with the
26
bounded symmetric domain U( r,s )/(U(r) × U(s)), whose natural metric is
always Riemannian [Sat, Appendix, §3].)
Holomorphic 1-forms. Let Ω( X) denote the g-dimensional vector space
of holomorphic 1-forms ω on X ∈ M g. Assume ω ⁄= 0, and let Z ⊂ X
denote its zero set.
The absolute periods of ω are given by
∫
Cω, where C ranges all closed
loops on X. The relative periods include, more generally, integrals along
paths joining the zeros of ω. The relative periods are recorded by the coho-
mology class
[ω] ∈H 1(X,Z ) = Hom(H1(X,Z ), C),
and the absolute periods by its image in H 1(X).
Moduli spaces, T eichm¨ uller spaces and periods. We will regard the
moduli spaces
M∗
0,n = T ∗
0,n/ Mod∗
0,n and Mg = Tg/ Modg
as quotients of the associated Teichm¨ uller spaces of marke d Riemann sur-
faces. Any two diﬀerent markings of the same surface are relat ed by the
action of the mapping-class group.
The set of pairs ( X,ω ) with ω ⁄= 0 forms the moduli space of 1-forms
Ω Mg → M g.
This moduli space is a union of strata Ω Mg(p1,...,p s) labeled by partitions
of 2g − 2; a form ( X,ω ) lies in a given stratum iﬀ the zero set of ω consists
of s distinct points with multiplicities ( p1,...,p s).
The bundle Ω Mg → M g pulls back to a bundle Ω Tg → T g which is
stratiﬁed in the same way. The cohomology groups H 1(X) form a trivial
bundle over Tg; thus if we ﬁx a basepoint ( X0,ω 0) ∈ Ω Tg, we have a natural
absolute period map
α : Ω Tg →H 1(X0)
given by α(X,ω ) = [ω] ∈H 1(X) ∼
=H 1(X0).
Similarly, the cohomology groups H 1(X,Z ) form a locally trivial bundle
over any stratum, so we have a locally deﬁned relative period map
π : Ω Tg(pi) →H 1(X0,Z 0).
By [V2] and [MS, Lemma 1.1], these relative period maps are ho lomorphic
local homeomorphisms.
27
Point conﬁgurations. Now ﬁx an integer n ≥ 2, a degree d > 1 and a
level k with 1/n < k/d <1. Set q = ζ −k
d and e = gcd(d,n ). As usual,
we associate to a point conﬁguration B = (b1,...,b n) ∈ C⟨n⟩ the branched
covering space
X :yd = (x −b1) · · · (x −bn)
with deck transformation T . The level k picks out a holomorphic eigenform
ω =dx/yk ∈H 1, 0(X)q, and F (B) = (X,ω ) gives a holomorphic map
F : C⟨n⟩ → Ω Mg(p1,...,p s).
Here the partition ( pi) depends only on ( n,k,d ); it can be read oﬀ from the
formula
(ω) = (kn/e −d/e − 1)~∞ + (d − 1 −k)~B,
which is a special case of equation (3.2).
Note that X and the divisor ( ω) depend only the pair ( C,B ) up to
isomorphism, and (ω) determines ω up to scale. Thus F descends to a map
M∗
0,n → PΩ Mg. If d|n thenX is unramiﬁed over inﬁnity, so it only depends
on the pair ( ˆC,B ); and if k/d = 2/n as well, then the same is true of the
divisor (ω) = (n − 3)~B. Summing up, we have a commutative diagram:
C⟨n⟩
/d15/d15
F /d47/d47Ω Mg
/d15/d15
M∗
0,n
/d15/d15
/d47/d47PΩ Mg
/d15/d15
M0,n
/d58/d58
/d47/d47Mg
(6.1)
whose bottom arrow exists when d|n, and whose diagonal arrow exists when
we also have k/d = 2/n.
The period map. Lifting to the universal cover of the domain, we obtain
a map
~F : ~C⟨n⟩ → Ω Tg
whose image we denote by (Ω Tg)q. By construction, the absolute periods of
any form in the image of ~F determine a positive vector
[ω] ∈H 1(X)q ∼
=H 1(X0)q ∼
= Cr,s,
28
because the trivialization of H 1(X) over (Ω Tg)q respects the action of T .
The line [ Cω] depends only the location of B in Teichm¨ uller space, soα ◦~F
descends to a function
fq : T ∗
0,n → H r,s
which we call the period map.
Since Hr,s is constructed from the ﬂat bundle H 1(X)q over C⟨n⟩ with
holonomy ρq : Bn → U(r,s ), the map fq is equivariant with respect to the
actions coming from Bn → Mod∗
0,n and Bn → PU(r,s ) (see equation (2.5)).
Lemma 6.6 The map ~F covers a bijection
T ∗
0,n → (PΩ Tg)q,
except when d|n and k/d = 2/n, in which case it factors through a bijection
on T0,n .
Proof. For each (X,ω ) ∈ (Ω Tg)q there is a T ∈ Aut(X) which is in the same
isotopy class as the deck transformation T0 at the basepoint X0, and which
satisﬁes T ∗(ω) = qω. The data ( X,ω,T ) generally allows us to reconstruct
the original conﬁguration ( ˆC,B, ∞) ∈ T ∗
0,n , by setting
~B ∪~∞ =Z(ω) ∪ Fix(T e) (6.2)
and passing to the quotient X/T ∼
=ˆC. This reconstruction succeeds unless
d|n and k/d = 2 /n. In this special case, X is unramiﬁed over ∞ and
(ω) = ( d − 3)~B, so (6.2) does not hold. But then ( X,ω ) depends only on
the location of [ B] in T0,n , and the same procedure recovers ( ˆC,B ).
Lemma 6.7 The relative period map from (Ω Tg)q toH 1(X0,Z 0)q is a local
homeomorphism.
Proof. Recall that the relative period map gives a local homeomorph ism
Ω Tg ⊃ U → H 1(X0,Z 0). The points in H 1(X0,Z 0)q correspond to eigen-
forms (X,ω,T ) with the same combinatorics as ( X0,ω 0,T 0), so they come
from branched coverings of the sphere.
29
Corollary 6.8 The image of M∗
0,n in PΩ Mg is locally a union of linear
submanifolds with respect to period coordinates.
Lemma 6.9 The map H 1(X0,Z 0)q →H 1(X0)q is surjective.
Proof. The map H 1(X0,Z 0) →H 1(X0) is surjective, and T has ﬁnite order
so its action is semisimple.
Proof of Theorems 6.1 and 6.4. The three lemmas above show fq
is a composition of submersions. By Corollary 3.3 we have dim Hr,s =
n − 2 if qn ⁄= 1 and n − 3 otherwise. Since dim T ∗
0,n = n − 2, fq is a local
homeomorphism in the ﬁrst case and fq has one-dimensional ﬁbers in the
second. When d|n andk/d =n/2 the map fq factors through T0,n by Lemma
6.6, and (r,s ) = (1,n − 3) by Corollary 3.2 so its target is CHn−3.
Proof of Corollaries 6.5 and 6.3. By Corollary 3.2 we have ( r,s ) =
(n − 3, 0) or (1 ,n − 2) in these two cases, so fq gives an equivariant map
to CPn−2 or CHn−2. Pulling back the U (r,s )-invariant metric on the target
gives the desired Mod ∗
0,n -invariant metric on the domain.
Example: conformal mapping. For a concrete instance of the period
map, suppose n = 3 and q =ζ −k
d with 1/3<k/d ≤ 1. We can identify the
moduli space ~M∗
0, 3 of ordered triples of points in C with C − {0, 1}. Then
anyt ⁄= 0, 1 determines a Riemann surface of the form
yd =x(x − 1)(x −t),
and the (multivalued) period map fq : ~M∗
0, 3 → P1 is given by
fq(t) = [
∫ 1
0 dx/yk :
∫ ∞
1 dx/yk].
This Schwarz triangle function is univalent on the upper halfplane, and
T =fq(H) is an equilateral circular triangle with internal angles
2π|k/d − 1/2|; compare [SG, §14, §16.6]. The triangle T is Euclidean for
k/d = 2/3, spherical for k/d> 2/3, and hyperbolic for k/d< 2/3.
Filtrations. We remark that diﬀerentials p(x)dx/yk with degp<i deter-
mine a ﬁltration
0 ⊂F1 ⊂F2 ⊂ · · ·Fr ⊂H 1(X)q,
whose variation as a function of B could also be studied. We have focused
our attention on the ﬁrst term so that the period map becomes a local
homeomorphism, providing a geometric structure on moduli s pace.
30
Notes. An elegant characterization of those classes C ∈ H 1(X) which lie
in H 1, 0(X) for some complex structure on X is given in [Kap] (see also §12
below). Another approach to Theorem 6.1 appears in [DM1, Pro p. 3.9].
