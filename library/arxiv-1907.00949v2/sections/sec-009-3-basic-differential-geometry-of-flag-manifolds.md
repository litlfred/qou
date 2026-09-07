---
doc_id: arxiv-1907.00949v2
doc_title: "OPTIMIZATION ON FLAG MANIFOLDS"
section_id: sec-009-3-basic-differential-geometry-of-flag-manifolds
section_title: "Basic differential geometry of flag manifolds"
section_number: 3
pages: 7-9
source_pdf: 1907.00949v2.pdf
source_sha256: 865defaa34bf42be
doc_brief: "OPTIMIZATION ON FLAG MANIFOLDS — A ﬂag is a sequence of nested subspaces."
---
We will now deﬁne ﬂags and ﬂag manifolds formally and discuss some basic properties. Let n be
a positive integer and V be an n-dimensional vector space over R. We write V(k, V) for the Stiefel
manifold [35] of k-frames in V and Gr(k, V) for the Grassmannian [19] of k-dimensional subspaces
in V. If the choice of V is unimportant or if V = Rn, then we will just write V( k,n ) and Gr(k,n ).
8 K. YE, K. S.-W. WONG, AND L.-H. LIM
Deﬁnition 3.1. Let 0<n 1<··· <n d<n be an increasing sequence of d positive integers and V
be ann-dimensional vector space over R. A ﬂag of type (n1,...,n d) in V is a sequence of subspaces
V1 ⊊ V 2 ⊊··· ⊊ Vd, dim Vi =ni, i = 1,...,d.
We denote the set of such ﬂags by Flag(n1,...,n d; V) and call it theﬂag manifold of type (n1,...,n d).
If V is unimportant or if V = Rn, then we will just write Flag( n1,...,n d;n).
For notational convenience we will adopt the following convention throughout:
n0 := 0, n d+1 :=n, V0 :={0}, Vd+1 := V.
We will see in Proposition 3.2 that ﬂag manifolds are indeed manifolds. When d = 1, Flag(k; V)
is the set of all k-dimensional subspaces of V, which is the Grassmannian Gr( k, V). The other
extreme case is when d =n− 1 and ni =i,i = 1,...,n − 1, and in which case Flag(1,...,n − 1; V)
comprises all complete ﬂags of V, i.e.,
V1 ⊊ V 2 ⊊··· ⊊ Vn−1, dim Vi =i, i = 1,...,n − 1.
Like the Grassmannian, the ﬂag manifold is not merely a set but has rich geometric structures.
We will start with the most basic ones and defer other useful characterizations to Sections 4 and 5.
Proposition 3.2. Let 0 < n1 <··· < nd < nbe integers and V be an n-dimensional real vector
space. The ﬂag manifold Flag(n1,...,n d; V) is
(i) a connected compact smooth manifold;
(ii) an irreducible aﬃne variety;
(iii) a closed submanifold of Gr(n1, V)× Gr(n2, V)×···× Gr(nd, V);
(iv) a closed submanifold of Gr(n1, V)× Gr(n2−n1, V)×···× Gr(nd−nd−1, V);
(v) a ﬁber bundle on Gr(nd, V) whose ﬁber over W∈ Gr(nd, V) is Flag(n1,...,n d−1; W);
(vi) a smooth projective variety.
Proof. Property (i) is well-known [27, 11] but also follows from the characterization in Propo-
sition 4.1 as a quotient of a compact connected Lie group by a closed subgroup. Property (ii)
is a consequence of Propositions 5.1 and 5.5, where we give two diﬀerent ways of representing
Flag(n1,...,n d; V) as an aﬃne variety in Rm,m = (nd)2. Property (vi) is a consequence of (iii) or
(iv), given that the Grassmannian is a projective variety.
In the following, let {Vi}d
i=1∈ Flag(n1,...,n d; V), i.e., dim Vi = ni, i = 1,...,d . For (iii), the
map
ε : Flag(n1,...,n d; V)→ Gr(n1, V)×···× Gr(nd, V), {Vi}d
i=1↦→ (V1, V2,..., Vd) (6)
is clearly an embedding. Its image is closed since if (V1,..., Vd)⁄∈ε
(
Flag(n1,...,n d; V)
)
, then there
exists some i∈{ 1,...,d − 1} such that Vi⁄⊆ Vi+1; so if V′
i∈ Gr(ni, V) and V′
i+1∈ Gr(ni+1, V) are
in some small neighborhood of Vi and Vi+1 respectively, then V′
i⁄⊆ V′
i+1.
For (iv), choose and ﬁx an inner product on V. Let V⊥
i denote the orthogonal complement of Vi
in Vi+1, i = 1,...,d − 1. The map
ε′ : Flag(n1,...,n d; V)→ Gr(n1, V)× Gr(n2−n1, V)×···× Gr(nd−nd−1, V),
{Vi}d
i=1↦→ (V1, V⊥
1,..., V⊥
d−1)
(7)
is clearly an embedding. That the image of ε′ is closed follows from the same argument used for ε.
For (v), consider the map
ρ : Flag(n1,...,n d; V)→ Gr(nd, V), {Vi}d
i=1↦→ Vd,
that is clearly surjective and smooth. For any W∈ Gr(nd, V), ρ−1(W) consists of ﬂags of the form
V′
1⊆ V′
2⊆···⊆ V′
d−1⊆ W, dim V′
i =ni, i = 1,...,d − 1.
In other words, the ﬁber ρ−1(W)∼= Flag(n1,...,n d−1; W). □
OPTIMIZATION ON FLAG MANIFOLDS 9
The ﬁber bundle structure in Proposition 3.2(v) may be recursively applied to get
Flag(n1,...,n d−1;nd)→ Flag(n1,...,n d;n)→ Gr(nd,n ),
Flag(n1,...,n d−2;nd−1)→ Flag(n1,...,n d−1;nd)→ Gr(nd−1,n ),
and so on, ending in the well-known characterization of the Stiefel manifold as a principal bundle
over the Grassmannian
O(n)→ V(k,n )→ Gr(k,n ).
In the next two sections, we will see how the ﬂag manifold may be equipped with extrinsic matrix
coordinates and be represented as either homogeneous spaces of matrices (Section 4) or manifolds
of matrices (Section 5) that in turn give closed-form analytic expressions for various diﬀerential
geometric objects and operations needed for optimization algorithms.
