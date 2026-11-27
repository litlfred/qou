---
doc_id: arxiv-2302.02540v3
doc_title: "Linear programming bounds for hyperbolic surfaces"
section_id: sec-003-2-the-fourier-transform
section_title: "The Fourier transform"
section_number: 2
pages: 5-5
source_pdf: 2302.02540v3.pdf
source_sha256: 0dfe07df944902ec
toc_source: outline
doc_brief: "Linear programming bounds for hyperbolic surfaces — We adapt linear programming methods from sphere packings to closed hy- perbolic surfaces and obtain new upper bounds on their systole, their"
---
The Fourier transform of an integrable functionf:R→Cis defined by
bf(y) := 1√
2π
Z
R
f(x)e−iyxdx
fory∈R. If bfis integrable, then the Fourier inversion theorem says that its Fourier
transform is almost everywhere equal tox7→f(−x).
We will frequently use the scaling property that fora >0, the Fourier transform of
x7→f(ax) isy7→ bf(y/a)/a. Iffandgare integrable, then
[f∗g=
√
2πbfbg
where∗denotes the convolution and if bfandbgare also integrable, then
cfg= 1√
2π
bf∗bg.
Whenfis an even function, which will be the case throughout the paper, its Fourier
transform reduces to the cosine transform
bf(y) =
r
2
π
Z ∞
0
f(x) cos(yx)dx
and is therefore even.
An continuous integrable functionfwith integrable Fourier transform is said to be
positive-definiteif bf(y)≥0 for everyy∈R. This is not the usual definition, but is
equivalent to it under these hypotheses, by Bochner’s theorem. Iff 1 andf 2 are positive-
definite (and continuous, integrable, with integrable Fourier transform), thenf 1∗f 2 is
positive-definite provided that bf1bf2 is integrable, andf 1f2 is positive-definite provided
that it is integrable.
