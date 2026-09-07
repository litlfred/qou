---
doc_id: arxiv-0908.4305v3
doc_title: "Higher Dimensional Algebra VII: Groupoidification"
section_id: sec-007-52-an-explicit-formula
section_title: "An Explicit Formula"
section_number: 5.2
pages: 50-52
source_pdf: 0908.4305v3.pdf
source_sha256: ab8d2b335b026a36
doc_brief: "Higher Dimensional Algebra VII: Groupoidification — Groupoidiﬁcation is a form of categoriﬁcation in which vect or spaces are replaced by groupoids and linear operators are replaced by spans of"
---
Our calculations in the proof of Theorem 34 yield an explicit formula for the
operator coming from a tame span, and a criterion for when a span is tame:
Theorem 36. A span of groupoids
S
q
/d127/d127/d127/d127/d127/d127/d127/d127/d127 p
/d31/d31/d64/d64/d64/d64/d64/d64/d64
Y X
is tame if and only if:
1. For any object y ∈Y , the groupoid p−1(x)∩q−1(y) is nonempty for objects
x in only a ﬁnite number of isomorphism classes of X.
2. For every x ∈X and y ∈Y , the groupoid p−1(x) ∩q−1(y) is tame.
Here p−1(x) ∩q−1(y) is the subgroupoid of S whose objects lie in both p−1(x)
and q−1(y), and whose morphisms lie in both p−1(x) and q−1(y).
If S is tame, then for any ψ ∈ RX we have
(S
~
ψ)([y]) =
∑
[x]∈X
∑
[s]∈p−1(x) ⋂ q−1(y)
|Aut(x)|
|Aut(s)| ψ([x]).
50
Proof. First suppose the span S is tame and v : Ψ →X is a tame groupoid over
X. Equations 13 and 15 show that if S,X,Y, and Ψ are skeletal, and Ψ has just
one object ∗, then
SΨ
~
([y]) =
∑
s∈p−1(x)∩q−1(y)
|Aut(v(∗))|
|Aut(s)||Aut(∗)|
On the other hand,
Ψ
~
([x]) =



1
|Aut(∗)| ifv(∗) = x
0 otherwise.
So in this case, writing Ψ
~
as ψ, we have
(S
~
ψ)([y]) =
∑
[x]∈X
∑
[s]∈p−1(x) ⋂ q−1(y)
|Aut(x)|
|Aut(s)| ψ([x]).
Since both sides are linear in ψ, and every nonnegative function in RX is a
pointwise convergent nonnegative linear combination of functions o f the form
ψ = Ψ
~
with Ψ as above, the above equation in fact holds for all ψ ∈ RX .
Since all groupoids in sight are skeletal, we may equivalently write the a bove
equation as
(S
~
ψ)([y]) =
∑
[x]∈X
∑
[s]∈p−1(x) ⋂ q−1(y)
|Aut(x)|
|Aut(s)| ψ([x]).
The advantage of this formulation is that now both sides are unchan ged when
we replace X and Y by equivalent groupoids, and replace S by an equivalent
span. So, this equation holds for all tame spans, as was to be shown .
If the span S is tame, the sum above must converge for all functions ψ of
the form ψ = Ψ
~
. Any nonnegative function ψ : X → R is of this form. For the
sum above to converge for all nonnegativeψ, this sum:
∑
[s]∈p−1(x) ⋂ q−1(y)
|Aut(x)|
|Aut(s)|
must have the following two properties:
1. For any object y ∈Y , it is nonzero only for objects x in a ﬁnite number
of isomorphism classes of X.
2. For every x ∈X and y ∈Y , it converges to a ﬁnite number.
These conditions are equivalent to conditions 1) and 2) in the statem ent of the
theorem. We leave it as an exercise to check that these conditions a re not only
necessary but also suﬃcient for S to be tame.
51
The previous theorem has many nice consequences. For example:
Proposition 37. Suppose S and T are tame spans from a groupoid X to a
groupoidY . Then S +T
~
=S
~
+T
~
.
Proof. This follows from the explicit formula given in Theorem 36.
6 Properties of Degroupoidiﬁcation
In this section we prove all the remaining results stated in Section 2. We start
