---
doc_id: arxiv-1402.4615v3
doc_title: "GAUSSIAN FLUCTUATIONS OF YOUNG DIAGRAMS AND STRUCTURE CONSTANTS OF JACK CHARACTERS"
section_id: sec-007-22-transition-measure-and-free-cumulants
section_title: "Transition measure and free cumulants"
section_number: 2.2
pages: 14-15
source_pdf: 1402.4615v3.pdf
source_sha256: b6e7c795cd1a7cd2
doc_brief: "GAUSSIAN FLUCTUATIONS OF YOUNG DIAGRAMS AND STRUCTURE CONSTANTS OF JACK CHARACTERS — In this paper, we consider a deformation of Plancherel meas ure linked to Jack polynomials."
---
tion of transition measure of a Young diagram. This is a probability measure µλ
on the real line R associated to λ and deﬁned by its Cauchy transform:
Gµλ (z) =
∫
R
dµλ(x)
z − x =
∏
o∈Oλ z − o∏
i∈Iλ z − i .
In particular, transition measure is supported onIλ. Besides, its moment generating
series is given by
∑
k≥0
M (1)
k (λ) tk := 1
t Gµλ(1/t) =
∏
o∈Oλ 1 − o t∏
i∈Iλ 1 − i t ,
where M (1)
k (λ) :=
∫
R xkdµλ(x) is the k-th moment of µλ. It is easily seen that,
for any diagram, M (1)
0 (λ) = 1 and M (1)
1 (λ) = 0 . This generating series can be
rewritten as
∑
k≥0
M (1)
k (λ) tk = exp

∑
i∈Iλ
∑
k≥1
ik
k tk −
∑
o∈Oλ
∑
k≥1
ok
k tk


= exp

∑
k≥1
1
k pk(Iλ − Oλ) tk

 .
This implies that M (1)
k (λ) = hk(Iλ − Oλ), where hk is the complete symmetric
function of degree k; see [Mac95, page 25].
LARGE DIAGRAMS AND STRUCTURE CONSTANTS 15
Corollary 2.4. The family (M (1)
k )k≥2 forms an algebraic basis of Λ ⋆
(1).
We will also be interested in free cumulants R(1)
k (λ) of the transition measure
µλ. They are deﬁned by their generating series
Kλ(t) = t−1 +
∑
k≥1
R(1)
k (λ) tk−1,
where Kλ is the (formal) compositional inverse ofGµλ. The fact that M (1)
1 (λ) = 0
implies that either R(1)
1 (λ) = 0 (for all diagrams λ).
As explained by Lassalle [Las09, Section 5], they can be expressed as
(10) R(1)
k (λ) = e⋆
k(Iλ − Oλ)
for some homogeneous symmetric function e⋆
k of degree k. Functions e⋆
k form an
algebraic basis of symmetric functions, hence we have the fo llowing corollary of
Proposition 2.3.
Corollary 2.5. (R(1)
k )k≥2 is an algebraic basis of ring of polynomial functions on
the set of Young diagrams.
Remark. Free cumulants are classical objects in free probability th eory [V oi86,
Spe94], but considering them outside this context may seem s trange at ﬁrst sight.
The relevance of free cumulants of the transition measure of Young diagrams ﬁrst
appeared in the work of Biane [Bia98] and they have played an i mportant role in
asymptotic representation theory since then.
