---
doc_id: arxiv-2206.14086v3
doc_title: "KPZ limit theorems"
section_id: sec-018-8-integrable-differential-equations
section_title: "Integrable differential equations"
section_number: 8
pages: 11-12
source_pdf: 2206.14086v3.pdf
source_sha256: b6c27f820f963079
toc_source: outline
doc_brief: "KPZ limit theorems — One-dimensional interacting particle systems, 1+1 random growth models, and two-dimensional di- rected polymers deﬁne 2d height ﬁelds."
---
Integrable diﬀerential equations
Distribution functions of the KPZ ﬁxed point have connections to deterministic integrable diﬀerential equa-
tions. As proved in 1994 [86], the Tracy-Widom distribution is expressible in terms of the Painlev´e II equation,
one of a family of six special nonlinear ordinary diﬀerential equations [43]. The papers [2,20,73,87,92] also
found diﬀerential equations for equal-time, multi-position distribution functions of the KPZ ﬁxed point. We
state the following result for multi-point distributions for both inﬁnite and periodic domains.
Deﬁne the parameters
ti = τi/3,
yi = γi,
xi = hi,
and let
∂t =
m
X
i=1
∂ti,
∂y =
m
X
i=1
∂yi,
∂x =
m
X
i=1
∂xi.
Theorem 8.1 ( [12,13]). Let K = Kζ be the operator in either (7.1) or (7.3). If det(1 −K)̸ = 0, which holds
for all but at most countably many parameters, then
∂2
x log det(1 −K) = −rT p
for complex-valued m × 1 vector functions p(t, y, x) and r(t, y, x) which satisfy the equations
∂yp = 1
2∂2
x p −prT p,
∂yr = −1
2∂2
x r + rpT r
(8.1)
and
∂tp + ∂3
x p −3(∂xp)rT p −3prT (∂xp) = 0,
∂tr + ∂3
x r −3(∂xr)pT r −3rpT (∂xr) = 0.
(8.2)
Equation (8.2) is a coupled system of vector-valued modiﬁed Korteweg-De Vries (mKdV) equations. The
scalar mKdV equation is ∂tf +∂3
x f −6(∂xf)f 2 = 0. On the other hand, equation (8.1) forms a coupled system
11
(n, k)
0
t1n
t2n
n
