---
doc_id: arxiv-math-0203060v11
doc_title: "ON FUSION CATEGORIES"
section_id: sec-035-7-the-yetter-cohomology-of-a-tensor-category-and
section_title: "The Yetter cohomology of a tensor category and Ocneanu rigidity"
section_number: 7
pages: 27-28
source_pdf: 0203060v11.pdf
source_sha256: fa7e21ceab3e9933
toc_source: outline
doc_brief: "ON FUSION CATEGORIES — Using a variety of methods developed in the literature (in partic- ular, the theory of weak Hopf algebras), we prove a number of general results about fusion categories in"
---
rigidity
7.1. The deﬁnition. The following cohomology of a tensor category with respect
to a tensor functor was deﬁned in [Y1, Y2], motivated by the previous work [CY],
and independently in [Da].
Let C, C′ be tensor categories over a ﬁeld k, and F : C →C′ be a (unital) tensor
functor.
For a nonnegative integer n, let Cn denote the n-th Cartesian power of C. In
particular, C0 has one object (empty tuple ∅) and one morphism (identity). Deﬁne
the functor Tn : Cn →C by Tn(X1, ..., Xn) := X1 ⊗... ⊗Xn. In particular, T0 :
C0 →C is deﬁned by T0(∅) = 1, and T1 = Id. Let Cn
F (C) = End(Tn ◦F ⊗n) (so e.g.,
C0
F (C) = End(1C′)). We deﬁne a diﬀerential d : Cn(C) →Cn+1(C) by the formula
df = Id⊗f2,...,n+1−f12,...,n+1+f1,23,...,n+1−...+(−1)nf1,...,nn+1+(−1)n+1f1,...,n⊗Id,
where for instance f12,3,...,n+1 is the endomorphism of the product of n objects
F(X1)⊗F(X2), F(X3), ..., F(Xn+1), and we use the identiﬁcation F(X1)⊗F(X2) →
F(X1 ⊗X2) deﬁned by the tensor structure on F.
It is easy to show that d2 = 0. Thus (C•(C), d) is a complex. We will call the
cohomology groups Hn
F (C), n ≥0 of this complex the Yetter cohomology groups of
C with respect to F. In the important special case C = C′, F = Id, we will denote
this cohomology simply by Hi(C) and call it the Yetter cohomology of C.
As usual, low dimensional Yetter cohomology groups have an independent mean-
ing [Y1, Y2, Da]. The group H1
F (C) classiﬁes derivations of F as a tensor functor.
The group H2
F (C) classiﬁes ﬁrst order deformations of the tensor structure on the
functor F. The group H3(C) classiﬁes ﬁrst order defomations of the associativity
constraint in C, i.e. of the structure of C itself. As usual, obstructions to these
deformations live in the cohomology groups one degree higher.
To illustrate this deﬁnition, we give a few examples.
Example 7.1. If C is Rep(H) for a Hopf algebra H and F the forgetful functor,
then Hi
F (C) is the usual Hochschild cohomology of H as a coalgebra.
28
PAVEL ETINGOF, DMITRI NIKSHYCH, AND VIKTOR OSTRIK
Example 7.2. Let G be a ﬁnite group, and C = VecG be the category of G-graded
vector spaces over an algebraically closed ﬁeld k (of any characteristic).
Then
Hi(C) = Hi(O(G)), the Hochschild cohomology of O(G) as a coalgebra, where O(G)
is the Hopf algebra of k-valued functions on G. In other words, Hi(C) = Hi(G, k),
the group cohomology of G with coeﬃcients in k.
Example 7.3. Let G be a reductive algebraic group over k with Lie algebra
g.
Let Rep(G) denote the category of algebraic representations of G.
Then
Hi(Rep(G)) = (Λig)G for all i.
Indeed, Rep(G) = Rep(O(G)∗).
Therefore,
Cn(Rep(G)) = (O(Gn)∗)G, where G acts diagonally by conjugation. Since G is
reductive, the cohomology of this complex is the G-invariants in the Hochschild
cohomology of O(G) with coeﬃcients in the trivial representation (corresponding
to 1 ∈G). This cohomology is well known to be Λg, so the answer is (Λg)G, as
desired. Thus, if g is a simple Lie algebra, then there is no nontrivial derivations or
tensor structure deformations of the identity functor, but there exists a unique (up
to scaling) ﬁrst order deformation of the associativity constraint, corresponding to
a basis element in (Λ3g)G. It is easy to guess that this deformation comes from an
actual deformation, namely from the deformation of O(G) to the quantum group
Oq(G).
