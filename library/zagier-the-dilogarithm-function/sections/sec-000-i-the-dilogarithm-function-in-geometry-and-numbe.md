---
doc_id: zagier-the-dilogarithm-function
doc_title: "The Dilogarithm Function"
section_id: sec-000-i-the-dilogarithm-function-in-geometry-and-numbe
section_title: "The dilogarithm function in geometry and number theory"
section_number: I
pages: 3-4
source_pdf: zagier-the-dilogarithm-function.pdf
source_sha256: 05079cf525c6ba0f
toc_source: inferred
doc_brief: "The Dilogarithm Function — 14 sections: Front matter; The dilogarithm function in geomet; Special values"
---
in geometry and number theory1
The dilogarithm function is the function deﬁned by the power series
Li2(z) =
∞

n=1
zn
n2
for |z| < 1 .
The deﬁnition and the name, of course, come from the analogy with the Taylor
series of the ordinary logarithm around 1,
−log(1 −z) =
∞

n=1
zn
n
for |z| < 1 ,
which leads similarly to the deﬁnition of the polylogarithm
Lim(z) =
∞

n=1
zn
nm
for
|z| < 1,
m = 1, 2, . . . .
The relation
d
dz Lim(z) = 1
z Lim−1(z)
(m ≥2)
is obvious and leads by induction to the extension of the domain of deﬁnition
of Lim to the cut plane C ∖[1, ∞); in particular, the analytic continuation of
the dilogarithm is given by
Li2(z) = −
 z
0
log(1 −u) du
u
for
z ∈C ∖[1, ∞) .
1 This paper is a revised version of a lecture which was given in Bonn on the
occasion of F. Hirzebruch’s 60th birthday (October 1987) and has also appeared
under the title “The remarkable dilogarithm” in the Journal of Mathematical and
Physical Sciences, 22 (1988).
6
Don Zagier
Thus the dilogarithm is one of the simplest non-elementary functions one
can imagine. It is also one of the strangest. It occurs not quite often enough,
and in not quite an important enough way, to be included in the Valhalla of
the great transcendental functions—the gamma function, Bessel and Legen-
dre - functions, hypergeometric series, or Riemann’s zeta function. And yet
it occurs too often, and in far too varied contexts, to be dismissed as a mere
curiosity. First deﬁned by Euler, it has been studied by some of the great
mathematicians of the past—Abel, Lobachevsky, Kummer, and Ramanujan,
to name just a few—and there is a whole book devoted to it [4]. Almost all
of its appearances in mathematics, and almost all the formulas relating to it,
have something of the fantastical in them, as if this function alone among all
others possessed a sense of humor. In this paper we wish to discuss some of
these appearances and some of these formulas, to give at least an idea of this
remarkable and too little-known function.
