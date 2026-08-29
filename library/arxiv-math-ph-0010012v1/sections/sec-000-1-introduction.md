---
doc_id: arxiv-math-ph-0010012v1
doc_title: "From random polynomials to symplectic geometry Steve Zelditch"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-2
source_pdf: 0010012v1.pdf
source_sha256: cd6eca5ccb81ff90
doc_brief: "From random polynomials to symplectic geometry Steve Zelditch — We review some recent results on random polynomials and their generalizations in complex and symplectic geometry."
---
This is a short survey of some results of P. Bleher, J. Neuheisel, B. Shiﬀman and the author on random
polynomials and their generalizations to holomorphic (and almost-holomorphic) sections of ample line bun-
dles, mainly following [BSZ1, BSZ2, BSZ3, N, ShZe, ShZe2, ShZe3, ShZe4, Ze1, Ze2]. Motivation
to study random polynomials and their generalizations in geometry comes from several sources:
• Classical Analysis: Value distribution theory of polynomials and analytic functions is a classical
topic. Computable examples may exhibit non-generic patterns of zeros (or other values) and one
would like to understand the typical distribution.
One forms ensembles of analytic functions by
deﬁning the coeﬃcients to be independent random variables with a given distribution. One can then
study expected behaviour, almost sure behaviour and so on (see e.g. [Kac, LO, O]).
• PDE: Spherical harmonics of degree N are examples of eigenfunctions of the Laplacian on a compact
Riemannian manifold. They are restrictions to the sphere Sm of homogeneous harmonic polynomials
of degree N on Rm+1. One would like to know about nodal lines, critical points, sup norms (etc.) of
general Laplace eigenfunctions. Studying features of random spherical harmonics gives insight into
the ‘typical’ properties of eigenfunctions and avoids pathologies such as occur in [L, JN]. Analogues
of spherical harmonics of degree N on general compact Riemannian manifolds are linear combinations
of eigenfunctions ∆ϕλ = λ2ϕλ with λ ∈[N log N, (N +1) log(N +1)]. References on random spherical
harmonics include [Be, N, V, Ze1]); for random combinations of eigenfunctions, see [Ze2].
• Quantum Chaos: Eigenfunctions of quantum chaotic Hamiltonians are well modeled by random
polynomials in regard to distribution of zeros or critical points, to sizes (sup-norms or Lp-norms),
to quantum expectation values, and in other respects (see, among others, [ABST, BBL, HKZ,
NoVo, Ze1, Ze2]). This is analogous to the similarity between eigenvalues of random matrices and
eigenvalues of quantum chaotic systems.
• Algebraic Geometry: Holomorphic sections s ∈H0(M, LN) of the Nth power of an ample line bundle
L →M over a K¨ahler manifold (M, ω) are quite analogous to homogeneous polynomials of degree N,
and coincide with such polynomials when M = CPm, L = O(1) ( CPm = complex projective m-space,
O(1) is the hyperplane bundle (cf. [GH])). The simultaneous zero set Zs1,...,sk of k holomorphic
sections deﬁnes a codimension k algeraic submanifold of M; one would like to know the ‘almost sure’
properties of such a submanifold.
• Symplectic Geometry: Almost-holomorphic sections s ∈H0
J(M, LN) of ample line bundles L →M
over almost-complex symplectic submanifolds (M, J, ω) in the sense of [Don, BoGu] are very similar
to holomorphic sections in the complex case. Under (diﬃcult) transversality conditions, they have
applications in symplectic geometry analogous to those in algebraic geometry.
Research partially supported by NSF grant #DMS-9703775 .
1
2
STEVE ZELDITCH
In this article, we will refer to the setting of holomorphic (or almost-holomorphic) sections as the ‘complex
case’, and the setting of eigenfunctions of Laplacians as the ‘real case’. The complex wave functions live
on phase space while the real eigenfunctions live on conﬁguration space. The main theme of our work has
been the universality of statistics of zeros and critical points of polynomials of large degree N on small
length scales (of order
D
√
N in the complex case, resp.
D
N in the real case). We have only considered compact
manifolds, and only Gaussian or spherical measures on their spaces of polynomials. Two universality classes
have emerged: (i) the ‘Heisenberg class’ in the complex case (connected to the Heisenberg group), and (ii)
the ‘Euclidean class’ in real case (connected to the Euclidean motion group). It should be mentioned that
the ‘real case’ has many other meanings in the literature on random polynomials (e.g. real polynomials and
their real zeros).
