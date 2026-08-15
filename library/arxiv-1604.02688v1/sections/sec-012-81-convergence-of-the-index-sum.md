---
doc_id: arxiv-1604.02688v1
doc_title: "THE 3D-INDEX AND NORMAL SURFACES"
section_id: sec-012-81-convergence-of-the-index-sum
section_title: "Convergence of the index sum"
section_number: 8.1
pages: 21-27
source_pdf: 1604.02688v1.pdf
source_sha256: bdcafe379519287c
doc_brief: "THE 3D-INDEX AND NORMAL SURFACES — Dimofte, Gaiotto and Gukov introduced a powerful invariant, the 3D-index, associated to a suitable ideal triangulation of a 3-manifold with torus boundary"
---
(as a formal Laurent series) we need to examine the lowest degree of the terms in this sum.
Given any coset[S] =S + T, we can choose its “minimal non-negative coset representative”
S∗. Explicitly, given
S = (a1,b 1,c 1,a 2,b 2,c 2,...,a n,bn,cn)∈Q(T; Z)
we have
S∗ = (a∗
1,b∗
1,c∗
1,a∗
2,b∗
2,c∗
2,...,a ∗
n,b∗
n,c∗
n),
where (a∗
j,b∗
j,c∗
j) = (aj−mj,bj−mj,cj−mj) and mj = min{aj,bj,cj}.
NowJ(S∗) has leading termq
1
2δ(S∗) of degree 1
2δ(S∗). So each surface[S] occurring in the
index sum (29) contributes a termI([S]) = (−q1/2)−χ(S∗)J(S∗) of lowestq1/2-degree
d([S]) =d(S∗) =−χ(S∗) +δ(S∗) (32)
and leading coeﬃcient(−1)−χ(S∗).
Remark 8.5. Note thatS∗ need not give an embedded normal surface, but there areat most
two non-zero quad coordinates in each tetrahedron. In the next section we will show how to
replace such a normal class by a uniqueembedded generalised normal surface˜S.
From this, it is easy to analyse the convergence of the index sums. First we give a new
proof that the sumI0
T(0) converges (as formal Laurent series) if and only ifT contains no
embedded normal surfaces of Euler characteristic≥ 0.
Theorem 8.6.The index sum forI0
T(0) converges (as a formal Laurent series) if and only
if the triangulationT is 1-eﬃcient.
22 STA VROS GAROUF ALIDIS, CRAIG D. HODGSON, NEIL R. HOFFMAN, AND J. HYAM RUBINSTEIN
Proof. (⇒) If the triangulationT is not 1-eﬃcient then it contains a closed embedded normal
surface with non-negative Euler characteristic. Doubling this, if necessary, gives a closed
embedded normal surfaceS∈Q0(T; Z+) withχ(S)≥ 0,δ(S) = 0 andS∗ =S⁄= 0. Then for
each integerk≥ 0, (kS)∗ =kS contributes a term to the sum (31) forI0
T(0) withq1/2-degree
d(kS) =−kχ(S)≤ 0. So the index sum cannot converge as a formal Laurent series inq1/2.
(⇐) Assume thatT is a 1-eﬃcient ideal triangulation. First we note the following general
fact.
Lemma 8.7.The functiond =−χ +δ :Q(T; R+)→ Z is superadditive, i.e.
d(S +S′)≥d(S) +d(S′).
Henced(∑
iniSi)≥∑
id(niSi)≥∑
inid(Si) for allSi∈Q(T; R+) and all integersni≥ 0.
Proof. This follows sinceχ is a linear function andδ(S +S′)≥ δ(S) +δ(S′) provided all
quad coordinates ofS and S′ are non-negative. □
Nextweobservethat N(T; Z+)isthesetofintegerpointsinaconedeﬁnedbyhomogeneous
linear inequalities with integer coeﬃcients. So we can choose a set offundamental solutions
(or Hilbert basisin integer linear programming theory)F1,...,F m forN(T; Z+). This means
that everyS∈N(T; Z+)can written (not necessarily uniquely) as a ﬁnite sumS =∑m
i=1niFi
where ni ∈ Z+ and each Fi is irreducible, i.e. has no decomposition Fi = x +y where
x,y∈N(T; Z+) and x,y⁄= 0.
Now considerfi(x) =d(xFi) =−χ(Fi)x +δ(Fi)x2, wherex≥ 0. Since T is 1-eﬃcient, for
each i = 1,...,m , we have either (i)δ(Fi) = 0 and−χ(Fi)≥ 1, or (ii)δ(Fi)≥ 1. Hence
fi(x)→∞ as x→ +∞, and in fact there are constantsai,bi∈ R with ai > 0 such that
fi(x)≥aix−bi for allx≥ 0.
Then eachS∈N(T; Z)can be written as a linear combinationS =∑m
i=1xiFi withxi∈ Z+
and, using Lemma 8.7, itsq1/2-degree satisﬁes
d(S)≥
m∑
i=1
d(xiFi)≥
∑
i
(aixi−bi).
Thus, d(S)≤ D implies∑
iaixi≤ D +∑
ibi, which has only ﬁnitely many solutions with
xi∈ Z+. HenceI0
T(0) converges as a formal Laurent series. □
A similar argument gives the following
Theorem 8.8. If T is 1-eﬃcient, thenIa
T(b) converges for alla and b; in fact∑
aIa
T(b) is
convergent for allb.
Proof. We may assume thatb⁄= 0. Now consider the set Qb(T; Z+) of Q-normal classes
S∈Q(T; Z+) whose boundary∂S is a non-negative integer multiple ofb. This is the set of
integer points in a cone deﬁned by a set of homogeneous linear equations and inequalities
with integer coeﬃcients, so we can choose a ﬁnite setF1,...,F m of fundamental solutions
for Qb(T; Z+) where ∂Fi =sib with si∈ Z+.
Given S∈ Qb(T; Z+) we can writeS =∑xiFi where xi∈ Z+ and ∂S = (∑sixi)b. Let
I :={1, 2,...,m } and writeI =I0∪I1 whereI0 ={i∈I :si = 0} andI1 ={i∈I :si≥ 1}.
THE 3D-INDEX AND NORMAL SURF ACES 23
Then S = S0 +S1 where S0 =∑
i∈I0xiFi and S1 =∑
i∈I1xiFi and ∂S = b if and only if∑
i∈I1sixi = 1. SoS1 belongs to the ﬁnite set{Fi :i∈I1 and si = 1}, andS0∈N(T; Z).
As in the proof of Theorem 8.6 there are constantsai,bi ∈ R with ai > 0 such that
d(xiFi)≥aixi−bi for eachi∈I1. Now
d(S)≥d(S1) +d(S0)≥d(S1) +
∑
i∈I1
d(xiFi)≥d(S1) +
∑
i∈I1
(aixi−bi).
Hence given anyD≥ 0 there are at most ﬁnitely manyS∈ Qb(T; Z+) with ∂S = b and
d(S)≤D. This implies the result. □
Theorem 8.9.If T is spun 1-eﬃcient, i.e. contains no embedded spun normal surfaceS⁄= 0
with χ(S)≥ 0, then the “total index”Itot
T =∑
all (a,b)Ia
T(b) converges.
Proof. LetF1,...,F m be a set of fundamental solutions for the setQ(T; Z+) of non-negative
integer solutions to the Q-matching equations.
Now considerfi(x) =d(xFi) =−χ(Fi)x+δ(Fi)x2, wherex≥ 0. Since T is spun 1-eﬃcient,
for eachi = 1,...,m , we have either (i)δ(Fi) = 0 and−χ(Fi)≥ 1, or (ii)δ(Fi)≥ 1. Hence
fi(x)→∞ as x→ +∞, and in fact there are constantsai,bi∈ R with ai > 0 such that
fi(x)≥aix−bi for allx≥ 0.
Then eachS∈Q(T; Z) can be written as a linear combinationS =∑m
i=1xiFi withxi∈ Z+
and, using Lemma 8.7, itsq1/2-degree satisﬁes
d(S)≥
m∑
i=1
d(xiFi)≥
∑
i
(aixi−bi).
Thus, d(S)≤ D implies∑
iaixi≤ D +∑
ibi, which has only ﬁnitely many solutions with
xi∈ Z+. Hence the total index sum converges. □
Theorem 8.10.Every 1-eﬃcient ideal triangulation of an anannular 3-manifold other than
the solid torus or solid Klein bottle is spun 1-eﬃcient.
Proof. This follows by a simple barrier argument. For more details see Jaco-Rubinstein
[JR03] and Section 10.3. Assume that T is a 1-eﬃcient triangulation of an anannular 3-
manifold M, which is not spun 1-eﬃcient. So there is an embedded spun normal surface
S with χ(S)≥ 0 in M. Clearly then S is a Möbius band, annulus or disk. IfS is a disk,
M must be a solid torus or solid Klein bottle, which are excluded by assumption. SoS
must be an annulus or Möbius band. On the other hand, ifS is an annulus or Möbius
band, sinceM is anannular,S must be topologically boundary parallel, so is contained in
a collar of a boundary component ofM. (The Möbius band case only occurs ifM is non-
orientable and the corresponding cusp is a Klein bottle). We can then push the appropriate
boundary surface across this collar to give a torus or Klein bottleT which is boundary
parallel. Moreover the product region bounded byT and a cusp containsS.
Wenowwishtoconstructabarrierusing S. ChooseanormaltorusorKleinbottle T0 which
consists entirely of triangular disks and is parallel to the cusp in the previous paragraph.
We can assume thatS and T0 are chosen to intersect transversely.S∪T0 separates M into
various regions, with one such regionR homeomorphic toM. The boundary ofR contains
a ‘piecewise normal’ torus or Klein bottle and this is a barrier for normalisation of surfaces
24 STA VROS GAROUF ALIDIS, CRAIG D. HODGSON, NEIL R. HOFFMAN, AND J. HYAM RUBINSTEIN
in R in the sense of Jaco-Rubinstein [JR03]. So we can normalise the essential torus or
Klein bottleT0 inR to give an embedded normal torus or Klein bottle which is not normally
peripheral, contradicting the assumption thatT is 1-eﬃcient. □
Remark 8.11. A 1-eﬃcient ideal triangulation of an (open) solid torus can contain an em-
bedded spun normal disk. In fact this happens in Example 11.1 below.
A discussion of angle structures and angle structure with rotational holonomy zero on each
peripheral curve follows in Appendix A.
Corollary 8.12.If T admits a strict angle structure with rotational holonomy zero on each
peripheral curve, then it is spun 1-eﬃcient. In particular, this applies to any geometric
triangulation of a cusped hyperbolic 3-manifold.
Proof. The Euler characteristic of any embedded spun normal surfaceS can be calculated as∑
q∈□−α(q)/π, ifα : □→ (0,π ) is an generalised angle structure with rotational holonomy
zero on each peripheral curve. Ifα is a strict angle structure then the sum is negative, unless
S = 0. □
Example 8.13. The 2-tetrahedron triangulation T of the trefoil knot complement in Ex-
ample 11.2, is not spun 1-eﬃcient. HereI0
T(xµ +yλ) =δ0,x+6y forx∈ Z,y∈ 1
2 Z so the total
index∑
x,yI0
T(xµ +yλ) diverges.
8.2. Non 1-eﬃcient ideal triangulations.When the triangulation T is not 1-eﬃcient,
it turns out that the seriesIa
T(b) may converge for someb⁄= 0 even when the seriesI0
T(0)
diverges. See Example 11.4 below. The following result gives an obstruction to convergence.
Lemma 8.14.Assume that an ideal triangulationT contains a Q-normal classS∈Q(T; Z+)
with [S]2 = a and ∂S satisfying [∂S] = b, and there is a closed normal surface0⁄= S′∈
N(T; Z+) such thatS′ is embedded and−χ(S′)+2δ(S,S′)≤ 0. Then the index sum forIa
T(b)
diverges.
Proof. By replacingS′ by 2S′, if necessary, we can assume thatS′∈ Q0(T; Z+). Then for
allk∈ Z+, the normal classSk =S +kS′ contributes a term in the index sum (30) forIa
T(b)
with q1/2-degree
d(Sk) =−χ(S +kS′) +δ(S +kS′)
=−χ(S)−kχ(S′) +δ(S) + 2kδ(S,S′) +k2δ(S′)
=d(S) +k (−χ(S′) + 2δ(S,S′)) +k2δ(S′). (33)
Hence d(Sk) remains bounded above ask→ +∞ if δ(S′) = 0 and−χ(S′) + 2δ(S,S′)≤ 0.
Thus the index sum diverges. □
In general, we have the following converse.
Theorem 8.15. Assume that an ideal triangulationT does not contain a Q-normal class
S ∈ Q(T; Z+) with ∂S = b, and a closed normal surfaceS′ ∈ N(T; Z+) such that S′ is
embedded and−χ(S′) + 2δ(S,S′)≤ 0. Then the index sumIa
T(b) converges.
THE 3D-INDEX AND NORMAL SURF ACES 25
Proof. We start by following the proof of Theorem 8.8. This shows that there exist ﬁnitely
many normal classesS1,...,S k∈ Q(T; Z+) with ∂Si = b and ﬁnitely many normal classes
F1,...,F m∈ Q(T; Z+) with ∂Fi = 0 such that everyS∈ Qb(T; Z+) with ∂S = b can be
written as
S =Sj +
m∑
i=1
xiFi, where 1≤j≤k and xi∈ Z+.
Now
d(S) =d(Sj) +
∑
i
(−χ(Fi) + 2δ(Fi,Sj))xi +
∑
i,j
δ(Fi,Fj)xixj
≥d(Sj) +
∑
i
(−χ(Fi) + 2δ(Fi,Sj))xi +δ(Fi)x2
i.
For eachi∈ I0 we have, by assumption, eitherδ(Fi)≥ 1 or−χ(Fi) + 2δ(Fi,S 1)≥ 1 so it
follows that
fi(x) := (−χ(Fi) + 2δ(Fi,S 1))x +δ(Fi)x2
is bounded below forx≥ 0 and approaches +∞ as x→ +∞. Since there are only ﬁnitely
possibilities forS1, it follows that there are only ﬁnitely manyS∈Qb(T; Z) such that∂S =b
and d(S)≤D. Hence the index sum forIa
T(b) converges. □
Remark 8.16. (1) Whenb = 0 this reduces to Theorem 8.6, as we can takeS = 0 in the
above theorem.
(2) If the triangulationT is 0-eﬃcientthen Theorem 8.15 simpliﬁes to the following:
Ia
T(b) converges if and only if T does not contain a Q-normal classS ∈ Q(T; Z+)
with ∂S = b, and anembedded closed normal surfaceS′ disjoint fromS such that
χ(S′) = 0.
9. Inv ariance under 2-3 and 0-2 moves
The arguments of [GHRS15] extend easily to prove the following.
Theorem 9.1. Let T be an ideal triangulation ofM and let ˜T be obtained fromT by a 2-3
move. Then for alla,b as above,Ia
T(b) =Ia
˜T(b) provided both sides are deﬁned.
Proof. We follow the argument from [GHRS15, Theorem A.1], indicating the main changes
needed in the current setting. Consider a 2-3 move fromT to ˜T; this occurs in a bipyramid
consisting of 2 tetrahedra in T which are replaced by 3 tetrahedra sharing an edge of order
3 in ˜T.
First note that eachQ-normal classS∈ Q(T; Σ) can be written as a linear combination
of edge solutions, tetrahedral solutions and peripheral curve solutions with coeﬃcients in
1
2 Z, by the results of Section 6 (see Remark 7.6). As in section 4.4 of [GHRS15], we can
represent S by a linear combinationω of oriented normal arcs in the induced triangulation
T∂ of ∂M, chosen so that each quad coordinate forS is a sum of 4 “turning numbers” of
normal arcs, coming from the 4 corners of the tetrahedron containing the quad (see ﬁgure 7
of [GHRS15]).
26 STA VROS GAROUF ALIDIS, CRAIG D. HODGSON, NEIL R. HOFFMAN, AND J. HYAM RUBINSTEIN
Explicitly, for each edge solution we choose a small normal linking circle in∂M around
one end of the edge in T, we choose oriented normal curves representing each peripheral
class, and for each tetrahedral solution we choose three normal arcs oriented anticlockwise in
a triangle coming from one corner of the tetrahedron. (If tetrahedral solutions are needed in
the bipyramid, we choose the two triangles at the degree 3 vertices at the top and bottom.)
One diﬀerence from [GHRS15] is that the coeﬃcients of the normal arcs here can behalf-
integers; but each sum of turning numbers giving a quad coeﬃcient is still an integer.
To compute the indexIa
T(b), we choose a normal classS0 with [S0]2 = a and [∂S0] = b,
and have a contribution from each normal class
Sk =S0 +
∑
kiEi,
where k = (ki)∈ Zn−r is a set of integer weights on a set ofn−r “basic edges”. (The
excluded edges are taken from a “maximal tree with 1- or 3- cycle forT” as in Theorem 4.3
of [GHRS15]; this ensures that the mapk = (ki)↦→∑kiEi + T is an isomorphism fromZn−r
onto (E + T)/T.) We can representS0 by a linear combinationω of oriented normal arcs as
described above. By addingki small linking circles around one end of theith edge inT we
obtain a linear combinationωk of oriented normal arcs which gives the quad coordinates of
Sk =S0 +∑kiEi.
The construction of [GHRS15] shows how to replace ω by a linear combination ˜ω of
oriented normal arcs in˜T∂ representing a normal class˜S0 in ˜T and this satisﬁes[ ˜S0]2 = [S0]2
and [∂S0] = [∂ ˜S0]. (Essentially, ˜S0 is obtained by subdividing the normal disks ofS0, so its
homology classes do not change.) Then the index sum forIa
˜T(b) has a contribution for each
normal class
˜S˜k = ˜S0 +k0 ˜E0 +
∑
ki ˜Ei,
where k0 is the integer weight on the new edge class˜E0 in ˜T, and k = (ki)∈ Zn−r as above
give the weights on the edge classes˜Ei coming from T. Adding small linking circles around
one end of each edge inT gives a linear combination of normal arcs˜ω˜k which gives the quad
coordinates of ˜S˜k.
TheproofofthePentagonEquality(LemmaA.3in[GHRS15])nowgoesthroughverbatim;
this gives the result. The only diﬀerence in the current setting is that coeﬃcients of normal
arcs and turning numbers can now be half-integers. However since the sums giving quad
coeﬃcients used in the tetrahedral index functions are integers, the arguments of [GHRS15]
go through without change. □
The arguments from [GHRS15] also extend to give the following.
Theorem 9.2. Let T be an ideal triangulation ofM and let ˜T be obtained fromT by a 0-2
move. Then for alla,b as above,Ia
T(b) =Ia
˜T(b) provided both sides are deﬁned.
Proof. Here the proof of Theorem 5.1 in [GHRS15] applies, if we start with a linear combi-
nation ω of oriented normal arcs inT∂ with 1
2 Z coeﬃcients giving the quad coordinates of
S0 with homology classes[S0]2 =a and [∂S0] =b. □
THE 3D-INDEX AND NORMAL SURF ACES 27
10. Generalised normal surf aces
Embedded normal surfaceswere introduced by Kneser [Kne29] in 1929. In the 1950s and
1960s, Haken [Hak61b, Hak61a, Hak68] extensively developed the theory of normal surfaces
(via handle decompositions and also via triangulations) and applied this to basic algorithmic
questions in topology. The solutions to Haken’s matching equations includebranched and
immersednormal surfaces, which are the result of gluing together ﬁnitely many normal disks
in tetrahedra of a triangulation of a closed manifold or an ideal triangulation of a compact
manifold with boundary. In the 1980s Thurston suggested the theory ofspun normal surfaces
(see [Til08, Wal11]). These are obtained by gluing ﬁnitely many quadrilaterals but possibly
inﬁnitely many triangular disks, as long as there are at most a ﬁnite number of such disks
which are not contained in ‘tails’ which are inﬁnite annuli spiralling around a cusp. We
will again specify if a spun normal surface is embedded — in general it can be branched
or immersed. Moreover spun normal surfaces may contain no tails, in which case they are
(closed) normal surfaces.
