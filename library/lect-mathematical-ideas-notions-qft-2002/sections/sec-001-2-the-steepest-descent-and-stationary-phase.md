---
doc_id: lect-mathematical-ideas-notions-qft-2002
doc_title: "Mathematical ideas and notions of quantum field theory"
section_id: sec-001-2-the-steepest-descent-and-stationary-phase
section_title: "The steepest descent and stationary phase formulas"
section_number: "2"
pages: 4-7
source_pdf: lect-mathematical-ideas-notions-qft-2002.pdf
source_sha256: 95cac1ccd6c80226
toc_source: inferred
text_source: text rebuilt from glyph codes of the ps2pdf'd dvips PostScript (bitmap Type-3 fonts carry raw TeX OT1 codes; ps2pdf reports 'c' as U+0020, so a char-level rebuild maps it back and expands ligatures); prose good, display math flattened
---
2. The steepest descent and stationary phase formulas
Now, let us forget for a moment that the integrals (1,2,3) are infinite dimensional
and hence problematic to define, and ask ourselves the following question: why
should we expect that when the parameter ≤ or ~ goes to zero, we recover the usual
classical mechanics or field theory? The answer is that this expectation is based on
the steepest descent (respectively, stationary phase) principle from classical analysis:
R R
d −f(x)=≤ if(x)=~
if f(x) is a function in R then the integrals g(x)e dx, g(x)e dx
“localize” to minima, respectively critical points, of the function f. As this classical
fact is of central importance to the whole course, let us now discuss it in some detail.
2.1. The steepest descent formula. Let f; g : [a; b] ! R be smooth functions.
Theorem 2.1. (The steepest descent formula) Assume that f attains a global min-
00
imum at a unique point c 2 (a; b), such that f (c) > 0. Then one has
Z
b
−f(x)=~ 1=2 −f(c)=~
(4) g(x)e dx = ~ e I(~);
a
p
g(c)
where I(~) extends to a smooth function on [0; 1) such that I(0) = 2 p .
f00(c)
Proof. Let I(~) be defined by the equation (4).
1
Let ffl be a real number, such that 2 > ffl > 0, and let I1(~) be defined by the same
1 1
equation, but with integration over [c − ~ 2−ffl; c + ~ 2 −ffl]. It is clear that I(~) − I1(~)
N
is “rapidly decaying in ~” (i.e. it is O(~ ); ~ ! 0 for any N). So it suÆces to prove
the theorem for I1(~).
Further, let us make in the integral defining I1(~) the change of variables y =
p
(x − c)= ~. Then we get
Z −ffl
~ p p
(f(c)−f(c+y ~))=~
(5) I1(~) = g(c + y ~)e dy:
−~−ffl
p
Now, note that the integrand is a smooth function with respect to ~ for ~  0.
Let I2(~) be the same integral as in (5) but with integrand replaced by its Taylor
p
N N−ffl
expansion in ~ at 0 modulo ~ . Then jI1(~) − I2(~)j ≤ C~ .
Finally, let I3(~) be defined by the same integral as I2(~) but with limits from
−1 to 1. Then I2(~) − I3(~) is rapidly decaying in ~.
1=2
Thus, it suÆces to show that I3(~) admits a Taylor expansion in ~ modulo
N−ffl
~ , and that the value at zero is as stated. But we know that I3(~) is a polynomial
p
in ~. Also, the integrals giving coeÆcients of non-integer powers of ~ are integrals
over R of odd functions, so they are zero. So the first statement (existence of the
Taylor expansion) is proved. The value I3(0) is given by the integral
Z
1 f00(c)y2
g(c) e− 2 dy;
−1
2
to be more precise, we will make sense of path integrals as power series in ≤ or ~.
MATHEMATICAL IDEAS AND NOTIONS OF QUANTUM FIELD THEORY 5
so it is computed from the well known Poisson integral:
Z 1 y2 p
e− 2 dy = 2:
−1
The theorem is proved. 
2.2. Stationary phase formula. This theorem has the following imaginary ana-
log, called the stationary phase formula.
00
Theorem 2.2. Assume that f has a unique critical point c 2 (a; b), with f (c) 6= 0,
and g vanishes with all derivatives at a; b. Then
Z b
if(x)=~ 1=2 if(c)=~
g(x)e dx = ~ e I(~);
a
p
i=4 g(c)
where I(~) extends to a smooth function on [0; 1) such that I(0) = 2e p ,
j f00(c)j
00
where  is the sign of f (c).
Remark. It is important to assume that g vanishes with all derivatives at the
ends of the the integration interval. Otherwise we will get some additional boundary
contributions.
Proof. (sketch). The proof is analogous to the real case, but slightly more subtle.
The differences are as follows. First of all, the Poisson integral is replaced with the
(conditionally convergent) Fresnel integral
Z 1 iy2 p
e 2 dy = 2ei=4:
−1
Further, one should partition g in a sum of two smooth functions, one localized
1=2−ffl
around c on an interval of size 2~ , and the other vanishing near c. Next, one
needs to show that only the first summand matters, by using Riemann's lemma: if
R
b if(x)=~
f has no critical points in the support of g then g(x)e is rapidly decaying
a
(prove this!). Finally, for g localized around c, ones makes the change of variable
like in the real case. The statement about existence of Taylor expansion is proved
as in the real case, and the value at 0 is calculated using Fresnel integral. 
2.3. Non-analyticity of I(~) and Borel summation. It is very important to
note that the Taylor series for I(~) is usually not convergent and is only an as-
ymptotic expansion, so that the function I is smooth but not analytic at zero. To
illustrate this, consider the integral
Z 1 x2+x4 p
e− 2~ dx = 2~1=2I(~);
−1
where Z
1 1 y2+~y4
I(~) = p e− 2 dy:
2 −1
The latter integral expands asymptotically as
1
X
n
I(~) = an~ ;
n=0
where Z
n 1 4n n
(−1) 2 y (−1) 1 1
an = p e−y =2 dy = p 2n+ 2 −(2n + )=n!:
n
2 −1 2 n! 2 2
6 MATHEMATICAL IDEAS AND NOTIONS OF QUANTUM FIELD THEORY
It is clear that this sequence has superexponential growth, so the radius of conver-
gence of the series is zero.
Remark. In fact, the non-analyticity of I(~) is related to the fact that the
integral defining I(~) is divergent for ~ < 0.
Let us now discuss the question: to what extent does the asymptotic expansion of
the function I(~) (which we can find using Feynman diagrams as explained below)
P
~ n
actually determines this function? Suppose that I(~) = n0 an~ is a series with
zero radius of convergence. In general, we cannot uniquely determine a function I
on [0; ”) whose expansion is given by such a series. However, assume that ai are
P
n
such that the series g(~) = n0 an~ =n! is convergent in some neighborhood of
0, analytically continues to [0; 1), and has at most exponential growth as ~ ! 1.
In this case there is a “canonical” way to construct a smooth function I on [0; ”)
~ ~
with (asymptotic) Taylor expansion I, called Borel summation of I. Namely, the
function I is defined by the formula
Z
1
−u
I(~) = g(~u)e du
0
~
The fact that I has the Taylor expansion I follows from the fact that for t > 0 one
has
Z
1
n −x
x e dx = n!:
0
P P
~ n n n n
For example, consider the series I = (−1) n!~ . Then g(~) = (−1) ~ =
n0 n0
1 R 1 e−u
. Hence, the Borel summation yields I(~) = du.
1+~ 0 1+~u
Physicists expect that in many situations perturbation expansions in quantum
field theory are Borel summable, and the actual answers are obtained from these
expansions by Borel summation. The Borel summability of perturbation series has
actually been established in a few nontrivial examples of QFT.
2.4. Application of steepest descent. Let us give an application of Theorem
2.1. Consider the integral
Z 1
s −t
t e dt; s > 0:
0
It is well known that this integral is equal to the Gamma function −(s + 1). By
doing a change of variable t = sx, we get
Z Z
1 1
−(s + 1)
s −sx −s(x−log x)
= x e dx = e dx:
s+1
s 0 0
Thus, we can apply Theorem 2.1 for ~ = 1=s, f(x) = x − log x, g(x) = 1 (of course,
the interval [a; b] is now infinite, and the function f blows up on the boundary, but
one can easily see that the theorem is still applicable). The function f(x) = x−log x
00
has a unique critical point on [0; 1), which is c = 1, and we have f (c) = 1. Then
we get
p
s −s 2
−(s + 1) = s e 2s(1 + a1=s + a2=s +    ):
This is the celebrated Stirling's formula.
MATHEMATICAL IDEAS AND NOTIONS OF QUANTUM FIELD THEORY 7
2.5. Multidimensional versions of steepest descent and stationary phase.
Theorems 2.1,2.2 have multidimensional analogs. To formulate them, let V be a
real vector space of dimension d with a fixed volume element dx, and let f; g be
smooth functions in a closed box B  V .
Theorem 2.3. Assume that f has global minimum on B at a unique interior point
00
c, such that f (c) > 0. Then
Z
−f(x)=~ d=2 −f(c)=~
(6) g(x)e dx = ~ e I(~);
B
d=2 g(c)
where I(~) extends to a smooth function on [0; 1) such that I(0) = (2) p .
detf00(c)
00
Theorem 2.4. Assume that f has a unique critical point c in B, such that det f (c)
6= 0, and that g vanishes with all derivatives on the boundary of the box. Then
Z
if(x)=~ d=2 if(c)=~
(7) g(x)e dx = ~ e I(~);
B
d=2 i=4 g(c)
where I(~) extends to a smooth function on [0; 1) such that I(0) = (2) e p ,
j det f00(c)j
00
where  is the signature of the symmetric bilinear form f (c).
Remark. In presence of a volume element on V , the determinant of a symmetric
bilinear form is well defined.
The proofs of these theorems are parallel to the proofs of their one dimensional
versions. Namely, the 1-dimensional Poisson and Fresnel integrals are replaced with
their multidimensional versions – the Gaussian integrals
Z
−B(x;x)=2 d=2 −1=2
e dx = (2) (det B) ;
V
for a symmetric bilinear form B > 0, and
Z
iB(x;x)=2 d=2 i(B)=4 −1=2
e dx = (2) e j det Bj ;
V
for nondegenerate B. These integral formulas are easily deduced from the one-
dimensional ones by diagonalizing the bilinear form B.
