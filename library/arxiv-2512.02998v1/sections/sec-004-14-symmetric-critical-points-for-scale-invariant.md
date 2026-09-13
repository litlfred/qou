---
doc_id: arxiv-2512.02998v1
doc_title: "STABILITY OFKNOT EQUIVALENCE AT LOW REGULARITY, AND SYMMETRIC CRITICAL KNOTS FOR THEMÖBIUS ENERGY"
section_id: sec-004-14-symmetric-critical-points-for-scale-invariant
section_title: "Symmetric critical points for scale-invariant knot energies"
section_number: 1.4
pages: 4-5
source_pdf: 2512.02998v1.pdf
source_sha256: 146ff93cd70baad4
doc_brief: "STABILITY OFKNOT EQUIVALENCE AT LOW REGULARITY, AND SYMMETRIC CRITICAL KNOTS FOR THEMÖBIUS ENERGY — We present sufficient criteria for the equivalence of tame knots at low regularity."
---
spaceW
3
2,2(R/Z,R 3) is the natural energy space for theM¨ obius energy
(1.5)E M¨ ob(γ) :=
ˆ
R/Z
ˆ
R/Z
 1
|γ(s)−γ(t)| 2− 1
dγ(γ(s),γ(t)) 2

|γ′(s)||γ′(t)|dsdt.
Indeed, an arclength parametrized curveγ:R/Z→R 3 has finite M¨ obius energy if and only
ifγis embedded and of classW
3
2,2(R/Z,R 3) as shown in [2] (see [23, Theorem 3.2 (i)] for an
explicit a priori bound on the fractional seminorm in terms of the energy). Freedman et al.
managed to use the M¨ obius invariance ofE M¨ obto find minimizing knots in any given prime
knot class [21, Theorem 4.3]. Critical points of the M¨ obius energy were shown to be smooth and
even real-analytic [5, 8] without using the invariance ofE M¨ obunder M¨ obius transformations.
But how can we find critical knots possibly different from the absolute minimizers? One option
is to use symmetry as carried out in [23] for O’Hara’s energies above scale-invariance whose
energy spacesdoembed intoC 1.
As in that paper we consider here for the M¨ obius energy a discrete rotational symmetry. To
be more precise, forp∈N,p≥2, we call a curveγ∈C 0(R/Z,R 3)(p-rotationally) symmetric
if and only if
(1.6) Rot 2π
p
◦γ(s− 1
p) =γ(s) for alls∈R/Z,
where Rotβ∈SO(3) denotes the rotation about a fixed axis, say, thee 3-coordinate axis, with
rotation angleβ. Define for a given knot equivalence classKthe(p-rotationally) symmetric
subset
(1.7) Σ p(K) :={η∈C 0,1(R/Z,R 3) :|η′|>0 a.e.,[η] =K, ηsatisfies (1.6)}.
STABILITY OF KNOT EQUIV ALENCE AND SYMMETRIC CRITICAL KNOTS 5
Theorem 1.6(Symmetric critical prime knots).If the symmetric subsetΣ p(K)of a prime knot
equivalence classKcontains a knot with finite M¨ obius energy or, equivalently, aW 3/2,2-knot,
then there exists an arclength parametrized knotγ∈C ω(R/Z,R 3)∩Σ p(K)such that
(1.8)E M¨ ob(γ) = inf
Σp(K)
EM¨ ob(·),
andγis a critical knot, i.e.,dE M¨ ob(γ)[h] = 0for allh∈W
3
2,2(R/Z,R 3). Moreover, all torus
knot classesT(a,b)for co-primea,b∈Z\{0,±1}contain at least two different critical knots
for the M¨ obius energy.
One may prove a similar result for other scale-invariant knot energies with energy spaces
W 1+1/p,p such as those from O’Hara’s family; cf. [6,33].
It might be easier to check the symmetries for polygonal curves, so instead of a knot with finite
M¨ obius energy we might require in Theorem 1.6 that Σp(K) contains a polygonal knot. Indeed,
smoothing the corners such that the symmetry is preserved yields an immersed embedded
smooth curve in Σ p(K) which has finite M¨ obius energy due to [2] and the energy’s invariance
under reparametrization. We do not know, on the other hand, if it suffices to assume in Theorem
1.6 only thatKis tame and that Σ p(K) is nonempty.
We mentioned before that two equivalent arclength parametrized tame knotsγ 1,γ 2 :R/Z→
R3 are either already ambiently isotopic, orγ 1 is ambiently isotopic to the mirror imageγ ∗
2 of
γ2. TheO(3)-invariance of the M¨ obius energy therefore allows us to strengthen Theorem 1.6
to ambient isotopy classes.
Corollary 1.7(Symmetric critical prime knots in ambient isotopy classes).LetKbe an ambient
isotopy class of prime knots andΣ p(K)be the class ofp-rotationally symmetric regular Lipschitz
curves whose ambient isotopy class equalsK. IfΣ p(K)contains a knot of finite M¨ obius energy,
then there is an arclength parametrized minimizing real analytic knot inΣ p(K)such that(1.8)
holds, and this knot isE M¨ ob-critical. If, more specifically,Kequals the ambient isotopy class of
torus knots,T(a,b)for co-primea,b∈Z\{0,±1}, then there are at least two suchE M¨ ob-critical
knots.
Kim and Kusner use in [27] symmetric criticality to constructE M¨ ob-critical torus knots (even
with explicit formulas for their energy values). Their numerical experiments suggest, that for
(co-prime) parametersa,bwith|a|,|b|>2 these critical points seize to be stable. Analytically,
this remains an open question.
