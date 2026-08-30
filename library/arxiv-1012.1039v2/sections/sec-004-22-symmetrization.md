---
doc_id: arxiv-1012.1039v2
doc_title: "where vn is the volume of a regular ideal hyperbolic n–simplex. This result gener- alizes the fact that hyperbolic Dehn ﬁlling of a 3–manifold d oes not increase hyperbolic volume"
section_id: sec-004-22-symmetrization
section_title: "Symmetrization"
section_number: 2.2
pages: 6-8
source_pdf: 1012.1039v2.pdf
source_sha256: acb2575050db419d
doc_brief: "SIMPLICIAL VOLUME AND FILLINGS OF HYPERBOLIC MANIFOLDS — Let M be a hyperbolic n–manifold whose cusps have torus cross- sections."
---
sume that all chains considered are symmetric. Here we say what this means and
justify the assumption.
Consider the abstract n–simplex ∆ n. The symmetric group Sn+1 acts in an
obvious way on the vertices, and any permutation p ∈ Sn+1 extends to ∆ n as an
aﬃne transformation.
Let X be some space. Any singular simplex σ : ∆ n → X can be altered by
precomposition with some p ∈ Sn+1 and the singular simplices σ and σ ◦p are
SIMPLICIAL VOLUME AND FILLINGS OF HYPERBOLIC MANIFOLDS 7
generally diﬀerent, though if p is an odd permutation and q is an even one (so
sgn(p) = −1 and sgn(q) = 1), we’d really like to think of σ ◦p as being the same as
σ ◦q orσ, just with opposite orientation. We would also like to avoid the annoyin g
bookkeeping which is standard when dealing with simplices. We therefo re deﬁne
the symmetrization map
S : C∗(X; R) →C∗(X; R)
on singular n-simplices σ by
(5) S(σ) = 1
(n + 1)!
∑
p∈Sn+1
sgn(p) (σ ◦p),
and extend linearly over C∗(X; R).
Lemma 2.6. S is a chain map, chain homotopic to the identity. Moreover ‖S(c)‖1 ≤
‖c‖1 for any chain c.
Proof. It is evident that norm does not increase. The chain homotopy is des cribed
in Appendix B. □
Deﬁne CS
∗ (X;R) to be the subcomplex of C∗(X;R) consisting of chains in the
image of S; the transformation S restricts to the identity on this subcomplex.
Lemma 2.6 implies that in computing Gromov norms, we may as well restr ict
attention to CS
∗ (X;R).
Suppose X has the structure of a simplicial complex (or more generally just a
CW complex so that each cell is a simplex, and so that each restriction of a gluing
map to a face is aﬃne) with triangulation T .
Deﬁnition 2.7. We call a singular simplex σ : ∆ n →X aﬃne if σ =τ ◦a where
a : ∆ n → ∆ k is some aﬃne surjection taking vertices to vertices, and τ is the
characteristic map of some k–simplex of T . A linear combination of aﬃne simplices
is an aﬃne chain , and so on.
Remark 2.8. There is a nice inclusion
CT
∗ (X; R)
i
− →CS
∗ (X; R)
of simplicial chains CT
∗ (X; R) given by sending a simplex of X to the symmetrization
of its characteristic map. This gives a way to think of simplicial chains a s symmetric
aﬃne singular chains.
In fact, the image of the map i from Remark 2.8 contains all of the symmetric
aﬃne simplices; the symmetrization of an aﬃne simplex which drops dime nsion
must vanish:
Lemma 2.9. LetX have a triangulation T , and suppose that σ is an aﬃne singular
n–simplex with image in the (n − 1)–skeleton of X. Then S(σ) = 0 .
Proof. Since σ has image in the ( n − 1)–skeleton, there must be a pair of vertices
{vi,v j} of the standard simplex ∆ n which are identiﬁed by σ. Let p be a permuta-
tion of the vertices of ∆ n, and let τ be the transposition switching vi and vj. The
maps σ ◦p and σ ◦τ ◦p are the same as singular simplices, but the permutations
p and τ ◦p have opposite signs, so the terms sgn( p)(σ ◦p) and sgn( τ ◦ p)(σ ◦τp )
cancel in the sum (5). □
8 K. FUJIW ARA AND J. F. MANNING
