---
doc_id: arxiv-hep-th-9304063v2
doc_title: "arXiv:hep-th/9304063v2 29 Jan 1999"
section_id: page-005
section_title: "Page 5"
section_number: null
pages: 5-5
source_pdf: 9304063v2.pdf
source_sha256: 14a82437462eae23
toc_source: undetermined
doc_brief: "arXiv:hep-th/9304063v2 29 Jan 1999 — 18 sections: Page 1; Page 2; Page 3"
---
D. Asymptotics
Again we take J = (0, s) and consider asymptotics as s →∞. From the random matrix point of view the interesting
quantities are
E(n; s) := (−1)n
n!
∂n
∂λn D(J; λ)

λ=1.
(1.23)
This is the probability that exactly n eigenvalues lie in J. The asymptotics of E(0, s) = D(J; 1) are obtained from
(1.19) using the asymptotics of q(s; 1) or equivalently σ(s; 1) obtained from (1.16) or (1.21), respectively.
(Our
derivation is heuristic since as far as we are aware the corresponding Painlev´e connection problem has not been
rigorously solved.) We ﬁnd that as s →∞,
E(0; s) = τα
e−s/4+α√s
sα2/4
(1.24)
×

1 + α
8 s−1
2 + 9α2
128 s−1 + ( 3α
128 + 51α3
1024 )s−3
2 + (75α2
1024 + 1275α4
32768 )s−2 + · · ·

,
where τα is a constant which cannot be determined from the asymptotics of q (or σ) alone. However, as we mentioned
above, when α = ∓1
2 this expansion must agree with those obtained from formulas (12.2.6) of [18] (see also (12.6.17)–
(12.6.19) in [18]) after replacing s by π2t2. This leads to the conjecture
τα = G(1 + α)
(2π)α/2
where G is the Barnes G-function [1]. This conjecture is further supported by numerical work similar to that described
for the analogous conjecture in [28].
As in [28], there are two approaches to the asymptotics of E(n; s) for general n. We use the notation
r(n; s) := E(n; s)
E(0; s) .
(1.25)
In the ﬁrst approach (see also [2,27]) one diﬀerentiates (1.21) successively with respect to λ. Using the known
asymptotics of σ(s; 1) and the diﬀerential equation (1.21) satisﬁed by σ(s; λ) for all λ, one can ﬁnd asymptotic
expansions for the quantities
σn(s) := ∂nσ
∂λn

λ=1
,
and these in turn can be used to ﬁnd expansions for the r(n; s).
This approach is inherently incomplete since
yet another undetermined constant enters the picture. And there are also computational problems since when one
expresses the r(n, s) in terms of the σn(s) a large amount of cancellation occurs, with the result that even the ﬁrst-order
asymptotics of r(n; s) are out of reach by this method when n is large.
The second approach uses the easily-established identity
r(n; s) =
X
i1<...<in
λi1 · · · λin
(1 −λi1) · · · (1 −λin)
(1.26)
where λ0 > λ1 > · · · are the eigenvalues of the integral operator K with λ = 1 acting on (0, s). It turns out that this
operator, rescaled so that it acts on (0, 1), commutes with the diﬀerential operator L deﬁned by
Lf(x) = (x(1 −x)f ′(x))′ −(α2
4x + sx
4 ) f(x),
with appropriate boundary conditions on f. Applying the WKB method to the equation, and a simple relationship
between the eigenvalues of K (as functions of s) and its eigenfunctions, we are able to derive the following asymptotic
formula for the eigenvalues as s →∞:
1 −λi ∼
2π
Γ(α + i + 1) i! si+ α+1
2
e−2√s 24i+2α+2.
(1.27)
5
