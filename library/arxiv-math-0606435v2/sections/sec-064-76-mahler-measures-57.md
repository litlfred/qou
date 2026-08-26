---
doc_id: arxiv-math-0606435v2
doc_title: "PROPERTIES OF CLOSED 3-BRAIDS"
section_id: sec-064-76-mahler-measures-57
section_title: "Mahler measures 57"
section_number: 7.6
pages: 57-58
source_pdf: 0606435v2 (1).pdf
source_sha256: 6dddaf838a19f0f5
doc_brief: "PROPERTIES OF CLOSED 3-BRAIDS — We show that 3-braid links with given (non-zero) Alexander o r Jones polynomial are ﬁnitely many, and can be effectively determined."
---
We consider the links Ln given by the closed 3-braids (σ1σ−1
2 )n. Using the Burau matrix eigenvalues, we ﬁnd
Vn := V (Ln) = t + 1
t + en
−(t) +en
+(t) ,
where
e±(t) = −t + 1/ t − 1
2 ±
√ ( t + 1/ t − 1
2
) 2
− 1 .
Similarly
∆n := ∆(Ln) = 1
t + 1/ t + 1
(
2 − en
−(t) − en
+(t)
)
.
Now the Jensen integral gives
log M(Vn) =
Z 1
0
log |Vn(e2πis)|ds .(65)
Since Vn is reciprocal, it sufﬁces to consider the integral over s ∈ [0,1/ 2]. Herein, with t = e2πis, for s ∈ (1/ 3,1/ 2],
we have real e±(t), one with norm > 1. So
Z 1/ 2
1/ 3
log |Vn(e2πis)|ds ≥ O(n) .
We must argue about s ∈ [0,1/ 3]. In that case, e±(t) are conjugate complex numbers of unit norm. This implies tha t
the integrand is bounded above when n → ∞, but our problem is to show that it does not decrease too quick ly with n.
The assignment (with i = √−1)
t ↦− →f (t) = −t + 1/ t − 1
2 + i
√
1 −
( t + 1/ t − 1
2
) 2
maps e2πi[0,1/ 3] → e2πi[1/ 6,1/ 2], so
1
2π argt
g
↦− →1
2π arg f (t)
is a map g : [0,1/ 3] → [1/ 6,1/ 2], which is bijective and monotonous, and C1 except in t = 1/ 3 where g′ → ∞. In
particular,
g′
min = min {g′(s) : s ∈ [0,1/ 3] } > 0 .
Now consider the functions
h(s) := 2cos2 πng(s) and m(s) := −2cos2 πs
for s ∈ [0,1/ 3]. The singularities of the Jensen integral (65) correspond to the intersections of the graphs of h and m.
If n ≫ g′
min, then all intersection points 1 si of the graphs of h and m have |m′(si)| > |h′(si)|. (Here we use also that
m ⁄= h when s = 0.) In particular, between two critical points xi of h, it intersects m at most once. So the number n′ of
intersections si satisﬁes ⏐⏐⏐⏐n′ − 2
3 n
⏐⏐⏐⏐ ≤ O(1) , and therefore n′ = O(n) .
Moreover,
|m′(si)| − |h′(si)| ≥ (2 − |m(si)|) ·C ,(66)
for a constant C independent on i and n. Now when n increases, the si will concentrate around s = 1
3, but since
g′
min > 0, for s small, the xi will be at distance ≥ O( 1
n ). So
2 − |m(xi)| ≥ C · i2
n2(67)
1For the rest of the proof i is used as an index rather than the complex unit.
58 7 Applications of the representation theory
for a constant C independent on i and n. Then if s1, . . . ,sn′ are the n′ intersection points of h and m, we can estimate
for values of s between the critical points xi and xi+1 of h
|m(s) − h(s)| ≥ C ·
(
2 − |m(si)|
)
· |s − si|2(68)
for a number C independent on i and s. Inequality (68) follows because we can control the behaviour of |m(s) − h(s)|
from (66) for s around si, and though |m − h| decreases slightly around the endpoints of the interval [xi,xi+1], this
decrease can be controlled by (67). So
Z xi+1
xi
log |m(s) − h(s) |ds ≥ (xi+1 − xi)
(
log
(
2 − |m(si)|
)
+ logC
)
+ 2
Z xi+1
xi
log |s − si|ds .(69)
Since for small i (when 2 − |m(si)| is small), the xi will be at distance ≥ O( 1
n ), using (67) and m(s) ≤ 1 when
0 ≤ s ≤ 1/3 we have
n′
∑
i=1
⏐⏐⏐log
(
2 − |m(si)|
) ⏐⏐⏐ ≤ n′ ·
(
C ·
⏐⏐⏐⏐
Z 1
0
log |x|dx
⏐⏐⏐⏐ +C′
)
= O(n) .(70)
Let di := xi+1 − xi. Because of g′
min > 0, we have
max
i
di ≤ O(1/ n) .(71)
So, similarly as in (70)
n′
∑
i=1
⏐⏐⏐di log
(
2 − |m(si)|
) ⏐⏐⏐ ≤ O(1) .(72)
Also, because of (71) and
R
1 + logx dx = x · logx +C, for n large
⏐⏐⏐⏐
Z xi+1
xi
(
1 + log|s − si|
)
ds
⏐⏐⏐⏐ ≤ −C · di ·
[
logdi + C′ ]
≤
√
di ≤ O
( 1√n
)
for some real number C′ independent on i and n, and so
n′
∑
i=1
⏐⏐⏐⏐
Z xi+1
xi
2 · log|s − si|ds
⏐⏐⏐⏐ ≤ O(√n) .
This, (72) and (69) imply that for s ∈ [0,1/ 3] the (part of the) Jensen integral (65) has a lower bound that behaves like
−O(√n), so the dominating part is for s ∈ [1/ 3,1/ 2], and we are done for V.
For ∆ the argument is similar. There m(s) ≡ 2, so instead of (68) we have fors ∈ [xi,xi+1] the estimate |m(s) − h(s)| ≥
|s − si|2 ·C · g′
min, with the same further reasoning. ✷
Remark 7.7 Dan Silver pointed out that for the Alexander polynomial a pr oof can be obtained (possibly more ele-
gantly, but not immediately) from the ideas in [SW].
