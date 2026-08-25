---
doc_id: arxiv-2111.04763v2
doc_title: "RESURGENCE OF CHERN–SIMONS THEORY AT THE TRIVIAL FLAT CONNECTION"
section_id: sec-006-24-borel-resummation-and-stokes-constants
section_title: "Borel resummation and Stokes constants"
section_number: 2.4
pages: 12-18
source_pdf: 2111.04763v2.pdf
source_sha256: 760a7f9794e8baaa
doc_brief: "RESURGENCE OF CHERN–SIMONS THEORY AT THE TRIVIAL FLAT CONNECTION — Some years ago, it was conjectured by the first author that the Chern–Simons perturbation theory of a 3-manifold at the trivial flat"
---
totic expansion asq= e 2πiτ →1of the vectorG(q)ofq-series and relate it to the vector
Φ(τ)of the asymptotic series, where
G(q) =


G(2)(q)
G(1)(q)
G(0)(q)

,Φ(τ) =


Φ(σ0)(τ)
Φ(σ1)(τ)
Φ(σ2)(τ)

 (30)
withG (0)(q),G (1)(q)given in (3), and the additional seriesG(2)(q)given in (9).
The three power seriesΦ(σj )(τ),j= 0,1,2can be resummed by Borel resummation. On
the other hand, according to the resurgence theory, the value of the Borel resummation of
an asymptotic power series depends crucially on the argument of the expansion variable. If
the Borel transform of the power series has a singular point located atι, the values of the
Borel resummation of the power series whose expansion variable has an argument slightly
greater and less than the angleθ= argιdiffer by an exponentially small quantity, called
the Stokes discontinuity. Usually the difference is identical with the Borel resummation of
another power series in the theory, a phenomenon called the Stokes automorphism.
In the case of the power seriesΦ(σj )(τ),j= 0,1,2, the singularities of the Borel transforms
ofΦ (σj )(τ),j= 1,2were already studied in [GGMn21, GGMn], and they are located at
Λ(σj ) ={ι j,i + 2πik|i= 1,2,i̸=j, k∈Z}∪{2πik|k∈Z ̸=0}, j= 1,2,(31)
as shown in the middle and the right panels of Fig. 1, while the singularities of the Borel
transform ofΦ (σ0)(τ)are located at (see also [Gar08a, Conj. 4])
Λ(σ0) ={ι 0,i + 2πik|i= 1,2, k∈Z},(32)
RESURGENCE OF CHERN–SIMONS THEORY AT THE TRIVIAL FLAT CONNECTION 13
ι1,2
ϕ(σ1)(τ)
Λ(σ1)
ι2,1
ϕ(σ2)(τ)
Λ(σ2)
ι0,2ι0,1
ϕ(σ0)(τ)
Λ(σ0)
Figure 1.Singularities of the Borel transforms ofφ (σj )(τ)forj= 0,1,2of
the knot4 1.
as shown in the left panel of Fig. 1, where
ιj,i = V(σj)−V(σ i)
2πi , i,j= 0,1,2.(33)
All the raysρθ (Stokes rays) passing through the singularities in the union
Λ =∪ j=0,1,2Λ(σj ),(34)
form a peacock pattern, cf. Fig. 2, and they divide the complex plane of Borel transform
into infinitely many cones. The Borel resummation of the vectorΦ(τ)is only well-defined
within one of these cones.
Recall that the Borel transformbφ(ζ)of a Gevrey-1 power seriesφ(τ)
φ(τ) =
∞X
n=0
anτn, a n =O(C nn!),(35)
is defined by
bφ(ζ) =
∞X
n=0
an
n!ζn.(36)
If it analytically continues to anL 1-analytic function along the rayρ θ := e iθR+ where
θ= argτ, we define the Borel resummation by the Laplace integral
sθ(φ)(τ) =
Z ∞
0
bφ(τζ)e−ζdζ= 1
τ
Z
ρθ
bφ(ζ)e−ζ/τ dζ.(37)
The Borel resummation of the trans-seriesΦ(τ) = e
V
2πiτφ(τ)is defined to be
sθ(Φ)(τ) = e
V
2πiτsθ(φ)(τ).(38)
In the following we will also use the notationsR(Φ)(τ)when the argument ofτis in the cone
Rand it is a continuous function ofτ.
14 STAVROS GAROUFALIDIS, JIE GU, MARCOS MARIÑO, AND CAMPBELL WHEELER
III
III IV
Figure 2.Stokes rays and cones in theτ-plane for the 3-vectorΦ(τ)of as-
ymptotic series of the knot41.
Coming back to the vector ofq-seriesG(q), we find that the asymptotic expansion ofG(q)
whenq=e 2πiτ andτ→0in a coneRcan be expressed in terms ofΦ(τ). Moreover, this
asymptotic expansion can be lifted to an exact identity betweenq-seriesG(j)(q)and linear
combinations of Borel resummation ofΦ (σj )(τ)multiplied by power series in˜q= e −2πiτ−1
(thought of as exponentially small corrections) with integer coefficients. This is the content
of the following conjecture.
Conjecture 5.For every coneR⊂C\Λand everyτ∈R, we have
∆′(τ)G(q) =M R(˜q)∆(τ)sR(Φ)(τ),(39)
where
∆′(τ) = diag(τ 3/2,τ 1/2,τ−1/2),∆(τ) = diag(τ 3/2,1,1),(40)
andM R(˜q)is a3×3matrix of˜q(resp.,˜q −1)-series ifImτ >0(resp.,Imτ <0) with integer
coefficients that depend onR.
As in [GGMn21, GGMn], we pick out in particular four of these cones, located slightly
above and below the positive or the negative real axis, labeled in clockwise direction by
I,II,III,IVas indicated in Fig. 2. We work out the exact matricesM R(˜q)in these four
cones.
RESURGENCE OF CHERN–SIMONS THEORY AT THE TRIVIAL FLAT CONNECTION 15
Conjecture 6.Equation (39) holds in the conesR=I,II,III,IVwhere the matrices
MR(˜q)are given in terms ofJ−1(˜q)as follows
MI(˜q) =J−1(˜q)


1 0 0
0 0−1
0 1−1

,|˜q|<1,(41a)
MII (˜q) =


1 0 0
0−1 0
0 0 1

 J−1(˜q)


1 0 0
0 1 0
0 1−1

,|˜q|<1,(41b)
MIII (˜q) =


1 0 0
0−1 0
0 0 1

 J−1(˜q)


1 1 0
0−1 0
0 2 1

,|˜q|>1,(41c)
MIV (˜q) =J−1(˜q)


1 0 1
0 0−1
0 1 2

,|˜q|>1.(41d)
We now discuss the Stokes automorphism. To any singularity in the Borel plane located
atι (k)
i,j :=ι i,j + 2πik, we can associate a local Stokes matrix
Sι(k)
i,j
(˜q) =I+S (k)
i,j ˜qkEi,j,S (k)
i,j ∈Z,(42)
whereE i,j is the elementary matrix with(i,j)-entry 1 (i,j= 0,1,2) and all other entries
zero, andS (k)
i,j is the Stokes constant. Let us assume thelocalitycondition that no two Borel
singularities share the same argument, or if there are, their Stokes matrices commute. This
is indeed the case in our example. Then for any ray of angleθ, the Borel resummations of
Φ(τ)withτwhose argument is raised slight above (θ +) or lowered sightly below (θ−)θare
related by the following formula of Stokes automorphism
∆(τ)sθ+(Φ)(τ) =S θ(˜q)∆(τ)sθ−(Φ)(τ),S θ(˜q) =
Y
argι=θ
Sι(˜q).(43)
Because of the locality condition, we don’t have to worry about the order of the product of
local Stokes matrices.
More generally, consider two raysρθ+ andρ θ− whose arguments satsify0<θ +−θ−≤π,
we define the global Stokes automorphism
∆(τ)sθ+(Φ)(τ) =S θ−→θ+(˜q)∆(τ)sθ−(Φ)(τ),(44)
where both sides are analytically continued smoothly to the same value ofτ. The global
Stokes matrixSθ−→θ+(˜q)satisfies the factorisation property [GGMn21, GGMn]
Sθ−→θ+(˜q) =
←Y
θ−<θ<θ+
Sθ(˜q),(45)
where the ordered product is taken over all the local Stokes matrices whose arguments are
sandwiched betweenθ−,θ + and they are ordered with rising arguments from right to left.
16 STAVROS GAROUFALIDIS, JIE GU, MARCOS MARIÑO, AND CAMPBELL WHEELER
Given (39) with explicit values ofMR(˜q)forR=I,II,III,IV, in general we can calculate
the global Stokes matrix via
SR→R′(˜q) =MR′(˜q)−1·MR(˜q).(46)
Here in the subscript of the global Stokes matrix on the left hand side,Rstands for any ray
in the cone. For instance, we find that the global Stokes matrix from coneIanti-clockwise
to coneIIis
SI→II (˜q) =


1 0 0
0 1 0
0 1−1

 J−1(˜q)−1


1 0 0
0−1 0
0 0 1

 J−1(˜q)


1 0 0
0 0−1
0 1−1

,|˜q|<1.(47)
This Stokes matrix has the block upper triangular form


1∗ ∗
0∗ ∗
0∗ ∗

.(48)
Let us note that this form implies thatΦ (σj )(τ)(j= 1,2) form a closed subset under
Stokes automorphisms (this was called in [GMn] a “minimal resurgent structure”). They are
controled by the2×2submatrix ofS I→II (˜q)in the bottom right and one can verity that it
is indeed the Stokes matrix in [GGMn21]. In addition we can also extract Stokes constants
S (k)
0,j (j= 1,2,k= 1,2,...) responsible for Stokes automorphisms intoΦ (σ0)(τ)from Borel
singularities in the upper half plane, and collect them in the generating series
S+
0,j(˜q) =
∞X
k=1
S (k)
0,j ˜qk, j= 1,2.(49)
We find
S+
0,1(˜q) =S+
0,2(˜q) =−G(2)
0 (˜q)−G(2)
1 (˜q) +

G(0)
0 (˜q) +G(0)
1 (˜q)

G(2)
0 (˜q)/G(0)
0 (˜q)
=−˜q−2˜q2−3˜q3−7˜q4−14˜q5−34˜q6 +....(50)
Similarly, we find that the global Stokes matrix from coneIIIanti-clockwise to coneIV
is
SIII→IV (˜q) =


1 0 0
0−1 1
0 1 0

·J−1(˜q−1)−1·


1 0 0
0−1 0
0 0 1

·J−1(˜q−1)·


1 0 0
0 1 0
0 1 1

,|˜q|>1.
(51)
It also has the form as (48), and the2×2submatrix ofS III→IV (˜q)in the bottom right
is the Stokes matrix given in [GGMn21]. We also extract Stokes constantsS(k)
0,j (j= 1,2,
k=−1,−2,...) responsible for Stokes automorphisms intoΦ (σ0)(τ)from Borel singularities
in the lower half plane, and collect them in the generating series
S−
0,j(˜q) =
−∞X
k=−1
S (k)
0,j ˜qk, j= 1,2.(52)
RESURGENCE OF CHERN–SIMONS THEORY AT THE TRIVIAL FLAT CONNECTION 17
We find
S−
0,2(˜q) =−S−
0,1(˜q) =S+
0,1(˜q−1).(53)
We can also use (46) to compute the global Stokes matrixSIV→I (˜q)and we find
SIV→I =


1 0 1
0 1 3
0 0 1

.(54)
Note that this can be identified asS0 associated to the rayρ0 and it can be factorised as
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
0 1 3
0 0 1

.(55)
Since the local Stokes matricesSι0,2 andS ι1,2 commute, the locality condition is satisfied.
We read off the Stoke discontinuity formulas
disc0Φ(0)(τ) =τ −3/2s(Φ(s2))(τ),
disc0Φ(1)(τ) = 3s(Φ (s2))(τ),
(56)
with
discθΦ(τ) =s θ+(Φ)(τ)−s θ−(Φ)(τ),(57)
and the second identity has already appeared in [GH18, GGMn21].
Finally, in order to compute the global Stokes matrixSII→III (˜q), we need to take into
account that the odd powers ofτ1/2 on both sides of (39) give rise to additional−1factors
when one crosses the branch cut at the negative real axis, and (46) should be modified by
SII→III (˜q) = diag(1,−1,−1)MIII (˜q)−1·MII (˜q),(58)
and we find
SII→III =


1 1 0
0 1 0
0−3 1

.(59)
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
0−3 1

.(60)
Note that the local Stokes matricesSι0,1 andS ι2,1 also commute. We read off the Stokes
discontinuity formulas
discπΦ(0)(τ) =τ −3/2s(Φ(s1))(τ),
discπΦ(2)(τ) =−3s(Φ (s1))(τ),
(61)
where the second identity has already appeared in [GGMn21].
18 STAVROS GAROUFALIDIS, JIE GU, MARCOS MARIÑO, AND CAMPBELL WHEELER
