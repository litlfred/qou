---
doc_id: arxiv-1308.2499v1
doc_title: "Towards a regularity theory for integral Menger curvature"
section_id: sec-006-b-equivalence-of-fractional-seminorms
section_title: "B Equivalence of fractional seminorms"
section_number: null
pages: 27-32
source_pdf: 1308.2499v1.pdf
source_sha256: 3b20abdc0e1b0ba9
toc_source: outline
doc_brief: "Towards a regularity theory for integral Menger curvature — We generalize the notion of integral Menger curvature introduced by Gonzalez and Maddocks [14] by decoupling the powers in the integrand."
---
Equivalence of fractional seminorms
We give a straightforward proof of the equivalence of two seminorms on the Sobolev-
Slobodecki˘ı spaces we used in this article.
Lemma B.1. For s ∈(0, 1), p ∈[1, ∞) the seminorms
 f
W1+s,p :=
 Z
R/Z
Z 1/2
−1/2
| f ′(u + w) −f ′(u)|p
|w|1+sp
dw du
!1/p
,
(0.11)
f
W1+s,p :=
 Z
R/Z
Z 1/4
−1/4
| f(u + w) −2 f(u) + f(u −w)|p
|w|1+(1+s)p
dw du
!1/p
(0.12)
are equivalent on W1,p.
Proof. We ﬁrst prove the equivalence of the two norms for smooth f. The fundamental
theorem of calculus and the triangle inequality tell us
 f
W1+s,p =
 Z
R/Z
Z 1/4
−1/4
| f(u + w) −2 f(u) + f(u −w)|p
|w|1+(s+1)p
dw du
!1/p
=

Z
R/Z
Z 1/4
−1/4
|
R 1
0 f ′(u + τw) −f ′(u −τw) dτ|p
|w|1+sp
dw du

1/p
≤

Z
R/Z
Z 1/4
−1/4
|
R 1
0 f ′(u + τw) −f ′(u) dτ|p
|w|1+sp
dw du

1/p
+

Z
R/Z
Z 1/4
−1/4
|
R 1
0 f ′(u) −f ′(u −τw) dτ|p
|w|1+sp
dw du

1/p
27
= 2
 Z
R/Z
Z 1/4
−1/4
Z 1
0
| f ′(u + τw) −f ′(u)|p
|w|1+sp
dτ dw du
!1/p
.
Using Fubini’s theorem and substituting ˜w = τw, we can estimate this further by
2
 Z
R/Z
Z 1
0
τsp
Z τ/4
−τ/4
| f ′(u + ˜w) −f ′(u)|p
| ˜w|1+sp
d ˜w dτ du
!1/p
≤
2
1 + sp
 f
W1+s,p .
Hence,
 f
W1+s,p ≤
2
1 + sp
 f
W1+s,p .
To get an estimate in the other direction, we calculate for ε > 0
 f
W1+s,p =
 Z
R/Z
Z 1/4
−1/4
| f(u + w) −2 f(u) + f(u −w)|p
|w|1+(s+1)p
dw du
!1/p
=

Z
R/Z
Z 1/4
−1/4
|
R 1
0 f ′(u + τw) −f ′(u −τw) dτ|p
|w|1+sp
dw du

1/p
≥

Z
R/Z
Z 1/4
−1/4
|
R 1
1−ε f ′(u + τw) −f ′(u −τw) dτ|p
|w|1+sp
dw du

1/p
−

Z
R/Z
Z 1/4
−1/4
|
R 1−ε
0
f ′(u + τw) −f ′(u −τw) dτ|p
|w|1+sp
dw du

1/p
=: I1 −I2.
Substituting ˜τ =
τ
1−ε and ˜w = (1 −ε)w, we get
I2 =

Z
R/Z
(1 −ε)(1+s)p
Z (1−ε)/4
−(1−ε)/4
|
R 1
0 f ′(u + ˜τ ˜w) −f ′(u −˜τ ˜w) d˜τ|p
| ˜w|1+sp
d ˜w du

1/p
≤(1 −ε)1+s f
W1+s,p .
For I1 we observe
I1 ≥

Z
R/Z
Z 1/4
−1/4
|
R 1
1−ε f ′(u + w) −f ′(u −w) dτ|p
|w|1+sp
dw du

1/p
−

Z
R/Z
Z 1/4
−1/4
|
R 1
1−ε f ′(u + τw) −f ′(u + w) dτ|p
|w|1+sp
dw du

1/p
−

Z
R/Z
Z 1/4
−1/4
|
R 1
1−ε f ′(u −τw) −f ′(u −w) dτ|p
|w|1+sp
dw du

1/p
= ε
 Z
R/Z
Z 1/4
−1/4
| f ′(u + w) −f ′(u −w)|p
|w|1+sp
dw du
!1/p
−2

Z
R/Z
Z 1/4
−1/4
|
R 1
1−ε f ′(u + τw) −f ′(u + w) dτ|p
|w|1+sp
dw du

1/p
.
28
To bound the ﬁrst integral from below, we calculate
 f
W1+s,p =
 Z
R/Z
Z 1/2
−1/2
| f ′(u + w) −f ′(u)|p
|w|1+sp
dw du
!1/p
= 2−s
 Z
R/Z
Z 1/4
−1/4
| f ′(u + w) −f ′(u −w)|p
|w|1+sp
dw du
!1/p
.
The second integral can be estimated further
Z
R/Z
Z 1/4
−1/4
|
R 1
1−ε f ′(u + τw) −f ′(u + w) dτ|p
|w|1+sp
dw du
≤εp−1
Z
R/Z
Z 1/4
−1/4
Z 1
1−ε
| f ′(u + τw) −f ′(u + w)|p
|w|1+sp
dτ dw du
= εp−1
Z
R/Z
Z 1/4
−1/4
Z 1
1−ε
| f ′(u + (τ −1)w) −f ′(u)|p
|w|1+sp
dτ dw du
= εp−1
Z
R/Z
Z 1/4
−1/4
Z ε
0
| f ′(u −τw) −f ′(u)|p
|w|1+sp
dτ dw du
≤εsp+p
sp + 1
Z
R/Z
Z 1/4
−1/4
| f ′(u + w) −f ′(u)|p
|w|1+sp
dw du.
So we ﬁnally arrive at
 f
W1+s,p ≥2sε  f
W1+s,p −2
εs+1
pp
sp + 1
 f
W1+s,p −(1 −ε)1+s  f
W1+s,p .
For ε = 21−2/s this leads to
f
W1+s,p ≥2−1−2/s  f
W1+s,p .
To get the statement for f ∈W1,p we use a standard molliﬁer φ ∈C∞(R) with φ ≥0,
bounded support and
Z
R
φ dx = 1.
We set φε(x) := 1
εφ( x
ε) and
fε = f ∗φε.
Then fε converges to f in W1,p and we can hence chose a sequence εk →0 such that
fk := fεk converge pointwise almost everywhere to f and f ′
k to f ′.
Using H¨older’s inequality, we see that
 fε
p
W s+1,p =
Z
R/Z
Z 1/2
−1/2
|
R
R( f ′(u + w −z) −f ′(u −z))φε(z) dz|p
|w|1+sp
dw du
≤
 Z
R
φε(˜z) d˜z
!p−1 Z
R
Z
R/Z
Z 1/2
−1/2
|( f ′(u + w −z) −f ′(u −z))|pφε(z)
|w|1+sp
dw du dz
=
Z
R
φε(z)
Z
R/Z
Z 1/2
−1/2
|( f ′(u + w) −f ′(u))|p
|w|1+sp
dw du dz
29
=  fp
W s+1,p
for all ε > 0. Similarly,
 fε

W s+1,p ≤ f
W s+1,p .
Hence Fatou’s lemma tells us that
f
W1+s,p ≤lim inf
k→∞
 fk

W1+s,p ≤C lim inf
k→∞
 fk

W1+s,p ≤C  f
W1+s,p
and
 f
W1+s,p ≤lim inf
k→∞
 fk

W1+s,p ≤C lim inf
k→∞
fk

W1+s,p ≤C  f
W1+s,p .
This completes the proof of the lemma.
□
References
[1] S. Blatt. Note on continuously diﬀerentiable isotopies. Report 34, Institute for
Mathematics, RWTH Aachen, August 2009.
[2] S. Blatt. Boundedness and regularizing eﬀects of O’Hara’s knot energies. J. Knot
Theory Ramiﬁcations, 21(1):1250010, 9, 2012.
[3] S. Blatt. A note on integral Menger curvature for curves. Math. Nachr., 286(2-
3):149–159, 2013.
[4] S. Blatt and S. Kolasi´nski. Sharp boundedness and regularizing eﬀects of the
integral Menger curvature for submanifolds. Adv. Math., 230(3):839–852, 2012.
[5] S. Blatt and Ph. Reiter. Regularity theory for tangent-point energies: The non-
degenerate sub-critical case. ArXiv e-prints, Aug. 2012.
[6] S. Blatt and Ph. Reiter. How nice are critical knots? Regularity theory for knot
energies. Submitted, 2013.
[7] S. Blatt and Ph. Reiter. Modeling repulsive forces on ﬁbres via knot energies.
Submitted, 2013.
[8] S. Blatt and Ph. Reiter. Stationary points of O’Hara’s knot energies. Manuscripta
Math., 140(1-2):29–50, 2013.
[9] S. Blatt, Ph. Reiter, and A. Schikorra. Hard analysis meets critical knots (Station-
ary points of the M¨obius energy are smooth). ArXiv e-prints, Feb. 2012.
[10] H. Brezis.
How to recognize constant functions. A connection with Sobolev
spaces. Uspekhi Mat. Nauk, 57(4(346)):59–74, 2002.
[11] S. Campanato. Propriet`a di h¨olderianit`a di alcune classi di funzioni. Ann. Scuola
Norm. Sup. Pisa (3), 17:175–188, 1963.
[12] J. J. Dudziak. Vitushkin’s conjecture for removable sets. Universitext. Springer,
New York, 2010.
[13] M. H. Freedman, Z.-X. He, and Z. Wang. M¨obius energy of knots and unknots.
Ann. of Math. (2), 139(1):1–50, 1994.
30
[14] O. Gonzalez and J. H. Maddocks.
Global curvature, thickness, and the ideal
shapes of knots. Proc. Natl. Acad. Sci. USA, 96(9):4769–4773 (electronic), 1999.
[15] O. Gonzalez, J. H. Maddocks, F. Schuricht, and H. von der Mosel. Global cur-
vature and self-contact of nonlinearly elastic curves and rods. Calc. Var. Partial
Diﬀerential Equations, 14(1):29–68, 2002.
[16] Z.-X. He. The Euler-Lagrange equation and heat ﬂow for the M¨obius energy.
Comm. Pure Appl. Math., 53(4):399–431, 2000.
[17] T. Hermes. Analysis of the ﬁrst variation and a numerical gradient ﬂow for inte-
gral Menger curvature. PhD thesis, RWTH Aachen, 2012.
[18] S. Kass. Karl Menger [1902–1985]. Notices Amer. Math. Soc., 43(5):558–561,
1996.
[19] S. Kolasi´nski. Integral Menger curvature for sets of arbitrary dimension and codi-
mension. ArXiv e-prints, Nov. 2010.
[20] S. Kolasi´nski.
Geometric Sobolev-like embedding using high-dimensional
Menger-like curvature. ArXiv e-prints, May 2012.
[21] S. Kolasi´nski, P. Strzelecki, and H. von der Mosel. Characterizing W2,p subman-
ifolds by p-integrability of global curvatures. ArXiv e-prints, Mar. 2012.
[22] S. Kolasi´nski and M. Szuma´nska. Minimal H¨older regularity implying ﬁniteness
of integral Menger curvature. ArXiv e-prints, Nov. 2011.
[23] J. C. L´eger. Menger curvature and rectiﬁability. Ann. of Math. (2), 149(3):831–
869, 1999.
[24] R. A. Litherland, J. Simon, O. Durumeric, and E. Rawdon. Thickness of knots.
Topology Appl., 91(3):233–244, 1999.
[25] M. S. Mel′nikov. Analytic capacity: a discrete approach and the curvature of
measure. Mat. Sb., 186(6):57–76, 1995.
[26] M. S. Mel′nikov and J. Verdera. A geometric proof of the L2 boundedness of the
Cauchy integral on Lipschitz graphs. Internat. Math. Res. Notices, (7):325–331,
1995.
[27] K. Menger. Untersuchungen ¨uber allgemeine Metrik. Math. Ann., 103(1):466–
501, 1930.
[28] J. O’Hara. Family of energy functionals of knots. Topology Appl., 48(2):147–161,
1992.
[29] J. O’Hara. Energy of knots and conformal geometry, volume 33 of Series on
Knots and Everything. World Scientiﬁc Publishing Co. Inc., River Edge, NJ,
2003.
[30] Ph. Reiter. All curves in a C1-neighbourhood of a given embedded curve are
isotopic. Report 4, Institute for Mathematics, RWTH Aachen, October 2005.
[31] Ph. Reiter. Regularity theory for the M¨obius energy. Commun. Pure Appl. Anal.,
9(5):1463–1471, 2010.
31
[32] Ph. Reiter. Repulsive knot energies and pseudodiﬀerential calculus for O’Hara’s
knot energy family E(α), α ∈[2, 3). Math. Nachr., 285(7):889–913, 2012.
[33] T. Runst and W. Sickel. Sobolev spaces of fractional order, Nemytskij operators,
and nonlinear partial diﬀerential equations, volume 3 of de Gruyter Series in
Nonlinear Analysis and Applications. Walter de Gruyter & Co., Berlin, 1996.
[34] S. Scholtes. Tangency properties of sets with ﬁnite geometric curvature energies.
Fund. Math., 218:165–191, 2012.
[35] P. Strzelecki, M. Szuma´nska, and H. von der Mosel.
Regularizing and self-
avoidance eﬀects of integral Menger curvature. Ann. Sc. Norm. Super. Pisa Cl.
Sci. (5), IX(1):145–187, 2010.
[36] P. Strzelecki, M. Szuma´nska, and H. von der Mosel. On some knot energies
involving Menger curvature. ArXiv e-prints, Sept. 2012.
[37] P. Strzelecki and H. von der Mosel. How averaged Menger curvatures control
regularity and topology of curves and surfaces. 2013.
[38] P. Strzelecki and H. von der Mosel. Menger curvature as a knot energy. Submitted
to Physics Reports, 2013.
[39] J. Verdera. L2 boundedness of the Cauchy integral and Menger curvature. In
Harmonic analysis and boundary value problems (Fayetteville, AR, 2000), vol-
ume 277 of Contemp. Math., pages 139–158. Amer. Math. Soc., Providence, RI,
2001.
32
