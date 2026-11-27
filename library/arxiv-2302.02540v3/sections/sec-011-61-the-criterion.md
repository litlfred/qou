---
doc_id: arxiv-2302.02540v3
doc_title: "Linear programming bounds for hyperbolic surfaces"
section_id: sec-011-61-the-criterion
section_title: "The criterion"
section_number: 6.1
pages: 10-11
source_pdf: 2302.02540v3.pdf
source_sha256: 0dfe07df944902ec
toc_source: outline
doc_brief: "Linear programming bounds for hyperbolic surfaces — We adapt linear programming methods from sphere packings to closed hy- perbolic surfaces and obtain new upper bounds on their systole, their"
---
any of its shortest closed geodesics (also called systoles). Our criterion for bounding the
systole goes as follows.
Theorem 6.1.Letg≥2. Suppose thatfis a non-constant admissible function for which
there exists anR>0such that
•f(x)≤0ifx≥R;
• bf(ξ)≥0for everyξ∈R∪i

− 1
2, 1
2

;
• bf(i/2)≥2(g−1)
R∞
0
bf(x)xtanh(πx)dx.
Thensys(M)≤Rfor every closed hyperbolic surfaceMof genusg.
Proof.Suppose that there is a hyperbolic surfaceMof genusgsuch that sys(M)>R. Then
sys(N)>Rfor every surfaceNin some connected neighborhoodUofMin moduli space.
LINEAR PROGRAMMING BOUNDS FOR HYPERBOLIC SURF ACES 11
This implies thatf(ℓ(γ))≤0 for everyγ∈C(N) and we also have bf
q
λj(N)− 1
4

)≥0
for everyj≥0 by the hypotheses onfand bf. From the Selberg trace formula, we obtain
bf(i/2)≤
∞X
j=0
bf
q
λj(N)− 1
4

= 2(g−1)
Z ∞
0
bf(x)xtanh(πx)dx+ 1√
2π
X
γ∈C(N)
Λ(γ)f(ℓ(γ))
2 sinh(ℓ(γ)/2)
≤2(g−1)
Z ∞
0
bf(x)xtanh(πx)dx
≤ bf(i/2)
for everyN∈U. We conclude that bf
q
λj(N)− 1
4

= 0 for everyj≥1. Since bfis
holomorphic in a strip and not constant equal to zero, its zeros are isolated. This implies
that for everyj≥1, the eigenvalueλ j(N) is a constant function ofN∈Usince eigenvalues
depend continuously on the metric (see e.g. [BU83]). Therefore, all the surfaces inUare
isospectral. However, Gel’fand proved that any continuous deformation ofMthat preserves
the entire Laplace spectrum is constant [Gel63], which is a contradiction.□
Remark6.2.The analogous result for flat tori was proved in [CE03, Theorem 3.2] using a
rescaling and limiting argument for the second half of the proof.
Remark6.3.It is easy to see that if the inequality in the third bullet point is strict, then
the conclusion can be strengthened to a strict inequality. The proof proceeds similarly as
above, but the chain of inequalities directly leads to a contradiction.
