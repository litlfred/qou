---
doc_id: arxiv-math-0606435v2
doc_title: "PROPERTIES OF CLOSED 3-BRAIDS"
section_id: sec-059-751-conditions-on-the-eigenvalues
section_title: "Conditions on the eigenvalues"
section_number: 7.5.1
pages: 53-55
source_pdf: 0606435v2 (1).pdf
source_sha256: 6dddaf838a19f0f5
doc_brief: "PROPERTIES OF CLOSED 3-BRAIDS — We show that 3-braid links with given (non-zero) Alexander o r Jones polynomial are ﬁnitely many, and can be effectively determined."
---
Using just norms clearly weakens the conditions considerably, and so one would like to identify the Burau eigenvalues
directly. However, the relations between theXi do not allow to recover by simple algebraic means the individual traces
from P.
Using Squier’s unitarity, there is an analytic way to recover the Burau trace of 4-braids (at least for generic t and up
to ﬁnite indeterminacy). Since by the previous remarks the u se of P is not essential, we will describe the procedure
given ∆, V and e. This gives the most signiﬁcant practical enhancement to the above 4-braid tests.
In the following we ﬁx a 4-braid β of exponent sum e, whose closure link has Jones polynomial V and Alexander
polynomial ∆. We let t be a unit norm complex number with non-negative real part.
54 7 Applications of the representation theory
We use that
tr ψ 3 ∧ ψ 3 = (−t)e/ 2tr ψ 3(−t)−e/ 2 .
Then we have
∆(t) = 1 − t
1 − t4
(
− 1√t
) e−3
·
[
1 − tr ψ 3 + (−t)e/ 2tr ψ 3(−t)−e/ 2 − (−t)e
]
.
So, with i = √−1,
δ := − 1
2i (−t)−e/ 2
[
∆(t)1 − t4
1 − t
(
− 1√t
) 3−e
− 1 + (−t)e
]
is a real number. Now when λ1,2,3 are the eigenvalues of ψ 3(β), we have
A = λ1 + λ2 + λ3 = ( −t)e/ 2(y + iδ)
B = λ1λ2 + λ1λ3 + λ2λ3 = ( −t)e/ 2(y − iδ)
C = λ1λ2λ3 = ( −t)e .
Here y is a real number we do not know, and we try to determine. Since |λk| = 1, we have as before |A| ≤ 3 and
|B| ≤ 3. So the range for y is [−y0,y0] with y0 =
√
9 − δ2. (If |δ| > 3 we are done as before.) Then
tr ψ 3 ∈ [(−t)e/ 2(−y0 + iδ), (−t)e/ 2(y0 + iδ)] ,
with the interval understood lying in C. Let ψ − and ψ + be the endpoints of this interval.
Now one can restrict the interval [−y0,y0] for y using the Jones polynomial as follows.
Let ρ := (−t)−e/ 2tr ¯ψ 2 ∈ [−2,2]. The restriction to the given range follows because J[3] (see the proof of proposition
7.1) is also deﬁnite when J[4] is. From (56) we have
tr ψ 3 = 1 − t2
t(1 − t3)
[
V (t)
(
− 1√t
) e−3
− 1 − t5
1 − t2 − t2
1 + t (−t)e/ 2 · ρ
]
=: ˜ψ(ρ) ,
so
˜ψ(ρ) = 1 − t2
t(1 − t3)
[
V (t)
( −1√t
) e−3
− 1 − t5
1 − t2
]
− ρ
1 + 2ℜ t (−t)e/ 2 .
(Just for the purpose of deﬁning ˜ψ, we should regard here ρ as a formal parameter, rather than as a concrete value.)
Let ˜ψ(±2) =: ˜ψ ±. Since 1 + 2ℜ t > 0, we have ℜ ((−t)−e/ 2 ˜ψ +) > ℜ ((−t)−e/ 2 ˜ψ −).
Then [ ˜ψ −, ˜ψ +] ⊂ C is an interval of the same slope as [ψ −,ψ +], so we check if they overlap.
Let
˜y± = (−t)−e/ 2 ˜ψ ± − iδ.
Then for a consistent restriction on tr ψ 3 the following holds:
1. ˜y± are real
2. ˜y+ ˜y− ≤ 0 or min( ˜y2
± + δ2) ≤ 9.
Potentially these conditions may be violated, but in practi ce they seem always to hold. (We have not elaborated on
why this is so, though it may be worth understanding.) Then at least, we consider
y ∈ [−y0,y0] ∩ [ ˜y−, ˜y+] .(60)
We have now the cubic
x3 + ax2 + bx + c := x3 − Ax2 + Bx −C = 0 .
