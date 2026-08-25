---
doc_id: arxiv-math-0508100v6
doc_title: "ASYMPTOTICS OF THE COLORED JONES FUNCTION OF A KNOT"
section_id: sec-010-32-the-cyclotomic-expansion
section_title: "The cyclotomic expansion"
section_number: 3.2
pages: 9-10
source_pdf: 0508100v6.pdf
source_sha256: 9cc100a86b40c336
doc_brief: "ASYMPTOTICS OF THE COLORED JONES FUNCTION OF A KNOT — To a knot in 3-space, one can associate a sequence of Laurent p olynomials, whose nth term is the nth colored Jones polynomial."
---
tion, known as the cyclotomic expansion. Although the cyclotomic ex pansion has important arithmetic
consequences, we discuss only its algebraic properties here. Let u s deﬁne:
(11) Cn,k (q) =
k∏
j=1
(qn + q−n − qj − q−j), with Cn, 0(q) := 1 .
Habiro showed that there exist unique Laurent polynomials HK,k (q) ∈ Z[q±1], k = 0, 1, . . . such that
(12) JK,n (q) =
n−1∑
k=0
Cn,k (q) HK,k (q).
For details, see [
Hab08, Section 6]. Note that our HK,n (q) is JK(P ′′
n ) in Habiro’s notation. We will call
the expansion ( 12) the cyclotomic expansion. Since Cn,k (q) = 0 if k ≥ n, the summation in ( 12) can be
assumed from 0 to ∞.
It is possible to solve for HK,n from Equation ( 12). Explicitly, from [ Hab08, Lemma 6.1] one has
(13) HK,n (q) = 1
{2n + 2}!
n+1∑
k=1
(−1)n+1−k{2k}{k}
[ 2n + 2
n + 1 − k
]
JK,k (q)
where we use the following deﬁnition
{n} := qn/ 2 − q−n/ 2 and {n}! :=
n∏
i=1
{i},
10 STA VROS GAROUF ALIDIS AND THANG TQ L ˆE
{a}b := {a}!
{a − b}! =
a∏
j=a−b+1
{j},
[
a
b
]
:= {a}!
{b}!{a − b}!
