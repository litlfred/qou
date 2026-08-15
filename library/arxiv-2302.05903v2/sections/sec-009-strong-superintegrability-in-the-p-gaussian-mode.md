---
doc_id: arxiv-2302.05903v2
doc_title: "On combinatorial generalization(s) of Borel transform: Averaging method in combinatorics of symmetric polynomials"
section_id: sec-009-strong-superintegrability-in-the-p-gaussian-mode
section_title: "Strong superintegrability in the p-Gaussian model"
section_number: null
pages: 9-11
source_pdf: 2302.05903v2.pdf
source_sha256: 9a17abd36cc8a317
doc_brief: "On combinatorial generalization(s) of Borel transform: Averaging method in combinatorics of symmetric polynomials — We elaborate on the recent suggestion to consider averaging of Cauchy identities"
---
In the p-Gaussian model with the measure (13), which is under our consideration in this paper, there is a
formula for the bilinear correlator similar to (57), however, in this case, one has to deal with the operators 3
ˆW (0)
∆ . They are defined as
ˆW (0)
∆ = 1
z∆
:
l∆Y
i=1
Tr

Λ ∂
∂Λ
δi
: (60)
where Λ is a matrix such that thepk-variables are parameterized aspk = Tr Λk, and the invariant operators ˆW (0)
∆
can be rewritten as operators in pk-variables. The normal ordering here, : ... : means that all the derivatives
are placed to the rightmost positions.
Note that these operators ˆW (0)
∆ require the normal ordering, otherwise they would depend on the size of the
Λ matrix [14]. In the case of operators ˆW (−)
∆ in (57), normal ordering did not affect the answer. Note that the
Schur functions form a set of eigenfunctions of ˆW (0)
∆ :
ˆW (0)
∆ SR =ϕR(∆)SR (61)
where the eigenvalue ϕR(∆) is manifestly expressed through the symmetric group characters ψµ(∆) by [15–17]
ϕR(∆) =
X
µ⊢∆
SR/µ{δk,1}
SR{δk,1}
ψµ(∆)
z∆
(62)
Now using the identity
X
∆⊢P
ψP (∆)ϕR(∆) = SR/P{δk,1}
SR{δk,1} (63)
which follows from the orthogonality relation
X
∆
ψP (∆)ψR(∆)
z∆
=δPR (64)
one finally comes to the formula
D
SP{ ˆW (−)
k }· SR{pk}
EA
= SR/P{δk,1}
SR{δk,1} (65)
Now, using integration by parts, one could again recast the action of the SP ( ˆW (0)
k )-operators into the action
to the measure (13) in order to produce a complete set of polynomials KP{pk} of pk:
D
SP{ ˆW (−)
k }· SR{pk}
EA
=
Z
dµASP{ ˆW (−)
k }· SR{pk} =
Z
dµASP{
← −− −
W (0)}· SR{pk} =
Z
dµAKP{pk}· SR{pk} (66)
where we use the left arrow to denote the operator acting to the left. Thus, one could construct this way the
map SP{
← −− −
W (0)}−→ KP{pk}. However, there is a problem in doing this.
To see the problem, let us consider the simplest case of the operator ˆW (0)
[1] , which is manifestly given by
ˆW (0)
[1] =
∞X
a=1
apa
∂
∂pa
(67)
When integrating by parts, this operator acts to the measure (13) as
← −− −
W (0)
[1] =−
∞X
a=1
a ∂
∂pa
·pa =−
∞X
a=1
apa
∂
∂pa
−
∞X
a=1
a (68)
3The superscript “0” here refers to a commutative part of the w∞ algebra, while the superscript “-” in the previous subsection
to its Borel part.
9
The last sum requires some regularization P∞
a=1a−→σreg, and, when acting to the measure, this operator
produces a function, not a polynomial. Still, the Schur functions are eigenfunctions of this operator. If one acts
to the Gaussian measure (13) with this operator, one obtains
 
−
∞X
a=1
apa
∂
∂pa
−σreg
!
·
∞Y
k=1
dpk exp

−(p2k−1− 1)2
2(2k− 1) − p2
2k
4k

| {z }
dµ
=
 ∞X
k=1
(p2
k−p2k−1)−σreg
!
·dµ (69)
i.e.
K[1]{pk} =
∞X
k=1
(p2
k−p2k−1)−σreg (70)
At the second level, the formulas are even more involved. Indeed, consider the operator
← −− −
W (0)
[2] , which is given by
← −− −
W (0)
[2] =
∞X
a,b
abpa+b
∂2
∂pa∂pb
−
∞X
a,b
(a +b)papb
∂
∂pa+b
(71)
In this case, there are no infinite sums emerging from differentiating within the operator, however, in contrast
with the standard ˆW (0)
[2] -operator [14,18],
− −− →
W (0)
[2] =
∞X
a,b
abpa+b
∂2
∂pa∂pb
+
∞X
a,b
(a +b)papb
∂
∂pa+b
(72)
whose eigenfunctions are the Schur functions, the eigenfunctions of
← −− −
W (0)
[2] do not form a complete basis in the
space of graded polynomials of pk. For instance, at grading 3,
← −− −
W (0)
[2] SR =ARPSP (73)
where the matrix
ARP =


0 −4 2
4 0 −4
−2 4 0

 (74)
is degenerate: it has rank 2. Here we labelled the indices: [3] → 1, [21]→ 2, [111]→ 3.
The action of
← −− −
W (0)
[2] to the Gaussian measure (13) is now cubic in pk:


∞X
a,b
abpa+b
∂2
∂pa∂pb
−
∞X
a,b
(a +b)papb
∂
∂pa+b

dµ = (75)
=

4
∞X
k=1
p2
kp2k− 4
 ∞X
k=1
p2k−1
 ∞X
k=1
p2k

+ 2
∞X
a>b≥1
papbpa+b

·dµ (76)
i.e.
K[2] = 4
∞X
k=1
p2
kp2k− 4
 ∞X
k=1
p2k−1
 ∞X
k=1
p2k

+ 2
∞X
a>b≥1
papbpa+b (77)
This is a general rule: any KR is a polynomial of degree|R|+1 in pk, however, it involvespk with arbitrary large
index k, and also involves infinite sums, which require a regularization. All this requires a careful treatment,
which we postpone for a separate publication.
10
