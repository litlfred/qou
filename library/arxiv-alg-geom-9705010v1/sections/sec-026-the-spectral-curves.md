---
doc_id: arxiv-alg-geom-9705010v1
doc_title: "Seiberg-Witten Integrable Systems"
section_id: sec-026-the-spectral-curves
section_title: "The spectral curves"
section_number: null
pages: 34-37
source_pdf: 9705010v1.pdf
source_sha256: 30ab8d0cc2d8f1ae
toc_source: inferred
doc_brief: "Seiberg-Witten Integrable Systems — 32 sections: Front matter; Contents; Introduction"
---
The spectral curves
For the classical groups we can write the equation of the Toda spectral curves
CF,u for the fundamental representation F as
w = z + µz−1, xǫw + p = 0
where
p = p(x) = xn+1 + u2xn−1 + · · · + un+1
for type An (G = SL(n + 1)), and
p = p(x2) = x2n + u2x2n−2+ . . . + u2n
for types Bn, Cn, and Dn, and the uℓare coordinates on the base. Here ǫ = 0
for An, Bn, Cn and ǫ = 2 for Dn.
In general, degx(p) is the dimension of the
representation, while the w term modiﬁes the coeﬃcient uhg corresponding to the
invariant of highest degree. For An, Bn, Cn, Dn, these Coxeter numbers are n +
1, 2n, 2n, 2n −2. (The Bn case is slightly diﬀerent since 0 is a weight of F. So the
actual “spectral” curve has equation x(w + p(x)) = 0. We may safely ignore the x
factor, since the distinguished Prym lives in the Jacobian of the other factor).
For An, the fundamental curve has genus n, so its Jacobian is the distinguished
Prym. It can be described geometrically as the ﬁber product over P1
w of the double
cover w = z+µz−1, branched at w = ±2√µ, and the degree n+1 cover w = −p(x),
with total ramiﬁcation over w = ∞and n simple branch points at the images of
the roots of p′(x) = 0. The substitution y = 2z + p(x)/2, 4µ = Λ2(n+1) converts it
to
y2 = p2(x) −Λ2(n+1),
the form obtained in [AF] and [KLTY]. (Here we have reinstated the scale param-
eter Λ of the asymptotically free theory. Previously this was set to 1).
The other spectral curves for An are easily obtained from the fundamental one.
The curve for ∧2F is of degree n(n+1)
2
over the z line, and of genus n(n−1)+1−[ n+1
2 ].
The obvious correspondence between it and CF,u produces a copy of J(CF,u) in
J(C∧2F,u).
The A3 case is described in [Ml], [MS]: The tetragenal curve CF,u
of genus 3 gives rise via Recillas’ trigonal construction (cf. [D3]) to the degree 6,
genus 5 curve C∧2F,u, together with an involution whose quotient is a trigonal curve
C′ of genus 2. The Jacobian of CF,u is isogenous to Prym(C∧2F,u/C′). (Actually,
the degree 6 and 3 curves produced by the trigonal construction have genera 7 and
4 respectively, but each has 2 nodes, over z = 0 and z = ∞; the curves C∧2F,u
and C′, of genera 5 and 3, are their respective desingularizations). A beautiful
picture of the g = 11 curve C∧2F,u for A4 is given in [MW1]. In contrast to these
small curves, there is the gigantic cameral cover, of degree n! over P1
z and of genus
1+
n−1
2(n+1)(n+2)!, whose Jacobian contains those of all (irreducible components of)
spectral covers.
SEIBERG-WITTEN INTEGRABLE SYSTEMS
35
For Dn, CF,u has equation x2w + p(x2) = 0. This depends on n parameters,
but has genus 2n −1, too big.
The quotient C′ by the involution x 7→−x is
hyperelliptic of genus n −1; the n-dimensional piece is Prym (CF,u/C′), and it can
be realized as the Jacobian of a curve C′′, the quotient of CF,u by the involution
x 7→−x, z 7→µz−1. The substitution y := x2(z −µz−1), 4µ = Λ4(n−1) takes the
equation of CF,u to
y2 = p2(x2) −Λ4(n−1)x4,
the form of the SO(2n) SYM curve obtained in [BL]. In terms of s = xy, t = x2,
the quotient C′′ becomes:
s2 = tp2(t) −Λ4(n−1)t3.
For type Cn, the fundamental Toda curve CF,u has equation w+p(x2) = 0, w =
z + µz−1. The substitution y = 2z + p(x2) changes this to
y2 = p2(x2) −4µ.
Just as in the Dn case, CF,u has automorphism group Z2 × Z2 over the t = x2 line:
P
I 1 :(t)
=p  (x  )-4  )
2
2
µ
:(x,y)/(y2
C F,u
C
:(t,s)/(s  =t(p  (t)-4  ))
2
2
µ
P
I 1:(x)
C :(t,y)/(y  -p  (t)-4  )
2
2
µ
and the n-dimensional piece is J(C′′). But this is not the right abelian variety for
the SYM theory. Rather, we should consider the Toda curves for (C(1)
n )∨= D(2)
n+1.
These have the form
w2 + p(x2) = 0, w = z + µz−1.
The coordinates on the three Z2 quotients by the involutions x 7→±x, z 7→±µz−1
are now:
(x,z)
(x,w)
(x,z  )
2
(x,w  )
(x,w  )
2
36
RON Y. DONAGI
where w′ = w −2µz−1 = z −µz−1. The corresponding genera are:
4n-3
n-1
2n-1
n-1
0
The middle curve has equation v + µ2
v + p(x2) −2µ = 0, where v = z2. It fac-
tors further: in fact, it looks just like the Cn-Toda curve, with z, µ, p replaced by
v, µ2, p −2µ respectively. So its Jacobian has an n-dimensional piece, which is the
Jacobian of:
s2 = t((p(t) −2µ)2 −4µ2) = tp(t)(p(t) −4µ).
This is essentially the Cn-curve obtained in [AS].
For Bn the story is similar, but simpler. The dual Toda curve has equation
x(z +µz−1)+p(x2) = 0. The substitution y = 2xz +p(x2), 4µ = Λ2(2n−1) converts
this to the form obtained in [DS],
y2 = p2(x2) −Λ2(2n−1)x2.
Again this is of genus 2n −1. The genus n quotient is
s2 = t(p2(t) −Λ2(2n−1)t).
For G2, we need Toda curves for (G(1)
2 )∨= D(3)
4 . These are given [MW1] as:
3(z −µz−1)2 −x8 + 2u2x6 −[u2
2 + 6(z + µz−1)]x4 + [u4 + 2u2(z + µz−1)]x2 = 0.
The various quotients involve the functions:
w = z + µz−1
s = x2
u = x(z −µz−1)
v = x(w −s2 + u2
3 s).
Some quotient curves, indicated by the functions which generate their ﬁelds, are:
(x,z)
(s,u)
(s,w)
(x,w)
(s,z)
(s)
(w)
(z)
(x)
(s,v)
SEIBERG-WITTEN INTEGRABLE SYSTEMS
37
The corresponding genera are:
11
5
5
3
0
0
0
0
2
1
I have not checked whether the genus 2 curve with functions (s, v) is the one
corresponding to the G2 theory. An explicit family of genus 2 curves was proposed
in several works (see references in [AAG]) for the G2 theory, but according to
[LPG] this family does not have good physical properties, and does not match the
Toda curves.
The E6 curves were considered in [LW], and turn out to involve some beautiful
geometry. The simplest curve is based on the 27-dimensional representation of E6.
The resulting 27-sheeted cover of the z line behaves like the lines on a 1-parameter
family of cubic surfaces. Each of the 6 simple roots corresponds to an ordinary
double point acquired by the surface, so the local monodromy at each ﬁnite branch
point is the product of 6 disjoint transpositions. Lerche and Warner study this
genus-34 spectral curve, and go on to relate it to an integrable system coming from
a string theory compactiﬁcation on a Calabi-Yau threefold which degenerates to a
ﬁbration of the E6 ALE singularity by a family of cubic surfaces.
