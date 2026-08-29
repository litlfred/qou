---
doc_id: arxiv-cond-mat-9811142v1
doc_title: "Correlations for the orthogonal-unitary and symplectic-unitary transitions at the hard and soft edges"
section_id: sec-001-introduction
section_title: "Introduction"
section_number: null
pages: 1-6
source_pdf: 9811142v1.pdf
source_sha256: 8666ebc040336b14
doc_brief: "Correlations for the orthogonal-unitary and symplectic-unitary transitions at the hard and soft edges — For the orthogonal-unitary and symplectic-unitary transitions in random matrix the- ory, the"
---
Random matrix ensembles for quantum Hamiltonians are deﬁned in terms of the con-
straint imposed on the general Hermitian matrix representing the Hamiltonian by time
reversal symmetry and spin-rotation invariance (when relevant). This leads to ten distinct
random matrix ensembles [1]. The corresponding eigenvalue probability density function
(p.d.f.) can be computed exactly when the independent elements are chosen to have a
Gaussian distribution. One then ﬁnds that the ten distinct random matrix ensembles
belong to one of six diﬀerent eigenvalue p.d.f.’s. These are
1
CN
N
Y
l=1
e−βx2
l /2
Y
1≤j<k≤N
|xk −xj|β
(1.1)
1
which deﬁnes the Gaussian random matrix ensemble, or
1
C′
N
N
Y
l=1
e−βx2
l /2xβa+1
l
Y
1≤j<k≤N
|x2
k −x2
j|β,
xl > 0
(1.2)
which deﬁnes the Laguerre random matrix ensemble, where β = 1, 2 or 4.
The study of these random matrix ensembles can be generalized to include a parameter
τ. This allows the situation to be studied in which the system evolves between two distinct
eigenvalue p.d.f.’s as τ is varied.
For the Gaussian ensemble this can be achieved by
choosing the joint distribution of the elements of the random matrix to be
P(X(0); X; τ) = Aβ,τ exp

−βTr
n
(X −e−τX(0))2o
/2|1 −e−2τ|

.
(1.3)
In this expression X is a real symmetric (β = 1), Hermitian (β = 2) or self dual quaternion
(β = 4) N × N matrix, and X(0) is a prescribed random matrix which must belong to a
subspace of the symmetry class of X. For τ →∞the p.d.f. is independent of X(0) and
is that of the standard Gaussian ensembles, with p.d.f. (1.1). For general τ Dyson [2]
proved that the eigenvalue p.d.f. p = p(x1, . . . , xN; τ) satisﬁes the Fokker-Planck equation
∂p
∂τ = Lp,
L = 1
β
N
X
j=1
∂
∂xj
e−βW ∂
∂xj
eβW
(1.4)
with
W = W (H) = 1
2
N
X
j=1
x2
j −
X
1≤j<k≤N
log |xk −xj|
(1.5)
(the superscript (H) is used because of a connection with the Hermite polynomials),
subject to the initial condition that p agrees with the eigenvalue p.d.f. of X(0) at τ = 0.
For the Laguerre ensemble, a parameter dependent theory can be developed (see
e.g. [3]) by considering the non-negative matrices A = X†X, where X is an n × m
parameter-dependent matrix
P(X(0); X; τ) = Aβ,τ exp

−βTr
n
(X −e−τX(0))†(X −e−τX(0))
o
/2|1 −e−2τ|

(1.6)
(c.f. (1.3)) and the elements of X are real (β = 1), complex (β = 2) or quaternion real
(β = 4), and X(0) is a prescribed random matrix which must belong to a subspace of the
symmetry class of X. For τ →∞the corresponding p.d.f. for the square of the eigenvalues
of A is given by (1.2) with a = n −m + 1 −2/β, while for general τ the eigenvalue p.d.f.
p = p(x2
1, . . . , x2
N; τ) satisﬁes (1.4) with
W = W (L) = 1
2
N
X
j=1
x2
j −(a + 1/β)
N
X
j=1
log xj −
X
1≤j<k≤N
log |x2
k −x2
j|
(1.7)
(the superscript (L) is used because of a connection with the Laguerre polynomials).
Associated with the parameter dependent eigenvalue p.d.f.’s are parameter dependent
distribution functions
ρ(n+m)(x(1)
1 , . . . , x(1)
n ; τ1; x(2)
1 , . . . , x(2)
m ; τ2)
(1.8)
2
The distribution function ρ(n+m) is deﬁned such that the ratio
ρ(n+m)(x(1)
1 , . . . , x(1)
n ; τ1; x(2)
1 , . . . , x(2)
m ; τ2)/ρ(n+(m−1))(x(1)
1 , . . . , x(1)
n ; τ1; x(2), . . . , x(2)
m−1; τ2)
gives the density of eigenvalues at x(2)
m when the parameter equals τ2, given that there
were eigenvalues at x(1)
1 , . . . , x(1)
n
when the parameter equalled τ1, and that there are also
eigenvalues at x(2)
1 , . . . , x(2)
m with parameter τ2 (it is assumed τ2 > τ1).
For the parameter dependent Gaussian and Laguerre ensembles, quaternion determi-
nant expressions have been derived for ρ(n+m) in the case that β = 2 in (1.4) and initial
condition proportional to e−β′W with β′ = 1 and 4 [7]. Because each β corresponds to
a diﬀerent symmetry class of the Hamiltonian (orthogonal, unitary and symplectic sym-
metry for β = 1, 2 and 4 respectively), this describes the transition from orthogonal or
symplectic symmetry to unitary symmetry as the parameter τ is varied from 0 to ∞.
The determinant expressions apply for the ﬁnite system. As revised in Section 2, they
involve skew orthogonal polynomials known from the study of the distribution functions
for τ = 0 in the β = 1 and 4 cases [5, 6], the orthogonal polynomials related to the
τ = 0, β = 2 case, as well as the elements of a connection matrix which speciﬁes the
orthogonal polynomials in terms of the appropriate skew orthogonal polynomials.
In
the Gaussian case, this matrix can be written down from knowledge of the expression
for the skew orthogonal polynomials in terms of the orthogonal polynomials (the Hermite
polynomials). In the Laguerre case this step requires some calculation which is undertaken
below.
Once all these quantities are speciﬁed, the general (n+ m)-point distribution function
in the ﬁnite system is known explicitly. The immediate task is to compute the scaled
thermodynamic limit. This is done in Section 3 for the Laguerre ensemble in the neigh-
bourhood of the hard edge (the smallest eigenvalues, which are constrained to be positive),
and in Section 4 for the Gaussian ensemble in the neighbourhood of the soft edge (the
largest eigenvalues).
In Section 5 inter-relationships between the distribution functions are discussed. This
is done by analyzing certain limits in (1.8): the limit τ1, τ2 →∞, τ1 −τ2 ﬁxed; the
a →∞limit of the hard edge; and the bulk limit corresponding to large distances
from the edge. Also considered is the asymptotic form of the dynamical density-density
function ρT
(1+1)(X, Y ; t), which is shown to exhibit a universal non-oscillatory decay for
X, Y, t →∞. A consequence of this decay is an O(1) ﬂuctuation formula for the variance
of a slowly varying linear statistic. In the ﬁnal subsections a realization of the density
at the soft edge for β = 1 initial conditions is given by an empirical computation based
on the parameter dependent matrices (1.3) with X(0) a real symmetric matrix, and the
explicit form of the static distribution functions at the hard and soft edges for β = 1 and
4 is noted.
In the Appendix it is shown how our results for the Laguerre ensemble with N ﬁnite
coincide, in the static limit τ →0, with formulas given recently by Widom [8].
3
2
Revision of the formalism
At the special coupling β = 2, the Fokker-Planck equation (1.4) with W given by (1.5) or
(1.7) can be transformed into an imaginary-time Schr¨odinger equation for N independent
fermions (see e.g. [3]). As such the exact N-body Green function G({x(0)
j }, {xj}; τ) can
be written as a determinant involving the corresponding single particle Green functions.
In terms of the new variable yj = xj in (1.1) and yj = x2
j in (1.2) we have previously
shown [4] that
G(x(0)
1 , · · ·, x(0)
N ; x1, · · · , xN; τ)dx1 · · ·dxN = G(y(0)
1 , · · · , y(0)
N ; y1, · · ·, yN; τ)dy1 · · · dyN (2.1)
where
G(y(0)
1 , · · · , y(0)
N ; y1, · · · , yN; τ)
=
eE0τ/2
N
Y
j=1
v
u
u
t w(yj)
w(y(0)
j )
Y
1≤j<k≤N
(yk −yj)
(y(0)
k
−y(0)
j )
det[g(y(0)
j , yk; τ)]j,k=1,···,N
(2.2)
Here
g(y(0), y; τ) =
q
w(y(0))w(y)
∞
X
j=0
pj(y(0))pj(y)e−γjτ
(2.3)
and {pj(x)} are the orthonormal polynomials associated with the weight function w(x).
In the Gaussian case
w(y) = e−y2, pn(y) = 2−n/2π−1/4(n!)−1/2Hn(y),
γn = n + 1
2,
(2.4)
where Hn(y) denotes the Hermite polynomial, while for the Laguerre ensemble
w(y) = yae−y,
pn(y) = (−1)n
Γ(n + 1)
Γ(a + n + 1)
1/2La
n(y),
γn = 2(n + a + 1
2
)
(2.5)
where La
n(y) denotes the Laguerre polynomial. The factor eE0τ/2 cancels out the formula
for the distribution function, so the explicit value of E0 is not needed.
Knowledge of the Green function allows the p.d.f.
p(y(1)
1 , · · ·, y(2)
N ; τ1; y(2)
1 , · · · , y(2)
N ; τ2)
for the event that there are eigenvalues at y(1)
1 , . . . , y(1)
N when the parameter equals τ1, and
at y(2)
1 , . . . , y(2)
N when the parameter is increased to τ2 to be calculated. Explicitly
p(y(1)
1 , · · · , y(2)
N ; τ1; y(2)
1 , · · ·, y(2)
N ; τ2)
= 1
N!
Z
I′ dy(0)
1 · · ·
Z
I′ dy(0)
N p0(y(0)
1 , · · · , y(0)
N )G(y(0)
1 , · · · , y(0)
N ; y(1)
1 , · · ·, y(1)
N ; τ1)
×G(y(1)
1 , · · · , y(1)
N ; y(2)
1 , · · ·, y(2)
N ; τ2 −τ1).
(2.6)
Here p0 denotes the prescribed initial p.d.f. (in the y variables) and I′ denotes the trans-
formed domain (for convenience this will be omitted from subsequent formulas). Initial
4
p.d.f.’s with orthogonal (β = 1) and symplectic (β = 4) symmetry are given by the
functional forms
p0(y1, · · ·, yN) ∝



QN
j=1
q
w(yj) QN
j<l |yj −yl|,
β = 1
QN/2
j=1 w(yj)δ(yj −yj+N/2) QN/2
j<l |yj −yl|4,
β = 4
(N even),
(2.7)
The parameter dependent distribution function ρ(n+m) is calculated from the p.d.f. (2.6)
according to the formula
ρ(n+m)(y(1)
1 , · · ·, y(1)
N ; τ1; y(2)
1 , · · · , y(2)
N ; τ2) =
N!
(N −n)!
N!
(N −m)!
×
Z
dy(1)
n+1 · · ·
Z
dy(1)
N
Z
dy(2)
m+1 · · ·
Z
dy(2)
N p(y(1)
1 , · · · , y(2)
N ; τ1; y(2)
1 , · · ·, y(2)
N ; τ2) (2.8)
In a recent work [7] we have shown that for initial conditions (2.7), and G speciﬁed
by (2.2) with general weight function w(y) and corresponding orthogonal polynomials
{pk(y)}k=0,1,... , the quantity (2.8) can be expressed as a (n + m)-dimensional quaternion
determinant Tdet (this quantity, which was introduced into random matrix theory by
Dyson [9], is explicitly deﬁned in e.g. [4]).
The entries of the quaternion determinant depend on the functions
S(x, y; τx, τy),
˜I(x, y; τx, τy),
D(x, y; τx, τy).
These functions in turn depend on the quantity F(x, y; τ), which is deﬁned for the β = 1
initial conditions in (2.7) by
F(x, y; τ) =
Z
dz′
Z z′
dz

g(x, z; τ)g(y, z′; τ) −g(y, z; τ)g(x, z′; τ)

,
(2.9)
while for the β = 4 initial conditions in (2.7) it is speciﬁed by
F(x, y; τ) =
Z
dz{g(x, z; τ) ∂
∂z g(y, z; τ) −g(y, z; τ) ∂
∂zg(x, z; τ)}.
(2.10)
They also depend on a family of skew-orthogonal monic polynomials Rk(x; τ) of degree
k.
The terminology skew-orthogonal means that they satisfy the skew orthogonality
relations
< R2m(·; τ), R2n+1(·; τ) >= −< R2n+1(·; τ), R2m(·; τ) >= rm(τ)δm,n,
< R2m(·; τ), R2n(·; τ) >= 0,
< R2m+1(·; τ), R2n+1(·; τ) >= 0
(2.11)
where
< f(x), g(y) >= 1
2
Z
dx
Z
dy
q
w(x)w(y)F(y, x; τ)

f(y)g(x) −f(x)g(y)

.
(2.12)
The polynomials Rk(x; τ) can be deduced from their static counterparts [10, 4]. Suppose
at τ = 0 we write
Rn(x; 0) =
n
X
j=0
αnjCj(x),
αnn = 1,
(2.13)
5
where the Cj(x) are the monic version of the orthogonal polynomials pj(x) in (2.3). Then
it is straightforward to verify that
Rn(x; τ)eγnτ =
n
X
j=0
αnjCj(x)eγjτ
(2.14)
and
rk(τ) = rk(0)e−(γ2k+γ2k+1)τ
(2.15)
Still another function involved is
Φk(x; τ) :=
Z
F(y, x; τ)
q
w(y)Rk(y; τ) dy.
(2.16)
Now, if we invert (2.13) by writing
Cn(x)eγnτ =
n
X
j=0
βnjeγjτRj(x; τ),
βnn = 1.
(2.17)
then Φk(x; τ) can be expanded according to [4]
Φ2k−1(x; τ)eγ2k−1τ
=
−
q
w(x)rk−1(0)
∞
X
ν=2k−2
Cν(x)e−γντ
hν
βν 2k−2,
Φ2k−2(x; τ)eγ2k−2τ
=
q
w(x)rk−1(0)
∞
X
ν=2k−1
Cν(x)e−γντ
hν
βν 2k−1.
(2.18)
where hν is the normalization
Z
w(x)Cj(x)Ck(x) dx = hjδj,k.
(2.19)
With this notation, we can now deﬁne the functions S, ˜I and D. We have, assuming
N even,
