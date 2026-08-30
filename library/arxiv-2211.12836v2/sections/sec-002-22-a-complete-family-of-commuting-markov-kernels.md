---
doc_id: arxiv-2211.12836v2
doc_title: "QUANTUM COHOMOLOGY OF THE GRASSMANNIAN AND UNITARY DYSON BROWNIAN MOTION"
section_id: sec-002-22-a-complete-family-of-commuting-markov-kernels
section_title: "A complete family of commuting Markov kernels associated to Bk,n"
section_number: 2.2
pages: 4-6
source_pdf: 2211.12836v2.pdf
source_sha256: 4ffbb8b21f8b175d
doc_brief: "QUANTUM COHOMOLOGY OF THE GRASSMANNIAN AND UNITARY DYSON BROWNIAN MOTION — We study a class of commuting Markov kernels whose simplest element describes the movement ofk particles on a discrete"
---
state our main results, let us brieﬂy explain how to associate to Bk,n a family of Markov chains.
By analogy with the space L2(Tk) of square integrable functions on Tk, denote by L2(Bk,n) the
Hermitian space of functions on Bk,n with the distinguished orthonormal basisB0 ={eI,I ∈Bk,n}
QUANTUM COHOMOLOGY OF THE GRASSMANNIAN AND UNITARY DYSON BROWNIAN MOTION 5
given by eI(J) = δI,J . The edge structure of Bk,n can then be encoded by the operator A :
L2(Bk,n)→L2(Bk,n) given by
A(eI) =
∑
I↗J
eJ.
SinceBk,n is strongly connected, the adjacency matrix A is irreducible and thus there exist unique
(up to a scaling) left and right Perron-Frobenius eigenvectors hl and hr of A corresponding to the
same Perron-Frobenius eigenvalueλ. The coordinates hr(I),hl(I), I∈Bk,n are positive and λ> 0
so that the transformed matrix Ah given by
Ah(eJ) = 1
λ
∑
I∈Bk,n
hr(J)
hr(I)AIJeI
is a stochastic matrix with respect to the basis B0. The corresponding Markov chain started at
any vertex converges then in probability to the invariant measure µh such that µh(I) =hl(I)hr(I)
for I∈Bk,n, where hl and hr are normalized so that hl(I0) = 1 and ⟨hl,hr⟩ = 1. We call Ah the
h-transform ofA, by analogy with the speciﬁc situation where A comes from the Markov kernel of
a random walk on Zk conditioned to stay in a ﬁnite connected domain D⊂ Zk (see [20]).
As we will see later, in the case of Bk,n we have the explicit expression
hl(I) =|V (ξn(I))|
V (I0) , µ h(I) =|V (ξn(I))|2
nk ,
where V (⃗ u) denoting the Vandermonde determinant of (exp( iuj))1≤j≤k for ⃗ u= (u1,...,u k)∈ Rk,
so that
(2) V (ξn(I)) =
∏
j<j′
(
e2iπIj′/n−e2iπIj/n
)
= (2i)k(k−1)/2e(k−1)iπ⟨I⟩
n
∏
j<j′
sin
((Ij′−Ij)π
n
)
.
As this can be readily seen from the graph structure of Bk,n,
Ah(eI0) = 1
λ
|V (I0)|
|V (I1)|eI 1
where I1 ={k,k− 2,k− 3,..., 0} and λ is the Perron-Frobenius eigenvalue of A, which can be
proven to be equal to ∑k
a=1e
2iπ(k+1−a)
n .
Anticipating with the continuous case, let us denote by M≥0(Bk,n) the set of positive measures
on Bk,n, which can be viewed as vectors of L2(Bk,n) with nonnegative entries, and M1(Bk,n)⊂
M≥0(Bk,n) the subset of vectors of M≥0(Bk,n) integrating to 1 with respect to µh, namely
M1(Bk,n) =


µ∈L2(Bk,n)
⏐⏐⏐⏐⏐⏐
∑
I∈Bk,n
µ(I)µh(I) = 1, µ(I)≥ 0,I ∈Bk,n


.
Elements ofM1(Bk,n) are called h-probability measures in the sequel.
Our ﬁrst results give a product structure on L2(Bk,n) which restricts to a convolution product
on the setM1(Bk,n) of h-probability measures.
Proposition 2.1. There exists a unique product ∗ :L2(Bk,n)×L2(Bk,n)→L2(Bk,n) such that
(1) (L2(Bk,n), +,∗) is a commutative algebra,
(2)M1(Bk,n)∗M 1(Bk,n)⊂M 1(Bk,n),
(3) 1
λAh(y) = eI1
µh(I 1)∗y for all y∈L2(Bk,n),
(4)
(
eI
µh(I)
)
∗
( eI0
µh(I0)
)
= eI
µh(I) for all I∈Bk,n.
6 J. GUILHOT, C. LECOUVEY, AND P. TARRAGO
The existence of this convolution product on L2(Bk,n) reﬂects the fact that Bk,n is a positively
multiplicative graph, as introduced in [28]. Such graphs have several properties which we recall in
Appendix 3.
Remark 2.2. The existence of this convolution product extending the action of A and under which
M1(Bk,n) is stable reﬂects the fact that Bk,n encodes the Pieri rules in the small quantum cohomol-
ogy of the Grassmannian (see Appendix A for an introduction to this notion), which is an algebra
having nonnegative structure coeﬃcients in a particular basis. As we will see in Section 4, the ring
(L2(Bk,n), +,∗) is actually isomorphic to the ring of symmetric functions specialized at k-tuples of
distinct roots of (−1)k+1. In particular, one can see through this isomorphism that the convolution
by
eIS
µh(IS) for IS = (k,k− 1,..., 1) corresponds to the operatorSh on L2(Bk,n), where S is the shift
operatorSeI =e˜I where{˜Ii, 1≤i≤k} ={Ii + 1 [n], 1≤i≤k}.
Remark 2.3. The convolution algebra M1(Bk,n) is also deeply related to the fusion algebra for
the semi-simple Lie algebra of type Ak, see [18]. The latter is also a quotient of the small quantum
cohomology ring of the Grassmannian, and the structure coeﬃcients of each of those algebras can
be easily deduced from the other.
