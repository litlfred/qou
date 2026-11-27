---
doc_id: arxiv-2302.02540v3
doc_title: "Linear programming bounds for hyperbolic surfaces"
section_id: sec-004-3-the-selberg-trace-formula
section_title: "The Selberg trace formula"
section_number: 3
pages: 5-6
source_pdf: 2302.02540v3.pdf
source_sha256: 0dfe07df944902ec
toc_source: outline
doc_brief: "Linear programming bounds for hyperbolic surfaces — We adapt linear programming methods from sphere packings to closed hy- perbolic surfaces and obtain new upper bounds on their systole, their"
---
Given a closed hyperbolic surfaceM(always assumed to be oriented), we list the eigen-
values of its Laplace–Beltrami operator (acting on square-integrable functions) in non-
decreasing order
0 =λ 0(M)<λ 1(M)≤λ 2(M)≤···
where each eigenvalue is repeated according to its multiplicity, i.e., the dimension of the
corresponding eigenspace.
The set of oriented closed geodesics inMis denoted byC(M). This means that each
unoriented closed geodesic appears twice inC(M), once for each orientation. The length of
a geodesicγ∈C(M) is denotedℓ(γ) and itsprimitive lengthis denoted Λ(γ). The latter
is defined as the length of the shortest geodesicαsuch thatγ=α k for some powerk≥1.
The geodesicαis calledprimitivebecause it cannot be expressed as a proper power of
another geodesic.
6 MAXIME FORTIER BOURQUE AND BRAM PETRI
A functionf:R→Cis said to beadmissibleif it is even, continuous, integrable, and
its Fourier transform bfis holomorphic in a horizontal strip of the form

z∈C:|Im(z)|< 1
2 +ε

for someε>0 and satisfies the decay condition
|bf(z)|=O
 1
1 +|z|p

for somep >2 in that strip. Note that the decay condition implies that bfandy bf(y) are
integrable on the real line so thatfmust be continuously differentiable by Fourier inversion
and differentiation under the integral sign.
With the above notation and normalizations, the Selberg trace formula [Bus10, Section
9.5] states that for every closed hyperbolic surfaceMof genusgand every admissible
functionf:R→C, we have
∞X
j=0
bf
q
λj(M)− 1
4

= 2(g−1)
Z ∞
0
bf(x)xtanh(πx)dx+ 1√
2π
X
γ∈C(M)
Λ(γ)f(ℓ(γ))
2 sinh(ℓ(γ)/2).
Since bfis even, it does not matter which square root we use on the left-hand side. It is
customary to writer j(M) for either of the two roots, so thatr j(M) 2 + 1
4 =λ j(M). Note
that our convention for the Fourier transform differs from the one used in [Bus10] by a
factor of 1/
√
2π, which explains the appearance of this factor in the above formula.
