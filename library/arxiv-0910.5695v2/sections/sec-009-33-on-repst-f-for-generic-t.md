---
doc_id: arxiv-0910.5695v2
doc_title: "ON BLOCKS OF DELIGNE’S CATEGORY Rep(St)"
section_id: sec-009-33-on-repst-f-for-generic-t
section_title: "On Rep(St; F) for generic t"
section_number: 3.3
pages: 18-19
source_pdf: 0910.5695v2.pdf
source_sha256: 703c2a2f1f9380b1
toc_source: outline
doc_brief: "ON BLOCKS OF DELIGNE’S CATEGORY Rep(St) — We describe blocks in Deligne’s category Rep(St)."
---
is semisimple for “generic” values of t.
Deligne showed that Rep(St; F) is not
semisimple if and only if t is a nonnegative integer (see [Del07]). That result will
follow from our description of the blocks in Rep(St; F) (see Corollary 5.23). For
now we conﬁne ourselves to prove a weaker result (see Theorem 3.15) which allows
us to conclude that Rep(ST ; K) is semisimple (see Corollary 3.17).
The following well-known lemma will be useful in showing that Rep(St; F) is
generically semisimple.
Lemma 3.13. Suppose A is a ﬁnite dimensional F-algebra. For a ∈A, let φa
denote the F-linear map A →A given by x 7→ax. Deﬁne the trace form on A by
(a, b) := tr (φaφb). Then A is a semisimple algebra if and only if the trace form on
A is non-degenerate.
Proof. Let S := {a ∈A | (a, b) = 0 for all b ∈A}. We will show that S is equal
to J(A) (the Jacobson radical of A). Suppose a ∈J(A). Since J(A) is a nilpotent
ideal, ab is nilpotent for every b ∈A. Hence (a, b) = 0 for all b ∈A, so J(A) ⊂S. To
show S ⊂J(A) it suﬃces to show that every element of S is nilpotent. If a ∈S then
tr (φn
a) = 0 for all integers n > 0. If we let x1, . . . , xr ∈F denote the eigenvalues of
φa, then we have Pr
i=1 xn
i = 0 for all n > 0. Hence, any non-constant symmetric
polynomial in x1, . . . , xr is zero (see for example [Mac95]). Thus the characteristic
polynomial of φa must be χ(X) = Xr. Therefore φa, and thus a, is nilpotent.
□
Before showing Rep(St; F) is generically semisimple we give two examples illus-
trating the usefulness of Lemma 3.13. The reader may ﬁnd these examples helpful
when reading the proof of Theorem 3.15.
Example 3.14. (1) Consider the partition algebra FP1(t). Let π be as in the
proof of Theorem 3.4 and ﬁx the ordered basis P1,1 = {id1, π} for FP1(t). Under
this ordered basis the matrix with entries (x, y) for x, y ∈P1,1 is
 2
t
t
t2

Since the determinant of the matrix above is t2, we conclude (by Lemma 3.13) that
FP1(t) is semisimple if and only if t̸ = 0.
(2) Consider the partition algebra FP2(t). Using the ordered basis
ON BLOCKS OF DELIGNE’S CATEGORY Rep(St).
19
the matrix with entries (π, µ) for π, µ ∈P2,2 is

















2t4
2t3
2t3
2t3
2t3
2t3
2t3
2t2
2t2
2t2
2t2
2t2
2t2
2t2
2t
2t3
5t2
2t2
2t2
2t2
2t2
2t2
5t
2t
2t
2t
5t
5t
2t
5
2t3
2t2
5t2
2t2
2t2
2t2
2t2
5t
2t
2t
5t
2t
2t
5t
5
2t3
2t2
2t2
2t2
2t3
2t2
2t2
2t
2t2
2t
2t2
2t2
2t
2t
2t
2t3
2t2
2t2
2t3
2t2
2t2
2t2
2t
2t2
2t
2t
2t
2t2
2t2
2t
2t3
2t2
2t2
2t2
2t2
2t2
5t2
2t
2t
5t
5t
2t
5t
2t
5
2t3
2t2
2t2
2t2
2t2
5t2
2t2
2t
2t
5t
2t
5t
2t
5t
5
2t2
5t
5t
2t
2t
2t
2t
15
2t
7
5
5
5
5
5
2t2
2t
2t
2t2
2t2
2t
2t
2t
2t2
2t
2t
2t
2t
2t
2t
2t2
2t
2t
2t
2t
5t
5t
7
2t
15
5
5
5
5
5
2t2
2t
5t
2t2
2t
5t
2t
5
2t
5
5
5
2t
5t
5
2t2
5t
2t
2t2
2t
2t
5t
5
2t
5
5
5
5t
2t
5
2t2
5t
2t
2t
2t2
5t
2t
5
2t
5
2t
5t
5
5
5
2t2
2t
5t
2t
2t2
2t
5t
5
2t
5
5t
2t
5
5
5
2t
5
5
2t
2t
5
5
5
2t
5
5
5
5
5
5

















The determinant of the matrix above is 1259712t14(t−1)4(t−2)6. Hence, by Lemma
3.13, FP2(t) is semisimple if and only if t̸ = 0, 1, 2.
2
Now to prove that Rep(St; F) is generically semisimple.
Theorem 3.15. Rep(St; F) is semisimple for all but countably many values of t.
Moreover, if Rep(St; F) is not semisimple, then t is an algebraic integer.
Proof. We may assume t̸ = 0. Suppose L1 and L2 are two indecomposable objects
in Rep(St; F). By Proposition 2.20(2) along with Lemma 3.6(1)(2) we can ﬁnd a
nonnegative integer n and idempotents e1, e2 ∈FPn(t) so that L1 ∼= ([n], e1) and
L2 ∼= ([n], e2). Whence HomRep(St;F )(L1, L2) = e2FPn(t)e1. Thus, in order to
show HomRep(St;F )(L1, L2) is either zero or a ﬁnite dimensional division algebra
over F, it suﬃces to show FPn(t) is a semisimple algebra. Therefore, for a ﬁxed
t ∈F, Rep(St; F) is semisimple whenever FPn(t) are semisimple for all n ≥0.
Let Mn(t) denote the matrix whose rows and columns are labelled by the ele-
ments of Pn,n (in some ﬁxed order) with the x, y-entry equal to (x, y) (the trace
form on FPn(t), see Lemma 3.13). Then the entries of Mn(t) are in Z[t]. Hence
det Mn(t) ∈Z[t]. It follows from Lemma 3.13 that FPn(t) is semisimple if and
only if det Mn(t)̸ = 0. However, from Theorem 2.6, we know that FPn(d) is semi-
simple for integers d ≥2n. Hence, det Mn(t) is a polynomial in t which is not
identically zero. Thus, for each n ≥0 there are only ﬁnitely many values of t for
which det Mn(t) = 0. Therefore there are only countably many values of t for which
FPn(t) is not semisimple for all n ≥0.
□
Remark 3.16. If t ∈F is not an algebraic integer, then by Theorem 3.15 we know
Rep(St; F) is semisimple. However, given an arbitrary t ∈F, neither Theorem 3.15
nor its proof allow us to determine if Rep(St; F) is semisimple. As mentioned at
the beginning of this section, we will eventually show that Rep(St; F) is semisimple
if and only if t is not a nonnegative integer.
We close this section with one ﬁnal observation.
Corollary 3.17. Rep(ST ; K) is semisimple.
Proof. This follows from Theorem 3.15 as T is not an algebraic integer.
□
