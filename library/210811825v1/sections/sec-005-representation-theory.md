---
doc_id: 210811825v1
doc_title: "Properties of Eigenvalues on Riemann Surfaces with Large Symmetry Groups"
section_id: sec-005-representation-theory
section_title: "Representation theory"
section_number: null
pages: 52-53
source_pdf: 2108.11825v1.pdf
source_sha256: 1c2a4b317d6239c5
toc_source: outline
doc_brief: "Properties of Eigenvalues on Riemann Surfaces with Large Symmetry Groups — 26 sections: Front matter; Introduction; Background"
---
Representation theory
Deﬁnition 2.36 (Representation) Let V be an n-dimensional vector space over C.
Then GL(V ) denotes the the group of isomorphisms V →V . If V has a ﬁnite basis of
vectors {e1, . . . , en}, then each linear map a : V →V is deﬁned by an n × n matrix (aij)
such that
a(ej) =
n
X
i=j
aijei.
A representation of a ﬁnite group G is a group homomorphism
ρ : G →GL(V ).
For each g, h ∈G, we have a map ρ(g) : V →V such that
(i) ρ(gh) = ρ(g)ρ(h),
(ii) ρ(1) = 1,
(iii) ρ(g−1) = ρ(g)−1.
Denote by dim(V ) the dimension of the representation. A sub-representation of ρ is
a sub-vector space W ⊆V such that ρ(g)w ∈W for all w ∈W and g ∈G. A subspace
with this property is called G-invariant (or just invariant).
Deﬁnition 2.37 (Irreducible representation) Let ρ : G →GL(V ) be a representa-
tion. We say that ρ is irreducible if V̸ = 0 and if no subspace of V is G-invariant, except
{0} and V , that is, only “trivial” subspaces are G-invariant.
Deﬁnition 2.38 (Unitary representation) Where V is a complex Hilbert space, a
representation ρ of G is unitary if ρ(g) = Ug is a unitary operator for every g ∈G,
that is, Ug is surjective and preserves the inner product on V . We have
U ∗
g Ug = UgU ∗
g = I,
that is, Ug is the inverse of its adjoint.
Deﬁnition 2.39 (Character) The character of a representation ρ of a group G, as
above, is a function χρ : G →F, where F is the ﬁeld over which the vector space V is
deﬁned. For g ∈G, it is given by
χρ(g) = Tr(ρ(g)).
Remark 2.40 We will not always include a subscript when talking about characters; it
will depend on the context. Characters take a constant value on each conjugacy class.
They will be used in the next section, where we introduce a general version of Selberg’s
trace formula that uses a character to restrict to a particular irreducible representation.
42
In Chapter 3 and Chapter 4, we look at the irreducible representations of the isometry
groups of speciﬁc surfaces. We use these to investigate the orthonormal basis of eigen-
functions of L2(Γ \ H); our ﬁrst step towards achieving this is the Peter-Weyl theorem.
Theorem 2.41 (Peter-Weyl Theorem, taken from [49]) Let H be the Hilbert space
of square integrable functions over G, that is L2(G). Let ρ be a unitary representation of
G that acts on H as
ρ(h)f(g) = f(h−1g).
Then L2(G) decomposes as an orthogonal direct sum of unitary irreducible representations
of G, where the multiplicity of a representation is equal to its degree. We have
L2(G) =
M
ρ
E ⊕dim(Eρ)
ρ
,
where the sum runs over the total spaces Eρ of the representations ρ.
Next, we have the following property of the Laplacian:
Lemma 2.42 The Laplace operator commutes with the group of isometries of the surface
(see, for example, [14]).
For a isometry φ : S →S of a compact Riemann surface S, and an eigenfunction of
the Laplacian f : S →R with eigenvalue λ, this means
∆(f ◦φ) = (∆f) ◦φ = (λf) ◦φ = λ(f ◦φ).
Consider the eigenspaces of the Laplacian
Ei = Ei(S) = {φi ∈L2(S) | ∆φi = λiφi}.
We can use the Peter-Weyl theorem along with the invariance of the Laplacian under
isometries to decompose the eigenspace Ei as a direct sum of eigenspaces of irreducible
representations (these can appear more than once). Huber showed that for every irre-
ducible representation, there are inﬁnitely many eigenspaces in which this representation
is involved [35].
2.5
