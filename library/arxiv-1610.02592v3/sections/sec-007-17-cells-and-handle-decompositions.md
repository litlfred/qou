---
doc_id: arxiv-1610.02592v3
doc_title: "An Introduction to Geometric Topology Bruno Martelli arXiv:1610.02592v3 [math.GT] 5 Apr 2022"
section_id: sec-007-17-cells-and-handle-decompositions
section_title: "Cells and handle decompositions"
section_number: 1.7
pages: 45-53
source_pdf: 1610.02592v3.pdf
source_sha256: 81020523d7d2bc1a
doc_brief: "An Introduction to Geometric Topology Bruno Martelli arXiv:1610.02592v3 [math.GT] 5 Apr 2022 — 68 sections: Introduction; Differential topology; Riemannian geometry"
---
WhenM is closed and has even dimension2n, the central form
ω :Hn(M, Z)×Hn(M, Z)−→ Z
is symmetric or skew-symmetric, depending on whethern is even or odd.
Everything we said about fundamental classes, Lefschetz duality, and in-
tersection forms holds for non-orientable manifolds as well, provided that we
pickR = Z/2Z and consider bilinear forms and intersections inZ/2Z.
1.7. Cells and handle decompositions
Many nice topological spaces can be constructed iteratively starting from
ﬁnitely many points and then attaching some discs of increasing dimension
called cells. When the topological space is a diﬀerentiable manifold one typi-
cally thickens the cells tohandles.
Cells and handles are beautifully introduced by Hatcher [25] and Kosinksi
[34], respectively.
1.7.1. Cell complexes. A ﬁnite cell complexof dimensionn (brieﬂy, a
n-complex) is a topological space obtained iteratively in the following manner:
• a 0-complexX0 is a ﬁnite set of points,
• an-complexXn isobtainedfroma (n−1)-complexXn−1 byattaching
ﬁnitely manyn-cells, that is copies ofDn glued along continuous
mapsϕ:∂Dn→Xn−1.
The closed subsetXk⊂Xn is thek-skeleton ofXn, for allk <n.
Proposition 1.7.1. Let X be an-complex. The inclusion mapXk ↪→ X
induces an isomorphismπj (Xk)→πj (X) for allj <k.
Proof. By transversality, mapsSj→X and homotopies between them can
be homotoped away from cells of dimension>j + 2. □
In particular, the spaceX is connected if and only ifX1 is, and its funda-
mental group is captured byX2.
Theorem 1.7.2. Every diﬀerentiable compactn-manifold may be realised
topologically as a ﬁniten-complex.
A presentation for the fundamental group of a cell complexX can be
constructed as follows. Ifx0∈X0, we ﬁx a maximal treeT⊂X1 containing
x0 and equip thek arcs inX1\T with some arbitrary orientations. These arcs
determine some generatorsg1,...,g k∈π1(X,x 0). The boundary of a2-cell
makes a circular path inX1: every time it crosses an arcgi in some direction
(entering from one side and exiting from the other) we write the corresponding
letterg±1
i and get a word. Thes two-cells produces word relations. We have
constructed a presentation forπ1(X).
38 1. PRELIMINARIES
1.7.2. Euler characteristic. The Euler characteristic of an-complex X
is the integer
χ(X) =
n∑
i=0
(−1)iCi
whereCi is the number ofi-cells inX. It is also equal to
χ(X) =
n∑
i=0
(−1)ibi (X)
wherebi (X) is thei-th Betti number ofX. Thereforeχ(X) is a number which
depends only on the topology ofX, that can be easily calculated from any cell
decomposition ofX.
Proposition 1.7.3. If ˜X→ X is a degree-d covering of ﬁnite complexes
thenχ( ˜X) =d·χ(X).
Proof. Ak-cell inX is simply-connected and hence lifts tod distinct k-
cells in ˜X. A cell decomposition ofX thus induces one of˜X where the numbers
Ci are all multiplied byd. □
It is much harder to control homology under coverings. The Euler char-
acteristic of a closed manifold measures the obstruction of constructing a
nowhere-vanishing vector ﬁeld.
Theorem1.7.4. Acloseddiﬀerentiablemanifold M hasanowhere-vanishing
vector ﬁeld if and only ifχ(M) = 0.
1.7.3. Aspherical cell-complexes. A ﬁnite cell complex is locally con-
tractible and hence has a universal cover˜X. If ˜X is contractible the complex
X is calledaspherical.
Example 1.7.5. If a closed manifoldM is covered byRn, it is aspherical.
By a theorem of Whitehead, a ﬁnite cell complexX is aspherical if and
only if all its higher homotopy groupsπi (X) withi> 2 vanish.
The following theorem says that maps to aspherical spaces are determined
(up to homotopy) by homomorphisms between fundamental groups.
Theorem 1.7.6. Let (X,x 0), (Y,y 0) be pointed connected ﬁnite cellular
complexes. If Y is aspherical, every homomorphismπ1(X,x 0)→π1(Y,y 0) is
induced by a continuous map(X,x 0)→ (Y,y 0), unique up to homotopy.
Proof. We construct a continuous mapf : Xk → Yk iteratively on the
k-skeleta, starting fromk = 1.
LetT be a maximal tree inX1. The oriented 1-cellsg1,...,g k inX1\T
deﬁne generators inπ1(X,x 0). We deﬁnef : X1→ Y 1 by sendingT to y0
and eachgi to any loop inY representing the image ofgi along the given
homomorphismπ1(X,x 0)→π1(Y,y 0).
1.7. CELLS AND HANDLE DECOMPOSITIONS 39
The mapf sends the boundary of each 2-cell to a homotopically trivial
loop inY and hence extends to a mapf : X2→ Y 2. Since Y is aspherical,
the higher homotopy groupsπi (Y ) withi> 2 vanish and hencef extends to
a mapf :Xk→Yk iteratively for allk> 3.
Weprovethat f isuniqueuptohomotopy. Let f′ beamapthatrealisesthe
given homomorphism on fundamental groups. We can construct a homotopy
betweenf andf′ iteratively onXk as follows.
Fork = 1, we can suppose that bothf andf′ sendT toy0. By hypothesis
they send the generatorsgi to homotopic loops, hence we can homotopef′
to f on X1. For k > 2, the mapsf and f′ on eachk-cell are homotopic
because they glue to a mapSk→Y, which is null-homotopic becauseπk(Y )
is trivial. □
Corollary 1.7.7. Let X and Y be connected ﬁnite aspherical complexes.
Every isomorphismπ1(X)→ π1(Y ) is realised by a homotopic equivalence
X→Y, unique up to homotopy.
In particular the homotopy type of an aspherical manifold is fully deter-
mined by its fundamental group.
Corollary 1.7.8.Twoasphericalclosedmanifoldsofdistinctdimensionhave
non-isomorphic fundamental groups.
Proof. Two closed manifolds of diﬀerent dimension cannot be homotopi-
cally equivalent because they have non-isomorphic homology groups. □
We cite for completeness this result, although we will never use it.
Theorem 1.7.9 (Cartan–Hadamard).A complete Riemannian manifoldM
with sectional curvature everywhere⩽ 0has a universal covering diﬀeomorphic
to Rn and is hence aspherical.
Sketch of the proof. Pick a pointx∈M. SinceM is complete, the expo-
nential map expx :TxM→M is deﬁned onTxM. The fact that the sectional
curvatures are⩽ 0 imply that (d expx )y is invertible for anyy∈Tx and expx
is a covering. □
At a single point in this book we will need the following theorem.
Theorem 1.7.10.The fundamental group of an aspherical manifoldM has
no torsion.
Sketch of the proof. Up to passing to a cover, it suﬃces to consider the
case π1(M) ∼= Z/nZ for some n > 2. This case is excluded because the
cohomology ofM is isomorphic to the (suitably deﬁned) cohomology ofZ/nZ,
which has however inﬁnite dimension. □
40 1. PRELIMINARIES
M N
X Y
M
X Y
N M N
Figure1.5. Togluetwosmoothmanifoldsalongportionsoftheirbound-
aries (left) we pick a collar for these portions (centre), then we remove
X,Y and identify the interiors of the collars (right).
Figure 1.6. Two 0-handles (yellow), two 1-handles (orange), and one
2-handle (red) in dimension 2 (left). Two 0-handles (yellow) and one
1-handle (orange) in dimension 3 (right).
1.7.4. Gluing portion of boundaries. Every compact diﬀerentiablen-
manifold M can be obtained topologically as a ﬁnite complex. The ﬁnite
complex structure is however not designed to describe the smooth structure
ofM, and for that purpose it is better to replacek-cells with some thickened
objects called k-handles. These handles are n-discs glued iteratively along
portions of their boundaries. Before describing them, we brieﬂy explain how
smooth manifolds can be glued along portions of their boundaries.
LetM andN be twon-manifolds with boundary andX⊂∂M,Y ⊂∂N be
two compact(n− 1)-submanifolds with boundary. A diﬀeomorphismϕ:X→
Y deﬁnes a topological space
M∪ϕN
that may be promoted to a diﬀerentiable manifold: it suﬃces to use a collar
as in Section 1.1.12, see Figure 1.5. The glued manifold depends (up to
diﬀeomorphism) only on the isotopy class ofϕ.
1.7.5. Handles. LetM be a (possibly empty or disconnected)n-manifold
withboundaryand 0⩽k⩽n. Ak-handle isamanifold Dk×Dn−k attachedto
M along some diﬀeomorphismϕ:∂Dk×Dn−k→Y ⊂∂M, hence producing
a new manifoldM′.
For instance, a0-handle is aD0×Dn = Dn attached to nothing, since
∂D 0 = ∅. This means that attaching a 0-handle toM consists of adding a
disjoint discDn to it. For instance, by attaching a 0-handle to the empty set
we create a discDn out of nothing.
1.7. CELLS AND HANDLE DECOMPOSITIONS 41
A 1-handleisa D1×Dn−1 attachedalong ∂D 1×Dn−1 =S0×Dn−1, thatis
two copies ofDn−1. Some examples in dimensionn = 2, 3 are shown in Figure
1.6. A 2-handle is aD2×Dn−2 attached along∂D 2×Dn−2 =S1×Dn−2.
Whenn = 2 this is a disc attached along its boundary, see Figure 1.6-(left).
1.7.6. Handle decompositions. A sequence of handle attachments
∅↝M1↝... ↝Mk =M
starting from the empty set and producing a compact manifoldM with (pos-
sibly empty) boundary is called ahandle decomposition for M. Using Morse
theory one proves the following.
Theorem 1.7.11.Every compact manifold (possibly with boundary) can be
obtained from a handle decomposition.
Example 1.7.12. The discDn has an obvious handle decomposition con-
sistingofasingle 0-handle. Italsohasmorecomplicatehandledecompositions,
as Figure 1.6 shows.
By transversality, handles may always be reordered so that the lower in-
dex handles are attached ﬁrst, and handles of the same index are attached
simultaneously. So we can think of a decomposition as the appearing of some
0-handles, then the simultaneous attaching of some 1-handles, then of some
2-handles, and so on.
A handle decomposition of a closed manifold may be turned upside down,
by reversing all arrows and interpreting everyk-handle as a(n−k)-handle.
Proposition 1.7.13. Every compact connected manifoldM has a handle
decomposition with one0-handle and at most onen-handle.
IfM has a handle decomposition withni handles of indexi then
χ(M) =
n∑
i=0
(−1)ini.
1.7.7. Triangulations. Instead of decomposing a manifold into handles,
one may decide to decompose it into simplexes as in Figure 1.7. One such
decomposition is called a triangulation: we now give a formal deﬁnition.
An (abstract and ﬁnite)simplicial complex is a ﬁnite setS of vertices
togetherwithaset X ofsubsetsof S, calledfaces, whichcontainsallsingletons
and such that every subset of a face is also a face. A face of cardinalityk + 1
has dimension k.
A simplicial complexX has a topological realisation|X|, in which every
faceF∈X of dimensionk transforms into ak-simplex with vertices inF (we
get a cell complex). The complexX is purely n-dimensional if every face is
contained in a face of dimensionn. This implies that|X| is the union of its
n-simplexes.
42 1. PRELIMINARIES
Figure 1.7. A triangulated torus.
Let nowM be a diﬀerentiablen-manifold. A smoothk-simplex inM is a
subset ∆⊂ M diﬀeomorphic to ak-simplex in Rn (we mean that there is a
diﬀeomorphism between open neighbourhoods of∆ and of the simplex sending
the ﬁrst to the second). Asmooth triangulationofM is a puren-dimensional
simplicial complexX together with a homeomorphism between|X|andM that
transforms everyk-simplex inX into a smoothk-simplex inM.
Theorem 1.7.14.Every compact manifold with (possibly empty) boundary
has a smooth triangulation.
Handle decompositions are often more ﬂexible and eﬃcient than triangula-
tions, but triangulations have a more combinatorial nature and can for instance
be handled by a computer. Both constructions are widely used.
On a simplicial complexX, thestar of a vertexv is the set of all simplexes
containingv plus all their sub-simplexes; thelink ofv is the subset of the star
consisting of the simplexes that do not containv. Topologically, the star ofv
is a closed neighbourhood ofv homeomorphic to a cone on its link.
1.7.8. Hypersurfaces and cohomology. The techniques introduced in
this chapter furnish another characterisation of the ﬁrst cohomology group
of a manifold. Let [X,Y ] denote the homotopy classes of continuous maps
X→Y.
Proposition 1.7.15. LetX be a cell complex. There is a canonical identi-
ﬁcation
H1(X; Z) = [X,S 1].
Proof. We know that H1(X; Z) = Hom( π1(X), Z). The circle S1 is
aspherical with π1(S1) = Z, so by Theorem 1.7.6 every homomorphism
π1(X)→π1(S1) is realised by a mapX→S1, unique up to homotopy. □
We have noted that an orientedk-submanifoldS⊂M determines a class
[S]∈ Hk(M, Z). It is natural to ask whether every homology class may be
1.7. CELLS AND HANDLE DECOMPOSITIONS 43
represented by an oriented submanifold: this is false in general, but it is true
in codimension one.
Proposition1.7.16. LetM beacompactoriented n-manifoldwith(possibly
empty) boundary. Every class inHn−1(M,∂M ; Z) is represented by an oriented
properly embedded hypersurfaceS⊂M.
Proof. We have
Hn−1(M,∂M ; Z) =H1(M; Z) = Hom(π1(M), Z) = [M,S 1].
Every mapM→ S1 is homotopic to a smooth map, hence each classα∈
H1(M, Z)is represented by a smooth mapf :M→S1. By Sard’s lemma there
is a regular valuex∈S1, whose counter-imageS =f−1(x) is a hypersurface,
transversely oriented byf and hence oriented (sinceM is).
To prove that[S] =α we verify that[S] andα act onπ1(M) in the same
way. Pick a loopγ∈π1(M) transverse toS. The numberα(γ) is the degree
off◦γ, that is the number of timesf◦γ crossesx counted with signs, which
equals the number of timesγ crossesS counted with signs. □
Proposition 1.7.17. An oriented connected properly embedded hypersur-
faceS⊂M is separating if and only if[S]∈Hn−1(M,∂M ; Z) is trivial.
Proof. The surfaceS is separating if and only ifS·α = 0 for every loopα
transverse toS (exercise). Sinceω([S], [α]) =S·α andω is non-degenerate
(see Section 1.6.3), this holds precisely when[S] = 0. □
1.7.9. Topological discs. Finally, we mention a purely topological theo-
rem that will be used only at one point in this book, in Chapter 8.
Theorem 1.7.18.LetM be a compact topological manifold, whose interior
and boundary are homeomorphic respectively toBn and Sn−1. Then M is
homeomorphic toDn.
Proof. We use two important theorems on topological manifolds, whose
proofs can be found in the ﬁrst chapter of the bookTopological embeddings
of Rushing [51].
As in every compact topological manifold, the boundary∂M has a topo-
logical collar by a theorem of Brown (see Theorem 1.7.4 in that book). The
interior boundary sphere of the collar is contained inint(M)∼=Bn and hence
bounds a closed disc by the Generalised Schönﬂies Theorem (see Theorem
1.8.2 there). The manifold M is obtained by collaring a closed disc and is
hence a closed disc. □
CHAPTER 2
Hyperbolic space
In every dimensionn> 2 there exists a unique simply connected complete
Riemannian manifold with constant sectional curvature1, 0, or−1. These are
the sphereSn, the Euclidean spaceRn, and the hyperbolic spaceHn.
ThesemanifoldsarethethreemostimportantspacesinRiemanniangeom-
etry. We introduce in this chapter the least familiar and the most interesting
of the three: hyperbolic space.
