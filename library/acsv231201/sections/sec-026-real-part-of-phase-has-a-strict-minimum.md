---
doc_id: acsv231201
doc_title: "Analytic Combinatorics in Several Variables Expanded Second Edition"
section_id: sec-026-real-part-of-phase-has-a-strict-minimum
section_title: "Real part of phase has a strict minimum"
section_number: null
pages: 139-143
source_pdf: ACSV231201.pdf
source_sha256: 1a664d0bf666041e
toc_source: outline
doc_brief: "Analytic Combinatorics in Several Variables Expanded Second Edition — 100 sections: Front matter; Preface to the second edition; Preface to the first edition"
---
121
Proof of Theorem 5.1.
Writing A(z) as a power series up to degree N plus a
remainder term,
A(z) =

N
X
n=0
X
|r|=n
arzr
+ R(z),
where R(z) = O

|z|N+1
. Using Corollary 5.7 to integrate all the monomial
terms and Proposition 5.8 to bound the integral of R(z)e−λS (z) shows that
I(λ) =
N
X
n=0
X
|r|=n
arβrλ−(d+n)/2 + O

λ−(d+N+1)/2
,
proving the stated asymptotic expansion.
□
Exercise 5.6. Let M(t) = sup{|A(z)| : |z| = t} and let KR be a ball of ﬁxed
radius R. Prove a version of Theorem 5.1 using the fact that if M(t) = O(tα)
then
Z
KR
A(z)e−λS (z) dz ≤
Z R
0
e−λtM(t) dV(Kt) ,
where dV(Kt) = cttd−1dt is the volume of a spherical shell of thickness dt and
radius t in d dimensions.
5.3 Real part of phase has a strict minimum
We extend our results beyond integrals with standard quadratic phases using
complex analytic techniques. If N is a neighborhood of the origin in Rd and φ :
N →C is analytic on N then φ can be viewed as a complex analytic function
on a neighborhood NC of the origin in Cd using its power series expansion.
Suppose that φ(0) = 0 and the real part of φ is nonnegative on N, so that the
gradient of φ must vanish at the origin. Our ﬁrst key lemma is that, under an
assumption of nondegeneracy, we can change variables so that φ becomes the
standard quadratic form.
Lemma 5.9 (Complex Morse Lemma). If φ(x) has vanishing gradient and
nonsingular Hessian H at the origin then there is a bi-holomorphic change of
variables x = ψ(y) around x = y = 0 such that φ(ψ(y)) = S (y) = Pd
j=1 y2
j.
The Jacobian matrix Jψ = dψ(0) satisﬁes (det Jψ)2 =
2d
det H .
Our proof of Lemma 5.9 is adapted from the proof of the real version given
in [Ste93, VIII:2.3.2].
122
Multivariate Fourier–Laplace integrals
Proof
To prove the claim about the Jacobian determinant, we apply the chain
rule to the equation φ(ψ(y)) = S (y) and conclude that the Hessian matrix of S
at the origin equals JT
ψ H Jψ. The Hessian of S is twice the identity matrix, so
2I = JT
ψ H Jψ and taking determinants gives the stated result.
To prove the change of variables, we begin by writing
φ(x) =
d
X
j,k=1
x jxkφ j,k(x)
for analytic functions φ j,k = φk,j with constant terms φj,k(0) = H j,k /2. There
is plenty of freedom, but a convenient choice is to take
x jxkφ j,k(x) =
X
|r|≥2
rj(rk −δ j,k)
|r|(|r| −1) arxr,
(5.9)
where ar are the Taylor coeﬃcients of φ at x and δ j,k = 1 if j = k and 0
otherwise. For ﬁxed r it is easy to check that
X
1≤j,k≤d
r j(rk −δ j,k)
|r|(|r| −1) = 1,
so that φ(x) = P
j,k x jxkφ j,k(x), and matching coeﬃcients on the terms of or-
der precisely two veriﬁes φ j,k(0) = H j,k /2. We may assume without loss of
generality that φ j, j(0) = H j, j , 0 for all j, because there is always a unitary
map U such that the Hessian of φ ◦U has nonvanishing diagonal entries, and
if (φ ◦U) ◦ψ0 = S for some ψ0 then φ ◦ψ = S , where ψ = U ◦ψ0.
We conclude with an induction. Since we are assuming that φ1,1(0) , 0, the
reciprocal 1/φ1,1(x) and a branch of
p
φ1,1(x) are both analytic in a neighbor-
hood of the origin. If
y1 =
p
φ1,1(x)
x1 +
X
k>1
xkφ1,k(x)
φ1,1(x)

then the terms of y2
1 of total degree at most one in x2, . . . , xd match those of φ,
since
φ(x) −y2
1 =
d
X
j,k=2
xjxk
 
φ j,k(x) −φ1,j(x)φ1,k(x)
φ1,1(x)
!
.
(5.10)
In the new coordinates y1, x2, x3, . . . , xd, the Hessian matrix of φ is a (1, d −
1) block matrix, where the submatrix H(1) that corresponds to the variables
x2, . . . , xd has determinant det H(1) = det H /φ1,1 , 0. In fact, if H is real
positive deﬁnite then so is H(1), provided the correct branch of the square root
5.3 Real part of phase has a strict minimum
123
is chosen. Equation (5.10) thus writes φ in the form
φ(x) = y2
1 +
X
j,k≥2
x jxkφ(1)
j,k(x)
(5.11)
for some analytic functions φ(1)
j,k satisfying φ(1)
j,k(0) = H(1)
j,k /2. By induction, if
we assume that
φ(x) =
r−1
X
j=1
y2
j +
X
j,k≥r
xjxkφ(r−1)
j,k
(x)
for some 1 ≤r ≤d then setting
yr =
p
φr,r(x)
xr +
X
k>r
xkφ(r−1)
r,k
(x)
φ(r−1)
r,r
(x)

gives
φ(x) =
rX
j=1
y2
j +
X
j,k≥r+1
xjxkφ(r)
j,k(x)
for some analytic functions φ(r)
j,k satisfying φ(r)
j,k(0) = H(r)
j,k /2 with H(r) nonsin-
gular, leading in the end to a sequence of bi-holomorphic changes of variables
writing φ(x) = Pd
j=1 y2
j as claimed.
□
Exercise 5.7. Use the Complex Morse Lemma to ﬁnd a bi-holomorphic change
of variables turning φ(x, y, z) = xy + yz + zx + xyz into the standard quadratic
form S (u, v, w).
We are now ready to prove Theorem 5.2.
Proof of Theorem 5.2.
The convergent power series expansion of φ allows us
to extend it to a neighborhood of the origin in Cd. Under the change of variables
ψ from Lemma 5.9,
I(λ) =
Z
ψ−1N
A(ψ(y))e−λS (y)(det dψ(y)) dy
=
Z
ψ−1N
˜A(y)e−λS (y) dy .
We need to check that we can move the chain of integration C = ψ−1N back
to the real plane. If we can, then applying the expansion from Theorem 5.1
and noting that the terms with odd values of |r| all vanish yields the desired
expansion in powers λ−d/2−ℓ.
Let h(z) = Re{S (z)}. Our assumption that the real part of φ is nonnegative
on N and vanishes only at the origin implies that the chain C lies in the region
124
Multivariate Fourier–Laplace integrals
{z ∈Cd : h(z) > 0} except when z = 0, meaning there exists ε > 0 such that
h(z) ≥ε > 0 for all z ∈∂C. Let
H(z, t) = Re{z} + (1 −t) i Im{z}
be a homotopy from the identity map to the projection map π(z) = Re{z}. For
any chain σ, the homotopy H induces a chain homotopy H(σ) satisfying
∂H(σ) = σ −π(σ) + H(∂σ) .
Taking σ = C, and using the fact that h(H(z, t)) ≥h(z), we see there is a
d-chain C′ supported on {z ∈Cd : h(z) > ε} and a (d + 1)-chain D such that
∂D = C −π(C) + C′.
Stokes’s Theorem (Theorem A.24 in Appendix A) implies that
Z
∂D
ω =
Z
D
dω = 0
for any holomorphic d-form ω, which means
Z
C
ω =
Z
π(C)
ω −
Z
C′ ω .
When ω = ˜A(y)e−λS (y) dy the integral over C′ is O

e−λε
, giving
I(λ) =
Z
π(C)
˜A(y)e−λS (y) dy + O

e−ελ
.
The projection π maps any real d-manifold in Cd locally diﬀeomorphically
into Rd wherever its tangent space is not parallel to the imaginary subspace of
Cd. Because h(z) ≥0 on C, the tangent space to the support of C at the origin is
not parallel to the imaginary subspace. The tangent space varies continuously,
so in a neighborhood of the origin π is a diﬀeomorphism. In particular, the
chain π(C) is a disk ∆in Rd plus a collection of points whose image under h is
bounded above zero (which will contribute an exponentially negligible term to
dominant asymptotic behavior). Observing that
˜A(0) = A(0) det(dψ(0)) = 2dA(0)
√
det H
ﬁnishes the proof, up to the choice of sign of the square root corresponding to
the orientation of ∆.
The stated sign choice of ˜A(0) in this theorem can be veriﬁed by proving
that the linear map dπ ◦dψ−1 at the origin sends the standard basis of Rd to
another positively oriented basis if and only if det(dψ(0)) is the product of
the principal square roots of the eigenvalues of H. We state and prove the
