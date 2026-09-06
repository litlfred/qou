---
doc_id: arxiv-1608.02961v3
doc_title: "Perturbative and nonperturbative aspects of complex Chern-Simons Theory Tudor Dimofte"
section_id: sec-007-42-state-integral-models-and-angle-structures
section_title: "State-integral models and angle structures"
section_number: 4.2
pages: 15-20
source_pdf: 1608.02961v3.pdf
source_sha256: ef3805c23133b8f2
doc_brief: "Perturbative and nonperturbative aspects of complex Chern-Simons Theory Tudor Dimofte — We present an elementary review of some aspects of Chern-Simons theory with complex gauge group SL(N, C)."
---
When M = S3\K is an oriented hyperbolic knot or link complement (or, more generally,
an oriented hyperbolic manifold with non-empty boundary of genus ≥ 1), there exists a
systematic construction of SL(2, C) Chern-Simons partition functions Z[M]k,s for all levels
k,s . The full deﬁnition of these partition functions appears in [81, 82] for k = 0, and [22, 21]
for k⁄= 0, respectively. It is a culmination of much previous work, including [72, 49, 83,
19, 84] for k = 1; [20] for k = 0 (and indirectly [85, 86, 87]); and (indirectly, via 3d-3d
correspondence) [88, 89] for k > 1. The deﬁnition extends to SL(N, C) using techniques
of [38].
The construction of these partition functions uses a topological ideal triangulation of
the three-manifold M =∪N
i=1∆i. This is a tiling of M by truncated tetrahedra ∆ i, as in
Figure 4.1, such that 1) various pairs of large hexagonal faces are glued together; but 2)
the small triangles at the truncated vertices are left untouched, and become part of the
boundary ∂M .
One then proceeds in standard TQFT fashion. For gauge group SL(2, C) (or more pre-
cisely,PSL (2, C)), the boundary of each tetrahedron is assigned a Hilbert space H[∂∆]k,s≃
L2(R)⊗ Ck. The Hilbert space comes from quantizing an open subset of the space of ﬂat
15
M
@M'T2
Figure 4.1: Ideal ( i.e. truncated) tetrahedra, glued together along their large hexagonal
faces to form an ideal triangulation of a knot complement M. The small triangular faces at
truncated vertices become part of the boundary of M.
connections on∂∆, viewed as a four-punctured sphere; in this caseP[∂∆]open≃ C∗×C∗, and
the quantization of Section 2 applies in a straightforward manner, with no Weyl quotient.
Each tetrahedron is assigned a canonical partition function Z[∆]k,s∈H [∂∆]k,s, which has
the form of a “quantum dilogarithm” function; for |k|≥ 1, this is
Z[∆i]k,s(µi,mi) =
∞∏
r=0
1−q1+rz−1
i
1− ˜q−r¯z−1
i
, (4.4)
with q, ˜q as in (2.13) or (2.20) and zi = e
2πb
k µi− 2πi
k mi, ¯zi = e
2πb−1
k µi+ 2πi
k mi as in (2.9). (For
k = 0, see Section 4.3.)
The partition functionZ[M]k,s is then obtained by taking a product∏N
i=1Z[∆i]k,s(µi,mi),
and integrating out all pairs of variables (µi,mi) associated to the interior of M, leaving be-
hind some variables associated to the boundary. It is slightly tricky to describe this operation
in precise terms, because the tetrahedron Hilbert space H[∂∆]k,s does not easily factorize
into contributions from the tetrahedron’s four large faces. 8 The right prescription comes
from viewing gluing in TQFT somewhat more globally, as a quantum symplectic reduction.
It turns out that the combinatorics of ideal triangulations have some fundamental symplec-
tic properties, ﬁrst discovered by Neumann and Zagier [90, 91], that allow the quantum
symplectic reduction to be deﬁned.
As an example, take M = S3\K to be a knot complement. In this case, there is a
canonical “A-cycle” on the boundary torus ∂M = T 2, deﬁned by a small loop linking the
8The Hilbert space can be factorized by introducing some redundant degrees of freedom [19], in a manner
directly analogous to Kashaev’s quantization of Teichm¨ uller space [40].
16
knot K in S3 (called the meridian cycle); and there is a canonical boundary condition for
SL(2, C) connections, deﬁned by requiring their holonomy along the meridian cycle to have
trivial eigenvalues. (Crucially, this does not require the actual holonomy to be trivial; in
SL(2, C) there are parabolic matrices ( 1 1
0 1 ) with trivial eigenvalues.) In the notation of
Section 2, the boundary condition sets x = ¯x = 1, or restricts functions f(µ,m )∈H [T 2]k,s
to their values atµ =m = 0. Suppose that the knot complement is glued from N tetrahedra
∆i. The combinatorics of the triangulation deﬁne a “Neumann-Zagier datum”
A, B ∈ MatN×N(Z), ν, ∈ ZN (4.5)
consisting of two N×N integer matrices A, B (that encode adjacency relations for edges
of the tetrahedra and satisfy the symplectic property ABT− BAT =IN×N) and a vector ν
of N integers. A precise deﬁnition is given in [73]. Then the partition function Z[M]k,s =
Z[M]k,s(0, 0) with the canonical boundary condition takes the concise form [35]
Z[M]k,s = C
kN
√
detB
∑
m∈(Z/kZ)N
∫
dNµ (−ζ
1
2 )mB−1Ame−iπ
k µB−1Aµ−π
k (b+b−1)µB−1ν
N∏
i=1
Z[∆]k,s(µi,mi),
(4.6)
with ζ = e
2πi
k . The prefactor C = ζ
1
4f B−1νe
iπ
4k (b2−b−2)f B−1ν depends on an integer solution
(f,f′′)∈ Z2N to Af + Bf′′ =ν.
There are several things to note about this partition function:
• It approximately takes the form of a “state sum” or “state integral,” with the partition
function (4.4) assigned to every tetrahedron building-block. The “state variables”
mi∈ Z/kZ and µi are summed/integrated over. The number of sums/integrals is the
same as the number of tetrahedra which is also the same as the number of internal
edges in the triangulation.
• As explained in [22, 35], the partition function is only deﬁned up to an overall phase,
of the form ζ
a
24e
iπ
12k (a′b2+a′′b−2),a,a′,a′′∈ Z. This subsumes the standard framing ambi-
guity in complex Chern-Simons theory [5], which would modify the partition function
by a factor of e−iπ
2k (b+b−1)2
upon shifting the framing of the tangent bundle of M.
• Each tetrahedron building-block manifestly admits a holomorphic-antiholomorphic fac-
torization as in (3.1). The full partition function is also expected to admit such a fac-
torization; this was demonstrated for some simple examples in [22]. (See also [57, 92]
for k = 0, k = 1 examples.)
• Perhaps most interestingly, the precise deﬁnition of the integration contour in (4.6)
and the convergence of the integral depends crucially on the existence of a positive
angle structure on the triangulation being used. This is ultimately what restricts the
computation to a particular class of 3-manifolds that includes all hyperbolic ones. It
also beautifully makes contact with the three-dimensional superconformal theoryT [M]
deﬁned combinatorially in [14] using an ideal triangulation — the deﬁnition of T [M]
17
does not make sense (cannot produce a superconformal theory) unless a positive angle
structure exists. We proceed to explain this idea momentarily.
• Via the 3d-3d correspondence, the integral (4.6) has a dual interpretation as a partition
function of T [M] on the lens space S3/Zk. This partition function is computed by
localization methods, as in Section 4.1 of B. Willett’s article, Contribution [47]. Each
Z[∆]k,s(µi,mi) is the contribution of a chiral multiplet to the partition function, and
the additional prefactor comes from background Chern-Simons terms involving ﬂavor
and R-symmetries.
• Changes of ideal triangulations are generated by 2–3 Pachner moves, which replace a
pair of tetrahedra glued along a common face by a triplet glued along three common
faces and a central edge. The state-integral (4.6) is invariant under 2–3 moves that
preserve the positive or non-negative angle structure (as appropriate), due to a 5-term
integral identity for the quantum dilogarithm (4.4). In the case k = 1, this identity
was ﬁrst discovered by Faddeev [93] (see also [94]).
An angle structure on a topological ideal triangulation is an assignment of real parameters
(“angles”) to the six long edges of each tetrahedron, in such a way that 1) angles on opposite
edges are equal (leaving three angles αi,α′
i,α′′
i per tetrahedron ∆ i); 2) the sum of angles
around any tetrahedron vertex equals π (thus αi +α′
i +α′′
i = π); and 3) the sum of angles
around every internal edge in the triangulation equals 2 π. In terms of the Neumann-Zagier
gluing datum (4.5) for a knot complement, the last condition translates to 9
Aα + Bα′′ =πν. (4.7)
The idea of an angle structure is motivated by hyperbolic geometry. In an ideal triangulation
by hyperbolic tetrahedra, the dihedral angles precisely obey the three conditions above [59].
A positive (respectively, non-negative) angle structure is one where all angles additionally
obey αi,α′
i,α′′
i > 0 (≥ 0). An oriented hyperbolic three-manifold with genus-one boundary
always admits an triangulation with non-negative dihedral angles, hence there a triangulation
with a non-negative angle structure [95]. It is conjectured and strongly believed that the same
holds for strictly positive angle structures. (As evidence for this, the default triangulations
produced by the computer program SnapPy [96] for the ﬁrst few thousand hyperbolic knot
complements all admit positive angle structures.)
It was shown in [81, 82] that analogue of the partition function (4.6) atk = 0 (cf. Section
4.3) is well-deﬁned when the triangulation admits a non-negative angle structure. Similarly,
it was shown in [19] for k = 1 and [22, 21] for |k|≥ 1 that the partition function (4.6) is
well deﬁned if the triangulation admits a positive angle structure. In each case, the angle
structure speciﬁes a canonical convergent integration contour.
9Technically, onlyN−1 out of the N components of (4.7) correspond to internal edges; the last component
of (4.7) relates to a boundary condition at ∂M = T 2, and can be removed from the angle-structure analysis.
We are bypassing such subtleties in this heuristic discussion.
18
↵0↵00
↵0 ↵00
↵
V+V 
 
V+ V 
 ↵
Figure 4.2: Left: dihedral angles assigned to edges of an oriented ideal tetrahedron, obeying
α +α′ +α′′ = π. Right: operators of the tetrahedron theory T [∆] assigned to the same
edges; these operators have R-charges ρ,ρ′,ρ′′ that obey ρ +ρ′ +ρ′′ = 1.
The combinatorial construction of theoriesT [M] given in [14] translates the ingredients of
the state-integral (4.6) to operations in three-dimensional N = 2 gauge theories. One starts
by associating a theory T [∆i] containing a single chiral multiplet Φ i (i.e. a free complex
boson φi and a complex fermion ψi) to each tetrahedron. In addition to the chiral (BPS)
operator Φi, the theory T [∆i] contains two elementary chiral monopole operators V±
i , which
exist only in the presence of a monopole background for the ﬂavor symmetry of the theory.10
Geometrically, the three operators Φi,V +
i ,V −
i are associated to three pairs of ∆ i, as on the
RHS of Figure 4.2. Moreover, T [∆i] has an R-symmetry 11 U(1)R that rotates (φi,ψi) with
charges (ρi,ρi− 1) for some (undetermined) ρi∈ R. One usually just says that Φ i has R-
chargeρi. The other BPS operators V +
i ,V −
i have some R-charges ρ′
i,ρ′′
i , subject to a single
relation ρi +ρ′
i +ρ′′
i = 1.
Even for the theory of a single tetrahedron, R-charges are beginning to look like angles,
and it is tempting to identifyρi =αi/π (etc.). The analogy persists upon gluing. The theory
T [M] of [14] is deﬁned by taking a tensor product ofN tetrahedron theories⊗N
i=1T [∆i], gaug-
ing some ﬂavor symmetries, and (most importantly here) adding superpotential interactions
W =∑N
E=1OE containing a chiral operatorOE for every internal edgeE of the triangulation
M =∪N
i=1∆i. If all the tetrahedron edges identiﬁed with E are labelled by elementary chiral
ﬁelds Φi, one simply constructsOE as a product∏
i Φi of these surrounding ﬁelds. For edges
identiﬁed with monopole operators, the prescription is more subtle. In either case, one ﬁnds
that the R-charge ofOE is a sum of the R-charges ρi,ρ′
i, orρ′′
i associated to operators on the
tetrahedron edges identiﬁed with E. The superpotential breaks U(1)R R-symmetry unless
the charge of everyOE is exactly 2.
Now, in order for the gauge theory T [M] to ﬂow (in a straightforward way) to a super-
conformal theory in the infrared, two conditions are necessary: 1) some U(1)R R-symmetry
10One does not usually talk about “ﬂavor” monopole operators like V ±
i , but they are essential in the
construction of theories T [M], and the relation between these theories and geometry. They can easily be
seen in the generalized index of a free chiral multiplet [87], and can also be understood as ordinary monopole
operators if the ﬂavor symmetry of T [∆i] were weakly gauged.
11This is a global symmetry that does not commute with supersymmetry, and is related to an SO(2)
automorphism of the 3d N = 2 SUSY algebra.
19
must be preserved; and 2) there must exist a choice ofU(1)R symmetry such that the charges
of all chiral operators are non-negative, because in a superconformal theory R-charges are
proportional to operator dimensions. This means that we must be able to choose ρi,ρ′
i,ρ′′
i for
individual tetrahedra in such a way that the sums of these charges around any internal edge
E is 2, and all these charges are non-negative. Together with the relation ρi +ρ′
i +ρ′′
i = 1,
the conditions become equivalent to the existence of a non-negative angle structure.
