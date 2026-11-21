---
doc_id: arxiv-1412.4711v1
doc_title: "CHARACTER VARIETIES FOR SL(3, C): THE FIGURE EIGHT KNOT"
section_id: sec-022-53-a-focus-on-the-pu21-case
section_title: "A focus on the PU(2,1) case"
section_number: 5.3
pages: 26-28
source_pdf: 1412.4711v1.pdf
source_sha256: 4fb1d6ee062cca8c
toc_source: outline
doc_brief: "CHARACTER VARIETIES FOR SL(3, C): THE FIGURE EIGHT KNOT — We give a description of several representation varieties of the fundamental group of the complement of the ﬁgure eight knot in PGL(3, C) or"
---
tions with image inside the real group PU(2, 1) may carry interesting geo-
metric properties. So we seek representations preserving Hermitian forms.
In the case of the ﬁrst component R1, the following condition on traces
holds:
tr(A) = tr(a)
,
tr(B) = tr(b) .
In particular, we note that since tr(B) = tr(b) = v, the parameter v is forced
to be real for such representations. Then, from tr(A) = tr(a), we obtain
(−1 + v)2(1 + v)
u
= u ,
or
u = | (−1 + v)
√
1 + v| z,
27
with z lying on the unit circle.
It is in fact possible to compute a Hermitian matrix H as a function of
the coordinates v , z,
H(v, z) =


1
r
s
r
1
r
s
r
1

,
whose associated form is respected by the representations just described;
the entries of H lie in an Abelian extension of degree 4 of Q(v, Re(z)), and
are a little too cumbersome for inclusion here. However, for speciﬁc v , z the
signature of H enables one to determine whether the representation takes
values in SU(3) or SU(2, 1), or whether the associated form is degenerate. In-
deed, the representations with degenerate forms occupy some isolated points
in the (v, z)–variety, together with some simple closed curves that separate
SU(3)–representations from SU(2, 1)–representations.
One can compute that the variety R1 gives rise to a single boundary
unipotent representation into PU(2, 1), obtained by composing the repre-
sentation
(u, v) = (−
√
3 i , 2)
with the natural projectivization map SU(2, 1) →PU(2, 1). The variety R1
also contains the other two lifts of this PU(2, 1)– representation to SU(2, 1),
at
(u, v) = (−ω(
√
3 i) , 2) ,
(u, v) = (−ω2(
√
3 i) , 2)
(where
ω = e2πi/3).
The other two components R2 and R3 each give rise to just one bound-
ary unipotent representation into PU(2, 1), given by (u, v) = (3, 3).
A necessary condition on traces for a representation in R2 or R3 to
respect a Hermitian forms is
tr(a) = tr(A) , tr(b) = tr(B)
,
i.e.
v = u .
Using the same technique as that described at the beginning of this sec-
tion, i.e. invoking LLL together with polynomial interpolation, the following
diagonal matrix:
H =


−1
8(∆−16)
√
∆+ |u|2 −4

0
0
0
∆−16
0
0
0
−8
√
∆+ 4



was found, satisfying
Ha−1 = a †H , Hb−1 = b †H
(v = u , ∆≥0) ,
where the superscript † denotes conjugate transpose, and ∆= 4u3 + 4v3 −
u2v2 −16uv + 16 = 4(u3 + u3) −|u|4 −16|u|2 + 16. Clearly the condition
∆≥0 is required for H to be Hermitian. We note that the form represented
28
E. FALBEL, A. GUILLOUX, P.-V. KOSELEFF, F. ROUILLIER AND M. THISTLETHWAITE
by H degenerates at ∆= 16; in the present context v = u the corresponding
values of u are 0 , 4 , 4e2πi/3 , 4e4πi/3.
Substituting u = x + iy , v = x −iy (x , y ∈R) in the expression for
∆(u, v), we obtain (with mild abuse of notation)
∆(x, y) = −x4 −y4 −2x2y2 −24xy2 + 8x3 −16x2 −16y2 + 16 .
We have therefore established that representations respecting Hermitian
forms occur in the bounded complementary regions in the (x, y)–plane of
the curve ∆(x, y) = 0, see Figure 4. The SU(3) representations lie in the
central complementary region, and the SU(2, 1) representations lie in the
three petals. Corresponding Hermitian representations occur also on the
curve itself, except for singularities at the three self-intersection points of the
curve, where representations are not deﬁned. The quantity ∆has geometric
signiﬁcance in that it is related to the Brehm shape invariant [3] of the
triangle in the associated homogeneous space (complex projective plane CP2
or complex hyperbolic plane CH2), whose vertices are the ﬁxed points of the
elliptic isometries α , β , γ.
-4
-2
0
2
4
6
-4
-2
0
2
4
Figure 4. SU(3) and SU(2, 1) representations in R2
