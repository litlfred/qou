---
doc_id: lect-mathematical-ideas-notions-qft-2002
doc_title: "Mathematical ideas and notions of quantum field theory"
section_id: page-006
section_title: "Page 6"
pages: 6-6
pdf_page: 6
source_pdf: lect-mathematical-ideas-notions-qft-2002.pdf
source_sha256: 95cac1ccd6c80226
text_source: ocr
granularity: page
doc_brief: "Mathematical ideas and notions of quantum field theory — 78 sections: Page 1; Page 2; Page 3"
---
6 MATHEMATICAL IDEAS AND NOTIONS OF QUANTUM FIELD THEORY

It is clear that this sequence has superexponential growth, so the radius of conver-
gence of the series is zero.

Remark. In fact, the non-analyticity of I(h) is related to the fact that the
integral defining I(h) is divergent for h < 0.

Let us now discuss the question: to what extent does the asymptotic expansion of
the function I(h) (which we can find using Feynman diagrams as explained below)
actually determines this function? Suppose that I(h) = Vaso anh” is a series with
zero radius of convergence. In general, we cannot uniquely determine a function I
on [0,¢) whose expansion is given by such a series. However, assume that a; are
such that the series g(h) = }°,,59 4nh”/n! is convergent in some neighborhood of
0, analytically continues to [0,0o), and has at most exponential growth as fi > oo.
In this case there is a “canonical” way to construct a smooth function I on [0,¢)
with (asymptotic) Taylor expansion T, called Borel summation of I. Namely, the
function I is defined by the formula

I(h) = [ g(hu)e~“du

The fact that I has the Taylor expansion I follows from the fact that for ¢ > 0 one

has
00
| ae *dx = nl.
0

For example, consider the series [ = 7 .)(—1)"nlh”. Then g(fi) = 7) 39(—D"A” =
zi: Hence, the Borel summation yields I(h) = Jo° Saad.

Physicists expect that in many situations perturbation expansions in quantum
field theory are Borel summable, and the actual answers are obtained from these
expansions by Borel summation. The Borel summability of perturbation series has
actually been established in a few nontrivial examples of QFT.

2.4. Application of steepest descent. Let us give an application of Theorem
2.1. Consider the integral

0
| te‘dt,s > 0.
0

It is well known that this integral is equal to the Gamma function I'(s + 1). By
doing a change of variable t = sx, we get

Tst) _ [is .-seqy = f[ e-8(e-l082) dy
seri A A

Thus, we can apply Theorem 2.1 for h = 1/s, f(x) = a—log x, g(x) = 1 (of course,
the interval [a,b] is now infinite, and the function f blows up on the boundary, but
one can easily see that the theorem is still applicable). The function f(x) = x—logx
has a unique critical point on [0,00), which is c = 1, and we have f(c) = 1. Then
we get

T(s +1) = s%e°V2ms8(1 + a1/s + a2/s? +---).

This is the celebrated Stirling’s formula.
