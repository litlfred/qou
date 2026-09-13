---
doc_id: arxiv-2103.07383v1
doc_title: "On the Analyticity of Critical Points of the Generalized Integral Menger Curvature in the Hilbert Case"
section_id: sec-006-51-recursive-estimate-and-iteration
section_title: "Recursive estimate and iteration"
section_number: 5.1
pages: 18-20
source_pdf: 2103.07383v1.pdf
source_sha256: 9dca35ea16490ad8
---
In order to show analyticity of a curve, we need to bound its higher derivatives. One possible
approach is to bound derivatives by the lower order ones and iterate this procedure inductively.
In the following we show how such recursive estimates can be obtained from the Euler-Lagrange
equations.
18
Let γ∈C∞(R/Z, Rn) be a critical point ofintM(p,2) with respect to ﬁxed length andp∈
( 7
3, 8
3). By the Lagrange multiplier theorem (see e.g. [Lue98, §9.3 Theorem 1]), we have the
existence ofλ∈R such that
0 =δintM(p,2)(γ,h) +λδL(γ,h).
Seeing as by integration by parts and periodicity, we have
δL(γ,h) =

R/Z
⟨γ′(u),h′(u)⟩du =−

R/Z
⟨γ′′(u),h (u)⟩du
forγparametrized by arc-length. Combining the decomposition of the ﬁrst variation ofintM(p,2)
mentioned in (4) with theL2-forms of the main termQ(p) in Lemma 3.1 and the remainder term
R(p) in Lemma 4.2, we may write
0 =

R/Z
⟨
12
(⟨Q(p)(γ)(u) +⟨R(p)(γ)(u)
{
−λγ′′(u),h (u)
⟩
du.
Thus, we have
⟨Q(p)(γ) = λ
12γ′′−⟨R(p)(γ). (12)
From this, we may easily deduce the following.
Corollary 5.1. Letγ∈C∞(R/Z, Rn) be a critical point ofintM(p,2) with respect to ﬁxed length
and parametrized by arc-length. Form > 1
2 there exist constantsC = C(γ,m,n,p) > 0, r =
r(γ,m,n,p)> 0, andµ=µ(γ,n,p) such that
‖γ(l+3)‖H m+3p−7
≤C
∑
j1+...+jK−1=l+1
( l + 1
j1,...,jK−1
{
p(3n)
j1
({ (|α|+ 1)!
r|α|+1
}
|α|≤j1
,{‖γ(j+1)‖H m+ 3
2 p−3}j=1,...,j1
i=1,...,3n
(
·
K−1
i=2
‖γ(ji+1)‖H m+ 3
2 p−3 +µ‖γ(l+2)‖H m.
Proof. By Corollary 3.3, we may estimate‖γ(l+3)‖H m+3p−7≤⟨C‖∂l⟨Q(p)(γ)‖H m. Noting that ⟨C
only depends onp and n, we only have to combine this estimate with (12) and Lemma 4.5.
The obtained estimate is already recursive, however, the diﬀerence in the order of diﬀeren-
tiability is less than 1 since
3p−7< 3
2p−3
for anyp∈( 7
3, 8
3). This can lead to substantial problems in the iteration of the recursive estimate
to bound higher derivatives. Therefore, we iterate the recursive estimate beforehand to get a
diﬀerence of order at least 1 in the recursion.
To make the structure of the estimate more visible, set
Φ(l,n,r,K ;x0,...,xl) :=
∑
j1+...+jK−1=l
( l
j1,...,jK−1
{
p(3n)
j1
({ (|α|+ 1)!
r|α|+1
}
|α|≤j1
,{xj}j=1,...,j1
i=1,...,3n
(
·
K−1
i=2
xji
(13)
19
and note thatΦ is non-decreasing in thexi. The upper bound from Corollary 5.1 may be written
as
CΦ
(
l + 1,n,r,K ;‖γ′‖H m+ 3
2 p−3,...,‖γ(l+2)‖H m+ 3
2 p−3
{
+µ‖γ(l+2)‖H m. (14)
Lemma 5.2. Let γ∈C∞(R/Z, Rn) parametrized by arc-length be a critical point ofintM(p,2)
with respect to ﬁxed length andm≥5
2. Then, there exist constantsC = C >0, µ=µand r> 0
all depending onγ,m,nand p such that
‖γ(l+3)‖H m+3p−7
≤CΦ
(
l + 1,n,r,K ;CΦ

1,n, r
2π,K ;‖γ‖H m,‖γ′‖H m

+µ‖γ′‖H m,...,
CΦ

l + 2,n, r
2π,K ;‖γ‖H m,...,‖γ(l+2)‖H m

+µ‖γ(l+2)‖H m
{
+µ‖γ(l+2)‖H m.
Proof. Using Corollary 5.1 and (14), it suﬃces to bound‖γ(˜l+1)‖H m+ 3
2 p−3 for ˜l∈{0,...,l + 1}.
Sincem≥5
2, we obtainm+ 3
2p−5> 1
2 and may use Lemma C.1, Corollary 3.3 and Corollary 5.1
to estimate
‖γ(˜l+1)‖H m+ 3
2 p−3≤‖γ(˜l+3)‖H m+ 3
2 p−5
≤⟨C(p)CΦ
(
˜l + 1,n,r,K ;‖γ′‖H m−1,...,‖γ(˜l+2)‖H m−1
{
+µ‖γ(˜l+2)‖H m+2−3
2 p.
It holds thatm + 2−3
2p<m −3
2 <m−1 and by Lemma C.1,‖γ(j+1)‖H m−1≤2π‖γ(j)‖H m. A
look at the deﬁnition ofΦ together with Lemma B.2 enables us to estimate the above by
⟨C(p)C(2π)K−2Φ
(
˜l + 1,n, r
2π,K ;‖γ‖H m,...,‖γ(˜l+1)‖H m
{
+ ˜µ‖γ(˜l+1)‖H m
for ˜µ:= ˜µ(γ,m,n,p)> 0. Relabelingµ:= max{µ,˜µ}gives the desired statement.
