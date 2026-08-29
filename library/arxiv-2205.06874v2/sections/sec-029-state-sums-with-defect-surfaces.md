---
doc_id: arxiv-2205.06874v2
doc_title: "State sum models with defectsbased on spherical fusion categories Catherine Meusburger Department Mathematik Friedrich-Alexander-Universität Erlangen-Nürnberg"
section_id: sec-029-state-sums-with-defect-surfaces
section_title: "State sums with defect surfaces"
section_number: null
pages: 51-59
source_pdf: 2205.06874v2.pdf
source_sha256: 9b41365160c17ab4
doc_brief: "State sum models with defectsbased on spherical fusion categories Catherine Meusburger Department Mathematik Friedrich-Alexander-Universität Erlangen-Nürnberg — We define a"
---
In the following, we assume that all triangulations are generic and transversal at the boundary. Our first
example is a defect sphere without defect lines or vertices embedded inside a 3-ball. We suppose that the
embedding isunknotted in the sense of Zeeman [Ze60]. This means that there is a PL homeomorphism from
the 3-ball to itself that sends the defect sphere to the boundary of a tetrahedron, see also Footnote 1 [Ze60].
Example 6.1. LetM be a 3-ball with an unknotted defect sphere in its interior. Suppose the boundary of
M is labeled by a spherical fusion categoryC and the defect sphere by a(C,D)-bimodule categoryM with a
bimodule trace. Then for all boundary labelingsl∂M, b∂M the state sum ofM is
Z(M,l∂M,b∂M ) = dimM
dimD ·Z (M′,l∂M,b∂M ), (92)
whereM′ is a triangulated 3-ball labeled byC with the same boundary triangulation, but without defects.
Proof. As the defect sphere is unknotted, there is a PL homeomorphism fromM to itself that sendsD to the
boundary of a tetrahedron. By Theorem 5.16, Corollary 5.18 and because different boundary triangulations
are related by elementary shellings and inverse shellings, it is sufficient to prove the claim for the triangulation
j
M
i k
l
h
g
q
m
np
We evaluate the state sum by gluing the polygon diagrams for the four tetrahedra in the triangulation. Gluing
51
the bottom tetrahedron to the three tetrahedra above with identity (66) yields for the rescaled state sum
Z′(M,l∂M,b∂M ) = 1
dimD
∑
m,n,p,q
α,β,γ
dimm dimn dimp dimq p n
m
m q m
g
i k
j
i
h
l k
h
λ
µν ρ
α β
α β
γ γ
Applying identity (67) to eliminate the summation overα, p yields
Z′(M,l∂M,b ) = 1
dimD
∑
m,n,q
β,γ
dimm dimn dimq m
n
m
q
k
h
l
j
g
i
h
k
β β
γ γ
λ
ν
µ ρ
and applying identity (67) to eliminate the summation overβ,n gives
Z′(M,l∂M,b∂M ) = 1
dimD
∑
m,q,γ dimm dimq mq
h
h
i
j
g
kl
γ
γ
ν
ρ
µ
λ
Applying identity (68) to this diagram yields the result
Z′(M,l∂M,b∂M ) = dimM
dimD
h
h
i
j
g
kl
ν
ρ
µ
λ= dimM
dimD ·Z′(M′,l∂M,b∂M ).
52
Note that Example 6.1 yields the usual Turaev-Viro-Barrett-Westbury invariant for a 3-ball without defects,
if one chooses forM a spherical fusion categoryC =D as a bimodule category over itself.
State sums with defect surfaces of genusg≥ 1 are more difficult to compute. We therefore restrict attention
to the spherical fusion categoryC = VecG for a finite groupG from Example 1.1, equipped with a trivial
3-cocycle and the standard spherical structure. The associated Turaev-Viro-Barrett-Westbury state sums are
a special case of the Dijkgraaf-Witten models from [DW90], see also Altschuler and Coste [AC93].
By Example 1.1 simple objects inVecG correspond to group elementsg∈G. For simplicity, we denote them
byg instead ofδg in the following. One hasdim(g) = 1 for allg∈G and dim(C) =|G| as well as
HomC(k,i⊗j)∼= HomC(i⊗j,k )∼=δk(ij)C ∀i,j,k ∈G. (93)
By Examples 1.7 and 1.16, every finite transitiveG×G′op-set X defines an indecomposable semisimple
(VecG, VecG′)-bimodule categoryM with a bimodule trace, whose simple objects are in bijection with elements
of X. In the following, we only consider the case, where the cocycle definingψ∈H2(L, C×) from Example
1.7 is trivial. One hasdim(x) = 1 for allx∈X and dim(M) =|X| as well as
HomM(x,g▷y)∼= HomM(g▷y,x )∼=δx(g▷y)C (94)
HomM(x,y◁g′)∼= HomM(y◁g′,x )∼=δx(y◁g′)C ∀x,y∈X, g∈G, g′∈G′.
Hence, any 6j symbol vanishes, unless for each triangle with edges labeled byx,y ∈ X and byg∈ G or
g′∈ G′, the objectsx and y are related by the action ofg or g′. Similarly, for any triangle with labeled
elements ofG or G′, the oriented product of the group elements must be trivial by(93). Morphism labels for
triangles are just numbers inC, and all sums over bases of morphism spaces become trivial.
Example 6.2. LetC = VecG andD = VecG′ for finite groupsG,G′ andM the indecomposable (C,D)-
bimodule category with bimodule trace defined by a finite transitiveG×G′op-set X.
Let Σ be a closed oriented triangulated surface of genusg≥ 1 and M = [0, 1]× Σ the fine neighbourhood ofΣ
obtained by replacing each triangle inΣ by a prism as in Figure 9, with a defect surface{ 1
2}× Σ labeled by
M and boundary components{1}× Σ and{0}× Σ labeled byC andD. Suppose that all boundary triangles
with non-trivial morphism spaces are labeled with identity morphisms.
Then the rescaled state sum ofM is
Z′(M,l∂M,b∂M ) =



|Xρ(π1(Σ))| if the oriented product of the group elements in each triangle
on{0}× Σ and{1}× Σ is trivial,
0 else,
where ρ :π1(Σ)→G×G′ is the group homomorphism defined by the labels on{0}× Σ and{1}× Σ and
Xρ(π1(Σ)) the fixed point set for the induced action ofπ1(Σ).
In particular:
• trivialdefectsurface: IfG =G′ =X with the standardG×Gop-set structure, thenZ′(M,l∂M,b∂M ) =
0 unless the oriented product of the group elements in each triangle on{0}× Σ and{1}× Σ is trivial
and the associated group homomorphismsρ0,ρ 1 :π1(Σ)→G are conjugated. ThenZ′(M,l∂M,b∂M ) =
|Stab(ρ0)|, where Stab(ρ0) is the stabiliser ofρ0 for the conjugation action ofG on HomGrp(π1(Σ),G ).
• trivial G×G′op-set: For a trivialG×G′-set X ={•}, one hasZ′(M,l∂M,b∂M ) = 1, whenever the
oriented product of the group elements in each triangle on{0}× Σ and{1}× Σ is trivial.
• normal subgroup: If X = G×G′op/N for a normal subgroupN⊂ G×G′op one has Stab(m) =
Stab(m′) =N for allm,m′∈X. This impliesZ′(M,l∂M,b∂M ) =|X|, whenever the oriented product
of the group elements in each triangle on{0}× Σ and{1}× Σ is trivial and the labelings of{1}× Σ
and{0}× Σ define a group homomorphismρ :π1(Σ)→N.
Proof. Orient the top and bottom triangle of each prism as the associated triangle ofΣ, the vertical edges
of each prism according to the orientation ofΣ. Subdivide each prism into three tetrahedra as in Figure 9.
Label its top and bottom edges with elements ofG and G′ and the vertical edges with elements ofX.
53
j′
i′k′
j
ik
m n
p
s q
Σ
r
nm
p
qs
r
i′ j
j
i
k
α
i′
j′k′
α′
λ µ
ν
ρσ
τ
Figure 9: A labeled triangular prism and the associated polygon diagram.
a1
b1
a1
b1
a2
b2
a2
b2
b′
2
a′
2
a′
2
b′
2
b′
1
b′
1
a′
1
a′
1
m
m
m
mm
m
m
m
Figure 10: Polygon diagramP for M = [0, 1]× Σ for triangulated defect surfaceΣ of genus 2.
• The orientation of the blue lines indicates the orientation of the triangulation onΣ.
• The group elements on the unlabeled edges are determined by the labels.
• ev(P ) = 0 unless [a1,b 1]··· [ag,bg] = 1 and [a′
1,b′
1]··· [a′
g,b′
g] = 1 and (ai,a′
i), (bi,b′
i)∈ Stab(m) for i = 1, 2.
54
By Proposition 5.14 the state sum of each labeled prism is given by the evaluation of the polygon diagram in
Figure 9. Also by Proposition 5.14, the state sum forM is given by the evaluation of any polygon diagramP
obtained by gluing the polygons of the prisms to a disc and summing over the objects at its boundary. We
can assume without loss of generality thatP is a 4g-gon with every vertex labeled bym∈X, as in Figure 10.
This yields
Z′(M,l∂M,b∂M ) =
∑
m∈X
ev(P ).
By identity(93), the evaluation ofP vanishes, unless at each vertex ofP that involves only edges labeled by
G or G′, the oriented product of these group elements is trivial. By choosing maximal trees in the graphs
labeled byG and G′, one can express the group elements on the trees in terms of the2g group elements
on edges that intersect∂P, whereg is the genus ofΣ. The labels on these2g edges then define a group
homomorphism ρ :π1(Σ)→G×G′, as shown in Figure 10.
By identity(94) the evaluationev(P ) vanishes unless the group elements(ai,a′
i), (bi,b′
i)∈G×G′op on each
side ofP are contained in the stabiliser ofm∈X or, equivalently, the group homomorphismρ takes values
in Stab(m). In that case, one hasev(P ) = 1. Summation over all elementsm∈X then yields the result.
Example 6.2 gives intuition how the data for the spherical fusion categories interacts with the defect data in
state sums of defect 3-manifolds. The next example shows that state sums for defect surfaces in the interior
of a 3-ball detect the genus of the defect surface.
Example 6.3. LetC = VecG andD = VecG′ for finite groupsG,G′ andM the (C,D)-bimodule category
with bimodule trace defined by a finite transitiveG×G′op-set X. LetM be the triangulated 3-ball from Figure
11 with an embedded defect surface of genusg≥ 1 in its interior. Then
Z(M,l∂M,b∂M ) =|X|·| StabG|g·| StabG′|g
|G′| ·Z (M′,l∂M,b∂M ), (95)
whereM′ is the 3-ball with the same boundary triangulation and labeling, but without defects and|StabG|,
|StabG′| are the cardinalities of the stabilisers for theG- andG′-actions onX.
Proof. The triangulated defect 3-manifold in Figure 11 is constructed as follows:
• take 2g triangular double-pyramids formed by three tetrahedra each, with a cylinder labeled byM
around the interior edge labeled byD,
• glue them pairwise along adjacent top and bottom faces to formg rectangular double-pyramids,
• glue the four bottom faces of each rectangular double-pyramid to the four top faces of the next one,
• glue a rectangular pyramid subdivided into four tetrahedra with defect triangles to the top and the
bottom of the resulting polyhedron.
If the edges are labeled by group elements as in Figure 11, then the edges labeledi,j,k,l,w s,xs,ys,zs∈G
for s = 1, 2 are boundary edges. The edges labeled by dr,d′
r ∈ G′, by cr ∈ G for r = 1,...,g and by
ms,ns,ps,qs,t,b ∈X for s = 1,...,g + 1 are internal, and their labels are summed over. Conditions(93) and
(94) on the morphism spaces imply that the state sum is zero unless the following conditions are met:
• boundary edges of top and bottom pyramid:
xs =ys·i =ws·j, z s =ys·k =ws·l s ∈{ 1, 2}, (96)
• defect edges of top and bottom pyramid:
m1 =x−1
1 ▷t, n 1 =y−1
1 ▷t, p 1 =w−1
1 ▷t, q 1 =z−1
1 ▷t, (97)
mg+1 =x−1
2 ▷b, n g+1 =y−1
2 ▷b, p g+1 =w−1
2 ▷b, q g+1 =z−1
2 ▷b,
• double-pyramids: forr∈{ 1,...,g}
nr =i▷mr =k▷qr, p r =cr▷nr =j▷mr =l▷qr, (98)
mr+1 =mr◁dr, n r+1 =nr◁dr =nr◁d′
r, p r+1 =pr◁dr =pr◁d′
r, q r+1 =qr◁dr =qr◁d′
r.
55
p1
n1
m1
m2
n2
p2
c1
ji
d1
p2
n2
q2
q1
p1
n1
c1 k
l
d′
1
p2
n2
m2
m3
n3
p3
c2
ji
d2
p3
n3
q3
q2p2 n2
c2 k
l
d′
2
c1
c2
k
l
j
i
j
i
k
l
b
t
p3
n3
m3
q3
i
j
k
l
q1
p1
n1
m1
x1 y1
w1
z1
x2 y2
z2w2
x1 y1w1 z1
z2y2x2 w2
Figure 11: Gluing a surface of genusg = 2 inside a 3-ball.
56
Condition (96) just states that the state sum is zero, unless the oriented product over the group elements of
each boundary triangle is trivial. The first condition in (97) and the second condition in (98) imply
mr+1 =x−1
1 ▷t◁d1··· dr qr+1 =w−1
1 ▷t◁d′
1··· d′
r (99)
nr+1 =y−1
1 ▷t◁d1··· dr =y−1
1 ▷t◁d′
1··· d′
r pr+1 =z−1
1 ▷t◁d1··· dr =z−1
1 ▷t◁d′
1··· d′
r
for allr∈{ 1,...,g}. This expressesms,ns,ps,qs∈X as functions oft∈X, d1,...,d g,d′
1,....,d′
n∈G′ and of
the group elements on the boundary edges and eliminates the summation overms,ns,ps,qs. The equations
in the second line of (99) are satisfied simultaneously iff for allr∈{ 1,...,.g}
d′
1··· d′
rd−1
r ··· d−1
1 ∈ StabG′(t) ={g∈G′|t◁g′ =t}. (100)
Combining (99) with the second line in (97) yields
b =w2w−1
1 ▷t◁d1··· dr =x2x−1
1 ▷t◁d1··· dr =y2y−1
1 ▷t◁d1··· dr =z2z−1
1 ▷t◁d1··· dr. (101)
As (96) implies x2x−1
1 =y2y−1
1 =w2w−1
1 =z2z−1
1 , equation(101) just expressesb in terms oft and d1,...,d r
and thus eliminates the summation overb from the state sum. The first line in(98) is then equivalent to
(99), (96) and the additional condition
w1cry−1
1 ∈ StabG(t) ={g∈G|g▷t =t} ∀r∈{ 1,...,g}. (102)
For fixedt and d1,...,d g, the summations overd′
1,...,d′
g and c1,...,c g contribute factors|StabG′(t)|g and
|StabG(t)|g, respectively, to the state sum. AsX is a transitiveG×G′op-set, all stabilisers have the same
cardinality, and the summation overt contributes a factor|X|. As each of theg + 1 internal vertices with
incident edges fromD contributes a factordim(D)−1 =|G′|−1 and the summation overd1,...,d g yields a
factor dim(D)g =|G′|g we obtain
Z′(M,l∂M,b∂M ) =|X||StabG|g|StabG′|g
|G′| C,
where C is a factor that depends only on the labeling of the boundary triangles. ForM =C =D = VecG as
a bimodule category over itself, one has|X| =|G′| =|G|,|StabG| =|StabG′| = 1.
It is instructive to compare Examples 6.1 and 6.3. If one restricts the data in Example 6.1 to the bimodule
category given by a finiteG×G′op-set X from Example 6.3, then formula(92) for the state sum of a 3-ball
with a defect sphere becomesZ(M,l∂M,b∂M ) =|X|/|G′|·Z (M′,l∂M,b∂M ), which is formula(95) for g = 0.
Examples 6.1 to 6.3 show that the state sums detect properties of the bimodule categories labeling a defect
surface and properties of the surface. The next example shows that the state sum models with defects depend
on theembeddings of defect surfaces into the 3-manifold, and not just on their topology.
This is manifest even for very simple non-trivial defect data. By taking a tubular neighbourhood of a knot
K embedded intoS3 and labeling it with theVecG-module category defined by a trivialG-set, one obtains
a triangulation of the knot complement with trivial data at the boundary. The associated state sum gives
the number of conjugacy classes of group homomorphismsρ :π1(S3\K)→G and hence is sensitive to the
embedding of the toroidal defect surface.
Example 6.4. LetK⊂S3 be a knot, realised as a subgraph of the dual cell complex of a triangulationT of
S3. LetM be the triangulated 3-manifold with defect data constructed as follows:
1. RefineT to a triangulationT′ by applying a 1-4 move to each tetrahedront in T with t∩K̸=∅ and a
stellar move to each triangle∆ in T with ∆∩K̸=∅, such thatK connects the midpoints of two faces
of t with the vertex in its interior, as shown in Figure 12.
2. Form a tubular neighbourhood ofK by inserting a defect plane as in Figure 2 (b) into each tetrahedron
of T′ that contains an edge inK and a defect plane as in Figure 2 (a) into each tetrahedron ofT′ that
contains a vertex, but not an edge ofK, as shown in Figure 12.
3. Label the region ofT′ that does not containK withC = VecG for a finite groupG and the region
containingK with the spherical fusion categoryD = Vec{1} = VectC. Label the defect surface with the
(C,D)-bimodule categoryM defined by the trivialG-set X ={•}.
57
g1
g2
g3
g5
g4
g6
Figure 12: A piece of a knot (red) in the dual complex of a triangulation and the associated defect surface.
The state sum vanishes unlessg3 =g1g2 and g5 =g1g4.
Then the state sum ofM is the number of conjugacy classes of group homomorphisms from the fundamental
groupπ1(S3\K) into G
Z(M) =|HomGrp(π1(S3\K),G )/G|.
Proof. Denote byrC the region labeled byC = VecG. By subdividing the triangulation as in Lemma 5.7, we
can assume that each vertex, edge or triangle inT′ that contained inrC is part of a tetrahedron contained
in rC. This does not change the state sum by Theorem 5.16. The union of the tetrahedra inrC is then PL
homeomorphic to the knot complementS3\K′, whereK′ is a solid torusS1×D2 embedded as a tubular
neighbourhood ofK. This defines a triangulationT′′ of S3\K′ labeled by VecG.
The remaining tetrahedra are as in Figure 12. By construction, all red edges in Figure 12 are labeled with
the simple objectC of VectC, all blue edges by the simple object• inM, while the black edges are labeled
with elements ofG. Each triangle∆ with ∆∩t̸=∅ has two edges labeled by•, one edge labeled by a group
elementg∈G and is assigned the morphism spaceHom(•,•)∼= C for anyg∈G. The triangles∆ in Figure
12 with ∆∩D =∅ are part of tetrahedra contained inrC. Their labeling is determined by the labeling ofT′′,
and their morphism spaces areHom(∆)∼= C if the oriented product of the group elements on their edges is
trivial and Hom(∆)∼={0} else.
Let l :E′′→G be a labeling of the oriented edges ofT′′ with elements ofG. As each triangle inT′ occurs in
exactly two tetrahedra and all morphism spaces are zero- or one-dimensional, the product of all generalised
6j symbols inT′ is one if the oriented product of the group elements on each triangle∆ in T′′ vanishes and
zero else. It follows that the state sum is proportional to the number of labelingsl that satisfy this condition
Z(M) =|{l :E′′→G| Πe∈fl(e) = 1∀f∈ ∆′′}|
|G||V′′| , (103)
where V′′, E′′ and ∆′′ are the sets of vertices, edges and triangles ofT′′.
Every such labelingl defines a group homomorphismρl :π1(S3\K)→G, and every group homomorphism
ρ :π1(S3\K)→G is obtained from such a labeling. The group homomorphismsρl,ρl′ for two labelings
l,l′ :E′′→G are conjugate iff there is a mapf :V′′→G, v↦→gv such thatl′(e) =gt(e)·l(e)·gs(e) for all
e∈E′′, wheres(e) and t(e) denote the starting and target vertex ofe. This shows thatZ(M) is the number
of conjugacy classes of group homomorphismsρ :π1(S3\K)→G.
Although the data in Example 6.4 is quite trivial, it shows that the state sum with defects can distinguish
non-isotopic embeddings of surfaces. It would be interesting to investigate this further and to see if it can
distinguish knotted embeddings of spheres.
58
