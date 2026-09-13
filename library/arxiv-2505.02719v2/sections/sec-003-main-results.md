---
doc_id: arxiv-2505.02719v2
doc_title: "On the Palais–Smale condition in geometric knot theory"
section_id: sec-003-main-results
section_title: "Main results"
section_number: null
pages: 4-7
source_pdf: 2505.02719v2.pdf
source_sha256: 1803d10aa55c18cf
---
We start with the Palais–Smale condition for linear combinations of the bending energy (1.1)
with any energy contained in one of the three families (1.2), (1.3), or (1.4). But we have to
shrink slightly3 the range of parameters by requiring in addition to (1.6) that
𝛼𝑝 < 𝑝+2for𝐸 𝛼,𝑝, 𝑝 <3
2𝑞+2forTP (𝑝,𝑞),and𝑝 < 5
6𝑞+1forintM (𝑝,𝑞) (1.9)
to allow for the compact embedding𝐻2↩→𝑊 1+𝑠,𝜚 for each knot energy.
Theorem 1.1 (Bending energy plus knot energy above scale-invariance)Let𝜃 >0,z∈
R𝑛, andF ∈{𝐸𝛼,𝑝,TP(𝑝,𝑞),intM(𝑝,𝑞)}, where the respective combinations of parameters𝛼,
𝑝, and𝑞are chosen as in(1.6)and(1.9). Then the total energyT≔𝐸 b+𝜃Frestricted to
the arclength submanifoldA2
z⊂𝐻 2(R/Z,R𝑛)defined in(1.8)satisfies the (PS)-condition.
Notice that (1.6) excludes the respective scale-invariant energies, whose energy spaces donot
embedcompactlyinto𝐶 1(R/Z,R𝑛). Forexample,theenergyspaceoftheMöbiusenergy𝐸 2,1
is the Hilbert space𝐻
3
2(R/Z,R𝑛). To include this energy as part of the total energy, we use
in our proof a slightly smaller Banach space thatdoesembed into𝐶1 (similarly as in [58] and
[42]).
Theorem 1.2 (Bending energy plus Möbius energy)The total energyT≔𝐸b+𝜃𝐸 2,1 re-
stricted toA2
z satisfies the (PS)-condition for every𝜃 >0andz∈R 𝑛.
We strongly believe that the statement of Theorem 1.1 carries over to all scale-invariant
energies, i.e., to𝐸𝛼,𝑝 for𝛼𝑝=2, toTP (𝑝,𝑞) for𝑝=𝑞+2, and tointM (𝑝,𝑞) for𝑝= 2
3𝑞+1, as
well.
The case of a pure knot energy is harder to handle, and we focus here on the tangent-point
energiesTP(𝑝,2) for𝑝∈(4,5)whose energy space𝐻 1+𝑝−3
2 (R/Z,R𝑛)is a Hilbert space.
Theorem 1.3 (Tangent-point energiesTP(𝒑,2))Letz∈R 𝑛 and𝑝∈(4,5)be fixed and set
𝑠(𝑝)≔ 𝑝−3
2 .(1.10)
Then the tangent-point energyTP(𝑝,2) restricted to the arclength submanifoldA 1+𝑠(𝑝)
z ⊂
𝐻1+𝑠(𝑝)(R/Z,R𝑛)satisfies the (PS)-condition.
3This doesnotchange the respective parameter range for𝐸𝛼,1, or forTP(𝑝,𝑞) andintM(𝑝,𝑞) if𝑞∈(1,2].
4
This result carries over to O’Hara’s energies𝐸𝛼,1 for𝛼∈(2,3)and to the integral Menger
curvaturefunctionalsintM (𝑝,2) for𝑝∈( 7
3, 8
3),whereonehastoreplace(1.10)bytherespective
differentiability index𝑠= 𝛼−1
2 or𝑠= 3
2𝑝−3of the corresponding energy space; see [28]. At
this point, it seems feasible to generalize our methods to the non-Hilbert caseTP(𝑝,𝑞), with
suitable restrictions on𝑝and𝑞. This is currently work in progress (see [29]).
Asanimmediateapplicationofthe(PS)-conditionwecanprovetheexistenceofminimizing
(PS)-sequences and of minimizing knots for the total energiesT=𝐸b+𝜃Fof Theorem 1.1
in any connected component of the arclength submanifold.
Corollary 1.4 (Minimizing knots for total energies)Fix a pointz∈R𝑛 and some𝜃 >0,
and letT=𝐸 b+𝜃Fbe any of the total energies considered in Theorems 1.1 and 1.2. Let
Kbe a connected component of the arclength submanifoldA2
z. Then there are a minimizing
(PS)-sequence and a minimizing knot forT|K. The same statements hold true for the whole
arclength submanifold, i.e., forK=A 2
z.
This result contains the existence results in [71, Theorem 3.1] and [33, Theorem 1.1]4, there
for specific choices of knot energies in pursuit ofelastic knotsin any given knot class. As
mentioned before, connected components ofA2
z correspond to different knot classes as we
show in Theorem 3.9.
For the pure tangent-point energiesTP(𝑝,2), which are even of class𝐶1,1
loc on the underlying
arclength submanifold of the larger Hilbert space𝐻1+𝑠(𝑝)(R/Z,R𝑛), we obtain the analogous
statement.
Corollary 1.5 (Minimizing knots forTP(𝒑,2))Letz∈R 𝑛,𝑝∈(4,5), and𝑠(𝑝)as in(1.10).
LetKbe a connected component of the arclength submanifoldA 1+𝑠(𝑝)
z . Then there are
a minimizing (PS)-sequence and a minimizing knot forTP(𝑝,2)|K. This is also true for
K=A 1+𝑠(𝑝)
z .
Theexistenceofminimizingknotsinprescribedknotclassesunderafixed-lengthconstrainthas
been proven in [15, Theorem 1.3] for the more general energy familyTP(𝑝,𝑞) with parameters
𝑝,𝑞as in (1.6).
If the energies are of class𝐶1,1
loc, then one can apply Hilbert gradient-flow techniques on the
arclength submanifold to find critical points. This was carried out by Okabe and Schrader for
the pure bending energy𝐸b in [51] which inspired the following result. Since at this point,
the necessary Lipschitz-estimates for the first variation are not available foreveryknot energy
considered above, we restrict the following result to the subfamilies of energy functionalsF
with
F=𝐸 2,1,orF∈

intM(𝑝,2) :𝑝∈( 7
3, 8
3)
	
∪

intM(𝑝,𝑝) :𝑝∈(3,6)
	
,
orF∈

TP(𝑝,𝑞) :𝑝,𝑞as in (1.6), (1.9), and𝑞≥2
	
.(1.11)
4The additional symmetry constraint considered in [33, Theorem 1.1] is of lower order and can be omitted to
obtain globalminimizers. Thiswas carried outin [31, Theorem2.1] butthere forthe non-smoothropelength
functional, which can be viewed as the𝐿∞-limit ofTP1/𝑞
𝑞 , or ofM1/𝑝
𝑝 as𝑞or𝑝tends to infinity.
5
Theorem 1.6 (Gradient flow for total energies)Fix𝜃 >0andz∈R 𝑛, setM≔A 2
z, and
consider the restriction eT≔T| M of the total energyT≔𝐸 b+𝜃Fto the arclength
submanifoldMfor any choice ofFin(1.11). Then there is a function𝜙:[0,∞)×M→M
such that𝜙(·,𝛾 0)∈𝐶 1([0,∞),M)for every knot𝛾 0∈M, that solves the Cauchy-Problem
(
d
d𝑡𝜙(𝑡,𝛾 0)=−∇ eT(𝜙(𝑡,𝛾 0))for all𝑡∈[0,∞),
𝜙(0,𝛾 0)=𝛾 0. (1.12)
Thefunction𝑡↦→ eT(𝜙(𝑡,𝛾 0))isstrictlydecreasingon[0,∞)unless𝛾 0isacriticalknotfor eT.
For every𝑡∈[0,∞)the knot𝜙(𝑡,𝛾 0)is ambiently isotopic to𝛾0, and as𝑡→∞the solution
𝜙(𝑡,𝛾 0)subconverges to a critical point𝛾∞ of eT, which is ambiently isotopic to𝛾0 as well.
ThisHilbertgradientflowresultisnew,anditcomplementsthelong-timeexistencetheorems
for the𝐿2-gradient flow of𝐸b+𝐸 2,1 in [40, Theorem 1], as well as the arclength-constrained
𝐿2-gradientflowin[18,Theorem4.13]fortotalenergieswithacertainfamilyofself-repulsive
potentials containing𝐸 2,1.
Note, that for geometric energies, one usually investigates a natural gradient flow with
respect to some geometric metric, often denoted𝐿2(d𝑠), or𝐻 2(d𝑠). However, since we
restrict the𝐻 2-flow (1.12) to the arclength manifold, it coincides with the projected (i.e.
intrinsic)𝐻 2(d𝑠)-gradient flow.
Thesubfamiliesofenergiesin(1.11)containthetangent-pointenergiesTP (𝑝,2) for𝑝∈(4,5).
For these pure knot energies we can also establish long-time existence for the Hilbert gradient
flow and its subconvergence to critical points.
Theorem 1.7 (Gradient flow forTP(𝒑,2))For fixedz∈R 𝑛,𝑝∈(4,5), and𝑠(𝑝)as in(1.10)
setM≔A 1+𝑠(𝑝)
z ⊂𝐻 1+𝑠(𝑝)(R/Z,R𝑛). Then for any given initial knot𝛾0∈Mwe have
long-time existence for the gradient flow(1.12)onMwithin the same knot class[𝛾0](with eT
replaced by the restrictionfTP≔TP (𝑝,2)|M), along whichfTPis strictly decreasing unless the
initialknot𝛾 0 isa fTP-criticalpoint. Moreover,theflowsubconvergestoa fTP-criticalknot𝛾 ∞
of the same knot type as𝛾0 as time tends to infinity.
This result carries over to the integral Menger curvaturesintM(𝑝,2) for𝑝∈( 7
3, 8
3)and to𝐸 𝛼,1
for𝛼∈ (2,3), [28]. In contrast to the long-time existence result for a projected Hilbert-
gradient flow forintM(𝑝,2) in [37, Theorem 1.1] we do not need to project the flow to control
the parametrizations, and we do have subconvergence of the flow to a critical knot. Very
recently, Döhrer in cooperation with the first author proved a Łojasiewicz–Simon inequality,
whichevenleadstofullconvergenceofthe flowforTP (𝑝,2) inTheorem1.7; see[25, Theorem
1.5]. In addition, the gradient flows in Theorems 1.6 and 1.7 preserve symmetries, induced,
forinstance,byagroupofisometriesactingonthearclengthsubmanifold;seeProposition2.5
where we address such symmetries in an abstract setting.
In view of the existing regularity results5 for critical points of knot energies on the open
subset of regular knots under a fixed-length constraint one may ask whether also the more
constrained arclength critical knots obtained in Corollaries 1.4 and 1.5 and Theorems 1.6
5[15, Theorem 1.5], [17, Theorem 4], [16, Theorem 1.2]
6
and1.7aresmooth. WeproveinTheorem3.10inanabstractsettingthatarclengthconstrained
critical knots are actually also critical knots for the more relaxed variational problem of fixed-
length,butundertheassumptionofonemoreorderofdifferentiabilityofthecriticalknot. For
theconcreteenergiestreatedaboveweprovidethisadditionalregularitybycarefullyanalyzing
the additional Lagrange parameter in the variational equation. In fact, we prove full𝐶∞-
smoothnessofcriticalknotsforallnon-negativelinearcombinationsofbendingenergy𝐸 band
tangent-point energiesTP(𝑝,2) including the cases when only one of these energies appears.
Theorem 1.8 (Smoothness of critical points of total energies)LetT𝜈𝜃 ≔𝜈𝐸 b+𝜃TP (𝑝,2)
for𝑝∈(4,5),𝜈,𝜃≥0with𝜈+𝜃 >0, andM∈{A 1+𝑠(𝜈),A 1+𝑠(𝜈)
z }for a fixed pointz∈R 𝑛,
where𝑠(𝜈)=1if𝜈 >0and𝑠(𝜈)=𝑠(𝑝)as in(1.10)if𝜈=0. Then each critical knot𝛾∈M
of the restricted energyT𝜈𝜃|M is of class𝐶∞(R/Z,R𝑛).
If𝜈 >0and𝜃=0, then also𝐸 b-critical immersions with possible self-intersections are
smooth.
Theorem1.8alsoholdsifonereplacesthetangent-pointenergiesTP (𝑝,2) bytheintegralMenger
curvature functionalsintM(𝑝,2) for𝑝∈( 7
3, 8
3), or by O’Hara’s energies𝐸𝛼,1 for𝛼∈(2,3);
see [28]. Critical points of these three energy families are actually also real-analytic, which
follows from Theorem 3.10 and the regularity proofs for the length-constrained critical points
of O’Hara’s energies in [72], or of integral Menger curvature in [63], the methods of which
transfer to the tangent-point energies.
