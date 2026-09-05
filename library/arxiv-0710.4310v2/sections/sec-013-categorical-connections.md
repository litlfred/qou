---
doc_id: arxiv-0710.4310v2
doc_title: "On Two-Dimensional Holonomy João Faria Martins Centro de Matemática da Universidade do Porto"
section_id: sec-013-categorical-connections
section_title: "Categorical connections"
section_number: null
pages: 17-18
source_pdf: 0710.4310v2.pdf
source_sha256: 9a7757f998b7f680
doc_brief: "On Two-Dimensional Holonomy João Faria Martins Centro de Matemática da Universidade do Porto — We deﬁne the thin fundamental categorical group P2(M, ∗) of a based smooth manifold ( M, ∗) as the"
---
Deﬁnition 26 LetG be a Lie group. Let M be a smooth manifold. Let P →M
be a smooth principal bundle with structure group G. Denote the right action of
G onP asg ∈G ↦→Rg ∈ diﬀ(M ). Let also G = (∂ : E →G,⊲ ) be a Lie crossed
module, where⊲ is a Lie group left action of G onE by automorphisms. Let also
G = (∂ : e → g,⊲ ) be the associated diﬀerential crossed module. A G-categorical
connection on P is a pair (ω,m ), where ω is a connection 1-form on P , i.e.
ω ∈ A1(P, g) is a 1-form on P with values in g such that:
1. R∗
g(ω) = g−1ωg, ∀g ∈G,
2. ω(A#) = A, ∀A ∈ g;
and m ∈ A2(P, e) is a 2-form on P with values in e, the Lie algebra of E, such
that:
1. The 2-form m isG-equivariant. In other words we have R∗
g(m) = g−1⊲m
for each g ∈G.
2. The 2-form m is horizontal, in other words:
m(X,Y ) = m(XH,Y H ), for each X,Y ∈ X(P ).
In particular m(Xu,Yu) = 0 if either of the vectors Xu,Yu ∈ TuP is
vertical, where u ∈ P . Here the map X ∈ X(P ) ↦→XH ∈ X(P ) denotes
the horizontal projection of vector ﬁelds on P with respect to the connection
1-form ω.
17
Finally we require that
∂(m) = Ω (9)
where Ω ∈ A2(P, g) is the curvature 2-form of ω.
This last condition is of course equivalent to the vanishing of the fake curvature
of [BS, BrMe]; see 2.2.4.
Example 27 Let P be any principal G-bundle with a connection 1-form ω.
Let Ω be the curvature 2-form of ω. If G = (id : G → G,⊲ ), where ⊲ is the
adjoint action of G onG, then (ω, Ω) is a G-categorical connection on P . More
generally we can take G to be given by the universal covering map E →G of G;
see example 9.
