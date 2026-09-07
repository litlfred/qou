---
doc_id: arxiv-2208.13448v2
doc_title: "ON THE COMPUTATION OF THE DIFFERENCE GALOIS GROUPS OF ORDER THREE EQUATIONS"
section_id: sec-014-62-imprimitive-case
section_title: "Imprimitive case"
section_number: 6.2
pages: 30-34
source_pdf: 2208.13448v2.pdf
source_sha256: 8bfa244cf7ca867d
doc_brief: "ON THE COMPUTATION OF THE DIFFERENCE GALOIS GROUPS OF ORDER THREE EQUATIONS — In this paper we consider the problem of computing the diﬀere nce Galois groups of order three equations for a large"
---
imprimitive. This case is solved in Section 3.2. It is imprimitive if and only if the diﬀerence
Galois group of φ3Y = A[3]Y is diagonal. We use the reducible case (with φ replaced by
φ3) to check this property. In that case we are able to compute d ∈ k∗, solution of the
Riccati equation corresponding to φ3Y = A[3]Y . We now follow Proposition 3.10. Let us
compute a reduced form of φ(y) = dy, that is compute f ∈ k∗ such that φ(y) = d φ(f )
f y
is reduced. Then, a reduced form is given by


0 1 0
0 0 f −1
φ(f )d 0 0

 with reduction matrix
Diag(1, 1, f).
6.3. Primitive case. Assume now that G is irreducible and primitive. Let D(G0) be the
derived subgroup of G0 that is irreducible and primitive by Proposition 3.18. By deﬁnition,
D(G0) ⊂ SL3(C). By [ SU93, Section 2.2], either D(G0) is SL 3(C), or it is isomorphic
to PSL 2(C). Since SO 3(C) is also a primitive subgroup of SL 3(C), it is isomorphic to
PSL2(C). The matrices commuting with SL 3(C) (resp. SO 3(C)) are dilatations and we
ﬁnd that Z(G0), the center of G0, is isomorphic to an algebraic subgroup of C ∗. Since it
is connected, it is then C ∗ or {1}. By Proposition 3.18, G0 = Z(G0).D(G0).
When D(G0) = SL 3(C) we ﬁnd that either G0 = GL 3(C), or G0 = SL 3(C). Since
G/G0 is cyclic, we deduce that either G = GL 3(C), or there exists an integer k, which
is the order of the group G/G0, such that G = {M ∈ GL3 (C) | det(M )k = 1 }. Then
G = Z(G).D(G), where Z(G) is composed by dilatations matrices and D(G) = SL 3(C).
Assume now that D(G0) = SO 3(C). Then either G0 ∼ C ∗.SO3(C), or G0 = SO 3(C).
Moreover, since G/G0 is cyclic, it is abelian and since the derived group D(G) is the
smallest subgroup H of G such that G/H is abelian, we have D(G) ⊂ G0. Then
SO3(C) = D(G0) ⊂ D(G) ⊂ G0 ⊂ C ∗.SO3(C). The normalizer of SO 3(C) in GL 3(C) is
ON THE COMPUTATION OF THE DIFFERENCE GALOIS GROUPS OF ORDER T HREE EQ. 31
C ∗.SO3(C) and the same holds for C ∗.SO3(C). Since the normalizer of D(G) in G, which
is G, is included in the normalizer of D(G) in GL 3(C), we ﬁnd that G ⊂ C ∗.SO3(C).
Thus, SO 3(C) ⊂ G ⊂ C ∗.SO3(C). Then, either G ∼ C ∗.SO3(C), or there exists k ∈ N∗,
such that G ∼ Uk.SO3(C), where Uk denote the group of all k-th roots of unity. Hence
G = Z(G).D(G), where Z(G) is composed by dilatations matrices and D(G) = SO 3(C).
To summary, we have proved the following result:
Proposition 6.6. Assume that G is irreducible and primitive. Then, G = Z(G).D(G),
where Z(G) is included in the group of scalar matrices and D(G) is either SL3(C) or
SO3(C).
Remark 6.7. If D(G) = SL 3(C), then Z(G) = {λId3 where λ3 ∈ det(G)} . Recall that
det(G) is the Galois group of an equation of order one φ(y) = det( A)y.
Assume now D(G) = SO 3(C). If det(G) = C ∗, then Z(G) = C ∗. If det(G) = Un with
gcd(n, 3) ⁄= 1 , then Z(G) = U3n. In the case det(G) = Un with gcd(n, 3) = 1 , we have
Z(G) = U3n or Un.
We want to give a criterion to decide whether D(G) = SO 3(C) or not. Let us prove the
following lemma.
Lemma 6.8. Assume that G is irreducible and primitive. Let k be the algebraic closure of
k. We may extend φ on the latter. The following facts are equivalent.
• D(G) = SO 3(C).
• there exist T ∈ GL3(k), λ ∈ k∗ and B ∈ SO3(k) such that
(6.6) φ(T )AT −1 = λB.
• there exist T ∈ GL3(k), λ ∈ k
∗
and B ∈ SO3(k) such that (6.6) holds.
Proof. Recall that G ∼ Z(G).D(G), where D(G) ∈ { SO3(C), SL3(C)} and Z(G) is
composed by dilatations matrices. By Theorem 2.1, D(G) = SO 3(C) if and only if there
exist T ∈ GL3(k), λ ∈ k∗ and B ∈ SO3(k) such that ( 6.6) holds. So the ﬁrst two items are
equivalent. If the second item holds, then the third item hol ds. Conversely assume that the
third item holds. Consider G, the Galois group over k. By Theorem 2.1, G ⊂ C
∗
.SO3(C).
By Galois correspondence, see [ VdPS97, Chapter 1], G is a subgroup of G and G/G is
ﬁnite. Since G ∼ Z(G).D(G), where D(G) ∈ { SO3(C), SL3(C)}, this shows that D(G)
cannot be SL 3(C). Then D(G) = SO 3(C). □
The equation ( 6.6) is non linear and may be complicated to solve. Let us see how w e
may reduce to a linear equation over k. For the sake of completeness, let us ﬁrst prove a
well-known result that will be used in the sequel.
Lemma 6.9. Let K be a ﬁeld of characteristic zero. Let X ∈ GLn(K) be a symmetric
matrix. Then, there exist F, D ∈ GLn(K) with D diagonal such that X = F DF t.
Proof. Let Ei,j be the square matrix of order n whose (i, j) entry is 1 and the other entries
are 0. For i ⁄= j, let Ti,j be the corresponding transvection matrix, that is Id n + Ei,j. If
we consider Ti,jX(Ti,j)t we make the following operations: the column Ci of X is replaced
32 THOMAS DREYFUS AND MARINA POULET
by Cj + Ci and then the line Li is replaced by Li + Lj. Take i = 1. This shows that X1,1
is replaced by X1,1 + Xj,1 + X1,j + Xj,j = X1,1 + 2X1,j + Xj,j.
Let us see how to reduce to the case X1,1 ⁄= 0. Assume X1,1 = 0. If there exists j > 1
such that Xj,j ⁄= 0 then we replace X by P XP t where P = E1,j + Ej,1 + ∑
k⁄=1,j
Ek,k is
the permutation matrix which exchanges the lines 1 and j. We have P = P −1 = P t. If
Xj,j = 0 for all j, we consider j such that X1,j ⁄= 0 (such j exists otherwise the ﬁrst line
is only composed of 0 entries, contradicting the fact that X is invertible). Let us perform
T1,jX(T1,j)t so that X1,1 is replaced by X1,1 + 2X1,j + Xj,j = 2X1,j ⁄= 0. So we may reduce
to the case where X1,1 ⁄= 0.
For i ∈ { 2, . . . , n}, let T := Id n + αiEi,1 with αi := −Xi,1/X1,1. Computing
T XT t, Xi,1 is replaced by αiX1,1 + Xi,1 = 0 thus, as in a Gaussian Pivot, we force
X2,1 = · · · = Xn,1 = 0. We also have X1,2 = · · · = X1,n = 0 since the matrix obtained
remains symmetric. We repeat the procedure to the other line s and columns to ﬁnd the
result. □
Toward an eﬃcient way to check that ( 6.6) holds, let us prove the following.
Lemma 6.10. The following facts are equivalent.
• There exist T ∈ GL3(k), λ ∈ k
∗
and B ∈ SO3(k) such that (6.6) holds.
• There exist λ ∈ k
∗
, X ∈ GL3(k) such that X = X t, and AXAt = λ2φ(X).
Proof. Let us prove that the ﬁrst point implies the second. Let us ass ume the existence
of T ∈ GL3(k), λ ∈ k
∗
, and B ∈ SO3(k) such that ( 6.6) holds. Let us set P := T −1 and
note that P t is the inverse of T t. Using BB t = Id 3 we ﬁnd that ( 6.6) implies
φ(T )AP P tAtφ(T t) = λ2Id3.
The latter is equivalent to
AP P tAt = λ2φ(P P t).
We obtain the result if we set X = P P t.
Conversely, assume that the second item holds. By Lemma 6.9, let us write X = F DF t
with matrices whose coeﬃcients are in k. Since k is algebraically closed, F
√
D has
coeﬃcients in k and we may write X = F
√
D(
√
D)tF t, where
√
D is any diagonal matrix
whose square is D. Let us perform φ(T )AT −1 where T ∈ GL3(k) is the inverse of F
√
D.
Note that X = T −1(T −1)t. It suﬃces to prove that B = φ(T )AT −1λ−1 ∈ SO3(k). Then,
BB t = λ−2φ(T )AT −1(T −1)tAtφ(T t) = λ−2φ(T )AXAtφ(T t).
We now use AXAt = λ2φ(X) to deduce that the latter equals φ(T )φ(X)φ(T t). With
X = T −1(T −1)t, we deduce that φ(T )φ(X)φ(T t) is the identity, that is B ∈ SO3(k). □
If we replace X by X ′ := X det(X)−1/3 ∈ SL3(k), we ﬁnd AX′At = det( A)2/3φ(X ′).
Indeed, the equality AXAt = λ2φ(X) is equivalent to
(6.7) AX′At = λ2 det(X)−1/3 det(φ(X))1/3φ(X ′) .
ON THE COMPUTATION OF THE DIFFERENCE GALOIS GROUPS OF ORDER T HREE EQ. 33
Taking the determinant in ( 6.7) and using that det( X ′) = 1, we have det( A)2 =
λ6 det(X)−1 det(φ(X)). We obtain the desired result thanks to ( 6.7) and this last equality.
With Lemma 6.8, and Lemma 6.9, we have proved the following result.
Proposition 6.11. Assume that G is irreducible and primitive. Then, D(G) = SO 3(C) if
and only if there exists X ∈ SL3(k) such that X = X t and AXAt = det(A)2/3φ(X).
Proposition 6.11 then reduces the criterion on D(G) to look at solutions in k of linear
φ-diﬀerence systems with coeﬃcients in k. More precisely the condition X = X t drops
the number of unknowns from 9 to 6. Solving a system in k is in general a complicated
task but in many examples, by studying the poles of the system for instance, we might be
able to prove that the system has no solutions, showing that D(G) ⁄= SO 3(C).
Let us now see how to compute the reduced form. First, assume t hat D(G) = SL 3(C).
We compute det(G) as the diﬀerence Galois group of an order one system φ(y) = a0y with
reduction matrix f ∈ k∗, that is φ(y) = a0
φ(f )
f y is reduced with Galois group det( G).
Then, we perform, as in [ Hen98, Section 4.4], the gauge transformation T = Diag( f, 1, 1)
to obtain a system [ B]. Since det( B) = a0
φ(f )
f , and φ(y) = a0
φ(f )
f y is reduced with Galois
group det( G), we ﬁnd that B ∈ G(k). Then, B is a reduced form and T is the reduction
matrix.
Now consider the case where D(G) = SO 3(C). By Lemma 6.8, we know that
there exist T ∈ GL3(k), λ ∈ k∗ and B ∈ SO3(k) such that ( 6.6) holds. As above,
let us set X ′ = T −1(T −1)t det(T )2/3 ∈ SL3(k). Then, X ′ satisﬁes X ′ = ( X ′)t and
AX′At = det(A)2/3φ(X ′). Let us write X ′ = F DF t as in Lemma 6.9. Note that the proof
of Lemma 6.9 is constructive so F and D may be eﬀectively computed. Let us perform
the gauge transformation φ(α(F
√
D)−1)A(α(F
√
D)−1)−1 where ( F
√
D)−1 ∈ GL3(k) and
α ∈ k
∗
. From what precedes, all reduction matrices with coeﬃcient s in k are of this
form. Since there is a reduction matrix with coeﬃcients in k, there is a choice of X ′ and
α such that the corresponding α(F
√
D)−1 has entries in k. Note that this procedure is
purely theoretical and not eﬀective. So if α(F
√
D)−1 does not have entries in k for all
α ∈ k
∗
, we take another solutions X ′ with a corresponding α(F
√
D)−1 ∈ GL3(k). At this
stage, we have φ(α(F
√
D)−1)A(α(F
√
D)−1)−1 = βA0, with β ∈ k∗ and A0 ∈ SO3(k).
By Theorem 2.1 and Proposition 6.6, we ﬁnd that a reduction matrix is of the form
α1α(F
√
D)−1, α1 ∈ k∗. We may compute α1 by reducing the system φ(y) = βy. Hence
the reduced form is φ(α1)
α1
βA0.
Example 6.12. Consider G the diﬀerence Galois group of (1.1) over C(z1/∗). Assume that
t ⁄= 0 . Assume by contradiction that D(G) = SO 3(C). The eigenvalues of matrices of
SO3(C) are of the form (1, a±1), a ∈ C∗. Then, the eigenvalues of elements of G are for
the form (c, ca±1), c, a ∈ C∗. By [RS09, Section 2.4] , combined with the computation of
the Newton polygon in Example 3.15, G contains the so-called theta torus, elements of the
form Diag(1, 1, d), d ∈ C∗. If the triple Diag(1, 1, d) is of the form (c, ca±1), then either
a = 1 = c = d, or a = c = −1 and d = −1. Then, Diag(1, 1, 2) can never be of the form
(c, ca±1), showing that D(G) ⁄= SO 3(C). Then D(G) = SL 3(C).
34 THOMAS DREYFUS AND MARINA POULET
