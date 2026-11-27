---
doc_id: arxiv-math-0102098v1
doc_title: "Skein theory and the Murphy operators"
section_id: sec-003-3-the-skein-of-the-annulus
section_title: "The skein of the annulus."
section_number: 3
pages: 8-10
source_pdf: 0102098v1.pdf
source_sha256: f4bc5ca0ba1e47aa
toc_source: inferred
doc_brief: "Skein theory and the Murphy operators — The Murphy operators in the Hecke algebra Hn of type A are ex- plicit commuting elements whose sum generates the centre."
---
The skein of the annulus.
The Homﬂy skein of the annulus, C, as discussed in [12] and originally in
[16], is deﬁned as linear combinations of diagrams in the annulus, modulo
the Homﬂy skein relations. The element X ∈C will be indicated on a diagram
as
X .
We shall make use of the results of section 2 to study C, and also to ﬁnd
simple skein representatives for the power sums of the Murphy operators in
Hn in a way which is independent of n.
The best known relation of C with the Hecke algebra Hn is the closure
map Rn
n →C, induced by taking a tangle T to its closure ˆT in the annulus,
deﬁned by
ˆT =
T
.
This is a linear map, whose image we will call Cn.
The skein C has a product induced by placing one annulus outside another,
under which C becomes a commutative algebra;
XY =
X
Y
.
Write Am ∈C for the closure of the m-braid
σm−1 · · · σ2σ1 =
.
An explicit spanning set of Cn consists of the monomials in {Aj} of total
weight n, where Aj has weight j. Such monomials correspond bijectively
with partitions of n.
8
A very simple skein theory construction determines a natural linear map
ϕ : C →C, induced by taking a diagram X in the annulus and linking it once
with a simple loop to get
ϕ(X) =
X
.
It is instructive to look at the eigenvectors of ϕ. Clearly ϕ carries Cn into
itself. What is more, if we take an element S ∈Hn with closure ˆS ∈Cn and
compose it with the central element T (n) then ST (n) has closure ϕ( ˆS).
Theorem 3.1 The eigenvalues of ϕ|Cn are all distinct.
Proof : Take S = Eλ to see that the closure of T (n)Eλ is tλ ˆ
Eλ and also ϕ( ˆ
Eλ).
The element Qλ = ˆ
Eλ ∈Cn is then an eigenvector of ϕ with eigenvalue tλ.
Now there are π(n) of these eigenvectors, (the number of partitions of n),
and the eigenvalues are all distinct, by [13]. Since Cn is spanned by π(n)
elements we can deduce that the elements Qλ form a basis for Cn, and that
the eigenspaces of ϕ are all 1-dimensional.
✷
It follows that any element of Cn which is an eigenvector of ϕ must be a
multiple of some Qλ.
The elements hi ∈C, discussed below, arise as Qλ for the Young diagram
λ consisting of a single row with i cells. Kawagoe [9] constructed an element
sλ of Cn for each partition λ of n, as a Schur polynomial of the sequence
{hi}, in Macdonald’s context of symmetric functions, [11]. He then used
skein theory to show that each sλ is also an eigenvector of the map ϕ. His
elements sλ can now be identiﬁed almost at once with the elements Qλ, by
theorem 3.1.
This gives an immediate proof of the multiplicative properties of the el-
ements Qλ in the skein of the annulus, since the elements sλ automatically
multiply according to the Littlewood-Richardson rules for Young diagrams
[11]. Conversely it guarantees that Kawagoe’s elements sλ are eigenvectors
for a wide range of skein maps on C as well as ϕ, using the skein properties
of Eλ from [13].
Recently Lukac, [10], has been able to simplify the proof that sλ is an
eigenvector of ϕ, by using algebraic properties of the skein A of the annulus
with an input on one boundary and an output on the other. Discussion and
9
use of the skein A in section 4 leads to simple descriptions for other symmetric
functions of the Murphy operators, derived from a direct interplay between
the skein of the annulus and the centre of the Hecke algebras.
