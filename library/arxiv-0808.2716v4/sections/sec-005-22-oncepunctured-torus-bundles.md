---
doc_id: arxiv-0808.2716v4
doc_title: "CUSP AREAS OF F AREY MANIFOLDS"
section_id: sec-005-22-oncepunctured-torus-bundles
section_title: "Once–punctured torus bundles"
section_number: 2.2
pages: 7-10
source_pdf: 0808.2716v4.pdf
source_sha256: ea66f7ddcf9e9fe6
doc_brief: "CUSP AREAS OF F AREY MANIFOLDS — This paper gives the ﬁrst explicit, two–sided estimates on t he cusp area of once– punctured torus bundles, 4–punctured sphere bundles, and 2 –bridge link"
---
with monodromy ϕ. The mapping class group of the punctured torus is isomorphi c to
8 D. FUTER, E. KALF AGIANNI, AND J. PURCELL
Figure 2. Copies of ideal tetrahedra in the cover ( R2/integerdivideZ2) × R of T × R.
SL2(Z). By a well–known argument that we recall below, either ϕ or −ϕ is conjugate to an
element of the form
Ω = Ra1Lb1 · · ·RasLbs,
where ai,b i are positive integers, and R and L are the matrices
R :=
[
1 1
0 1
]
, L :=
[
1 0
1 1
]
.
Moreover, Ω is unique up to cyclic permutation of its letters .
By projecting ϕ down to PSL 2(Z) ⊂ Isom(H2), we may view the matrix ±ϕ as an
isometry of H2 in the upper half–plane model, where the boundary at inﬁnity of H2 is
R ∪ {∞}. Then the slopes of the eigenvectors of ϕ are the ﬁxed points of its action on
H2.
Now, subdivide H2 into ideal triangles, following the Farey tesselation F. In this tessela-
tion, every vertex is a rational number (or ∞) in ∂H2. Each such vertex corresponds to a
slope on the punctured torus T , that is, an isotopy class of arcs running from the puncture
to itself. Two vertices are connected by an edge in F if and only if the corresponding arcs
can be realized disjointly. Thus an ideal triangle of F corresponds to a triple of disjoint arcs,
which gives an ideal triangulation of T . The monodromy ϕ naturally acts on F.
There is an oriented geodesic γϕ running from the repulsive ﬁxed point of ϕ to its at-
tractive ﬁxed point. This path crosses an inﬁnite sequence o f triangles of the Farey graph
(...,t −1,t 0,t 1,t 2,... ). We can write down a bi-inﬁnite word corresponding to ϕ, where the
k-th letter is R (resp. L) if γϕ exits the k-th triangle tk to the right (resp. left) of where
it entered. This bi-inﬁnite word will be periodic of period m, where m is some integer such
that t0 is taken by ϕ to tm. Then letting Ω be any subword of length m, and substituting
the matrices above for R and L, we ﬁnd that ±Ω is conjugate to ϕ.
Next, we review the relation between the word Ω and the triang ulation of Vϕ . The path γϕ
through the Farey graph determines a sequence of triangulat ions of the punctured torus T .
Every time γϕ crosses an edge e ⊂ F , moving from one triangle of F to an adjacent triangle,
we change one ideal triangulation of T (call itτ−(e)) into a diﬀerent ideal triangulation τ+(e),
replacing a single edge with another. In other words, we are p erforming a diagonal exchange
in a quadrilateral of T . This diagonal exchange determines an ideal tetrahedron ∆( e) as
follows. The boundary of the tetrahedron is made up of two ple ated surfaces homotopic to
T , with triangulations corresponding to τ−(e) and τ+(e). These two pleated surfaces are
glued together along the two edges in T where τ−(e) and τ+(e) agree. The result is an ideal
tetrahedron. See Figure 2.
CUSP AREAS OF F AREY MANIFOLDS 9
R
L
R
R
R
R
L
L
L
L
Figure 3. Zigzags on the boundary torus of a punctured torus bundle. Th e
pleated surfaces in this ﬁgure correspond to a sub-word RL4R4L ⊂ Ω.
If γϕ crosses the edges ei, ei+1, then we may glue ∆( ei) to ∆( ei+1) top to bottom, since
τ+(ei) = τ−(ei+1). Thus γϕ determines a bi-inﬁnite stack U of tetrahedra. U is homeo-
morphic to T × R, and there is an orientation–preserving homeomorphism Φ of U , taking
the i-th tetrahedron to the ( i +m)-th tetrahedron, acting as ϕ on T . The quotient U/Φ is
homeomorphic to Vϕ , and gives a triangulation of Vϕ into m ideal tetrahedra. This is the
Floyd–Hatcher triangulation of Vϕ , also called the monodromy triangulation.
We summarize the discussion above as follows.
(1) The monodromy ϕ of the bundle is conjugate to a word
Ω = ±Ra1Lb1 · · ·RasLbs.
(2) Each letter R or L corresponds to a triangle in the Farey tesselation of H2.
(3) Each letter R or L corresponds to a pleated surface homotopic to T , pleated along
arcs whose slopes are the vertices of the corresponding tria ngle of the Farey graph.
This pleated surface forms the boundary between two tetrahe dra of the canonical
triangulation of Vϕ .
Deﬁnition 2.1. Let Ω = ±Ra1Lb1...R asLbs. A syllable of Ω is deﬁned to be a subword Rai
or Lbi. That is, a syllable is a maximal string of R’s orL′s in the word Ω.
A punctured torus bundle is a manifold with a single torus bou ndary component. It is
often convenient to work with the universal cover H3 of the bundle, seen as the upper half
space model, with the boundary lifting to the point at inﬁnit y in this model. Each of the
pleated surfaces corresponding to the letters R and L will lift to H3. Their intersection
with the boundary of a maximal cusp gives a triangulation of t he boundary which is well
understood. In particular, these intersections give a coll ection of zigzags that determine a
triangulation of the boundary with combinatorics speciﬁed by the word Ω. See Figure 3.
Deﬁnition 2.2. A zigzag is deﬁned to be the lift of one of the pleated surfaces corresp onding
to R or L to the universal cover H3, with the cusp lifting to inﬁnity.
Note that in pictures of zigzags, as in Figure 3, the vertices of the zigzag correspond to
edges in H3 along which these zigzags meet. To distinguish separate zig zags, it is conventional
to split them apart at the vertices. (In the manifold M , a sequence of pleated surfaces
10 D. FUTER, E. KALF AGIANNI, AND J. PURCELL
corresponding to a syllable of Ω will meet along a single edge . Thus, in a more topologically
accurate but less enlightening picture, one would collapse together the split–apart vertices
in Figure 3. See also [31, Figure 4].)
Akiyoshi [6], Lackenby [38], and Gu´ eritaud [30] have indep endently proved that this tri-
angulation is geometrically canonical, i.e. dual to the For d domain. As a result, each edge
of the triangulation runs through the geometric center of a f ace of the Ford domain. (More
precisely, each face of the Ford domain lifts to a hemisphere in H3, and each edge of the
triangulation runs through the geometric center of the hemi sphere.) Thus, when viewed
from inﬁnity, the “corners” of the zigzag lie over centers of hemispheres projecting to faces
of the Ford domain. We will use this extensively below. See, f or example, Figure 8 below.
