---
doc_id: arxiv-1108.4389v1
doc_title: "b partition functions of two mirror 3d N = 2 gauge theories are equal. Three-dimensional N = 2 ﬁeld theories associated to 3-manifolds can be thought of as theories that describe b"
section_id: sec-007-23-geodesic-boundaries
section_title: "Geodesic boundaries"
section_number: 2.3
pages: 13-15
source_pdf: 1108.4389v1.pdf
source_sha256: d3ac77510654d828
doc_brief: "Gauge Theories Labelled by Three-Manifolds — We propose a dictionary between geometry of triangulated 3-manifolds and physics of three-dimensional N = 2 gauge theories."
---
We proceed to provide some details of the phase spaces P∂M associated to the various types
of boundary for M, and to give explicit examples of their construction. A more complete,
mathematical analysis of boundaries and phase spaces will appear in [ 13].
It is perhaps simplest to begin with geodesic boundaries. As discussed above, these arise
when tetrahedra ∆i are impartially glued; then some tetrahedron faces are left over to form
one or more disjoint boundaries C⊂ ∂M , each a triangulated, punctured Riemann surface.
The punctures are places where vertices of the tetrahedra ∆ i are located, and can ultimately
be regularized into cusps that end onC — we will say a bit more about this later. The induced
2d triangulation ofC is “ideal” in the sense that all edges begin and end on punctures.
The phase spacePC, a factor inP∂M , is the moduli space of ﬂat SL(2, C) connections on
C, with speciﬁed (ﬁxed) holonomy eigenvalues at every puncture. These eigenvalues become
central elements in the algebra of functions on PC. Geometrically, we can also describe PC
as the complexiﬁed Teichm¨ uller space of C, a complexiﬁcation of the moduli space of 2-
dimensional hyperbolic metrics. From this perspective, the puncture eigenvalues reﬂect the
geometric size of holes in C.
We can construct coordinates on PC by associating to every edge E in the triangulation
ofC the total complexiﬁed dihedral angle around it. 3 In other words,
edge E ↝ coordinate XE =
N∑
i=1
[
n(E,i )Zi +n′(E,i )Z′
i +n′′(E,i )Z′′
i
]
, (2.15)
where n(E,i )∈{ 0, 1, 2} is the number of times an edge of tetrahedron ∆ i with parameter
Zi coincides with the glued edge E, and similarly for n′(E,i ) and n′′(E,i ). This deﬁnition is
analogous to (2.12), except that now E is an external edge of M.
3In fact, these are coordinates on algebraically open patches of PC that have the topology of complex tori,
cf. [15, 16].
– 12 –
It turns out that the coordinates XE are already well known
E
E
￿
E
￿￿
E
￿￿￿
Figure 9: Poisson bracket for
external edges. Here {XE,X E′}
={XE′,X E′′} ={XE′′,X E}
={XE′′,X E′′′} = ℏ, etc.
mathematically as complexiﬁed “shear coordinates” on PC
[17, 18], deﬁned rigorously in [ 15] in the complex case. 4 By
following the arguments of [14], one can show that the Pois-
son structure induced on these edge coordinates is
{XE,XE′} =f(E,E′), (2.16)
where f(E,E′)∈{ 0,±1,±2} is the number of faces shared
by edges E and E′, counted with orientation ( cf. Figure
9). Expression ( 2.16) is precisely the Weil-Petersson Poisson
structure onPC, cf. [18]. Moreover, for each puncture p∈C , one ﬁnds that the sum of edge
coordinates encircling the puncture is
∑
E ending on p
(
iπ−XE
)
= 2(Λp−iπ), (2.17)
where exp(±Λp) are the holonomy eigenvalues at p. The elements Λ p form a basis for the
center of the Poisson algebra ( 2.16).
Shear coordinates onPC recently featured prominently in the analysis of BPS states and
wall crossing for 4-dimensional N = 2 theories associated to punctures Riemann surfaces C
[16]. In particular, we note that [ 16] considered edge coordinates XE = exp(iπ−XE), which
could be identiﬁed as the exponentiated central charges for a generating set of BPS states in
4d gauge theory. The electric-magnetic pairing of BPS charges was given by ( 2.16).
The simplest example of shear/edge coordinates already ap-
z
z
￿
z
￿￿
w
w
￿
w
￿￿
Figure 10: ∂∆ as a four-
punctured sphere.
peared above, when we described the phase space P∂∆ (2.6) of
an ideal tetrahedron. If we view the boundary ∂∆ as a trian-
gulated four-punctured sphere, we should start with six (log-
arithmic) edge coordinates ( Z,Z′,Z′′,W,W ′,W′′) that obey a
Poisson algebra
{Z,Z′} ={Z′,Z′′} ={Z′′,Z} ={Z,W′}
={Z′,W′′} ={Z′′,W} ={W,Z′} ={W′,Z′′} (2.18)
={W′′,Z} ={W,W′} ={W′,W′′} ={W′′,W} = ℏ,
according to the faces shared by these edges, with all other
brackets vanishing. Then we impose conditions ( 2.17) that the holonomy eigenvalue around
each vertex p is Λp = 2πi — in other words, we require that the holonomy be unipotent:
W +W′ +W′′ =Z +Z′ +W′′ =Z +W′ +Z′′ =W +Z′ +Z′′ =iπ (2.19)
This forces opposite edges to have equal parameters, W =Z, W′ =Z′, W′′ =Z′′, and cuts
down the phase space toP∂∆ ={(Z,Z′,Z′′)|Z +Z′ +Z′′ =iπ}, with Poisson structure (2.7)
4We thank R. Kashaev for ﬁrst making us aware of this connection.
– 13 –
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
z￿
w￿￿
z￿￿
w￿
z￿
y￿￿
z￿￿
y￿
w￿
y￿￿
w￿￿
y￿
z w
y
Figure 11: Forming a bipyramid from three tetrahedra.
As an example involving a nontrivial gluing, we can consider the “bipyramid”M of Figure
