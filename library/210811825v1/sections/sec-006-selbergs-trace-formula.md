---
doc_id: 210811825v1
doc_title: "Properties of Eigenvalues on Riemann Surfaces with Large Symmetry Groups"
section_id: sec-006-selbergs-trace-formula
section_title: "Selberg's trace formula"
section_number: null
pages: 53-60
source_pdf: 2108.11825v1.pdf
source_sha256: 1c2a4b317d6239c5
toc_source: outline
doc_brief: "Properties of Eigenvalues on Riemann Surfaces with Large Symmetry Groups — 26 sections: Front matter; Introduction; Background"
---
We start by following the basic presentation of the trace formula given in [10, 38, 56].
Recall that a hyperbolic surface S can be represented as a quotient of the hyperbolic
plane by a Fuchsian group that only has hyperbolic elements (with the exception of the
43
identity), that is, S ∼= Γ \ H. The space of square integrable functions on S comes from
the functions f ∈L2(H) that are invariant under the action of an isometry
Tγ(z)f = f(γ−1z) = f(z),
γ ∈Γ,
and are square integrable over any fundamental domain FΓ of Γ (recall Deﬁnition 2.26).
We obtain the Hilbert space L2(Γ \ H) by deﬁning the obvious inner product
⟨f1, f2⟩=
Z
FΓ
f1f2dµ
on these functions, where dµ is the Riemannian measure. In a similar way, we can identify
functions in C∞(Γ \ H) with the functions in C∞(H) that are invariant under the action
of Tγ, γ ∈Γ. We have seen that the Laplacian commutes with isometries; as a result it
commutes with Tγ and thus maps C∞(H) →C∞(H).
Deﬁnition 2.43 (Point pair invariant) A point pair invariant for a Fuchsian group
Γ is a function k : H × H →C that satisﬁes the following relations:
1. k(γz, γw) = k(z, w) for all γ ∈Γ, z, w ∈H;
2. k(z, w) = k(w, z) for all z, w ∈H.
Such a function k(z, w) depends on the hyperbolic distance d(z, w) = u between the
two points. In this way, we can view k as a function of one non-negative variable k(u).
If we take k(z, w) to be the kernel of an integral operator
(Lf)(z) =
Z
H
k(z, w)f(w)dµ,
then L is invariant under the action of Isom(H). Both the Laplacian and L are invariant
under isometries, and in particular, we have the following theorem (see [38, Theorem
1.9]):
Theorem 2.44 The invariant integral operators commute with the Laplace operator.
This commutative property gives a relation between eigenfunctions of the Laplacian
and those of the invariant integral operators; in particular, if f is a solution to
(∆f −λf) = 0,
where λ = 1
2 + t2, then it is also a solution to
Lf = h(t)f,
where h(t) can be computed from k(z, w) using the Selberg/Harish-Chandra transform
[38]:
q(v) =
Z ∞
v
k(u)(u −v)−1
2du,
44
g(r) =2q

sinh
r
2
2
,
h(t) =
Z ∞
−∞
eirtg(r)dr.
To study the spectrum of the Laplacian on Γ \ H, note that the point pair invariant
on H × H induces a point pair invariant on Γ \ H × Γ \ H with
kΓ(z, w) =
X
γ∈Γ
(γz, w).
This allows us to deﬁne an invariant integral operator
(Kf)(z) =
Z
Γ\H
kΓ(z, w)f(w)dµ
on functions f ∈C∞(Γ \ H). If such an f is an eigenfunction of the Laplacian, then it
again satisﬁes
Kf = h(t)f,
since
Z
FΓ
kΓ(z, w)f(w)dµ =
Z
H
k(z, w)f(w)dµ,
where FΓ is a fundamental domain for Γ \ H.
Remark 2.45 In this presentation, we have given little attention to the convergence of
the various series and integrals considered - the ﬁner details can be found in [56]. The
relation between eigenfunctions of the Laplacian and of the invariant integral operators
depends on k being smooth, and of compact support, on H (or Γ\H). It is more common to
specify conditions on the spectral function h(t), since this function, along with its Fourier
transform, appear in Selberg’s trace formula below. In particular, we require the following
conditions:
(i) h is analytic on |ℑ(t)| ≤σ for some σ > 1
2;
(ii) h(t) = h(−t);
(iii) |h(t)| ≪(1 + ℜ(t))−2−δ for ﬁxed δ > 0, uniformly ∀t in |ℑ(t)| ≤σ.
Let {ϕ0, ϕ1, . . .} ∈C∞(Γ \ H) be eigenfunctions of ∆, and recall that these form an
orthonormal basis of L2(Γ \ H). In particular, for f ∈C2(Γ \ H), we have the spectral
decomposition
f(z) =
X
j
⟨f, ϕj⟩ϕj(z).
Now for h(t) satisfying the conditions in Remark 2.45, we have the eigenvalue equation
Kϕj = h(tj)ϕj,
45
and the decomposition of our point pair invariant (see [56, Proposition 9])
kΓ(z, w) =
∞
X
j=0
h(tj)ϕj(z)ϕj(w).
Deﬁnition 2.46 (Trace class) Let FΓ be a fundamental domain for Γ \ H as above.
The integral operator with K with kΓ(z, w) as its kernel are of trace class if kΓ(z, w) is
absolutely integrable for z = w. The trace of K is
TrK =
Z
FΓ
kΓ(z, z)dµ.
Selberg’s trace formula allows us to compute TrK in two diﬀerent ways; one using the
spectral decomposition of kΓ, and the other using the geometry of Γ. First, we integrate
over the spectral decomposition of kΓ, that is
kΓ(z, z) =
X
j
h(tj)|ϕj(z)|2,
to get
TrK =
X
j
h(tj),
since the ϕj are orthonormal. This gives us the spectral side of the formula. Now recall
kΓ(z, z) =
X
γ∈Γ
k(γz, z).
Taking the trace of K, we get
TrK =
X
γ∈Γ
Z
FΓ
kΓ(γz, z)dµ.
Let [γ] denote the conjugacy class of an element of Γ, that is
[γ] =

˜γ ∈Γ | ˜γ = τγτ −1 for some τ ∈Γ
	
.
We deﬁne the partial kernel over a conjugacy class to be
k[γ](z, z) =
X
γ∈[γ]
k(γz, z).
Note that
kΓ(z, z) =
X
[γ]
k[γ](z, z)
and
TrK =
X
[γ]
TrK[γ],
where K[γ] is the integral operator that has kernel k[γ]. The centralizer of γ is
Zγ = {τ ∈Γ | τγ = γτ} .
46
Two elements τ, τ ′ ∈Γ give the same conjugate of γ if and only if τ ′τ −1 belongs to
the centralizer of γ. The upshot is that the fundamental domain of the centralizer of a
hyperbolic element is in general much simpler than that of the fundamental domain FΓ
(and therefore the integrals over such a domain are much simpler). Such a fundamental
domain is shown in Figure 2.4.
i
Figure 2.4: Fundamental domain for the centralizer of a hyperbolic element
For γ ∈[γ]
TrK[γ] =
X
τ∈Zγ\Γ
Z
FΓ
k(τ−1γτz, z)dµ
=
Z
Zγ\H
k(γz, z)dµ.
This depends only on [γ], that is, if γ′ = g−1γg, g ∈SL2(R), then
TrK[γ] =
Z
g−1Z(γ)g\H
k(g−1γgz, z)dµ = TrK[γ′].
The integral depends only on the distance d(z, γz), and can be explicitly computed
(see [38, Sections 10.4 and 10.5]). The most common version of the trace formula is for
compact Riemann surfaces, where there are only hyperbolic conjugacy classes (and the
identity motion). There is an exact correspondence between hyperbolic conjugacy classes
and the lengths of primitive geodesics (multiple loops are not included), so this is the
most interesting version for seeing the relation between the energy and length spectra.
Theorem 2.47 (Selberg’s trace formula, [74]) Let h(t) be as above, and let g(t) be
its Fourier transform. Let S be a compact Riemann surface. Then
∞
X
j=0
h(tj) = Area(S)
4π
Z ∞
−∞
h(t) tanh(πt)tdt +
X
[γ]
∞
X
n=1
lγg(nlγ)
2 sinh(nlγ/2).
47
One interesting application of this theorem is to prove Weyl’s law, the famous formula
that describes the asymptotic properties of Laplace eigenvalues. We deﬁne the set of
eigenvalues below a certain value as
N(λ) = #j{λj ≤λ}.
Theorem 2.48 (Weyl’s law, [82]) Let S be a compact Riemann surface. Then
N(λ) ∼Area(S)
4π
λ,
λ →∞.
This can be proved by using the heat kernel
h(t) = e−βt2
with Fourier transform
g(s) = e−s2/2β
√4πβ
in Selberg’s trace formula, where β > 0. In particular, with λj = t2
j + 1
4, we take the limit
lim
β→0
∞
X
j=0
e−βλj,
and the result follows from a Tauberian theorem of Wiener-Ikehara (see Theorem 9.4.7
in [13]).
If one has information about the irreducible representations of the automorphism
group of a surface, one can consider a more general version of Selberg’s trace formula,
given in [9]. The advantage of this is that one can restrict the formula to a single unitary
character χ on Γ, that is, consider the space L2(Γ \ H, χ) rather than simply L2(Γ \ H).
L2(Γ \ H, χ) is the Hilbert space of functions f : H →C such that
f(Tz) ≡χ(T)f(z)
for all T ∈Γ and f ∈L2(Γ \ H).
Theorem 2.49 ( [9]) Let M be the set T ∈Γ such that T does not have a cusp of [Γ+] as
a ﬁxed point. Let I denote the identity action, and MI = M ∪[I]. Let F be a fundamental
domain for Γ\H. For each non-elliptic T ∈M, there exists a hyperbolic element or glide
reﬂection T0 ∈Z(T) such that the inﬁnite cyclic group
[T0] = {T n
0 | n ∈Z}
48
has index 1, 2, or 4 in Z(T). Then for each admissible h(t) we have
X
T∈MI
Z
Γ\H
χ(T)k(z, Tz)dµz = Area(F)
4π
Z ∞
−∞
h(t) tanh(πt)tdt
+
X
T∈M
non−ell
log N(T0)
[ZΓ(T) : [T0]]
χ(T)g(log N(T))
N(T)
1
2 −sgn(det T)N(T)−1
2
+
X
T∈M
elliptic
χ(T)
2|ZΓ(T)| sin(θ(T))
Z ∞
−∞
exp(−2θ(T)t)
1 + exp(−2πt)h(t)dt,
where the [T] sums are taken over distinct conjugacy classes of Γ, and the non-elliptic sum
consists of conjugacy classes where T is a reﬂection, hyperbolic transformation or glide
reﬂection (see Section 2.2 on hyperbolic geometry; also for θ). The sums and integrals are
all convergent with good majorants. The elliptic sum is ﬁnite. Note the sgn function in
the non-elliptic sum, which distinguishes between orientation preserving and orientation
reversing isometries.
This theorem is interesting in that it includes orientation reversing isometries. The
disadvantage is that it only applies to unitary characters. For characters of higher di-
mensional irreducible representations, Theorem 4.1 in Chapter 8 of [33] provides a similar
formula, although this does not deal with reﬂections. One might conjecture that it is pos-
sible to combine the two formulae to get a more general version of Selberg’s trace formula
for characters of higher dimensional representations of an automorphism group that in-
cludes reﬂections.
49
Chapter 3
The Bolza Surface
