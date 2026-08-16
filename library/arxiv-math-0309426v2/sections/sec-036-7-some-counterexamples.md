---
doc_id: arxiv-math-0309426v2
doc_title: "ELEMENTARY DIVISORS OF SPECHT MODULES"
section_id: sec-036-7-some-counterexamples
section_title: "Some counterexamples"
section_number: 7
pages: 17-19
source_pdf: 0309426v2.pdf
source_sha256: f2aa01164d9f243c
doc_brief: "ELEMENTARY DIVISORS OF SPECHT MODULES — 46 sections: MATTHIAS K ¨UNZER AND ANDREW MATHA; Introduction and statement of main; The Hecke algebra and permutation"
---
LetR = Z[q,q −1]. We write the mth cyclotomic polynomial in q as Φ m = Φ m(q).
Andersen remarked that in general the Gram matrix G(λ) is not diagonalizable
[1, Remark 5.11]. We give two examples of this kind.
Note that G(λ) is divisibly diagonalizable over Z(p)[q,q −1] for all but ﬁnitely
many primes p. In fact, it suﬃces to exclude the primes occurring in the denomi-
nators of the entries of the matrices used to diagonalize G(λ) over Q[q,q −1].
We record the elementary divisors in “jump notation”. That is, we wr ite
✲f1
m1 ✲f2
m2 ✲f3
m3 ✲f4
· · · ✲fs
ms
18 MATTHIAS K ¨UNZER AND ANDREW MATHAS
to indicate that the matrix has the elementary divisor f1 with multiplicity m1,
the elementary divisor f1f2 with multiplicity m2, . . . , and the elementary divisor
f1 · · ·fs with multiplicity ms.
7.1. Example. Letλ = (3, 3, 2). The elementary divisors of G(3, 3, 2) over Q[q,q −1]
are given by
✲Φ 2
2
1
✲Φ 4
20 ✲Φ 3Φ 5
20 ✲Φ 4
1 ;
over F2[q,q −1] they are given by
✲Φ 3
2
1
✲Φ 2
20 ✲Φ 3Φ 5
20 ✲Φ 2
1 ;
and, putting q = 1, over Z they are given by
✲23
21 ✲3·5
21.
We claim that G(3, 3, 2) is not diagonalizable over Z(2)[q,q −1]. To see this suppose
that it is diagonalizable. Then, considered as an element of Z(2)[q,q −1], any result-
ing diagonal entry must contain the factor ( q + 1) with exponent 2. Considered as
an element of F2[q,q −1] the factor ( q + 1) can occur only with even exponent in
such a diagonal entry. But this is not the case, so we have a contra diction.
This claim in particular implies that G(3, 3, 2) is not diagonalizable over Z[q,q −1].
We remark that the comparison of the elementary divisors over Q[q,q −1] and
over Z yields a contradiction to diagonalizability over Z(2)[q,q −1], too.
7.2. Example. Let λ = (4, 2, 1, 1). The elementary divisors of G(4, 2, 1, 1) over
Q[q,q −1] are given by
✲Φ 2
14 ✲Φ 2
1 ✲Φ 4
30 ✲Φ 7
30 ✲Φ 4
1 ✲Φ 2
14 ;
over F2[q,q −1] they are given by
✲Φ 2
14 ✲Φ 2
2
1
✲Φ 2
30 ✲Φ 7
30 ✲Φ 2
1 ✲Φ 2
2
14 ;
over F3[q,q −1] they are given by✲Φ 2
13 ✲Φ 2
2 ✲Φ 4
30 ✲Φ 7
30 ✲Φ 4
2 ✲Φ 2
13 ;
and, putting q = 1, over Z they are given by
✲2
14 ✲22
31 ✲7
31 ✲22
14.
We claim that G(4, 2, 1, 1) is not diagonalizable over Z(2)[q,q −1]. Again, by way
of contradiction suppose that it is diagonalizable. In F2[q,q −1], 14 of the resulting
diagonal entries contain the factor (q+1) with exponent 1. Therefore, in Z(2)[q,q −1],
14 of them contain the factor ( q + 1) with exponent 1 and the factor ( q2 + 1) with
exponent 0. Similarly, in F2[q,q −1], 14 of the resulting diagonal entries contain the
factor (q + 1) with exponent 7. Thus in Z(2)[q,q −1], 14 of them contain the factor
(q +1) with exponent 3 and the factor ( q2 +1) with exponent 2. Hence in F2[q,q −1],
no other diagonal entry can contain ( q + 1) with odd exponent. But in F2[q,q −1],
there is a diagonal entry containing ( q + 1) to the power 3 and another containing
it to the power 5 so, again, we have a contradiction.
We claim that G(4, 2, 1, 1) is not diagonalizable over Z(3)[q,q −1]. Assume it
to be diagonalizable. In Z(3)[q,q −1], 14 of the resulting diagonal entries contain
ELEMENTARY DIVISORS OF SPECHT MODULES 19
(q + 1) with exponent 1. This contradicts the fact that in F3[q,q −1], only 13 of
them contain (q + 1) with exponent 1.
Both claims independently imply that G(4, 2, 1, 1) is not diagonalizable over
Z[q,q −1].
We remark that the comparison of the elementary divisors over Q[q,q −1] and
over Z yields a contradiction to diagonalizability over Z(2)[q,q −1], too.
Finally, we give a (non-exhaustive) list of elementary divisors of some divisi-
bly diagonalizable Gram matrices for non-hooks, calculated using Gap 3 [12] and
Magma [9]. We omit the respective conjugate partition; compare (5.9).
n λ Elementary divisors of G(λ )
