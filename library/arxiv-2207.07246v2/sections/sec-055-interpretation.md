---
doc_id: arxiv-2207.07246v2
doc_title: "Path Integral Quantum Monte Carlo Method for Light Nuclei"
section_id: sec-055-interpretation
section_title: "Interpretation"
section_number: null
pages: 136-137
source_pdf: 2207.07246v2.pdf
source_sha256: 91e70e5fe39e07a5
toc_source: outline
doc_brief: "Path Integral Quantum Monte Carlo Method for Light Nuclei — 73 sections: Front matter; ABSTRACT; ACKNOWLEDGEMENTS"
---
A walker means a conﬁguration, x, for the N-particle system. If M walkers are dis-
tributed according φ, the number of them around the conﬁguration x + dx is Mφ(x).
In other words the normalized probability (density) for a walker to be around x + dx
is φ(x). Notice that now φ means a distribution, so it must be non-negative.
Assuming there are M (1) walkers in the ﬁrst generation, denoted as x(1), x(2),
..., x(M(1)), and are distributed according to φ. For a short-time τ, we move each
conﬁguration according to P(y, x) and branch them according to the weight W(y, x).
The number of walkers around a particular conﬁguration y is,
M(1)
X
i=1
P(y, x(i))W(y, x(i))M (1)φ(x(i)).
If M (1) is large enough, this sum becomes the following estimator of the integral,
M (1)
Z
dxP(y, x)W(y, x)φ(x).
126
On the other hand, summing over all the weight, we obtain the number of the second
generation of walkers, M (2). We denote the probability that they are around y as
φ′(y, τ), so the number of them is M (2)φ′(y, τ), and we have
M (2)φ′(y, τ) = M (1)
Z
dxP(y, x)W(y, x)φ(x).
In other words,
φ′(y, τ) = M (1)
M (2)
Z
dxP(y, x)W(y, x)φ(x) = M (1)
M (2)φ(y, τ).
So, the ratio of number of walkers between any two conﬁgurations in the next generation
y and y′ is φ′(y, τ)/φ′(y′, τ) = φ(y, τ)/φ(y′, τ). This means that the walkers will indeed
be distributed according to φ(y, τ). This is remarkable because now an integral with
high dimensions can be equivalently done through a stochastic process! In the spirit
of Eq.(B.12), by repeating the short-time diﬀusion process for suﬃcient number of
generations, ﬁnally the conﬁgurations will be distributed according to ground state
wave function Ψ0 (not Ψ2
0).
