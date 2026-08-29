---
doc_id: arxiv-2205.06874v2
doc_title: "State sum models with defectsbased on spherical fusion categories Catherine Meusburger Department Mathematik Friedrich-Alexander-Universität Erlangen-Nürnberg"
section_id: sec-024-moves-between-triangulated-pl-manifolds
section_title: "Moves between triangulated PL manifolds"
section_number: null
pages: 39-41
source_pdf: 2205.06874v2.pdf
source_sha256: 9b41365160c17ab4
doc_brief: "State sum models with defectsbased on spherical fusion categories Catherine Meusburger Department Mathematik Friedrich-Alexander-Universität Erlangen-Nürnberg — We define a"
---
To establish triangulation independence for state sum models with defects, we require some background from
PL topology. We consider different moves on triangulations that relate PL homeomorphic 3-manifolds with
and without boundary. The main references are the articles [P91, P90] by Pachner, see also the articles [Li99]
by Lickorish and [C95] by Casali.
Theorem 5.1. [P91, Th. 5.5],[Li99, Th. 5.9]
Two closed triangulatedn-dimensional PL manifolds are PL homeomorphic iff they are related by a finite
sequence of bistellar moves.
Theorem 5.2. [C95]
Two triangulatedn-dimensional PL manifolds with boundary, whose boundary triangulations coincide, are PL
homeomorphic iff they are related by bistellar moves.
The bistellar movesfor a 3-manifold are the 2-3 move and the 1-4 move depicted in Figure 4. The 1-4 move
subdivides a tetrahedron into four by inserting a new vertex in its interior or reverses this step. The 2-3 move
replaces two tetrahedra that share a triangle by three tetrahedra that share an edge or reverses this step.
We also considerstellar subdivisions, see for instance [RS]. The stellar subdivision for a tetrahedron is the
1-4 move from Figure 4. The stellar subdivisions for a triangle and an edge are shown in Figure 5. A stellar
subdivision of a triangle∆ inserts a vertex in the interior of∆ and connects it to the vertices of∆ and to
the opposite vertices of all tetrahedra containing∆. A stellar subdivision of an edgee inserts a vertex in the
interior ofe and connects it to the opposite vertices of all triangles containinge.
It is shown in [BW96] that stellar subdivisions are composites of 1-4 and 2-3 moves. The stellar subdivision
for a triangle∆ is obtained by to first applying a 1-4 move to one of the two tetrahedra containing∆ and
39
1-4 2-3
Figure 4: Bistellar moves for a tetrahedron.
Figure 5: Stellar subdivisions for a triangle and an edge of a triangulation.
then a 2-3 move to the other tetrahedron and the adjacent tetrahedron created by the 1-4 move, see the proof
of Theorem 4.6 in [BW96]. The stellar subdivision for an edgee shared byn tetrahedra is obtained by first
applying a 1-4 move to one of the tetrahedra containinge. Then one applies a sequence of(n− 2) 2-3 moves
clockwise to the remaining tetrahedra containinge. These 2-3 moves connect the new vertex to the vertices
of these tetrahedra. Finally one applies a 2-3 move that removese, see the proof of Theorem 4.6 in [BW96].
For 3-manifolds with boundaries one also needs to consider elementary shellings and their inverses. An
elementary shellingof a PL 3-manifoldM removes a 3-simplext that is the joint =A⋆B = conv(A∪B)
of two simplexesA and B with A∩M =∂A and B⋆∂A ⊂∂M and replacesM by the closure ofM\A⋆B ,
see [Li99, Def. 5.2]. This amounts to removing the tetrahedront, which has one, two or three faces in the
boundary ∂M, such that its remaining faces become boundary faces, as shown in Figure 6. Correspondingly,
an inverse shellingamounts to adding a tetrahedron toM that shares one, two or three triangles with∂M.
Figure 6: Elementary shellings: removing a tetrahedron with one, two or three faces in the boundary.
40
Elementary shellings and their inverses on a 3-manifoldM induce bistellar moves on the boundary∂M.
These are the 1-3 move, which subdivides a boundary triangle into three by adding a vertex in its interior or
reverses this step, and the 2-2 move, which replaces a common edge shared by two boundary triangles with
the edge connecting their remaining two vertices, as in Figure 6. It is shown in [P90, P91] that triangulations
of a PL manifold with boundary are related by bistellar moves, elementary shellings and their inverses.
Theorem 5.3. [P91, Th. 4.14], [P90, Th. 2]
Two triangulatedn-dimensional PL manifoldsM,M′ with boundary are PL homeomorphic iffM can be
transformed intoM′ by a finite number of elementary shellings and bistellar moves.
Theorem 5.4. [P91, Th. 6.3], [Li99, Th. 5.10]
Two connected triangulatedn-dimensional PL manifolds with non-empty boundary are PL homeomorphic iff
they are related by a finite sequence of elementary shellings and inverse shellings.
If a triangulatedn-manifold M is transformed intoM′ by a finite number of elementary shellings, one says
that M shells to M′. A triangulatedn-manifold M is calledshellable if it shells to ann-simplex. It is
well-known that every triangulation and, more generally, CW-decomposition of a2-disc is shellable. This does
not hold for triangulations or CW-decompositions of the 3-ball, see Ziegler [Zi98] and the references therein.
The triangulation independence of the Turaev-Viro-Barrett-Westbury state sum from [TV92, BW96] follows
from its invariance under bistellar moves. It is shown in [BW96] and [T] that the invariance of the state
sum under the 2-3 move in Figure 4 encodes the pentagon relation for the associator of a spherical fusion
category. Its invariance under the 1-4 move in Figure 4 corresponds to an equivalent relation obtained by
inverting one of the associators in the pentagon relation. It follows from the invariance under the 2-3 move
and under abubble move. The latter corresponds to the invertibility of the associator and states that gluing
two tetrahedra with opposite orientations along four faces yields the trivial state sum.
The pentagon relation for the associator is encoded in the Biedenharn-Elliott relations for the 6j symbols and
the invertibility of the associator in their orthogonality relations [BW96, Prop. 5.2]. They are obtained by
expressing the associator on simple objects ofC as in(74) and using its naturality. In our notation they read
∑
β
m
m
k
j
i
n
p
α
β
γ
δ
m
m
a
b
k
q
n
ϕ
ρ
σ
β
=∑
c,λ,µ,ν dim(c)
m
m
a
c
i
q
n
λ
ρ
µ
δ
a
a
k
j
i
b
c
α
ϕ
ν
λ
p
p
c
b
j
q
n
ν
µ
σ
γ
(86)
∑
p,γ,δ dim(p) dim(k) =δασδβρδkl
m
m
k
j
i
n
p
α
β
γ
δ
m
m
i
j
l
p
nσ
δ
γ
ρ
(87)
These relations yield a direct proof of the triangulation independence of the state sum for closed 3-manifolds
[BW96, Th. 5.1]. For 3-manifolds with boundary one has the following result.
Theorem 5.5. [TV92, Th. 1.4], [T, Th. 1.7]
LetM,M′ be compact triangulated 3-manifolds with boundary whose boundary triangulations and boundary
labelingsl∂M and b∂M coincide. Then their state sums(84) are equal.
