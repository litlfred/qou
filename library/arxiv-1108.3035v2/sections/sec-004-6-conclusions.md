---
doc_id: arxiv-1108.3035v2
doc_title: "Random Matrix Theory for the Hermitian Wilson Dirac Operator and the chGUE – GUE Transition"
section_id: sec-004-6-conclusions
section_title: "Conclusions"
section_number: 6
pages: 18-27
source_pdf: 1108.3035v2.pdf
source_sha256: 935bf1bd3e13821b
doc_brief: "Random Matrix Theory for the Hermitian Wilson Dirac Operator and the chGUE – GUE Transition — We introduce a random two-matrix model interpolating between a chiral Hermitian (2n + ν) × (2n+ν) matrix"
---
In this paper we have introduced a parameter dependent Gaussian random two-matrix model that
interpolates between the chGUE (a = 0) and the GUE (a = 1) symmetry class (possibly shifted by
a constant matrix). At the same time this model describes the spectral properties of the Hermitian
Wilson Dirac operator when we take the microscopic weakly non-chiral limit at the origin.
Here
the rescaled parameter ˆa ∼a√n is interpreted as the eﬀect of ﬁnite lattice spacing. It is properly
incorporated in a continuum eﬀective ﬁeld theory as Wilson chiral Perturbation theory in the epsilon
regime to order O(ˆa2).
We have completely determined all spectral k-point density correlation functions when starting
from a chGUE of size (2n + ν) with ν = 0 or ν = 1 exact zero modes, both for ﬁnite n and in the
microscopic large-n origin limit at weak non-chirality. They are given in terms of the Pfaﬃan of a
2 × 2 matrix kernel, containing three individual kernels as building blocks. Each kernel is expressed
as a sum over skew-orthogonal polynomials (and their integral transforms) depending on ν = 0 or
1, which we explicitly constructed in terms of Gaussian integrals over Laguerre polynomials. In the
large-n limit these 3 respective kernels contain in their ﬁnal form a ﬁxed number of 2 up to 4 Gaussian
integrals over modiﬁed Bessel functions, respectively. The Pfaﬃan of the matrix kernel is thus easily
evaluated for any k-point function.
Let us compare to what is known in the literature. In [20, 21] the supersymmetric method was used
to compute the microscopic spectral density (k = 1) directly from the chiral Lagrangian for arbitrary
ν, the so-called index. In [26] this was extended to include one (Nf = 1) extra quark determinant.
This method rapidly becomes cumbersome when adding more ﬂavours Nf > 1 or increasing k, as the
number of integrations increases with the dimension of the auxiliary supermatrix from the Hubbard-
Stratonovich transformation.
This problem was partly circumvented in [27] by using the graded
supereigenvalue method, where explicit examples where provided for the density k = 1 up to Nf = 2,
and for the two-point density k = 2 quenched.
However, also here it is diﬃcult to establish the
Pfaﬃan structure of the k-point functions, and thus the number of integrals grows with k and Nf for
the k-point density correlation function (for recent progress see however [36]).
It is an open problem how to include both Nf > 0 and ν > 1 in our skew-orthogonal polynomial
method, in particular the latter, as the joint probability distribution of eigenvalues which we computed
here for the general Nf and ν case is no longer a simple Pfaﬃan of a single block matrix for ν > 0.
The reason for attempting this problem in the future is not only an independent conﬁrmation for the
aforementioned analytical results which are mainly for k = 1. The extension to arbitrary k is crucial
if we want to get a hand on individual eigenvalue distributions at least in a perturbative expansion
18
(see e.g. [9]), apart from the conceptual aspect of integrability of our two-matrix model. Furthermore,
in all works [20, 21, 26, 27] also the density of real eigenvalues of the complex non-Hermitian Wil-
son Dirac operator was considered. The extension to this operator is another challenge to our method.
Acknowledgments: It is a pleasure to thank P. Damgaard, M. Kieburg, K. Splittorﬀ, and J.
Verbaarschot for collaborations on related topics and many discussions. The Niels Bohr Institute
and Niels Bohr International Academy are thanked (G.A.) for hospitality and partial ﬁnancial sup-
port when this work was initiated. This work was partially supported by the Japan Society for the
Promotion of Science (KAKENHI 20540372) (T.N.).
A
Equivalence to the partition function of WchPT
In this appendix we show the equivalence of our matrix model in the microscopic limit to WchPT in
the epsilon regime, as it was displayed in eq. (2.7). For non-degenerate parameters we have
Z(Nf )
ν
∼
Z
dAdBdWdΩ
Nf
Y
f=1
det
 (zf + mf)11n + A
W + Ω
W † + Ω†
(zf −mf)11n+ν + B

e
−
1
2(1−a2)Tr(W W †)
×e−
1
4a2 Tr(A2+B2+2ΩΩ†) .
(A.1)
Deﬁning z±
f ≡zf±mf we now express the determinants as integrals over Nf sets of complex Grassmann
variables ηf
i , i = 1, . . . , n and ψf
b , b = 1, . . . , n + ν,
Nf
Y
f=1
det[. . .]
=
Z
d2ηd2ψeη∗f
i
(z+
f δij+Aij)ηf
j +ψ∗f
b
(W †
bj+Ω†
bj)ηf
i +η∗f
i
(Wib+Ωib)ψf
b +ψ∗f
c
(z−
f δcb+Bcb)ψf
b , (A.2)
using summation conventions in all indices.
A completion of the squares and integration of the
Gaussian matrices yields
Z(Nf )
ν
∼
Z
d2ηd2ψ ez+
f η∗f
i
ηf
i +z−
f ψ∗f
b
ψf
b −a2
(η∗f
i
ηf
i )2+(ψ∗f
b
ψf
b )2
−2ψ∗f
b
ψf
b η∗g
i
ηg
i
=
Z
dQ1dQ2dT det[Z+ −i
√
2(aQ1 + T †)]n det[Z−−i
√
2(aQ2 + T)]n+νe−Tr(TT †+Q2
1+Q2
2) .
(A.3)
Here we have introduced two Hermitian matrices Q1,2 and one complex non-Hermitian matrix T
of size Nf × Nf to do the Hubbard-Stratonovich transformation.
Integrating out all Grassmann
variables yields an exact expression containing the diagonal matrices Z± with elements z±
f (up to
some constant prefactors that we dropped). If we parametrise T = UR with U unitary and R positive
deﬁnite Hermitian the saddle point is taken at R ∼11Nf
√n when we employ the scaling of masses and
a indicated in eq. (2.9). We obtain
lim
n→∞Z(Nf )
ν
∼
Z
dQ1dQ2
Z
dU det[U]νe
i
2Tr( ˆZ+U+ ˆZ−U†)+
√
2ˆa2Tr(Q1U+Q2U†)−1
2Tr(Q2
1+Q2
2)
∼
Z
dU det[U]ν exp
h1
2Tr( ˆ
M(U + U †)) + 1
2Tr( ˆZ(U −U †)) −ˆa2Tr(U 2 + U † 2)
i
,(A.4)
after integrating out the matrices Q1,2 and performing a further rotation U →iU, U † →−iU †. Eq.
(A.4) is the partition function of WchPT in the epsilon regime for non-degenerate masses, hence we
have completed our claimed proof.
19
A.1
Alternative representation of Nf = 1 WchPT
Finally we would like to make the equivalence between the Nf = 1 ﬂavour partition function for the
large-N limit of our even polynomials R2n(x) explicit. The reason why we present this check in detail
is that we require a slightly diﬀerent form from the one given in [20] eq. (13), or in [21] eq. (151) (for
ˆz = 0 there):
Z(Nf =1)
ν
( ˆm, ˆz, ˆa)
=
e−2ˆa2 Z π
−π
dθ
2π eiθν exp[ ˆm cos(θ) + iˆz sin(θ) + 4ˆa2 sin2(θ)]
=
e−2ˆa2 Z π
−π
dθ
2π eiθν
Z ∞
−∞
dx
√πe−x2 exp[ ˆm cos(θ) + iˆz sin(θ) −4xˆa sin(θ)] , (A.5)
where after using a trigonometric identity we have linearised the sine-squared term instead. We can
now use the following identity [37] for generic matrices A, B
Z
U(Nf )
det[U]ν exp
1
2Tr(AU + BU †)

= 2Nf (Nf −1)/2
Nf −1
Y
j=1
j!
det[B]
det[A]
ν/2 det[µj−1
i
Iν+j−1(µi)]
∆Nf({µ2})
,
(A.6)
with µ2
i being the eigenvalues of the product matrix AB. Specifying to U = eiθ ∈U(1) and identifying
A = ˆm + ˆz + 4ixˆa, B = ˆm −(ˆz + 4ixˆa) we arrive at
Z(Nf =1)
ν
( ˆm, ˆz, ˆa) = e−2ˆa2 Z ∞
−∞
dx
√πe−x2  ˆm −(ˆz + 4ixˆa)
ˆm + ˆz + 4ixˆa
ν/2
Iν
p
ˆm2 −(ˆz + 4ixˆa)2

,
(A.7)
which agrees perfectly with eq. (5.3), see also eq. (99) in [27].
B
Consistency checks of the partition function and factorisation
In this appendix we perform a few consistency checks of the eigenvalue representation of the partition
function eq. (3.15). For simplicity we will set m = 0 and Nf = 0 here. The antisymmetric weight eq.
(3.16) thus reduces to
F(x)|m=0 = 2 e
x2(1−a2)
8a2
erf
x
√
1 −a2
2
√
2a2

.
(B.1)
B.1
The GUE limit a →1 for ν = 0
On the level of the distribution eq. (2.2) it is clear that the matrix W gets suppressed for a →1.
After reducing to eigenvalues the same result should come out. Here we will look at the simplest case
only, that is ν = 0. We can insert the simpliﬁcation eq. (B.1) into eq. (3.17) at ν = 0. Noting that in
the limit a →1 the exponential factor in eq. (B.1) reduces to unity, we can use the following result of
[28] (see end of section 3 in the ﬁrst paper) for the limit of a Pfaﬃan of an error-function,
lim
a→1 Pf1≤i,j≤2n
"
erf
 
(di −dj)
r
(1 −a2)
8a2
!#
∼∆2n({d}) .
(B.2)
This provides the second Vandermonde determinant in eq. (3.17) to constitute the GUE, and we
arrive at
lim
a→1 Z(Nf =0)
ν=0
|m=0 ∼
Z ∞
−∞
N
Y
j=1
ddj dNf
j
exp
h
−
d2
j
4
i
∆N({d})2 .
(B.3)
20
B.2
The chGUE limit a →0 and factorisation
Here we would like to perform a more detailed check. As it was shown in [21] in the large-N limit
the spectral density of the Hermitian Wilson Dirac operator behaves like the density of a ﬁnite GUE-
matrix of size ν×ν plus the microscopic chGUE density. We therefore expect that our general partition
function will factorise in the limit a →0 into a ﬁnite GUE times a second chGUE partition function
of the remaining 2n eigenvalues.
In order to show that we will ﬁrst simplify Z(0)
ν
further before using the de Bruijn integration
theorem. Taking eq. (3.13) as a starting point we can use the fact that the jpdf integrated over all
variables is totally symmetric under exchange or relabeling of the dj 4. We can split the variables
into two sets, denoted by tj=1,...,ν ≡dj=1,...,ν, and sj=1,...,2n ≡dj=ν+1,...,2n+ν. If we do a Laplace
expansion of the determinant into blocks of sizes 2n × 2n and ν × ν, we can split oﬀa Vandermonde
type determinant in the variables tj, after appropriately relabeling all other permutations:
Z(0)
ν
∼
Z ∞
−∞
ν
Y
j=1
dtj e−
t2
j
4a2 ∆ν({t})
Z ∞
−∞
2n
Y
j=1
dsj e−
s2
j
4a2
νY
i=1
(sj −ti) ∆2n({s})
(B.4)
×
Z ∞
0
n
Y
b=1
dube
−u2
b
2a2(1−a2)

e
s1u1
2a2 . . . e
s1un
2a2
e−s1u1
2a2 . . . e−s1un
2a2
· · ·
· · ·
e
s2nu1
2a2 . . . e
s2nun
2a2
e−s2nu1
2a2 . . . e−s2nun
2a2

1
t1
· · ·
tν−1
1
· · ·
· · ·
· · ·
· · ·
1
tν
· · ·
tν−1
ν

.
We can now perform the integrations over u1, . . . , un with the help of the standard de Bruijn inte-
gral formula eq. (3.14). To make it applicable we can simply multiply the weight factors into the
determinant, and we obtain the following result:
Z(0)
ν
∼
Z ∞
−∞
ν
Y
j=1
dtj e−
t2
j
4a2 ∆ν({t})2
Z ∞
−∞
2n
Y
j=1
dsj e−
s2
j
4a2
ν
Y
i=1
(sj −ti)∆2n({s})Pf1≤i,j≤2n [F(si −sj)].(B.5)
In eq. (B.5) we can make further use of the symmetry under relabeling of the variables sj and the
anti-symmetry of the Vandermonde determinant to write the Pfaﬃan as the following product:
Z(0)
ν
∼
Z ∞
−∞
ν
Y
j=1
dtj e−
t2
j
4a2 ∆ν({t})2
Z ∞
−∞
2n
Y
j=1
dsj e−
s2
j
4a2
ν
Y
i=1
(sj −ti) ∆2n({s})
n
Y
k=1
F(s2k −s2k−1). (B.6)
Now consider the exponents of two consecutive variables, say s1 and s2, from the Gaussian and the
exponential part of F:
exp
h
−s2
1 + s2
2
4a2
+ (s2 −s1)2(1 −a2)
8a2
i
= exp
h
−(s1 + s2)2
8a2
−(s1 −s2)2
8
i
.
(B.7)
In the limit a →0 the ﬁrst term on the right hand side will give a delta-function, whereas the second
Gaussian term remains:
lim
a→0
√
8a2π exp
h
−(s1 + s2)2
8a2
−(s1 −s2)2
8
i
= δ(s1 + s2) e−s2
1/2 .
(B.8)
In the same limit the error-function in eq. (B.1) becomes the sign function (see e.g. [28]),
lim
a→0 erf
h
(s2 −s1)
r
(1 −a2)
8a2
i
= sign[s2 −s1] .
(B.9)
4Using this symmetry our manipulations from now on will not be valid in general for correlation functions.
21
We are now ready to take the limit a →0 of the partition function eq. (B.6). We ﬁrst formally
change variables rj = tj/a to isolate the a-dependence, and then take the limit only on the remaining
a-dependence, that is the variables rj,
lim
a→0 Z(0)
ν
∼
Z ∞
−∞
νY
j=1
drj e−
r2
j
4 ∆ν({r})2
Z ∞
−∞
n
Y
j=1
dsj sjsign[sj] exp
h
−
s2
j
2
i νY
i=1
(s2
j −a2r2
i ) ∆n({s2})2.
(B.10)
We have used the fact that for s2k →−s2k−1 we obtain ∆2n({s}) →Qn
i=1 2si ∆n({s2})2. The variables
rj thus act as mass terms to the s-variables, but to leading order these masses can be neglected, leading
to a complete decoupling of variables. Our ﬁnal result is thus reading
Z ∞
−∞
νY
j=1
drj exp
h
−
r2
j
4
i
∆ν({r})2
Z ∞
−∞
n
Y
j=1
dsj |sj|2ν+1 exp
h
−
s2
j
2
i
∆n({s2})2,
(B.11)
where the ν would-be zero-eigenvalues at a = 0 have decoupled into a GUE of size ν, times the
standard massless chGUE with exactly ν zero eigenvalues. However, we should remember that due to
rescaling the original variables tj are all of the order O(a).
It is clear how to this order of approximation the microscopic spectral density would look like:
it is the superposition of a ﬁnite-ν semi-circle from the GUE and the Bessel spectral density with
ν zero-eigenvalues from the chGUE. This conﬁrms the analysis of [21] on the level of the partition
function, to that order.
C
Skew-orthogonal polynomials
In this appendix we compute the skew-orthogonal polynomials given in eqs. (4.6) for ν = 0. We
ﬁrst recall that the expectation value of a single characteristic polynomial (or equivalently the Nf =
1 partition function) gives the even polynomials R2j where we follow the argument of [38].
This
expectation value is computed using the supersymmetric method in the next subsection C.1. Based
on that the odd polynomials R2j+1 then follow as shown in C.2.
Starting from the quenched partition function eq. (3.17) for ν = 0
Z(0)
0
=
Z ∞
−∞
2n
Y
j=1
dsjw(sj) ∆2n({s}) Pf1≤i,j≤2n[F(si −sj)] ,
(C.1)
we can write the expectation value of a single determinant as follows:
⟨det[z −/D5]⟩2n
=
1
Z(0)
0
Z ∞
−∞
2n
Y
j=1
dsjw(sj)(z −sj) ∆2n({s}) Pf1≤i,j≤2n[F(si −sj)]
=
1
Z(0)
0
(2n)!
2nn!
Z ∞
−∞
N
Y
j=1
dsjw(sj) ∆2n+1({s}, z)
n
Y
l=1
F(s2l −s2l−1).
(C.2)
Here we have used the fact that both the Vandermonde determinant and the Pfaﬃan are antisym-
metric in order to simplify their product (times the symmetric integral over all eigenvalues), cf. [29]
Appendix 25. Furthermore we have included the determinant into a larger Vandermonde. Writing the
Vandermonde determinant in terms of even and odd monic polynomials Φ2i and Ψ2i+1 respectively,
∆2n+1({s}, z) =
det
i=0,...,n−1;j=1,...,2n+1
h
{Φ2i(sj), Ψ2i+1(sj)} Φ2n(sj)
i
,
(C.3)
22
and relabeling z = s2n+1, we have from the generalised de Bruijn formula (cf. [38] eq. (4.9), or [34])
⟨det[z −/D5]⟩2n =
n!
Z(0)
0
Pf0≤i,j≤2n


⟨ϕi, ϕj⟩
. . .
ϕ0(s2n+1)
. . .
· · ·
ϕ2n(s2n+1)
−ϕ0(s2n+1) . . .
−ϕ2n(s2n+1)
0

,
(C.4)
for the set of all monic polynomials ϕi = {Φ0, Ψ1, Φ2, Ψ3, · · · , Φ2n}, with the scalar product deﬁned
in eq. (4.9). Choosing polynomials ϕj = Rj to satisfy the skew-orthogonality eq. (4.8) we obtained
the desired relation
R2n(z) = ⟨det[z −/D5]⟩2n = ⟨det[z + /D5]⟩2n ,
(C.5)
which obviously has parity.
C.1
Expectation value of a single characteristic polynomial
We now compute the expectation value of a single characteristic polynomial eq.
(C.5) using the
supersymmetric method for ﬁnite-N. As we have shown already this yields the subset of the even
skew-orthogonal polynomials R2n(x) from which the odd polynomials are constructed. At the same
time this also gives the one ﬂavour partition function, which we can compare to the known result from
Wilson chiral perturbation theory [20] in the large-N limit as a consistency check.
The calculation we present here for ν ≥0 is slightly more general than needed in eq. (4.6). Using
the deﬁnitions (2.1) and (2.11) for the Hermitian matrices A and B of sizes n×n and (n+ν)×(n+ν)
as well as matrices W, Ωof sizes n × (n + ν) with weights eqs. (2.2) we have for N = 2n + ν
⟨det[z + /D5]⟩N
=
1
Z(0)
0
Z
dAdBdWdΩdet
 (z + m)11n + A
W + Ω
W † + Ω†
(z −m)11n+ν + B

e
−
1
2(1−a2)Tr(W W †)
×e−
1
4a2 Tr(A2+B2+2ΩΩ†)
(C.6)
Expressing the determinant through integrals over complex Grassmann variables ηi, i = 1, . . . , n and
ψb, b = 1, . . . , n + ν,
det[. . .]
=
Z
d2ηd2ψeη∗
i ((z+m)δij+Aij)ηj+ψ∗
b (W †
bj+Ω†
bj)ηi+η∗
i (Wib+Ωib)ψb+ψ∗
c ((z−m)δcb+Bcb)ψb , (C.7)
we obtain the following result after performing the Gaussian integrals over the matrices A, B, W, Ω:
⟨det[z + /D5]⟩N
∼
Z
d2ηd2ψ e(z+m)η∗
i ηi+(z−m)ψ∗
b ψb−a2((η∗
i ηi)2+(ψ∗
b ψb)2)−2ψ∗
b ψbη∗
i ηi
=
Z
d2ηd2ψ
Z ∞
−∞
dt
Z
C
d2u
π e−t2−|u|2 exp[(z + m −2iat)η∗
j ηj + (z + m −2iat)ψ∗
b ψb]
× exp[−i
p
2(1 −a2)(uη∗
j ηj + u∗ψ∗
bψb)]
=
Z ∞
−∞
dt
Z
C
d2u
π e−t2−|u|2
z + m + 2iat + i
p
2(1 −a2)u
n
×

z −m + 2iat + i
p
2(1 −a2)u∗n+ν
.
(C.8)
In the second step we have linearised upon using one real and one complex variable in our Hubbard-
Stratonovich transformation. As a last step we use the following integral representation for generalised
Laguerre polynomials Lν
n(x) [39]
Z
C
d2u
π e−|u|2(iu + γ)n(iu∗+ λ)n+ν = (−)nλνL(ν)
n (λγ) ,
(C.9)
23
to obtain
⟨det[z + /D5]⟩N
=
n! (2(1 −a2))n+ ν
2
(−)n√π
Z ∞
−∞
dt e−t2z + 2iat −m
p
2(1 −a2)
ν
L(ν)
n
(z + 2iat)2 −m2
2(1 −a2)

.(C.10)
Here we have put the correct normalisation coeﬃcient that can be read oﬀfrom ⟨det[z + /D5]⟩N =
zN + O(zN−1) for large z. For ν = 0 this reduces to the result given in eq. (4.6). It can be easily seen
that in the microscopic limit eq. (5.1) using eq. (5.2) this reduces to the Nf = 1 ﬂavour partition
function eq. (A.7)
C.2
The odd polynomials R2j+1(x)
In this subsection we construct the odd set of skew orthogonal polynomials directly from the even
ones by diﬀerentiation. Instead we could have computed the R2j+1(x) again from the supersymmetric
method as in the previous subsection, using the relation [38] R2n+1(x) = ⟨det[x −/D5](x + Tr /D5)⟩2n.
Based on our result above eq. (C.10) for ν = 0 R2n(x) = ⟨det[x −/D5]⟩2n we deﬁne
R2j+1(x)
≡
−2a2w(x)−1 d
dx
h
w(x)R2j(x)
i
,
(C.11)
w(x)
≡
exp[−x2/(4a2)] .
(C.12)
In the following we will show by direct computation that these satisfy the skew-orthogonality relations
eq. (4.8) with respect to the scalar product
⟨h, g⟩
=
Z
dxdy w(x)w(y)F(x −y)h(y)g(x) ,
(C.13)
F(x)
=
e
x2(1−a2)
8a2
"
erf
x
√
1 −a2
√
8a2
+
m
p
2a2(1 −a2)

+ erf
x
√
1 −a2
√
8a2
−
m
p
2a2(1 −a2)
#
.
Because the polynomials obviously have parity, Rj(−x) = (−)jRj(x), and because the weight is
antisymmetric, F(−x) = −F(x), it holds
⟨R2j, R2l⟩= 0 = ⟨R2j+1, R2l+1⟩.
(C.14)
Furthermore, the even polynomials are skew-orthogonal to all polynomials of lower degree, as can be
seen from eq. (C.4),
⟨R2j, R2l+1⟩= 0 , for j > l.
(C.15)
It remains to investigate the remaining cases. For j < l we have
⟨R2j, R2l+1⟩
=
−2a2
Z
dxdyw(y)F(x −y)R2j(y) d
dx
h
w(x)R2l(x)
i
=
−2a2
Z
dxdyw(x)w(y)dF(x −y)
dy
R2j(y)R2l(x)
=
2a2
Z
dxdyw(x)F(x −y)R2l(x) d
dy
h
w(y)R2j(y)
i
= 0 .
(C.16)
After a ﬁrst integration by parts with respect to x we have used dF (x−y)
dx
= −dF (x−y)
dy
, and a second
integration by parts with respect to y yields zero after using eq. (C.15).
24
It remains to compute the only nonvanishing product for j = l:
⟨R2j, R2j+1⟩
=
2a2
Z
dxdyw(x)w(y)dF(x −y)
dx
R2j(y)R2l(x)
=
Z
dxdyw(x)w(y)1 −a2
2
(x −y)F(x −y)R2j(y)R2l(x)
+
r
2a2(1 −a2)
π
e
−
m2
2a2(1−a2)
Z
dxdyw(x)w(y)

e
m(x−y)
2a2
+ e
−m(x−y)
2a2

R2j(y)R2l(x)
=
a2(1 −a2)
Z
dxdy
dw(x)
dx
w(y) −w(x)dw(y)
dy

F(x −y)R2j(x)R2j(y)
+2
r
2a2(1 −a2)
π
e
−
m2
2(1−a2)
Z
dxw(x −m)R2j(x)
Z
dyw(y + m)R2j(y) .
(C.17)
In the ﬁrst step we simply integrate by parts. We then observe that the ﬁrst line in the last equation
is proportional to ⟨R2j, R2j+1⟩because when the derivatives also act on the polynomials R2j(x) and
R2j(y) this gives zero as the polynomials R2j are skew-orthogonal to all lower order polynomials.
Putting this term on the left hand side and using parity we obtain
a2⟨R2j, R2j+1⟩= 2
r
2a2(1 −a2)
π
e
−
m2
2(1−a2)
Z
dxw(x −m)R2j(x)
2
.
(C.18)
In a last step we have to evaluate the integral over the weighted even polynomials. Using eq. (C.10)
we have
Z
dxw(x −m)R2j(x)
=
j! (2(1 −a2))j
(−)j√π
Z ∞
−∞
dx e−(x−m)2
4a2
Z ∞
−∞
dt e−t2Lj
(x + 2iat)2 −m2
2(1 −a2)

=
j! (2(1 −a2))j
(−)j√π
1
2a
Z ∞
−∞
dxds e−s2+x2
4a2 Lj
x2 + 2isx −s2 + 2m(x + is)
2(1 −a2)

=
j! (2(1 −a2))j
(−)j√π
2aπ .
(C.19)
In the last but one line we can change to complex coordinates z = x+is and to an integration over the
full complex plane. Because of the argument of Ln(z(z + 2m)/2(1 −a2)) the angular integration will
give zero for all powers of the argument z, except for the constant term z0 which is unity, Ln(0) = 1.
Collecting all factors we thus obtain
rj = ⟨R2j, R2j+1⟩= 8
√
2π a 22j(j!)2(1 −a2)2j+ 1
2 e
−
m2
2(1−a2) .
(C.20)
References
[1] E. V. Shuryak and J. J. M. Verbaarschot, Nucl. Phys. A 560, 306 (1993) [hep-th/9212088].
[2] J. J. M. Verbaarschot and I. Zahed, Phys. Rev. Lett. 70, 3852 (1993) [hep-th/9303012];
J. J. M. Verbaarschot, Phys. Rev. Lett. 72, 2531 (1994) [hep-th/9401059].
[3] J. J. M. Verbaarschot, “Applications of Random Matrix Theory to QCD”, chapter 32 in The
Oxford Handbook of Random Matrix Theory, Oxford University Press, Oxford (2011), Eds. G.
Akemann, J. Baik, and P. Di Francesco [arXiv:0910.4134];
P. H. Damgaard, “Chiral Random Matrix Theory and Chiral Perturbation Theory”, Lectures at
the XIV Mexican School on Particles and Fields 2010, arXiv:1102.1295v1 [hep-ph].
25
[4] G. Akemann, P. H. Damgaard, U. Magnea and S. Nishigaki, Nucl. Phys. B 487, 721 (1997)
[hep-th/9609174];
E. Kanzieper and V. Freilikher, Phil. Mag. B 77, 1161 (1998) [cond-mat/9704149v1];
A.B.J. Kuijlaars and M. Vanlessen, Commun. Math. Phys. 243 (2003) 163 [math-ph/0305044].
[5] P. H. Damgaard and S. M. Nishigaki, Nucl. Phys. B 518, 495 (1998) [hep-th/9711023].
[6] T. Wilke, T. Guhr, and T. Wettig, Phys. Rev. D 57, 6486 (1998) [hep-th/9711057].
[7] S. M. Nishigaki,
P. H. Damgaard,
and T. Wettig,
Phys. Rev. D 58, 087704 (1998)
[hep-th/9803007];
P. H. Damgaard and S. M. Nishigaki, Phys. Rev. D 63, 045012 (2001) [hep-th/0006111].
[8] T. Nagao and P. J. Forrester, Nucl. Phys. B 509, 561 (1998).
[9] G. Akemann and P. H. Damgaard, Phys. Lett. B 583, 199 (2004) [hep-th/0311171].
[10] P. H. Damgaard, J. C. Osborn, D. Toublan and J. J. M. Verbaarschot, Nucl. Phys. B 547, 305
(1999) [hep-th/9811212];
D. Toublan and J. J. M. Verbaarschot, Nucl. Phys. B 603, 343 (2001) [hep-th/0012144];
K. Splittorﬀand J. J. M. Verbaarschot, Phys. Rev. Lett. 90, 041601 (2003) [cond-mat/0209594];
Nucl. Phys. B 683, 467 (2004) [hep-th/0310271]; Nucl. Phys. B 695, 84 (2004) [hep-th/0402177];
Y. V. Fyodorov and G. Akemann, JETP Lett. 77, 438 (2003) [Pisma Zh. Eksp. Teor. Fiz. 77,
513 (2003)] [cond-mat/0210647];
F. Basile and G. Akemann, JHEP 0712, 043 (2007) [arXiv:0710.0376 [hep-th]].
[11] J. Gasser and H. Leutwyler, Phys. Lett. B 184, 83 (1987) .
[12] G. Akemann, F. Basile, and L. Lellouch, JHEP 0812 , 069 (2008) [arXiv:0804.3809 [hep-lat]];
P. H. Damgaard, T. DeGrand and H. Fukaya, JHEP 0712, 060 (2007) [arXiv:0711.0167 [hep-lat]].
[13] P. H. Damgaard and H. Fukaya, JHEP 0901 , 052 (2009) [arXiv:0812.2797 [hep-lat]].
[14] C. Lehner, J. Bloch, S. Hashimoto, and T. Wettig JHEP 05, 115 (2011) [arXiv:1101.5576v2
[hep-lat]].
[15] G. Akemann, J. C. Osborn, K. Splittorﬀ, and J.J.M. Verbaarschot Nucl. Phys. B 712, 287 (2005)
[hep-th/0411030].
[16] P. H. Damgaard, U. M. Heller, K. Splittorﬀ, and B. Svetitsky, Phys. Rev. D 72 , 091501 (2005)
[hep-lat/0508029].
[17] G. Akemann, P. H. Damgaard, J. C. Osborn and K. Splittorﬀ, Nucl. Phys. B 766, 34 (2007);
Erratum-ibid. B 800, 406 (2008) [hep-th/0609059].
[18] R. G. Edwards, U. M. Heller, J. E. Kiskis, and R. Narayanan, Phys. Rev. Lett. 82, 4188
(1999)[hep-th/9902117].
[19] H. Fukaya et al. [JLQCD and TWQCD collaborations], Phys. Rev. D 83, 074501 (2011)
[arXiv:1012.4052 [hep-lat]].
[20] P. H. Damgaard, K. Splittorﬀand J. J. M. Verbaarschot, Phys. Rev. Lett. 105, 162002 (2010).
[arXiv:1001.2937 [hep-th]].
26
[21] G. Akemann, P. H. Damgaard, K. Splittorﬀ, and J. J. M. Verbaarschot, Phys. Rev. D 83, 085014
(2011) [arXiv:1012.0752v2 [hep-lat]].
[22] M. Goltermann, “Applications of chiral perturbation theory to lattice QCD”, Lectures at Les
Houches School ”Modern perspectives in lattice QCD” 2009 arXiv:0912.4042v4 [hep-lat];
S. R. Sharpe, “Applications of Chiral Perturbation theory to lattice QCD”, Lectures at ILFTN
Workshop ”Perspectives in Lattice QCD” 2005 hep-lat/0607016v2.
[23] S. R. Sharpe, Phys. Rev. D 74, 014512 (2006) [hep-lat/0606002].
[24] A. Shindler, Phys. Lett. B 672, 82 (2009) [arXiv:0812.2251 [hep-lat]];
O. B¨ar, S. Necco, and S. Schaefer, JHEP 0903, 006 (2009) [arXiv:0812.2403 [hep-lat]].
[25] S. Necco, A. Shindler, JHEP 1104 , 031 (2011) [arXiv:1101.1778 [hep-lat]].
[26] G. Akemann, P. H. Damgaard, K. Splittorﬀ, and J. J. M. Verbaarschot, Proceedings of the XXVIII
International Symposium on Lattice Field Theory, PoS (Lattice 2010) 079 [arXiv:1011.5121v1
[hep-lat]].
[27] K. Splittorﬀand J. J. M. Verbaarschot, arXiv:1105.6229v1 [hep-lat].
[28] A. Pandey and M. L. Mehta, Commun. Math. Phys. 87, 449 (1983);
M. L. Mehta and A. Pandey, J. Phys. A: Math. Gen. 16 2655 (1983).
[29] M. L. Mehta, Random Matrices, Academic Press, Third Edition, London (2004).
[30] P. J. Forrester, T. Nagao, and G. Honner, Nucl. Phys. B 553, 601 (1999) [cond-mat/9811142v1];
M. Katori and H. Tanemura, Probab. Th. Rel. Fields 138, 113 (2007) [arXiv:math/0506187].
[31] Harish–Chandra, Am. J. Math. 79 (1957) 87;
C. Itzykson and J. B. Zuber, J. Math. Phys. 21, 411 (1980).
[32] T. Nagao and P. Forrester, Nucl. Phys. B 530 [PM] (1998), 742; Nucl. Phys. B 563, 547 (1999);
T. Nagao, Nucl. Phys. B 602, 622 (2001); J. Stat. Phys. 129, 1137 (2007) [arXiv:0708.2036[math-
ph]].
[33] E. Br´ezin and S. Hikami, Phys. Rev. E 57, 4140 (1998) [cond-mat/9804023v1].
[34] M. Kieburg and T. Guhr, J. Phys. A: Math. Theor. 43, 075201 (2010) [arXiv:0912.0654].
[35] I. S. Gradshteyn and I. M. Ryzhik, Table of Integrals, Series, and Products, Academic Press,
Sixth Edition, SanDiego (2000).
[36] M. Kieburg and J. J. M. Verbaarschot, private communication.
[37] B. Schlittgen and T. Wettig, J. Phys. A: Math. Gen. 36, 3195 (2003) [math-ph/0209030v2].
[38] G. Akemann, M. Kieburg, and M. J. Phillips, J. Phys.
A: Math. Theor. 43, 375207 (2010)
[arXiv:1005.2983v2 [math-ph]].
[39] G. Akemann, M. J. Phillips, and H.-J. Sommers, J. Phys. A: Math. Theor. 42, 012001 (2009)
[arXiv:0810.1458v1 [math-ph]].
27
