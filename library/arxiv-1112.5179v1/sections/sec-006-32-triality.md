---
doc_id: arxiv-1112.5179v1
doc_title: "3-Manifolds and 3d Indices"
section_id: sec-006-32-triality
section_title: "Triality"
section_number: 3.2
pages: 18-21
source_pdf: 1112.5179v1.pdf
source_sha256: b58af08336c40994
doc_brief: "3-Manifolds and 3d Indices — We identify a large classR of three-dimensionalN = 2 superconformal ﬁeld the- ories."
---
Experimentally, we observe that the tetrahedron index enjoys yet another more interesting
discrete symmetry of order three:
I∆(m,e ;q) =
(
−q
1
2
)−eI∆(e,−e−m;q) =
(
−q
1
2
)mI∆(−e−m,m ;q). (3.11)
For a visual demonstration of this symmetry, let us deﬁne lead(m,e ) to be the leading power
of q that appears inI∆(m,e ;q) when written as a series in q. For example,
I∆(0, 0;q) = 1−q− 2q2− 2q3− 2q4 +q6 + 5q7 +... ⇒ lead(0, 0) = 0,
I∆(1, 0;q) =−q−q2 +q4 + 3q5 + 4q6 + 6q7 + 6q8 +... ⇒ lead(1, 0) = 1,
I∆(1, 2;q) =−q2−q3−q4−q5 +q7 + 3q8 + 5q9 +... ⇒ lead(1, 2) = 2,
(3.12)
etc. It can be shown from (3.5) that lead(m,e )≥ 0 for allm,e . A graph of lead(m,e ) appears
in Figure 1, which clearly hints at a Z3 “rotation” symmetry in the index as in (3.11). We will
describe a method of proving (3.11) in Section 3.3, using diﬀerence equations for the index.
– 17 –
Figure 1. Leading powers of q in the index. The graph interpolates smoothly between integer points.
In order to acquire further intuition for the triality symmetry of I∆, it is instructive to
observe that (3.11) can be written as
I∆(m,e ;q) =IσeST◦∆(m,e ;q) =I(σeST )2◦∆(m,e ;q), (3.13)
whereST∈Sp(2, Z) andσe≡σR
eσF
e are aﬃne symplectic transformations of the tetrahedron
theory, as described in Section 2. The transformation σeST has order three. Then we recall
from [19] that the tetrahedron SCFT T∆ is invariant9 under the cyclic action of σeST , due
to 3dN = 2 mirror symmetry [3–6]. In other words, the following UV theories ﬂow to the
same IR ﬁxed point:
T∆ : free chiral with global U(1) symmetry at CS level − 1
2
σeST◦T∆ : gauged U(1) theory at CS level + 1
2, coupled to a single chiral .
(3.14)
Since these theories are mirror symmetric their indices must be the same, and that is precisely
what we see in (3.11) and (3.13).
3.3 Diﬀerence equations
A ﬁnal interesting property of the tetrahedron index is the fact that it obeys two diﬀerence
equations. In terms of operators ˆx± = exp( ˆX±) and ˆp± = exp( ˆP±) as deﬁned in Section 2.5,
these are (
ˆp+ + ˆx−1
+ − 1
)
I∆ = 0,
(
ˆp− + ˆx−1
− − 1
)
I∆ = 0. (3.15)
9The decoration of the symplectic transformation ST by an R-charge and fermion number shiftσe =σR
eσF
e
is correlated with the precise deﬁnition of the tetrahedron theory in the twisted S2×S1 geometry, as discussed
above (3.2). Had we chosen diﬀerent R andF assignments forT∆, the aﬃne shift would look slightly diﬀerent.
– 18 –
For example, writing these out in the charge basis we ﬁnd
q
e
2I∆(m + 1,e ) +q−m
2I∆(m,e + 1)−I ∆(m,e ) = 0, (3.16a)
q
e
2I∆(m− 1,e ) +q−m
2I∆(m,e− 1)−I ∆(m,e ) = 0, (3.16b)
for all m,e . These equations are compatible with the ρ symmetry of the index, which in-
terchanges the two (±) sets of operators. The validity of (3.15) can be checked easily by
writing the index in a fugacity basis, and using the product formula (3.3). Also, in the semi-
classical regime (3.6) each of the diﬀerence equations (3.15) turns into a diﬀerential equation,
equivalent to the standard property of the dilogarithm function, z d
dz Li2(z) = log(1−z−1).
Equations (3.15) may look familiar from the study of “quantum Lagrangians” and S3
b
partition functions in [9, 19]. As anticipated in Section 2.5, these are the same diﬀerence
equations obeyed by the S3
b partition function of T∆, with an appropriate identiﬁcation of
the operators ˆx±, ˆp±. We will try to explain the reason behind this in Section 5. In essence,
the same universal algebra of line operators is acting on both the index and the S3
b partition
functions; Ward identities for the line operators then lead to (3.15).
z
z
￿
z
￿￿
z
￿
z
￿￿ z
￿￿
Figure 2. An ideal tetrahedron,
with edge parameters.
In terms of the tetrahedron ∆ itself, Equations (3.15)
are two copies of the quantized Lagrangian ˆL∆ that describes
which ﬂat SL(2, C) connections on the boundary ∂∆ can be
extended as ﬂat connections in the interior of ∆. To see
this, recall 10 from [19, 31] that the set of ﬂat connections
on ∂∆, a.k.a. the phase space P∂∆, is described by three
C∗–valued edge coordinatesz,z′,z′′, subject to the condition
thatzz′z′′ =−1. Upon quantization, these coordinates form
an algebra of operators with q-commutation relations
ˆzˆz′ =qˆz′ˆz, ˆz′ˆz′′ =qˆz′′ˆz′, ˆz′′ˆz =qˆzˆz′′, (3.17)
and a central constraint
ˆz′′ˆz′ˆz =−1. (3.18)
(For logarithms of the ˆz’s, written in uppercase letters, the constraint reads ˆZ + ˆZ′ + ˆZ′′ =
iπ + ℏ/2.) Similarly, the classical Lagrangian L∆ ={z′′ +z−1− 1 = 0}, describing ﬂat
connections in the interior of ∆, becomes promoted to a quantum operator ( cf. [28])
ˆL∆ = ˆz′′− ˆz−1− 1, (3.19)
which must annihilate any putative wavefunction of the tetrahedron, in any representation.
It should then be clear that Equations (3.15) are just two copies of (3.19), with opposite
10Throughout this paper, we will be quite brief with details of ﬂat connections and 3d geometry. We direct
the reader to the summary of triangulations in Section 2 of [19] and references therein (especially the classic
[23, 50]) for some potentially useful background.
– 19 –
quantization parameters ℏ and−ℏ. Indeed, using the classical complex variablesz =q
m
2ζ, z =
q
m
2ζ−1, or logarithmicallyZ = m
2 ℏ+iθ, Z = m
2 ℏ−iθ (cf. (2.32)), we ﬁnd that we can identify
( ˆP+, ˆX+) = (ℏ∂Z,Z ) and ( ˆP−, ˆX−) = (−ℏ∂Z,Z).
The Lagrangian (3.19) is invariant under cyclic permutations ˆ z → ˆz′ → ˆz′′ → ˆz in
the operator algebra for the tetrahedron. That is, the equation ˆL∆ψ = 0 for any putative
wavefunctionψ can be written using any pair of consecutive variables (ˆz′′, ˆz), (ˆz, ˆz′), or (ˆz′, ˆz′′),
thanks to the constraint (3.18). Moreover, the generator of the Z3 cyclic symmetry is none
other than our familiar aﬃne Sp(2, Z) element σeST , cf. (3.13), acting on logarithms of the
ˆz operators. For example, if we identify ( ˆP+, ˆX+) = ( ˆZ′′, ˆZ) and ( ˆP′
+, ˆX′
+) = ( ˆZ, ˆZ′), then
( ˆX′
+
ˆP′
+
)
=σeST
( ˆX+
ˆP+
)
=
(
−1−1
1 0
)( ˆX+
ˆP+
)
+
(
iπ + ℏ
2
0
)
. (3.20)
Together with the intertwining property (2.34) for the index, the cyclic symmetry of the
quantized Lagrangian guarantees thatI∆,IσeST◦∆, andI(σeST )2◦∆ all satisfy the same equa-
tions (3.15). This constitutes the basis for a proof that I∆ =IσeST◦∆ =I(σeST )2◦∆, as in
(3.13), since the solutions to the diﬀerence equations are unique given appropriate boundary
conditions. Details appear in Appendix A.
