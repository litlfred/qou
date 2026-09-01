---
doc_id: ising
doc_title: "WEIGHTED DEPENDENCY GRAPHS AND THE ISING MODEL"
section_id: sec-017-22-jehanne-dousse-and-valentin-f-eray
section_title: "JEHANNE DOUSSE AND VALENTIN F ´ERAY"
section_number: 22
pages: 22-23
source_pdf: ising.pdf
source_sha256: 9f84d7209731d299
doc_brief: "WEIGHTED DEPENDENCY GRAPHS AND THE ISING MODEL — Weighted dependency graphs have been recently introduced by the second author, as a toolbox to prove central limit theorems."
---
Condition (3) is fulﬁlled since, using (1.2) and the above inequality for ∆ n,
(Nn
∆n
) 1
s ∆n
an
≤
( |Λn|m
m2|Λn|m−1C
) 1
s m2|Λn|m−1C√
A|Λn|2m−2+η≤C′|Λn|1/s−η/2
for some constantC′, and, for s large enough, the right-hand side tends to 0 as n tends to inﬁnity. □
We now show a simple suﬃcient condition – the pattern consisting of positive spins only – so that
the bound (1.2) on the variance is satisﬁed. We start with a lemma.
Lemma 4.9. Fix m≥ 2. There exist some constants R> 0 and B >0 such that the following holds.
For any lists (x(1),...,x (m)) and (y(1),...,y (m)) such that x(1) =y(1) but no two elements in the set
{x(1),...,x (m),y (2),...,y (m)} are at distance less than R from each other, we have
Cov
( m∏
i=1
X(x(i),+),
m∏
i=1
X(x(i),+)
)
≥B.
Proof: By deﬁnition, and using that X(x(1),+)X(y(1),+) =X2
(x(1),+) =X(x(1),+), we have
Cov
( m∏
i=1
X(x(i),+),
m∏
i=1
X(x(i),+)
)
= E
[
X(x(1),+)··· X(x(m),+)X(y(2),+)··· X(y(m),+)
]
− E
[
X(x(1),+)··· X(x(m),+)
]
E
[
X(x(1),+)X(y(2),+)··· X(y(m),+)
]
.
Using the expression of joint moments in terms of cumulants – see, e.g. [10, Eq. (3)] – and the bound
for cumulants of spins (Theorem 1.1), we have that there exists a constant Cm such that
⏐⏐E
[
X(x(1),+)··· X(x(m),+)
]
− E
[
X(x(1),+)]··· E
[
X(x(m),+)
]⏐⏐≤CmεR,
whenever the x(i) all lie at distance at least R from each other. The same holds for the other joint
moments in the above expression for the covariance and we get
Cov
( m∏
i=1
X(x(i),+),
m∏
i=1
X(x(i),+)
)
=
(
E
[
X(x(1),+)
]
− E
[
X(x(1),+)
]2)
· E
[
X(x(2),+)]··· E
[
X(x(m),+)
]
E
[
X(y(2),+)]··· E
[
X(y(m),+)
]
+ error,
where the error is uniformly bounded by CmεR. The main term in the above equation is positive (as a
product of positive terms) and independent from thex(i) and they(i) (by translation invariance), while
the error can be made as small as wanted by making R tend to inﬁnity. This proves the lemma. □
Proposition 4.10. Let ˜P be a global pattern of size m and assume that the function s deﬁning ˜P
takes only value +1. Then there exists a constant A such that Var(Sn, ˜P)≥A|Λn|2m−1.
Proof: We expand the variance as
Var(Sn, ˜P) =
∑
{x(1),...,x(m)}⊂Λn
{y(1),...,y(m)}⊂Λn
Cov
(
Z
˜P
{x(1),...,x(m)},Z
˜P
{y(1),...,y(m)}
)
.
When ˜P involves only positive spins, the FKG inequalities ensure that all summands are positive. Re-
stricting the sum to sets with an ordering that fulﬁls the hypothesis of Lemma 4.9 gives a lower bound.
Therefore Var(Sn, ˜P)≥B·N1, whereN1 is the number of pairs of sets ({x(1),...,x (m)},{y(1),...,y (m)})
as in Lemma 4.9. For ﬁxed R> 0, this number is clearly of order |Λn|2m−1, ﬁnishing the proof of the
proposition. □
WEIGHTED DEPENDENCY GRAPHS AND THE ISING MODEL 23
