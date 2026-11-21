---
doc_id: akemann-2022-j-phys-a-math-theor-55-194002
doc_title: "Consecutive level spacings in the chiral Gaussian unitary ensemble: from the hard and soft edge to the bulk"
section_id: sec-002-2-transition-from-bessel--and-airy--to-the-sine
section_title: "Transition from Bessel- and Airy- to the sine-kernel"
section_number: 2
pages: 5-11
source_pdf: Akemann_2022_J._Phys._A__Math._Theor._55_194002.pdf
source_sha256: 3753499c4b23f189
toc_source: outline
doc_brief: "Consecutive level spacings in the chiral Gaussian unitary ensemble: from the hard and soft edge to the bulk — 20 sections: Front matter; Consecutive level spacings in the ; Introduction"
---
The spacing between consecutive eigenvalues of random matrices with unitary symmetry in
the bulk of the spectrum is well-approximated by Wigner’s surmise [1, 11] for 2 × 2 GUE
matrices,
pWigner(s) = 32s2
π2 e−4s2/π.
(1)
We will also give a much more precise expression in appendix A, cf [14], which is universal.
In the present case of the χGUE also called complex Wishart–Laguerre ensemble, deviations
should show up at the hard edge because there the k-point correlation functions differ from the
ones in the bulk of the spectrum.
Before we address this question in terms of the nearest neighbour level spacing distribution
in detail, see section 3, let us investigatethe transition on the level of the kernelof the underlying
limiting determinantal point process, that is the transition from the Bessel-kernel at the hard
edge to the sine-kernel in the bulk. Additionally, we also discuss the transition from the Airy-
kernel at the soft edge to the sine-kernel in the bulk for completeness. Although we do not have
analytical results at the soft edge, we will numerically study this transition for the spacing as
well in section 5.3.
The eigenvalue statistics of the χGUE follows a determinantal point process. This means
the k-point correlation function of the eigenvalues has the form
Rk(x1, . . . , xk) = det [K(xa, xb)]a,b=1,...,k,
(2)
with correlation kernel K(xa, xb). This holds already at finite matrix size, see (48) in section 4,
as well as in the asymptotic scaling limit in the bulk, at the hard and soft edge. For example,
the microscopic level density is given by ρ(x) = R1(x).
The difference between the eigenvalue statistics at different locations in the spectrum can
be seen in the kernel which is the sine-kernel [14] inside the bulk of the spectrum,
Ksine(xa, xb) = sin[π(xa −xb)]
π(xa −xb)
,
(3)
and the Bessel-kernel [29, 30] at the hard edge of the spectrum,
Kν(xa, xb) = √xaxb
xbJν(xa)Jν−1(xb) −xaJν(xb)Jν−1(xa)
x2a −x2
b
,
(4)
where Jν is the Bessel function of the first kind and the index ν counts the number of zero
eigenvalues, measuring the strength of the repulsion from the origin. The Airy-kernel [30, 31]
KAiry(xa, xb) = Ai(xa)Ai′(xb) −Ai′(xa)Ai(xb)
xa −xb
,
(5)
is obtained at the soft edge of the spectrum, with Ai(x) and Ai′(x) the Airy function (of the first
kind) and its first derivative.All three kernels are universal for a broad class of systems and hold
for a much larger class of unitarily invariant ensembles of random matrices than Gaussian, see
the review by Kuijlaars [8, chapter 6]. For an extension to orthogonaland symplectic ensembles
see the book by Deift and Gioev [37].
In principle, all spectral information is contained in the kernels in the respective region of
the spectrum, including the spacing distribution. To assess the latter, one typically uses the gap
4
J. Phys. A: Math. Theor. 55 (2022) 194002
G Akemann et al
probability, the probability P[a,b] that an interval [a, b] does not contain eigenvalues, expressed
in terms of the Fredholm determinant of the corresponding kernel,
P[a,b] = det[1 −K[a,b]],
(6)
where the integral operator is
K[a,b]φ(x) =
 b
a
K(x, y)φ(y)dy,
(7)
for an arbitrary (L2-integrable) test function φ. The spacing distribution then follows by differ-
entiation, as it is explained in more detail in section 3. However, we will not follow this route
of Fredholm determinants and compute the spacing distribution in a different manner.
The second information that can be retrieved from the kernel is the mean level spacing. It
follows from the microscopic level density at large argument, which yields the macroscopic
level density at that point in the spectrum, which gives the inverse mean level spacing. This
quantity is important for the unfolding of the spacing distribution. From the sine-kernel we
have
R1,sine(x) = Ksine(x, x) = 1,
(8)
that is the mean level spacing is already normalised to unity. For the Bessel density we obtain
after using l’Hôpital’s rule
R1,ν(x) = Kν(x, x) = x
2

J2
ν(x) −Jν−1(x)Jν+1(x)
 x→∞
−→1
π ,
(9)
implying that the mean level spacing is π in this normalisation of the Bessel-kernel. We will
come back to this point in section 5. The soft edge is an exception, as here the macroscopic den-
sity vanishes at the point we zoom in. However, also here is it possible to unfold the spectrum
and we refer to [38].
The Bessel-kernel can yield the Airy- as well as the sine-kernel in certain limits, which is
rather expected. For instance, a large index ν pushes the spectral edge away from the origin so
that it becomes a soft edge, see e.g. [39], where this transition is studied on a microscopic level.
This limit is not in our main focus in the present work. On the other hand, when taking the limit
of large arguments in the Bessel-kernel, moving away from the hard edge, the sine-kernel is
obtained. We are interested how much the hard edge statistics differs from the bulk statistics
and will quantify this below in such a large-argument expansion.
To understand how the Bessel- and the sine-kernel are related, one needs to exploit the
following asymptotic expansion of the Bessel function [40, equation (10.17.3)]
Jν(x) =

2
πx

cos

x −π
4 (2ν + 1)

+ O
	1
x

.
(10)
The aim is to asymptotically expand the Bessel-kernel for xa, xb →∞, under the condition
of a fixed difference xa −xb. In the kernel (4), we only encounter the product of two Bessel
functions, such that we consider the asymptotic expansion
Jν(xa)Jν−1(xb) =
1
π√xaxb

(−1)ν cos(xa + xb) + sin(xa −xb) + O
	1
x

.
(11)
5
J. Phys. A: Math. Theor. 55 (2022) 194002
G Akemann et al
Plugging these terms into the kernel, we either have to symmetrise or anti-symmetrise these
terms in xa and xb. Thence, we arrive at the expansion
Kν(xa, xb) = sin(xa −xb)
π(xa −xb) −(−1)ν cos(xa + xb)
π(xa + xb) + O
	 1
x2
a,b

.
(12)
Let us point out that we have taken xa, xb ≫1 to be of the same order. Below we will also
assume that xa + xb ≫|xa −xb|.
The sine-kernel can be easily identified as the first term in (12). The question is whether
the 1/(xa + xb) can be cancelled by an unfolding transformation. For that we underline that,
after unfolding, the bulk level density is simply equal to unity, highlighting the translation
invariance, cf [1]. In the current situation, the level density corresponding to the kernel (12) is
equal to
ρν(x0) = 1
π
	
1 −(−1)ν cos(2x0)
2x0

+ O
	 1
x2
0

.
(13)
We note that we understand xa = x0 + δxa and xb = x0 + δxb, with δxa and δxb being kept
fixed in the asymptotic x0 ≫1. The unfolding works along the formula
ya =
 x0+δxa
x0
ρν(x′)dx′ = 1
π

δxa −(−1)ν sin(2x0 + 2δxa) −sin(2x0)
4x0

+ O
	
δx2
a, 1
x2
0

,
(14)
and ditto for yb and xb = x0 + δxb. This relation is born out of the requirement dya = ρ(x0 +
δxa)dδxa so that the level density in y is ρ(y) = 1, as it is for the sine-kernel. This relation can
be inverted by recursively inserting δxa in the non-linear part, which leads to
δxa = πya + (−1)ν sin(2x0 + 2πya) −sin(2x0)
4x0
+ O
	
δx2
a, 1
x2
0

.
(15)
From the first term we see that in this way we rescale the mean spacing of the Bessel-kernel
from 1/π to unity. Plugging this into (12) and multiplying the kernel with the Jacobian of this
transformation, we eventually arrive at
1
√ρ(x0 + δxa)ρ(x0 + δxb)Kν (x0 + δxa, x0 + δxb)
= Ksine(ya, yb) + (−1)ν
sin[π(ya −yb)]
π(ya −yb)
−sin2[π(ya −yb)]
π2(ya −yb)2
−1

× cos[2x0 + π(ya + yb)]
2x0
+ O
	 1
x2
0

.
(16)
The calculation above shows that indeed the rate of convergence of the Bessel-kernel to the
sine-kernel goes with 1/x0 which is not very fast. Thus, it is rather amazing how close the level
spacing distribution at the hard edge is to the one in the bulk, as we will see in section 5.2.
It looks more like a 1/x2
0 convergence than 1/x0. The reason is that one fixes the distance
s = ya −yb and integrates over the centre of mass ¯y = ya + yb. This strongly suppresses the
pre-factor of the leading correction—it might be equal to zero which we have not checked in
6
J. Phys. A: Math. Theor. 55 (2022) 194002
G Akemann et al
the present work. Indeed, for the two-point correlation function, we obtain
1
ρ(x0 + δxa)ρ(x0 + δxb)R2 (x0 + δxa, x0 + δxb)
= 1 −sin2[π(ya −yb)]
π2(ya −yb)2
−2(−1)ν sin[π(ya −yb)]
π(ya −yb)
×
sin[2π(ya −yb)]
π(ya −yb)
−sin2[π(ya −yb)]
π2(ya −yb)2
−1

× cos[2x0 + π(ya + yb)]
2x0
+ O
	 1
x2
0

.
(17)
When integrating over ¯y = ya + yb as it has to be done for the level spacing distribution, we
see that the leading order correction vanishes,
lim
L→∞
1
2L
 L
−L
d¯y
1
ρ(x0 + δxb)ρ(x0 + δxb)R2 (x0 + δxa, x0 + δxb)
= 1 −sin2[π(ya −yb)]
π2(ya −yb)2
+ O
	 1
x2
0

.
(18)
This heuristic argument works in general for all k-point correlation functions, so that their aver-
age starts from 1/x2
0, and as the level spacing distribution between two consecutive eigenvalues
is described by such an average, see section 3. We expect that this may explain our numerical
observation of a faster convergence of the level spacing distribution from the hard edge to the
bulk limit.
Since the analytical expression which we derive in the ensuing sections are too complicated
to actually see whether this argument regarding the rate of convergence is indeed the case, it
remains an open problem.
Finally, let us briefly describe the limit from the Airy- to the sine-kernel. In the scaling
limit leading to the Airy-kernel (5), the bulk statistics is attained by taking the limit of large
negative arguments. Therefore, we consider arguments xa = −x, xb = −y in (5) and take the
limit x, y →∞. The asymptotic expansion of the Airy function and its derivative read
Ai(−x) =
1
√πx1/4
	
cos(ζ −π/4) + O
	1
ζ

,
ζ = 2
3 x3/2,
(19)
Ai′(−y) = y1/4
√π
	
sin(η −π/4) + O
	1
η

,
η = 2
3y3/2,
(20)
cf [40, equations (9.7.9) and (9.7.10)], respectively. Rather than starting with the unfolded
Airy-kernel [38, equation (VI.16)], we will depart directly from (5) and attain the sine-kernel
through a change of variables. Multiplying out, we have for x, y →∞
KAiry(−x, −y) =
1
2π(x −y)

 y
x
 1
4 +
	 x
y

 1
4 
sin(ζ −η)
+

y
x
 1
4 −
	 x
y

 1
4 
cos(ζ + η) + O
	1
ζ , 1
η


.
(21)
7
J. Phys. A: Math. Theor. 55 (2022) 194002
G Akemann et al
When changing variables from x, y to ζ, η, we need to take into account the Jacobian
(symmetrised in both entries) (2/3)
1
3 (ζη)−1
6 , which needs to be multiplied with the kernel,
KAiry(ζ, η) = 1
3π
⎡
⎣
sin(ζ −η)
(ζη)
1
3

ζ
1
3 −η
1
3
 −
cos(ζ + η)
(ζη)
1
3

ζ
1
3 + η
1
3

⎤
⎦+ O
	 1
ζ2
0

.
(22)
Here, the correction term is to be understood using ζ, η ≈ζ0 ≫1. The first term does note
quite yet look like the sine-kernel. However, an expansion about the base point ζ0 yields the
correct terms,
1
3(ζη)
1
3

ζ
1
3 −η
1
3
 = ζ
2
3 + ζ
1
3 η
1
3 + η
2
3
3(ζη)
1
3 (ζ −η)
≈
1
ζ −η ,
(23)
where only the difference between ζ and η (or powers thereof) is of order unity. Thus, the first
terms of (12) and (22) do agree. The second term, whose prefactor is approximately
1
3(ζη)
1
3

ζ
1
3 + η
1
3
 ≈
1
3ζ
2
3
0 2ζ
1
3
0
=
1
6ζ0
,
(24)
can be absorbed via unfolding using the same route as starting from (12). Thus, we expect the
same rate of convergence from the soft edge to the bulk statistics like at the hard edge.
To highlight and get a feeling how close the two edge statistics are, we need to unfold both.
This is particularly important as it is known [39], that the Bessel-kernel becomes the Airy-
kernel when taking the limit ν →∞, while the edge will be located at x = ν, see [42]. To make
both kernels, especially the Bessel-kernel with its varying parameter ν, comparable, we need
to properly unfold the microscopic spectrum. For the Airy-kernel (5), we have already seen
that the unfolding is given by x = −sgn(λ)(3π|λ|/2)2/3 with λ ∈R. The factor π guarantees
that the mean level spacing is equal to 1, and the minus sign reflects the spectrum at the origin
so that the bulk will be to the right-hand side as it is for the Bessel-kernel. The sign sgn(λ)
of λ has to be dealt with separately, because of the root that has to be taken. Taking the limit
xa, xb →−sgn(λ)(3π|λ|/2)2/3 by applying l’Hopital’s rule, and multiplying the kernel with
the Jacobian [2π2/(3|λ|)]1/3, the unfolded microscopic Airy level density is given by [38]
R(∞)
1,unf(λ) = sgn (λ)
	3π4|λ|
2

1/3
Ai2

−sgn (λ)
3π|λ|
2

2/3
+
	 2π2
3|λ|

1/3
Ai′2

−sgn (λ)
3π|λ|
2

2/3
.
(25)
The superscript ∞indicates that this expression agrees with the properly unfolded Bessel-
kernel density (9) in the limit ν →∞. Evidently there will be a singularity at the origin, which
is a relict of the unfolding and has no deeper meaning, cf, figure 1.
To get the proper unfolding for all ν of the hard edge statistics, we start from the integral
representation of the Bessel function
Jν(x) =
 π
−π
exp[ix sin(ϕ) −iνϕ]dϕ
2π ,
(26)
for an arbitrary integer ν ∈N0. For large x ≫1 and ν ≫1, regardless what kind of relation
they have, it is clear that the saddle point equation gives x cos(ϕ) = ν. This can be only solved
8
J. Phys. A: Math. Theor. 55 (2022) 194002
G Akemann et al
Figure 1. The properly unfolded microscopic level densities of the Bessel-kernel result
(32) for ν = 0 (blue solid curve), ν = 1 (red finely dashed curve), ν = 20 (green
coarsely dashed curve), and ν = ∞(black solid curve). The latter agrees with the
unfolded Airy-kernel result (25) reflected at the origin. As a guideline we have added the
asymptotic unfolded level density, which is equal to the constant 1 (solid black horizon-
tal line) and the half-sided picket fence spectrum (spectrum of the harmonic oscillator),
with eigenvalues at n + 1/2 (dashed horizontal lines). These auxiliary lines indicate the
proper unfolding of the spectra. The singularity at the origin is a relic of the unfolding,
as it is not smooth at the macroscopic (as well as mesoscopic) spectral edge, cf [38].
when x ⩾ν, hinting at the creation of a soft edge. In the regime x ⩾ν, via standard stationary
phase approximation the Bessel function becomes as follows
Jν(x) ≈1
π

2
x
1
(1 −ν2/x2)1/4 cos

x

1 −ν2
x2 −ν arccos
ν
x

−π
4

.
(27)
In particular limits, this agrees with the asymptotic in [39, theorem 1.3]. A simple comparison
with (10) shows that the proper unfolding is equal to
λ = g(x) = 1
π

x

1 −ν2
x2 −ν arccos
ν
x

,
for x ⩾ν.
(28)
As a check, the Taylor expansion gives the behaviour λ ∝(x/ν −1)3/2 in the limit ν/x ≈1,
which is the unfolding of the Airy-kernel. To mimic the sign sgn(λ) that has appeared for the
unfolding of the soft edge statistics, we choose
λ = g(x) = 1
π

x

ν2
x2 −1 −ν arccosh
ν
x

,
when x < ν.
(29)
One can check that g(x) is monotonously increasing on R+. Indeed again a Taylor expansion
about ν/x ≈1 gives the proper unfolding of the soft edge statistics. To invert the relation
between x and λ we have exploited the integral formula
x(λ) =
 ∞
0
Θ[λ −g(˜x)]d˜x,
(30)
9
J. Phys. A: Math. Theor. 55 (2022) 194002
G Akemann et al
where Θ is the Heaviside step function. The Jacobian of this substitution is
dx
dλ(λ) =
⎧
⎪
⎨
⎪
⎩
π

1 −ν2/x2(λ), x(λ) ⩾ν,
π

ν2/x2(λ) −1, x(λ) < ν.
(31)
Thus, the unfolded Bessel-kernel is given by
R(ν)
1,unf(λ) = x(λ)
2

J2
ν(x(λ)) −Jν−1(x(λ))Jν+1(x(λ))
 dx
dλ(λ).
(32)
It indeed satisfies the point-wise limit limν→∞R(ν)
1,unf(λ) = R(∞)
1,unf(λ) for fixed λ, see (25) and
figure 1.
The unfolded microscopic level densities (25) and (32) are illustrated in figure 1. All curves
from ν = 0 to ν = ∞almost perfectly agree, starting from the fourth eigenvalue. Hence we
would not expect a big difference in any of the level spacing distributions. For ν = 20 the
Bessel-kernel seems to agree with the Airy-kernel even from the first eigenvalue, judged with
the bare eye. Hence, we also expect a quick convergence in increasing ν. The biggest deviation
for the level spacing distribution might be seen between the first and second eigenvalue for
ν = 0.
