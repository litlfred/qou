---
doc_id: acsv231201
doc_title: "Analytic Combinatorics in Several Variables"
section_id: sec-023-real-part-of-phase-has-a-strict-minimum
section_title: "Real part of phase has a strict minimum"
section_number: null
pages: 139-147
source_pdf: ACSV231201.pdf
source_sha256: 1a664d0bf666041e
---
Proof of Theorem 5.1. Writing A(z) as a power series up to degree N plus a
remainder term,
A(z) =

N∑
n=0
∑
|r|=n
arzr
 + R(z),
where R(z) = O
(
|z|N+1
)
. Using Corollary 5.7 to integrate all the monomial
terms and Proposition 5.8 to bound the integral of R(z)e−λS (z) shows that
I(λ) =
N∑
n=0
∑
|r|=n
arβrλ−(d+n)/2 + O
(
λ−(d+N+1)/2)
,
proving the stated asymptotic expansion. □
Exercise 5.6. Let M(t) = sup{|A(z)| :|z| = t} and let KR be a ball of ﬁxed
radius R. Prove a version of Theorem 5.1 using the fact that if M(t) = O(tα)
then ∫
KR
A(z)e−λS (z) dz≤
∫ R
0
e−λtM(t) dV(Kt),
where dV(Kt) = cttd−1dt is the volume of a spherical shell of thickness dt and
radius t in d dimensions.
5.3 Real part of phase has a strict minimum
We extend our results beyond integrals with standard quadratic phases using
complex analytic techniques. IfN is a neighborhood of the origin inRd andφ :
N→ C is analytic onN thenφ can be viewed as a complex analytic function
on a neighborhood NC of the origin in Cd using its power series expansion.
Suppose that φ(0) = 0 and the real part of φ is nonnegative onN, so that the
gradient of φ must vanish at the origin. Our ﬁrst key lemma is that, under an
assumption of nondegeneracy, we can change variables so that φ becomes the
standard quadratic form.
Lemma 5.9 (Complex Morse Lemma) . If φ(x) has vanishing gradient and
nonsingular HessianH at the origin then there is a bi-holomorphic change of
variablesx = ψ(y) aroundx =y = 0 such that φ(ψ(y)) = S (y) = ∑d
j=1 y2
j.
The Jacobian matrix Jψ = dψ(0) satisﬁes (det Jψ)2 = 2d
detH .
Our proof of Lemma 5.9 is adapted from the proof of the real version given
in [Ste93, VIII:2.3.2].
122 Multivariate Fourier–Laplace integrals
Proof To prove the claim about the Jacobian determinant, we apply the chain
rule to the equationφ(ψ(y)) = S (y) and conclude that the Hessian matrix of S
at the origin equals JT
ψH Jψ. The Hessian of S is twice the identity matrix, so
2I = JT
ψH Jψ and taking determinants gives the stated result.
To prove the change of variables, we begin by writing
φ(x) =
d∑
j,k=1
x jxkφ j,k(x)
for analytic functions φ j,k = φk, j with constant terms φ j,k(0) =H j,k/2. There
is plenty of freedom, but a convenient choice is to take
x jxkφ j,k(x) =
∑
|r|≥2
r j(rk−δ j,k)
|r|(|r|− 1) arxr, (5.9)
where ar are the Taylor coe ﬃcients of φ atx and δ j,k = 1 if j = k and 0
otherwise. For ﬁxedr it is easy to check that
∑
1≤ j,k≤d
r j(rk−δ j,k)
|r|(|r|− 1) = 1,
so that φ(x) = ∑
j,k x jxkφ j,k(x), and matching coe ﬃcients on the terms of or-
der precisely two veriﬁes φ j,k(0) =H j,k/2. We may assume without loss of
generality that φ j, j(0) =H j, j , 0 for all j, because there is always a unitary
map U such that the Hessian of φ◦ U has nonvanishing diagonal entries, and
if (φ◦ U)◦ψ0 = S for someψ0 thenφ◦ψ = S , whereψ = U◦ψ0.
We conclude with an induction. Since we are assuming thatφ1,1(0), 0, the
reciprocal 1/φ1,1(x) and a branch of
√
φ1,1(x) are both analytic in a neighbor-
hood of the origin. If
y1 =
√
φ1,1(x)
x1 +
∑
k>1
xkφ1,k(x)
φ1,1(x)

then the terms of y2
1 of total degree at most one in x2,..., xd match those ofφ,
since
φ(x)− y2
1 =
d∑
j,k=2
x jxk
(
φ j,k(x)− φ1, j(x)φ1,k(x)
φ1,1(x)
)
. (5.10)
In the new coordinates y1, x2, x3,..., xd, the Hessian matrix of φ is a (1, d−
1) block matrix, where the submatrix H (1) that corresponds to the variables
x2,..., xd has determinant detH (1) = detH/φ1,1 , 0. In fact, if H is real
positive deﬁnite then so isH (1), provided the correct branch of the square root
5.3 Real part of phase has a strict minimum 123
is chosen. Equation (5.10) thus writesφ in the form
φ(x) = y2
1 +
∑
j,k≥2
x jxkφ(1)
j,k(x) (5.11)
for some analytic functions φ(1)
j,k satisfyingφ(1)
j,k(0) =H (1)
j,k/2. By induction, if
we assume that
φ(x) =
r−1∑
j=1
y2
j +
∑
j,k≥r
x jxkφ(r−1)
j,k (x)
for some 1≤ r≤ d then setting
yr =
√
φr,r(x)
xr +
∑
k>r
xkφ(r−1)
r,k (x)
φ(r−1)
r,r (x)

gives
φ(x) =
r∑
j=1
y2
j +
∑
j,k≥r+1
x jxkφ(r)
j,k(x)
for some analytic functions φ(r)
j,k satisfyingφ(r)
j,k(0) =H (r)
j,k/2 withH (r) nonsin-
gular, leading in the end to a sequence of bi-holomorphic changes of variables
writingφ(x) = ∑d
j=1 y2
j as claimed. □
Exercise 5.7. Use the Complex Morse Lemma to ﬁnd a bi-holomorphic change
of variables turning φ(x, y, z) = xy + yz + zx + xyz into the standard quadratic
form S (u, v, w).
We are now ready to prove Theorem 5.2.
Proof of Theorem 5.2. The convergent power series expansion ofφ allows us
to extend it to a neighborhood of the origin inCd. Under the change of variables
ψ from Lemma 5.9,
I(λ) =
∫
ψ−1N
A(ψ(y))e−λS (y)(det dψ(y)) dy
=
∫
ψ−1N
˜A(y)e−λS (y) dy.
We need to check that we can move the chain of integration C = ψ−1N back
to the real plane. If we can, then applying the expansion from Theorem 5.1
and noting that the terms with odd values of |r| all vanish yields the desired
expansion in powersλ−d/2−𝓁.
Let h(z) = Re{S (z)}. Our assumption that the real part of φ is nonnegative
onN and vanishes only at the origin implies that the chainC lies in the region
124 Multivariate Fourier–Laplace integrals
{z∈ Cd : h(z) > 0} except whenz = 0, meaning there exists ε >0 such that
h(z)≥ε> 0 for allz∈∂C. Let
H(z, t) = Re{z} + (1− t) i Im{z}
be a homotopy from the identity map to the projection mapπ(z) = Re{z}. For
any chainσ, the homotopy H induces a chain homotopy H(σ) satisfying
∂H(σ) =σ−π(σ) + H(∂σ).
Takingσ = C, and using the fact that h(H(z, t)) ≥ h(z), we see there is a
d-chainC′ supported on{z∈Cd : h(z)>ε} and a (d + 1)-chainD such that
∂D =C− π(C) +C′.
Stokes’s Theorem (Theorem A.24 in Appendix A) implies that
∫
∂D
ω =
∫
D
dω = 0
for any holomorphic d-formω, which means
∫
C
ω =
∫
π(C)
ω−
∫
C′
ω.
Whenω = ˜A(y)e−λS (y) dy the integral overC′ is O
(
e−λε
)
, giving
I(λ) =
∫
π(C)
˜A(y)e−λS (y) dy + O
(
e−ελ)
.
The projection π maps any real d-manifold inCd locally diﬀeomorphically
intoRd wherever its tangent space is not parallel to the imaginary subspace of
Cd. Because h(z)≥ 0 onC, the tangent space to the support ofC at the origin is
not parallel to the imaginary subspace. The tangent space varies continuously,
so in a neighborhood of the origin π is a di ﬀeomorphism. In particular, the
chainπ(C) is a disk ∆ inRd plus a collection of points whose image under h is
bounded above zero (which will contribute an exponentially negligible term to
dominant asymptotic behavior). Observing that
˜A(0) = A(0) det(dψ(0)) = 2dA(0)√
detH
ﬁnishes the proof, up to the choice of sign of the square root corresponding to
the orientation of ∆.
The stated sign choice of ˜A(0) in this theorem can be veriﬁed by proving
that the linear map dπ◦ dψ−1 at the origin sends the standard basis of Rd to
another positively oriented basis if and only if det( dψ(0)) is the product of
the principal square roots of the eigenvalues of H. We state and prove the
5.4 General nondegenerate phase with ﬁnite critical set 125
necessary technical result in Lemma 5.10 below, which completes our proof of
this theorem. □
Lemma 5.10. Let W ={z∈Cd : Re{S (z)}> 0} and suppose thatα∈ GLd(C)
maps Rd into W. If M = αTα is the matrix representing the quadratic form
S◦α and π is the projection map from Cd ontoRd then π◦α is orientation
preserving onRd if and only ifdetα is the product of the principal square roots
of the eigenvalues of M (rather than the negative of this).
Proof First suppose α∈ GLd(R). Then M has positive eigenvalues, and the
product of their principal square roots is positive. The mapπ is the identity on
Rd, so the claimed statement boils down to saying thatα preserves orientation
if and only if it has positive determinant, which is true by deﬁnition. In the
general case, let αt = πt◦ α, where πt(z) = Re{z} + (1− t) Im{z}. Since
πt(Rd)⊆ W for all 0 ≤ t≤ 1, the matrix Mt = αT
t αt always has eigenvalues
with nonnegative real parts. The product of the principal square roots of the
eigenvalues is a continuous function on the set of nonsingular matrices with
no negative real eigenvalues. The determinant of αt is a continuous function
of t, and we have seen it agrees with the product of principal square roots of
eigenvalues of Mt when t = 1 (the real case), so by continuity this is the correct
sign choice for all 0≤ t≤ 1. Taking t = 0 proves the lemma. □
Exercise 5.8. Supposeφ is the logarithm of an analytic function, deﬁned only
up to the addition of (2πi)n for n∈ Z. How does this aﬀect the conclusion of
Theorem 5.2?
5.4 General nondegenerate phase with ﬁnite critical set
In this section we prove Theorem 5.3 by moving the chain of integration ofI
so that Reφ is minimized only at the ﬁnite set of critical points, then applying
Theorem 5.2. We ﬁrst remark on some di ﬀerences from our previous argu-
ments. While the chain of integration may be deﬁned on a subspace X⊆ Rd,
the form in the integrand will be extended to a neighborhood ofX inCd and the
deformation in general will not be conﬁned toX. To accomplish this, we deﬁne
a complexiﬁcation of X with analytic structure. Our deformation is deﬁned by
a smooth vector ﬁeld v which, although not analytic, lies in the complex tan-
gent bundle to the complexiﬁcation of each stratum. The proof is broken into
the following steps.
(1) Deﬁne the complexiﬁcation X⊗C.
(2) Extend φ andη to a neighborhood U of X inCd.
126 Multivariate Fourier–Laplace integrals
(3) Construct a vector ﬂowv on U, tangent to the strata ofX⊗C and vanishing
precisely on G, such that⟨Re dφ,v⟩> 0 on U\ G.
(4) Show that
∫
C e−λφη =
∫
C′ e−λφη, whereC′ is obtained fromC by ﬂowing
alongv for a short time.
(5) Use Theorem 5.2 on the deformed chain C′.
Step (2) follows in a straightforward manner from Step (1). Step (3) is where
the special assumptions on X are used. This allows us to follow the methodol-
ogy of locally constant vector ﬁelds and partitions of unity in [ABG70], rather
than the more di ﬃcult methodology of controlled vector ﬁelds in [Mat70].
Step (4) is an application of Stokes’s Theorem together with the crucial obser-
vation that part of the boundary of the chain representing the deformation lies
in a complex manifold of dimension less than d. Step (5), once we reach it, is
immediate.
Step 1: Complexiﬁcation
Lemma 5.11. Under the hypotheses of Theorem 5.3, there is a complex strat-
iﬁed space X⊗C with strataS⊗ C asS ranges over the strata of X, such that
X⊗C is a neighborhood of X inCd and such that the chart mapsψ⊗C :Ck→
S⊗ C restricted toRk are chart maps forS.
Proof We complexify ∆p inCp and Md−k inCd separately and take the prod-
uct. First, we note that the set ∆p is deﬁned by p + 1 linear inequalities. Re-
laxing these by ε > 0 produces a neighborhood D of ∆p in Rd. Taking the
product with a su ﬃciently small imaginary interval [−εi,ε i] in each of the p
coordinates produces a complex stratiﬁed space that is a neighborhood of ∆p
inCd. Because of our assumptions, we can complexify Md−k toV. Taking the
product of F⊗C and Md−k⊗C as stratiﬁed spaces, where F is a face of ∆p,
produces (F× M)⊗C; these are the strataS⊗ C and ﬁt together to form the
stratiﬁed space X⊗C satisfying the conclusion of the theorem. □
Remark 5.12. In Chapter 9, we always have k = 1 and Md−k is a smooth
open (d− 1)-patch inVQ. In Chapter 10, we have k = 0 and Md is a patch
of a middle-dimensional torus in Cd\V . In general, under the condition that
the real tangent space spans a complex space of dimension d− k, one may
deﬁne Md−k⊗C to be the intrinsic complexiﬁcation of M, namely the smallest
complex manifold containing M. This is known to exist [BER99], following a
construction of [BW59], and will be a complex (d− k)-manifold.
Exercise 5.9. Suppose X is the circle in R3 deﬁned by the real solutions to
x2 + y2− 1 = z = 0. Find the complexiﬁcation X⊗C.
5.4 General nondegenerate phase with ﬁnite critical set 127
Step 2: Extending analytic maps
Proposition 5.13. Letφ : X→C be an analytic map on an analytic stratiﬁed
space X, and let ψ1 andψ2 be chart maps whose ranges are overlapping do-
mainsN1 andN2 in X. As y takes values in the intersection of the ranges of
ψ1⊗C andψ2⊗C, the function ˜φ = ˜φ j deﬁned by
˜φ j(y) =τ j◦ (ψ j⊗C)−1(y) (5.12)
is independent of j, whereτ j represents analytic continuation of the mapφ◦ψ j
from the real parameter space to a complex neighborhood of it. This common
value deﬁnes an analytic extension ofφ on a neighborhood of X in Cd.
Proof The maps ˜φ1 and ˜φ2 agree wheny∈N 1∩N 2∩ X. Being analytic, they
must agree in a neighborhood of X in X⊗C. □
Step 3: Constructing the vector ﬂow
Lemma 5.14. Under the assumptions of Theorem 5.3, there is a vector ﬁeldv
on a neighborhood U of X in Cd, tangent to each complexiﬁed stratumS⊗ C
of X⊗C and vanishing only on G, with the property that ⟨Re dφ,v⟩ > 0 at
every point of U\G. For suﬃciently small s, there is a well-deﬁned diﬀerential
ﬂow Ψ : [0, 1]×|C|→ Cd satisfying (d/dt)Ψ(t, x) = sv(Ψ(t, x)), and the map
x↦→ Ψ(ε,x) is a local diﬀeomorphism for suﬃciently smallε> 0.
Proof As described in Proposition D.14 of Appendix D, there is a di ﬀeo-
morphic local product structure under the assumptions of Theorem 5.3. The
argument discussed in Step 2 of the proof of Proposition D.13 in Appendix D
implies that there is a Lipschitz vector ﬂowv on a neighborhood U of X inCd
deﬁned by (D.2.1). This vector ﬁeldv is tangent to each complexiﬁed stratum,
vanishes precisely on G, and satisﬁes⟨Re dφ,v⟩> 0 on U\ G.
The map x ↦→ Ψ(ε,x) is a local di ﬀeomorphism for su ﬃciently small
ε > 0 because v is smooth and bounded (see, for example, [Lee03, Propo-
sition 9.12]). □
Step 4: Deforming the contour
Composing the ﬂow from Lemma 5.14 with the simplex σ j gives a homotopy
from eachσ j to a new analytic simplexσ′
j, and summing theσ′
j deﬁnes a new
chainC′. Becausev is tangent toS⊗ C for each stratumS, the ﬂow preserves
each complexiﬁed stratumS⊗ C, and because∂C is contained in the union of
strata of dimensions at most p + d− k− 1, it follows that Ψ(∂C) is contained in
the union of complexiﬁed strata of dimensions at most p + d− k− 1.
128 Multivariate Fourier–Laplace integrals
Lemma 5.15. Using the above notation,
∫
C
e−λφη =
∫
C′
e−λφη. (5.13)
Proof The homotopy Ψ deﬁned by Lemma 5.14 is a chain with boundary
C−C′−[0, 1]×∂C. Since e−λφη is a holomorphic p+d−k-form, it is annihilated
by the diﬀerential, and Stokes’s Theorem implies
0 =
∫
Ψ
d(e−λφη)
=
∫
∂Ψ
e−λφη
=
∫
C′
e−λφη−
∫
C
e−λφη−
∫
D
e−λφη,
whereD is a chain representing [0, 1]×∂C. Because e−λφη is a holomorphic
(p + d− k)-form, its integral vanishes over any p + d− k-chain supported
on a ( p + d− k− 1)-dimensional complex manifold (see Exercise A.15 of
Appendix A), ﬁnishing the proof. □
Exercise 5.10. A simpler version of the deformation argument can be illus-
trated in two real variables. Suppose thatV(x, y) is a smooth function onR2 and
η = Vx(x, y)dx + Vy(x, y)dy. Assume that a homotopy H : [0, T]× [0, 1] carries
the path α : [0, T]→ R2 to the path β : [0, T]→ R2, meaning H(t, 0) = α(t)
and H(t, 1) = β(t) for all t∈ [0, T]. If f (u) = H(0, u) and g(u) = H(T, u) then
what conditions on d f and dg guarantee that
∫
αη =
∫
βη by implying that the
integrals over the paths traced out by the endpoints of the path as it moves from
α toβ are everywhere zero?
Step 5: Evaluating the integral onC′
From the construction of v we see that C′ = ∑m
j=1σ′
j, where each simplex
σ′
j contains the same critical point q in its interior as σ j. By Lemma 5.14 we
know that Reφ(σ′
j(x))≥ Reφ(σ j(x))≥ 0 for all j≤ m andx∈ ∆p, where
the ﬁrst inequality is strict unlessσ j(x) is a critical point. Thus, the image|C′|
is a stratiﬁed space represented analytically by ( p + d− k)-simplices σ′
j for
1≤ j≤ m and the function Reφ is nonnegative and vanishes precisely on G′.
If σ′
j contains no point of G′ then the modulus of
∫
σ′
j
e−λφ(z)η is bounded
above by Me−λK, where M = max{|A(x)| : x∈ ∆d} and K = min{Reφ(x) :
x∈ ∆d}. Ifσ′
j containsq∈ G′ then translating the preimage ofq to the origin
turns ∆p+d−k into a neighborhoodN of the origin on which A and ˜φ = φ◦σ′
j
are analytic and Re ˜φ(z)≥ 0, with equality only at the origin. Theorem 5.2
