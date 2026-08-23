---
doc_id: arxiv-math-0502543v2
doc_title: "CONTINUITY OF VOLUMES – ON A GENERALIZATION OF A CONJECTURE OF J.W.MILNOR"
section_id: sec-000-2-a-simple-proof-for-simplices-among-other-thing
section_title: "A simple proof for simplices (among other things)"
section_number: 2
pages: 3-5
source_pdf: 0502543v2.pdf
source_sha256: 227ef8150cb08faf
doc_brief: "CONTINUITY OF VOLUMES – ON A GENERALIZATION OF A CONJECTURE OF J.W.MILNOR — In his paper [6] J."
---
In dimension 2 , the result follows immediately from Gauss’ for-
mula, which states that area is a linear function of the angle s, so we
will only discuss dimensions 3 or above.
The simple proof relies on the Schl¨ aﬂi diﬀerential equality (see [6],
which states that in a space of constant curvature K, and dimension n
the volume of a smooth family of polyhedraP satisﬁes the di ﬀerential
equation:
(1) KdV(P) = 1
n − 1
∑
F
Vn−2(F)dθF,
where the sum is over all codimension-2 faces, Vn−2 is the n − 2
dimensional volume of F, and θF is the dihedral angle at F.
Another way of writing the Schl¨ aﬂi formula is:
(2) K ∂V(P)
∂θF
= Vn−2(F).
This is the form we will use.
The ﬁrst observation is that Vn−2(F) is bounded by a constant (di-
mensional for Sn, , depending on the number of vertices of F, but
nothing else, and if n ≥ 4, in Hn.).
This immediately shows the continuity of volume for all Sn, and
for Hn, whenever n ≥ 4.
We are left with dimension 3 . All we really need is noting that the
partial derivatives of V with respect to the dihedral angles develop
at worst logarithmic singularities as we approach the front ier of
ΩH3
– this result su ﬃces by the following form of the Sobolev Embedding
Theorem (this is [3, Theorem 7.26]):
Theorem 3. Let Ωbe a C 0,1 domain in Rn. Then,
4 IGOR RIVIN
• (i) If kp < n, the space W k,p(Ω) is continuously imbedded in L p∗
(Ω),
where p∗ = np/(n − kp), and compactly imbedded in L q(Ω) for any
q < p∗.
• (ii) If 0 ≤ m < k− n
p < m+1, the space Wk,p is continously embedded
in Cm,α(Ω), α = k − n/p − m, and compactly embedded in C m,β(Ω)
for any β < α.
Here, the Sobolev space Wk,p is the space of functions whose ﬁrst k
(distributional) derivatives are in Lp.
In our case, we know that the domainΩis bounded, convex “curvi-
linear polyhedral” (hence C0,1) domain, volume is a bounded func-
tion, and we assume that the gradient grows logarithmically as we
approach the boundary . This implies that V is in W1,p for all p > 0, so
we get the following corollary:
Corollary 2. Volume is in C 0,α(
Ω) for any α < 1.
The logarithmic growth of diameter of the simplex as a functi on
of the distance to ∂Ω can be shown in a completely elementary way
using Eq. (2) and elementary reasoning about Gram matrices, as
follows:
Let G be “angle Gram matrix” of a simplex ∆, that is, Gi j = − cos θi j,
where θi j is the angle between the i-th and the j-th face. Let S be
the matrix whose columns are the normals to the faces of ∆ (all
the computations take place in Minkowski space, and we use th e
hyperboloid model of Hn. It is immediate that G = StS.
Let now W be the matrix whose columns are the (possibly scaled)
vertices of ∆. W satisﬁes the equation StW = I, and to get the vertices
to lie on the hyperboloid ⟨x, x⟩= −1 we must rescale in such a way
that the squared norms of the columns of W become −1. Call the
scaled matrix Ws. Since the usual “length” Gram matrix G∗ of ∆S can
be written as Wt
sWs, and G∗
i j = − cosh(d(vi, v j)), a simple computation
using Cramer’s rule gives:
cosh d(vi, v j) =
ci j
√ciic j j
,
where ci j is the i j-th cofactor of G. (see [7] for many related results).
It follows that the distances between the vertices (which ar e the
lengths of the edges, which are the faces of codimension 2 .) behave
as | log cii|. Since the cofactors are polynomial in the cosines of the
angles, we are done.
CONTINUITY OF VOLUMES 5
It should be noted that this argument works mutatis mutandis for
hyperideal simplices, or simplices with some ﬁnite and some hyper-
inﬁnite vertices..
3. C onvex polytopes
