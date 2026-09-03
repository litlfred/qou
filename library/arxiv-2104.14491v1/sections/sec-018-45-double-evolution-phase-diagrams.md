---
doc_id: arxiv-2104.14491v1
doc_title: "Khovanov polynomials for satellites and asymptotic adjoint polynomials A. Anokhinaa,∗ A. Morozova,b,c,† A. Popolitova,b,c,‡ a Institute for Theoretical and Experimental Physics, Mo"
section_id: sec-018-45-double-evolution-phase-diagrams
section_title: "Double-evolution phase diagrams"
section_number: 4.5
pages: 11-12
source_pdf: 2104.14491v1.pdf
source_sha256: 1aea658f17283df1
doc_brief: "Khovanov polynomials for satellites and asymptotic adjoint polynomials A. Anokhinaa,∗ A. Morozova,b,c,† A. Popolitova,b,c,‡ a Institute for Theoretical and Experimental Physics, Moscow 117218, Russia"
---
Now one can combine companion-evolution formulae (29,36) with
pattern-evolution formulae (15,16,17) to obtain double-evolution di-
agrams as in [38, 39]. A subtle point is that the invariant pattern-
evolution variablek is related to the parameters of the knot diagram
via a companion-dependent expression, as we discussed in sec.2.3.
If the companion’s crossing number n and the pattern’s half-twist
number w are chosen as variables, the critical values of the pat-
tern lie on a line determined by the relevant ShK from (18) for the
companion family we consider. In addition, there are critical values
of the companion evolution (when the companion is the unknot).
Altogether the critical lines divide the parametric plane into four
evolution domains, as shown in ﬁg.3.
5 Eigenvalue expressions, polynomiality and
positivity
Our evolution formulae for the Khovanov polynomials must give the
positive Laurent polynomials in q and t, but it is far from obvious
that they do. Now we rewrite the formulae so that this property
becomes explicit.
In this section, we introduce the eigenvalue variables
u = 1, x =q2t, y =q4t6. (38)
as follows. First we substitute
q2 = x4
y , t = y
x3. (39)
Then we place proper powers of u to complete the coeﬃcients to the fractions of homogeneous polynomials,
so that the total homogeneity degree is the same for all three coeﬃcients in each series. Introduce the
11
functions
S2(ν;y,x ) = sgn(ν)xν−yν
x−y =
max(0,ν)∑
i+j=ν−1
min(1,ν)
xiyj, (40)
and
S3(ν;u,x,y ) = uν
(u−x)(u−y) + xν
(x−u)(x−y) + yν
(y−u)(y−x) =
max(0,ν)∑
i+j+k=ν−2
min(1,ν)
xiyjzk (41)
Then the reduced AAK for the positive-torus half-family can be presented in an explicitly positive-polynomial
form as
KTorn>0 =x4n−2
((
x2 +u2 +uy +y2)
S2
( 1
2(n− 1);y2,x 2)
+S3
(
2−n;u2,x 2,y 2))
. (42)
A similar form for the negative-torus half-family can be obtained via the mirror symmetry
KTorn(x,y,u ) = KTor−n(x−1,y−1,u−1). (43)
Similarly, the AAK for the twist family can be expanded as
KTwn =p2x2ν +P1S2(ν;u2,x 2) +P3S2(ν;y2,x 2) +P13S3(ν;u2,x 2,y 2), (44)
with the explicitly positive polynomial coeﬃcients given by (45). Note that there are inﬁnitely many
expansions similar to (42,44), and we just try to ﬁnd the most nice one.
n ≥ 2 ≤ 0
ν 2−n
2 ≤ 0 −n
2 ≥ 0
p2 x−9y−1(
u2x2 +u2y2 +x2y2 +ux(u2 +xy)
)
0
P1 u2x−7(x +y) u4y−2(u +x)(u +y) +u6x−2 +u2x3y−1
P3 x−6y−1(u +x)(u2 +xy) x−1y−1(x +u)(ux2 +yu2 +xy2 +uxy)
P13 x−7(u +x)(u +y)(x +y)(u2 +xy) u2x−1y−1(u +x)2(u +y)(x +y)
(45)
