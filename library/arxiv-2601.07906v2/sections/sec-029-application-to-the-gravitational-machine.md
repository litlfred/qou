---
doc_id: arxiv-2601.07906v2
doc_title: "A universal sum over topologies in 3d gravity"
section_id: sec-029-application-to-the-gravitational-machine
section_title: "Application to the gravitational machine"
section_number: null
pages: 93-98
source_pdf: 2601.07906v2.pdf
source_sha256: e69b1bf37f2c75b0
toc_source: outline
doc_brief: "A universal sum over topologies in 3d gravity — We explore the sum over topologies in AdS3 quantum gravity and its relationship with the statistical interpretation of the boundary theory."
---
Application to the gravitational machine
The fundamental groups of the gravitational machine are changed by gluing opera-
tions along 2-punctured spheres (or cylinders). By repeatedly applying this gluing,
the fundamental group of the resulting manifolds can be precisely described using
– 93 –
graph of groups where all the vertex groups are free groups (since these correspond to
handlebodies) and all the edge groups are Z (since we are gluing along 2-punctured
spheres). By the condition a), all boundary monomorphisms ∂±
e are injective, so the
graphs of groups are well defined. The main purpose of the theory introduced above
is now that we can construct the Bass-Serre covering tree and study the action of
the fundamental group acting on it. We use this technology to prove two results:
Result 1: Given the amalgamated product G = G1 ∗H G2, if H is malnormal
in G1, then the centralizer C(g) = {h ∈G | gh = hg} is either infinite cyclic or
conjugate to a subgroup of G1 or G2. Namely, C(g) ∼= Z or there is an injective
homomorphism from C(g) to G1 or G2.
Result 2: Given the HNN extension G = G1∗H∼K, if H is malnormal in G1,
and H ∩g1Kg−1
1
= {1} for all g1 ∈G1, then C(g) is either infinite cyclic or
conjugate to a subgroup of G1.
These two results will follow from the following observation: for the group G satisfy-
ing the assumptions above, the action of G on its Bass-Serre tree T is 2-acylindrical,
i.e. diam(Fix(g)) ⩽2 for every g ∈G, g̸ = 1. The diameter defined here is the
maximum distance between any two vertices ˜v, ˜w which are fixed by the action of
g ∈G on T. Intuitively, this means that when G acts on T, it only stabilizes a small
portion of the tree.
We present the proof of these results in three parts. First, we show that G acting
on T is 2-acylindrical. Recall that for a given g ∈G, its action on the tree is either
hyperbolic or elliptic. In the second and third parts we show that, in either case,
C(g) is either infinite cyclic or conjugate to G1 or G2. The first result is not new and
appears in [97]. To the best of our knowledge, the second result has not been stated
in this form.
Part I: Fixed-point sets.
For G a group acting on a tree T, let Fix(g) the set
of vertices fixed by g. On T, there is a natural metric given by the number of edges
between two vertices. Fix(g) is a subtree since for any two fixed vertices, the group
action necessarily has to fix the geodesic connecting the two vertices. Let
diam(Fix(g)) = sup{d(˜x, ˜y) | ˜x, ˜y ∈Fix(g)}
(B.20)
the diameter of the fixed point set. The action of a group on a tree T is called
k-acylindrical if for all g̸ = 1, diam(Fix(g)) ⩽k. Note that the centralizer C(g) maps
Fix(g) to Fix(g). Indeed, for ˜v ∈Fix(g) and c ∈C(g), g c˜v = c g˜v = c˜v and so
c˜v ∈Fix(g).
Consider now the case of the amalgamated product G = G1 ∗H G2 with H
malnormal in G1. We show that the group action on the associated Bass-Serre tree
– 94 –
T is 2-acylindrical. Suppose a portion of the tree of the form
gG2
gG1 = g′G1
g′G2
gH
g′H
(B.21)
is fixed by some group element. For such a portion of the graph, we have g−1g′ ∈
G1 \ H. The stabilizers of the edges are Stab(gH) = gHg−1, Stab(g′H) = g′H(g′)−1.
Thus the group element has to live in the intersection of both edge stabilizers, but
this is impossible due to the malnormality of H in G1. Indeed, if ˜g ∈Stab(gH) ∩
Stab(g′H), there are h, h′ ∈H such that
ghg−1 = ˜g = g′h′(g′)−1,
thus
h = (g−1g′)h′(g−1g′)−1,
(B.22)
which by malnormality means that h = 1 = h′ (since g−1g′ ∈G1\H). Thus the fixed-
point set cannot contain any interior red vertex. Note that the opposite orientation,
with an interior blue vertex, could in principle be fixed by g, since we do not assume
H is malnormal in G2. However, since edges only connect red and blue vertices, we
conclude that diam(Fix(g)) ⩽2 for any g ∈G.
We can make a similar observation for the HNN case. There are three non-
equivalent configurations to consider. By the same argument as above, the fixed-
point set of g cannot contain the corresponding portion
gtG1
gG1 = g′G1
g′tG1
gH
g′H
(B.23)
since H is malnormal in G1.
Consider now a portion of the form
gt−1G1
gG1 = g′G1
g′tG1
gt−1H
g′H
,
(B.24)
where t is the stable letter. Elements ˜g that stabilize this portion of the tree must
be in the stabilizers (gt−1)H(tg−1) and g′H(g′)−1, which means that there exist h, h′
such that
gt−1 h tg−1 = ˜g = g′h′(g′)−1,
hence
t−1ht = (g−1g′)h(g−1g′)−1.
(B.25)
Recall that t−1ht ∈K = ∂+(H) and g−1g′ ∈G1. By the assumption that H ∩
g1Kg−1
1
= {1} for all g1 ∈G1, it follows that h = 1 = h′.47 Thus, such a portion can
47Here, we are also using the fact that the homomorphism G1 →G induced by the inclusion of
G1 in its HNN extension is injective. Thus H ∩g1Kg−1
1
= {1} with g1 ∈G1 being trivial in G1
means the intersection is also trivial in G.
– 95 –
also not be part of the fixed-point set. The largest possible fixed-point set is then of
the form
gt−1G1
gG1 = g′G1
gt−1G1
gt−1H
g′t−1H
(B.26)
and thus also diam(Fix(g)) ⩽2 and the action on T is 2-acylindrical.
Part II: Centralizer of hyperbolic elements.
We start with the case where g
is a hyperbolic element of a group G whose action on the tree T is k-acylindrical.
We prove that C(g) is infinite cyclic.
By definition, g translates along a unique geodesic L ⊂T, that is, gL = L. Let
c ∈C(g), then the geodesic cL is also fixed by g, since g cL = c gL = cL. Since
the geodesic fixed by g is unique, it follows that cL = L. Since the group G acts
on the tree as an isometry (i.e. the action preserves distances) we have the following
homomorphism between the centralizer and the group of isometries of the integer
line
φ : C(g) −→Isom(L)
(B.27)
where c gets mapped to the isometry induced by the action cL. The kernel of this
map corresponds to the elements of c which fix the geodesic L point-wise. Thus, if
c ∈kerφ then c fixes infinitely many points, so diam(Fix(c)) = ∞. This contradicts
the k-acylindricity of the action of G. Therefore φ is injective.
The group Isom(L) consists of translations along L and possibly reflections
around vertices (depending on the orientation of the edge arrows). Suppose c ∈C(g)
corresponds to a reflection. But g translates along the geodesic and cgc−1 translates
along the geodesic in the other direction. Since g = cgc−1 this is impossible. Thus,
the image of the homomorphism φ has to lie in the translation subgroup along L,
which is isomorphic to the integers. We conclude that C(g) is an infinite cyclic group.
Part III: Centralizer of elliptic elements.
Finally, we consider the case where
g is an elliptic element, and thus fixes a vertex ˜v. For this part we will need the
following fact about finite trees, we include a derivation of this result at the end of
the section. Let T ′ be a tree with finite diameter, i.e.
diam(T ′) = sup
˜u, ˜w∈T ′ d(˜u, ˜w) < ∞,
(B.28)
and G′ a group acting on T ′. Then there is one vertex ˜u∗∈T ′ that is fixed by every
element g′ ∈G′. In particular all elements of G′ are elliptic.
Returning to the proof, we assume that g is an elliptic element of a group G whose
action on the tree T is k-acylindrical. Thus, Fix(g) at least contains one vertex ˜v
and is a non-empty subtree T ′ ⊂T. Since the action is k-acylindrical, Fix(g) has
finite diameter. Hence, the group C(g) acts on the subtree of finite diameter Fix(g).
– 96 –
It follows that there is a vertex ˜v∗in the subtree that is fixed by the action of C(g).
Thus,
C(g) ⊆Stab(˜v∗).
(B.29)
If T is the Bass-Serre tree of G1 ∗H G2 or G1∗H, then ˜v∗= gGi for some g ∈G
and i ∈{1, 2}. It follows that C(g) ⊆Stab(v∗) = gGig−1; namely, C(g) is conjugate
to a subgroup of one of the vertex groups. This proves the theorems stated at the
beginning of the section.
Finite trees.
For completeness, we include two proofs of the fact that any tree T
with a finite diameter and a group G acting on T has a vertex ˜v∗∈T that is fixed
by the group action. We suppress the tilde notation in this part of the section and
simply write v∗instead of ˜v∗.
The first proof follows from the observation that a nontrivial tree with finite
diameter must contain vertices of different degrees. The degree of a vertex is the
number of edges attached to it. In particular, the vertices at the end of the tree
must be of degree one. The only trees where all vertices have the same degree are
the single vertex with no edges, and two vertices joined by one edge.
The action of any element g ∈G must preserve the degree of the vertex, so G
permutes between vertices of the same degree. Let T ′ be the subtree obtained by
removing the vertices of degree one. It follows that G preserves T ′, and diam(T ′) <
diam(T). Since the diameter decreases at each step, this process can occur only
finitely many times. The final tree is one of the trivial cases: either a single vertex or
a single edge with two vertices. In either case, since G preserves edge orientations,
G either fixes the single vertex or the two vertices joined by an edge.
The second proof we present identifies the fixed vertex with the the central vertex
of the graph. To explain the construction, let
e(v) = sup
w∈T
d(v, w)
(B.30)
be the eccentricity of a vertex. By definition, e(v) ⩽diam(T) < ∞. We also let
ρ = minv∈T e(v) the minimal eccentricity. We define the center of the graph as the
set of vertices with minimal eccentricity,
C(T) = {v ∈T | e(v) = ρ} .
(B.31)
Since the group action preserves distances, it has to preserve the set C(T). We claim
that C(T) consists of either one of two vertices connected with a single edge. In both
cases (since edge inversions are not allowed), G fixes C(T) elementwise and thus we
may choose v∗∈C(T).
To see why C(T) consists of at most two vertices, let γ be a path of maximal
length diam(T) through T realizing maxv, w∈T d(v, w) (without backtracking). Denote
the two endpoints by γ−and γ+. Let v ∈T be any vertex. We can find a unique
– 97 –
closest vertex on γ which we denote by π(v). This is also called the projection of v
on γ. The geodesic path from v to γ± then has to pass through π(v). Thus
e(v) ⩾max(d(v, γ+), d(v, γ−))
(B.32)
= d(v, π(v)) + max(d(π(v), γ+), d(π(v), γ−))
(B.33)
⩾d(v, π(v)) + ⌈1
2 diam(T)⌉.
(B.34)
In the last step, we used that d(π(v), γ+)+d(π(v), γ−) = diam(T). Thus we see that
ρ = ⌈1
2 diam(T)⌉. It is precisely attained by the central or the two central vertices of
the path γ. For a vertex outside of γ, d(v, π(v)) > 0 and thus they are not part of
C(T). The claim follows.
