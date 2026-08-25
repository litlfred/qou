---
doc_id: arxiv-2012.00062v3
doc_title: "PEACOCK PATTERNS AND RESURGENCE IN COMPLEX CHERN-SIMONS THEORY"
section_id: sec-003-14-perturbative-series-and-their-resurgence
section_title: "Perturbative series and their resurgence"
section_number: 1.4
pages: 6-8
source_pdf: 2012.00062v3.pdf
source_sha256: 2aacb7fa43f5e0da
doc_brief: "PEACOCK PATTERNS AND RESURGENCE IN COMPLEX CHERN-SIMONS THEORY — The partition function of complex Chern-Simons theory on a 3-manifold with torus boundary reduces to a ﬁnite dimensional"
---
erties of the asymptotic expansion of the state-integralZM(u;τ). Once we ﬁx an integral
presentation ofZM(u;τ), the critical points of the integrand are described by an aﬃne curve
S deﬁned by a polynomial equation
S :p(x,y ) = 0. (11)
We denote byP the labeling set of the branchesy =yσ(x) ofS. The perturbative expansion
of the state-integral has the form
Φ(x,y ;τ) = e
V (u,v)
2πiτ ϕ(x,y ;τ), ϕ (x,y ;τ)∈ 1√
iδ
Q [x±,y±,δ−1][[2πiτ]] (12)
whereV :S∗→ C /(2πi),S∗ is the exponentiated deﬁned byp(x,y ) = 0 withx = eu,y =−ev
and δ∈ Q (x,y ) is the so-called 1-loop invariant. The asymptotic seriesϕ(x,y ;τ) satisﬁes
ϕ(x,y ; 0) = 1. The 8-th root of unity that appears as a prefactor inφ(x,y ;τ) exactly matches
withoneappearingintheasymptoticsoftheKashaevinvariantnoticedin[GZb, Sec.1]. After
choosing local branches, we deﬁne the vectorϕ(x;τ) = (ϕσ(x;τ))σ∈P = (ϕ(x,yσ(x);τ))σ∈P
of asymptotic series. Recall the vector of holomorphic blocksB(x;q) from (4). We now
discuss the relation between the asymptotics ofB(x;q) when q = e 2πiτ and τ approaches
zero (in sectors) and the Borel resummations(Φ) of the vector of power seriesΦ(x;τ).
The next conjecture summarizes the singularities ofΦ(x;τ) in the Borel plane, the relation
between the asymptotics of the holomorphic blocks with the Borel resummationsθ(Φ)(x;τ)
as well as the properties of the Stockes automorphism matricesS, whose detailed deﬁnition
is given in Section 2.
Conjecture 3.(a) The singularities ofΦσ(x;τ) in the Borel plane are a subset of
{ι(𝓁,k)
σ,σ′ | σ′∈P , k,𝓁∈ Z , k =O(𝓁2)} (13)
where
ι(𝓁,k)
σ,σ′ = V (σ)−V (σ′)
2πi + 2πik +𝓁 logx (σ,σ′∈P , k,𝓁∈ Z ). (14)
In particular, the set of trans-series is labeled by three indices,σ∈P andk,𝓁∈ Z, and they
are of the formΦσ(τ)˜qk˜x𝓁.
(b) On each rayρ in the complement of the singularities ofΦ(x;τ) in Borel plane, there exist
a matrixMρ(˜x; ˜q) with entries inZ [˜x±][[˜q]] such that
∆(τ)B(x;τ) =Mρ(˜x; ˜q)sρ(Φ)(x;τ). (15)
(c) The Stokes matricesS+(x,q ), S−(x,q−1) are given by
S+(x;q)
·
=W−1(x−1;q−1)·W−1(x;q)T, S−(x;q−1)
·
=W−1(x;q)·W−1(x−1;q−1)T (16)
where
·
= means equality up to multiplication on the left and on the right by a matrix in
GL(r, Z [x±]).
(d) The Stokes matrixS uniquely determines the Stokes matrices at each Stokes ray, and
the Stokes constants are integers corresponding to the Donaldson–Thomas invariants in
PEACOCK PATTERNS AND RESURGENCE IN COMPLEX CHERN-SIMONS THEORY 7
[KS11, KS14, KS] and the BPS degeneracies in [GMN10, GMN13].
(e) The Stokes matrices satisfy the inversion relation
S+(x;q)T S−(x−1;q) = 1. (17)
The Stokes automorphism matrix has an interesting connection to physics which we now
discuss. Given a hyperbolic knot K in S3, one can construct a three-dimensionalN = 2
supersymmetric theory TM associated to the knot complementM = S3\K [DGG14] (see
also [TY13]), whose BPS invariants are conjectured to coincide with the Stokes constants of
s(Φ)(x;τ). This conjecture can be made more precise in the following manner. The BPS
invariantsof TM areencodedinthe3D-index IK(m,e )(q)labeledbytwointegers (m,e )called
magnetic and electric ﬂuxes respectively [DGG14]. One can further deﬁne the 3D-index in
the fugacity basis (also known as the rotated index) by [DGG13]
Indrot
K (m,ζ ;q) =
∑
e∈Z
IK(m,e )(q)ζe. (18)
The 3D-index is a topological invariant of hyperbolic 3-manifolds with at least one cusp
(see [GHRS15]). And it can be evaluated using holomorphic blocksBα
K(x;q) by [BDP14]
Indrot
K (m,ζ ;q) =
∑
α
Bα
K(qm/2ζ;q)Bα
K(qm/2ζ−1;q−1). (19)
We have observed the following relation between the Stokes matrix and the rotated 3D-index,
and have proven it for the case of the41 and 52 knots using the explicit formulas for the
Stokes matrices.
Conjecture 4.For every hyperbolic knotK, we have
S+(x;q)
··
=
(
Indrot
K (j−i,q
j+i
2 x;q)
)
i,j=0,1,...
(20)
where
··
= means equality up to multiplication on the left and on the right by a matrix in
GL(r, Z (x,q )). In particular, we ﬁnd
S+
σ1σ1(x;q) = Indrot
K (0,x ;q), (21)
where the equality is exact. This holds true for the41 and the 52 knots.
One consequence of (15) is that (after multiplying both terms of (15) by the inverse of
MR(˜x; ˜q)), we can express the Borel resummation of the factorially divergent seriesΦ(τ)
in terms of descendant state-integrals which are holomorphic functions in the cut plane
C ′ = C \ (−∞, 0].
Another consequence of theq-holonomic module deﬁned by the annihilation idealIM is a
reﬁnement of theˆA-polynomial of a knot as well as a newˆB-polynomial whose classical limit
is new. The reﬁnement comes in the form of a new variableqm where m is the descendant
variable, whose geometric meaning is not understood but might be related to some kind
of quantum K-theory, or perhaps related to the Weil-Gelfand-Zak transform of [AK]. This
reﬁnement does not seem to be directly related to other reﬁnements of theˆA-polynomial, as
those considered in [AV12, FGS13, GLL18]. At any rate, theq-holonomic idealIM contains
unique polynomials ˆAM(Sx,x,q m,q )∈W and ˆBM(Sm,qm,x,q ) (of lowest degree, content-
free) that annihilate the functionszM,m,k(u;τ) in the variables(m,x ).
8 STA VROS GAROUF ALIDIS, JIE GU, AND MARCOS MARIÑO
Conjecture 5.When M =S3\K is the complement of a knotK, then
(a) ˆAM(Sx,x, 1,q )isthehomogeneous ˆA-polynomialoftheknot[Gar04]and ˆAM(Sx,x, 1, 1)
is the A-polynomial of the knot with meridian variablex2 and longitude variable
Sx [CCG+94]
(b) ˆBM(y,x, 1, 1) is the deﬁning polynomial of the curveS.
In theorems 17 and 25 we prove the following.
Theorem 6.Conjecture 5 holds for the41 and 52 knots.
