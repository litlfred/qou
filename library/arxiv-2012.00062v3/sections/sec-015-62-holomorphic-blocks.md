---
doc_id: arxiv-2012.00062v3
doc_title: "PEACOCK PATTERNS AND RESURGENCE IN COMPLEX CHERN-SIMONS THEORY"
section_id: sec-015-62-holomorphic-blocks
section_title: "Holomorphic blocks"
section_number: 6.2
pages: 47-60
source_pdf: 2012.00062v3.pdf
source_sha256: 2aacb7fa43f5e0da
doc_brief: "PEACOCK PATTERNS AND RESURGENCE IN COMPLEX CHERN-SIMONS THEORY — The partition function of complex Chern-Simons theory on a 3-manifold with torus boundary reduces to a ﬁnite dimensional"
---
state-integral of the52 knot by
Z52,m,µ(u;τ) =
∫
D
Φb(v) Φb(v +u) Φb(v−u) e−2πiv2+2π(mb−µb−1)vdv (240)
for integersm andµ, which agrees with the Andersen-Kashaev invariant of the52 knot when
m = µ = 0. Here the contourD was introduced in (67). It is expressed in terms of three
descendant holomorphic blocks, which we denote byAm, Bm and Cm instead of B
σj
m for
j = 1, 2, 3. For|q|⁄ = 1, Am(x;q), Bm(x;q) and Cm(x;q) are given by
Am(x;q) =H(x,x−1,qm;q) (241a)
Bm(x;q) =θ(−q1/2x;q)−2xmH(x,x 2,qmx2;q) (241b)
Cm(x;q) =θ(−q−1/2x;q)−2x−mH(x−1,x−2,qmx−2;q) (241c)
where H(x,y,z ;qε) :=Hε(x,y,z ;q) for|q|< 1 and ε =± and
H+(x,y,z ;q) = (qx;q)∞(qy;q)∞
∞∑
n=0
qn(n+1)zn
(q;q)n(qx;q)n(qy;q)n
(242a)
H−(x,y,z ;q) = 1
(x;q)∞(y;q)∞
∞∑
n=0
(−1)n q
1
2n(n+1)x−ny−nzn
(q;q)n(qx−1;q)n(qy−1;q)n
. (242b)
Note that the summand ofH+ (a properq-hypergeometric function) equals to that ofH−
after replacingq by q−1. This implies thatH± have a common annihilating idealIH with
respect tox,y,z which can be computed as in the case of Lemma 15.
Thenexttheoremexpressesthedescendantstate-integralsbilinearlyintermsofdescendant
holomorphic blocks.
Theorem 22.(a) The descendant state-integral can be expressed in terms of the descendant
holomorphic blocks by
Z52,m,µ(ub;τ) =(−1)m+µqm/2˜qµ/2
(
e
3πi
4 + 5πi
12 (τ+τ−1)Am(x;q)A−µ(˜x; ˜q−1)
+e−πi
4 +πi
12 (τ+τ−1)Bm(x;q)B−µ(˜x; ˜q−1) + e−πi
4 +πi
12 (τ+τ−1)Cm(x;q)C−µ(˜x; ˜q−1)
)
.
(243)
(b) The functionsAm(x;q), Bm(x;q) and Cm(x;q) are holomorphic functions of|q|⁄ = 1 and
meromorphic functions ofx∈ C ∗ with poles inx∈qZ of order at most2.
(c) Let
Wm(x;q) =


Am(x;q) Bm(x;q) Cm(x;q)
Am+1(x;q) Bm+1(x;q) Cm+1(x;q)
Am+2(x;q) Bm+2(x;q) Cm+2(x;q)

 (|q|⁄ = 1). (244)
For all integersm and µ, state-integralZ52,m,µ(u;τ) and the matrix-valued function
Wm,µ(u;τ) =W−µ(˜x; ˜q−1)∆(τ)Wm(x;q)T, (245)
48 STA VROS GAROUF ALIDIS, JIE GU, AND MARCOS MARIÑO
where
∆(τ) =


e
3πi
4 + 5πi
12 (τ+τ−1) 0 0
0 e −πi
4 +πi
12 (τ+τ−1) 0
0 0 e −πi
4 +πi
12 (τ+τ−1)

 , (246)
are holomorphic functions ofτ∈ C ′ and entire functions ofu∈ C .
Proof. Part (a) follows by applying the residue theorem, just as in the proof of part (a) of
Theorem 14. A similar result was stated in [Dim15].
Part (b) follows from the fact that when|q|< 1, the ratio test implies thatH+(x,y,z ;q) is
an entire function of(x,y,z )∈ C 3 andJ−(x,y,z ;q) is a meromorphic function of(x,y,z )∈
C 2× C with poles atx =qZ and y∈qZ .
For part (c), one uses parts (a) and (b) to deduce thatWm,µ(u;τ) is holomorphic ofτ∈ C′
and meromorphic inu with possible poles of second order atibZ + ib−1Z . An expansion at
these points, done by the method of Section 6.3, demonstrates that the function is analytic
at the pointsibZ + ib−1Z . □
Note that the holomorphic blocks have the symmetry
Am(x−1;q) =Am(x;q), B m(x−1;q) =Cm(x;q), (247)
which implies the symmetry of the matrixWm(x;q)
Wm(x−1;q) =Wm(x;q)


1 0 0
0 0 1
0 1 0

 . (248)
ConsequentlyWm,µ(u;τ) is invariant under the reﬂectionu↦→−u.
Lemma 23.(a) The annihilating ideal ofIH of H± is given by
IJ =⟨yzSx−xzSy + (x2y−xy2)Sz + (−x2y +xy2 +xz−yz), (249)
−xy2S2
z +zSy + (y2 +xy2−qyz)Sz + (−y2−z),−qySySz +Sy− 1,
zS 2
y + (−x +qy +qxy−q2y2−z−qz)Sy +qxySz + (x−qy−qxy +qz)⟩
where Sx, Sy and Sz are the shiftsx to qx, y to qy and z to qz, respectively.
(b) When|q|< 1, we have
H(x,y,z ;q−1) =
det
(
H(x−1,x−1y,x−2z;q) H(y−1,y−1x,y−2z;q)
xH(x−1,x−1y,q−1x−2z;q) yH(y−1,y−1x,q−1y−2z;q)
)
yθ(−q− 1
2x;q)θ(−q− 1
2y;q)θ(−q− 1
2xy−1;q)
. (250)
Proof. Part (a) follows as in the proof of Lemma 15.
For part (b), observe that both sides of the equation are power series inz andq-holonomic
functions of z. Using the HF package, we ﬁnd that the(i,j )-entry of the determinant is
PEACOCK PATTERNS AND RESURGENCE IN COMPLEX CHERN-SIMONS THEORY 49
annihilated by the operatorrij given by
r11 =−yS3
z + (x +y +xy−q2z)S2
z + (−x−x2−xy)Sz +x2
r12 =−xS3
z + (x +y +xy−q2z)S2
z + (−y−xy−y2)Sz +y2
r21 =−yS3
z + (x +y +xy−qz)S2
z + (−x−x2−xy)Sz +x2
r22 =−xS3
z + (x +y +xy−qz)S2
z + (−y−xy−y2)Sz +y2,
whereas the left hand side of (250), after being multiplied by the denominator of the right
hand side, is annihilated by the operator
r =S3
z + (−1−x−y)S2
z + (x +y +xy−qz)Sz−xy. (251)
Using the commandsDFiniteTimes and DFiniteTimes, we computed a 9th order operator
R (which is too long to type here) that annihilates the determinant, and using the command
OreReduce, we proved that it is a left multiple ofr. It follows that both sides of (250)
satisfy the same 9th order recursion with respect toz, with nonvanishing leading term.
Thus, the identity follows once we prove that the coeﬃcient ofzk in both sides agree, for
k = 0,..., 8. When|q| < 1, the coeﬃcient ofzk in H(x,y,z ;q) (resp., H(x,y,z ;q−1)) is in
(qx;q)∞(qy;q)∞Q (x,y,q )(resp., (x;q)−1
∞ (y;q)−1
∞ Q (x,y,q )), andthisimpliesthattheequality
of the coeﬃcient ofzk in the above identity reduces to an equality on the ﬁeldQ (x,y,q )
of rational functions in three variables. The latter is easy to check fork = 0,..., 8. This
completes the proof of (250). □
The next theorem concerns the properties of the linearq-diﬀerence equations satisﬁed by
the descendant holomorphic blocks.
Theorem 24. (a) They areq-holonomic functions in the variables(m,x ) with a common
annihilating ideal
I52 =⟨P1,P 2,P 3⟩ (252)
where
P1 =x(1−q3x2)(1−qx2−q2x2−q3+mx3 +q3x4)− (1−qx)(1 +qx)(1−qx2)(1−q3x2)Sm (253a)
−x(1−qx)(1 +qx)(1−qx−qx2−q3x2 +q2x3 +q4x3−q3+mx3−q4+mx3 +q4x4−q5x5)Sx
−q4+mx4(1−qx2)S2
x
P2 =x−Sm−xSx +qx2SxSm (253b)
P3 =x(1−q1+m−qx2)− (1−q1+m +x−qx2 +q2+mx2−qx3)Sm (253c)
+ (1−qx2)S2
m +q1+mxSx.
I52 has rank 3 and the three functions form a basis of solutions of the corresponding system
of linear equations.
(b) As functions of an integerm, Am(x;q), Bm(x;q) and Cm(x;q) form a basis of solutions
of the linearq-diﬀerence equationˆB52(Sm,x,q m,q )fm(x;q) = 0 for|q|⁄ = 1 where
ˆB52(Sm,x,q m,q ) = (1−Sm)(1−xSm)(1−x−1Sm)−q2+mS2
m. (254)
(c) The WronskianWm(x;q) of (254), deﬁned in (244), satisﬁes
det(Wm(x;q)) =−θ(−q− 1
2x;q)−2θ(−q− 1
2x2;q) ( |q|⁄ = 1). (255)
50 STA VROS GAROUF ALIDIS, JIE GU, AND MARCOS MARIÑO
(d) The Wronskian satisﬁes the orthogonality relation
W−1(x;q)W−1(x;q−1)T =


1 0 0
0 0 1
0 1 x +x−1

 . (256)
It follows that for all integersm,𝓁
Wm(x;q)W𝓁(x;q−1)T∈ PSL(3, Z [q±,x±]) (257)
(e)Asfunctionsof x, theyformabasisofalinear q-diﬀerenceequation ˆA52(Sx,x,q m,q )fm(x;q) =
0 where
ˆA52(Sx,x,q m,q ) =
3∑
j=0
Cj(x,qm,q )Sj
x, (258)
Sx is the operator that shiftsx to qx and
C0 =−q2+mx2(1−q2x)(1 +q2x)(1−q5x2) (259a)
C1 =(1−qx)(1 +qx)(1−q5x2)×
(1−qx−qx2−q4x2 +q2+mx2 +q3+mx2 +q2x3 +q5x3 +q5x4 +q5+mx4−q6x5) (259b)
C2 =qx(1−q2x)(1 +q2x)(1−qx2)×
(1−q2x−q2+mx−q2x2−q5x2 +q4x3 +q7x3−q5+mx3−q6+mx3 +q7x4−q9x5) (259c)
C3 =q8+mx4(1−qx)(1 +qx)(1−qx2) (259d)
(f) The Wronskian of Equation (258)
Wm(x;q) =


Am(x;q) Bm(x;q) Cm(x;q)
Am(qx;q) Bm(qx;q) Cm(qx;q)
Am(q2x;q) Bm(q2x;q) Cm(q2x;q)

, (|q|⁄ = 1) (260)
satisﬁes
detWm(x;q) =q−5−2mx−5(1−q2x2)(1−qx2)(1−q3x2)θ(−q− 1
2x;q)−2θ(−q− 1
2x2;q). (261)
Proof. SinceAm(x;q),Bm(x;q), andCm(x;q) are given in terms ofq-proper hypergeometric
multisums, it follows from the fundamental theorem of Zeilberger [Zei90, WZ92, PWZ96]
(see also [GL16]) that they areq-holonomic functions in both variablesm and x. Part (a)
follows from an application of theHF package of Koutschan [Kou09, Kou10].
Part (b) follows from theHF package. The fact that they are a basis follows from (c).
For part (c), Equation (254) implies that the determinant of the Wronskian satisﬁes the
ﬁrst order equationdet(Wm+1(x;q)) = det(Wm(x;q)) (see [GK13, Lem.4.7]). It follows that
det(Wm(x;q)) = det(W0(x;q)) with initial condition a function ofx given by
det(W0(x;q)) =−θ(−q− 1
2x;q)−2θ(−q− 1
2x2;q) ( |q|⁄ = 1), (262)
which can be proved in a manner similar to section 5.2. Using Lemma 23 and theHF package
we ﬁnd the following recursion relation for theq-function H(x,y,z ;q) when|q|< 1
xyH(x,y,qz ;q)−(x+y+xy−z)H(x,y,z ;q)+(1+x+y)H(x,y,q −1z;q)+H(x,y,q −2z;q) = 0.
(263)
PEACOCK PATTERNS AND RESURGENCE IN COMPLEX CHERN-SIMONS THEORY 51
It then follows that
Hµ,ν,1(z;q) =H(qµ,qν,z ;q), (264)
Hµ,ν,2(z;q) =z−µH(q−µ,qν−µ,q−2µz;q), (265)
Hµ,ν,3(z;q) =z−νH(q−ν,qµ−ν,q−2νz;q), (266)
are three independent solutions to
qµ+νH(qz;q)− (qµ +qν +qµ+ν−z)H(z;q) + (1 +qµ +qν)H(q−1z;q) +H(q−2z;q) = 0. (267)
The corresponding Wronskian
Wµ,ν(z;q) =


Hµ,ν,1(q−1z;q) Hµ,ν,2(q−1z;q) Hµ,ν,3(q−1z;q)
Hµ,ν,1(z;q) Hµ,ν,2(z;q) Hµ,ν,3(z;q)
Hµ,ν,1(qz;q) Hµ,ν,2(qz;q) Hµ,ν,3(qz;q)

 (268)
satisﬁes the recursion relation (see [GK13, Lem.4.7])
detWµ,ν(z;q) =q−µ−ν detWµ,ν(q−1z;q) (269)
which implies that the determinant ofU(z;q) = zµ+νWµ,ν(z;q) is invariant under the shift
z↦→qz. We can thus identify it with the limitz↦→ 0, which is easy to compute. Since
lim
z↦→0
H(x,y,z ;q) = (qx;q)∞(qy;q)∞, (270)
we have
lim
z↦→0
detU(z;q)
= lim
z↦→0
det


H(qµ,qν,q−1z;q) qµH(q−µ,qν−µ,q−2µq−1z;q) qνH(q−ν,qµ−ν,q−2νqz−1;q)
H(qµ,qν,z ;q) H(q−µ,qν−µ,q−2µz;q) H(q−ν,qµ−ν,q−2νz;q)
H(qµ, eν,qz ;q) q−µH(q−µ,qν−µ,q−2µqz;q) q−νH(q−ν,qµ−ν,q−2νqz;q)


=(qqµ;q)∞(qqν;q)∞(qq−µ;q)∞(qqν−µ;q)∞(qq−ν;q)∞(qqµ−ν;q)∞ det


1 qµ qν
1 1 1
1 q−µ q−ν


=q−µ−ν(1−qµ)(1−qν)(qµ−qν)
× (qqµ;q)∞(qqν;q)∞(qq−µ;q)∞(qqν−µ;q)∞(qq−ν;q)∞(qqµ−ν;q)∞. (271)
We thus have
zµ+ν detWµ,ν(z;q) =−(qµ;q)∞(qq−µ;q)∞(qqν;q)∞(q−ν;q)∞(qqµ−ν;q)∞(qν−µ;q)∞. (272)
Using the substitution
qµ =x−1, q ν =x, z = 1 (273)
in the above equation and cancelling with theθ-prefactors ofBm(x;q)andCm(x;q)we obtain
Equation (262) for|q|< 1. The case for|q|> 1 can be obtained by analytic continuation on
both sides of (262).
52 STA VROS GAROUF ALIDIS, JIE GU, AND MARCOS MARIÑO
For part (d), Equation (256) follows from (250). To see this, let us introduce
~Wm(x;q) =


H(x,x−1,qm;q) xmH(x,x 2,qmx2;q) x−mH(x−1,x−2,qmx−2;q)
H(x,x−1,qm+1;q) xm+1H(x,x 2,qmx2;q) x−m−1H(x−1,x−2,qm+1x−2;q)
H(x,x−1,qm+2;q) xm+2H(x,x 2,qm+2x2;q) x−m−2H(x−1,x−2,qm+2x−2;q)

.
(274)
Then Equation (256) can equally be written as
~W−1(x;q−1) =


1 0 0
0 0 1
0 1 x +x−1


(
~W−1(x;q)−1
)T


1 0 0
0 x−2 0
0 0 x2

, (275)
consisting of 9 scalar equations. Each of these equations is a specialization of (250), some-
times after applying the recursion relation (254).
Observe that Equation (254) written in matrix form, implies that
Wm+1(x;q) =


0 1 0
0 0 1
1 −s(x) s(x)−q2+m

Wm(x;q) (276)
where
s(x) =x +x−1 + 1. (277)
Equation (257) follows from (256) together with (276).
Part (e) follows from theHF package. The fact that they are a basis follows from (f).
For part (f), the ﬁrst and third generators of the annihilating ideal (252), which an-
nihilate Am(x;q), Bm(x;q), Cm(x;q) allow expressing Am(qx;q), Am(q2x;q) in terms of
Am(x;q),Am+1(x;q),Am+2(x;q), and similarly forBm(qjx;q), Cm(qjx;q) (j = 1, 2). It fol-
lows that the Wronskian (260) and the Wronskian (244) are related
Wm(x;q) =Mm(x;q)Wm(x;q) (278)
PEACOCK PATTERNS AND RESURGENCE IN COMPLEX CHERN-SIMONS THEORY 53
where Mm(x;q) is a 3× 3 matrix with entries
(Mm(x;q))1,1 =1, (Mm(x;q))1,2 = 0, (Mm(x;q))1,3 = 0,
(Mm(x;q))2,1 =−q−1−m(1−q1+m−qx2)
(Mm(x;q))2,2 =q−1−mx−1(1−q1+m +x + (−q +q2+m)x2−qx3)
(Mm(x;q))2,3 =−q−1−mx−1(1−qx2)
(Mm(x;q))3,1 =q−5−2mx−3(
1 + (−q +q2+m)x− (q +q2 +q3)x2
+(q2 +q3 +q4−q3+m− 2q4+m−q5+m +q5+2m)x3
+(q3 +q4 +q5)x4 + (−q4−q5−q6 +q5+m +q6+m +q7+m)x5−q6x6 +q7x7)
(Mm(x;q))3,2 =−q−5−2mx−4(1−qx)(1 +qx)
(
1 + (1−q +q2+m)x + (−2q−q3 +q2+m)x2
+(−q +q2−q3 +q4− 2q3+m−q4+m−q5+m +q4+2m +q5+2m)x3
+(q2 + 2q4−q3+m−q4+m−q5+m)x4 + (q4−q5 +q6+m)x5−q5x6)
(Mm(x;q))3,3 =q−5−2mx−4(1−qx)(1 +qx)
(
1−qx− (q +q3)x2
+(q2 +q4−q3+m−q4+m)x3 +q4x4−q5x5)
(279)
After taking determinants on both sides, one ﬁnds that
det(Wm(x;q)) =−q−5−2mx−5(1−qx)(1 +qx)(1−qx2)(1−q3x2) det(Wm(x;q)) (280)
This, together with (255) concludes the proof of (261). □
We now come to Conjecture 5 concerning a reﬁnement of theˆA-polynomial. As in Sec-
tion 5.2, we can use Theorems 22 and 24 to obtain explicit linearq-diﬀerence equations for
the descendant integrals with respect to theu and the m variables, and in doing so, we
will obtain a reﬁnement of theˆA-polynomial. To simplify Equation (129), let us deﬁne a
normalized version of the descendant state-integral
z52,m,µ(u;τ) = (−1)m+µq−m/2˜q−µ/2Z52,m,µ(u;τ). (281)
Our next theorem conﬁrms Conjecture 5 for the52 knot.
Theorem 25. z52,m,k(ub;τ) is aq-holonomic function of (m,u ) with annihilator idealI52
given in (252). As a function ofu(resp.,m) it is annihilated by the operatorsˆA52(Sx,x,q m,q )
(resp., ˆB52(Sm,x,q m,q )) given by (254) and (258), whose classical limit is
ˆA52(Sx,x,q m, 1) =
− (1−x)2(1 +x)2
(
qmx2− (1−x− 2(1−qm)x2 + 2x3 + (1 +qm)x4−x5)Sx
−x(1− (1 +qm)x− 2x2 + 2(1−qm)x3 +x4−x5)S2
x−qmx4S3
x
)
,
(282)
and
ˆB52(Sm,x,q m, 1) = (1−Sm)(1−xSm)(1−x−1Sm)−qmS2
m. (283)
ˆA52(Sx,x, 1, 1) is theA-polynomial of the knot,ˆA52(Sx,x, 1,q ) is the (homogeneous part) of
the ˆA-polynomial of the knot andˆB52(y,x, 1, 1) is the deﬁning equation of the curve (233).
54 STA VROS GAROUF ALIDIS, JIE GU, AND MARCOS MARIÑO
6.3. Taylor series expansion atu = 0. In this section we discuss the Taylor expansion of
the descendant holomorphic blocks and descendant state-integral of the52 knots atu = 0.
Using the deﬁnition ofH(x,y,z ;q) and (161a)–(161b), we ﬁnd
Am(eu;q) = (q;q)2
∞
∞∑
n=0
qn(n+1)+nm
(q;q)3
n
φn(u)φn(−u)
= (q;q)2
∞
(
α(m)
0 (q) +u2α(m)
2 (q) +O(u3)
)
(284)
where
α(m)
0 (q) =H+
0,m(q), (285)
α(m)
2 (q) =
∞∑
n=0
qn(n+1)+nm
(q;q)3
n
(−E(n)
2 (q)), (286)
and
Cm(e−u;q) =Bm(eu;q)
= (1− e−u)−2(q;q)−2
∞φ0(u)−2φ0(−u)−2
∞∑
n=0
qn(n+1)+nm
(q;q)3
n
φn(u)φn(2u)e(m+2n)u
=u−2(q;q)−2
∞
(
β(m)
0 (q) +uβ(m)
1 (q) +u2β(m)
2 (q) +O(u3)
)
(287)
where the coeﬃcients satisfy
β(m)
0 (q) =H+
0,m(q), (288)
β(m)
1 (q) =H+
1,m(q), (289)
β(m)
2 (q) = 1
2H+
2,m(q) +α(m)
2 (q). (290)
Similarly, using the deﬁnition ofH(x,y,z ;q−1), we ﬁnd
Am(eu;q−1) = 1
(1− eu)(1− e−u)(q;q)2
∞
∞∑
n=0
(−1)nq
1
2n(n+1)−nm
(q;q)3
n
~φn(u)~φn(−u)
=−u−2(q;q)−2
∞
(
~α(m)
0 (q) +u2~α(m)
2 (q) +O(u3)
)
(291)
where
~α(m)
0 (q) =H−
0,−m(q), (292)
~α(m)
2 (q) =
∞∑
n=0
(−1)nq
1
2n(n+1)−nm
(q;q)3
n
(
− 1
12 + 2E(0)
2 (q)−E(n)
2 (q)
)
, (293)
PEACOCK PATTERNS AND RESURGENCE IN COMPLEX CHERN-SIMONS THEORY 55
and
Cm(e−u;q−1) =Bm(eu;q−1)
= (1− eu)(1− e2u)−1(q;q)2
∞φ0(u)2φ0(−u)2
∞∑
n=0
(−1)nq
1
2n(n+1)−nm
(q;q)3
n
~φn(u)~φn(2u)e(2n+m)u
= 1
2(q;q)2
∞
(
~β(m)
0 (q) +u~β(m)
1 (q) +u2~β(m)
2 (q) +O(u3)
)
(294)
where the coeﬃcients satisfy
~β(m)
0 (q) =H−
0,−m(q), (295)
~β(m)
1 (q) =−H−
1,−m(q), (296)
~β(m)
2 (q) = 1
2H−
2,−m(q) +~α(m)
2 (q) (297)
Applying these results to the right hand side of (243), as well as using the trick
1
2πi =− 1
12(τE 2(q)−τ−1E2(˜q)), (298)
we ﬁnd theO(1/u2) and O(1/u) contributions from (291) and (294) cancel, and theO(u0)
contributions reproduce (103).
As an application of the above computations, we demonstrate that Theorem 11, especially
(91), (93), as well as the recursion relation (86), can be proved by taking theu = 0 limit of
the analogue identities in Theorem 24.
Using the expansion formulas of holomorphic blocks (284), (287), (291), (294), the Wron-
skians can be expanded as
Wm(eu;q) =
(∑
j=0
W +
m,j(q)uj
)

(q;q)2
∞ 0 0
0 u−2(q;q)−2
∞ 0
0 0 u−2(q;q)−2
∞

, (299)
Wm(eu;q−1) =
(∑
j=0
W−
m,j(q)uj
)

−u−2(q;q)−2
∞ 0 0
0 1
2(q;q)2
∞ 0
0 0 1
2(q;q)2
∞

 (300)
where
W +
m,j(q) =


α(m)
j β(m)
j (−1)jβ(m)
j
α(m+1)
j β(m+1)
j (−1)jβ(m+1)
j
α(m+2)
j β(m+2)
j (−1)jβ(m+2)
j

 (q), W −
m,j(q) =


~α(m)
j ~β(m)
j (−1)j~β(m)
j
~α(m+1)
j ~β(m+1)
j (−1)j~β(m+1)
j
~α(m+2)
j ~β(m+2)
j (−1)j~β(m+2)
j

 (q).
(301)
Note thatα(m)
j (q) =~α(m)
j (q) = 0 if j is odd. Taking the determinant of (299), we ﬁnd
detWm(eu;q) =u−1(q;q)−2
∞ detWm(q) +O(u0) (302)
which together with theu-expansion of the right hand side of (255) leads to the determinant
identity (91). Furthermore, by substituting (299), (300) into the Wronskian relation (256),
56 STA VROS GAROUF ALIDIS, JIE GU, AND MARCOS MARIÑO
we ﬁnd the left hand side reduces to
1
2W−1(q)


0 0 1
0 2 0
1 0 0

W−1(q−1)


0 0 1
0 1 0
1 0 0

 +O(u1), (303)
which together with theu-expansion of the right hand side, leads in the leading order to
(92) form = 1. The more general case follows from the identity ofm = 1 by applying the
recursion relations (86) on the Wronskians.
Finally, from the expression (285),(288) of the leading order coeﬃcientsα(m)
0 (q), β(m)
0 (q),
of Am(eu;q), Bm(eu;q), Cm(eu;q) in the expansion ofu, one concludes that the recursion
relation (86) should be theu = 0 limit of the recursion relation (254) inm, and one can
easily check it is indeed the case.
ϕσ1(τ )
ϕσ2(τ )
ϕσ3(τ )
Figure 10. The singularities in the Borel plane for the seriesϕσj(u;τ) with
j = 1, 2, 3 of knot 52 where u is close to zero.
6.4. Stokes matrices near u = 0. In this section we give a conjecture for the Stokes
matrices of the asymptotic seriesϕ(x;τ).
We only consider the case whenu is not far away from zero, or equivalentlyx not far
away from 1. To be more precise, we focus on realx and constrainx to be in the interval
containing 1 between the two real solutions to the discriminant (236). In this case, there
are mild changes to the resurgent structure discussed in Section 3.2. Each singular point
in Figure 4 splits to a cluster of neighboring singular points as shown in Figure 10. In
particular, each of the six singular pointsιi,j (i⁄=j) splits to a cluster of neighboring three
separated from each other bylogx. We label the four regions separating singularities on
positive and negative real axis and the other singularities byI,II,III,IV (see Figure 11).
In each of the four regions, we have the following the results.
PEACOCK PATTERNS AND RESURGENCE IN COMPLEX CHERN-SIMONS THEORY 57
III
IVIII
Figure 11. Four diﬀerent sectors (and additional two auxiliary regions) in
the τ-plane for Φ(u;τ) of knot 52 with u close to zero.
Conjecture 26.The asymptotic series and the holomorphic blocks are related by (15) with
the diagonal matrix∆(u) as in (246) where the matricesMR(x;q) are given in terms of the
W−1(x;q) as follows
MI(x;q) =W−1(x;q)T


0 0 −1
1 −s(x) 0
0 1 0

, |q|< 1, (304a)
MII (x;q) =W−1(x−1;q)T


0 0 −1
−s(x) 1 0
1 0 0

, |q|< 1, (304b)
MIII (x;q) =W−1(x−1;q)T


0 0 −1
1 1 0
1 0 0

, |q|> 1, (304c)
MIV (x;q) =W−1(x;q)T


0 0 −1
1 1 0
0 1 0

, |q|> 1, (304d)
and wheres(x) is given in (277).
Just as inthe case of the41 knot, theabove conjecturecompletely determines the resurgent
structure of Φ(τ). Indeed, it implies that the Stokes matrices, given by Equations (34)
58 STA VROS GAROUF ALIDIS, JIE GU, AND MARCOS MARIÑO
and (33) are explicitly given by:
S+(x;q) =


0 1 0
0 1 1
−1 0 0

W−1(x−1;q−1)W−1(x;q)T


0 0 −1
1 1 0
0 1 0

 , (305a)
S−(x;q) =


0 −s(x) 1
0 1 0
−1 0 0

W−1(x;q)W−1(x−1;q−1)T


0 0 −1
−s(x) 1 0
1 0 0

 (305b)
for|q|< 1. Note that Equations (233), (234), (235), (238) imply that (one can also see this
from (230))
s(Φσ)(x−1;τ) =s(Φσ)(x;τ) (306)
for anyτ∈ C whenever the asymptotic series is Borel summable. It follows that the Stokes
matrices must be invariant under the reﬂectionπ : x↦→ x−1. Using the property (248)
of Wm(x;q), it is easy to show that the Stokes matrices (305a),(305b) indeed satisfy this
consistency condition.
The q↦→ 0 limit of the Stokes matrices factorizes
S+(x; 0) = Sσ3,σ1(x)Sσ3,σ2(x)Sσ1,σ2(x)
=


1 0 0
0 1 0
−s(x) 0 1




1 0 0
0 1 0
0 s(x) 1




1 s(x) + 1 0
0 1 0
0 0 1

, (307)
S−(x; 0) = Sσ1,σ3(x)Sσ2,σ3(x)Sσ2,σ1(x)
=


1 0 s(x)
0 1 0
0 0 1




1 0 0
0 1 −s(x)
0 0 1




1 0 0
−s(x)− 1 1 0
0 0 1

, (308)
where the non-vanishing oﬀ-diagonal entries ofSσi,σj(x) encode the Stokes constants asso-
ciated to the Borel singularities split fromιi,j. Using the unique factorization Lemma 8 and
the Stokes matrixS from above, we can compute the Stokes constants and the corresponding
PEACOCK PATTERNS AND RESURGENCE IN COMPLEX CHERN-SIMONS THEORY 59
matrixS of Equation (36) to arbitrary order inq, and we ﬁnd that
S+
σ1,σ1 =S+(q)1,1− 1
=(−4−x−2− 3x−1− 3x−x2)q + (−1 +x−3 +x−2 +x2 +x3)q2 +O(q3), (309a)
S+
σ1,σ2 =(4 +x−2 + 3x−1 + 3x +x2)q
+(37 +x−4 + 5x−3 + 16x−2 + 30x−1 + 30x + 16x2 + 5x3 +x4)q2 +O(q3), (309b)
S+
σ1,σ3 =q + (1 +x−1 +x)q2 +O(q3), (309c)
S+
σ2,σ1 =− (4 +x−2 + 3x−1 + 3x +x2)q
−(37 +x−4 + 5x−3 + 16x−2 + 30x−1 + 30x + 16x2 + 5x3 +x4)q2 +O(q3), (309d)
S+
σ2,σ2 =(4 +x−2 + 3x−1 + 3x +x2)q
+(37 +x−4 + 5x−3 + 16x−2 + 30x + 30x + 16x2 + 5x3 +x4)q2 +O(q3), (309e)
S+
σ2,σ3 =− (7 + 2x−2 + 5x−1 + 5x + 2x2)q
−(59 + 2x−4 + 10x−3 + 27x−2 + 49x−1 + 49x + 27x2 + 10x3 + 2x4)q2 +O(q3),
(309f)
S+
σ3,σ1 =−q− (1 +x−1 +x)q2 +O(q3) (309g)
S+
σ3,σ2 =(7 + 2x−2 + 5x−1 + 5x + 2x2)q
+(59 + 2x−4 + 10x−3 + 27x−2 + 49x−1 + 49x + 27x2 + 10x3 + 2x4)q2 +O(q3),
(309h)
S+
σ3,σ3 =0. (309i)
Note that the seriesS+
σ1,σ2 andS+
σ2,σ2 are diﬀerent, even though their ﬁrst few terms are
coincidental. They diﬀer in higher orders, as one can already see in theu = 0 limit in
Section 3.2. The matrixS satisﬁes the symmetry
S+
σi,σj(x;q) =−S+
σϕ(i),σϕ(j)(x;q), i ⁄=j, (310)
withϕ(1) = 2,ϕ (2) = 1,ϕ (3) = 3, and they display the familiar feature that the entries of the
matrixS+(x;q) = (S+
σi,σj(x;q)) (except the upper-left one) are (up to a sign) inN[x±1][[q]].
Similarly we can extract the Stokes constantsS(𝓁,k) (k <0) associated to the singularities
below ιi,j in the lower half plane and assemble intoq−1-seriesS−
σi,σj(x;q−1). We ﬁnd the
relation
S−
σi,σj(x;q) =−S+
σj,σi(x;q), i⁄=j and S−
σi,σi(x;q) = +S+
σϕ(i),σϕ(i)(x;q). (311)
Let us now verify Conjecture 4 for the52 knot. The same logic presented at the end of
Section 5.4 also holds here. From the form of the Stokes matrix (305a) as well as (276),(278),
we immediately conclude that
S+(x;q)
··
=W0(x−1;q−1)·W 0(x;q)T. (312)
Using the uniform notation for all holomorphic blocks
(Bα
52(x;q))α=1,2,3 = (A0(x;q),B 0(x;q),C 0(x;q)), (313)
60 STA VROS GAROUF ALIDIS, JIE GU, AND MARCOS MARIÑO
the right hand side of (312) reads2
W0(x−1;q−1)·W 0(x;q)T =
(∑
α
Bα
52(qjx;q)Bα
52(q−ix−1;q−1)
)
i,j=0,1,2
=
(
Indrot
52 (j−i,q
j+i
2 x;q)
)
i,j=0,1,2
, (315)
reproducing the right hand side of (20) in Conjecture 4. Furthermore, the forms of the
accompanying matrices on the left and on the right are such that the(1, 1) entry ofS+(x;q)
equates exactly the DGG index with no magnetic ﬂux. By explicit calculation,
S+(x;q)1,1 =H(x,x−1, 1;q)H(x−1,x, 1;q−1) +H(x,x 2,x 2;q)H(x−1,x−2,x−2;q−1)
+H(x−1,x−2,x−2;q)H(x,x 2,x 2;q−1)
=1− (x−2 + 3x−1 + 4 + 3x +x2)q + (x−3 +x−2− 1 +x2 +x3)q2 +O(q3).
(316)
The right hand side of the ﬁrst two lines in (316) is the formula for the DGG index given in
[BDP14].
