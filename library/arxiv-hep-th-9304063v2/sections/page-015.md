---
doc_id: arxiv-hep-th-9304063v2
doc_title: "arXiv:hep-th/9304063v2 29 Jan 1999"
section_id: page-015
section_title: "Page 15"
section_number: null
pages: 15-15
source_pdf: 9304063v2.pdf
source_sha256: 14a82437462eae23
toc_source: undetermined
doc_brief: "arXiv:hep-th/9304063v2 29 Jan 1999 — 18 sections: Page 1; Page 2; Page 3"
---
4. The region x →1
Letting y = 1 −x, f(x) = g(y) gives the approximating equation
(y g(y)′)′ −s
4 g(y) = 0.
The general solution of this is a constant times I0(√y) where I0 is the modiﬁed Bessel function. Thus we deduce that
as x →1
f(x) ∼c(s) I0
p
s(1 −x)

(3.10)
for some c(s).
5. Determination of a(s), b(s) and c(s)
From the asymptotics of I0 at inﬁnity and (3.10) we deduce that
f(x) ∼
c(s)
√
2π s
1
4
e
√s√1−x
(1 −x)
1
4
when x →1 and s(1 −x) →∞. Comparing this with (3.9) shows that a(s) = 0 and that
c(s) ∼
√
2π s
1
4 b(s).
(3.11)
And now comparing (3.9) with (3.6) and (3.8) in their overlapping range of validity we see that we must be in case 2
and that
b(s) ∼(−1)i
Γ(α + 1)
Γ(α + i + 1) 22n+α+1 e−√s.
(3.12)
What we shall need from all this is, ﬁrst, the asymptotics of f(1). This follows immediately from (3.10), (3.11),
(3.12), and the fact that I0(0) = 1:
f(1) ∼(−1)n √
2π
Γ(α + 1)
Γ(α + i + 1) s
i
2 + 1
4 e−√s22n+α+1.
(3.13)
We shall also need the asymptotics of
R
f(x)2dx. It follows from the asymptotics we have derived that the main
contribution to this integral comes from an arbitrarily small neighborhood of x = 0. It follows from (3.5), (3.7) and
the fact
Z ∞
0
xα e−x Lα
i (x)2 dx = Γ(α + i + 1)
i!
that
Z 1
0
f(x)2 dx ∼Γ(α + 1)2 i!
Γ(α + i + 1 s−α
2 −1
2 .
We put these two relations together to get what we really want, which is
f(1)2
R 1
0 f(x)2 dx
∼
2π
Γ(α + i + 1)i! si+ α
2 +1 e−2√s 24i+2α+2.
(3.14)
15
