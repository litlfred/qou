---
doc_id: arxiv-0811.2435v1
doc_title: "Stability structures, motivic Donaldson-Thomas invariants and cluster transformations"
section_id: sec-004-multiplicative-wall-crossing-formula
section_title: "Multiplicative wall-crossing formula"
section_number: null
pages: 10-15
source_pdf: 0811.2435v1.pdf
source_sha256: 615b04eca83bcade
doc_brief: "Stability structures, motivic Donaldson-Thomas invariants and cluster transformations — 43 sections: Introduction; Counting problems for 3-dimensiona; Non-commutative varieties with pol"
---
The wall-crossing formulas for the numerical Donaldson-Th omas invariants
do not depend on their origin and can be expressed in terms of g raded Lie
algebras. This is explained in Section 2. Our main applicati on is the case of
3d Calabi-Yau categories. Let us recall that if C is an Ext-ﬁnite Calabi-Yau
category of the odd dimension d (e.g. d = 3) then the Euler form
χ :K0(C)⊗K0(C)→ Z, χ (E,F ) :=
∑
n∈Z
(−1)n dim Extn(E,F )
10
is skew-symmetric. In this case we also assume that if C is endowed with
polarization, then a skew-symmetric bilinear form ⟨•,•⟩: Γ⊗ Γ → Z is given
and satisﬁes
⟨cl(E), cl(F )⟩=χ(E,F ) ∀E,F ∈Ob(C).
In general, having a free abelian group Γ of ﬁnite rank endowe d with an
integer-valued skew-symmetric form ⟨•,•⟩, we deﬁne a Lie algebra over Q
gΓ := g(Γ,⟨•,•⟩), with the basis ( eγ)γ∈Γ and the Lie bracket
[eγ1,eγ2] = (−1)⟨γ1,γ2⟩⟨γ1,γ 2⟩eγ1+γ2 .
This Lie algebra is isomorphic (non-canonically) to the Lie algebra of
regular functions on the algebraic Poisson torus Hom(Γ , Gm) endowed with
the natural translation-invariant Poisson bracket. 4
An additive map Z : Γ → C is called generic if there are no two Q-
independent elements of the lattice Γ which are mapped by Z into the same
straight line in R2 = C. The set of non-generic maps is a countable union of
real hypersurfaces in Cn = Hom(Γ , C). These hypersurfaces are called walls.
Let us choose such an additive map Z and an arbitrary norm ‖•‖on
the real vector space Γ R = Γ ⊗ R. We will keep the same notation for the
R-linear extension of Z to Γ R. Finally, assume that we are given an even
map Ω : Γ \{ 0}→ Z supported on the set of γ∈ Γ such that ‖γ‖≤C|Z(γ)|
for some given constant C >0.
Let (Zt)t∈[0,1] be a generic piece-wise smooth path in Cn = Hom(Γ , C)
such that Z0 and Z1 are generic. The wall-crossing formula calculates the
function Ω 1 corresponding to Z1 in terms of the function Ω = Ω 0 correspond-
ing to Z0. This is analogous to the analytic continuation of a holomor phic
function expressed in terms of its Taylor coeﬃcients. The co ntinuation is
unique if it exists, and is not changed under a small deformat ion of the path
with the ﬁxed endpoints.
Let us call strict a sector in R2 with the vertex at the origin (0 , 0) which
is less than 180 ◦. With a strict sector V⊂ R2 we associate a group element
AV given by the inﬁnite product
AV :=
−→∏
γ∈Z −1(V )∩Γ
exp
(
−Ω( γ)
∞∑
n=1
enγ
n2
)
.
4Later we will use the multiplication as well. It is given expl icitly by eγ 1eγ 2 =
(−1)⟨γ 1,γ 2⟩ eγ 1+γ 2 .
11
The product takes value in a certain pro-nilpotent Lie group GV :=
GV,Γ,⟨•,•,⟩, which we will describe below. The right arrow in the product
sign means that the product is taken in the clockwise order on the set of
rays R+·Z(γ)⊂V⊂ C. For the product in the anti-clockwise order we will
use the left arrow.
Let us describe the Lie algebra gV = Lie(GV ) of the pro-nilpotent Lie
groupGV . We denote by C(V ) a convex cone in Γ R which is the convex hull
of the set of points v∈ Z−1(V ) such that ‖v‖≤C|Z(v)|. The Lie algebra
Lie(GV ) is the inﬁnite product ∏
γ∈Γ∩C(V ) Q·eγ equipped with the above Lie
bracket.
Now we can formulate the wall-crossing formula. It says (rou ghly) that
AV does not change as long as no lattice point γ∈ Γ with Ω t(γ)⁄= 0 crosses
the boundary of the cone Z−1
t (V ) (here Ω t corresponds to the point t∈ [0, 1]).
By our assumptions, if t =t0 corresponds to a non-generic central charge Zt0
then there exists a 2-dimensional lattice Γ 0⊂ Γ such that Zt0(Γ 0) belongs to
a real line Reiα for some α∈ [0,π ].
The wall-crossing formula describes the change of values Ω( γ) for γ∈ Γ 0
and depends only on the restriction Ω |Γ 0 of Ω to the lattice Γ 0. Values Ω( γ) for
γ /∈ Γ 0 do not change at t =t0. Denote by k∈ Z the value of the form ⟨•,•⟩
on a ﬁxed basis γ1,γ 2 of Γ 0≃ Z2 such thatC(V )∩Γ 0⊂ Z/greaterorequalslant0·γ1⊕Z/greaterorequalslant0·γ2. We
assume that k⁄= 0, otherwise there will be no jump in values of Ω on Γ 0. The
group elements which we are interested in can be identiﬁed wi th products
of the following automorphisms 5 of Q[[x,y ]] preserving the symplectic form
k−1(xy)−1dx∧dy:
T (k)
a,b : (x,y )↦→
↦→
(
x· (1− (−1)kabxayb)−kb,y· (1− (−1)kabxayb)ka)
,a,b /greaterorequalslant0,a +b /greaterorequalslant1.
Forγ =aγ1 +bγ2 we have
T (k)
a,b = exp
(
−
∑
n/greaterorequalslant1
enγ
n2
)
in the above notation. Any exact symplectomorphism φ of Q[[x,y ]] can be
5Here we write an automorphism as acting on elements of the alg ebra of functions. The
corresponding automorphism on points is given by the inverse formula.
12
decomposed uniquely into a clockwise and an anti-clockwise product:
φ =
−→∏
a,b
(
T (k)
a,b
)ca,b
=
←−∏
a,b
(
T (k)
a,b
)da,b
with certain exponents ca,b,da,b∈ Q. These exponents should be interpreted
as the limiting values of the functions Ω ±
t0 = limt→t0±0 Ω t restricted to Γ 0.
The passage from the clockwise order (when the slope a/b∈ [0, +∞]∩ P1(Q)
decreases) to the anti-clockwise order (when the slope incr eases) gives the
change of Ω |Γ 0 as we cross the wall. It will be convenient to denote T (1)
a,b
simply by Ta,b. The pro-nilpotent group generated by transformations T (k)
a,b
coincides with the one generated by transformations Ta,|k|b.
The compatibility of the wall-crossing formula with the integrality of the
numbers Ω( γ) is not obvious but follows from:
Conjecture 1 If for k > 0 one decomposes the product T1,0·T0,k in the
opposite order:
T1,0·T0,k =
∏
a/b increases
(Ta,kb)d(a,b,k),
then d(a,b,k )∈ Z for all a,b,k .
An equivalent form of this conjecture says that if one decomp osesTk
1,0·Tk
0,1
in the opposite order then all exponents will belong to kZ.
Here are decompositions for k = 1, 2
T1,0·T0,1 =T0,1·T1,1·T1,0 ,
T (2)
1,0·T (2)
0,1 =T (2)
0,1·T (2)
1,2·T (2)
2,3····· (T (2)
1,1 )−2····· T (2)
3,2·T (2)
2,1·T (2)
1,0 ,
or equivalently
T1,0·T0,2 =T0,2·T1,4·T2,6····· T−2
1,2····· T3,4·T2,2·T1,0 .
Greg Moore and Frederik Denef pointed out that the factors in the last
formula correspond to the BPS spectrum of N = 2,d = 4 super Yang-Mills
model studied by Seiberg and Witten in [63]. A “physical” exp lanation of
our formulas in this context was given in [24], see also our Se ction 2.7.
13
Fork /greaterorequalslant3 or k≤− 1 the decomposition of T (k)
1,0·T (k)
0,1 is not yet known
completely. Computer experiments give a conjectural formu la for the diago-
nal term with the slope a/b = 1. The corresponding symplectomorphism is
given by the map
(x,y )↦→(x·Fk(xy)−k,y·Fk(xy)k),
where the series Fk =Fk(t)∈ 1 +tZ[[t]] is an algebraic hypergeometric series
given for k /greaterorequalslant3 by the formulas:
∞∑
n=0
((k− 1)2n +k− 1
n
) tn
(k− 2)n + 1 = exp
( ∞∑
n=1
((k− 1)2n
n
) k
(k− 1)2
tn
n
)
.
The function Fk satisﬁes the equation
Fk(t)
(
1−tFk−2
k (t)
)k
− 1 = 0 .
Remark 3 The above example for k = 1 is compatible with the expected
behavior of Donaldson-Thomas invariants when we have two sp herical objects
E1,E 2∈C (sphericity means that Ext•(Ei,Ei) = H•(S3)) such that
Ext1(E2,E 1) = k, Extn(E2,E 1) = 0 for n⁄= 1 .
In this case on the one side of the wall we have two semistable o bjectsE1,E 2,
and on the other side we have three semistable objects E1,E 2,E 12 whereE12
is the extension of E2 by E1. In the case of the derived of the Fukaya cat-
egory the objects Ei,i = 1, 2 can correspond to embedded special Lagrangian
spheres intersecting transversally at one point. Then E12 corresponds to their
Lagrangian connected sum.
The automorphisms Ta,b are a special case of the more general ones.
Namely, we can consider the following rational automorphis ms of gΓ (consid-
ered as a Poisson algebra):
Tγ :eµ↦→(1−eγ)⟨γ,µ⟩eµ, γ,µ ∈ Γ .
The group element AV in the above notation has the form
AV =
−→∏
γ∈Z −1(V )∩Γ
T Ω( γ)
γ
14
and acts on a completion of gΓ . It is easy to quantize this Poisson alge-
bra. The corresponding algebra (quantum torus) is additive ly generated by
quantum generators ˆeγ,γ ∈ Γ subject to the relations
ˆeγ ˆeµ =q
1
2⟨γ,µ⟩ˆeγ+µ ,
where q is a parameter (with the classical limit q
1
2 →− 1). Then one has
formulas similar to the above for the “quantum” analogs of au tomorphisms
Tγ,γ ∈ Γ (see Sections 6.4 and 7.1).
For general k≥ 2 the decomposition of the product T1,0·T0,k as in Con-
jecture 1, describes numerical DT-invariants of the Calabi -Yau category as-
sociated with the Kronecker quiver consisting of two vertic es and k parallel
arrows (see Section 8 for a general theory). Recent paper [58 ] gives an ex-
plicit formula for d(a,b,k ) in terms of the Euler characteristic of the framed
moduli space of semistable representations of the quiver. M oreover, a weak
form of the integrality Conjecture 1 is proved in [58].
