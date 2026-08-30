---
doc_id: arxiv-1409.0435v2
doc_title: "Asymptotics for Toeplitz determinants: perturbation of symbols with a gap"
section_id: sec-001-introduction
section_title: "Introduction"
section_number: null
pages: 1-18
source_pdf: 1409.0435v2.pdf
source_sha256: 0c6abbb9c5a720d9
doc_brief: "Asymptotics for Toeplitz determinants: perturbation of symbols with a gap — We study the determinants of Toeplitz matrices as the size of the matrices tends to inﬁnity, in the particular case where"
---
We consider Toeplitz determinants of the form
Dn(f) = det(fj−k)j,k=0,...,n−1,
fj = 1
2π
Z 2π
0
f(eiθ)e−ijθdθ,
(1.1)
where the symbol f is given by
f(eiθ) = eW(eiθ) ×
(
1,
for −θ0 ≤θ ≤θ0,
s,
for θ0 < θ < 2π −θ0,
(1.2)
and fk is the k-th Fourier coeﬃcient of f. The symbol depends on the parameters
s ∈[0, 1] and θ0 ∈(0, π), and on a function W(z) which we assume to be analytic in a
neighbourhood of the unit circle. In the simplest case where W(z) = 0, f is piecewise
constant with jump discontinuities at e±iθ0.
For s ∈[0, 1] and θ0 ∈(0, π) ﬁxed, the large n asymptotic behavior for the Toeplitz
determinants Dn(f) = Dn(s, θ0, W) is well understood.
For s = 0, the symbol is
supported on the arc γ = {eiθ : −θ0 ≤θ ≤θ0}. If f is positive on γ and symmetric,
f(eiθ) = f(e−iθ), we have the following asymptotics due to Widom [22],
ln Dn (s = 0, θ0, W) = n2 ln sin θ0
2 + nf
W0 −1
4 ln n
+
∞
X
k=1
kf
Wkf
W−k −1
4 ln cos θ0
2 + 1
12 ln 2 + 3ζ′(−1) + o(1),
as n →∞,
(1.3)
∗Institut de Recherche en Math´ematique et Physique, Universit´e catholique de Louvain, Chemin du
Cyclotron 2, B-1348 Louvain-La-Neuve, BELGIUM
1
arXiv:1409.0435v2  [math-ph]  25 Feb 2015
where f
Wk is the k-th Fourier coeﬃcient of f
W, deﬁned by
f
W(eiθ) = W(e2i arcsin(sin θ0
2 sin θ
2 )),
(1.4)
and where ζ is the Riemann ζ-function. For W = 0, it was shown in [17, 18] that this
result holds not only for 0 < θ0 < π ﬁxed, but also if θ0 approaches π slowly enough
such that n(π −θ0) is large. The error term in (1.3) then becomes O(n−1(π −θ0)−1).
On the other end of the parameter range for s, we have s = 1: here the symbol is
smooth and we have the Szeg˝o asymptotics
ln Dn (s = 1, θ0, W) = nW0 +
∞
X
k=1
kWkW−k + o(1),
as n →∞.
(1.5)
For 0 < s < 1, f has two jump discontinuities which are special cases of Fisher-Hartwig
(FH) singularities. FH singularities are generally characterized by two parameters: α,
which describes a root-type singularity, and β, which describes a jump discontinuity.
Our symbol f has Fisher-Hartwig singularities at e±iθ0 with parameters α = 0 (which
means that there are no root-type singularities) and β = ∓1
2πi log s. Asymptotics for
Toeplitz determinants with Fisher-Hartwig singularities have been studied by many
authors [15, 23, 2, 3, 4, 14, 8, 9]. Applied to our symbol f, the results from, e.g., [8]
imply that, for s ∈(0, 1) ﬁxed, i.e. independent of n, we have
ln Dn (s, θ0, W) = nW0 + (ln s)2
2π2
ln n + ln(2 sin θ0)
2π2
+ ln s
π
+∞
X
k=1
(Wk + W−k) sin(kθ0) +
+∞
X
k=1
kWkW−k
+ 2 ln

G

1 + ln s
2πi

G

1 −ln s
2πi

+ o(1),
(1.6)
as n →∞, where G is Barnes’ G-function.
If we let s tend to 0, the jump discontinuities of f turn into endpoints of the support
of f, and f transforms from a Fisher-Hartwig symbol to an arc-supported symbol on
[−θ0, θ0]. Nevertheless, letting s →0 in (1.6), we do not recover the Widom asymptotics
(1.3). This means that a non-trivial critical transition in the asymptotic behavior for
Dn(s, θ0, W) takes place as s →0. In this paper, we show that the Widom asymptotics
(1.3) extend to the case where s̸ = 0 but s = s(n) →0 suﬃciently rapidly as n →∞.
Theorem 1.1 Let θ0 ∈(0, π) and deﬁne
xc = −2 ln tan θ0
4 .
(1.7)
Let f be of the form (1.2) with W analytic in a neighbourhood of the unit circle. As
n →∞and simultaneously s →0 in such a way that 0 ≤s ≤e−xcn, we have
ln Dn(s, θ0, W) = ln Dn(0, θ0, W) + o(1).
(1.8)
The error term o(1) is uniform for 0 ≤s ≤e−xcn and ϵ ≤θ0 ≤π −ϵ, ϵ > 0, and can
be speciﬁed as
o(1) = O(n−1/2excns).
(1.9)
2
Figure 1: As n →∞, ln Dn(s, θ0, W) follows Widom asymptotics for s = 0, Fisher-
Hartwig asymptotics for s ∈(0, 1) ﬁxed, and Szeg˝o asymptotics for s = 1. Theorem
1.1 implies that the Widom asymptotics remain valid as n →∞with s = s(n) below
the curve s = e−xcn. As n →∞with s = s(n) above the curve, a diﬀerent type of
asymptotic behavior is expected.
In addition, the result extends to the case where θ0 approaches π at a suﬃciently slow
rate: (1.8) holds for ϵ < θ0 < π −M
n with M suﬃciently large and 0 ≤s ≤e−xcn, with
the error term given by
o(1) = O((π −θ0)1/2n−1/2enxcs).
(1.10)
Remark 1.2 We believe the bound s ≤e−xcn is sharp: as n →∞, s →0 with
s > e−xcn, the asymptotic behavior for ln Dn(s, θ0, W) is expected to be described in
terms of elliptic θ-functions. For a heuristic discussion, see Section 5.4.
Remark 1.3 If f is positive on γ and even in θ, the asymptotics for ln Dn(0, θ0, W) in
(1.8) are given by (1.3). The perturbative result (1.8) is valid for general analytic W,
even if the positivity and symmetry conditions needed for the Widom asymptotics do
not hold. Note that the error term o(1) = O((π−θ0)1/2n−1/2enxcs) in (1.8) improves as
θ0 approaches π. This is reasonable since the perturbation of the arc-supported symbol
then takes place on a shrinking arc near −1. For our proof, it is however crucial that
n(π −θ0) is suﬃciently large.
Application 1: the Circular Unitary Ensemble
Consider the Circular Unitary Ensemble (CUE) which is the set of unitary n × n
matrices with the Haar measure. The eigenvalues eiθ1, . . . , eiθn in this ensemble have
the joint probability distribution
1
(2π)nn!
Y
1≤j<k≤n
|eiθj −eiθk|2
n
Y
j=1
dθj,
θ1, . . . , θn ∈[0, 2π).
(1.11)
3
Deﬁne the random variable X = Xθ0 as the number of eigenvalues of a CUE matrix on
the arc γ = {eiθ : −θ0 ≤θ ≤θ0}. The average value of Xθ0 is given by
En(Xθ0) = θ0
π n.
(1.12)
Deﬁne the moment generating function
Fn(λ) = En(eλXθ0).
(1.13)
By (1.11), we can write this as
Fn(λ)
=
1
(2π)nn!
Z
[0,2π]n
Y
1≤j<k≤n
|eiθj −eiθk|2eλXθ0
n
Y
j=1
dθj
(1.14)
=
1
(2π)nn!
Z
[0,2π]n
Y
1≤j<k≤n
|eiθj −eiθk|2
n
Y
j=1
eλχγ(eiθj )dθj,
(1.15)
with χγ the characteristic function of the arc γ.
But using the standard multiple
integral representation for Toeplitz determinants, we obtain
Fn(λ) = enλDn(s = e−λ, θ0, W = 0).
(1.16)
This is an identity for any λ ≥0. The moment generating function Fn(λ) at large
positive values of λ contains statistical information about large deviations where Xθ0 is
much bigger than its average value. As an illustration, a rough estimate of the integral
in (1.15) gives us the inequality
Probn [Xθ0 ≥p] ≤e−pλF(λ) = e(n−p)λDn(e−λ, θ0, 0),
(1.17)
which holds for any λ ≥0 and p ∈{0, 1, . . . , n}. Theorem 1.1 gives asymptotics for
Dn(e−λ, θ0, 0) for λ ≥nxc. For large n, the minimum of the right hand side of (1.17)
in the range λ ≥nxc is attained near
λ = nxc = −2n ln tan θ0
4 .
(1.18)
Substituting this value for λ and the asymptotic behavior for Dn(e−nxc, θ0, 0), we obtain
Probn [Xθ0 ≥p] ≤

tan θ0
4
−2n2+2pn 
sin θ0
2
n2
×
n−1/4

cos θ0
2
−1/4
21/12e3ζ′(−1)(1 + o(1)),
n →∞.
(1.19)
For typical values of p ∼θ0
π n, and even more generally for p < (1 −c)n with
c =
ln sin θ0
2
2 ln tan θ0
4
,
(1.20)
this estimate does not give any useful information since the right hand side is large for
large n. We do get non-trivial information for large deviations from the typical value.
4
If we let p = n −ω(n), we have
Probn [Xθ0 ≥p] ≤

tan θ0
4
−2nω(n) 
sin θ0
2
n2
×
n−1/4

cos θ0
2
−1/4
21/12e3ζ′(−1)(1 + o(1)),
(1.21)
as n →∞, and the right hand side decays whenever ω(n) < cn. If ω(n) = o(n) as
n →∞, we observe that the probability to have at least n −ω(n) eigenvalues on γ can
be estimated by
Probn [Xθ0 ≥n −ω(n)] = O(n−1/4en2φ(θ0)−2nω(n) ln tan θ0
4 ),
as n →∞, (1.22)
where the rate function φ is given by φ(θ0) = ln sin θ0
2 . Note that this is not a large
deviation principle since we only have an asymptotic upper bound for the left hand
side of (1.22). A more detailed analysis of the moment generating function F(λ) may
lead to better estimates, but it is not our aim to proceed in this direction.
Application 2: sine kernel determinants
In the double scaling limit where n →∞and θ0 approaches π at rate O(1/n), the
Toeplitz determinant Dn(s, θ0, 0) converges to the Fredholm determinant of the oper-
ator 1 −(1 −s)Ky, where Ky is the integral operator acting on (−y, y) with kernel
sin π(x−t)
π(x−t) : we have [10, formulas (236)-(241)]
lim
n→∞Dn(s, θ0 = π(1 −2y
n ), 0) = det(1 −(1 −s)Ky),
(1.23)
where the operator Ky is deﬁned by
(Kyg)(x) =
Z y
−y
sin π(x −t)
π(x −t)
g(t)dt.
(1.24)
Asymptotics for the right hand side of (1.23) have been studied by Dyson [13], see also
[10] for a historical review; the double scaling limit where y →∞and simultaneously
s →0 appears to be subtle. As y →∞, s →0 in such a way that s ≤e−2πy, with
c = 1
12 ln 2 + 3ζ′(−1),
(1.25)
we have
ln det(1 −(1 −s)Ky) = −π2y2
2
−1
4 ln πy + c + o(1).
(1.26)
Except for s = 0, (1.26) had not been proved rigorously until the recent paper [6],
where double scaling asymptotics were obtained both for s ≤e−2πy and for s > e−2πy.
The value of the constant (1.25) was also proved in [6].
As a consequence of our Theorem 1.1, we re-derive (1.26) and (1.25). Indeed, by
(1.3), (1.8), and (1.10), we have
ln Dn(s, π(1−2y
n ), 0) = n2 ln cos πy
n −1
4 ln n−1
4 ln sin πy
n +c+O(y1/2
n enxcs)+O(y−1),
5
(1.27)
with the error term uniform for n, y large, y1/2/n small, and
s ≤e−xcn = e2n ln tan θ0
4 = e2n ln tan( π
4 −πy
2n).
(1.28)
The right hand side of (1.28) can be written as e−2πy  1 + O(y2n−1)

for n, y large and
y2/n small.
Now, let us choose an arbitrary small function ϵ(y) > 0 and assume s ≤(1−ϵ(y))e−2πy.
Then for n suﬃciently large, i.e. for n >> y2/ϵ(y), (1.28) holds, and letting n →∞in
(1.27), we obtain
lim
n→∞ln Dn(s, π(1 −2y
n ), 0) = −π2y2
2
−1
4 ln πy + c + O(y−1),
(1.29)
for large y. We thus re-derive (1.26) in the double scaling limit where y →∞, s →0 in
such a way that s ≤(1 −ϵ(y))e−2πy, and we conﬁrm the value of the constant (1.25),
using diﬀerent methods than in [6].
In [6], the double scaling asymptotics y →∞, s →0 such that s ≥e−2πy have also
been considered, and asymptotics for det(1 −(1 −s)Ky) in terms of elliptic θ-functions
were obtained. This is consistent with Remark 1.2 and the discussion in Section 5.4.
Outline
In Section 2, we will derive identities which express
d
ds ln Dn(s, θ0, W) in terms of or-
thogonal polynomials on the unit circle. In Section 3, we will study an equilibrium
problem which is crucial to obtain asymptotics for the orthogonal polynomials. In Sec-
tion 4, we will obtain asymptotics for the orthogonal polynomials as the degree tends
to inﬁnity, via the Riemann-Hilbert (RH) method. An important novel feature in the
RH analysis is the construction of a modiﬁed Bessel parametrix compared to Bessel
parametrices that appeared in the literature before. This modiﬁcation is needed be-
cause s̸ = 0. The asymptotics for the orthogonal polynomials will lead us towards large
n asymptotics for
d
ds ln Dn(s, θ0, W). Integrating the diﬀerential identity will complete
the proof of Theorem 1.1 in Section 5 for θ0 ﬁxed. In addition, we explain how the
proof can be extended to the case where θ0 →π at a suﬃciently slow rate.
2
Diﬀerential identities for Toeplitz determinants
In this section, we derive an identity for
d
ds ln Dn(s, θ0, W) in terms of orthogonal poly-
nomials on the unit circle. Deﬁne φj, bφj, j = 0, 1, 2, . . . as the family of orthogonal
polynomials on the unit circle characterized by
1
2π
Z 2π
0
φk(eiθ) c
φm(e−iθ)f(eiθ)dθ = δkm,
∀k, m ∈N,
(2.1)
where the degree of φj, bφj is j, and their leading coeﬃcients χj are equal and positive.
For general weight functions f(eiθ), it is a standard fact that φn, bφn exist and are
unique if Dn(f), Dn+1(f)̸ = 0 and that they are given by the determinantal formulas
6
[21]
φn(z) =
1
√DnDn+1

f0
f−1
f−2
· · ·
f−n
f1
f0
f−1
· · ·
f−n+1
...
...
...
...
...
fn−1
fn−2
fn−3
· · ·
f−1
1
z
z2
· · ·
zn

,
(2.2)
and
bφn(z) =
1
√DnDn+1

f0
f−1
f−2
· · ·
f−n+1
1
f1
f0
f−1
· · ·
f−n+2
z
...
...
...
...
...
...
fn
fn−1
fn−2
· · ·
f1
zn

,
(2.3)
where Dn = Dn(f) is the Toeplitz determinant deﬁned in (1.1), and where fk is, as
before, the k-th Fourier coeﬃcient of f. If f(eiθ) is positive, Dn(f) > 0 for all n ∈N and
the OPs are well-deﬁned. For complex f, existence and uniqueness of the orthogonal
polynomials is not guaranteed for any n. For f given in (1.2), it will follow from our
analysis that they are well-deﬁned for n suﬃciently large and 0 ≤s ≤e−xcn. If W = 0,
the symbol f is even in θ and positive, which implies that bφk = φk = φk.
From (2.2), we see that the leading coeﬃcient χn of φn is equal to
χn = χn(s, θ0, W) =
s
Dn(s, θ0, W)
Dn+1(s, θ0, W).
We can thus express Dn(s, θ0, W) in terms of the leading coeﬃcients of the OPs if
D0, D1, . . . , Dn̸ = 0:
Dn(s, θ0, W) =
n−1
Y
j=0
χ−2
j .
(2.4)
To obtain an asymptotic formula for Dn(s, θ0, W) from this formula, we would need
information about all OPs of degree 0 up to n −1. To circumvent this problem, we
derive diﬀerential identities for ln Dn(s, θ0, W).
2.1
Diﬀerential identity for general W
For general suﬃciently smooth symbols f(z; s) depending on a parameter s, there exists
an identity for the logarithmic derivative of Dn(f) with respect to s: if Dn−1, Dn, Dn+1̸ =
0, we have [9, Proposition 3.3]
∂s ln Dn(s, θ0, W) =
1
2πi
Z
S1
z−n 
Y −1(z)Y ′(z)

21 ∂sf(z, s)dz,
where S1 is the unit circle in the complex plane,
′ = d
dz, ∂s = d
ds, and
Y (z) =




χ−1
n φn(z)
χ−1
n
Z
S1
φn(w)
w −z
f(w)
2πiwn dw
−χn−1zn−1bφn−1(z−1)
−χn−1
Z
S1
bφn−1(w−1)
w −z
f(w)
2πiwdw



.
(2.5)
7
For our symbol given by (1.2), this formula reduces to
∂s ln Dn(s, θ0, W) =
1
2πi
Z
γc z−n 
Y −1(z)Y ′(z)

21 eW(z)dz,
(2.6)
where γc = S1 \ γ.
2.2
Diﬀerential identity for W = 0
If W = 0, the integral at the right hand side of (2.6) can be simpliﬁed. Although
(2.6) will be suﬃcient for the proof of Theorem 1.1, we will show here how to simplify
the diﬀerential identity if W = 0. This will allow us to give a more elegant proof of
Theorem 1.1 in this case.
Proposition 2.1 Let Dn(s, θ0, 0) be the Toeplitz determinant with symbol (1.2) in the
case where W(eiθ) = 0. We have the following diﬀerential identity for ln Dn:
∂s ln Dn(s, θ0, 0) = −2n∂sχn
χn
+ 2(1 −s)
π
Im

φn(eiθ0)∂sφn(eiθ0)

.
(2.7)
Proof.
Taking the logarithm of both sides in (2.4), and then diﬀerentiating with
respect to s, we get
∂s ln Dn(s, θ0, 0) = −2
n−1
X
j=0
∂sχj
χj
.
On the other hand, by (2.1),
1
2π
Z 2π
0
∂s

φj(eiθ)φj(eiθ)

f(eiθ)dθ = 2∂sχj
χj
,
and this gives
∂s ln Dn(s, θ0, 0) = −1
2π
Z 2π
0
∂s


n−1
X
j=0
φj(eiθ)φj(eiθ)

f(eiθ)dθ.
(2.8)
Here we can use the Christoﬀel-Darboux formula (see e.g. [21, 8] for a proof of it):
n−1
X
j=0
φj(z)φj(z−1) = −nφn(z)φn(z−1) + z

φn(z−1)φ′
n(z) −
 φn(z−1)
′ φn(z)

.
Substituting this into (2.8), we obtain
∂s ln Dn(s, θ0, 0) = 2n∂sχn
χn
−1
2π
Z 2π
0
∂s
h
eiθ 
φn(e−iθ)φ′
n(eiθ) −
 φn(z−1)
′

z=eiθ φn(eiθ)
i
f(eiθ)dθ
= 2n∂sχn
χn
+ I1 + I2 + I3 + I4,
(2.9)
8
where
I1 = −1
2π
Z 2π
0
eiθ∂s

φn(e−iθ)

φ′
n(eiθ)f(eiθ)dθ,
(2.10)
I2 = −1
2π
Z 2π
0
eiθφn(e−iθ)∂s

φ′
n(eiθ)

f(eiθ)dθ,
(2.11)
I3 = 1
2π
Z 2π
0
eiθ∂s
 φn(z−1)
′

z=eiθ

φn(eiθ)f(eiθ)dθ,
(2.12)
I4 = 1
2π
Z 2π
0
eiθ  φn(z−1)
′

z=eiθ ∂sφn(eiθ)f(eiθ)dθ.
(2.13)
From the orthogonality relation (2.1), we easily get
I2 = I3 = −n∂sχn
χn
.
(2.14)
The computation of I1 and I4 is slightly more involved. Using (1.2), we have
I1 = −1
2πi
Z 2π
0
∂s

φn(e−iθ)
 d
dθ

φn(eiθ)

dθ
+ 1 −s
2πi
Z 2π−θ0
θ0
∂s

φn(e−iθ)
 d
dθ

φn(eiθ)

dθ.
(2.15)
Integrating by parts and then using orthogonality, we obtain
I1
=
1 −s
2πi
h
∂s

φn(e−iθ)

φn(eiθ)
i2π−θ0
θ0
+
1
2πi
Z 2π
0
φn(eiθ)∂s
d
dθ

φn(e−iθ)

f(eiθ)dθ
=
1 −s
2πi
h
∂s

φn(e−iθ)

φn(eiθ)
i2π−θ0
θ0
−n∂sχn
χn
.
(2.16)
In the same way, we show that
I4
=
1
2π
Z 2π
0
eiθ  φn(z−1)
′

z=eiθ ∂sφn(eiθ)f(eiθ)dθ
=
−1 −s
2πi
h
φn(e−iθ)∂sφn(eiθ)
i2π−θ0
θ0
−n∂sχn
χn
.
(2.17)
Summing up (2.14), (2.16), and (2.17), and using the fact that φn = φn if W = 0, we
get the result.
2
As a consequence of Proposition 2.1 and (2.5), we can express the right hand side
of (2.7) in terms of Y = Y (n) given by (2.5):
Corollary 2.2 We have
∂s ln Dn(s, θ0, 0) = n∂s ln Y12(0) + 2(1 −s)
π
Im
 
Y11(eiθ0)
p
Y12(0)
∂s
 
Y11(eiθ0)
p
Y12(0)
!!
. (2.18)
Proof.
By (2.5), we have
Y12(0) = χ−2
n ,
Y11(eiθ0) = χ−1
n φn(eiθ0).
Substituting this into (2.7), we get (2.18).
2
9
Integrating both sides from 0 to s0 in (2.6) or (2.7), we obtain
ln Dn(s0, θ0, W) −ln Dn(0, θ0, W) =
Z s0
0
[∂s ln Dn(s, θ0, W)] ds.
(2.19)
In order to obtain asymptotics for ln Dn(s0, θ0, W), we need large n asymptotics for
the right-hand side of (2.6) and (2.7) uniformly for 0 ≤s ≤s0.
To obtain large n asymptotics for Y , we will use the following RH characterization
[16]: Y (z) = Y (n)(z) is the unique 2 × 2 matrix-valued function which satisﬁes the
following properties.
RH problem for Y
(a) Y : C \ S1 →C2×2 is analytic.
(b) Y has the following jumps:
Y+(z) = Y−(z)
1
z−nf(z)
0
1

,
for z ∈S1 \
n
z0 = eiθ0, z0 = e−iθ0o
,
where Y+(z) (Y−(z)) denotes the limit as z is approached from the inside (outside)
of the unit circle.
(c) Y (z) =
 I + O(z−1)
 zn
0
0
z−n

as z →∞.
(d) As z tends to z0 or z tends to z0, Y behaves as
Y (z) =
O(1)
O(ln |z −z0|)
O(1)
O(ln |z −z0|)

as z →z0,
Y (z) =
O(1)
O(ln |z −z0|)
O(1)
O(ln |z −z0|)

as z →z0.
3
Equilibrium measures
It will be convenient to introduce a new parameter x ∈R+ ∪{+∞} deﬁned by
s = e−xn,
(3.1)
such that f can be written as f(eiθ) = eW(eiθ)e−nV (eiθ), where
V (eiθ) =
(
0,
for eiθ ∈γ,
x,
for eiθ ∈S1 \ γ.
(3.2)
An important ingredient for the large n analysis of the orthogonal polynomials and the
RH problem for Y is the following minimization problem: ﬁnd the measure µ = µ(x)
which minimizes
ZZ
log |z −s|−1dµ(z)dµ(s) +
Z
V (z)dµ(z)
(3.3)
among all Borel probability measures on the unit circle S1.
10
This measure, which is unique and absolutely continuous with respect to the Lebesgue
measure, is called the equilibrium measure, is denoted dµ(x) = u(x)(eiθ)dθ, and its sup-
port is denoted J(x). The equilibrium measure µ = µ(x) and its support J = J(x)
are uniquely determined by the following Euler-Lagrange variational conditions [1, 20]:
there exists a real constant ℓ= ℓ(x) such that
2
Z π
−π
log |z −eiθ|dµ(eiθ) −V (z) + ℓ= 0,
for z ∈J,
(3.4)
2
Z π
−π
log |z −eiθ|dµ(eiθ) −V (z) + ℓ≤0,
for z ∈S1 \ J.
(3.5)
The support and density of the equilibrium measure can be computed explicitly.
Proposition 3.1
(a) For x = +∞, the support of the equilibrium measure and its
density are given by
J = J(∞) = γ,
u(eiθ) = u(∞)(eiθ) = 1
2π
r
cos θ + 1
cos θ −cos θ0
.
(3.6)
The constant ℓ= ℓ(∞) in the variational conditions (3.4)-(3.5) is given by
ℓ(∞) = −2 ln sin θ0
2 ,
(3.7)
and the variational inequality (3.5) is strict for z ∈S1 \ γ.
(b) Let xc be given by (1.7). For x ≥xc, we have the same result as for x = +∞:
J = γ ,
u(eiθ) = u(∞)(eiθ),
ℓ= ℓ(∞).
(3.8)
Moreover, the variational inequality (3.5) is strict for z ∈S1 \ γ if x̸ = xc; if
x = xc, it is strict for z ∈S1 \ (γ ∪{−1}), and there is equality for z = −1.
(c) For 0 < x < xc, the support of µ consists of two disjoint arcs: we have
J = {eiθ : θ ∈[−θ0, θ0] ∪[π −θ1, π + θ1]},
(3.9)
where θ1 = θ1(x) ∈(0, π −θ0) is the unique solution of
2
Z
[−θ0,θ0]∪[π−θ1,π+θ1]
log

1 + eiθ
1 −eiθ

 u(eiθ)dθ = x,
(3.10)
and the density is given by
u(eiθ) = 1
2π
r
cos θ + cos θ1
cos θ −cos θ0
.
(3.11)
The constant ℓis given by
ℓ= −
Z 1
0
1
s
 
1 −
s
s2 + 2 cos(θ1)s + 1
s2 −2 cos(θ0)s + 1
!
ds,
(3.12)
and the variational inequality (3.5) is strict for z ∈S1 \ J.
11
Remark 3.2 Although part (c) of the proposition is not needed for the proof of The-
orem 1.1, we present it here for completeness and to support the heuristic arguments
in Section 5.4, where we will discuss asymptotics for Dn if x < xc.
Proof.
Note ﬁrst that the equation (3.10) has indeed a unique solution θ1 for x < xc,
since the function
θ1 7→2
Z
[−θ0,θ0]∪[π−θ1,π+θ1]
log

1 + eiθ
1 −eiθ

 u(eiθ)dθ
decreases as a function of θ1 ∈(0, π −θ0), and is bijective from (0, π −θ0) to (0, xc).
The equilibrium measure µ is uniquely characterized by the conditions (3.4)-(3.5),
which means that it is suﬃcient for us to show that the measure µ deﬁned in cases (a),
(b), and (c) satisfy these variational conditions. To do so, consider the function
f(z) = 2
Z
log |z −eiθ|dµ(x)(eiθ).
(3.13)
If we deﬁne θ1 > 0 as the unique solution of (3.10) if x < xc, and if we let θ1 = 0 for
x ≥xc, we have
f(eiα) = 1
π
Z
[−θ0,θ0]∪[π−θ1,π+θ1]
log |eiα −eiθ|
r
cos θ + cos θ1
cos θ −cos θ0
dθ.
(3.14)
The derivative
d
dαf(eiα) can be written as a contour integral
d
dαf(eiα) = −1
2πi
Z
Σ
1
ξ
ξ + eiα
ξ −eiα
(ξ −z1)(ξ −z1)
(ξ −z0)(ξ −z0)
1/2
dξ,
z1 = eiθ1,
(3.15)
where the square root is analytic oﬀJ and tends to 1 as ξ →∞, and where the contour
Σ consists of one (if x ≥xc) or two (if x < xc) counterclockwise oriented circles around
the arc(s) of J. If eiα ∈S1 \J, the contour has to be chosen suﬃciently small such that
eiα lies in the exterior of Σ.
If eiα ∈J, a residue calculation shows that
d
dαf(eiα) = 0. If eiα ∈S1 \ J on the
other hand, we have
d
dαf(eiα) =





q
cos θ1+cos α
cos θ0−cos α,
if θ0 < α < π −θ1,
−
q
cos θ1+cos α
cos θ0−cos α,
if π + θ1 < α < 2π −θ0.
(3.16)
It follows that f(eiα) is constant on [−θ0, θ0] ∪[π −θ1, π + θ1], and that it achieves its
maximum on [π −θ1, π + θ1] (i.e. at π if x ≥xc). We have
f(eiα) = f(1),
for −θ0 ≤α ≤θ0,
(3.17)
f(eiα) = f(−1),
for π −θ1 ≤α ≤π + θ1,
(3.18)
f(eiα) < f(−1),
for α /∈[π −θ1, π + θ1].
(3.19)
If we show that
f(1) = −ℓ, f(−1) < f(1) + x,
for x > xc,
(3.20)
f(1) = −ℓ, f(−1) = f(1) + x,
for x ≤xc,
(3.21)
12
then (3.17)-(3.19) imply the Euler-Lagrange conditions (3.4)-(3.5).
For the case x ≥xc, using (3.16), we obtain after a straightforward calculation,
f(−1) −f(1) = f(eiπ) −f(eiθ0) =
Z π
θ0
r
1 + cos θ
cos θ0 −cos θdθ = −2 ln tan θ0
4 = xc ≤x,
which proves the inequality in (3.20), and the fact that there is equality at −1 if x = xc.
Moreover, using an other residue calculation, we get
f(1) =
Z 1
0
f′(s)ds =
Z 1
0
1
s
 
1 −
1 + s
p
s2 −2 cos(θ0)s + 1
!
ds = 2 ln sin θ0
2 = −ℓ(∞).
This proves the equality in (3.20). For 0 < x < xc, by (3.16),
f(−1) −f(1) = f(ei(π−θ1)) −f(eiθ0) =
Z π−θ1
θ0
r
cos θ1 + cos θ
cos θ0 −cos θdθ = x,
by deﬁnition of f and θ1, and
f(1) =
Z 1
0
1
s
 
1 −
s
s2 + 2 cos(θ1)s + 1
s2 −2 cos(θ0)s + 1
!
ds = −ℓ.
This completes the proof.
2
4
Riemann-Hilbert analysis for x ≥xc
We will now perform an asymptotic analysis of the RH problem for Y as n →∞with
x ≥xc. Our analysis uses the Deift/Zhou steepest descent method [7, 11, 12] and shows
many similarities with the analysis done in [17] for s = 0 (or x = +∞). An important
diﬀerence is that we need to modify the Bessel parametrices around the points z0, z0,
see Section 4.4 below.
4.1
First transformation Y →T
We deﬁne g by
g(z) =
Z θ0
−θ0
log(z −eiθ)dµ(∞)(eiθ).
(4.1)
Below we write µ = µ(∞), u = u(∞), and ℓ= ℓ(∞). We have that eg is analytic for
z ∈C \ γ, and by the Euler-Lagrange variational conditions (3.4)-(3.5), we also have
g+(z) + g−(z) −log(z) −iπ + ℓ= 0,
for z ∈γ \ {z0, z0},
(4.2)
2g(z) −log(z) −iπ + ℓ< 0,
for z ∈S1 \ γ,
(4.3)
g′
+(z) −g′
−(z) = −2π
z u(z),
for z ∈γ \ {z0, z0}.
(4.4)
Deﬁne
T(z) = e
nπi
2 σ3e
nℓ
2 σ3Y (z)e−ng(z)σ3e−nℓ
2 σ3e−nπi
2 σ3.
(4.5)
Then it is straightforward to check that T satisﬁes the following conditions.
13
RH problem for T
(a) T : C \ S1 →C2×2 is analytic.
(b) T satisﬁes the jump relation
T+(z) = T−(z)JT (z),
on S1 \ {z0, z0} ,
(4.6)
with
JT (z) =
 
e−n(g+(z)−g−(z))
(−1)nz−ne−nV (z)enℓen(g+(z)+g−(z))eW(z)
0
en(g+(z)−g−(z))
!
.
(c) T(z) = I + O(z−1) as z →∞.
(d) As z →z0 = eiθ0 or z →z0 = e−iθ0, we have
T(z) =
O(1)
O(ln |z −z0|)
O(1)
O(ln |z −z0|)

,
as z →z0,
T(z) =
O(1)
O(ln |z −z0|)
O(1)
O(ln |z −z0|)

,
as z →z0.
We deﬁne
φ(z) = 2g(z) −log z −iπ + ℓ,
(4.7)
so that eφ is analytic in a neighborhood of γ with the exception of γ itself. For z ∈
γ \ {z0, z0}, we have
φ+(z)
=
(g+(z) + g−(z) −log z −iπ + ℓ) + (g+(z) −g−(z))
(4.8)
=
g+(z) −g−(z),
(4.9)
by (4.2).
But g+(z0) = g−(z0), and integrating (4.4) between z0 and z, and then
substituting it into (4.8), we obtain
φ+(z) = −2π
Z z
z0
u(ξ)
ξ
dξ.
(4.10)
Analytically continuing the left and right hand side, we obtain
φ(z) =
Z z
z0
ξ + 1
((ξ −z0)(ξ −z0))1/2
dξ
ξ ,
(4.11)
where the branch cut of the square root is chosen on γ. It is now convenient to express
JT in terms of φ:
JT (z) =











 
e−nφ+(z)
eW(z)
0
e−nφ−(z)
!
,
z ∈γ \ {z0, z0},
 
1
e−nxenφ(z)eW(z)
0
1
!
,
z ∈S1 \ γ.
14
z0
γ
γ+
γ−
γc
z0
Figure 2: The jump contour for S.
4.2
Second transformation T →S
We can factorize JT on γ as follows:
e−nφ+(z)
eW(z)
0
e−nφ−(z)

=

1
0
e−nφ−(z)e−W(z)
1

×

0
eW(z)
−e−W(z)
0
 
1
0
e−nφ+(z)e−W(z)
1

.
(4.12)
Using this factorization, we can split the jump on γ into three diﬀerent jumps on a
lens-shaped oriented contour, see Figure 2. It is important that the jump contour lies
in the region where W is analytic. Denote by γ+ and γ−the lenses around γ on the
|z| < 1 side and the |z| > 1 side respectively. Deﬁne
S(z) =

















T(z)

1
0
−e−nφ(z)e−W(z)
1

,
|z| < 1, z inside the lenses around γ,
T(z)

1
0
e−nφ(z)e−W(z)
1

,
|z| > 1, z inside the lenses around γ,
T(z),
z outside the lenses.
(4.13)
Then S solves the following RH problem.
RH problem for S
(a) S : C \ (S1 ∪γ−∪γ+) →C2×2 is analytic.
(b) S satisﬁes the jump relations
S+(z) = S−(z)JS(z),
for z ∈S1 ∪γ−∪γ+,
(4.14)
where S+ (S−) denotes the boundary value from the left (right) of the contour,
15
and where
JS(z) =





















 
1
e−nxenφ(z)eW(z)
0
1
!
,
for z ∈S1 \ γ,
 
0
e−W(z)
−e−W(z)
0
!
,
for z ∈γ \ {z0, z0},
 
1
0
e−nφ(z)e−W(z)
1
!
,
for z ∈γ+ ∪γ−.
(4.15)
(c) S(z) = I + O(z−1) as z →∞.
(d) As z →z0 = eiθ0 or z →z0 = e−iθ0, we have
S(z) = O(ln |z −z0|),
S(z) = O(ln |z −z0|).
(4.16)
By (4.7) and (4.3), we observe that the jump matrices for S converge to the iden-
tity matrix on S1 \ γ as n →∞, except at −1 if x = xc. On γ+ ∪γ−, one shows
that Re φ(z) > 0 and consequently the jump matrices for S also converge to the
identity matrix on γ+ ∪γ−. The convergence of the jump matrices is point-wise in
z and breaks down as z approaches z0, z0, and also as z approaches −1 if x = xc.
Therefore, we will need to construct approximations to S for large n in diﬀerent
regions of the complex plane: local parametrices will be constructed in small disks
D(z0, r), D(z0, r), D(−1, r) surrounding z0, z0, −1, and a global parametrix will be con-
structed in C \ (D(z0, r) ∪D(z0, r) ∪D(−1, r)).
4.3
Global parametrix
Ignoring the exponentially small jumps for S and small neighborhoods of z0, z0, −1, we
are led to the following RH problem:
RH problem for P (∞)
(a) P (∞) : C \ γ →C2×2 is analytic.
(b) P (∞) has the jump
P (∞)
+
(z) = P (∞)
−
(z)

0
eW(z)
−e−W(z)
0

,
z ∈γ \ {z0, z0}.
(4.17)
(c) P (∞)(z) = I + O(z−1) as z →∞.
(d) As z →z0 or z →z0, we have
P (∞)(z) = O(|z −z0|−1/4),
P (∞)(z) = O(|z −z0|−1/4).
(4.18)
The solution of this RHP is explicitly given by
P (∞)(z) = eh∞σ3
 1
2
 β(z) + β−1(z)

−1
2i
 β(z) −β−1(z)

1
2i
 β(z) −β−1(z)

1
2
 β(z) + β−1(z)


e−h(z)σ3,
(4.19)
16
γc
γ+ γ
γ−
z0
∂D(z0, r)
Figure 3: The jump contour for P.
where β(z) =

z−z0
z−z0
1/4
is analytic in C \ γ and β(z) →1 as z →∞, where h∞=
limz→∞h(z), and
h(z) = ((z −z0)(z −z0))1/2
2πi
Z
γ
W(ξ)
((ξ −z0)(ξ −z0))1/2
+
1
ξ −z dξ,
(4.20)
with ((z −z0)(z −z0))1/2 analytic oﬀγ. Note that h is analytic in C \ γ, bounded near
z0, z0, and ∞, and that it satisﬁes the jump relation
h+(z) + h−(z) = W(z),
z ∈γ \ {z0, z0}.
Using these properties, it is straightforward to verify that P (∞) solves the above RH
problem.
4.4
Local parametrix near z0
We want to construct a function P deﬁned in D(z0, r) satisfying the following RH
conditions.
RH problem for P
(a) P : D(z0, r) \ (S1 ∪γ+ ∪γ−) →C2×2 is analytic.
(b) For z on the contour shown in Figure 3, P satisﬁes the jump conditions
P+(z) = P−(z)

0
eW(z)
−e−W(z)
0

,
on γ \ {z0, z0},
P+(z) = P−(z)

1
en(φ(z)−x)eW(z)
0
1

,
on γc,
P+(z) = P−(z)

1
0
e−nφ(z)e−W(z)
1

,
on γ−∪γ+.
(4.21)
(c) For z ∈∂D(z0, r), we have
P(z) =
 I + O(n−1)

P (∞)(z),
as n →∞.
(4.22)
17
(d) As z tend to z0, the behaviour of P is
P(z) = O(ln |z −z0|).
(4.23)
4.4.1
Bessel model RH problem
We will construct P in terms of a model RH problem for which the solution is con-
structed using Bessel functions. Consider the following model RH problem:
RH problem for Ψ
(a) Ψ : C \ ΣΨ →C2×2 is analytic, where ΣΨ = R−∪{xe± 2π
3 i : x ∈R+}, with the
orientation from ∞towards 0 for the three half-lines.
(b) Ψ satisﬁes the jump conditions
Ψ+(ζ) = Ψ−(ζ)
 0
1
−1
0

,
ζ ∈R−,
Ψ+(ζ) = Ψ−(ζ)
1
0
1
1

,
ζ ∈{xe
2π
3 i : x ∈R+},
Ψ+(ζ) = Ψ−(ζ)
1
0
1
1

,
ζ ∈{xe−2π
3 i : x ∈R+}.
(c) Ψ(ζ) =

2πζ
1
2
−σ3
2
1
√
2
1
i
i
1
 
I + O(ζ−1
2 )

e2ζ
1
2 σ3,
as ζ →∞, ζ /∈ΣΨ.
(d) As ζ tend to 0, the behaviour of Ψ(ζ) is
Ψ(ζ) = O(ln |ζ|).
(4.24)
This model RH problem is well-known and it can be solved explicitly using Bessel
functions, see e.g. [19, 17]. The unique solution to this RH problem is given by
Ψ(ζ) =

























 
I0(2ζ
1
2 )
i
πK0(2ζ
1
2 )
2πiζ
1
