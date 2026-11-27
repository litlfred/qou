---
doc_id: arxiv-2302.02540v3
doc_title: "Linear programming bounds for hyperbolic surfaces"
section_id: sec-023-91-the-criterion
section_title: "The criterion"
section_number: 9.1
pages: 32-33
source_pdf: 2302.02540v3.pdf
source_sha256: 0dfe07df944902ec
toc_source: outline
doc_brief: "Linear programming bounds for hyperbolic surfaces — We adapt linear programming methods from sphere packings to closed hy- perbolic surfaces and obtain new upper bounds on their systole, their"
---
Laplacian on a hyperbolic surfaceMbym 1(M). The following criterion for boundingm 1
was first stated and proved in [FBP24, Lemma 3.2] in a slightly more general form.
Theorem 9.1.LetMbe a closed hyperbolic surface of genusg≥2and suppose thatfis
an admissible function such that
•f(x)≥0for allx∈R;
• bf
q
λ− 1
4

≤0wheneverλ≥λ 1(M);
• bf
q
λ1(M)− 1
4

<0.
Then
m1(M)≤
bf(i/2)−2(g−1)
Z ∞
0
bf(x)xtanh(πx)dx
−bf
q
λ1(M)− 1
4
 .
Proof.Let us writer j(M) =
q
λj(M)− 1
4. The Selberg trace formula tells us that
bf(i/2) +m 1(M)bf(r 1(M))≥
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
≥2(g−1)
Z ∞
0
bf(x)xtanh(πx)dx
since bf(rj(M)) is non-positive forj≥2 andfis non-negative on the length spectrum of
M. Rearranging yields the desired result.□
LINEAR PROGRAMMING BOUNDS FOR HYPERBOLIC SURF ACES 33
Observe that since we requirefto be non-negative onRand not constant equal to zero,
we automatically have that bfis positive on the imaginary axis. In particular, Theorem 9.1
cannot be used to prove bounds on the multiplicity ofλ 1 for surfaces withλ 1(M)≤
1/4, because then
p
λ1(M)−1/4 is on the imaginary axis. When applying the linear
programming method numerically, it also seems that the resulting bounds tend to infinity
asλ 1(M) decreases to 1/4 in any fixed genus.
We thus have to use different methods in order to boundm 1(M) whenλ 1(M) is close to
the interval [0,1/4]. Whenλ 1(M)∈[0,1/4], a theorem of Otal [Ota08] (later generalized
in [OR09]) says thatm 1(M)≤2g−3. Ifλ 1(M) is a little bit beyond 1/4, then the bound
gets slightly worse, namely, we have
m1(M)≤
(
2g−1 ifλ 1(M)∈(1/4,a g]
2gifλ 1(M)∈(a g,bg)
wherea g (resp.b g) is the smallest eigenvalue of the Laplacian on a hyperbolic disk of area
4π(g−1) (resp. 2π(g−1)) subject to Dirichlet boundary conditions [FBP24, Theorem
1.1]. Estimates fora g andb g are given in [FBP24, Section 2].
We thus use a combination of linear programming bounds and the above inequalities to
boundm 1 in a given genus since we need to consider all possible values forλ 1. Similarly
as for kissing numbers, when applying linear programming bounds over an intervalIof
values forλ 1, we need to subdivide it into smaller intervals and use a single functionfon
each subintervalJ, taking care to bound bf
q
λ− 1
4

forλ∈J.
