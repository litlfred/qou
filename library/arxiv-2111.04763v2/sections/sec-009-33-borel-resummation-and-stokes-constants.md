---
doc_id: arxiv-2111.04763v2
doc_title: "RESURGENCE OF CHERN–SIMONS THEORY AT THE TRIVIAL FLAT CONNECTION"
section_id: sec-009-33-borel-resummation-and-stokes-constants
section_title: "Borel resummation and Stokes constants"
section_number: 3.3
pages: 27-37
source_pdf: 2111.04763v2.pdf
source_sha256: 760a7f9794e8baaa
doc_brief: "RESURGENCE OF CHERN–SIMONS THEORY AT THE TRIVIAL FLAT CONNECTION — Some years ago, it was conjectured by the first author that the Chern–Simons perturbation theory of a 3-manifold at the trivial flat"
---
in Section 2.4 to includex-deformation. We analyse the asymptotic expansion asq= e2πiτ
andτ→0ofthe(x,q)-seriespresentedinSection3.2andrelatethemtothe(x,τ)-asymptotic
series given in Section 3.1. For this purpose, it is more convenient to introduce the decorated
(x,q)-series
Cm(x,q) =Cm(x,q),
Am(x,q) = (qx2;q)∞
θ(−q1/2x,q)Am(x,q),
Bm(x,q) =x (qx−2;q)∞
θ(−q1/2x−1,q)Bm(x,q),
(107)
where
θ(x,q) = (−q 1/2x;q)∞(−q1/2x−1;q)∞.(108)
The associated decorated matrixJ(x,q)is given by
Jm(x,q) =


1C m(x,q)C m+1(x,q)
0A m(x,q)A m+1(x,q)
0B m(x,q)B m+1(x,q)


=


1 0 0
0 (qx2;q)∞
θ(−q1/2x;q)2 0
0 0x (qx−2;q)∞
θ(−q1/2x−1;q)2

 Jm(x,q)(109)
and it has
detJ(x,q) := detJ m(x,q) =θ(−q −1/2x2,q)θ(−q 1/2x;q)−2θ(−q1/2x−1,q)−2.(110)
We will focus on the vectorB(x,q)of(x,q)-series
B(x,q) =


C0(x,q)
A0(x,q)
B0(x,q)

,(111)
which is defined for|q|̸= 1and satisfies by
B(x,q−1) =


1 0 0
0 0xdetJ(x,q) −1
0−xdetJ(x,q) −1 0

B(x,q).(112)
We will write
q=e 2πiτ, x=e u (113)
28 STAVROS GAROUFALIDIS, JIE GU, MARCOS MARIÑO, AND CAMPBELL WHEELER
and we will show that the asymptotic expansion ofB(x,q)in the limitτ→0is related to
the vectorΦ(x,τ)of(x,τ)asymptotic series
Φ(x,τ) =


Φ(σ0)(x,τ)
Φ(σ1)(x,τ)
Φ(σ2)(x,τ)

 (114)
with corrections given byB(˜x,˜q)where
˜q=e−2πi/τ,˜x=e u/τ.(115)
ϕ(σ0)(x,τ )
(a)
Λσ0(x)
ϕ(σ1)(x,τ )
(b)
Λσ0(x)
ϕ(σ2)(x,τ )
(c)
Λσ0(x)
Figure 4.Singularities of the Borel transforms ofφ(σj )(x,τ)forj= 0,1,2of
the knot4 1.
The asymptotic seriesΦ(x,τ)can be resummed by Borel resummation. As we have ex-
plained in Section 2.4 the value of the Borel resummation depends on the singularities of the
Borel transform ofΦ(x,τ). The positions of these singular points, denoted collectively as
Λ(x), are smooth functions ofx, and in the limitx= 1they are equal toΛdefined in (34).
Whenxis near 1, which is the regime we will be interested in, each singular pointι(k)
i,j inΛ
splits to a finite set of points located atι(k,ℓ)
i,j :=ι (k)
i,j +ℓlog(x),ℓ∈Z, i.e. they are aligned on
a line and are apart from each other by a distancelog(x). We illustrate this schematically in
Fig. 4. The complex plane ofτis divided to infinitely many cones by rays passing through
these singular points, and the Borel resummation ofΦ(x,τ), denoted bysR(Φ)(x,τ), is only
well-defined within a coneR.
Weconjecturethattheasymptoticexpansioninthelimitq→1ofthevectorof(x,q)-series
B(x,q)can be expressed in terms ofsR(Φ)(x,τ). Furthermore, in each cone, the asymptotic
expansion can be upgraded to exact identities betweenB(x,q)and linear transformation of
Borel resummation ofΦ(x,τ)up to exponentially small corrections characterised by˜qand
˜x= exp(logx
τ ).
RESURGENCE OF CHERN–SIMONS THEORY AT THE TRIVIAL FLAT CONNECTION 29
Conjecture 14.For everyx∼1, every coneR⊂C\Λ(x)and everyτ∈Rwe have
∆′(x,τ)B(x,q) =M R(˜x,˜q)∆(x,τ)sR(Φ)(x,τ),(116)
where
∆′(x,τ) = diag(τ 1/2x1/2−x−1/2
˜x1/2−˜x−1/2,(˜x/x)1/2e
3πi
4 −πi
4 (τ+τ−1),(˜x/x)1/2e
3πi
4 −πi
4 (τ+τ−1)),
∆(x,τ) = diag(τ 1/2x1/2−x−1/2
˜x1/2−˜x−1/2,1,1),
(117)
andM R(˜x,˜q)is a3×3matrix of˜q(resp.,˜q −1)-series ifImτ >0(resp.,Imτ <0) with
coefficients inZ[˜x±1]that depend onR.
III
III IV
Figure 5.Stokes rays and cones in theτ-plane for the 3-vectorΦ(x,τ)of
asymptotic series of the knot41.
To illustrate examples ofMR(˜x,˜q), we pick four of these cones, located slightly above and
belowthepositiveornegativerealaxis, labeledincounterclockwisedirectionbyI,II,III,IV,
cf. Fig. 5.
30 STAVROS GAROUFALIDIS, JIE GU, MARCOS MARIÑO, AND CAMPBELL WHEELER
Conjecture 15.Equation (116) holds in the conesR=I,II,III,IVwhere the matrices
MR(˜x,˜q)are given in terms ofJ−1(˜x,˜q)as follows
MI(˜x,˜q) =J−1(˜x,˜q)


1 0 0
0 0−1
0 1−1

,|˜q|<1,(118a)
MII (˜x,˜q) =


1 0 0
0 0 1
0 1 0

J−1(˜x,˜q)


1 0 0
0 1 0
0 1−1

,|˜q|<1,(118b)
MIII (˜x,˜q) =


1 0 0
0 0−1
0−1 0

J−1(˜x,˜q)


1 ˜x−1−1 0
0−1 0
0 ˜x+ ˜x−1 1

,|˜q|>1,(118c)
MIV (˜x,˜q) =J−1(˜x,˜q)


1 0 ˜x −1−1
0 0−1
0 1 ˜x+ ˜x−1

,|˜q|>1.(118d)
Remark 16.It is sometimes stated in the literature that the Gukov–Manolescu series is
obtained by “resumming” the perturbative seriesΦ(σ0)(x,τ)associated to the trivial connec-
tion, although it is not always clear what “resumming” means in that context. The above
conjecture shows that, generically,C0(x,q)involves the Borel resummation of all perturbative
seriesΦ (σj )(x,τ),j= 0,1,2, as well as non-perturbative corrections in˜q,˜x.
We now discuss the Stokes automorphism of the Borel resummationsR(Φ)(x,τ). The
discussion is similar to the one in Section 2.4. To any singular point of the Borel transform
ofΦ(x,τ)locatd atι (k,ℓ)
i,j , we can associate a local Stokes matrix
Sι(k,ℓ)
i,j
=I+S (k,ℓ)
i,j ˜qk˜xℓEi,j,S (k,ℓ)
i,j ∈Z,(119)
whereE i,j is the elementary matrix with(i,j)-entry 1 (i,j= 0,1,2) and all other entries
zero, andS (k,ℓ)
i,j is the Stokes constant. Let us again assume the locality condition. Then
for any ray of angleθ, the Borel resummations ofΦ(x,τ)withτwhose argument is raised
slightly aboveθ(θ +) or sightly below (θ−) are related by the following formula of Stokes
automorphism
∆(x,τ)s θ+(Φ)(x,τ) =S θ(˜x,˜q)∆(x,τ)sθ−(Φ)(x,τ),S θ(˜x,˜q) =
Y
argι=θ
Sι(˜x,˜q).(120)
Because of the locality condition, we don’t have to worry about the order of product of local
Stokes matrices.
In addition, given two raysρθ+ andρ θ− whose arguments satisfy0< θ +−θ−≤π, we
define the global Stokes matrixSθ−→θ+(˜x,˜q)by
∆(x,τ)s θ+(Φ)(x,τ) =S θ−→θ+(˜x,˜q)∆(x,τ)sθ−(Φ)(x,τ),(121)
RESURGENCE OF CHERN–SIMONS THEORY AT THE TRIVIAL FLAT CONNECTION 31
where both sides are analytically continued smoothly to the same value ofτ. The global
Stokes matrixSθ−→θ+(˜x,˜q)satisfies the factorisation property [GGMn21, GGMn]
Sθ−→θ+(˜x,˜q) =
←Y
θ−<θ<θ+
Sθ(˜x,˜q),(122)
where the ordered product is taken over all the local Stokes matrices whose arguments are
sandwiched betweenθ−,θ + and they are ordered with rising arguments from right to left.
Given (116) with explicit values ofMR(˜x,˜q)forR=I,II,III,IV, in general we can
calculate the global Stokes matrix via
SR→R′(˜x,˜q) =MR′(˜x,˜q)−1·MR(˜x,˜q).(123)
For instance, we find the global Stokes matrix from coneIanti-clockwise to coneIIis
SI→II (˜x,˜q) =


1 0 0
0 1 0
0 1−1

J−1(˜x,˜q)−1


1 0 0
0 0 1
0 1 0

J−1(˜x,˜q)


1 0 0
0 0−1
0 1−1

,|˜q|<1.
(124)
This Stokes matrix has the block upper triangular form


1∗ ∗
0∗ ∗
0∗ ∗

.(125)
Onecanverifythatthe2×2submatrixofS I→II (˜x,˜q)inthebottomrightistheStokesmatrix
in [GGMn21]. In addition we can also extract Stokes constantsS(k,ℓ)
0,j (j= 1,2,k= 1,2,...)
responsible for Stokes automorphisms intoΦ(σ0)(x,τ)from Borel singularities in the upper
half plane, and collect them in the generating series
S+
0,j(˜x,˜q) =
∞X
k=1
X
ℓ
S (k,ℓ)
0,j ˜xℓ˜qk, j= 1,2.(126)
We find
S+
0,1(˜x,˜q) =S+
0,2(˜x,˜q) =˜x−1

−C−1(˜x,˜q) +C0(˜x,˜q)A−1(˜x,˜q) +B−1(˜x,˜q)
A0(˜x,˜q) +B0(˜x,˜q)

=−˜q−(˜x+ ˜x−1)˜q2−(˜x2 + 1 + ˜x−2)˜q3 +....(127)
Similarly, we find the global Stokes matrix from coneIIIanti-clockwise to coneIVis
SIII→IV (˜x,˜q) =


1 0 0
0−1 1
0 1 0

·J−1(˜x,˜q−1)−1·


1 0 0
0 0 1
0 1 0

·J−1(˜x,˜q−1)·


1 0 0
0 1 0
0 1 1

,|˜q|>1.
(128)
It also has the form as (125). This, together with the same phenomenon in the upper
half plane, implies thatΦ (sj )(x,τ)(j= 1,2) form a minimal resurgent structure. The
2×2submatrix ofS III→IV (˜x,˜q)in the bottom right is identical to the Stokes matrix given
in [GGMn21]. We also extract Stokes constantsS(k,ℓ)
0,j (j= 1,2,k=−1,−2,...) responsible
32 STAVROS GAROUFALIDIS, JIE GU, MARCOS MARIÑO, AND CAMPBELL WHEELER
for Stokes automorphisms intoΦ (σ0)(x,τ)from Borel singularities in the lower half plane,
and collect them in the generating series
S−
0,j(˜x,˜q) =
−∞X
k=−1
X
ℓ
S (k,ℓ)
0,j ˜xℓ˜qk, j= 1,2.(129)
And we find
S−
0,2(˜x,˜q) =−S−
0,1(˜x,˜q) =S+
0,1(˜x,˜q−1).(130)
We can also use (123) to compute the global Stokes matrixSIV→I (˜q)and we find
SIV→I =


1 0 1
0 1 ˜x+ 1 + ˜x−1
0 0 1

.(131)
Note that this can be identified asS0, associated to the rayρ0, and it can be factorised as
S0 =S ι0,2Sι1,2,S ι0,2 =


1 0 1
0 1 0
0 0 1

,S ι1,2 =


1 0 0
0 1 ˜x+ 1 + ˜x−1
0 0 1

.(132)
Since the local Stokes matricesSι0,2 andS ι1,2 commute, the locality condition is satisfied.
We read off the Stoke discontinuity formulas
disc0Φ(0)(x,τ) = ˜x1/2−˜x−1/2
x1/2−x−1/2τ−1/2s(Φ(s2))(x,τ),
disc0Φ(1)(x,τ) = (˜x+ 1 + ˜x−1)s(Φ(s2))(x,τ).
(133)
Theyreduceproperlyto(56)inthex→1limit, andthesecondidentityhasalreadyappeared
in [GGMn21].
Finally, in order to compute the global Stokes matrixSII→III (˜q), we need to take into
account that the odd powers ofτ1/2 on both sides of (116) give rise to additional−1factors
when one crosses the branch cut at the negative real axis, and (123) should be modified by
SII→III (˜q) = diag(−1,1,1)MIII (˜q)−1diag(−1,1,1)M II (˜q),(134)
and we find
SII→III =


1 1 0
0 1 0
0−˜x−1−˜x −1 1

.(135)
Similarly this can be identified asSπ associated to the rayρπ and it can be factorised as
Sπ =S ι0,1Sι2,1,S ι0,1 =


1 1 0
0 1 0
0 0 1

,S ι2,1 =


1 0 0
0 1 0
0−˜x−1−˜x −1 1

.(136)
RESURGENCE OF CHERN–SIMONS THEORY AT THE TRIVIAL FLAT CONNECTION 33
Note that the local Stokes matricesSι0,1 andS ι2,1 also commute. We read off the Stokes
discontinuity formulas
discπΦ(0)(x,τ) = 1−˜x
1−x τ−1/2s(Φ(s1))(x,τ),(137)
discπΦ(2)(x,τ) =−(˜x+ 1 + ˜x−1)s(Φ(s1))(x,τ).(138)
Theyreduceproperlyto(61)inthex→1limit, andthesecondidentityhasalreadyappeared
in [GGMn21].
3.4.(u,τ)state-integrals.In parallel to the discussion in Sections 2.6 and 2.7, we now
introduce a new state-integral which depends onτ, but also on a variableu. Let us consider
the state-integral
ZB(u,τ) =− i
2b
sinh(πb−1u)
sinh(πbu)
Z
B
tanh(πb−1v) Φb(−v+ i
2 b−1 +u)
Φb(v− i
2 b−1 +u) e2πiu(v− i
2 b−1)dv,(139)
where the contour of integralBis not specified yet. The integrand reduces to that of (69) in
the limitu→0. For genericb 2∈C′ so thatReb>0, the integrand has the following poles
and zeros
Poles:

±ib
1
2 +m

,±u−ib
1
2 +m

−ib−1n

m,n= 0,1,2,...

Zeros:

±u+ ib
1
2 +m

+ ib−1(1 +n)

m,n= 0,1,2,...

.
(140)
We can choose for the integral the contourAN in the upper half plane that wraps the
following poles, as in the left panel of Fig. 3,
vm = ib
1
2 +m

, m= 0,1,2,...,N−1.(141)
By summing over the residues of these poles, the integral evaluates as follows
ZAN (ub,τ) =
N−1X
n=0
(−1)nq−n(n+1)/2(qx;q) n(qx−1;q)n, x= e u, q= e2πiτ,(142)
where we definedu b =u/(2πb), as in [GGMn, Eqn.(2)]. Whenx=q N this is none other
than the colored Jones polynomial of the knot41
ZAN (iNb,b 2) =J 41
N (q) =
N−1X
n=0
(−1)nq−n(n+1)/2(q1+N;q)n(q1−N;q)n.(143)
Alternatively, we can choose for the integral the contourCas in the right panel of Fig. 3,
which is asymptotic to a horizontal line slightly belowIm(v) = Re(b−1), but deformed near
the origin in such a way that all the poles
v±
m,n =±u−ib
1
2 +m

−ib−1n, m,n= 0,1,2,...(144)
are below the contourC. LetZ(u,τ) :=Z C(u,τ)denote the corresponding state-integral.
Similar to the discussion in Section 2.6, as the integrand has non-trivial contributions from
34 STAVROS GAROUFALIDIS, JIE GU, MARCOS MARIÑO, AND CAMPBELL WHEELER
infinity in the upper half plane, the two integralsZAN (u,τ)andZ(u,τ)are different. On
the other hand, since the integrand does have vanishing contributions from infinity in the
lower half plane, we can smoothly deform the contourCdownwards so thatZ(u,τ)can be
evaluated by summing over residues at the polesv±
m,n, and we find
Z(u,τ) =C 0(x,q) + ˜x−1e
3πi
4 −πi
4 (τ+τ−1)
τ 1/2 A0(x,q)

LA0(˜x,˜q−1) + 1−˜x
2 A0(˜x,˜q−1)

+ ˜x−1e
3πi
4 −πi
4 (τ+τ−1)
τ 1/2 B0(x,q)

LB0(˜x,˜q−1) + 1−˜x
2 B0(˜x,˜q−1)

,(145)
whereLA µ(x,q),LB µ(x,q)are defined as in (101) with Roman lettersA,B,Creplaced by
caligraphic lettersA,B,C. As mentioned above, the change of integration contour imple-
ments the Habiro inversion of [Par]: the integration overAN gives the Habiro series (143),
while the integration overCinvolvesC 0(x,q), which was interpreted in [Par] as an inverted
Habiro series. This contribution comes from the poles−vm in the lower half-plane.
The integralZ(u,τ)can also be identified with the Borel resummation of the perturbative
seriesΦ (σj )(x;τ)forj= 0,1,2. By inverting the matrixM R(˜x,˜q)in (116), we can also
express the Borel resummationsR(Φ)(x,τ)in any coneRin terms of combinations of(x,q)-
and(˜x,˜q)-series, and they can be then compared with the right hand side of (145). For
instance, in the conesIandIVrespectively, we find
Z(u,τ) =s I(Φ(σ0))(x;τ)− ˜x1/2−˜x−1/2
2(x1/2−x−1/2)τ−1/2sI(Φ(σ2))(x;τ),(146a)
=sIV (Φ(σ0))(x;τ) + ˜x1/2−˜x−1/2
2(x1/2−x−1/2)τ−1/2sIV (Φ(σ2))(x;τ).(146b)
This also implies that for positive realτ,
Z(u,τ) =s med(Φ(σ0))(x;τ).(147)
Finally, we can introduce the descendants of the integralZ(u,τ)as follows
Zλ,µ(u,τ) =− i
2b
sinh(πb−1u)
sinh(πbu)
Z
C
tanh(πb−1v) Φb(−v+ i
2 b−1 +u)
Φb(v− i
2 b−1 +u) e2πiu(v− i
2 b−1)−2π(λb−µb−1)vdv.
(148)
The integrand has the same poles and zeros as in (140). To ensure convergence, the contour
Cneeds slight modification: it is asymptotic to a horizontal line slightly belowIm(v) =
1
2 Re(b−1)−|Re(λb−µb −1)|, and it is deformed near the origin in such a way that all
the poles (144) are below the contourC. Similarly, by smoothly deforming the contour
downwards we can evaluate this integral by summing up residues of all the poles in the lower
half plane, and we find
Zλ,µ(u,τ) =(−1) µqλ/2
 
Cλ(x,q) + ˜x−1e
3πi
4 −πi
4 (τ+τ−1)
τ 1/2 Aλ(x,q)

LA−µ(˜x,˜q−1) + 1−˜x
2 A−µ(˜x,˜q−1)

+ ˜x−1e
3πi
4 −πi
4 (τ+τ−1)
τ 1/2 Bλ(x,q)

LB−µ(˜x,˜q−1) + 1−˜x
2 B−µ(˜x,˜q−1)
!
.(149)
RESURGENCE OF CHERN–SIMONS THEORY AT THE TRIVIAL FLAT CONNECTION 35
3.5.AnanalyticextensionofthecoloredJonespolynomial.Inthissectionwediscuss
a Borel resummation formula for the colored Jones polynomial of the41 knot. The latter is
defined by
J 41
N (q) =
N−1X
k=0
(−1)kq−k(k+1)/2(q1+N;q)k(q1−N;q)k.(150)
Letu∼0be in a small neighborhood of the origin in the complex plane. It is related to
x=q N andτby
x= e u, τ= u
2πiN + 1
N.(151)
Thenuis near0, thenxis close to1, which is the regime that we studied in Section 3.3,
andτis close to1/N. Note thatNτ= 1 + u
2πi is the analogue ofn/kin [Guk05], and here
we are considering a deformation from the case ofn/k= 1.
Experimentally, we found that in conesIandIVrespectively, we have
J 41
N (q) =sI(Φ(σ0))(x;τ) + ˜x1/2−˜x−1/2
x1/2−x−1/2τ−1/2sI(Φ(σ1))(x;τ)
−(1 + ˜x)˜x1/2−˜x−1/2
x1/2−x−1/2τ−1/2sI(Φ(σ2))(x;τ)(152a)
=sIV (Φ(σ0))(x;τ) + ˜x1/2−˜x−1/2
x1/2−x−1/2τ−1/2sIV (Φ(σ1))(x;τ)
+ (1 + ˜x−1) ˜x1/2−˜x−1/2
x1/2−x−1/2τ−1/2sIV (Φ(σ2))(x;τ)(152b)
where˜x=e u/τ =e 2πiNu/(u+2πi). This, together with Conjecture 6 implies
J 41
N (q) =smed(Φ(σ0))(x;τ) + ˜x1/2−˜x−1/2
x1/2−x−1/2τ−1/2smed(Φ(σ1))(x;τ)
− ˜x−˜x−1
2
˜x1/2−˜x−1/2
x1/2−x−1/2τ−1/2smed(Φ(σ2))(x;τ),(153)
which is Conjecture 2 for the41 knot.
We now make several consistency checks of the above conjecture. The first is that equa-
tion (153) is invariant under complex conjugation which movesτfrom coneIto coneIV.
The second is that the conjecture implies the Generalised Volume Conjecture. Indeed, in
the limit
N→∞, τ→0,log(x) = 2πiNτfinite (154)
the right hand side of (152a),(152b) are dominated by the first term. If we keep only the
exponential, this is the generalised Volume Conjecture [Mur11, Guk05]. Recall from [Mur11],
the generalised Volume Conjecture reads, foruin a small neighborhood of origin such that
u̸∈πiQ,
lim
N→∞
logJ K
N (exp((u+ 2πi)/N))
N = H(y,x)
u+ 2πi ,(155)
wherex= exp(u+ 2πi)andH(y,x) = Li 2(1/(xy))−Li 2(y/x) + log(x) log(y), withya
solution toy+y −1 =x+x −1−1. By the identificationu+ 2πi = 2πi(Nτ)∼2πi, and since
A(x)is identical withH(y,x)(up to±1), one can check that (152a),(152b) imply (155).
36 STAVROS GAROUFALIDIS, JIE GU, MARCOS MARIÑO, AND CAMPBELL WHEELER
4.The5 2-knot
4.1.A3×3matrix ofq-series.The trace field of the5 2 knot is the cubic field of dis-
criminant−23, with a distinguished complex embeddingσ1 (corresponding to the geometric
representation of5 2), its complex conjugateσ2 and a real embeddingσ3. The5 2 knot has
three boundary parabolic representations whose associated asymptotic seriesφ (σj )(h)for
j= 1,2,3correspond to the three embeddings of the trace field. In [GGMn21] these asymp-
totic series were discussed, and a3×3matrixJ red
m (q)ofq-series was constructed to describe
the resurgence properties of the asymptotic series. The matrixJ red
m (q)is a fundamental
solution to the linearq-difference equation [GGMn21, Eqn.(23)]
fm(q)−3f m+1(q) + (3−q 2+m)fm+2(q)−f m+3(q) = 0(156)
and it is defined by4
Jred
m (q) =


H (2)
m (q)H (2)
m+1(q)H (2)
m+2(q)
H (1)
m (q)H (0)
m+1(q)H (1)
m+2(q)
H (0)
m (q)H (0)
m+1(q)H (0)
m+2(q)

,(|q|̸= 1)(158)
where for|q|<1
H (0)
m (q) =
∞X
n=0
qn(n+1)+nm
(q;q) 3
n
,
H (1)
m (q) =
∞X
n=0
qn(n+1)+nm
(q;q) 3
n

1 + 2n+m−3E (n)
1 (q)

,
H (2)
m (q) =
∞X
n=0
qn(n+1)+nm
(q;q) 3
n

(1 + 2n+m−3E (n)
1 (q))2−3E (n)
2 (q)− 1
6E2(q)

,
(159)
and
H (0)
−m(q−1) =
∞X
n=0
(−1)nq
1
2n(n+1)+nm
(q;q) 3
n
,
H (1)
−m(q−1) =−
∞X
n=0
(−1)nq
1
2n(n+1)+nm
(q;q) 3
n
1
2 +n+m−3E (n)
1 (q)

,
H (2)
−m(q−1) =
∞X
n=0
(−1)nq
1
2n(n+1)+nm
(q;q) 3
n
 1
2 +n+m−3E (n)
1 (q)
2
−3E (n)
2 (q)− 1
12E2(q)

.
(160)
4The matricesJ red
m (q)are related to the WronskiansWm(q)in [GGMn21, GGMn] by
Jred
m (q) =


0 0 1
0 1 0
1 0 0

Wm(q)T.(157)
RESURGENCE OF CHERN–SIMONS THEORY AT THE TRIVIAL FLAT CONNECTION 37
