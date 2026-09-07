---
doc_id: arxiv-0806.2317v1
doc_title: "Bounds for codes and designs in complex subspaces Aidan Roy ∗"
section_id: sec-002-representations
section_title: "Representations"
section_number: null
pages: 5-7
source_pdf: 0806.2317v1.pdf
source_sha256: c54e80d460413a5e
doc_brief: "Bounds for codes and designs in complex subspaces Aidan Roy ∗ — We introduce the concepts of complex Grassmannian codes and designs."
---
In this section and the next, we develop the representation t heory needed for
Grassmannian LP bounds.
As is standard for compact Lie groups, we work with functions on Gm,n to
ﬁnd irreducible representations. Deﬁne an inner product fo r functions on Gm,n
5
as follows:
⟨f, g ⟩ :=
∫
Gm,n
f (a)g(a) da.
Here da is the unique measure invariant on Gm,n , normalized so that
∫
da = 1.
That such a measure exists an is unique (the Haar measure) fol lows from the
fact that Gm,n is a compact Lie group. Equivalently, we may write
⟨f, g ⟩ :=
∫
U (n)
f (U ∗PaU )g(U ∗PaU ) dU,
where dU is the Haar measure on U (n), and Pa is the projection matrix for
some ﬁxed a ∈ G m,n . Now let L2(Gm,n ) denote the space of square-integrable
functions on Gm,n . Then U (n) acts on f ∈ G m,n as follows:
(U f)(Pa) := f (U ∗PaU ).
It follows that L2(Gm,n ) provides a representation of U (n). As we will see, this
representation can be decomposed into irreducible subrepr esentations explicity,
and the decomposition is multiplicity-free: no irreducible representation of U (n)
occurs more than once in L2(Gm,n ).
Since U (n) is a compact Lie group, its irreducible representations ar e well-
studied: see for example [22, 15, 6, 12]. Every irreducible r epresentation is
indexed by a dominant weight [22, Theorem 7.34]. In the case of U (n), we may
take these weights to have the form [6, Theorem 38.3]
λ = (λ 1, . . . , λ n) : λ 1 ≥ λ 2 ≥ . . . ≥ λ n, λ i ∈ Z.
The dimension of the irreducible representation Vλ indexed by λ is given by
Weyl’s character formula [22, Theorem 7.32]. In the case of U (n), the formula
reduces to:
dim Vλ =
∏
1≤i<j≤n
λ i − λ j + j − i
j − i . (3.1)
For example, the standard representation of U (n) is indexed by λ = (1, 0, . . . , 0),
which gives
dim V(1, 0,..., 0) = n.
Note that there is more than one irreducible representation with the same
dimension.
Each dominant weight may also be thought of as a form acting on a maximal
Abelian subgroup of the Lie group. Here λ acts on the diagonal matrix d =
6
diag(d1, . . . , d n) ∈ U (n) as follows:
dλ :=
n∏
i=1
dλ i
i .
The next section describes exactly which of these forms cont ribute to the de-
composition of L2(Gm,n ).
