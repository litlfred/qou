---
doc_id: arxiv-1106.2975v1
doc_title: "The Polyanalytic Ginibre Ensembles"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 2-8
source_pdf: 1106.2975v1.pdf
source_sha256: 7e966c7392b70ae0
doc_brief: "The Polyanalytic Ginibre Ensembles — For integers n, q = 1, 2, 3, . . ., let Poln,q denote the C-linear space of polynomials in z and ¯z, of degree ≤n −1 in z and of degree ≤q −1 in ¯z."
---
Notation. We will write use standard notation, such as ∂X and int(X) for the
boundary and the interior of a subset X of the complex plane C. The complex
conjugate of a complex number z is usually written as ¯z. We write R for the real
line, D := {z ∈C : |z| < 1} for the open unit disk, and De := {z ∈C : |z| > 1} for the
open exterior (punctured) disk. The characteristic function of a set E is written 1E.
We write
dA(z) = π−1dxdy,
where z = x + iy ∈C,
for the normalized area measure in C, and use the standard Wirtinger derivatives
∂z := 1
2(∂x −i∂y),
¯∂z := 1
2(∂x + i∂y),
where z = x + iy.
We also write ∆for the (quarter) Laplacian
∆z := ∂z ¯∂z = 1
4(∂2
x + ∂2
y).
Determinantal projection processes. Given a locally compact topological space
X with a Radon measure µ, a determinantal projection process (in the sequel
just determinantal process) is a random conﬁguration of n points deﬁned by the
following probability measure on Xn:
(1.1)
dP(z1, . . . , zn) = 1
n! det[Kn(zi, zj)]n
i,j=1dµ(z1) · · · dµ(zn).
Here, Kn is the integral kernel of a projection operator to an n-dimensional sub-
space of L2(X, µ). It is customary to identify all the permutations of the points and
think the process as a random measure Pn
j=1 δzj on X.
A general deﬁnition of a determinantal process was introduced by Macchi
[17], who wanted to model fermions in quantum mechanics. Indeed, for any
determinantal process, the probability density vanishes whenever any two points
in the n-tuple (z1, ..., zn) coincide (fermions are forbidden to be in the same state).
We interpret this as saying that the points in the n-tuple repel each other. Point
processes of this kind appear in several contexts, e.g., in random matrix theory
and combinatorics (for general surveys, s [15], [8]; we should also mention the
books [18], [9], [10], [4]).
Eigenvalues of random normal matrix ensembles. Our main motivating exam-
ple comes from the theory of random normal matrices. This topic has in re-
cent years been subject to rather active investigation by physicists as well as by
mathematicians. For an introduction, see, e.g., [24]. So, we shall use X = C and
dµ(z) = e−mQ(z)dA(z), for a positive weight function Q satisfying some mild regu-
larity and growth conditions; m is a positive real parameter, and dA(z) = π−1dxdy
is the normalized area measure. Let us write L2(C, e−mQ) := L2(X, µ) in this situ-
ation. The determinantal projection process is associated with an n-dimensional
subspace of L2(C, e−mQ), and we will use the space Poln of all polynomials in z
of degree ≤n −1; we write Polm,n to indicate that we have supplied Poln with
the Hilbert space structure of L2(C, e−mQ). The density of the process is then given
by the reproducing kernel Km,n of the space Polm,n. So, we are talking about the
probability measure
(1.2)
dP(z1, . . . , zn) = 1
n! det[Km,n(zi, zj)]n
i,j=1e−m{Q(z1)+···+Q(zn)}dA(z1) · · · dA(zn).
The Polyanalytic Ginibre Ensembles
3
In terms of the correlation kernel
(1.3)
m,n(z, w) := Km,n(z, w)e−1
2 m{Q(z)+Q(w)},
which is the an integral kernel of an orthogonal projection L2(C), the expression
(1.2) simpliﬁes to
(1.4)
dP(z1, . . . , zn) = 1
n! det
h
m,n(zi, zj)
in
i,j=1dA(z1) · · · dA(zn).
The process described by (1.2) and (1.4) represents the eigenvalues of a random
normal matrix picked from the distribution
(1.5)
1
Zm,n
e−m tr[Q(M)]dvolnm(n)(M),
where dvolnm(n)(M) is the natural Riemannian volume form on the n × n nor-
mal matrices inherited from the metric of Cn2; Zm,n is the normalization constant
needed to make the total mass equal to 1. We are interested in the limiting be-
haviour of the process as m, n →+∞while n = mτ + O(1) for some positive real
number τ. Without loss of generality, we will consider only τ = 1.
Local blow-up processes. Let N+ and N+,0 be the set of points deﬁned by
N+ :=
n
w ∈C : ∆Q(w) > 0
o
,
N+,0 :=
n
w ∈C : ∆Q(w) ≥0
o
.
In the arXiv preprint [12], which will appear later in the expanded form [13], the
function b
Q was deﬁned as a certain envelope of Q, namely the largest subharmonic
function in C which is ≤Q everywhere and has the growth bound
b
Q(z) = log |z|2 + O(1),
as |z| →+∞.
It is known that ∆b
Q = 1S∆Q for some compact set S (see, e.g., [13]). We assume
that S is the minimal compact with this property, and call S a spectral droplet.
We then have S ⊂N+,0. The point process (1.2) has the following property: as
m, n →+∞while n = m + O(1), the points will tend to accumulate on the set S
with density ∆Q there. Moreover, the set S ∩N+ is rather regular for real-analytic
Q, as the Sakai theory applies (cf. [14]). Typically we then expect a real-analytic
boundary, with the exception of cusps and contact (or kissing) points. Let us refer
to the set int(S ∩N+) as the bulk. The results of [2], [3] show that for bulk points z,
the local blow-up process at z, with coordinates (ξ1, . . . ξn),
ξj := m1/2[∆Q(z)]1/2(zj −z),
where (z1, . . . , zn) are from the process (1.2), converges weakly to the translation
invariant Ginibre(∞) process, as m, n →+∞while n = m + o(1). The associated
generating kernel is the reproducing kernel (ξ, η) 7→eξ ¯η of the Bargmann-Fock
space. This has the ﬂavor of a universality result. The corresponding statement in
the Gaussian unitary ensemble (GUE) case is the universality of the sine kernel for
bulk. We observe here that the sine kernel is the reproducing kernel for the Paley-
Wiener space (a subspace of L2(R) consisting of entire functions). As for the two
boundary points in the GUE model, the Tracy-Widom distribution appears, which
is generated by the Airy kernel. The Airy kernel is reproducing for another Hilbert
space of entire functions. This suggests that for real-analytic Q and z ∈∂S ∩N+,
there should exist a local blow-up
ξj := mθ(zj −z),
4
Haimi and Hedenmalm
where θ = θ(z) is a suitable positive real, such that as m, n →+∞while n =
m+o(1), the process (ξ1, . . . , ξn) would converge to a determinantal process whose
generating kernel is the reproducing kernel of a Hilbert space of entire functions.
We verify this in the context of the Ginibre ensemble (i.e., with Q(z) = |z|2), and
identify the associated Hilbert space with a closed subspace of the Bargmann-Fock
space characterized by slow growth in a half-plane. In that case, θ = 1
2 as in the
case of interior points.
The Berezin measure and the Berezin density. In [2], [3], Ameur, Hedenmalm,
and Makarov study the Berezin measure dB⟨z⟩
m,n and Berezin density B⟨z⟩
m,n:
dB⟨z⟩
m,n(w) := B⟨z⟩
m,n(w)dA(w),
B⟨z⟩
m,n(w) := |Km,n(z, w)|2
Km,n(z, z) e−mQ(w),
which arise in the study of the Berezin transform. The Berezin measure is a
probability measure, which makes it more stable than the reproducing kernel
Km,n of Polm,n itself as we let m, n →+∞. In terms of the point process (1.2), B⟨z⟩
m,n
measures the amount of repulsion from z caused by placing one of the points at
z. For bulk points z, we have the convergence dB⟨z⟩
m,n →dδz in the weak-star sense
of measures, as m, n →+∞while n = m + o(1). Here, dδz is the Dirac point mass
at z. In fact, there is a better result: the blow-up Berezin density
ˆB⟨z⟩
m,n(ξ) =
1
m∆Q(z) B⟨z⟩
m,n

z +
ξ
p
m∆Q(z)

converges to the standard Gaussian e−|ξ|2. This corresponds to the convergence of
the local blow-up of the point process to the Ginibre(∞) process (cf. [2], [3]). On the
other hand, for points z outside the spectral droplet, i.e., for z ∈C \ S, the Berezin
measure dB⟨z⟩
m,n converges in the weak-star sense of measures to harmonic measure
at z with respect to the exterior domain C \ S as m, n →+∞while n = m + o(1)
(see [2] for Q = |z|2, and [3] for the general result).
The local blow-up of the point process and the Berezin density. It is convenient
to think of the point process (1.2) in terms of the k-point intensities
det
h
m,n(zi, zj)
ik
i,j=1 = det
h
Km,n(zi, zj)e−1
2 m[Q(zi)+Q(zj)]ik
i,j=1.
We notice quickly that the intensities are unchanged if the kernel changed to
Kχ
m,n(z, w) := χ(z) ¯χ(w)Km,n(z, w),
provided that χ is measurable with |χ(z)| ≡1 (we can call this a “guage transfor-
mation”). This can help in the asymptotical analysis of local blow-ups. For k = 2,
we get the 2-point intensity
n
Km,n(z1, z1)Km,n(z2, z2) −|Km,n(z1, z2)|2o
e−mQ(z1)−mQ(z2)
= Km,n(z1, z1)e−mQ(z1)

Km,n(z2, z2)e−mQ(z2) −|Km,n(z1, z2)|2
K(z1, z1)
e−mQ(z2)

,
where we recognize the Berezin density as a correction to the product of the two
1-point densities, where the 1-point intensity is
Km,n(z1, z1) e−mQ(z1).
The Polyanalytic Ginibre Ensembles
5
So, as far as the 2-point intensity goes, we just need the 1-point intensity and
the Berezin density. Since the 1-point intensity is just the restriction to z1 = z2
of the Berezin density, the Berezin density is all we need to describe the 2-point
intensity. We will be a little lazy and just work with the Berezin density in the
context of local blow-ups, although the asymptotics of the k-point intensity would
strictly speaking require a little more work. So, although we state our many of our
assertions regarding local blow-ups in terms of the Berezin density, we maintain
that they generalize to statements about the point processes (cf. [3]).
The Ginibre ensemble and its polyanalytic generalization. The case Q(z) = |z|2
of (1.5) (or (1.2) is known as the Ginibre ensemble. The (probability generating or
reproducing) kernel is now particularly simple:
Km,n(z, w) = m
n−1
X
j=0
(mz ¯w)j
j!
.
Here, S = ¯D, the closed unit disk. We will consider a family of generalizations of
the Ginibre ensemble, the polyanalytic Ginibre ensembles, which are deﬁned by the
reproducing kernels Km,n,q of the subspaces
Polm,n,q := span
n
zjzk : 0 ≤j ≤n −1, 0 ≤k ≤q −1
o
supplied with the Hilbert space structure of L2(C, e−m|z|2). The parameter value
q = 1 corresponds to the standard Ginibre process. In general, we now project to
the nq-dimensional subspace of the polyanalytic polynomials, where the degree in ¯z
is ≤q −1, and the degree in z is ≤n −1. Note that the dimension of the subspace
is now nq and not n. We can think of the case q > 1 as permitting more Landau
levels than the lowest one (there are two similar models, see [5], [19], [25]; see also
[1]). We will keep the polyanalyticity degree q ﬁxed in the process, while we let
both m, n tend to inﬁnity. We remark here that we have noticed that Tomoyuki
Shirai is interested in a similar model [22].
As for the point process, the points generally repel each other, but for q > 1,
they also tend to avoid certain geometric conﬁgurations, such as circles and lines.
We have run a simulation in Figure 1.1.
Results. Macroscopically, we ﬁnd that the behavior of the polyanalytic Ginibre
ensemble is similar to that of the Ginibre ensemble. If we measure this in terms of
the Berezin measure, we have that as m, n →+∞while n = m + O(1),
dB⟨z⟩
m,n,q →dδz for z ∈¯D,
dB⟨z⟩
m,n,q →dωz for z ∈De,
where ωz is the harmonic measure of z with respect to the exterior disk De. Here,
Km,n,q is the reproducing kernel for Polm,n,q, and we use the notation
dB⟨z⟩
m,n,q(w) := B⟨z⟩
m,nq(w)dA(w),
B⟨z⟩
m,n,q(w) :=
|Km,n,q(z, w)|2
Km,n,q(z, z) e−mQ(w),
for the corresponding Berezin measure and Berezin density. Interestingly, the
microscopic behavior of the Berezin measure dB⟨z⟩
m,n,q is quite diﬀerent for q > 1
compared with the Ginibre case q = 1. In terms of the blow-up Berezin density
(∆Q(z) = ∆|z|2 ≡1 here)
ˆB⟨z⟩
m,n,q(ξ) = m−1 B⟨z⟩
m,n,q(z + m−1/2ξ),
6
Haimi and Hedenmalm
Figure 1.1. The polyanalytic Ginibre process with the kernel
Km,n,q with m = n = 61 and q = 3. The simulation is based on
the algorithm by Hough, Krishnapur, Peres, and Virág [15].
we have the following asymptotics as m, n →+∞while n = m + O(1):
ˆB⟨z⟩
m,n,q(ξ) −→q−1L1
q−1(|ξ|2)2e−|ξ|2
for z ∈D,
where L1
q−1 denotes the (generalized) Laguerre polynomial of degree q −1 with
parameter 1. It is well-known that the Laguerre polynomial L1
q−1 has exactly q −1
strictly positive roots, which implies that the Berezin density will exhibit a typical
Fresnel-type ring pattern. This resembles what happens in the one-dimensional
GUE case, where the zero density points for the Berezin density come from the
zeros of the sine kernel. Actually, the analogy is more than a superﬁcial similarity.
If we consider rather big values of q, and scale down to local distance (mq)−1/2,
with
˜B⟨z⟩
m,n,q(ξ′) = (mq)−1 B⟨z⟩
m,n,q

z + (mq)−1/2ξ′
,
then by the above we have, for z ∈D,
ˆB⟨z⟩
m,n,q(ξ) −→q−2L1
q−1(q−1|ξ′|2)2e−q−1|ξ′|2,
as m, n →+∞with n = m + O(1). Next, if we let q →+∞, we get that
q−2L1
q−1(q−1|ξ′|2)2e−q−1|ξ′|2 −→
 +∞
X
i=0
(−1)i|ξ′|2i
i!(i + 1)!
2
= J1(2|ξ′|)2
|ξ′|2
,
where J1 is the standard Bessel function. The identity
J1(2|ξ′|)
|ξ′|
=
Z
D
e2i Re[ξ′ ¯ζ]dA(ζ)
The Polyanalytic Ginibre Ensembles
7
shows that we are dealing with a planar analogue of the sine kernel (the sine
kernel is the Fourier transform of the characteristic function of the interval [−1, 1],
the one-dimensional unit ball).
We also investigate the local behaviour of the Berezin transform when |z| = 1,
i.e., when z is on the boundary of the bulk. Using the same blow-up scale as with
an interior point, we show that the blow-up Berezin density ˆB⟨z⟩
m,n,q(ξ) tends to
a limit which can be expressed in terms of Hermite polynomials (see Theorem
5.10). Here, too, there is a ring-like pattern in the interior direction, but it is not so
pronounced as it is for interior points (the bulk). We express the 1-point intensity
near a boundary point in terms of a sum of squares of Hermite polynomials. The
Wigner semi-circle law then gives the asymptotic behavior of the 1-point function,
which tells us the intensity of the process. We ﬁnd that for big q, but much bigger
m, n with m = n + O(1), the 1-point function is nontrivial in the annulus
1 −q1/2m−1/2 ≤|z| ≤1 + q1/2m−1/2;
inside it is essentially constant, and outside it more or less vanishes. Near the
outward boundary of the annulus at the scale (mq)−1/2, we expect the statistics of
the point process to be related with the well-known Airy process.
Lifting to two complex variables. Analogous results to [2] are obtained on com-
plex manifolds by Berman [6]. We note that the polyanalytic Ginibre processes can
also be viewed as processes in C2 with the rather singular weight e−|z1|2δ0(z1 −¯z2),
where δ0 is unit point mass at 0. Berman considers reproducing kernels of polyno-
mial subspaces as the total degree of the polynomials tends to inﬁnity. In contrast,
here we discuss the case where one variable has bounded degree and the degree
of the other variable goes to inﬁnity.
The polyanalyticGinibre ensembleandweighted interpolation. Itiswell known
in the theory of random matrices that
1
n! det[Km,n,1(zi, zj)]n
i,j=1 =
1
Zm,n,1
|∆(z1, ..., zn)|2,
where ∆(z1, ..., zn) = Πi,j:i<j(zj −zi) is the van der Monde determinant. A point
conﬁguration in a compact set which maximizes the van der Monde determinant
is known to be a good choice of nodes for Lagrange interpolation [21]. Instead of
considering points conﬁned to a compact set, one can add a weight to prevent the
points from going oﬀto inﬁnity. This leads to the same expression which arises in
the context of random eigenvalues.
We turn to the polyanalytic case. One shows that
1
(nq)! det[Km,n,q(zi, zj)]nq
i,j=1 =
1
Zm,n,q
|∆q(z1, ..., znq)|2,
where Zm,n,q is a normalization constant
Zm,n,q :=
Z
Cnq |∆q(z1, ..., znq)|2e−m Pnq
j=1 Q(zj)dA(z1) . . . dA(znq)
8
Haimi and Hedenmalm
and
∆q(z1, ..., znq) = det


1
. . .
1
z1
. . .
znq
...
. . .
...
zn−1
1
. . .
zn−1
nq
¯z1
. . .
¯znq
¯z1z1
. . .
¯znqznq
...
. . .
...
¯zq−1
1
. . .
¯zq−1
nq
...
. . .
...
¯zq−1
1
zn−1
1
. . .
¯zq−1
nq zn−1
nq


.
So, ∆q(z1, ..., znq) is the polyanalytic analogue of the van der Monde determinant.
As in the case q = 1 (which gives the usual van der Monde determinant), the
expression |∆q(z1, ..., znq)|2 measures how good the conﬁguration is for Lagrange
interpolation by polyanalytic polynomials. So, the polyanalytic Ginibre ensemble
is a way to produce random Lagrange interpolation sets, using the Gaussian
weight for conﬁnement.
Further results and open problems. In [20] and [3], the authors showed that the
ﬂuctuations of eigenvalues of random normal matrices tend to Gaussian free ﬁeld.
The ﬂuctuations of the polyanalytic Ginibre process will be discussed in a separate
paper – the limit is again the Gaussian free ﬁeld, but the variance depends on the
degree of polyanalyticity.
One could naturally address all the questions discussed in this article with
a more general weight Q. We conjecture that the spectral droplet will be the same
as in the analytic case. It is also likely that the blow-up of the Berezin density
at a bulk point z will have a universal limit, which we here computed to be
q−1L⟨1⟩
q−1(|ξ|2)2e−|ξ|2.
