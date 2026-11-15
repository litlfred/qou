---
doc_id: arxiv-2207.07246v2
doc_title: "Path Integral Quantum Monte Carlo Method for Light Nuclei"
section_id: sec-054-theoretical-foundation
section_title: "Theoretical foundation"
section_number: null
pages: 135-136
source_pdf: 2207.07246v2.pdf
source_sha256: 91e70e5fe39e07a5
toc_source: outline
doc_brief: "Path Integral Quantum Monte Carlo Method for Light Nuclei — 73 sections: Front matter; ABSTRACT; ACKNOWLEDGEMENTS"
---
Let us begin with a system of N particles with mass m. The energy shifted imaginary
time Schr¨odinger equation is
∂φ(x, τ)
∂τ
= D∇2φ(x, τ) + (ET −V (x))φ(x, τ),
(B.13)
where D = ℏ2/2m is called the diﬀusion constant, which is 1/2 in atomic unit. One
can see from Eq.(B.13) that, if (ET −V (x))φ(x, τ) = 0, we have a diﬀusion equation
∂φ(x, τ)
∂τ
= D∇2φ(x, τ).
(B.14)
If D∇2φ(x, τ) = 0, we have a rate equation which can be simulated by the branching
process,
∂φ(x, τ)
∂τ
= (ET −V (x))φ(x, τ).
(B.15)
By using short-time approximation, we can decompose the operator of the Green’s
function G into a diﬀusion part operator Gdiﬀand a branching part operator GB. We
know that, as an operator,
G = e−Hτ = e−(J+V −ET )τ̸ = e−Jτe−(V −ET )τ = GdiﬀGB,
(B.16)
where Gdiﬀ≡e−Jτ, GB ≡e−(V −ET )τ, J ≡−D∇2. However, if τ is very small, doing
Taylor expansion around τ for G, we obtain G−GdiﬀGB = 1
2[V, J]τ 2+O(τ 3). Therefore
we can write down the approximation
lim
τ→0 G = GdiﬀGB.
(B.17)
According to Trotter formula (Kalos and Whitlock (2008)), we can further write it in
a symmetrical way such that
G(y, x, τ)
=
⟨y|e−(J+V −ET )τ|x⟩
≈
⟨y|e−V −ET
2
e−Jτe−V −ET
2
|x⟩
≡
Gdiﬀ(y, x, τ)GB(y, x, τ).
(B.18)
The diﬀusion part Gdiﬀ(y, x, τ) ≡⟨y|e−Jτ|x⟩has the form of the free particle
propagator,
Gdiﬀ(y, x, τ) = (4πDτ)−3N
2
N
Y
i=1
e−(yi−xi)2
4Dτ
≡
N
Y
i=1
G(i)
diﬀ(yi, xi, τ).
(B.19)
Note that
R
Gdiﬀ(y, x, τ)dx = 1 and
R
Gdiﬀ(y, x, τ)dy = 1 are Gaussian integrals. So,
actually Gdiﬀ(y, x, τ) is a probability density which tells us that for a given xi or yi,
(yi)α −(xi)α = χ,
(B.20)
125
where χ is a Gaussian random number with zero mean value and variance 2Dτ, and
the subscript α means the x, y or z component of the ith particle. Eq.(B.20) already
tells us how to move the ith particle from xi(yi) to yi(xi) for ﬁxed xi(yi), as long
as we have a gaussian random number generator. We can denote Gdiﬀ(y, x, τ) as the
transition probability from x to y as P(y, x). Gdiﬀ(y, x, τ) is called diﬀusion part
because it satisﬁes the diﬀusion equation
∂Gdiﬀ(y, x, τ)
∂τ
≡D∇2Gdiﬀ(y, x, τ).
(B.21)
The solution of the branching part GB(y, x, τ) is
GB(y, x, τ) = e−[
V (x)+V (y)
2
−ET]τ.
(B.22)
It is called branching part because
∂GB(y, x, τ)
∂τ
= (ET −V )GB(y, x, τ),
(B.23)
which is a rate equation. The branching part GB(y, x, τ) serves as a weight which can
be denoted as W(y, x). If W(y, x) < 1, we delete the new conﬁguration y with the
probability 1 −W(y, x). If W(y, x) > 1, we replicate the new conﬁguration y with
INT[W(y, x)] copies, and with the probability W(y, x) −INT[W(y, x)] to replicate
it once more.
Now, the short-time evolution of φ can be written as
φ(y, τ) =
Z
Gdiﬀ(y, x, τ)GB(y, x, τ)φ(x)dx ≡
Z
dxP(y, x)W(y, x)φ(x), (B.24)
this expression provides the foundation for the simulation.
