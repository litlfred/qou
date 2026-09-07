---
doc_id: arxiv-2208.13448v2
doc_title: "ON THE COMPUTATION OF THE DIFFERENCE GALOIS GROUPS OF ORDER THREE EQUATIONS"
section_id: sec-012-61-reducible-case
section_title: "Reducible case"
section_number: 6.1
pages: 22-23
source_pdf: 2208.13448v2.pdf
source_sha256: 8bfa244cf7ca867d
doc_brief: "ON THE COMPUTATION OF THE DIFFERENCE GALOIS GROUPS OF ORDER THREE EQUATIONS — In this paper we consider the problem of computing the diﬀere nce Galois groups of order three equations for a large"
---
if and only if G is reducible. Recall, see Lemma 2.5, that it is equivalent to the existence
of a solution α of the Riccati equation φ(y)y + a1y + a0 = 0.
Assume ﬁrst that L is reducible and let us write L = (φ−β)(φ−α). Then, α is a solution
of the Riccati equation φ(y)y+a1y+a0 = 0, and β is determined by αβ = a0. The diﬀerence
equation is equivalent to φ(Y ) = AY where A =
(
α 1
0 β
)
. We now follow the strategy of
Section 3.1. As in the diagonal case, we reduce the diagonal system φ(Y ) =
(
α 0
0 β
)
Y
with a diagonal matrix D. Let B := φ(D)AD−1, with B =
(
α′ γ′
0 β′
)
. By [ Hen98,
Lemma 4.4], either [ B] is already reduced, or a reduced form is
(
α′ 0
0 β′
)
. We now have
to decide if there exists t ∈ k such that T =
(
1 t
0 1
)
satisﬁes φ(T )B =
(
α′ 0
0 β′
)
T .
Note that this is equivalent to
γ′ + φ(t)β′ = α′t.
So we just have to decide if an equation of order 1 has a solutio n t in k or not. If such
a t exists, then the reduction matrix is given by T D, and a reduced form is
(
α′ 0
0 β′
)
.
Otherwise, the reduction matrix is given by D and a reduced form is
(
α′ γ′
0 β′
)
.
Imprimitive case. Assume now that G is irreducible. It is imprimitive if and only if the
diﬀerence Galois group of φ2(Y ) = A[2]Y is diagonal. We use the reducible case (with φ
replaced by φ2) to check this property. In that case we are able to compute d ∈ k∗, solution
of the Riccati equation corresponding to φ2(Y ) = A[2]Y . We now follow Proposition 3.10.
The system [ A] is equivalent to φ(Y ) =
(
0 1
d 0
)
Y . Let us compute a reduced form of
φ(y) = dy, that is compute f ∈ k∗ such that φ(y) = d φ(f )
f y is reduced. Then, a reduced
form is given by
(
0 f −1
φ(f )d 0
)
and a reduction matrix is given by Diag(1 , f) .
Primitive case. Assume that G is irreducible and primitive. By [ Hen98, Section 4.4], either
G = GL 2(C), or there exists an integer k such that
G = {M ∈ GL2 (C) | det(M )k = 1}.
ON THE COMPUTATION OF THE DIFFERENCE GALOIS GROUPS OF ORDER T HREE EQ. 23
Recall that a0 = det( A) and the algebraic group det( G) is the diﬀerence Galois group of
φ(y) = a0y, a system of order 1. Let f ∈ k∗ be such that φ(y) = a0
φ(f )
f y is reduced
with Galois group det( G). Then, we perform, as in [ Hen98, Section 4.4], the gauge
transformation T = Diag( f, 1) to obtain a system [ B]. Since det( B) = a0
φ(f )
f , and
φ(y) = a0
φ(f )
f y is reduced with Galois group det( G), we ﬁnd that B ∈ G(k). Then,
B is a reduced form and T is the reduction matrix.
