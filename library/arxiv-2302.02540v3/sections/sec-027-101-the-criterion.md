---
doc_id: arxiv-2302.02540v3
doc_title: "Linear programming bounds for hyperbolic surfaces"
section_id: sec-027-101-the-criterion
section_title: "The criterion"
section_number: 10.1
pages: 39-40
source_pdf: 2302.02540v3.pdf
source_sha256: 0dfe07df944902ec
toc_source: outline
doc_brief: "Linear programming bounds for hyperbolic surfaces — We adapt linear programming methods from sphere packings to closed hy- perbolic surfaces and obtain new upper bounds on their systole, their"
---
N[0,L](M) of eigenvalues of ∆ M in the interval [0,L] for anyL>0.
Theorem 10.1.LetL,R>0and suppose thatf:R→Ris an admissible function such
that
•f(x)≤0for everyx≥R;
• bf(ξ)≥0for everyξ∈R;
• bf(
p
λ−1/4)≥1for everyλ∈[0,L];
Then every closed hyperbolic surfaceMof genusg≥2withsys(M)≥Rsatisfies
N[0,L](M)≤2(g−1)
Z ∞
0
bf(x)xtanh(πx)dx+ 1− bf(i/2).
Proof.By hypothesis, bf(rj(M)) is at least 1 for all eigenvaluesλ j(M) in the interval [0,L]
and non-negative at all eigenvalues. Also note thatλ 0(M) = 0∈[0,L] corresponds to the
term bf(i/2). We thus have
N[0,L](M)−1 + bf(i/2)≤
∞X
j=0
bf(rj(M))
= 2(g−1)
Z ∞
0
bf(x)xtanh(πx)dx+ 1√
2π
X
γ∈C(M)
Λ(γ)f(ℓ(γ))
2 sinh(ℓ(γ)/2)
≤2(g−1)
Z ∞
0
bf(x)xtanh(πx)dx
by the Selberg trace formula, where the last inequality is because the geometric terms are
non-positive by hypothesis.□
Recall that an eigenvalue of the Laplacian onMissmallif it belongs to the interval
[0,1/4]. The numberN small(M) of small eigenvalues ofMis therefore equal toN [0,1/4](M).
40 MAXIME FORTIER BOURQUE AND BRAM PETRI
Also note thatλ∈[0,1/4] if and only if
p
λ−1/4∈i[−1/2,1/2]. In practice, we will
often use the weaker bound
Nsmall(M)
2(g−1) ≤inf
f
Z ∞
0
bf(x)xtanh(πx)dx
(where the infimum is over the functionsfthat satisfy the hypotheses of the theorem)
instead of the one given in Theorem 10.1 because the right-hand side only depends on
sys(M) and not on the genus. A theorem of Otal and Rosas [OR09] states that the left-
hand side is always bounded above by 1, and this is sharp for surfaces with a very short
pants decomposition [Bus77] (see also [Bus10, Theorem 8.1.3]). Our goal is therefore to
find the smallest value ofR= sys(M) for which the right-hand side becomes smaller than
1 and to estimate how it decreases as the systole increases.
