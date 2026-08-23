---
doc_id: zagier-the-dilogarithm-function
doc_title: "The dilogarithm function"
section_id: sec-030-1-variants-of-the-dilogarithm-function
section_title: "Variants of the dilogarithm function"
section_number: 1
pages: 20-21
source_pdf: zagier-the-dilogarithm-function.pdf
source_sha256: 05079cf525c6ba0f
doc_brief: "The dilogarithm function — 56 sections: Don Zagier; The dilogarithm function in geomet; The Bloch-Wigner function D(z) and"
---
As explained in Chapter I, one of the disadvantages of the classical dilogarithm
function Li
2(z) is that, although it has a holomorphic extension beyond the
region of convergence |z| < 1 of the deﬁning power series ∑∞
n=1zn/n2, this
extension is many-valued. This complicates all aspects of the analysis of the
dilogarithm function. One way to circumvent the diﬃculty, discussed in detail
in§§3–4 of Chapter I, is to introduce the Bloch-Wigner dilogarithm function
D(z)= ℑ
[
Li
2(z)− log|z|Li1(z)
]
, which extends from the original region of
deﬁnition 0<|z|< 1 to a continuous functionD : P1(C)→ R which is (real-)
analytic on P1(C)/integerdivide{0,1,∞}; this function has an appealing interpretation as
the volume of an ideal hyperbolic tetrahedron and satisﬁes “clean” functional
equations which do not involve products of ordinary logarithms.
It turns out, however, that there are other natural dilogarithm functions
besides Li
2 and D which have interesting properties. In this section we shall
discuss six of these: the Rogers dilogarithm L, which is similar to D but is
deﬁned on P1(R) (where D vanishes); the “enhanced” dilogarithm ˆD,w h i c h
takes values in C/π2Q and is in some sense a combination of the Rogers
and Bloch-Wigner dilogarithms, but is only deﬁned on the Bloch group of
The Dilogarithm Function 23
C rather than for individual complex arguments; the double logarithm Li1,1,
the simplest of the multiple polylogarithms, which has two arguments but
can be expressed in terms of ordinary dilogarithms; the quantum dilogarithm
of Faddeev and Kashaev, which will play a role in the discussion of Nahm’s
conjecture in§3; and, very brieﬂy, the p-adic and the modulo p analogues of
the dilogarithm.
A. The Rogers dilogarithm. This function is deﬁned in the interval (0,1)
by
L(x)=L i
2(x)+ 1
2 log(x) log(1−x)i f 0 <x<1
and then extended to the rest of R by settingL(0) = 0,L(1) =π2/6, and
L(x)=
{
2L(1)− L(1/x)i f x> 1,
−L(x/(x− 1)) if x< 0.
The resulting function is then a monotone increasing continuous real-valued
function on R and is (real-)analytic except at 0 and 1, where its derivative
becomes inﬁnite. At inﬁnity it is not continuous, since one has
lim
x → +∞
L(x)=2 L(1) = π2
3 , lim
x →− ∞
L(x)= −L(1) = −π2
6 ,
but it is continuous if we consider it moduloπ2/2. Moreover, the new function
L(x): = L(x) (mod π2/2) from P1(R)t o R/π2
