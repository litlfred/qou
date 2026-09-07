---
doc_id: arxiv-2108.03616v2
doc_title: "Circuit imbalance measures and linear programming ∗"
section_id: sec-001-2-preliminaries
section_title: "Preliminaries"
section_number: 2
pages: 5-6
source_pdf: 2108.03616v2.pdf
source_sha256: 63696ad045602440
doc_brief: "Circuit imbalance measures and linear programming ∗ — We study properties and applications of various circuit imbalance mea sures associated with linear spaces."
---
We let [n] :={1,...,n }. For k∈ N, a number q∈ Q is 1/k-integral if it is an integer multiple
of 1/k. Let P⊆ N denote the set of primes. Let R++ denote the set of positive reals, and R+
the set of nonnegative reals.
For a prime number p∈ P, the p-adic valuation for Z is the function νp : Z→ N deﬁned by
νp(n) =
{
max{v∈ N :pv|n} if n⁄= 0
∞ if n = 0. (1)
We denote the support of a vector x∈ Rn by supp(x) = {i∈ [n] : xi⁄= 0}. We let /BD
n
denote the n-dimensional all-ones vector, or simply /BD , whenever the dimension is clear from the
context. Let ei denote the i-th unit vector.
For vectors v,w ∈ Rn we denote by min{v,w} the vector z∈ Rn with zi = min{vi,wi},i∈
[n]; analogously for max {v,w}. Further, we use the notation v+ = max{v, 0n} and v− =
max{−v, 0n} ; note that both v+ andv− are nonnegative vectors. For two vectors x,y∈ Rn, we
let⟨x,y⟩ =x⊤y denote their scalar product. For sets S,T ⊆ R we let S·T ={st|s∈S,t∈T}.
We let In∈ Rn×n denote the n-dimensional identity matrix. We let Dn denote the set of all
positive deﬁnite n×n diagonal matrices. For a vector v∈ Rn, we denote by diag(v) the diagonal
matrix whosei-th diagonal entry isvi and for a matrix A∈ Rm×n, letA1,A 2,...,A n∈ Rn denote
the column vectors, and A1,A 2,...,A m∈ Rm denote the row vectors, transposed. For S⊆ [n],
letAS denote the submatrix formed by the columns of A and for B⊆ [n],|B| =m, we say that
A is in basis form for B if AB =Im.
We will use ℓ1,ℓ 2 and ℓ∞ vector norms, denoted as ‖.‖1,‖.‖2, and ‖.‖∞, respectively. By
‖v‖, we always mean the 2-norm ‖v‖2. Further, for a matrix A∈ Rm×n,‖A‖ will refer to the
ℓ2→ℓ2 operator norm, and ‖A‖max = maxi,j|Aij| to the max-norm.
For an index subset I⊆ [n], we use πI : Rn→ RI for the coordinate projection. That is,
πI(x) = xI , and for a subset S⊆ Rn, πI (S) ={xI : x∈S}. We let Rn
I ={x∈ Rn :x[n]\I = 0}.
For a subspace W⊆ Rn, we let WI =πI (W∩ Rn
I ). It is easy to see that πI (W )⊥ = (W ⊥)I .
Assume we are given a matrix A∈ Rm×n such that W = ker(A). Then, WI = ker(AI ), and we
can obtain a matrix A′ fromA such thatπI (W ) = ker(A′) by performing a Gaussian elimination
of the variables in [ n]\I.
For a subspace W⊆ Rn, we deﬁne by Π W : Rn→ Rn the orthogonal projection onto W .
For a set of vectors V ={vi : i∈I} we let span(V ) denote the linear space spanned by the
vectors in V . For a matrix A∈ Rm×n, span(A)⊆ Rm is the subspace spanned by the columns
of A. A circuit basis of a subspace W⊆ Rn is a set F⊆F (W ) of rk(W ) linearly independent
elementary vectors, i.e., span(F) = W .
Linear Programming (LP) in matrix formulation We will use LPs in the following
standard primal and dual form for A∈ Rm×n, b∈ Rm, c∈ Rn.
min⟨c,x⟩
Ax =b
x≥ 0.
max⟨y,b⟩
A⊤y +s =c
s≥ 0.
(LP(A,b,c ))
Linear Programming in subspace formulation Since our main focus is on properties of
subspaces, it will be more natural to think about linear prog ramming in the following subspace
formulation. For A, b and c as above, let W = ker(A)⊆ Rn and d∈ Rn such that Ad =b. We
assume the existence of such a vector d as otherwise the primal program is trivially infeasible.
5
We can write LP(A,b,c ) in the following equivalent form:
min⟨c,x⟩
x∈W +d
x≥ 0.
max⟨c−s,d⟩
s∈W ⊥ +c
s≥ 0.
(LP(W,d,c ))
Conformal circuit decompositions We say that the vector y∈ Rn conforms to x∈ Rn if
xiyi > 0 whenever yi⁄= 0. Given a subspace W⊆ Rn, a conformal circuit decomposition of a
vectorz∈W is a decomposition
z =
h∑
k=1
gk,
whereh≤n andg1,g 2,...,g h∈F (W ) are elementary vectors that are conformal with z. A fun-
damental result on elementary vectors asserts the existenc e of a conformal circuit decomposition,
see e.g. [ Ful68, Roc69].
Lemma 2.1. For every subspace W⊆ Rn, every z∈W admits a conformal circuit decomposi-
tion.
Proof. Let F ⊆ W be the set of vectors conformal with z. F is a polyhedral cone; its faces
correspond to inequalities of the form yk≥ 0, yk≤ 0, or yk = 0. The rays (edges) of F are of
the form {αg : α≥ 0} for g∈F (W ). Clearly, z∈ F , and thus, z can be written as a conic
combination of at most n rays by the Minkowski–Weyl theorem. Such a decomposition yi elds a
conformal circuit decomposition.
Linear matroids For a linear subspace W⊆ Rn, letM(W ) = ([n],I) denote the associated
linear matroid, i.e. the matroid deﬁned by the set of circuit sCW . Here, I denotes the set of
independent sets; S∈I if and only if there exists no z∈W\{0} with supp(z)⊆S; the maximal
independent sets are the bases. We refer the reader to [ Sch03, Chapter 39] or [ Fra11, Chapter
5] for relevant deﬁnitions and background on matroid theory .
Assume rk(W ) = m and W = ker(A) for A∈ Rm×n. Then B⊆ [n],|B| = m is a basis in
M(A) :=M(W ) if and only if AB is nonsingular; then, A′ =A−1
B A is in basis form for B such
that ker(A′) = W .
The matroid M is separable, if the ground set [ n] can be partitioned into two nonempty
subsets [n] = S∪T such that I∈I if and only if I∩S,I∩T∈I . In this case, the matroid
is the direct sum of its restrictions to S and T . In particular, every circuit is fully contained in
S or in T . For the linear matroid M(A), separability means that ker( A) = ker(AS)⊕ ker(AT ).
In this case, we have κA = max{κAS,κAT} and ˙κA = lcm{ ˙κAS, ˙κAT}; solving LP(A,b,c ) can be
decomposed into two subproblems, restricted to the columns in AS and in AT .
Thus, for most concepts and problems considered in this pape r, we can focus on the non-
separable components ofM(W ). The following characterization will turn out to be very us eful,
see e.g. [ Fra11, Theorem 5.2.5].
Proposition 2.2. A matroid M = ([n],I) is non-separable if and only if for any i,j ∈ [n],
there exists a circuit containing i and j.
