---
doc_id: arxiv-1907.00949v2
doc_title: "OPTIMIZATION ON FLAG MANIFOLDS"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-2
source_pdf: 1907.00949v2.pdf
source_sha256: 865defaa34bf42be
doc_brief: "OPTIMIZATION ON FLAG MANIFOLDS — A ﬂag is a sequence of nested subspaces."
---
Launched around 20 years ago in a classic article of Edelman, Arias, and Smith [16], Riemannian
manifold optimization is now entrenched as a mainstay of optimization theory [1, 2, 15, 40]. While
studies of optimization algorithms on Riemannian manifolds predate [16], the distinguishing feature
of Edelman et al.’s approach is that their algorithms are built entirely and directly from standard
algorithms in numerical linear algebra; in particular, they do not require numerical solutions of
diﬀerential equations. For instance, the parallel transport of a vector in [16] is not merely discussed
in the abstract but may be explicitly computed in eﬃcient and numerically stable ways via closed-
form analytic expressions involving QR and singular value decompositions of various matrices.
The requirement that diﬀerential geometric quantities appearing in a manifold optimization
algorithms have analytic expressions in terms of standard matrix decompositions limits the type
of Riemannian manifolds that one may consider. Aside from Euclidean spaces, we know of exactly
three Riemannian manifolds [2] on which one may deﬁne optimization algorithms in this manner:
(i) Stiefel manifold V(k,n ),
(ii) Grassmann manifold Gr(k,n ),
(iii) manifold of positive deﬁnite matrices Sn
++.
The main contribution of this article is to furnish a fourth: ﬂag manifolds.
A ﬂag in a ﬁnite-dimensional vector space V over R is a nested sequence of linear subspaces
{Vi}d
i=1 of V, i.e.,
{0} ⊊ V 1 ⊊··· ⊊ Vd ⊊ V.
For any increasing integer sequence of length d, 0 < n1 < ··· < nd < n, the set of all ﬂags
{Vi}d
i=1 with dim(Vi) =ni, i = 1,...,d , is a smooth manifold called a ﬂag manifold, and denoted
by Flag(n1,...,n d; V). This is a generalization of the Grassmannian Gr( k, V) that parameterizes
k-dimensional linear subspaces in V as ﬂags of length one are just subspaces, i.e., Flag( k; V) =
Gr(k, V). Flag manifolds, sometimes also called ﬂag varieties, were ﬁrst studied by Ehresmann [17]
2010 Mathematics Subject Classiﬁcation. 62H12, 14M15, 90C30, 62H10, 68T10.
Key words and phrases. Flag manifold, generalized ﬂag variety, linear subspaces, distances and metrics, manifold
optimization, multivariate data analysis, numerical analysis.
1
arXiv:1907.00949v2  [math.OC]  7 Aug 2019
2 K. YE, K. S.-W. WONG, AND L.-H. LIM
and saw rapid development in 1950’s [12, 9, 10, 14]. They are now ubiquitous in many areas of
pure mathematics, and, as we will discuss next, they are also ubiquitous in applied mathematics,
just hidden in plain sight.
The optimization algorithms on Grassmann and Stiefel manifolds originally proposed in [16]
have found widespread applications: e.g., computer vision [38, 39], shape analysis [33, 34], matrix
computations [37, 25], subspace tracking [6], and numerous other areas — unsurprising as subspaces
and their orthonormal bases are ubiquitous in all areas of science and engineering. For the same
reason, we expect optimization algorithms on ﬂag manifolds to be similarly useful as ﬂags are also
ubiquitous — any multilevel, multiresolution, or multiscale phenomena likely involve ﬂags, whether
implicitly or explicitly. We will discuss some examples from numerical analysis and statistics.
