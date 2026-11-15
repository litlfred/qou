---
doc_id: arxiv-1604.02688v1
doc_title: "THE 3D-INDEX AND NORMAL SURFACES"
section_id: sec-031-appendix-a-generalised-angle-structures-and-the
section_title: "Appendix A. Generalised angle structures and the Euler characteristic"
section_number: null
pages: 50-51
source_pdf: 1604.02688v1.pdf
source_sha256: bdcafe379519287c
toc_source: outline
doc_brief: "THE 3D-INDEX AND NORMAL SURFACES — Dimofte, Gaiotto and Gukov introduced a powerful invariant, the 3D-index, associated to a suitable ideal triangulation of a 3-manifold with torus boundary"
---
The relationship between angle structures and geometric structures is often described by
saying that a generalised angle structure is a solution to the “linear part” of Thurston’s gluing
equations (see [Thu77, §4]). However, often this simpliﬁcation involves only considering the
edge equations, as in [LT08]. For the discussion below, we will pay special attention to the
completeness conditions coming from the holonomies of the peripheral curves.
THE 3D-INDEX AND NORMAL SURFACES
51
Let T be an ideal triangulation with n tetrahedra of a compact, orientable manifold 3-
manifold M with boundary consisting of r tori, and let □denote the set of all quad types
in T.
Recall, from Section 3.2, that a generalised angle structure on T is a function α : □→R
satisfying the equations (13) and (14), which represent the imaginary part of Thurston’s
logarithmic tetrahedral and edge equations (11), (10).
As described in [Thu77, §4.3.2], the logarithm of the derivative of the holonomy H′(γ) for
each peripheral curve γ must also vanish for a complete hyperbolic structure. Writing down
these conditions for a pair of simple closed peripheral curves generating the fundamental
group of each boundary component gives the logarithmic cusp equations (12).
The analogous condition for angle structures is deﬁned as follows.
Deﬁnition A.1. Given a generalised angle structure α on an ideal triangulation T, the
rotational holonomy of a peripheral curve γ is the imaginary part of the logarithm of the
derivative of its holonomy: ρα(γ) = Im log H′(γ).
If a generalised angle structure satisﬁes ρα(γ) = 0 for each peripheral curve γ, we say it
has vanishing peripheral rotational holonomy.
More concretely, this means the vector x = [α(qj) α(q′
j) α(q′′
j )] ∈R3n satisﬁes the linear
equations given by the imaginary parts of Thurston’s logarithmic edge, tetrahedral and
completeness equations (10), (11), (12).
In the next section, we will discuss how to assign Euler characteristics to quad disks in
the presence of a generalised angle structure.
Proposition A.2. Let T be an ideal triangulation of a compact manifold M with boundary
consisting of tori. Then there exist generalised angle structures on T with vanishing peripheral
rotational holonomy.
Proof. We closely follow the argument for Lemma 10 in [LT08].
Assume that T has n
tetrahedra and ∂M consists of r tori. A vector x ∈R3n deﬁnes a generalised angle structure
with vanishing peripheral rotational holonomy if and only if
Ax = b,
where A is the (2n + 2r) × 3n matrix with rows Ei, Tj, Mk, Lk and b ∈R2n+2r is the vector
with n entries 2π, followed by n entries π, then 2r zero entries.
From linear algebra, the equation Ax = b has a solution if and only if b ∈Im(A) =
Ker(AT)⊥if and only if
z ∈R2n+2r and ATz = 0 ⇒zTb = 0.
Now z =
xi
yj
pk
qk
T ∈Ker(AT) if and only if S = P
i xiEi + P
j yjTj + P
k pkMk +
P
k qkLk = 0, i.e. S gives the trivial normal class in Q(T; R). But this implies that ∂S = 0 so
pk = qk = 0 for all k, hence S = P
i xiEi+P
j yjTj = 0. Further −χ(S) = P
i 2xi+P
j yj = 0,
hence zTb = 0. This proves the result.
□
