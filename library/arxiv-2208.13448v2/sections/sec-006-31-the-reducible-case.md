---
doc_id: arxiv-2208.13448v2
doc_title: "ON THE COMPUTATION OF THE DIFFERENCE GALOIS GROUPS OF ORDER THREE EQUATIONS"
section_id: sec-006-31-the-reducible-case
section_title: "The reducible case"
section_number: 3.1
pages: 9-11
source_pdf: 2208.13448v2.pdf
source_sha256: 8bfa244cf7ca867d
doc_brief: "ON THE COMPUTATION OF THE DIFFERENCE GALOIS GROUPS OF ORDER THREE EQUATIONS — In this paper we consider the problem of computing the diﬀere nce Galois groups of order three equations for a large"
---
Lemma 2.4, G is reducible if and only if there exist T ∈ GLn(k), A1 ∈ GLm(k), m < n ,
and A2, A3 matrices of convenient size, such that
φ(T )AT −1 =
(
A1 A2
0 A3
)
.
The strategy of reduction will follow the one given in the diﬀe rential setting in [ DW19,
Section 5]. Let us assume that the bloc diagonal system [ D], where D :=
(
A1 0
0 A3
)
, is in
reduced form and let us see how to reduce [ A]. In general, [ D] is not in reduced form and
we have to reduce the bloc diagonal system with a bloc diagona l gauge transformation.
For small orders, we will see how to do this in practice but we w ant to emphasize the fact
that reducing the bloc diagonal system is a hard task in gener al. We denote by GD the
Galois group of [ D].
Lemma 3.1. Let B be a matrix of the form
(
A1 A2
0 A3
)
where D :=
(
A1 0
0 A3
)
is such
that the system [D] is in reduced form. A matrix T ∈ GLn(k) such that
[
φ(T )BT −1]
is
reduced can be found of the form T =
(
Idm ⋆
0 Id n−m
)
.
10 THOMAS DREYFUS AND MARINA POULET
Proof. It is the same kind of results as [ DW19, Theorem 2.4] adapted to this diﬀerence
context. We denote by G (respectively by GD) the Galois group of [ B] (respectively of
[D]). Let H be the smallest algebraic group of upper bloc triangular mat rices such that
B ∈ H(k). It is an algebraic group whose elements are of the form
(
H1 H2
0 H3
)
. We denote
by HD the group whose matrices are of the form
(
H1 0
0 H3
)
where
(
H1 H2
0 H3
)
∈ H for
a matrix H2, it is a block diagonal algebraic group. Let HU (respectively GU ) be the
subgroup of H (respectively G) whose elements are of the form
(
Idm ⋆
0 Id n−m
)
. We
have HD ∼ H/HU . Let us prove that the group HD is the smallest algebraic group
such that D ∈ HD(k). Indeed, considering the projection morphism π : H → HD,
where we identify H/HU and HD, if there exists an algebraic group ~HD ⊊ HD such that
D ∈~HD(k), then the algebraic group ~H := π−1(~HD) ⊊ H is such that B ∈ ~H(k), which
contradicts the minimality of H. Since [ D] is in reduced form, we have GD = HD. Let
R =
(
R1 R2
0 R3
)
∈ H(k) be such that the system
[
φ(R)BR−1]
is in reduced form. Let
RD :=
(
R1 0
0 R3
)
∈ HD(k) = GD(k).
Since GD ∼ G/GU , there exists Q2, such that Q :=
(
R1 Q2
0 R3
)
∈ G(k). Therefore
Q−1 =
(
R−1
1 ⋆
0 R−1
3
)
∈ G(k). A gauge transformation of φ(R)BR−1 ∈ G(k) by the
matrix Q−1 ∈ G(k) gives an element of G(k). Hence
[
φ(T )BT −1]
is in reduced form
where T := Q−1R =
(
Idm ⋆
0 Id n−m
)
. □
Remark 3.2. As in [DW19, Section 5] , we may also consider the case where the system
has more than two blocs. More precisely, consider a bloc tria ngular system [A], where
A =


A1 A1,2 . . .
A2 A2,3
. . .
0 Ak

 .
Let us assume that the bloc diagonal system [D], with D = Diag(A1, . . . , Ak), is in reduced
form. Then, the proof of Lemma 3.1 may be adapted in that context and we ﬁnd a gauge
transformation T =


Id ⋆ . . . ⋆
0 Id . . . ...
. . . ⋆
Id


∈ GLn(k) such that [φ(T )AT −1] is in reduced
form.
ON THE COMPUTATION OF THE DIFFERENCE GALOIS GROUPS OF ORDER T HREE EQ. 11
