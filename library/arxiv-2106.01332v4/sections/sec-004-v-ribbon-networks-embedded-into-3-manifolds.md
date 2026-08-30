---
doc_id: arxiv-2106.01332v4
doc_title: "Braided matter interactions in quantum gravity via 1-handle attachment"
section_id: sec-004-v-ribbon-networks-embedded-into-3-manifolds
section_title: "RIBBON NETWORKS EMBEDDED INTO 3-MANIFOLDS"
section_number: V
pages: 6-7
source_pdf: 2106.01332v4.pdf
source_sha256: 44c19a99624997bf
doc_brief: "Braided matter interactions in quantum gravity via 1-handle attachment — 9 sections: INTRODUCTION; (for C𝓁(6)) and B3 (for C𝓁(4)). In; THEORIES ON RIBBON GRAPHS"
---
We suppose that particle systems constitute ribbon graphs in which vertices are thickened to be (homeomorphic
to) two dimensional disks (or rectangles), and edges are thickened to ribbons. These objects are embedded in a
3-dimensional ground space, which is taken to be a 3-manifold, and they are also referred to as fat graphs in the
literature. See for instance [13, 14].
Ribbon graphs are formally deﬁned as oriented surfaces decomposed into two families of rectangular surfaces, i.e.
embeddings of the square [0 , 1]× [0, 1] in the base 3-dimensional manifold, called “ coupons” and “ ribbons”, and a
family of “ annuli”, i.e. embeddings of the cylinder S1× [0, 1]. We will think of coupons as vertices of a graph,
thickened into rectangles or, equivalently a 2-dimensional closed ball, while ribbons will constitute the connecting
edges of a graph, thickened to rectangles. Annuli determine the components of framed links, and will therefore be
given with a trivialization of the normal bundle, which is described by an integer corresponding to the twisting.
Moreover, it is assumed that coupons, ribbons and annuli do not self-intersect, but coupons and ribbons are allowed
to meet at one side of the boundary of the rectangular surface. Figure 4 shows a portion of ribbon graph where a
central coupon, rectangular and corresponding to a “fat vertex” of the graph, is connected to ribbon edges on top
and bottom. This is the fundamental unit of a ribbon network considered below, as we can concatenate them by
joining their ribbons.
Two ribbon graphs are said to be equivalent if there exists an isotopy that transforms one into the other. Equivalence
of ribbon graphs is conveniently expressed in combinatorial terms by considering diagrams of ribbon graphs, i.e.
projections on the plane. In terms of their diagrams, two ribbon graphs are equivalent if and only if there exists a
ﬁnite sequence of plane isotopies and moves of type:
• Oriented framed Reidemeister moves;
• Ribbons can slide above and below coupons;
• Opposite crossings cancel, after orientation turning is applied;
• Coupons can be rotated with surface parallel to the plane, so that the attached ribbons spiral around the
coupons.
7
B
FIG. 6: Fragment of trivalent ribbon network embedded in a 3-manifold. The box named “ B” corresponds to a braid of
Bilson-Thompson model
This combinatorial moves correspond to the generators of the category of ribbon graphs in [15], relations rel 1 to rel13.
In analogy with spin networks in quantum gravity, we call ribbon networks the elements of an appropriate subclass
of ribbon graphs (introduced below) considered in this article. We assume that our ribbon networks are embedded
into 3-manifolds. A 3-manifold M is thought of as a temporal fragment of space-time, in the sense that it represents
the spatial coordinates at a ﬁxed time. A network embedded in M represents a physical system at time t0. Figure 6
illustrates a portion of a trivalent network embedded into a 3-manifold corresponding to an arbitrary braid B of
Bilson-Thompson’s model.
We take our “admissible” ribbon networks to be closed trivalent ribbon graphs, i.e. ribbon networks with no
open edges whose vertices have three incident edges. We allow, moreover, disconnected annuli, i.e. loops, knotted
with the rest of a ribbon network. In other words, an admissible ribbon network is a compact (not necessarily
connected) surface with boundary whose corresponding spine is a trivalent graph embedded in 3-space. A vertex
coupon is represented as in Figure 7, and will be called a trinion. We consider isotopy classes of braided networks,
and therefore do not distinguish between representatives of the same class. An isotopy class is determined combi-
natorially by a slightly modiﬁed version of the moves described above. In fact, the set of moves relating diagrams
of isotopic surfaces with boundary embedded in a 3-manifold has been determined in [16] in both the oriented and
non-oriented case. Since Bilson-Thompson’s framed braids are all oriented, it is reasonable to require that our
ribbon graphs, and hence ribbon networks, are all taken to be oriented. In the oriented case, Matsuzaki’s moves
[16] correspond to the framed Reidemeister moves, as given for example in [17], Figure 1.8, slide of trinions over
and underneath ribbons, and Ishii’s IH move in [18]. In fact, the latter move has been considered in [2] under the
name of exchange move. We remark that using Matsuzaki’s moves, in principle, the procedure of trading braiding
for twists discussed in [19] is not allowed, as the oriented moves do not include vertex twists. Roughly speaking,
we always look at one side of the ribbons, without allowing half-twists. This is consistent with the constructions
found in this article, as a consequence of restricting ourselves to oriented surfaces. 3 We will see below that it is
useful to derive a relation between self-crossing twists and composition of half-twists in order to simplify com-
putations. We will use this relation as a computational tool, although no isolated half-twist appears in our framework.
Lastly, recall that each 3-manifold arises from surgery on a framed link embedded in the 3-sphere S3, see for
instance [20]. This result, known in the literature as Lickorish-Wallace Theorem, allows us to represent a 3-manifold
M3 by a framed link L whose S3-surgery producesM3
