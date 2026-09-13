---
doc_id: arxiv-2103.07383v1
doc_title: "On the Analyticity of Critical Points of the Generalized Integral Menger Curvature in the Hilbert Case"
section_id: sec-007-52-proof-of-theorem-12
section_title: "Proof of Theorem 1.2"
section_number: 5.2
pages: 20-23
source_pdf: 2103.07383v1.pdf
source_sha256: 9dca35ea16490ad8
doc_brief: "On the Analyticity of Critical Points of the Generalized Integral Menger Curvature in the Hilbert Case — We prove the analyticity of smooth critical points for generalized integral Menger cur- vature"
---
Now we are ready to proof the main statement of this paper by the method of majorants.
Proof of Theorem 1.2.Recall we have given a simple closed curve
γ= (γ1,...,γn)∈C∞(R/Z, Rn)
parametrized by arc-length which is a critical point of integral Menger curvatureintM(p,2) +λL,
subject to a ﬁxed length constraint, wherep∈( 7
3, 8
3) and λ∈R. We deﬁne
al :=‖γ(l)‖H
5
2
for all integersl≥0 by using the smoothness of the curveγ. Our aim is show that there exist
positive constantsCγand rγsuch that we have for any integerl≥0
al≤Cγ
l!
rlγ
;
from which the analyticity of the critical pointγon R/Z immediately follows by Proposition A.1.
20
First we establish a recursive estimate for the termsal. We begin with applying the criticality
of the curveγand Lemma 5.2 to obtain
al+3≤‖γ(l+3)‖H
5
2 +3p−7
≤CΦ
(
l + 1,n,r,K ;CΦ

1,n, r
2π,K ;‖γ‖H
5
2
,‖γ′‖H
5
2

+µ‖γ′‖H
5
2
,...,
CΦ

l + 2,n, r
2π,K ;‖γ‖H
5
2
,...,‖γ(l+2)‖H
5
2

+µ‖γ(l+2)‖H
5
2
{
+µ‖γ(l+2)‖H
5
2
=CΦ
(
l + 1,n,r,K ;CΦ

1,n, r
2π,K ;a0,a 1

+µa1,...,
CΦ

l + 2,n, r
2π,K ;a0,...,al+2

+µal+2
{
+µal+2.
(15)
for positive constantsC,C,r,µ, alll≥0 and someK∈N.
Next, we try to ﬁnd˜al that satisfy this recursive formula with equality and such that the
ﬁrst three coeﬃcients˜a0, ˜a1 and ˜a2 are greater than or equal toa0,a 1 and a2, respectively.
Deﬁne
G : R3n⊇B˜ε(0)→R3n,
Gi(z) := C
(
1 + 3na0−∑3n
k=1zk
r
2π
(−2
zK−2
i +µzi,
F : R3n⊇B˜ε(0)→R3n,
Fi(y) :=C
(
1 + 3nDG1((a0,...,a 0)⊺)(a1,...,a 1)⊺−∑3n
k=1yk
r
(−2
yK−2
i ,
for ˜ε:= min{3na0 + r
2π, 3nDG1((a0,...,a 0)⊺)(a1,...,a 1)⊺ +r}. These functions are clearly
analytic and by the Cauchy-Kovalevsky Theorem A.2, there is an analyticc : (−ε,ε)→R3n
satisfying 
}

c′′(t) =C·
(
F (DG(c(t))c′(t)) +µc′(t)
{
,
c(0) = (a0,...,a 0)⊺,
c′(0) = (a1,...,a 1)⊺,
(16)
where
C := max
{
1, a2
F1(DG((a0,...,a 0)⊺)(a1,...,a 1)⊺)
}
.
A little further along, we give a formula for all derivatives ofG(c(t)) which implies thatC is
well-deﬁned.
Since all entries of the right hand side in (16) are identical given the initial values, we have
that ci(t) =c1(t) for all validi and t. Setting ˜al :=c(l)
1 (0), we have by deﬁnition that
˜al≥al for l = 0, 1, 2. (17)
It remains to show the recursion.
21
An application of Leibniz’ rule and (20) yields
dl
dtlGi(c(t))
⏐⏐⏐⏐
t=0
=C
∑
j1+...+jK−1=l
( l
j1,...,jK−1
{
p(3n)
l
({(
1 +
3na0−∑3n
j=1cj(0)
r
2π/∏⟨hti⨂u⨂l⟨⟩t/∏⟨hti⨂own∏ight/∏⟨hti⨂ownl⟨⟩t/∏⟨hti⨂u⨂∏ight
=0
(−|α|−2
(|α|+ 1)!
(r
2π
{|α|+1
{
|α|≤j1
,
{
c(k)
j (0)
}
k=1,...,j1
j=1,...,3n
(
·
K−1
k=2
c(jk)
i (0) +µc(l)
i (0)
=CΦ
(
l,n, r
2π,K ;c1(0),...,c (l)
1 (0)
{
+µc(l)
1 (0) = CΦ
(
l,n, r
2π,K ; ˜a0,..., ˜al
{
+µ˜al.
(18)
Note that this corresponds to the innerΦ terms in (15).
Forl = 1this is a polynomial in˜a0, ˜a1 with positive coeﬃcients, so as long as both˜a0 =a0 and
˜a1 = a1 are positive, so is each component ofDG((a0,...,a 0)⊺)(a1,...,a 1)⊺ and consequently
F1 applied to that. Sinceγis not constant, neitherγnorγ′are 0∈H
5
2 (R/Z, Rn) and soa0 and
a1 have to be positive, makingC well-deﬁned.
Analogously to (18), taking advantage of the identity for all components inG,
˜al+3 =c(l+3)
1 (0) =C dl+1
dtl+1F1
( d
dtG(c(t))
{⏐⏐⏐⏐
t=0
+Cµc(l+2)
1 (0)
=CC
∑
j1+...+jK−1=l+1
( l + 1
j1,...,jK−1
{
p(3n)
l
({(
1 +
3nDG1(c(0)) ˙c(0)−∑3n
j=1
d
dtGj(c(t))
⏐⏐
t=0
r/∏⟨hti⨂u⨂l⟨⟩t/∏⟨hti⨂own∏ight/∏⟨hti⨂ownl⟨⟩t/∏⟨hti⨂u⨂∏ight
=0
(−|α|−2
(|α|+ 1)!
r|α|+1
{
|α|≤j1
,
{ dk+1
dtk+1Gj(c(t))
⏐⏐⏐⏐
t=0
}
k=1,...,j1
j=1,...,3n
(
·
K−1
k=2
djk+1
dtjk+1G1(c(t))
⏐⏐⏐⏐
t=0
+Cµ˜al+2
=CC Φ
(
l + 1,n,r,K ; d
dtG1(c(t))
⏐⏐⏐⏐
t=0
,..., dl+2
dtl+2G1(c(t))
⏐⏐⏐⏐
t=0
{
+Cµ˜al+2
≥CΦ
(
l + 1,n,r,K ; d
dtG1(c(t))
⏐⏐⏐⏐
t=0
,..., dl+2
dtl+2G1(c(t))
⏐⏐⏐⏐
t=0
{
+µ˜al+2,
hence we conclude together with (18) that
˜al+3≥CΦ
(
l + 1,n,r,K ;CΦ

1,n, r
2π,K ; ˜a0, ˜a1

+µ˜a1,...,
CΦ

l + 2,n, r
2π,K ; ˜a0,..., ˜al+2

+µ˜al+2
{
+µ˜al+2.
(19)
Using the fact thatΦ is nondecreasing inx0,...,xl (see (13)) , we obtain by comparing (15) and
(19) inductively with initial values (17), that
˜al≥al
22
for alll∈N0. By the analyticity ofc1 in zero and Proposition A.1, we have that there exist
positive constantsCγand rγsuch that
‖γ(l)‖H
5
2
=al≤˜al =c(l)
1 (0)≤Cγ
l!
rlγ
for alll∈N0 and thus,γis analytic.
Note that the method presented here ought to work with even smaller diﬀerences between the
orders of diﬀerentiability of the main and the remainder terms. If the regularity gain in one
step is 1
m we would expect an analogue of (15) to hold with roughlym layers of nestedΦ-terms
attainable via an analogue of Lemma 5.2. This approach would possibly lead to anm-th order
ODE in place of (16).
