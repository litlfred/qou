---
doc_id: arxiv-hep-th-9304063v2
doc_title: "arXiv:hep-th/9304063v2 29 Jan 1999"
section_id: sec-004-3-asymptotics
section_title: "Asymptotics"
section_number: 3
pages: 12-18
source_pdf: 9304063v2.pdf
source_sha256: 14a82437462eae23
toc_source: inferred
---
A. Asymptotics of the σ-equation
In the case of the ﬁnite N ensemble and α = 0, Edelman [7,8] and Forrester [11] (by a direct evaluation of the
integrals deﬁning the probability EN(0; s)) has shown that E(0; s) is exactly equal to e−s/4. From this it follows, for
α = 0 and λ = 1, that σ(s; 1) = s/4. For general α and λ = 1 it is therefore reasonable to assume an asymptotic
expansion of the form:
σ(s; 1) = c1s + c2s1/2 + c3 + c4s−1/2 + · · · ,
s →∞.
Substituting this into the diﬀerential equation (1.21) results in equations that uniquely determine the coeﬃcients cj
once a choice in the square root
√
α2 is made. Since for α = ∓1
2 our asymptotic expansion of E(0; s) must agree with
those of Dyson (recall (1.3)), we see that we must choose the square root −α −α. A calculation then gives
σ(s; 1) = s
4 −α
2 s1/2 + α2
4 + α
16s−1/2 + α2
16 s−1 + α
256(16α2 + 9)s−3/2 + α2
64 (4α2 + 9)s−2
+ α
2048(128α4 + 720α2 + 225)s−5/2 + · · ·
s →∞,
(3.1)
from which (1.24) follows.
B. Asymptotics via the commuting diﬀerential operator
Throughout this section we take λ = 1. The operator K, when rescaled to act on (0, 1) instead of (0, s), has kernel
s K(sx, sy). By (2.2) this is equal to
s
4
Z 1
0
φ(sxt) φ(syt) dt,
12
and so K (rescaled, as it will be throughout this section), is the square of the operator on (0, 1) with kernel
J(x, y) =
√s
2 φ(sxy) =
√s
2 Jα(√sxy).
This function satisﬁes the diﬀerential equation
x2Jxx + xJx + (sxy
4
−α2
4 )J = 0.
(3.2)
The operator J will commute with a diﬀerential operator
L = d
dxα(x) d
dx + β(x)
if α(0) = α(1) = 0 and if
α(y)Jyy + α′(y)Jy + β(y)J = α(x)Jxx + α′(x)Jx + β(x)J.
If we use (3.2) we see that this will be satisﬁed if
−α(x)

x−1Jx + ( sy
4x −α2
4x2 )

+ α′(x)Jx + β(x)J
= the same expression with x and y interchanged.
Equating the terms involving the ﬁrst derivatives of J gives
(α′(x) −x−1α(x))Jx = (α′(y) −y−1α(y))Jy.
But x Jx = y Jy, so the above will hold if
x−1(α′(x) −x−1α(x)) = y−1(α′(y) −y−1α(y)).
This is satisﬁed if α(x) is a quadratic without constant term and, of course, we choose
α(x) = x(1 −x).
What is required of β, then, is seen to be
β(x) −x(1 −x)( sy
4x −α2
4x2 ) = β(y) −y(1 −y)(sx
4y −α2
4y2 ),
which is satisﬁed by
β(x) = −α2
4x −sx
4 .
We write the diﬀerential equation, for which the eigenfunctions f(x) are the eigenfunctions of J, as
(x(1 −x)f ′x))′ + (µ√s −α2
4x −sx
4 )f(x) = 0.
(3.3)
The boundary conditions are that f(x) be bounded as x →1 and that f(x) be asymptotic to a constant times xα/2
as x →0. The reason we wrote the eigenvalues as we did is that for each i the µ corresponding to the i’th largest
eigenvalue is bounded as s →∞. This is easily seen by an oscillation argument. So we assume i is ﬁxed and proceed
to ﬁnd the asymptotics of the corresponding eigenfunction f(x) as s →∞. We assume it normalized so that
f(x) ∼xα/2 as x →0.
(3.4)
13
1. The region x ≪1
The approximating equation is
f ′′(x) + 1
xf ′(x) + (µ√s
x
−α2
4x2 −s
4)f(x) = 0.
The solution of this equation which satisﬁes (3.4) is
xα/2e−√sx/2Φ(1 + α
2
−µ, 1 + α, √sx)
where Φ is the conﬂuent hypergeometric function [9]. We deduce that when x ≪1,
f(x) ∼xα/2 e−√sx/2 Φ(1 + α
2
−µ, 1 + α, √sx).
(3.5)
2. The region x ≪1, √sx ≫1
Case 1. µ̸ = i + 1+α
2
(i = 0, 1, . . .). Then from the known asymptotics of Φ as its argument tends to ∞(6.13(3) of
[9]) we deduce that
f(x) ∼
Γ(1 + α)
Γ( 1+α
2
−µ) s−1
2 ( 1+α
2
+µ) x−1
2 −µ e
√sx/2.
(3.6)
Case 2. µ = i + 1+α
2 . Then
Φ(−i, 1 + α, √sx) = Γ(α + 1) i!
Γ(α + i + 1) Lα
i (√sx)
(3.7)
where Lα
i is the generalized Laguerre polynomial (6.9(36) of [9]). So we ﬁnd that in this case
f(x) ∼(−1)i
Γ(α + 1)
Γ(α + i + 1) s
i
2 xi+ α
2 e−√sx/2.
(3.8)
3. The region √s x ≫1, (1 −x) s ≫1
Here we use the standard WKB approximation for the solutions of a diﬀerential equation (p f ′)′ + q f = 0 given
by e±y/(p q)
1
4 where y =
R p
q/p. In the case of our equation (3.3), the range of validity of the approximation is as
indicated in the heading of this section. To be deﬁnite, we take
y = −
Z 1
x
p
q(z)/p(z) dz.
It is easy to compute that for the range in question we have
y = −√s
√
1 −x −µ log x + 2 µ log(1 +
√
1 −x) + o(1).
Also, in this case p q is asymptotically −s/4 times x2(1 −x). Hence
f(x) ∼

a(s) x−µ (1 +
√
1 −x)2µ e−√s√1−x
+b(s) xµ (1 +
√
1 −x)−2µ e
√s√1−x
(3.9)
where a(s) and b(s) are constants depending on s.
14
4. The region x →1
Letting y = 1 −x, f(x) = g(y) gives the approximating equation
(y g(y)′)′ −s
4 g(y) = 0.
The general solution of this is a constant times I0(√y) where I0 is the modiﬁed Bessel function. Thus we deduce that
as x →1
f(x) ∼c(s) I0
p
s(1 −x)

(3.10)
for some c(s).
5. Determination of a(s), b(s) and c(s)
From the asymptotics of I0 at inﬁnity and (3.10) we deduce that
f(x) ∼
c(s)
√
2π s
1
4
e
√s√1−x
(1 −x)
1
4
when x →1 and s(1 −x) →∞. Comparing this with (3.9) shows that a(s) = 0 and that
c(s) ∼
√
2π s
1
4 b(s).
(3.11)
And now comparing (3.9) with (3.6) and (3.8) in their overlapping range of validity we see that we must be in case 2
and that
b(s) ∼(−1)i
Γ(α + 1)
Γ(α + i + 1) 22n+α+1 e−√s.
(3.12)
What we shall need from all this is, ﬁrst, the asymptotics of f(1). This follows immediately from (3.10), (3.11),
(3.12), and the fact that I0(0) = 1:
f(1) ∼(−1)n √
2π
Γ(α + 1)
Γ(α + i + 1) s
i
2 + 1
4 e−√s22n+α+1.
(3.13)
We shall also need the asymptotics of
R
f(x)2dx. It follows from the asymptotics we have derived that the main
contribution to this integral comes from an arbitrarily small neighborhood of x = 0. It follows from (3.5), (3.7) and
the fact
Z ∞
0
xα e−x Lα
i (x)2 dx = Γ(α + i + 1)
i!
that
Z 1
0
f(x)2 dx ∼Γ(α + 1)2 i!
Γ(α + i + 1 s−α
2 −1
2 .
We put these two relations together to get what we really want, which is
f(1)2
R 1
0 f(x)2 dx
∼
2π
Γ(α + i + 1)i! si+ α
2 +1 e−2√s 24i+2α+2.
(3.14)
15
6. The asymptotics of λi
Since L commutes with our integral operator K, rescaled to act on (0, 1), the set {fi} of eigenfunctions corresponding
to the eigenvalues µ0 < µ1 < . . . of L is the set of eigenfunctions of K corresponding to its eigenvalues, in some order.
Lemma 1. The eigenvalues of K are simple.
Proof. Since the eigenvalues of K are the squares of the eigenvalues of J what we have to show is that if f1(x) and
f2(x) are eigenfunctions of L (they need not correspond to any particular µ here) and if for some ν we have either
Z 1
0
Jα(√sxy)fi(y)dy = νfi(x)
(i = 1, 2)
or
Z 1
0
Jα(√sxy)f1(y)dy = νf1(x),
Z 1
0
Jα(√sxy)f2(y)dy = −νf2(x)
then f1 and f2 are linearly dependent. We shall assume them normalized so that they both have the value 1 at x = 1.
Notice ﬁrst that ν̸ = 0 for otherwise if we expand the f1 equation near x = 0 we would ﬁnd that
Z 1
0
x
α
2 +kf1(x)dx = 0,
k = 0, 1, . . .,
and f1 would be identically 0.
Next we deﬁne
H(x) = e−x/2Jα(
√
s e−x), gi(x) = e−x/2fi(e−x),
make the obvious variable changes, and ﬁnd that our relations become
Z ∞
0
H(x + y) gi(y) dy = ν gi(x),
(i = 1, 2),
(3.15)
Z ∞
0
H(x + y) g1(y) dy = ν g1(x),
Z ∞
0
H(x + y) g2(y) dy = −νg2(x).
(3.16)
What comes now is almost identical to the proof of Lemma 1 of [28]. Assuming ﬁrst that (3.15) holds, we diﬀerentiate
twice this relation with i = 1 and then integrate by parts twice to obtain
ν g1(x) = −H′(x) + H(x) g′
1(0) +
Z ∞
0
H(x + y) g1(y) dy.
If we multiply both sides by g2(x) and integrate, using (3.15) and its diﬀerentiated version, we obtain (recall that
gi(0) = 1)
ν
Z ∞
0
g′′
1(x) g2(x) dx = −νg′
2(0) + νg′
1(0) + ν
Z ∞
0
g2(y) g′′
1 (y) dy.
Thus, since ν̸ = 0, we have g′
1(0) = g′
2(0). Equivalently, f ′
1(1) = f ′
2(1). But since also f1(1) = f2(1), it follows from
equation (2) that the corresponding eigenvalues µ must be the same, and so the eigenfunctions are the same.
Next, assume (3.16) holds. Diﬀerentiating both sides of the ﬁrst relation once and integrating by parts give
ν g′
1(x) = −H(x) −
Z ∞
0
H(x + y) g′
1(y) dy.
Multiplying both sides of this by g2(x) and integrating, using the second part of (3.16), we obtain
ν
Z ∞
0
g′
1(x) g2(x) dx = −ν + ν
Z ∞
0
g2(y) g′
1(y) dy,
16
contradicting ν̸ = 0.
Now that we know the eigenvalues λi of K are simple we can order them so that λ0 > λ1 > . . . . There is a
permutation σ of N such that the eigenvalue corresponding to fi is λσ(i). This permutation is independent of s since
the eigenvalues µi and λi both vary continuously with s. The next lemma allows us to compute dλi/ds for each i.
Lemma 2. Let λ be a simple eigenvalue of an integral operator on (0, 1) with symmetric kernel of the form s K(sx, sy)
where K(x, y) is smooth and symmetric. Let f be a corresponding eigenfunction. Then
dλ
ds = λ
s
f(1)2
R 1
0 f(x)2 dx
.
Proof. We may assume f normalized so that
R 1
0 f(x)2dx = 1. Then according to Lemma 3 of [28] we have
dλ
ds =
Z 1
0
Z 1
0
∂
∂s(s K(sx, sy)) f(y) f(x) dy dx.
(This holds no matter what the form of the kernel.) In the case at hand the ﬁrst factor in the integrand equals
K(sx, sy) + (x ∂
∂x + y ∂
∂y)K(sx, sy)
and we easily deduce from this that the integral itself equals
λ
s
Z 1
0
f(x)2dx +
Z 1
0
x f ′(x) f(x) dx +
Z 1
0
y f ′(y) f(y) dy

and integration by parts shows that the expression in parentheses equals f(1)2.
Remark. It is easily seen that the conclusion of the lemma holds when the kernel has a mild singularity at 0 such as
our Besssel kernel has when α < 0.
Lemma 3. For each i we have λi →1 as s →∞.
Proof. The Hankel transform, when rescaled by the variable change x 7→√x, is the integral operator H on (0, ∞) with
kernel 1
2Jα(√xy) and so our operator K on (0, s) may be thought of as Ps H Ps H Ps where Ps denotes the projection
from L2(0, ∞) to L2(0, s). Since, as is well-known, H2 = I, the minimax characterization of the eigenvalues shows
that for each i the eigenvalue of Ps H Ps with i’th largest absolute value tends to ± 1 as s →∞. Since our operator
is the square of this one, the statement of the lemma follows.
We can now deduce the asymptotic formula (15) for the eigenvalues λi. We apply Lemma 2 to the eigenvalue λσ(i)
associated with the eigenfunction fi(x) of (3.3) and use (3.14) to deduce
d log λσ(i)
ds
∼
2π
Γ(α + i + 1) i! si+ α
2 e−2√s 24i+2α+2.
Recalling Lemma 3 we see that we can integrate from s to ∞and we obtain
1 −λσ(i) ∼
2π
Γ(α + i + 1) i! si+ α+1
2
e−2√s 24i+2α+2.
It remains to show that σ(i) = i for all i. But it is clear from the above formula that i < j implies that λσ(i) > λσ(j)
for large s (and so for all s) and therefore σ(i) < σ(j). Since σ : N →N is onto, we must have σ(i) = i for all i.
ACKNOWLEDGMENTS
We wish to thank Professor F. J. Dyson for bringing to our attention the notion of “hard edge” random matrix
ensembles. This work was supported in part by the National Science Foundation, DMS–9001794 and DMS–9216203,
and this support is gratefully acknowledged.
17
[1] E. W. Barnes, The theory of the G-function, Quart. J. Pure and Appl. Math. 31 (1900) 264–314.
[2] E. L. Basor, C. A. Tracy, and H. Widom, Asymptotics of level spacing distributions for random matrices, Phys. Rev. Letts.
69 (1992) 5–8.
[3] M. J. Bowick and E. Br´ezin, Universal scaling of the tail of the density of eigenvalues in random matrix models, Phys.
Letts. B268 (1991) 21–28.
[4] B. V. Bronk, Exponential ensemble for random matrices, J. Math. Phys. 6 (1965) 228–237.
[5] F. J. Dyson, Fredholm determinants and inverse scattering problems, Commun. Math. Phys. 47 (1976) 171–183.
[6] F. J. Dyson, The Coulomb ﬂuid and the ﬁfth Painlev´e transcendent, IASSNSS-HEP-92/43 preprint, to appear in the
proceedings of a conference in honor of C. N. Yang, ed. S.-T. Yau.
[7] A. Edelman, Eigenvalues and Condition Numbers of Random Matrices, SIAM J. Matrix Anal. Appl. 9 (1988) 543–560.
[8] A. Edelman, The distribution and moments of the smallest eigenvalue of a random matrix of Wishart type, Linear Alg.
and Its Appl. 159 (1991) 55–80.
[9] A. Erd´elyi (ed.), Higher Transcendental Functions, Vols. I and II (McGraw-Hill, New York, 1953).
[10] H. Flaschka and A. C. Newell, Monodromy- and Spectrum-Preserving Deformations I, Commun. Math. Phys. 76 (1980)
65–116.
[11] P. J. Forrester, The spectrum edge of random matrix ensembles, preprint.
[12] I. S. Gradshteyn and I. M. Ryzhik, Tables of Integrals, Series, and Products, Corrected and Enlarged Edition (Academic,
San Diego, 1980).
[13] V. I. Gromak, Reducibility of Painlev´e equations, Diﬀ. Urav. 20 (1984) 1674–1683.
[14] M. Jimbo, Monodromy problem and the boundary condition for some Painlev´e equations, Publ. RIMS, Kyoto Univ. 18
(1982) 1137–1161.
[15] M. Jimbo, T. Miwa, Y. Mˆori, and M. Sato, Density matrix of an impenetrable Bose gas and the ﬁfth Painlev´e transcendent,
Physica 1D (1980) 80–158.
[16] R. D. Kamien, H. D. Politzer, and M. B. Wise, Universality of random-matrix predictions for the statistics of energy levels,
Phys. Rev. Letts. 60 (1988) 1995–1998.
[17] G. Mahoux and M. L. Mehta, A method of integration over matrix variables: IV, J. Phys. I France 1 (1991) 1093–1108.
[18] M. L. Mehta, Random Matrices, 2nd edition (Academic, San Diego, 1991).
[19] M. L. Mehta, A non-linear diﬀerential equation and a Fredholm determinant, J. de Phys. I France, 2 (1992) 1721–1729.
[20] M. L. Mehta and G. Mahoux, Level spacing functions and non-linear diﬀerential equations, to appear in J. Phys. I France.
[21] B. M. McCoy, C. A. Tracy, and T. T. Wu, Painlev´e functions of the third kind, 18 (1977) 1058–1092.
[22] G. Moore, Matrix models of 2D gravity and isomonodromic deformation, Prog. Theor. Physics Suppl. No. 102 (1990)
255–285.
[23] T. Nagao and M. Wadati, Correlation functions of random matrix ensembles related to classical orthogonal polynomials,
J. Phys. Soc. Japan 60 (1991) 3298–3322.
[24] L. A. Pastur, On the universality of the level spacing distribution for some ensembles of random matrices, Letts. Math.
Phys. 25 (1992) 259–265.
[25] C. E. Porter, Statistical Theory of Spectra: Fluctuations (Academic, New York, 1965).
[26] M. Sato, T. Miwa, and M. Jimbo, Holonomic quantum ﬁelds, III, IV, Publ. RIMS Kyoto Univ. 15 (1979) 577–629; 15
(1979) 871–972.
[27] C. A. Tracy and H. Widom, Introduction to random matrices, to appear in the proceedings of the 8th Scheveningen
Conference, Springer Lecture Notes in Physics.
[28] C. A. Tracy and H. Widom, Level spacing distributions and the Airy kernel, to appear in Commun. Math. Phys.
[29] H. Widom, The asymptotics of a continuous analogue of orthogonal polynomials, to appear in J. Approx. Th.
[30] T. T. Wu, B. M. McCoy, C. A. Tracy, and E. Barouch, Spin-spin correlation functions for the two-dimensional Ising model:
Exact theory in the scaling region, Phys. Rev. B13 (1976) 316–374.
18
