---
doc_id: monodromyhitchiny
doc_title: "On the monodromy of the Hitchin connection"
section_id: sec-000-on-the-monodromy-of-the-hitchin-connection
section_title: "ON THE MONODROMY OF THE HITCHIN CONNECTION"
section_number: null
pages: 2-14
source_pdf: MonodromyHitchinY.pdf
source_sha256: 1c9288ddbb5bc2d8
toc_source: inferred
doc_brief: "On the monodromy of the Hitchin connection — 2 sections: Front matter; ON THE MONODROMY OF THE HITCHIN CO"
---
YVES LASZLO, CHRISTIAN PAULY, AND CHRISTOPH SORGER
Abstract. We show that the image of the monodromy representation of the Hitchin con-
nection on the sheaf of generalized SL(2)-theta functions over a family of complex smooth
projective curves of genus g ≥3 contains an element of inﬁnite order.
1. Introduction
Let π : C →B be a family of smooth connected complex projective curves of genus1 g ≥3. For
any positive integer l, we denote Zl the vector bundle over B having ﬁbers H0(MCb(SL(2)), L⊗l),
where MCb(SL(2)) is the moduli space of semistable rank-2 vector bundles with trivial deter-
minant over the curve Cb = π−1(b) for b ∈B and L is the ample generator of the Picard group.
Following Hitchin [H], the bundle Zl is equipped with a projectively ﬂat connection called the
Hitchin connection.
Theorem. Assume that the level l̸ = 1, 2, 4, 8 and that the genus g ≥3. Then there exists
a family π : C →B of smooth connected projective curves of genus g such that the monodromy
representation of the Hitchin connection
ρl : π1(B, b) −→PGL(Zl,b)
has an element of inﬁnite order in its image.
Remark 1.1. An analagous statement is true for more general simple groups, at least for
SL(n), n ≥2 (see remark 4.3 below).We will discuss this question in a future paper.
In the context of Topological Quantum Field Theory as deﬁned by Blanchet-Habegger-
Masbaum-Vogel [BHMV], the analogue of the above theorem is well known due to work of
Funar [F] for the inﬁniteness of the image and of Masbaum [Ma] for the exhibition of an
explicit element in the mapping class group with image of inﬁnite order.
It is enough to show the above theorem in the context of Conformal Field Theory as deﬁned
by Tsuchiya-Ueno-Yamada [TUY]: following a result of the ﬁrst author [L], the monodromy
representation associated to Hitchin’s connection coincides with the monodromy representation
of the WZW connection. As both, the above Conformal Field Theory and the above Topological
Quantum Field Theory are predicted to be equivalent by work in progress of Andersen and
Ueno ([AU1], [AU2] and [AU3]), the above theorem should follow from the work of Funar and
Masbaum.
In this short note, we give a direct algebraic proof, avoiding the above identiﬁcation: we ﬁrst
recall Masbaum’s initial argument applied to Tsuchiya-Kanie’s description of the monodromy
2000 Mathematics Subject Classiﬁcation. Primary 14D20, 14H60, 17B67.
Partially supported by ANR grant G-FIB.
1The genus assumption is just a simplicity assumption and can be relaxed.
1
2
YVES LASZLO, CHRISTIAN PAULY, AND CHRISTOPH SORGER
representation for the WZW connection in the case of the projective line with 4 points labeled
with the standard 2-dimensional representation (see also [AMU]), then we observe that the
sewing procedure induces a projectively ﬂat map, enabling us to make an induction on the
genus.
A couple of words about the exceptional levels l = 1, 2, 4, 8 are in order. For l = 1 the mon-
odromy representation ρ1 is ﬁnite for any g. This follows from the fact that Beauville’s [B1]
strange duality isomorphism PH0(MCb(SL(2)), L)∗
∼→PH0(Picg−1(Cb), 2Θ) is projectively ﬂat
over B for any family π : C →B (see e.g. [Bel1]) and that ρ1 thus identiﬁes with the monodromy
representation on a space of abelian theta functions, which is known to have ﬁnite image (see
e.g. [W]). For l = 2 there is a canonical morphism H0(MCb(SL(2)), L⊗2)→H0(Picg−1(Cb), 4Θ)+,
which is an isomorphism if and only if Cb has no vanishing theta-null [B2]. But this map is
not projectively ﬂat having not constant rank. So the question about ﬁniteness of ρ2 remains
open — see also [Bel2]. For l = 4 there is a canonical isomorphism [OP] between the dual
H0(MCb(SL(2)), L⊗4)∗and a space of abelian theta functions of order 3. We expect this isomor-
phism to be projectively ﬂat. For l = 8 no isomorphism with spaces of abelian theta functions
seems to be known.
Our motivation to study the monodromy representation of the Hitchin connection comes from
the Grothendieck-Katz conjectures on the p-curvatures of a local system [K]. In a forthcoming
paper we will discuss the consequences of the above theorem in this set-up.
Acknowledgements: We would like to thank Jean-Benoˆıt Bost, Louis Funar and Gregor
Masbaum for helpful conversations.
2. Review of mapping class groups, moduli spaces of pointed curves and braid
groups
2.1. Mapping class groups. In this section we recall the basic deﬁnitions and properties of
the mapping class groups. We refer the reader e.g. to [I] or [HL].
2.1.1. Deﬁnitions. Let S be a compact oriented surface of genus g without boundary and with
n marked points x1, . . . , xn ∈S.
Associated to the n-pointed surface S are the mapping
class groups Γn
g and Γg,n deﬁned as the groups of isotopy classes of orientation-preserving
diﬀeomorphisms φ : S →S such that φ(xi) = xi for each i, respectively such that φ(xi) = xi
and the diﬀerential dφxi : TxiS →TxiS at the point xi is the identity map for each i.
An alternative deﬁnition of the mapping class groups Γn
g and Γg,n can be given in terms of
surfaces with boundary. We consider the surface R obtained from S by removing a small disc
around each marked point xi. The boundary ∂R consists of n circles. Equivalently, the groups
Γn
g and Γg,n coincide with the groups of isotopy classes of orientation-preserving diﬀeomorphisms
φ : R →R such that φ preserves each boundary component of R, respectively such that φ is
the identity on ∂R.
The mapping class group Γg is deﬁned to be Γ0
g = Γg,0.
3
2.1.2. Dehn twists. Given an (unparametrized) oriented, embedded circle γ in R ⊂S we can
associate to it a diﬀeomorphism Tγ up to isotopy, i.e., an element Tγ in the mapping class groups
Γn
g and Γg,n, the so-called Dehn twist along the curve γ. It is known that the mapping class
groups Γn
g and Γg,n are generated by a ﬁnite number of Dehn twists. We recall the following
exact sequence
1 −→Zn −→Γg,n −→Γn
g −→1.
The n generators of the abelian kernel Zn are given by the Dehn twists Tγi, where γi is a loop
going around the boundary circle associated to xi for each i.
2.1.3. The mapping class groups Γ4
0 and Γ0,4. Because of their importance in this paper we recall
the presentation of the mapping class groups Γ4
0 and Γ0,4 by generators and relations. Keeping
the notation of the previous section, we denote by R the 4-holed sphere and by γ1, γ2, γ3, γ4 the
circles in R around the four boundary circles. We denote by γij the circle dividing R into two
parts containing two holes each and such that the two circles γi and γj are in the same part.
It is known (see e.g. [I] section 4) that Γ0,4 is generated by the Dehn twists Tγi for 1 ≤i ≤4
and Tγij for 1 ≤i, j ≤3 and that, given a suitable orientation of the circles γi and γij, there is
a relation (the lantern relation)
Tγ1Tγ2Tγ3Tγ4 = Tγ12Tγ13Tγ23.
Note that the images of the Dehn twists Tγi under the natural homomorphism
Γ0,4 −→Γ4
0,
Tγ 7→T γ,
are trivial. Thus the group Γ4
0 is generated by the three Dehn twists T ij for 1 ≤i, j ≤3 with
the relation T γ12T γ13T γ23 = 1.
For each 4-holed sphere being contained in a closed genus g surface without boundary one
can consider the Dehn twists Tij as elements in the mapping class group Γg.
2.2. Moduli spaces of curves. Let Mg,n denote the moduli space parameterizing n-pointed
smooth projective curves of genus g. The moduli space Mg,n is a (possibly singular) algebraic
variety.
It can also be thought as an orbifold (or Deligne-Mumford stack) and one has an
isomorphism
(1)
j : π1(Mg,n, x)
∼
−→Γn
g,
where π1(Mg,n, x) stands for the orbifold fundamental group of Mg,n. In case the space Mg,n is a
smooth algebraic variety, the orbifold fundamental group coincides with the usual fundamental
group.
2.3. The isomorphism between π1(M0,4, x) and Γ4
0. The moduli space M0,4 parametrizes
ordered sets of 4 points on the complex projective line P1
C up to the diagonal action of
PGL(2, C).
The double ratio induces an isomorphism with the projective line P1
C with 3
punctures at 0, 1 and ∞
M0,4
∼
−→P1
C \ {0, 1, ∞}.
We deduce that the fundamental group of M0,4 is the group with three generators
π1(M0,4, x) = ⟨σ1, σ2, σ3 | σ3σ2σ1 = 1⟩,
where σ1, σ2 and σ3 are the loops starting at x ∈P1
C \ {0, 1, ∞} and going once around the
points 0, 1 and ∞with the same orientation. We choose the orientation such that the generators
4
YVES LASZLO, CHRISTIAN PAULY, AND CHRISTOPH SORGER
σi satisfy the relation σ3σ2σ1 = 1. Clearly π1(M0,4, x) coincides with the fundamental group
π1(Q, x) of the 3-holed sphere Q.
In this particular case the isomorphism j : π1(M0,4, x)
∼
−→Γ4
0 can be explicitly described as
follows (see e.g. [I] Theorem 2.8.C): we may view the 3-holed sphere Q as the union of the
4-holed sphere R with a disc D glued on the boundary corresponding to the point x4. Given
a loop σ ∈π1(Q, x) we may ﬁnd an isotopy {ft : Q →Q}0≤t≤1 such that the map t 7→ft(x)
coincides with the loop σ, f0 = idQ and f1(D) = D. Then the isotopy class of f1 resticted to
R ⊂Q determines an element j(σ) = [f1] ∈Γ4
0. Moreover, with the previous notation, we have
the equalities (see e.g. [I] Lemma 4.1.I)
j(σ1) = T γ23,
j(σ2) = T γ13,
j(σ3) = T γ12.
Remark 2.1. At this stage we observe that under the isomorphism j the two elements σ−1
1 σ2 ∈
π1(M0,4, x) and T
−1
γ23T γ13 ∈Γ4
0 coincide. It was shown by G. Masbaum in [Ma] that the latter
element has inﬁnite order in the TQFT-representation of the mapping class group Γg — note
that T −1
γ23Tγ13 also makes sense in Γg. We will show in Proposition 5.1 that the loop σ−1
1 σ2 has
inﬁnite order in the monodromy representation of the WZW connection.
2.4. Braid groups and conﬁguration spaces. We recall some basic results about braid
groups and conﬁguration spaces. We refer the reader e.g. to [KT] Chapter 1. For our purposes
it will be suﬃcient to deal with braid groups on 3 braids.
2.4.1. Deﬁnitions. The braid group B3 is the group generated by two generators g1 and g2 and
one relation
g1g2g1 = g2g1g2.
The pure braid group is the kernel P3 = ker(B3 →Σ3) of the group homomorphism which
associates to the generator gi the transposition (i, i + 1) in the symmetric group Σ3. The braid
groups B3 and P3 can be identiﬁed with the fundamental groups
P3 = π1(X3, p3),
B3 = π1(X3, p3),
where X3 and X3 are the complex manifolds parametrizing ordered respectively unordered
triples of distinct points in the complex plane
X3 = {(z1, z2, z3) ∈C3 | zi̸ = zj}
and
X3 = X3/Σ3.
The points p3 and p3 are base points in X3 and X3.
2.4.2. Relation between P3 and π1(M0,4, x). The natural map
M0,4 = P1
C \ {0, 1, ∞} −→X3,
z 7→(0, 1, z)
induces a group homomorphism at the level of fundamental groups
Ψ : π1(M0,4, x) = ⟨σ1, σ2⟩−→P3 = π1(X3, p3),
with p3 = (0, 1, x). Then Ψ is a monomorphism by [KT] Theorem 1.16. Moreover, the image
of Ψ coincides with the kernel of the natural group homomorphism
im Ψ = ker (P3 = π1(X3, p3) −→P2 = π1(X2, p2))
induced by the projection onto the ﬁrst two factors X3 →X2, (z1, z2, z3) 7→(z1, z2) and
p2 = (0, 1). One computes explicitly (see [KT] section 1.4.2) that
Ψ(σ1) = g2g2
1g−1
2 ,
and
Ψ(σ2) = g2
2.
5
For later use we introduce the element
(2)
σ = σ−1
1 σ2 ∈π1(M0,4, x).
3. Conformal blocks and the projective WZW connection
3.1. General set-up. We consider the simple Lie algebra g = sl2. The set of irreducible sl2-
modules, i.e. the set of dominant weights of sl2, is in bijection with the set of positive integers
N. We ﬁx an integer l ≥1, called the level, and introduce the set Pl = {λ ∈N | λ ≤l}. Given
an integer n ≥1, a collection⃗λ = (λ1, . . . , λn) ∈(Pl)n of dominants weights of sl2 and a family
F = (π : C →B; s1, . . . , sn; ξ1, . . . , ξn)
of n-pointed stable curves of arithmetic genus g parameterized by a base variety B with sections
si : B →C and formal coordinates ξi at the divisor si(B) ⊂C, one constructs (see [TUY] section
4.1) a locally free sheaf
V†
l,⃗λ(F)
over the base variety B, called the sheaf of conformal blocks or the sheaf of vacua. We recall
that V†
l,⃗λ(F) is a subsheaf of OB ⊗H†⃗
λ, where H†⃗
λ denotes the dual of the tensor product
H⃗λ = Hλ1 ⊗· · ·⊗Hλn of the integrable highest weight representations Hλi of level l and weight
λi of the aﬃne Lie algebra bsl2. The formation of the sheaf of conformal blocks commutes with
base change. In particular, we have for any point b ∈B
V†
l,⃗λ(F) ⊗OB Ob ∼= V†
l,⃗λ(Fb),
where Fb denotes the data (Cb = π−1(b); s1(b), . . . , sn(b); ξ1|Cb, . . . , ξn|Cb) consisting of a stable
curve Cb with n-marked points s1(b), . . . , sn(b) and formal coordinates ξi|Cb at the points si(b).
We recall that the sheaf of conformal blocks V†
l,⃗λ(F) does not depend (up to a canonical
isomorphism) on the formal coordinates ξi (see e.g. [U] Theorem 4.1.7). We therefore omit the
formal coordinates in the notation.
We will denote⃗
1n = (1, 1, . . . , 1) ∈(Pl)n
the collection having all dominants weights equal to 1, i.e., corresponding to the standard
2-dimensional representation of sl2.
3.2. The projective WZW connection. We now outline the deﬁnition of the projective
WZW connection on the sheaf V†
l,⃗λ(F) over the smooth locus Bs ⊂B parameterizing smooth
curves and refer to [TUY] or [U] for a detailed account. Let D ⊂B be the discriminant locus
and let S = `n
i=1 si(B) be the union of the images of the n sections. We recall the exact
sequence
0 −→π∗ΘC/B(∗S) −→π∗Θ′
C(∗S)π
θ
−→ΘB(−log D) −→0,
where ΘC/B(∗S) denotes the sheaf of vertical rational vector ﬁelds on C with poles only along
the divisor S, and Θ′
C(∗S)π the sheaf of rational vector ﬁelds on C with poles only along the
divisor S and with constant horizontal components along the ﬁbers of π. There is an OB-linear
map
p : π∗Θ′
C(∗S)π −→
n
M
i=1
OB((ξi)) d
dξi
,
6
YVES LASZLO, CHRISTIAN PAULY, AND CHRISTOPH SORGER
which associates to a vector ﬁeld⃗l in Θ′
C(∗S)π the n Laurent expansions li
d
dξi around the divisor
si(B). Abusing notation we also write⃗l for its image under p⃗
l = (l1
d
dξ1
, · · · , ln
d
dξn
) ∈
n
M
i=1
OB((ξi)) d
dξi
.
We then deﬁne for any vector ﬁeld⃗l in Θ′
C(∗S)π the endomorphism D(⃗l) of OB ⊗H†⃗
λ by
D(⃗l)(f ⊗u) = θ(⃗l).f ⊗u +
n
X
i=1
f ⊗(T[li].u)
for f a local section of OB and u ∈H†⃗
λ. Here T[li] denotes the action of the energy-momentum
tensor on the i-th component H†
λi. It is shown in [TUY] that D(⃗l) preserves V†
l,⃗λ(F) and that
D(⃗l) only depends on the image θ(⃗l) up to homothety.
One therefore obtains a projective
connection ∇on the sheaf V†
l,⃗λ(F) given by
∇θ(⃗l) = θ(⃗l) + T[⃗l].
Remark 3.1. For a family of smooth n-pointed curves of genus 0 the projective WZW con-
nection is actually a connection.
4. Monodromy of the WZW connection for a family of 4-pointed rational
curves
In this section we review the results by Tsuchiya and Kanie [TK] on the monodromy of the
WZW connection for a family of rational curves with 4 marked points. We take B = X3 =
{(z1, z2, z3) ∈C3 | zi̸ = zj} (see section 2.4.1) and consider the universal family
F = (π : C = B × P1 →B; s1, s2, s3, s∞),
where the section si is given by the natural projection X3 →C on the i-th component followed
by the inclusion C ⊂P1
C = C∪{∞} and s∞is the constant section corresponding to ∞∈P1
C.
We will denote
(3)
F univ
4
= (π : C = M0,4 × P1 →M0,4; t0, t1, t, t∞)
the pull-back of the family F under the natural embedding M0,4 →X3 (see section 2.4.2). We
consider for l ≥1 and for⃗λ =⃗14 ∈(Pl)4 the sheaf of conformal blocks V†
l,⃗14(F). The rank of
this locally free sheaf equals 2 for any l ≥1(see e.g. [TK] Theorem 3.3). Moreover V†
l,⃗14(F) is
equipped with a ﬂat actual connection ∇(not only projective) (see section 3.2).
Remark 4.1. It is known [TK] that the diﬀerential equations satisﬁed by the ﬂat sections of
(V†
l,⃗14(F), ∇) coincide with the Knizhnik-Zamolodchikov equations (see e.g. [EFK]). Moreover,
we will show in a forthcoming paper that the local system (V†
l,⃗14(F), ∇) also coincides with a
certain Gauss-Manin local system.
We observe that the symmetric group Σ3 acts naturally on the base variety X3. The local sys-
tem (V†
l,⃗14(F), ∇) is invariant under this Σ3-action and admits a natural Σ3-linearization. Thus
by descent we obtain a local system (V†
l,⃗14(F), ∇) over X3. Therefore, we obtain a monodromy
representation
7
eρl : B3 = π1(X3, p3) −→GL(V†
l,⃗14(F)
p3) = GL(2, C)
Proposition 4.2 ([TK] Theorem 5.2). We put q = exp( 2iπ
l+2). There exists a basis B of the
vector space V†
l,⃗14(F)
p3 = V†
l,⃗14(F)p3 such that
MatB(eρl(g1)) = q−3
4

q
0
0
−1

,
MatB(eρl(g2)) = q−3
4
q + 1

−1
t
t
q2

,
with t =
p
q(1 + q + q2). Note that both matrices have eigenvalues q
1
4 and −q−3
4.
Remark 4.3. We would like to mention that the above theorem has been generalized to the
Lie algebra sln in [Ka].
5. Infinite monodromy over M0,4
We denote by ρl the restriction of the monodromy representation eρl to the subgroup π1(M0,4, x)
ρl : π1(M0,4, x) →GL(2, C).
Proposition 5.1. Let σ ∈π1(M0,4, x) be the element introduced in (2). If the level l̸ = 1, 2, 4
and 8, then the element ρl(σ) has inﬁnite order in both PGL(2, C) and GL(2, C)
Proof. Using the explicit form of the monodromy representation ρl given in Proposition 4.2 we
compute the matrix associated to Ψ(σ) = Ψ(σ−1
1 σ2) = g2g−2
1 g2
MatB(eρl(Ψ(σ))) =
1
(q + 1)2

q−2 + t2
t(q2 −q−2)
t(q2 −q−2)
t2q−2 + q4

.
This matrix has determinant 1 and trace 2 −q −q−1 + q2 + q−2. Hence the matrix has ﬁnite
order if and only if there exists a primitive root of unity λ such that
λ + λ−1 = 2 −q −q−1 + q2 + q−2.
In [Ma] it is shown that this can only happen if l = 1, 2, 4 or 8: using the transitive action of
Gal( ¯Q/Q) on primitive roots of unity, one gets that for any primitive (l + 2)-th root ˜q there
exists a primitive root ˜λ such that
˜λ + ˜λ−1 = 2 −˜q −˜q−1 + ˜q2 + ˜q−2.
In particular, we have the inequality |1 −Re(˜q) + Re(˜q2)| ≤1 for any primitive (l + 2)-th
root ˜q. But for l̸ = 1, 2, 4 and 8, one can always ﬁnd a primitive (l + 2)-th root ˜q such that
Re(˜q2) > Re(˜q) — for the explicit root ˜q see [Ma].
Finally, since ρl(σ) has trivial determinant, its class in PGL(2, C) will also have inﬁnite
order.
□
Remark 5.2. The same computation shows that the element ρl(σ1σ−1
2 ) ∈GL(2, C) also has
inﬁnite order if l̸ = 1, 2, 4 and 8. This implies that the orientation chosen for both loops σ1 and
σ2 around 0 and 1 is irrelevant. On the other hand, it is immediately seen that the elements
ρl(σ1), ρl(σ2) and ρl(σ1σ2) have ﬁnite order for any level l.
8
YVES LASZLO, CHRISTIAN PAULY, AND CHRISTOPH SORGER
Proposition 5.3. In the four cases l = 1, 2, 4 and 8, the image ρl(π1(M0,4, x)) in the projective
linear group PGL(2, C) is ﬁnite and isomorphic to the groups given in table
l
1
2
4
8
ρl(π1(M0,4, x))
µ3
µ2 × µ2
A4
A5
Here An denotes the alternating group on n letters.
Proof. We denote by m1, m2 ∈PGL(2, C) the elements deﬁned by the matrices MatB(ρl(σ1))
and MatB(ρl(σ2)) and denote by ord(mi) their order in the group PGL(2, C). In the ﬁrst two
cases one immediately checks the relations m1 = m2, ord(m1) = ord(m2) = 3 (for l = 1) and
ord(m1) = ord(m2) = ord(m1m2) = 2 (for l = 2).
In the case l = 4 we recall that the alternating group A4 has the following presentation by
generators and relations
A4 = ⟨a, b | a3 = b2 = (ab)3 = 1⟩.
Using the formulae of Proposition 4.2 and 5.1 we check that ord(m1) = ord(m2) = 3 and
ord(m−1
1 m2) = 2, so that a = m1 and b = m−1
1 m2 generate the group A4.
In the case l = 8 we recall that the alternating group A5 has the following presentation by
generators and relations
A5 = ⟨a, b | a2 = b3 = (ab)5 = 1⟩.
Using the formulae of Proposition 4.2 and 5.1 we check that ord(m1) = ord(m2) = 5 and
ord(m−1
1 m2) = 3. Moreover a straightforward computation shows that the element m−1
1 m2m−1
1
is (up to a scalar) conjugate to the matrix
MatB(eρl(g−2
1 g2
2g−2
1 )) = ∗

q−4(1 + t2)
t(1 −q−2)
t(1 −q−2)
t2 + q4

,
which has trace zero. Note that t2 = q + q2 + q3 and q−4 = −q. Hence ord(m−1
1 m2m−1
1 ) =
ord(m1m−1
2 m1) = 2. Therefore if we put a = m1m−1
2 m1 and b = m−1
1 m2, we have ab = m1 and
ab2 = m2, so that ord(a) = 2, ord(b) = 3, and ord(ab) = 5, i.e. a, b generate the group A5.
□
Corollary 5.4. In the four cases l = 1, 2, 4 and 8, the image eρl(B3) in GL(2, C) is ﬁnite.
Proof. First, we observe that the image ρl(π1(M0,4, x)) in GL(2, C) is ﬁnite. In fact, by Propo-
sition 5.3 its image in PGL(2, C) is ﬁnite and its intersection ρl(π1(M0,4, x)) ∩C∗Id with
the center of GL(2, C) is also ﬁnite. The latter follows from the fact that the determinant
det MatB(eρl(gi)) = −q−1
2 has ﬁnite order in C∗.
Secondly, we recall that P3 is generated by the normal subgroup π1(M0,4, x) and by the
element g2
1. Since eρl(g2
1) has ﬁnite order and since B3/P3 = Σ3 is ﬁnite, we obtain that eρl(B3)
is a ﬁnite subgroup.
□
6. Infinite monodromy over Mg,n
6.1. Desingularization of families of nodal curves. We introduce the notation R = C[[τ]],
K = C((τ)) and K the algebraic closure of K. For a variety B deﬁned over C we denote
BR = B × Spec(R) and BK = B × Spec(K).
Proposition 6.1. Let eF = (eπ : eC →B; s1, . . . , sn+2) be a family of smooth n + 2 pointed
(not necessarily connected) curves parameterized by a base variety B and let F0 = (π0 : C0 →
9
B; s1, . . . , sn) be the n-pointed family of nodal curves obtained from e
F by identifying the two
points sn+1(b) and sn+2(b) of eCb = eπ−1(b) for each point b ∈B. Then there exists a ﬂat family
FR = (πR : CR →BR; s1,R, . . . , sn,R),
such that
(1) the restriction of FR to the special ﬁber (FR)0 is isomorphic to F0,
(2) the generic ﬁber FK is a family of smooth n-pointed curves over BK.
Proof. Let b ∈B.
We denote by A = b
OB,b the completion of the local ring OB,b and by
π0 : C0 →Spec(A) the pull-back of the family F0 of nodal curves of genus g to Spec(A). We
introduce the formal deformation space Γ →M of the stable n-pointed nodal curve (C0)b = C
with one node z ∈C (see [DM] section 1). Then we have the cartesian diagram
C0
−−−→
Γ
y
y
Spec A
s
−−−→M,
as well as n sections σi : M →Γ. By [DM] page 82, we have
M = Spec C[[t1, . . . , t3g−3+n]],
and
b
OΓ,z ∼= C[[t1, . . . , t3g−3+n, u, v]]/(uv −t1),
where t1 = 0 is the equation of the locus of singular curves in M.
The classifying map
s : Spec A →Spec C[[t1, . . . , t3g−3+n]] = M sends t1 to 0 ∈A (since Spec A parameterizes
singular curves) and ti to an element fi ∈A for i ≥2. We extend s to bs : Spec A[[τ]] −→
Spec C[[t1, . . . , t3g−3+n]] by mapping t1 to τ and ti to fi for i ≥2. The base change by bs then
deﬁnes an n-pointed family FR over Spec A[[τ]] such that F|Spec A((τ)) is smooth.
Hence, we have constructed the n-pointed family FR over Spec A[[τ]] for any complete local
ring A = b
OB,b, which proves the theorem.
□
6.2. The sewing procedure. We will brieﬂy sketch the construction of the sewing homomor-
phism and give some of its properties (for the details see [TUY] or [U]).
We consider two versal families e
F and FR parameterized by the base varieties B and BR as in
Proposition 6.1. For any dominant weight µ the Virasoro operator L0 induces a decomposition
of the representation space Hµ into a direct sum of eigenspaces Hµ(d) for the eigenvalue d+∆µ
of L0, where ∆µ ∈Q is the trace anomaly and d ∈N. We recall that there exists a unique (up
to a scalar) bilinear pairing (.|.) : Hµ × Hµ† →C such that (X(n)u|v) + (u|X(−n)v) = 0 for
any X ∈sl2, n ∈Z, u ∈Hµ, v ∈Hµ† and (.|.) is zero on Hµ(d)×Hµ†(d′) if d̸ = d′. We choose a
basis {v1(d), . . . , vmd(d)} of Hµ(d) and let {v1(d), . . . , vmd(d)} be its dual basis of Hµ†(d) with
respect to the above bilinear form. Then the element
γd =
md
X
i=1
vi(d) ⊗vi(d) ∈Hµ(d) ⊗Hµ†(d) ⊂Hµ ⊗Hµ†
does not depend on the basis. Given ψ ∈V†
l,⃗λ,µ,µ†( eF) we deﬁne an element eψ ∈H†⃗
λ ⊗OBR =
H†⃗
λ[[τ]] ⊗OB by the formula
⟨eψ|φ⟩=
∞
X
d=0
⟨ψ|φ ⊗γd⟩τ d,
for any φ ∈H⃗λ ⊗OB.
10
YVES LASZLO, CHRISTIAN PAULY, AND CHRISTOPH SORGER
Here ⟨.|.⟩denotes the standard pairing between H⃗λ,µ,µ† and its dual H†⃗
λ,µ,µ†. It is shown in
[TUY] that eψ ∈V†
l,⃗λ(FR), hence we obtain for any µ ∈Pl and any⃗λ ∈(Pl)n an OBR-linear map
sµ : V†
l,⃗λ,µ,µ†( eF) ⊗OB OBR −→V†
l,⃗λ(FR),
ψ 7→eψ.
Proposition 6.2. For any µ ∈Pl and any⃗λ ∈(Pl)n the sewing map over the generic ﬁber BK
sµ : V†
l,⃗λ,µ,µ†( eF) ⊗OB OBK −→V†
l,⃗λ(FK)
is projectively ﬂat for the WZW connections on both sheaves of conformal blocks.
Proof. By deﬁnition of the sewing map sµ it is clear that ∇D( eψ) = 0 if ∇D(ψ) = 0 for any local
vector ﬁeld D coming from B, i.e. independent of τ. Therefore the theorem is a corollary of
the following result proved in [TUY].
□
Theorem 6.3 ([TUY] Theorem 6.2.2). For any section ψ ∈V†
l,⃗λ,µ,µ†( eF) the multi-valued formal
power series bψ = τ ∆µ eψ satisﬁes the relation
∇τ d
dτ ( bψ) = 0
(mod OBK bψ).
Remark 6.4. We note that the statement given in [TUY] Theorem 6.2.2 says that there exists
a vector ﬁeld⃗l such that

−τ d
dτ + T[⃗l]

. bψ = 0
(mod OBK bψ),
which is equivalent to the above statement using the property θ(⃗l) = −τ d
dτ . This last equality
is actually proved in [TUY] Corollary 6.1.4, but there is a sign error. The correct formula of
[TUY] Corollary 6.1.4 is θ(⃗l) = −τ d
dτ , which is obtained by writing the 1-cocycle θ12(u, τ) =
˜l′
u,τ|U2 −˜lu,τ|U1.
Remark 6.5. By making the base change νk = τ, where k is the denominator of the trace anom-
aly ∆µ, we obtain a section bψ ∈V†
l,⃗λ(FR′) with R′ = C[[ν]] satisfying ∇ν d
dν ( bψ) = 0 (mod OBK bψ).
Moreover, summing over all dominant weights µ ∈Pl we obtain a OBR-linear isomorphism
(the factorization rules, see e.g. [TUY] Theorem 6.2.6 or [U] Theorem 4.4.9)
⊕sµ :
M
µ∈Pl
V†
l,⃗λ,µ,µ†( eF) ⊗OB OBR
∼
−→V†
l,⃗λ(FR).
Hence, the ﬁber over a point b ∈BK has a direct sum decomposition (as K-vector spaces)
(4)
M
µ∈Pl
V†
l,⃗λ,µ,µ†( eF)b ⊗C K
∼
−→V†
l,⃗λ(FK)b.
We denote by D the subgroup of PGL(V†
l,⃗λ(FK)b) consisting of projective K-linear maps
preserving the direct sum decomposition (4) and by pµ : D −→PGL(V†
l,⃗λ,µ,µ†( eF)b ⊗C K) the
projection onto the summand corresponding to µ ∈Pl.
The next proposition is an immediate consequence of the fact that the maps sµ are projec-
tively ﬂat (Proposition 6.2).
11
Proposition 6.6. Let eF and FR be two families of curves as in Proposition 6.1. Then for any
µ ∈Pl and any⃗λ ∈(Pl)n
(1) the monodromy representation of the sheaf of conformal blocks V†
l,⃗λ(FK) over BK takes
values in the subgroup D, i.e.,
ρl,⃗λ : π1(BK, b) −→D ⊂PGL(V†
l,⃗λ(FK)b).
(2) we have a commutative diagram
π1(BK, b)
ρl,⃗λ
−−−→
D
y∼
=
ypµ
π1(B, b)
ρl,⃗λ,µ,µ†
−−−−→PGL(V†
l,⃗λ,µ,µ†( eF)b ⊗C K)
6.3. Proof of the Theorem. We will now prove the theorem stated in the introduction. This
theorem will be a corollary of the following more general result (Theorem 6.7) since we know by
[L] assuming g ≥3 that there is a projectively ﬂat isomorphism between the two projectivized
vector bundles
PZl
∼
−→PV†
l,∅
equipped with the Hitchin connection and the WZW connection respectively. Here V†
l,∅stands
for the sheaf of conformal blocks V†
l,0(F) associated to the family F = (π : C →B; s1) of curves
with one point labeled with the trivial representation λ1 = 0 (propagation of vacua).
Theorem 6.7. Assume that the level l̸ = 1, 2, 4, 8. For the following values of g, n and⃗λ ∈(Pl)n
there exists a family F = (π : C →B; s1, . . . , sn) of smooth connected n-pointed projective curves
of genus g such that the projective monodromy representation ρl,⃗λ of the WZW connection on
the sheaf of conformal blocks
ρl,⃗λ : π1(B, b) −→PGL(V†
l,⃗λ(F)b)
has an element of inﬁnite order in its image:
(1) g ≥0, n = 2m ≥2, g + m ≥2 and⃗λ =⃗12m,
(2) g ≥2, n = 1 and⃗λ = 0.
Proof. We will prove part (1) of the theorem by induction on the genus g and the number of
points 2m. The ﬁrst case g = 0, m = 2 is given by Proposition 5.1: we can take B = M0,4 =
P1
C \ {0, 1, ∞} with the universal family F univ
4
of 4-pointed curves (3). Suppose now that the
theorem holds for curves of genus g = 0 with 2m points. Let F = (π : C →B; s1, . . . , s2m)
be a family of 2m-pointed smooth connected curves of genus 0 having an element of inﬁnite
order in the image of the monodromy representation of V†
l,⃗12m(F). Consider the family eF given
by the disjoint union F ∪F univ
4
, i.e. the family parameterized by B × M0,4 of 2m + 4 marked
curves equal to the disjoint union P1 ∪P1 with 2m marked points s1, . . . , s2m on the ﬁrst P1
and 4 marked points t0, t1, t∞, t on the second P1. We then consider the family F0 of nodal
reducible curves obtained from e
F by identifying the two points s2m(b) ∈P1 and t(b′) ∈P1
for each (b, b′) ∈B × M0,4 as well as a family FR satisfying the conditions of Proposition 6.1.
Then the family FK parameterizes (2m + 2)-marked smooth connected curves of genus 0 and
by the direct sum decomposition (4) the K-vector space V†
l,⃗12m+2(FK)(b,b′) with (b, b′) ∈B×M0,4
12
YVES LASZLO, CHRISTIAN PAULY, AND CHRISTOPH SORGER
contains the direct summand V†
l,⃗12m+2,1,1( eF)(b,b′) ⊗C K corresponding to µ = 1 ∈Pl. Note that
µ† = µ for any dominant weight µ of sl(2). Moreover, by [U] Proposition 3.1.10 we have a
decomposition
V†
l,⃗12m+2,1,1( eF)(b,b′) ∼= V†
l,⃗12m(F)b ⊗V†
l,⃗14(F univ
4
)b′.
By the induction hypothesis V†
l,⃗12m(F)b̸ = {0}. So the monodromy representation of the confor-
mal block V†
l,⃗12m(F) ⊗V†
l,⃗14(F univ
4
) has an element of inﬁnite order in its image (by Proposition
5.1 or by the induction hypothesis). Hence, from Proposition 6.6(2) for µ = 1 we deduce that
the monodromy representation of V†
l,⃗12m+2(FK) also has an element of inﬁnite order in its image.
By induction this shows part (1) of the theorem for g = 0 and any m ≥2.
In order to complete the proof of part (1) we assume that the theorem holds for curves of
genus g with 2k marked points for any k such that g + k ≥2. We take k = m + 1 and let
eF = (eπ : eC →B; s1, . . . , s2m+2) be a versal family of 2m + 2-pointed smooth connected curves
of genus g having an element of inﬁnite order in the image of the monodromy representation
of V†
l,⃗12m+2( eF). We now apply Proposition 6.1 to the family eF. As before, the direct sum
decomposition (4) the K-vector space V†
l,⃗12m(FK)b with b ∈B contains the direct summand
V†
l,⃗12m+2( eF)b⊗CK corresponding to µ = 1 ∈Pl. By the induction hypothesis and by Proposition
6.6(2) for µ = 1, we obtain that the monodromy representation of V†
l,⃗12m(FK) has an element
of inﬁnite order in its image. This proves the statement for 2m-marked curves of genus g + 1
with (g + 1) + m ≥2.
Finally, in order to prove part (2) we shall use the existence of a family eF = (eπ : eC →
B; s1, s2, s3) of 3-pointed smooth curves of genus g ≥1 having an element of inﬁnite order in
the image of the monodromy representation on the conformal block V†
l,⃗λ( eF) with⃗λ = (0, 1, 1).
The existence of such a family is shown by induction exactly as in part (1) starting the induction
with the 5-pointed family
F univ
5
= (π : C = M0,4 × P1 →M0,4; −t, t0, t1, t, t∞)
and the sheaf of conformal blocks V†
l,0,⃗14(F univ
5
). Note that there is a projectively ﬂat isomor-
phism (propagation of vacua, see e.g. [U] Theorem 3.3.1)
V†
l,0,⃗14(F univ
5
)
∼
−→V†
l,⃗14(F univ
4
).
We then apply Proposition 6.1 to the 3-pointed family eF, which produces a 1-pointed family FK
over BK. By the same argument as in part (1) we show that FK has inﬁnite monodromy.
□
References
[AMU]
J.E. Andersen, G. Masbaum, K. Ueno: Topological quantum ﬁeld theory and the Nielsen-Thurston
classiﬁcation of M(0,4), Math. Proc. Cambridge Philos. Soc. 141 (2006), no. 3, 477-488.
[AU1]
J.E. Andersen, K. Ueno: Geometric construction of modular functors from conformal ﬁeld theory,
Journal of Knot theory and its Ramiﬁcations. 16 2 (2007), 127-202.
[AU2]
J.E. Andersen, K. Ueno: Abelian Conformal Field theories and Determinant Bundles, International
Journal of Mathematics, Vol. 18, No. 8 (2007) 919-993.
[AU3]
J.E. Andersen, K. Ueno: Construction of the Reshetikhin-Turaev TQFT from conformal ﬁeld theory.
In preparation.
13
[B1]
A. Beauville: Fibr´es de rang 2 sur une courbe, ﬁbr´es d´eterminant et fonctions thˆeta, Bull. Soc. Math.
France 116 (1988), 431- 448
[B2]
A. Beauville: Fibr´es de rang 2 sur une courbe, ﬁbr´es d´eterminant et fonctions thˆeta II, Bull. Soc.
Math. France 119 (1991), 259-291
[Bel1]
P. Belkale: Strange duality and the Hitchin/WZW connection, J. Diﬀerential Geom. 82 (2009), no. 2,
445-465
[Bel2]
P.
Belkale:
Orthogonal bundles,
theta
characteristics and
the
symplectic
strange
duality,
arXiv:0808.0863
[BHMV] C. Blanchet, N. Habegger, G. Masbaum, P. Vogel: Topological Quantum Field Theories derived from
the Kauﬀman bracket. Topology 34 (1995), 883-927.
[DM]
P. Deligne, D. Mumford: The irreducibility of the space of curves of given genus, Publ. Math. IHES
36 (1969), 75-109
[EFK]
P. Etingof, I. Frenkel, A. Kirillov: Lectures on representation theory and Knizhnik-Zamolodchikov
Equations, Mathematical Surveys and Monographs, Vol. 58, AMS, 1998
[F]
L. Funar: On the TQFT representations of the mapping class group, Paciﬁc J. Math., Vol. 188, No. 2
(1999), 251-274
[HL]
R. Hain, E. Looijenga: Mapping class groups and moduli spaces of curves. In J. Koll´ar, R. Lazarsfeld,
D. Morrison, editors, Algebraic Geometry Santa Cruz 1995, Number 62.2 in Proc. of Symposia in Pure
Math., 97 - 142 (AMS), 1997
[H]
N. Hitchin: Flat connections and geometric quantization, Comm. Math. Phys. 131 (1990), 347-380
[I]
N. Ivanov: Mapping Class Groups, in: Handbook in Geometric Topology, Ed. by R. Daverman and
R. Sher, Elsevier 2001, 523-633
[KT]
Ch. Kassel, V. Turaev: Braid groups, Graduate Texts in Mathematics 247 (2008), Springer, New York
[Ka]
Y. Kanie: Conformal Field Theory and the Braid Group, Bulletin of the Faculty of Education Mie
University 40 (1989), 1-43.
[K]
N. Katz: Algebraic solutions of diﬀerential equations (p-curvature and the Hodge ﬁltration). Invent.
Math. 18 (1972), 1-118.
[L]
Y. Laszlo: Hitchin’s and WZW connections are the same, J. Diﬀerential Geom. 49 (1998), 547-576
[Ma]
G. Masbaum: An element of inﬁnite order in TQFT-representations of mapping class groups, Low-
dimensional topology (Funchal, 1998), 137-139, Contemp. Math., 233, Amer. Math. Soc., Providence,
RI, 1999
[OP]
W.M. Oxbury, C. Pauly: SU(2)-Verlinde spaces as theta spaces on Pryms, Internat. J. Math. 7 (1996),
393-410
[TK]
A. Tsuchiya, Y. Kanie: Vertex operators in two dimensional conformal ﬁeld theory on P1 and mon-
odromy representations of braid groups, Adv. Studies Pure Math., Tokyo, 16 (1988), 297-372
[TUY]
A. Tsuchiya, K. Ueno, Y. Yamada: Conformal Field Theory on Universal Family of Stable Curves
with Gauge Symmetries, Advanced Studies in Pure Mathematics 19 (1989), Kinokuniya Shoten and
Academic Press, 459-566
[U]
K. Ueno: Introduction to conformal ﬁeld theory with gauge symmetries, in Geometry and Physics,
Lecture Notes in Pure and Applied Mathematics 184, Marcel Dekker, 1996, 603-745
[W]
G. Welters: Polarized abelian varieties and the heat equation, Compositio Math. 49 (1983), no. 2,
173-194
´Ecole polytechnique, Centre de Math´ematiques Laurent Schwartz, UMR 7640 ´Ecole polytechnique-
CNRS, 91128 Palaiseau, France
E-mail address: laszlo@math.polytechnique.fr
D´epartement de Math´ematiques, Universit´e de Montpellier II - Case Courrier 051, Place
Eug`ene Bataillon, 34095 Montpellier Cedex 5, France
E-mail address: pauly@math.univ-montp2.fr
Laboratoire de Math´ematiques Jean Leray, Universit´e de Nantes, 2, rue de la Houssini`ere,
BP 92208, 44322 Nantes Cedex 03, France
E-mail address: christoph.sorger@univ-nantes.fr
