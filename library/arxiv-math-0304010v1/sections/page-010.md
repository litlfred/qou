---
doc_id: arxiv-math-0304010v1
doc_title: "Kerov's central limit theorem for the Plancherel measure on Young diagrams"
section_id: page-010
section_title: "Page 10"
section_number: null
pages: 10-10
source_pdf: 0304010v1.pdf
source_sha256: fc2296c027b3feb0
toc_source: undetermined
doc_brief: "Kerov's central limit theorem for the Plancherel measure on Young diagrams — Consider random Young diagrams with ﬁxed number n of boxes, dis- tributed according to the Plancherel measure Mn."
---
Deﬁne the functions ep1, ep2, . . . on D by setting
epk[ω] = −k
Z ∞
−∞
xk−1σ′(x)dx
(2.2)
=
Z ∞
−∞
xkσ′′(x)dx,
(2.3)
where ω ∈D, k = 1, 2, . . ..
Proposition 2.2. If ω ∈D0 then ep1[ω] = 0 and
epk[ω] = k(k −1)
Z ∞
−∞
xk−2σ(x)dx,
k = 2, 3, . . .
Proof. Recall that σ(x) is ﬁnitely supported when ω ∈D0. This implies the ﬁrst
claim. Further, integrating (2.2) by parts gives the second claim.
□
Deﬁnition 2.3. Given λ ∈Y, we deﬁne a piece–wise linear function λ( · ) as fol-
lows.
Let (r, s) and ∂λ be as in the proof of Proposition 1.1. Then the graph
y = λ(x) describes ∂λ in the coordinates x = s −r, y = r + s. The correspondence
λ 7→λ( · ) yields an embedding Y֒ →D0.
We have λ′(x) = ±1, except ﬁnitely many points, which are exactly the local
extrema of the function λ(x). These local extrema form two interlacing sequences
of points
x1 < y1 < x2 < · · · < xm < ym < xm+1 ,
(2.4)
where the xi’s are the local minima and the yj’s are the local maxima of the function
λ(x).
Proposition 2.4. We have
xi ∈Z,
yj ∈Z,
X
xi −
X
yj = 0.
(2.5)
Conversely, any couple of interlacing sequences (2.4) satisfying (2.5) comes from a
Young diagram λ, which is determined uniquely.
Idea of proof. For any couple of interlacing sequences (2.4), there exists a unique
polygonal line ω ∈D, with center at x0 = P xi −P yj and such that, for the
corresponding function σ,
σ′′(x) =
m+1
X
i=1
δ(x −xi) −
m
X
j=1
δ(x −yj) −δ(x −x0).
The line ω represents a Young diagram if and only if x0 = 0.
□
The correspondence λ 7→{xi} ∪{yj} provides one more useful system of param-
eters for Young diagrams.
10
