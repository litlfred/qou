---
doc_id: amc-2730
doc_title: "(Also available at http://amc-journal.eu) Braid representatives minimizing the number of simple walks* Hans U. Boden † , Matthew Shimoda ‡"
section_id: sec-002-the-colored-jones-polynomial-in-closed-form
section_title: "The colored Jones polynomial in closed form"
section_number: null
pages: 6-10
source_pdf: amc_2730.pdf
source_sha256: 65730074a2925c6e
doc_brief: "(Also available at http://amc-journal.eu) Braid representatives minimizing the number of simple walks* Hans U. Boden † , Matthew Shimoda ‡ — Given a knot, we develop methods for finding a braid"
---
In this section, we apply Theorem 2.2 and Lemma 2.3 to compute JN,Kpqq, the colored
Jones polynomial, for the knots 52, 61 and 72. This is achieved by choosing favorable braid
representatives, namely those with only a few simple walks.
In [22], Masbaum uses skein theory to compute the colored Jones polynomial for all
twist knots, a class which includes 52, 61, and 72. More general calculations of the colored
Jones polynomial for the double twist knots can be found in [20, 21].
 
 
Figure 1: The simple walks A and B shown as arcs with zebra stripes for the braid
σ´1
2 σ1σ3
2σ1 with closure the knot 52.
Example 3.1. The braid wordσ´1
2 σ1σ3
2σ1 represents the knot 52 and has two simple walks
with J Ď t2, 3u. They are A “ qa1,´c3,`a4,`b5,` and B “ q3b1,´c1,´c2,`c3,`a4,`
b5,`b6,` (see Figure 1). Notice thatA hasJ“t 3u andB hasJ“t 2, 3u. Since the walks
A andB both traverse the third strand at top and bottom, stacks only need to be considered
up to levelN´ 1.
Using Theorem 2.2, we can write the colored Jones polynomial as the following:
H. U. Boden and M. Shimoda: Braid representatives minimizing the number of simple walks 7
JN,Kpqq“ qp1´Nq
N´1ÿ
n“0
ENppA`Bqnq,
“ qp1´Nq
N´1ÿ
n“0
ENppqa1,´c3,`a4,`b5,``q3b1,´c1,´c2,`c3,`a4,`b5,`b6,`qnq.
We will expand the above expression using the q-binomial theorem. For that purpose,
we introduce the Gaussian binomial coefficients (or q-binomial coefficients), which are
defined by ˆn
k
˙
q
“
k´1ź
i“0
ˆ 1´qn´i
1´qi`1
˙
.
The expansion of the above expression includes a sum of products of A’s andB’s, which
can be interpreted as stacks.
To apply Lemma 2.3, the weights at each crossing must be placed into the orderbscrad,
and it is preferable to expandpA`Bqn as a sum of terms of the formBkAn´k. Since the lo-
cal weights at different crossings commute, the only potential issue with non-commutativity
ofA andB is at the first crossing. Since a1,´b1,´c1,´ “ qb1,´c1,´a1,´, we have AB “
qBA, so we can adjust for inversions using theq-binomial coefficient:
pA`Bqn“
nÿ
k“0
ˆn
k
˙
q
BkAn´k.
Next we use Lemma 2.3 to apply ENp¨q to evaluate each stack. First, these walks
have weights bi,` indexed alone at the fifth and sixth crossings, which evaluates to 1.
Additionally, the ci,˘ weights at the first and second crossings in walk B always cancel
out sinceENpc1,´q“ q´pN´1q andENpc2,`q“ qN´1. We still havec3,` in each walkA
and walk B. Therefore, for each walk in a stack, the term A orB, qN´1 is contributed.
Similarly, the weight a4,` appears in both walks, so a stack consisting of n walks will
contribute śn
i“1p1´qN´iq. Meanwhile, the weight a1,´ is only in walk A, so the stack
BkAn´k will contribute śn´k
i“1p1´qn`i´Nq. Additionally, we need to adjust for the
correct order of b1,´ andc1,´ in the weights in products containing Bk. The number of
times the relation is applied increases quadratically with the exponent of B. That is, for a
weight containing Bk, its contribution is qk2´k. Finally, the remaining powers of q arise
from the existing variables in the simple walks.
Applying Theorem 2.2, the colored Jones polynomial of 52 can be written in closed
form as
JN,Kpqq“ qN´1
N´1ÿ
n“0
nÿ
k“0
ˆn
k
˙
q
qnN`kpk`1q
nź
i“1
`
1´qN´i˘n´kź
i“1
`
1´qn`i´N˘
.
Example 3.2. The braid word σ1σ2σ1´1σ3´1σ2σ3´1σ1 represents the knot 61 and has
three simple walks withJĎt 2, 3, 4u. They areA“qa4,´a6,´,B“q3c2,`a3,´a4,´b5,`
b6,´c6,´ andC“q5c1,`c2,`b3,´c3,´a4,´b5,`b6,´c6,´b7,` (see Figure 2). Notice that A
hasJ “t 4u,B hasJ “t 3, 4u, andC hasJ “t 2, 3, 4u. Since the walks A,B andC all
traverse the fourth strand at top and bottom, stacks only need to be considered up to level
N´ 1.
8 Ars Math. Contemp. 23 (2023) #P1.10
 
 
 
Figure 2: The simple walks A,B and C shown as arcs with zebra stripes for the braid
σ1σ2σ1
´1σ3
´1σ2σ3
´1σ1 with closure the knot 61.
Using Theorem 2.2, the colored Jones polynomial for 61 can be written as
JN,Kpqq“ qp1´Nq
N´1ÿ
n“0
ENppA`B`Cqnq,
“qp1´Nq
N´1ÿ
n“0
EN
`
pqa4,´a6,´`q3c2,`a3,´a4,´b5,`b6,´c6,´
`q5c1,`c2,`b3,´c3,´a4,´b5,`b6,´c6,´b7,`qn˘
.
We use theq-multinomial theorem to expand the termspA`B`Cqn, and to that end
we recall the definition of theq-multinomial coefficients.
 
 
 
Figure 3: The simple walks A,B and C as arcs with zebra stripes on the braid
σ1σ2σ3
3σ´1
1 σ2σ1σ´1
3 with closure the knot 72.
H. U. Boden and M. Shimoda: Braid representatives minimizing the number of simple walks 9
Given an integer r ě 1 and sequence of nonnegative integers m1,m 2,...,m r such
thatn“m1`¨¨¨` mr, let
ˆ n
m1,m 2,...,m r
˙
q
“ rnsq!
rm1sq!rm2sq!... rmrsq!, (2)
wherernsq “ qn´1`¨¨¨` q` 1 andrnsq!“ r1sq¨¨¨r nsq. The term
` n
m1,m2,...,mr
˘
q is
called the Gaussian multinomial coefficient orq-multinomial coefficient.
With the weights indexed at the third and sixth crossings, the natural order of the walks
isC,B,A , as this will allow use of Lemma 2.3 with only a few other adjustments. The use
of theq-multinomial coefficient is suitable for this order because inversions with respect to
the alphabet C,B,A are reversed with multiplication by q. That is, AB “ qBA,AC “
qCA andBC “qCB . The expansion of the trinomial takes the form
pA`B`Cqn“
nÿ
m“0
mÿ
k“0
ˆ n
n´m,m ´k,k
˙
q
Cn´mBm´kAk, (3)
where
` n
n´m,m´k,k
˘
q denotes theq-trinomial coefficient of Equation (2).
We can now expand the trinomial for any powern and use Lemma 2.3 to applyENp¨q
and evaluate each stack. Theb˘ andc˘ weights are evaluated the same as in Example 3.1.
The weight a4,´ appears in each of A,B,C , so for every term Cn´mBm´kAk, it will
contribute śn
i“1p1´qi´Nq. Meanwhile, the weight a3,´ only appears in the walk B,
so for the term Cn´mBm´kAk, it contributes śm´k
i“1 p1´qn´m`i´Nq. Similarly, the
weight a6,´ only appears in the walk A, so for the term Cn´mBm´kAk, it contributesśm´k
i“1 p1´qn´k`i´Nq.
Finally, we need to adjust for the correct order of the termsb6,´ andc6,´ in the products
containingCn´mBm´k. The number of times the relation is applied increases quadrati-
cally with the sum of the exponents ofB andC, which ispn´mq`pm´kq“ n´k. That
is, for the termCn´mBm´kAk, applying the relation introduces a factor ofqpn´kq2´pn´kq.
We follow the same logic for products Cn´m to adjust for the order of the weights b3,´
andc3,´ at the third crossing.
Applying Theorem 2.2, the colored Jones polynomial of 61 can be written in closed
form as
JK,Npqq“ q1´N
N´1ÿ
n“0
nÿ
m“0
mÿ
k“0
ˆ n
n´m,m ´k,k
˙
q
q3n´k´m`pn´kq2`pn´mq2
ˆ
nź
i“1
p1´qi´Nq
m´kź
i“1
p1´qn´m`i´Nq
kź
i“1
p1´qn´k`i´Nq.
Example 3.3. The braid word σ1σ2σ3
3σ´1
1 σ2σ1σ´1
3 represents the knot 72 and has three
simple walks with J Ď t2, 3, 4u. They are A “ qc3,`a4,`b5,`a9,´, which has has
J “ t4u; B “ q3c2,`c3,´a4,`b5,`a6,´b7,`b9,´c9,´, which has has J “ t3, 4u; and
C “ q5c2,`c3,`a4,`b5,`b6,´c6,´b7,`b8,´b9,´c9,´, which has J “ t2, 3, 4u (see Fig-
ure 3). Since the walks A,B andC all traverse the fourth strand at top and bottom, stacks
only need to be considered up toN´ 1.
10 Ars Math. Contemp. 23 (2023) #P1.10
We use Theorem 2.2 to write the colored Jones polynomial for 72 as:
JN,Kpqq“ qp1´Nq
N´1ÿ
n“0
ENppA`B`Cqnq,
“qp1´Nq
N´1ÿ
n“0
EN
`
pqc3,`a4,`b5,`a9,´`q3c2,`c3,´a4,`b5,`a6,´b7,`b9,´c9,´
`q5c2,`c3,`a4,`b5,`b6,´c6,´b7,`b8,´b9,´c9,´qn˘
.
With the weights indexed at the sixth and ninth crossings, the most natural order of the
walks is C,B,A . Note that AB “ qBA,AC “ qCA andBC “ qCB . Therefore, the
expansion of the trinomial is as given in equation (3) above.
We expand the trinomial for all powers of n and use Lemma 2.3 to apply ENp¨q and
evaluate each stack. The b˘ and c˘ weights are evaluated the same as in Examples 3.1
and 3.2. The weight a4,` appears in each of A,B,C , so for every term Cn´mBm´kAk,
it will contribute śn
i“1p1´qN´iq. Meanwhile, the weight a6,´ only appears in the walk
B, so for the term Cn´mBm´kAk, it contributes śm´k
i“1 p1´qn´m`i´Nq. Similarly, the
weight a9,´ only appears in the walk A, so for the term Cn´mBm´kAk, it contributesśk
i“1p1´qn´k`i´Nq.
Finally, we need to adjust for the correct order of the termsb9,´ andc9,´ in the products
containingCn´mBm´k. The number of times the relation is applied increases quadrati-
cally withpn´mq`p m´kq“ n´k. That is, for the term Cn´mBm´kAk, applying
the relation introduces a factor of qpn´kq2´pn´kq. We follow the same logic for products
Cn´m to adjust for the weights at the sixth crossing.
Applying Theorem 2.2, the colored Jones polynomial of 72 can be written in closed
form as
JK,Npqq“ qN´1
N´1ÿ
n“0
nÿ
m“0
mÿ
k“0
ˆ n
n´m,m ´k,k
˙
q
qnN`2n´m´k`pn´kq2`pn´mq2
ˆ
nź
i“1
p1´qN´iq
m´kź
i“1
p1´qn´m`i´Nq
kź
i“1
p1´qn´k`i´Nq.
For hyperbolic knots, the V olume Conjecture asserts that
lim
NÑ8
log|JN,Kpe2πi{Nq|
N “ V olpS3 ∖Kq
2π .
For more information about this important open problem, see the book [24]. The knots in
Examples 3.1, 3.2, and 3.3 are all hyperbolic, and the V olume Conjecture has been verified
for each of them. For 52, this was proved by Ohtsuki [25]; for61, it was proved by Ohtsuki
and Yokota [27]; and for72, it follows from Ohtsuki’s work on7-crossing hyperbolic knots
[26]. It would be interesting to use the formulas given here to independently verify the
V olume Conjecture for these knots.
