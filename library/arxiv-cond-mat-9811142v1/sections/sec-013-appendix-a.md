---
doc_id: arxiv-cond-mat-9811142v1
doc_title: "arXiv:cond-mat/9811142v1 [cond-mat.mes-hall] 10 Nov 1998"
section_id: sec-013-appendix-a
section_title: "Appendix A"
section_number: null
pages: 34-37
source_pdf: 9811142v1.pdf
source_sha256: 8666ebc040336b14
toc_source: inferred
---
In the case τx = τy = 0, the formula (3.9) for S2 at β = 1 reads
S2(x, y; 0, 0) =
q
w(y)
ΦN−2(x; 0)
rN/2−1(0) −
q
w(x)CN−1(x)
hN−1

CN−1(y)−(N−1)RN−2(y)

. (A.1)
34
Use of the explicit formulas (3.1) and (3.2) gives
CN−1(y) −(N −1)RN−2(y) = −(N −1)!

La
N−1(y) −d
dyLa
N−1(y)

= (N −1)! d
dyLa
N(y),
(A.2)
where the second equality follows from an appropriate Laguerre polynomial identity [13].
For the x-dependent factor in (A.1), we require an explicit formula for ΦN−2(x; 0).
Now (2.31) substituted in (2.16) gives
Φk(x; 0) =
Z
sgn(x −y)
q
w(y)Rk(y).
Making use of the explicit formulas (3.2) and (3.3) then gives
ΦN−2(x; 0)
rN/2−1(0) = −
1
4Γ(a + N)
Z ∞
0
sgn(x −y)ya/2e−y/2 d
dyLa
N−1(y) dy.
Integrating by parts, and making use of the Laguerre polynomial identity
(y −a)La
N−1(y) = y d
dyLa
N−1(y) −N

La
N(y) −La
N−1(y)

,
we see from this that
ΦN−2(x; 0)
rN/2−1(0) =
q
w(x)CN−1(x)
hN−1
+
N
4Γ(a + N)
Z ∞
0
sgn(x −y)ya/2−1e−y/2
La
N(y) −La
N−1(y)

dy.
(A.3)
Substituting (A.2) and (A.3) in (A.1) shows
S2(x, y; 0, 0) =
N!
4Γ(N + a)
q
w(y)
×
 d
dyLa
N(y)
 Z ∞
0
sgn(x −y)ya/2−1e−y/2
La
N(y) −La
N−1(y)

dy,
(A.4)
which is the formula recently given by Widom [8].
Consider next the expression (3.42) for S2 at β = 4 with τx = τy = 0. To simplify this
expression, we note that the formula in (3.39) for R2j(x) can be written in the simpliﬁed
form
R2j(x) =
1
a + 2j + 1

C2j+1(x) + 1
2(2j + 1)!x−a/2ex/2
Z x
0 ta/2e−t/2 d
dtL2j+2(t)

dt

.(A.5)
This formula can be checked by multiplying both sides by xa/2e−x/2 and diﬀerentiating.
(We also verify that the x →∞behaviour of both sides agrees.) Now, according to the
deﬁnition (2.16) of Φk and the second formula in (2.32)
ΦN−2(x; 0)
rN/2−1(0) = −
2
rN/2−1(0)
d
dx

xa/2e−x/2RN−2(x)

35
Substituting (A.5), and making use of the diﬀerentiation formulas
y d
dyLa
n(y) = nLa
n(y) −(n + a)La
n−1(y) = (n + 1)La
n+1(y) −(n + a + 1 −y)La
n(y)
and the fact that
(a + N −1)rN/2+1(0) = hN−1 = Γ(N)Γ(N + a)
we readily ﬁnd
ΦN−2(x; 0)
rN/2−1(0) −
q
w(x)CN−1(x)
hN−1
= −
q
w(x)
N
Γ(N + a)
(La
N(x) −La
N−1(x))
x
(A.6)
which thus simpliﬁes the x-dependent factor in (3.42). For the y-dependent factor, we see
from (A.5) that
q
w(y)

CN−1(y) −(a + N −1)RN−2(y)

= −1
2(N −1)!
Z y
0 ta/2e−t/2 d
dtLa
N(t) dt. (A.7)
Multiplying (A.6) and (A.7) shows
S2(x, y; 0, 0) =
N!
q
w(x)
2Γ(N + a)
La
N(x) −La
N−1(x)
x
Z y
0 ta/2e−t/2 d
dtLa
N(t) dt,
(A.8)
in agreement with the formula given recently by Widom [8].
References
[1] M.R. Zirnbauer, J. Math. Phys., 37 (1997) 4986.
[2] F.J. Dyson, J. Math. Phys., 3 (1962) 1191.
[3] P.J. Forrester, in Quantum Many Problems and Representation Theory, MSJ Mem-
oirs Vol. 1 (Math. Soc. Japan, 1998).
[4] T. Nagao and P.J. Forrester. Nucl. Phys. B in press.
[5] T. Nagao and M. Wadati, J. Phys. Soc. Jpn. 60 (1991) 3298; 61 (1992) 78; 61 (1992)
1910.
[6] T. Nagao and P.J. Forrester, Nucl. Phys. B 435 (1995) 401.
[7] T. Nagao and P.J. Forrester,
Quaternion determinant expressions for multilevel
dynamical correlation functions of parametric random matrices, in preparation.
[8] H. Widom, solv-int/9804005
[9] F.J. Dyson, Commun. Math. Phys. 19 (1970) 235.
[10] K. Frahm and J.L. Pichard, J. Phys. I France 5 (1995) 877.
36
[11] A. Erd´elyi et al.(ed.) Higher Transcendental Functions, Volumes I and II, (McGraw-
Hill, New York, 1953).
[12] G. Mahoux and M.L. Mehta, J. Phys. I (France) 1 (1991) 1093.
[13] G. Szeg¨o,
Orthogonal Polynomials (4th edition, American Mathematical Society,
1975).
[14] A.M.S. Macˆedo, Europhys. Lett. 26 (1994) 641.
[15] A.M.S. Macˆedo, Phys. Rev. B 53 (1996) 8411.
[16] P.J. Forrester, Nucl. Phys. B 403 (1993) 709.
[17] T.H. Baker, P.J. Forrester and P.A. Pearce, J. Phys. A 31 (1998) 6087.
[18] G.N. Watson, Theory of Bessel functions, 2nd ed. (Cambridge Univ. Press, Cam-
bridge, 1966).
[19] T. Nagao and P.J. Forrester, Phys. Lett. A 247 (1998) 42.
[20] P.J. Forrester, Physica A 223 (1996) 365
[21] P.J. Forrester and T. Nagao, J. Stat. Phys. 89 (1997) 69.
[22] B. Jancovici and P.J. Forrester, Phys. Rev. B 50 (1994) 14599.
[23] C.A. Tracy and H. Widom, solv-int/9804004.
[24] J. Verbaarschot Nucl. Phys. B 426 (1994) 559.
37
