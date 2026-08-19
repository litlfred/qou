---
doc_id: zagier-the-dilogarithm-function-copy-b
doc_title: "The Dilogarithm Function Don Zagier"
section_id: sec-028-1-variants-of-the-dilogarithm-function
section_title: "Variants of the dilogarithm function"
section_number: 1
pages: 20-21
source_pdf: zagier-the-dilogarithm-function-copy-b.pdf
source_sha256: c584944a501ef0c5
doc_brief: "The Dilogarithm Function Don Zagier — 56 sections: Don Zagier; The dilogarithm function in geomet; The Bloch-Wigner function D(z) and"
duplicate_of: "zagier-the-dilogarithm-function"
---
As explained in Chapter I, one of the disadvantages of the classical dilogarit hm
function Li 2(z) is that, although it has a holomorphic extension beyond the
region of convergence |z| < 1 of the deﬁning power series ∑ ∞
n=1 zn/n2, this
extension is many-valued. This complicates all aspects of the analysis of the
dilogarithm function. One way to circumvent the diﬃculty, discu ssed in detail
in §§3–4 of Chapter I, is to introduce the Bloch-Wigner dilogarithm functi on
D(z)= ℑ
[
Li2(z) − log |z| Li1(z)
]
, which extends from the original region of
deﬁnition 0 < |z| < 1 to a continuous function D : P1(C) → R which is (real-)
analytic on P1(C)/integerdivide{0, 1, ∞} ; this function has an appealing interpretation as
the volume of an ideal hyperbolic tetrahedron and satisﬁes “clean” funct ional
equations which do not involve products of ordinary logarithms.
It turns out, however, that there are other natural dilogarithm functi ons
besides Li 2 and D which have interesting properties. In this section we shall
discuss six of these: the Rogers dilogarithm L, which is similar to D but is
deﬁned on P1(R) (where D vanishes); the “enhanced” dilogarithm ˆD,w h i c h
takes values in C/π2Q and is in some sense a combination of the Rogers
and Bloch-Wigner dilogarithms, but is only deﬁned on the Bloch group of
The Dilogarithm Function 23
C rather than for individual complex arguments; the double logarithm Li 1,1,
the simplest of the multiple polylogarithms, which has two arguments but
can be expressed in terms of ordinary dilogarithms; the quantum dilogari thm
of Faddeev and Kashaev, which will play a role in the discussion of Nahm’s
conjecture in §3; and, very brieﬂy, the p-adic and the modulo p analogues of
the dilogarithm.
A. The Rogers dilogarithm. This function is deﬁned in the interval (0 , 1)
by
L(x)=L i 2(x)+ 1
2 log(x) log(1 − x)i f 0 <x< 1
and then extended to the rest of R by setting L(0) = 0, L(1) = π2/6, and
L(x)=
{
