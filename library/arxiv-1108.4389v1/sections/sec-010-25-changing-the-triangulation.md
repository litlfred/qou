---
doc_id: arxiv-1108.4389v1
doc_title: "b partition functions of two mirror 3d N = 2 gauge theories are equal. Three-dimensional N = 2 ﬁeld theories associated to 3-manifolds can be thought of as theories that describe b"
section_id: sec-010-25-changing-the-triangulation
section_title: "Changing the triangulation"
section_number: 2.5
pages: 19-20
source_pdf: 1108.4389v1.pdf
source_sha256: d3ac77510654d828
doc_brief: "Gauge Theories Labelled by Three-Manifolds — We propose a dictionary between geometry of triangulated 3-manifolds and physics of three-dimensional N = 2 gauge theories."
---
We have explained, in principle, how to construct 3-manifolds M, phase spaces P∂M , and
LagrangiansLM by gluing together ideal tetrahedra ∆ i. It would be useful to verify that
such constructions do not depend on a precise choice of triangulation {∆i}. Geometrically,
once we ﬁx the triangulation of geodesic boundaries, any two triangulations of M are related
by a sequence of “2–3 Pachner moves,” cf. [21]. These replace two tetrahedra glued along
a common face with three tetrahedra glued along three faces and a common edge, and vice
versa, as shown in Figure 15.
z
z￿z￿￿
z
z￿
z￿￿
w
w￿
w￿￿
w
w￿
w￿￿
y
y￿
y￿￿
y
y￿
y￿￿
r
r￿
r￿￿
r
r￿
r￿￿
s
s￿
s￿￿
s
s￿ s￿￿
Figure 15: The 2–3 Pachner move
Invariance of phase spaces and Lagrangians under the 2–3 move was veriﬁed 8 in detail
in (e.g.) [ 12], guaranteeing the internal consistency of our present gluing constructions. For
example, for phase spaces, the essence of the argument is that the product phase spaces
corresponding to the bipyramid on the left of Figure 15 is the symplectic reduction of the
product phase space on the right,
P∂(bipyramid) = P∆R×P ∆S =
(
P∆Z×P ∆W×P ∆Y
)//
(C = 2πi), (2.33)
whereC is the gluing constraint coming from the internal edge. In fact, we already described
the right-hand side of (2.33) in Section 2.3. The left-hand side is even easier to analyze. In the
same two polarizations Π eq and Πlong of Figure 12, we now ﬁnd coordinates for P∆R×P ∆S:
positions momenta
Πeq : X1 =R +S′′, X 2 =R′′ +S P 1 =R′′, P 2 =S′′
Πlong : X′
1 =R, X ′
2 =S P ′
1 =R′′, P ′
2 =S′′
(2.34)
The two equivalent descriptions ( 2.22)–(2.34) of P∂(bipyramid) are related by combining or
splitting the coordinates associated to the external dihedral angles, for example splitting
Z↔R′′ +S′′.
8Again we note that the invariance of Lagrangians comes with a few subtle caveats, as discussed in [ 10, 11]
and reviewed in Sections 4–5 of [12]. For suﬃciently generic triangulations, these caveats can be safely ignored.
– 18 –
The 2–3 Pachner moves always preserve the triangulations of geodesic boundaries of M.
In contrast, they do not preserve the “small” triangulations of cusp boundaries; but the
triangulations of cusp boundaries are never important for deﬁning phase spaces here, or 3d
gauge theories later on.
If we want to change the triangula-
p
x z
z
￿
z
￿￿z
z
￿
z
￿￿
x
￿=
z
p
￿
pz
￿
=
∪
ﬂip
Figure 16: Flipping an external edge by attaching
a tetrahedron.
tion of a geodesic boundary C⊂ ∂M , we
must consider another type of fundamen-
tal move: a ﬂip. The ﬂip acts by gluing an
additional tetrahedron ∆F onto a quadri-
lateral inC, as in Figure 16, and eﬀectively
“ﬂipping” the diagonal of this quadrilat-
eral. In the process of attaching ∆F , a new
internal edge IF is created, which imposes
a new gluing constraint CIF . The ﬂipped
phase spacePC′ is therefore related to PC
by a symplectic reduction
PC′ =
(
PC×P∂∆F
)//
(CIF = 2πi). (2.35)
ObviouslyPC′ andPC must be isomorphic, but the two have diﬀerent “natural” polarizations.
To illustrate this explicitly, if we start with a polarized phase space PC in which one of
the canonical position–momentum pairs ( X,P ) corresponds to dihedral angles as in Figure
16, then gluing on the tetrahedron ∆ F yields an internal edge constraint
CIF =X +Z → 2πi. (2.36)
Now, let us attach a new position coordinate X′ to the newly ﬂipped diagonal, and its
conjugate momentumP′ to the same edge asP . After the symplectic reduction (in particular,
imposing (2.36)), we ﬁnd that
X′ = 2πi−X, P ′ =−(P +Z′). (2.37)
If we also keep track of Lagrangians, we would ﬁnd that the ﬂipped LM′ is related toLM by
substituting x→x′−1, p→p′−1(1−x′) in the deﬁning equations for LM.9
The ﬂip transformation, described here from a 3-dimensional viewpoint, is very familiar
in 2-dimensional Teichm¨ uller (and quantum Teichm¨ uller) theory,cf. [22, 18, 23, 24, 15]. This
should not be surprising, given the above observation that shear coordinates of Teichm¨ uller
theory should be identiﬁed with 3d dihedral angles.
