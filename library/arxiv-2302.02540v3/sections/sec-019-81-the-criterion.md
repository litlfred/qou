---
doc_id: arxiv-2302.02540v3
doc_title: "Linear programming bounds for hyperbolic surfaces"
section_id: sec-019-81-the-criterion
section_title: "The criterion"
section_number: 8.1
pages: 25-26
source_pdf: 2302.02540v3.pdf
source_sha256: 0dfe07df944902ec
toc_source: outline
doc_brief: "Linear programming bounds for hyperbolic surfaces — We adapt linear programming methods from sphere packings to closed hy- perbolic surfaces and obtain new upper bounds on their systole, their"
---
Laplacian onMgoes as follows.
Theorem 8.1.Letg≥2. Suppose thatfis a non-constant admissible function for which
there exists anL>0such that
•f(x)≥0for allx∈R;
• bf
q
λ− 1
4

≤0wheneverλ≥L;
• bf(i/2)≤2(g−1)
R∞
0
bf(x)xtanh(πx)dx;
Thenλ 1(M)≤Lfor every hyperbolic surfaceMof genusg.
26 MAXIME FORTIER BOURQUE AND BRAM PETRI
Proof.Suppose thatMis a hyperbolic surface withλ 1(M)> L. By continuity, the same
inequality holds for every surfaceNin some neighborhoodUofMin moduli space. Let
rj(N)∈Cbe such thatr j(N) 2 =λ j(N)− 1
4. The Selberg trace formula yields
∞X
j=0
bf(rj(N))≤ bf(i/2)
≤2(g−1)
Z ∞
0
bf(x)xtanh(πx)dx
≤2(g−1)
Z ∞
0
bf(x)xtanh(πx)dx+ 1√
2π
X
γ∈C(N)
Λ(γ)f(ℓ(γ))
2 sinh(ℓ(γ)/2)
=
∞X
j=0
bf(rj(N))
from which we conclude that bf(rj(N)) = 0 for everyj≥1 and everyN∈U. As in the
proof of Theorem 6.1, this leads to a contradiction since the zero set of bfis discrete and
there are no non-trivial isospectral deformations of a hyperbolic surface. We conclude that
λ1(M)≤Lfor everyM.□
Remark8.2.If the inequality in the third bullet point is strict, then the conclusion can be
strengthened to a strict inequality and this is easier to prove.
