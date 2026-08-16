---
doc_id: arxiv-1203.2182v1
doc_title: "Volume Conjecture: Reﬁned and Categoriﬁed"
section_id: sec-031-323-recursion-in-various-limits
section_title: "Recursion in various limits"
section_number: 3.2.3
pages: 36-38
source_pdf: 1203.2182v1.pdf
source_sha256: 2fe21af194f65227
doc_brief: "Volume Conjecture: Refined and Categorified — The generalized volume conjecture relates asymptotic behavior of the colored Jones polynomials to objects naturally deﬁned on an algebra ic curve, the"
---
In order to understand better the reﬁned recursion relation (3.129), let us consider what
happens in various special limits, when t = −1 or q = ±1. We begin with the unreﬁned limit
t = −1, which is special for several reasons. First, a direct subs titution
t = −1 in (3.129)
gives rise to the following 3-term homogeneous relation
α(t=−1)Jn−1 + β(t=−1)Jn + γ(t=−1)Jn+1 = 0 , (3.138)
– 35 –
with the coeﬃcients (rescaled by q2 −q1−n compared to (3.130)-(3.132))
α(t=−1) = q2n(qn −q)
q2n −q , (3.139)
β(t=−1) = q
(
1 +q−n −qn + q −qn
q2n −q − qn − 1
q2n+1 − 1
)
, (3.140)
γ(t=−1) = q −q−n
1 −q2n+1. (3.141)
This is precisely the homogeneous relation found in [5] by ha nd and obtained more system-
atically in the recent work [7, 19] by quantizing A(x,y ).
Moreover, in the t = −1 limit, there is also an inhomogeneous 2-term relation, whi ch
does not exist for other values of t. To derive this inhomogeneous relation we again start
from the ratios (3.116)-(3.118). The crucial point is that a t t = −1 the factors (1 −qk+1) in
the numerator and denominator cancel. As a result, equation s (3.117) and (3.118) take the
form
qn−1q−kJ(n,k ) = J(n,k ) −q−nJ(n,k + 1), (3.142)
q−kJ(n + 1,k + 1) = qn+2(1 −qn)J(n,k ), (3.143)
and factors q2k do not appear. 8 Moreover if we shift the indices n and k by one unit in the
second equation, we can explicitly solve for the factor q−kP (n,k ) to obtain a single relation
J(n,k + 1) = qnJ(n,k ) −q3n−1(1 −qn−1)J(n − 1,k − 1).
Performing the sum over k and using the deﬁnition (3.113), as well as taking care of the
boundary terms, we get
Jn =qn−1 1 −q2n−1
1 −qn −q3n−1 1 −qn−1
1 −qn Jn−1. (3.144)
This is the same 2-term inhomogeneous relation as presented in [5]. In fact, the homogeneous
relation (3.138) also follows from (3.144): if we normalize (3.144) so that the inhomogeneous
term is an n-independent constant, we get
const = δnJn +ǫnJn−1 = δn+1Jn+1 +ǫn+1Jn,
or, equivalently,
ǫnJn−1 + (δn −ǫn+1)Jn −δn+1Jn+1 = 0 .
It is not hard to check that this structure reproduces (3.138 ), with α(t=−1) ∼ ǫn, β(t=−1) ∼
(δn −ǫn+1), and γ(t=−1) ∼ −δn+1.
8Note that for general t it is not possible to solve for combinations qkP (n, k) directly, which is why we had
to sum over k ﬁrst using auxiliary Rn and Sn, to get 3-term homogeneous relation.
– 36 –
Other interesting limits of (3.129) arise when q takes special values. Thus, when q = 1
the coeﬃcients in (3.130)-(3.132) simplify and, up to an ove rall factor 1 +t3, take the form
α(q=1) = 0, β (q=1) = −(1 +t2 +t3), γ (q=1) = 1. (3.145)
Vanishing ofα(q=1) means that the recursion reduces to the 2-term form:
Pn+1 = (1 + t2 +t3)Pn. (3.146)
In fact, in the classical limit q = 1, even the full-ﬂedged superpolynomial (3.61), without t he
specialization to a =q2, enjoys a simple and elegant recursion relation, which for ( 2, 2p + 1)
torus knots looks like:
P Sn
(T 2,2p+1) = ap
[1 −t2p+2
1 −t2 +at3 1 −t2p
1 −t2
]
P Sn−1
(T 2,2p+1). (3.147)
In the limit q = −1 there are also simpliﬁcations. However, the recursion (3.1 29) still
involves 3 terms with
α(q=−1) =
(
1 + (−1)n)
t4, (3.148)
β(q=−1) = (1 +t3)
(
− 1 + (−1)nt2 +t3)
, (3.149)
γ(q=−1) = −1 + (−1)nt3. (3.150)
All these limits have a nice physical interpretation that fo llows from (3.29) and will be dis-
cussed elsewhere. Basically, setting the parameters q and t to special values means that in
the corresponding generating functions (3.31) – (3.33) one ignores the dependence on either
the spin F or the D0-brane charge P .
