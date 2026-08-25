---
doc_id: arxiv-2302.05903v2
doc_title: "On combinatorial generalization(s) of Borel transform: Averaging method in combinatorics of symmetric polynomials"
section_id: sec-010-relation-of-sum-formulas-to-ramanujan-sums
section_title: "Relation of sum formulas to Ramanujan sums"
section_number: null
pages: 11-12
source_pdf: 2302.05903v2.pdf
source_sha256: 9a17abd36cc8a317
doc_brief: "On combinatorial generalization(s) of Borel transform: Averaging method in combinatorics of symmetric polynomials — We elaborate on the recent suggestion to consider averaging of Cauchy identities"
---
Another amusing fact about the two nice cases (9) and (11) is their possible relation to the celebrated Ramanujan
sums [19]
cm,k :=
kX
(a,m)=1
e
2πiak
m (78)
where the sum goes over a, which are coprime with m, and it is always a positive integer. Counterparts of (9)
and (11), not literal, still surprisingly similar appear in two ways: with plethystic and ordinary exponentials.
Defining the plethystic exponential of a function f(x) as
P.E.

f(q)

:= exp
 ∞X
k=1
f(qk)
k
!
(79)
one obtains
P.E.
 q
1−q

=ξ0(q)
P.E.
 ∞X
k=1
c2,kqk
k
!
=eq2+q =
p
ξ1(2q)
P.E.
 ∞X
k=1
c1,kqk
k
!
=eq =ξ2(q) (80)
where
ξm(q) :=
X
R
q|R|dm
R (81)
is the quantity (6). In terms of ordinary exponentials, one gets
ξ0(q) = exp
 ∞X
k=1
qk
k(1−qk)
!
ξ1(q) = exp
 ∞X
k=1
c2,kqk
1−qk
!
=e2q2+q
ξ2(q) = exp
 ∞X
k=1
c1,kqk
1−qk
!
=eq (82)
In fact,
P.E.
 ∞X
k=1
c0,kqk
k
!
= exp
 q
1−q

exp
 ∞X
k=1
c0,kqk
1−qk
!
= exp
 q
(1−q)2

(83)
and
P.E.
 ∞X
k=1
cm,kqk
k
!
= exp

X
d|m
qd

, m> 0
exp
 ∞X
k=1
cm,kqk
1−qk
!
= exp

X
d|m
d·qd

, m> 0 (84)
are always expressed through the exponentiated finite sum over divisors of m. Thus, these are simple formulas,
which, unfortunately, have nothing to do with our ξm at m> 2.
11
