---
doc_id: arxiv-1207.6711v1
doc_title: "GLUING EQUATIONS FOR PGL(n, C)-REPRESENTATIONS OF 3-MANIFOLDS"
section_id: sec-024-71-applications-in-quantum-topology
section_title: "Applications in quantum topology"
section_number: 7.1
pages: 23-25
source_pdf: 1207.6711v1.pdf
source_sha256: 320c4301ac66fff1
doc_brief: "GLUING EQUATIONS FOR PGL(n, C)-REPRESENTATIONS OF 3-MANIFOLDS — In [11] we parametrized boundary-unipotent representations of a 3-manifold group into SL(n, C) using Ptolemy coordinates, which were"
---
M with torus boundary components and their gluing equations have found several applica-
tions in quantum topology, and this has been a main motivation for our work. We will list
three applications here, and refer to the literature for more details:
(a) The Quantum Riemann surfaces of [4]
(b) The loop invariants of [7]
(c) The 3D index of [6, 5, 10]
The input of a quantum Riemann surface of [4] is an ideal triangulationT of a 3-manifold
with torus boundary components, and the output is a polynomial in q-commuting variables
(one per meridian and longitude of each torus boundary component). The operators generate
24 STA VROS GAROUF ALIDIS, MATTHIAS GOERNER, AND CHRISTIAN K. ZICKERT
a q-holonomic ideal which depends on T and ought to map to the gluing equation variety
V2(T ) when q = 1.
The input of the loop invariants of [7] is a Neumann-Zagier datum which consists of an
ideal triangulation together with a solution of the gluing equations whose image under the
map (1.2) is the discrete faithful representation of M. The output is a formal power series
in a variable ℏ with coeﬃcients rational functions on the image of the map (1.2). The
coeﬃcient of ℏ in the above series ought to agree with the non-abelian torsion of [16] and
the evaluation of the series at the discrete faithful representation when ℏ = 2πi/N, ought to
agree to all orders in 1/N with the asymptotics of the Kashaev invariant [13] of a hyperbolic
knot complement.
The input of the 3D index of [6, 5] (see also the survey article [10]) is an ideal triangulation
T which supports a strict angle structure. The output is a q-holonomic functionIT : Z2r−→
Z((q1/2)) where r is the number of torus boundary components of M and Z((q1/2)) is the
ring of Laurent series in q with integer coeﬃcients.
Using our Theorems 1.1 and 1.2, one can extend the above invariants to the case of
representations in PGL(n, C). For example, ﬁx an ideal triangulation T with t tetrahedra
of a 3-manifold M with torus boundary. Following [7, Sec.1.2], choose a pair of opposite
edges of each subsimplex, remove n− 1 gluing equations which are dependent on the others,
and replace them with the n− 1 cusp equations of the meridian to obtain matrices r×r
An and Bn where r =t
(n+1
3
)
. Let z denote the r vector of shapes of solutions to the gluing
equations. Following [7, Defn.1.1] consider the Neumann-Zagier datum βT,n = ((An|Bn),z )
and its enhanced version ˆβT,n = ((An|Bn),z,f ) where f is a choice of ﬂattening of each
subsimplex. Following [7, Defn.1.2] we deﬁne the 1-loop invariant of ˆβT,n by
(7.17) τT,n =±1
2 det
(
An∆z′′ +Bn∆−1
z
)
zf′′
z′′−f
where ∆z := diag(z1,...,z r) and ∆z′′ := diag(z′′
1,...,z ′′
r ) are diagonal matrices, andzf′′
z′′−f :=∏
izif′′
iz′′
i
−fi. When z is the solution that comes from the discrete faithful representation of
M, then τT,n lies in the invariant trace ﬁeld of M. An exact computation is possibe using
the SnapPy tools [3]. We thank N. Dunﬁeld for providing an automated code for exact
computation. Let us give some examples.
Example 7.8. The 41 knot has invariant trace ﬁeld Q(x) where
x2−x + 1 = 0, x = 1 +i
√
3
2
If τn =τ41,n, the quotient τn+2/τn appears to have lower complexity than τn and is given by
τ2 = 1/2−x τ 3 = 21/2
τ4
τ2
= 6720 τ5
τ3
= 52147200
τ6
τ4
=−5381278156800 τ7
τ5
=−7383730314510950400
τ8
τ6
=−138731589652863387775795200
GLUING EQUATIONS FOR PGL( n, C)-REPRESENTATIONS OF 3-MANIFOLDS 25
Example 7.9. Consider the knot 5 2 with invariant trace ﬁeld Q(x) where
x3−x2 + 1 = 0, x = 0.877439···− i 0.744862... .
The mirror−(−2, 3, 7) of the ( −2, 3, 7) pretzel knot has the same volume and the same
invariant trace ﬁeld as 5 2. If τn =τ52,n and τ′
n =τ−(−2,3,7),n then we have
τ2 = 1− 3/2x τ ′
2 =−2 + 5x− 3x2
τ3
τ2
=−63 + 57x2 τ′
3
τ′
2
=−120− 48x + 144x2
τ4
τ3
= 1536− 3072x− 9792x2 τ′
4
τ′
3
= 21984 + 5712x− 31008x2
τ5
τ4
=−12831360− 10393200x + 8023440x2 τ′
5
τ′
4
=−3196800 + 14346000x + 24614400x2
τ6
τ5
=−95788707840− 84869406720x τ′
6
τ′
5
= 158834390400 + 213765955200x
+ 55161630720x2 + 4444675200x2
