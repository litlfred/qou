---
doc_id: lect-mathematical-ideas-notions-qft-2002
doc_title: "Mathematical ideas and notions of quantum field theory"
section_id: page-004
section_title: "Page 4"
pages: 4-4
pdf_page: 4
source_pdf: lect-mathematical-ideas-notions-qft-2002.pdf
source_sha256: 95cac1ccd6c80226
text_source: ocr
granularity: page
doc_brief: "Mathematical ideas and notions of quantum field theory — 78 sections: Page 1; Page 2; Page 3"
---
4 MATHEMATICAL IDEAS AND NOTIONS OF QUANTUM FIELD THEORY

exist and come to correct and interesting conclusions (both physical and mathe-
matical). Therefore, making sense of such integrals is an interesting problem for
mathematicians, and will be one of our main occupation during the course.”

2. THE STEEPEST DESCENT AND STATIONARY PHASE FORMULAS

Now, let us forget for a moment that the integrals (1,2,3) are infinite dimensional
and hence problematic to define, and ask ourselves the following question: why
should we expect that when the parameter « or h goes to zero, we recover the usual
classical mechanics or field theory? The answer is that this expectation is based on
the steepest descent (respectively, stationary phase) principle from classical analysis:
if f(x) is a function in R? then the integrals f[ g(x)eS@/"da, f g(a)ef@/Pdx
“localize” to minima, respectively critical points, of the function f. As this classical
fact is of central importance to the whole course, let us now discuss it in some detail.

2.1. The steepest descent formula. Let f,g : [a,b] > R be smooth functions.

Theorem 2.1. (The steepest descent formula) Assume that f attains a global min-
imum at a unique point c € (a,b), such that f"(c) > 0. Then one has

b
(4) / g(a)eF(?)/Pdax = ni? eFflO/hT(H),

. _ alc)
where I(h) extends to a smooth function on (0,00) such that I(0) = Vinay:
Proof. Let I(h) be defined by the equation (4).

Let € be a real number, such that $ >> 0, and let [,(h) be defined by the same
equation, but with integration over [e— h?~*,c-+h?~‘]. It is clear that I(h) — (A)
is “rapidly decaying in h” (i.e. it is O(h’), h + 0 for any N). So it suffices to prove
the theorem for I, (h).

Further, let us make in the integral defining [,(h) the change of variables y =
(« —c)/Wh. Then we get

hoe
(5) L(h) = / g(e+ yV hel) fetaVB)) hy,
_pce

Now, note that the integrand is a smooth function with respect to Vh for h > 0.
Let J2(h) be the same integral as in (5) but with integrand replaced by its Taylor
expansion in Vf at 0 modulo AN. Then |I1 (A) — In(h)| < CAN~<.

Finally, let I3(h) be defined by the same integral as I2(h) but with limits from
—oo to oo. Then Iy(h) — I3(h) is rapidly decaying in h.

Thus, it suffices to show that I3(h) admits a Taylor expansion in fi!/? modulo
hN-©, and that the value at zero is as stated. But we know that I;(h) is a polynomial
in Vh. Also, the integrals giving coefficients of non-integer powers of h are integrals
over R of odd functions, so they are zero. So the first statement (existence of the
Taylor expansion) is proved. The value I3(0) is given by the integral

00 uw 2
_ fey?
ate) [ e 2 “dy,
00

2to be more precise, we will make sense of path integrals as power series in « or h.
