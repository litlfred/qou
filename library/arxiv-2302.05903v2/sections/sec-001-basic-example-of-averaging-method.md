---
doc_id: arxiv-2302.05903v2
doc_title: "On combinatorial generalization(s) of Borel transform: Averaging method in combinatorics of symmetric polynomials"
section_id: sec-001-basic-example-of-averaging-method
section_title: "Basic example of averaging method"
section_number: null
pages: 3-4
source_pdf: 2302.05903v2.pdf
source_sha256: 9a17abd36cc8a317
doc_brief: "On combinatorial generalization(s) of Borel transform: Averaging method in combinatorics of symmetric polynomials — We elaborate on the recent suggestion to consider averaging of Cauchy identities"
---
Eq.(3) counts Young diagrams, or the ordered integer partitions, while (4) is the Cauchy identity for the Schur
functions, i.e. for the characters of linear groups GLN. Technically, upon choosing pk = ¯pk = δk,1 in (4),
the difference between the two formulas is in the power of dR := SR{δk,1}: they are the sums of d0
R and d2
R,
accordingly. Generally,|R|!·dR = dimR are integer-valued dimensions of representations of the symmetric group
S|R| [10], and the sum
ξm :=
X
R
q|R|dm
R =
X
R
q|R| dimm
R
(|R|!)m (6)
looks somewhat terrible. The first terms in (6) are
ξm = 1 +q + 2
(2!)mq2 + 2m + 2
(3!)m q3 + 2· 3m + 2m + 2
(4!)m q4 + 6m + 2· 5m + 2· 4m + 2
(5!)m q5 +
+16m + 2· 10m + 2· 9m + 4· 5m + 2
(6!)m q6 + 2· 35m + 2· 21m + 20m + 2· 15m + 4· 14m + 2· 6m + 2
(7!)m q7 +
+90m + 2· 70m + 2· 64m + 2· 56m + 42m + 2· 35m + 2· 28m + 2· 21m + 2· 20m + 2· 14m + 2· 7m + 2
(8!)m q8+
+... (7)
The more surprising is that, at some particular values of m, one gets sensible formulas.
The best known is the quadratic case, m = 2, where the generic theory of finite groups implies that the sum
of the squared dimensions is always a dimension of the group. In the case of Sr, this gives
X
R⊢r
dim2
R =r! (8)
and leads to the particular case of (4)
ξ2 =
X
R
q|R|SR{δk,1}2 =
X
R
q|R|d2
R =eq (9)
For m = 0, one gets a far more transcendental, still comprehensible formula (3), which just counts the
numbers of representations ofS|R|.
Amusingly, the case of m = 1 is also simple:
Σn =
X
R⊢n
qndimR =n!
X
R⊢n
qndR (10)
gives rise to sequence A000085 from [9] which counts the numbers of Young tableaux of a given sizer, and this is
in perfect accordance with the fact that the dimension dimR is equal to the number of Youngtableaux associated
with the diagram R. For the exponential generating function of this sequence, see [9, sequence A000085 and
references therein],
ξ1 =
X
R
q|R|dR =
∞X
n=0
Σn
n! =eq+q2
2 (11)
Moreover, this sum can be lifted to a sum of single(!) Schur functions
X
R
q|R|SR{p} =
X
R
q|R|SR{p}⟨SR{¯p}⟩A
¯p| {z }
1
(4)
=
*
exp
 ∞X
k=1
qkpk ¯pk
k
!+A
¯p
= exp
(∞X
k=1

q2kp2
k
2k +q2k−1 p2k−1
2k− 1
)
(12)
In the language of [8], this follows from taking average of the Cauchy identity (4) over the variables ¯pk with the
measure
Measure A:
D
SR
EA
= 1 : dµA∼
∞Y
k=1
dpk exp

−(p2k−1− 1)2
2(2k− 1) − p2
2k
4k

(13)
3
Hereafter, the average with a given measure dµ over variablespk, k = 1, 2,... is defined as
D
f({pk})
E
:=
Z ∞
−∞
dµf({pk}) (14)
and normalized in such a way that
D
1
E
= 1.
Average (13) converts the Schur polynomials into 1,

 ¯SR{¯p}

A
= 1, and is Gaussian, so it is trivial to take
averages of the r.h.s. of (4),
*
exp
 ∞X
k=1
qkpk ¯pk
k
!+A
¯p
∼
∞Y
k=1
Z
e
q2k−1p2k−1 ¯p2k−1
2k−1 e−
(¯p2k−1−1)2
2(2k−1) d¯p2k−1
Z
e
q2kp2k ¯p2k
2k e−
¯p2
2k
4k d¯p2k

(15)
is just the r.h.s. of (12).
The sum (11) can be also represented as
X
R
q|R|dR =
X
R
qRSR{δk,1}⟨SR{¯pk}⟩A
¯p| {z }
1
(4)
=

eq¯p1

A
=
∞X
r=0
qr⟨¯pr
1⟩A
r! (16)
i.e.
r!·
X
R⊢r
dR =⟨pr
1⟩A (17)
Note that while (3) is a generating function for numbers of Young diagrams, (11) is an exponential (i.e.
weighted with additional factors 1
r!) generating function for numbers of Young tableaux.
Another important difference between counting diagrams and tables is that the latter, being related to
dimensions, admit a quantum deformation, see sec.3.3 below.
According to [9], no interpretations for ξm are yet known for m≥ 3.
