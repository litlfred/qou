---
doc_id: arxiv-1803.04009v2
doc_title: "Symmetry enhancement and closing of knots in 3d/3d correspondence"
section_id: sec-007-32-su3-enhancement
section_title: "SU(3) enhancement"
section_number: 3.2
pages: 33-38
source_pdf: 1803.04009v2.pdf
source_sha256: 8b34299b739cd2b0
toc_source: outline
doc_brief: "Symmetry enhancement and closing of knots in 3d/3d correspondence — We revisit Dimofte-Gaiotto-Gukov’s construction of 3d gauge theories asso- ciated to 3-manifolds with a torus boundary."
---
SU(3) enhancement
From the point of view of 6d N = (2, 0) theories, we only expect that the symmetry
associated to codimension-2 defects (which are knots in 3-manifolds) are su(2). However,
we will see that there are many theories which have larger symmetry enhancement.
We consider a pair of (N, A; B) and (N′, A′; B′) such that
1) A is of SO(3) type while A′ is of SU(2) type ,
2) I(A,B)
N
(m, e; x) = I(A′,B′)
N′
(m, e; x) ,
3) Both of A and A′ are non-closable cycles .
(3.19)
which we call SU(3)-enhancement pair. The I(A,B)
N
in 2) denotes a topological invariant
called 3d index, see Appendix A. For such a pair, we claim that
I. Two theories T DGG[N, XA] and T DGG[N′, XA′] are identical
possibly modulo a topological sector
II. The theory has enhanced SU(3) ﬂavor symmetry where SO(3)A and SU(2)A′ are
embedded into the SU(3) in a way that 3SU(3) →3SO(3)A and 3SU(3) →(2 ⊕1)SU(2)A′ .
(3.20)
The 3d index I(A,B)
N
(x) is equivalent to the superconformal index of T DGG[N, XA] in charge
basis. For hyperbolic complement N, the index is a non-trivial power series in x. The non-
trivial match of the superconformal indices in the 2nd condition strongly suggests that two
theories are actually equivalent possibly up to a topological sector.
From 1st and 3rd conditions in (3.19), the theory T DGG[N, XA] = T DGG[N′, XA′] has
both of SU(2)A and SO(3)A′ symmetry where the U(1)XA = U(1)X′
A is embedded into
them as 2SU(2) = (±1)U(1) and 3SO(3) = (±1, 0)U(1) respectively. The only consistency
way of this happening is that the theory has a SU(3) symmetry into which the SU(2)A
and SO(3)A′ are embedded as II in (3.20). The reason is that the SU(2)A enhancement
requires that there are conserved currents with charge ±2 under U(1)XA from oﬀ-diagonal
components of SU(2)A, while the SO(3)A′ enhancement requires that there are conserved
currents with charge ±1 under U(1)X′
A. Then the conserved currents with charge ±1 from
SO(3)A′ is a doublet of SU(2)A. A minimal completion of such a situation to a Lie algebra
is to embed the symmetries to the SU(3) algebra.
One may wonder if there exits such a pair. Surprisingly, we can ﬁnd inﬁnitely many
examples of these pairs. A class of examples is
N = (S3\52
1)µ1+kλ1 ,
A = µ2 ,
B = 2µ2 + λ2
N′ = (S3\52
1)(4k+1)µ1−kλ1 ,
A′ = 2µ2 −λ2 ,
B′ = µ2 −λ2 .
(3.21)
As shown in ﬁg. 5, the N above are nothing but twist knots which will be denoted as Kk.
Let us check that the pair satisfy the 3 conditions in (3.19). First, note that both of N and
N′ can be considered as a knot complement in Z2-homological spheres, L(1, k) = (N)µ2
and L(4k −1, −k) = (N′)µ2 respectively. Applying (3.9) with µ = µ2 and λ = λ2, we
– 32 –
µ2 + kλ2
k −twist
=
k −twist
....
....
| k | -copy
{
=
, k > 0
, k < 0
Figure 5. A rational surgery calculus [41] shows that (S3\52
1)µ2+kλ2 is a twist knot Kk. For
example, Kk=1 = 41, Kk=−2 = 52 and Kk=2 = 61.
can conclude that A/A′ is of SO(3)/SU(2) type. Now let us check the 2nd condition in
(3.19). Combining the D8-symmetry (A.27) of the Whitehead link index I52
1 (A.26) and
the following polarization transformation rules of 3d index
I(−λ1,µ2;µ1,2µ2+λ2)
S3\52
1
(m1, m2, e1, e2; x) = I52
1(e1, m2, −m1, e2 −m2; x)
I(4µ1−λ1,2µ2−λ2;µ1,λ2−µ2)
S3\52
1
(m1, m2, e1, e2) = I52
1(e1, 2m2 + e2, 2e1 −m1, m2 + e2; x)
(3.22)
and the following matrix multiplication (S2 is a generator of the D8 in (A.27))





e1
2m2 + e2
2e1 −m1
m2 + e2





(e1,e2)→(−e1,−e2)
= S2 ·





e1
m2
−m1
e2 −m2





(3.23)
we have following identity
I(−λ1,µ2;µ1,2µ2+λ2)
S3\52
1
(m1, m2, e1, e2; x) = I(4µ1−λ1,2µ2−λ2;µ1,λ2−µ2)
S3\52
1
(m1, m2, −e1, −e2; x) .
(3.24)
Applying the Dehn ﬁlling formula in eq. (A.21) to the above equality,
I(µ2;2µ2+λ2)
(S3\52
1)µ1+kλ1(m2, e2; x) = I(2µ2−λ2;λ2−µ2)
(S3\52
1)(4k+1)µ1−kλ1(m2, −e2; x) ,
⇒I(µ2;2µ2+λ2)
(S3\52
1)µ1+kλ1(m2, e2; x) = I(2µ2−λ2;µ2−λ2)
(S3\52
1)(4k+1)µ1−kλ1
(m2, e2; x) ,
for all k ∈Z .
(3.25)
we conﬁrm 2) in (3.19). In the above, we use the transformation rule of 3d index under the
orientation reversal in (A.6). Finally, from the following topological facts [42]
NA = (S3\52
1)µ1+kλ1,µ2 = L(1, k) ,
(N′)A′ = (S3\52
1)(4k+1)µ1−kλ1,2µ2−λ2 = L(−8k −2, −2k −1) ,
(3.26)
– 33 –
we see that both of A and A′ are non-closable cycles according to (3.6). So we conﬁrm that
the pair, (N, A) and (N′, A′), in (3.21) satisfy all the conditions in (3.19) and the correspond-
ing DGG theory is expected to have SU(3) ﬂavor symmetry. We will check the ehancement
explicitly for k = 1, −2 by explicitly constructing T DGG[N, A] and T DGG[N′, A′].
For k = 1
In the case,
(S3\52
1)µ1+λ1 = (S3\41) = m004 ,
(S3\52
1)5µ1−λ1 = (Sister of S3\41) = m003 .
(3.27)
m003 is a knot complement called sister of ﬁgure-eight knot complement. Both 3-manifolds
have the same hyperbolic volume and are the smallest hyperbolic 3-manifolds with one
cusp torus boundary.
From ideal triangulations of m003 and m004 given below, their
orientation are ﬁxed. The equality in the above means not only that the two manifolds
are homeomorphism but also that they have the same orientation, i.e. the orientation of
m004 is same as the orientation induced from a Dehn ﬁlling on S3\52
1, whose orientation
is induced from an ideal triangulation in (A.25).
According to SnapPy, both can be ideally triangulated by two tetrahedra and have
common internal edge variables given in (2.62) while boundary variables are diﬀerent by a
factor 2 or 1/2
aµ2 = Z1 −Z2 ,
bλ2+2µ2 = 4Z1 −2Z′
1 −2Z2 ,
for m004 .
a2µ2−λ2 = 2Z1 −2Z2 ,
bµ2−λ2 = 2Z1 −Z′
1 −Z2 ,
for m003 .
(3.28)
For DGG’s construction, we choose
Xµ2 = aµ2 ,
P2µ2+λ2 = 1
2b2µ2+λ2 ,
for m004 .
X2µ2−λ2 = 1
2a2µ2−λ2 ,
Pµ2 = bµ2−λ2 ,
for m003 .
(3.29)
Thus, both DGG theories are identical and described by the Lagrangian in (2.69) up to
background CS level for U(1)X which is irrelevant in symmetry enhancement. We reproduce
the Lagrangian here with the modiﬁed background CS level;
LT DGG[m004,Xµ2;P2µ2+λ2](VX, VC) = LT DGG[m003,X2µ2−λ2;Pµ2−λ2](VX, VC)
= 1
4π
Z
d4θ

−1
2ΣCVX + Σ(2VC + 3VX) + ΣXVX

+
Z
d4θ

Φ†
1eV + VX
2 Φ1 + Φ†
2eV −VX
2 Φ2

.
(3.30)
So the theory is
T DGG[m004, µ2] = T DGG[m003, 2µ2 −λ2]
= A U(1) vector multiplet coupled to 2 chirals of charge +1 .
(3.31)
The theory has manifest u(1)top×su(2)manifest where u(1)top is the topological monopole
charge of the u(1)gauge gauge symmetry, and su(2)manifest acts on the two chiral ﬁelds. This
u(1)top × su(2)manifest will be enhanced to SU(3).
– 34 –
The u(1)C ﬂavor symmetry associated to the background ﬁeld VC corresponds to the
topological symmetry u(1)top and will be embedded to SU(3) as
u(1)C = u(1)top = T8 := diag(−1/3, −1/3, 2/3) ∈SU(3) .
(3.32)
This is because the “oﬀ-diagonal components” of SU(3) (which are not in u(1)C×su(2)manifest)
are provided by monopole operators with monopole charge ±1 = ±(1/3 −(−2/3)).
On the other hand, the VX is coupled to the system as follows. Let
T3 := diag(1/2, −1/2, 0) .
(3.33)
be the Cartan generator of the manifest su(2)manifest. The VX is coupled to the chiral ﬁelds
via this generator T3. Also, notice that VX is coupled to the monopole current Σ with
coeﬃcients 3/2. Therefore the u(1)X is embedded in SU(3) as
u(1)X = 3
2T8 + T3 = diag(0, −1, 1) ∈SU(3) .
(3.34)
This u(1)X must be enhanced to su(2)X because the A-cycle is non-closable.
Notice that this su(2)X is diﬀerent from the manifest su(2)manifest symmetry. Therefore,
if u(1)X is enhanced to su(2)X, then the u(1)top×su(2)manifest must be enhanced to SU(3).
This agrees with our general discussion that this theory has enhanced SU(3) symmetry.
The superconformal index of theory is
Im003/m004(u1, u2; x)
=
X
(e1,e2)∈Z2
(−x
1
2 )e2I∆(−e2, −e1 + 2e2; x)I∆(−e2, e1 −e2; x)ue1
1 ue2
2 .
(3.35)
Here u1 and u2 fugacity variable for u(1)X and u(1)C symmetry respectively. The index de-
pends on the choice of R-charge mixing between u(1)R and u(1)C. In the above expression,
we in particularly choose12,
R(Φa) = 1
3,
R(V±) = 2
3 .
(3.36)
Here V± denote a BPS monopole operator of charge ±1. Then the index show the SU(3)
structure :
Im003/m004(u1, u2; x) = 1 −(χ1,1)x −(χ0,0 + χ1,1)x2 + (χ2,2 −χ0,0 −χ1,1)x3
+ (χ3,0 + χ2,2 + χ0,3 −χ0,0)x4 + (χ0,3 + 2χ1,1 + 2χ2,2 + χ3,0)x5 + . . .
(3.37)
Here χm,n(u1, u2) is the character of SU(3)-representation with Dynkin labels (m, n). The
correct IR R-charge mixing should be determined by F-maximization, but the non-trivial
appearance of the SU(3) in a particular choice strongly suggests that the choice gives the
correct R-charge assignment. The ﬁrst non-trivial terms comes form operators listed in the
Table below. In the table, φa and (ψ±)a denote the scalar and fermionic ﬁelds in chiral ﬁeld
12In general, R-charge of BPS monopole operators V+, V−of charge ±1 are related to the R-charges of
chiral multiplets Φa as R(V±) = 1
2
P qa(1 −R(Φa)) where qa is the u(1)gauge charge of Φa.
– 35 –
u(1)C
u(1)X
SCI contribution
φa(ψ∗
+)b
0
±1
2 ± 1
2
−(2 + u1 + 1
u1 )x
V−(φa)
1
(1, 2)
−(u1u2 + u2
1u2)x
V+(φa)
−1
(−1, −2)
−(
1
u2
1u2 +
1
u1u2 )x
Φa respectively with a = 1, 2. V±(. . .) denote a gauge invariant BPS monopole operator
of charge ±1 dressed by matter ﬁelds (. . .). All these operators have quantum numbers
(R, j3, ∆) = (1, 1
2, 3
2) and form descents of conserved current multiplet for SU(3) ﬂavor
symmetry. In 3d N = 2 SCFT, a conserved current multiplet of ﬂavor group F consists of
following operators in the adjoint representation of F:
[0](0)
∆=1
Q, ˜Q
−−−→[1
2](1)
∆= 3
2 ⊕[1
2](−1)
∆= 3
2
Q, ˜Q
−−−→[1](0)
∆=2 ⊕[0](0)
∆=2
(3.38)
Here operators are denoted by its quantum number [j](r)
∆where j denote a spin of space-time
rotational symmetry su(2) in a normalization such that [1/2] corresponds to the fundamen-
tal representation.
For k = −2
In the case,
(S3\52
1)µ1−2λ1 = S3\52 = m015; ,
(S3\52
1)−7µ1+2λ1 = m017 .
(3.39)
Both manifolds have the same hyperbolic volume vol(m015) = vol(m017) = 2.82812 . . ..
According to SnapPy, both can be ideally triangulated by three tetrahedra and have com-
mon internal edge variables
C1 = Z′
1 + Z′′
1 + 2Z2 + Z′
3 + Z′′
3 ,
C2 = Z1 + Z′
1 + Z′
2 + Z3 + Z′
3 ,
C3 = Z1 + Z′′
1 + Z′
2 + 2Z′′
2 + Z3 + Z′′
3 .
(3.40)
while boundary variables are diﬀerent by a factor 2 or 1/2
aµ2 = −Z1 + Z2 ,
b−2µ2−λ2 = 2(2Z1 −Z′′
1 −2Z2 + Z′′
3 ) ,
for m015 .
a2µ2−λ2 = −2Z1 + 2Z2 ,
bλ2−µ2 = 2Z1 −Z′′
1 −2Z2 + Z′′
3 ,
for m017 .
(3.41)
We choose
Xµ2 = aµ2 ,
P−2µ2−λ2 = 1
2b−2µ2−λ2 ,
for m015 .
X2µ2−λ2 = 1
2a2µ2−λ2 ,
Pµ2 = bλ2−µ2 ,
for m017 .
(3.42)
– 36 –
Then, the Sp(6, Z)+(aﬃne-shifts) are









X
C1
C2
P
Γ1
Γ2









= gm0015/m017 ·









Z1
Z2
Z3
Z′′
1
Z′′
2
Z′′
3









+ iπνm015/m017
gm015/m017 =









−1 1
0
0
0
0
−1 2 −1 0
0
0
0 −1 0 −1 −1 −1
2 −2 0 −1 0
1
0
0
0
0
0 −1
0
1
0
0
0
0









,
νm015/m017 =









0
−2
−3
0
0
0









(3.43)
The matrix gm015/m017 can be decomposed into gm015/m017 = gs
Jm015gt
Km015ggl
Um015 (2.43)
Um015 =



−1 1 0
−1 2 −1
0 1 0


,
Km015 =



−2 0 0
0 0 0
0 0 1


,
Jm015 =



0 0 0
0 0 0
0 0 1


.
(3.44)
Using the decomposition, we have
LT DGG[m015,Xµ2;P−2µ2−λ2](VX, VC1, VC2) = LT DGG[m017,X2µ2−λ2;Pλ2−µ2](VX, VC1, VC2)
= 1
4π
Z
d4θ
 −3ΣXVX + ΣXVC1 −1
2(ΣC1 −Σ)(VC1 −V ) + 2ΣVC2

+
Z
d4θ
 Φ†
1eV −VXΦ1 + Φ†
2eV Φ2 + Φ†
3eV +VX−VC1Φ3

.
(3.45)
Here V is a dynamical u(1) vector multiplet. Since C1 and C2 are hard internal edges and
we can not add OC1 and OC2 to superpotential. So, the DGG theory is
T DGG[m015, µ2] = T DGG[m017, 2µ2 −λ2]
= A u(1)−1/2 vector multiplet coupled to 3 chirals of charge +1 .
(3.46)
The theory has manifest SU(3) ﬂavor symmetry rotating 3 chrials as expected.
