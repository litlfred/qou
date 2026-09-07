---
doc_id: arxiv-2108.03616v2
doc_title: "Circuit imbalance measures and linear programming ∗"
section_id: sec-004-32-fractional-integrality-characterization
section_title: "Fractional integrality characterization"
section_number: 3.2
pages: 9-10
source_pdf: 2108.03616v2.pdf
source_sha256: 63696ad045602440
doc_brief: "Circuit imbalance measures and linear programming ∗ — We study properties and applications of various circuit imbalance mea sures associated with linear spaces."
---
Hoﬀman and Kruskal [ HK56] gave the following characterization of TU matrices. A poly hedron
P⊆ Rn is integral, if all vertices (=basic feasible solutions) are integer.
Theorem 3.5 (Hoﬀman and Kruskal, 1956) . An integer matrix A∈ Zm×n is totally unimodular
if and only if for every b∈ Zm , the polyhedron {x∈ Rn : Ax≤b,x≥ 0} is integral.
Since ˙κ is a property of the subspace, it will be more convenient to wo rk with the standard
equality form of an LP. Here as well as in Section 4.2, we use the following straightforward
correspondence between the two forms. Recall that an edge of a polyhedron is a bounded one
dimensional face; every edge is incident to exactly two vert ices. The following statement is
standard and easy to verify.
Lemma 3.6. Let A∈ Rm×n be of the form A = (A′|Im) for A′ = Rm×(n−m). For a vector
b∈ Rm, let
Pb ={x∈ Rn : Ax =b,x≥ 0} and P ′
b ={x′∈ Rn−m : A′x′≤b,x ′≥ 0}.
LetI = [n−m] denote the index set of A′. Then, P ′
b =πI (Pb), i.e., P ′
b is the projection of Pb
to the coordinates in I. For every vertex x of Pb, x′ =xI is a vertex of P ′
b, and conversely, for
every vertex x′ ofP ′
b, there exists a unique vertex x ofP such that xI =x′. There is a one-to-one
correspondence between the edges of Pb and P ′
b. Further, if b∈ Zm, then Pb is 1/k-integral if
and only if P ′
b is 1/k-integral.
Using Theorem 3.4 and Lemma 3.6, we can formulate Theorem 3.5 in subspace language.
Corollary 3.7. LetW⊆ Rn be a linear space. Then, κW = 1 if and only if for every d∈ Zn,
the polyhedron{x∈ Rn : x∈W +d,x≥ 0} is integral.
Proof. Letn′ =n−m = dim(W ). W.l.o.g., assume the last m variables form a basis, and let us
represent W in a basis form as W = ker(A) for A = (A′|Im), where A′∈ Rm×n′
. It follows by
Theorem 3.4 that κW = 1 if and only if A is TU, which is further equivalent to A′ being TU.
Further, note that the system {x∈ Rn : x∈W +d,x ≥ 0} coincides with Pb ={x∈ Rn :
(A′|Im)x =b,x≥ 0}, where b =Ad.
Note that b = Ad is integer whenever d ∈ Zm. Moreover, we can obtain every integer
vector in b∈ Zm this way, since A contains an identity matrix. According to Lemma 3.6, Pb
is integral if and only if P ′
b ={x∈ Rn−m : A′x′≤ b,x ′≥ 0} is integral. The claim follows by
Theorem 3.5.
We provide the following natural generalization. Related s tatements, although in substan-
tially more complicated forms, were given in [ Lee89, Proposition 6.1 and 6.2].
Theorem 3.8. LetW⊆ Rn be a linear space. Then, ˙κW is the smallest integer k∈ Z such that
for every d∈ Zn, the polyhedron {x∈ Rn : x∈W +d,x≥ 0} is 1/k-integral.
9
Proof. Let dim(W ) = n−m, and let us represent W = ker(A) for A∈ Rm×n. Then, x∈W +d,
x≥ 0 can be written as Ax =Ad, x≥ 0. Let x be a basic feasible solution (i.e. vertex) of this
system. Then, x =A−1
B Ad. By Proposition 3.1,A−1
B A is 1/ ˙κW -integral. Thus, if d∈ Zn thenx
must be also 1 / ˙κW -integral.
Let us now show the converse direction. Assume {x∈ Rn : x∈W +d,x≥ 0} is 1/k-integral
for every d∈ Zn. For a contradiction, assume there exists a circuit C∈C W such that the entries
of the elementary vector are not all divisors of k (or that gC is not even a rational vector if
W is not a rational space). In particular, select an index ℓ∈C such that gC
ℓ ∤ k, or such that
(1/gC
ℓ )gC is not rational.
Let us select a basis B⊆ [n] such that C\B ={ℓ}. For simplicity of notation, let B = [m].
We can represent W = ker(A) in a basis form as A = (Im|A′). Let g∈ Rn be deﬁned by gℓ = 1,
gj =−Ajℓ for j∈B and gj = 0 otherwise; thus, g = (1/gC
ℓ )gC .
Let us pick an integer t∈ N, t≥‖ g‖∞, and deﬁne d∈ Zn by dj = t for j∈ B, dℓ =−1,
and dj = 0 otherwise. Then, the basic solution of x∈W +d, x≥ 0 corresponding to the basis
B is obtained as xj = t +gj for j∈ B and xj = 0 for j∈ [n]\B. The choice of t guarantees
x≥ 0. By the assumption, x is 1/k-integer, and therefore g is also 1 /k-integer. Recall that
g = (1/gC
ℓ )gC , where either gC∈ Zn with lcm(gC ) = 1 and gC
ℓ ∤ k, or g is not rational. Both
cases give a contradiction.
Using again Lemma 3.6, we can write this theorem in a form similar to the Hoﬀman-Krus kal
theorem.
Corollary 3.9. LetA = (A′|Im)∈ Rm×n. Then, ˙κA is the smallest value k such that for every
b∈ Zm, the polyhedron {x′∈ Rn−m : A′x′≤b,x ′≥ 0} is 1/k-integral.
Appa and Kotnyek [ AK04, Theorem 17] show that k-regularity of A′ (in the sense that the
inverse of every square submatrix is 1 /k-integral) is equivalent to the property above.
Subspaces with ˙κA = 2 The case ˙ κW = 2 is a particularly interesting class. As already
noted, it includes incidence matrices of undirected graphs , and according to Theorem 3.8, it
corresponds to half-integer polytopes. This class include s the following matrices, ﬁrst studied
by Edmonds and Johnson [ EJ70]; the following result follows e.g. from [ AK04,GS86,HMNT93].
Theorem 3.10. Let A∈ Zm×n such that for each column j ∈ [n], ∑ m
i=1|Aij| ≤2. Then
˙κA∈{ 1, 2}.
Appa and Kotnyek [ AK04] deﬁne binet matrices as A′ = A−1
B A for a matrix A as in The-
orem 3.10 for a basis B. Clearly, these matrices have ˙ κA′∈{ 1, 2} since they deﬁne the same
subspace.
Deciding whether a matrix has ˙ κA = 2 (or more generally, ˙ κA = k for a ﬁxed constant
k) is an interesting open question: is it possible to extend Se ymour’s decomposition [ Sey80]
from TU matrices? The matrices in Theorem 3.10 could be a natural building block of such a
decomposition.
