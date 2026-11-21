---
doc_id: arxiv-1701.06567v2
doc_title: "BPS spectra and 3-manifold invariants"
section_id: sec-033-44-comparison-with-refined-cs
section_title: "Comparison with refined CS"
section_number: 4.4
pages: 66-72
source_pdf: 1701.06567v2.pdf
source_sha256: c1610b50f5a7e22c
toc_source: inferred
doc_brief: "BPS spectra and 3-manifold invariants — We provide a physical deﬁnition of new homological invariants Ha(M3) of 3- manifolds (possibly, with knots) labeled by abelian ﬂat connections."
---
In this section, we wish to compare the categoriﬁcation of WRT invariants of knots in 3-
manifolds considered in the previous section with analogous calculations using the tools of
reﬁned CS theory and DAHA [19,72]. To the best of our knowledge, such calculations (that
involve both knots and 3-manifolds) were not done in the literature on reﬁned Chern-Simons
theory.
Let us consider the unknot K wrapping the Hopf ﬁber in M3 = L(p, 1) and colored by
an irreducible representation R = λ. Note, that now the representation λ (whose weight we
denote by the same letter) does represent the “color” of K ⊂M3. The partition function of
the reﬁned CS theory with such insertion can be expressed through S and T matrices (listed
in section 3.2.6) as follows:
Zref. CS
SU(2) [L(p, 1); K, λ] =
k−1
X
n=1
g−1
n S1nSn,λ+1(Tnn)−p =
=
k−1
X
n=1
q−pn2
4 −pnβ
2 −pβ2
4
β
Y
j=0
(q−n+j+β
2
−q
n+j+β
2
)(q−n−j+β
2
−q
n−j+β
2
) Mλ(qβ+n).
(4.54)
where Mλ(x) is the SU(2) Macdonald polynomial, whose coeﬃcients are rational functions
of q and t = qβ. By repeating the manipulations of section 3.2.6, we obtain (up to the same
simple overall factor):
Zref. CS
SU(2) [L(p, 1); K, λ] =
X
a,b∈Zp/Z2
e2πi(k+2β)CS(a) · Sab ·
1
|Wb|
bZ(ref.CS;β)
b
(q; K, λ)
(4.55)
with
bZ(ref.CS;β)
a
(q; K, λ) =
Z
dz
2πiz (z±2; q)β+1 Mλ(z2)
X
n∈pZ+a
qn2/p z2n =
=
Z
dz
2πiz
 (z±2; q)∞
(z±2qt; q)∞

Mλ(z2)
X
n∈pZ+a
qn2/p z2n

t=qβ
(4.56)
For λ = 1, the Macdonald polynomial coincides with the Schur polynomial, M1(z2) = χ1(z),
and the expression above agrees with the D2 × S1 partition function with a Wilson line
insertion (4.48). However, in order to ﬁnd an agreement for more general λ, we need to make
– 65 –
a replacement χλ(z) →Mλ(z2) in (4.48). At the catogoriﬁed level, this means that (4.22)
needs to be replaced by
Wλ
⇝
M
µ≤λ
Wµ ⊗Hµ
λ
(4.57)
where Hµ
λ are appropriate categoriﬁcations of the coeﬁﬁcients Cµ
λ(q, t) in the decomposition
Mλ(z2) = P
µ≤λ Cµ
λ(q, t)χµ(z). This suggests that the insertion of the Macdonald polynomial
in the partition function of 3d N = 2 theory T[M3] corresponds to a λ-colored unknot
wrapping the Hopf ﬁber of M3, cf. (4.22):
Mλ(z2)
↔
K = unknot along the Hopf ﬁber colored by R = λ
(4.58)
It would be interesting to test this against many examples of λ-colored sl(N) homology for
various knots and links [43,44,72,79,83–85].
Note, that the coeﬃcients in fusion rules of Macdonald polynomials are non-trivial ra-
tional functions of q, t. Therefore, the dependence on λ in (4.56) does not agrees with the
cabling formula, unlike the case of Wilson line insertions. On the other hand, the dependence
on framing in the reﬁned CS is simple and is given by the corresponding power of the matrix
element Tλ+1,λ+1. In particular, when p = 1 the result of (4.56) is
bZ(ref.CS;β)
0
(q; K, λ)
bZ(ref.CS;β)
0
(q)
= Tλ+1,λ+1Mλ(qt).
(4.59)
Note that, for λ > 1, it is a nontrivial rational function of q and t, which means that the
underlying doubly graded vector space is inﬁnite dimensional, unlike the ﬁnite dimensional
vector spaces produced by Wilson line insertions (see Appendix B).
Acknowledgments
We would like to thank J. E. Andersen, M. Aganagic, F. Benini, C. Cordova, A. Gadde,
E. Gorsky, K. Hori, H. Kim, S. Nawata, M. Romo, S. Shakirov, L. Rozansky and K. Ye for
useful comments and discussions. The work of S.G. and D.P. is supported in part by the
U.S. Department of Energy, Oﬃce of Science, Oﬃce of High Energy Physics, under Award
Number DE-SC0011632. In addition, the work of D.P. is supported by the center of excellence
grant “Center for Quantum Geometry of Moduli Space” from the Danish National Research
Foundation (DNRF95). P.P. gratefully acknowledges the support from Marvin L. Goldberger
Fellowship and the DOE Grant DE-SC0009988. The research of C.V. is supported in part
by NSF grant PHY-1067976. This work was performed in part (by P.P.) at Aspen Center
for Physics which is supported by National Science Foundation grant PHY-1066293. The
authors would like to thank Simons Center for Geometry and Physics and the organisers of
the Simons Summer Workshop 2016, where the work on the project has begun, for generous
hospitality.
– 66 –
A. Z[[q]]-valued invariant for negative deﬁnite plumbed 3-manifolds
We are interested in obtaining a certain analytic continuation of su(2)k WRT invariant [86,87]
of a plumbed 3-manidfold M3(Γ),54 where Γ is a tree. Let us ﬁrst consider the case of positive
integer level, with k ∈Z+. The colored Jones polynomial of link L(Γ) is explicitly known
(see e.g. [87])55:
J[L(Γ)]n1,...,nL =
2i
q1/2 −q−1/2
Y
v ∈Vertices ∼
= {1,...,L}
q
av(n2v−1)
4

2i
qnv/2 −q−nv/2
deg(v)−1
×
Y
(v1,v2) ∈Edges
qnv1nv2/2 −q−nv1nv2/2
2i
(A.2)
where q = e2πi/k.56 For the purposes of computing the WRT invariant of 3-manifold obtained
by Dehn surgery on a link L(Γ), it is useful to consider the following quantity:
F[L(Γ)] ≡
X
n∈{1,...,k−1}L
J[L(Γ)]n1,...,nL
L
Y
v=1
qnv/2 −q−nv/2
q1/2 −q−1/2 .
(A.3)
Then the WRT invariant of M3(Γ) is given by [86]57
τ[M3(Γ)] =
F[L(Γ)]
F[L(+1•)]b+F[L(−1•)]b−
(A.5)
where b± are the number of positive/negative eigenvalues of the linking matrix M while ±1•
denotes a plumbing graph with one vertex corresponding to an unknot with ±1 framing. The
SU(2)k CS partition function, in the usual physical normalization, with
ZSU(2)k[S2 × S1] = 1,
(A.6)
diﬀers from (A.5) by a simple factor:
ZSU(2)k[M3(Γ)] =
r
2
k sin π
k · τ[M3(Γ)].
(A.7)
54Everything below in principle can be generalized to su(N) and u(N).
55We use the normalization in which the colored Jones polynomial of unlink with L components with
canonical framing is given by
J[Unlink]n1,...,nL =
L
Y
v=1
qnv/2 −q−nv/2
q1/2 −q−1/2 .
(A.1)
56In this appendix, we use q to denote a k-th (k ∈Z+) root of unity e
2πi
k
and reserve q to denote the
corresponding continuous variable which will appear in analytic continuation.
57Normalized such that
τ[S3] = 1.
(A.4)
– 67 –
The following Gauss sum reciprocity formula will be very useful for us (see e.g. [88,89]):
X
n ∈ZL/2kZL
exp
 πi
2k(n, Mn) + πi
k (ℓ, n)

=
e
πiσ
4 (2k)L/2
| det M|1/2
X
a ∈ZL/MZL
exp

−2πik

a + ℓ
2k, M−1

a + ℓ
2k

(A.8)
where ℓ∈ZL, (·, ·) is the standard pairing on ZL and σ = b+ −b−is the signature of the
linking matrix M. In particular, from this formula it follows that
F[L(±1•)] =
k−1
X
n=1
q± n2−1
4
 
qn/2 −q−n/2
q1/2 −q−1/2
!2
= (2k)1/2 e± πi
4 q∓3
4
q1/2 −q−1/2
.
(A.9)
Therefore
τ[M3(Γ)] =
e−πiσ
4 q
3σ
4
2 (2k)L/2 (q1/2 −q−1/2)×
X
n∈ZL/2kZL
′
Y
v ∈Vertices
q
av(n2v−1)
4

1
qnv/2 −q−nv/2
deg(v)−2
×
Y
(v′,v′′) ∈Edges
qnv′nv′′/2 −q−nv′nv′′/2
2
(A.10)
where we used invariance of the summand under nv ↔−nv and the fact that L−|Edges| = 1.
The prime ′ in the sum means that the singular values nv = 0, k are omitted.
Consider the following factor in the expression above:
Y
(v′,v′′) ∈Edges
(qnv′nv′′/2 −q−nv′nv′′/2) =
X
s∈{±1}Edges
Y
(v′,v′′) ∈Edges
s(v′,v′′)qs(v′,v′′)nv′nv′′/2. (A.11)
If one picks a vertex v and makes a change nv →−nv, a term in the sum with a given
conﬁguration of signs associated to edges (that is s ∈{±1}Edges) will transform into a term
with a diﬀerent conﬁguration times (−1)deg v. Using the fact that the graph Γ is a tree, by a
sequence of such transforms, any conﬁguration of signs can be brought to the conﬁguration
with all signs +1. Therefore (A.10) can be rewritten as follows:
τ[M3(Γ)] =
e−πiσ
4 q
3σ−P
v av
4
2 (2k)L/2 (q1/2 −q−1/2)×
X
n∈ZL/2kZL
′ q
(n,Mn)
4
Y
v ∈Vertices

1
qnv/2 −q−nv/2
deg(v)−2
.
(A.12)
– 68 –
Before we can apply (A.8) to (A.12) we need to explicitly regularize the sum. In order to do
this, let us introduce the following auxiliary quantities:
∆v ∈Z+ : ∆v = deg v −1
mod 2,
∀v ∈Vertices,
(A.13)
ω ∈C :
0 < |ω| < 1.
(A.14)
Then
X
n∈ZL/2kZL
′ q
(n,Mn)
4
Y
v ∈Vertices

1
qnv/2 −q−nv/2
deg(v)−2
=
lim
ω→1
1
2L
X
n∈ZL/2kZL
q
(n,Mn)
4
Fω(x1, . . . , xL)|xv=qnv/2
(A.15)
where
Fω(x1, . . . , xL) =
Y
v ∈Vertices
(xv −1/xv)∆v
(
1
xv −ω/xv
deg(v)−2+∆v
+

1
ωxv −1/xv
deg(v)−2+∆v)
ω≈0
=
X
m≥0
X
ℓ∈Im
Nm,ℓ
Y
v
xℓv
v
· ωm
∈Z[x±1
1 , . . . , x±1
L ][[ω]]
(A.16)
with Im being a ﬁnite set of elements from ZL. If, after expansion in ω one collects coeﬃcients
in front of powers of x, the expression has the following form:
Fω(x1, . . . , xL)
Formally
====
X
ℓ∈2ZL+δ
F ℓ
ω
Y
v
xℓv
v
∈Z[ω][[x±1
1 , . . . , x±L
1 ]]
(A.17)
where
F ℓ
ω =
X
m: ℓ∈Im
Nm,ℓωm
∈Z[ω]
(A.18)
and
δ ∈ZL/2ZL,
δv ≡deg v
(mod 2).
(A.19)
Note that F ℓ
1 = P
m Nm,ℓ∈Z does not depend on the choice of ∆∈ZL in (A.13). Formally,
F1(x1, . . . , xL) =
X
ℓ∈2ZL+δ
F ℓ
1
Y
v
xℓv
v =
Y
v ∈Vertices

Expansion
at x →0
1
(xv −1/xv)deg v−2 + Expansion
at x →∞
1
(xv −1/xv)deg v−2

.
(A.20)
– 69 –
Now let us assume that the quadratic form M : ZL × ZL →Z is negative deﬁnite, 58i.e. σ =
−L). Then we can deﬁne the following q-series, convergent for |q| < 1:
bZb(q) Def
== 2−Lq−3L+P
v av
4
X
ℓ∈2MZL+b
F ℓ
1 q−(ℓ,M−1ℓ)
4
∈2−cq∆bZ[[q]]
(A.21)
where
c ∈Z+,
c ≤L,
(A.22)
b ∈(2ZL + δ)/2MZL /Z2 ∼= (2Coker M + δ) /Z2
Set
∼= H1(M3, Z) /Z2,
(A.23)
∆b = −3L + P
v av
4
−
max
ℓ∈2MZL+b
(ℓ, M−1ℓ)
4
∈Q
(A.24)
where Z2 acts as follows:
b →−b
(A.25)
which is a symmetry of (A.21).
Using relation (A.15) and applying Gauss reciprocity formula (A.8) we arrive at the
following expression for the WRT invariant:
τk[M3(Γ)] =
e−πiσ
4 q−3L+P
v av
4
2 (2k)L/2 (q1/2 −q−1/2) lim
ω→1
X
n∈ZL/2kZL
q
(n,Mn)
4
Fω(x1, . . . , xL)|xv=qnv/2 =
2−Lq−3L+P
v av
4
2 (q1/2 −q−1/2) | det M|1/2
X
a ∈Coker M
b ∈2Coker M + δ
e−2πi(a,M−1b)e−2πik(a,M−1a)×
lim
ω→1
X
ℓ∈2MZL+b
F ℓ
ω q−(ℓ,M−1ℓ)
4
.
(A.26)
Now, assume that the limit limq→q bZb(q), where bZb(q) is deﬁned in (A.21) and q ap-
proaches k-th primitive root of unity from inside of the unit disc |q| < 1, exists and moreover,
lim
ω→1
X
ℓ∈2MZL+b
F ℓ
ω q−(ℓ,M−1ℓ)
4
= lim
q→q
X
ℓ∈2MZL+b
F ℓ
1 q−(ℓ,M−1ℓ)
4
.
(A.27)
Then
τk[M3(Γ)] =
1
2 (q1/2 −q−1/2) | det M|1/2 ×
X
a∈Coker M
e−2πik(a,M−1a)
X
b∈2Coker M+δ
e−2πi(a,M−1b) lim
q→q
bZb(q).
(A.28)
58In principle, this condition can be relaxed. It is only necessary that M is negative on a certain subspace
of ZL.
– 70 –
We do not provide a proof of (A.27), and therefore (A.28), but believe it should be similar
to the proof of the similar statement in [90]. However, even without the relation (A.28), the
formula (A.21) provides an invariant of negative-deﬁnite plumbed 3-manifolds valued in q-
series with integer coeﬃcients. As was already mentioned before, the resulting q-series do not
depend on the auxiliary choices of ∆v in (A.16). One can show that they are also invariant
under the action of Kirby moves (see Figure 6) acting on Γ, and therefore indeed depend only
on homeomorphism class of M3(Γ).
The formula (A.21) for the homological blocks bZa can also be rewritten as a contour
integral:
bZb(q) = q−3L+P
v av
4
· v.p.
Z
|zv|=1
Y
v ∈Vertices
dzv
2πizv
(zv −1/zv)2−deg(v) · Θ−M
b
(z)
(A.29)
where Θ−M
b
(x) is the theta function of the lattice corresponding to minus the linking form
M:
Θ−M
b
(x) =
X
ℓ∈2MZL+b
q−(ℓ,M−1ℓ)
4
L
Y
i=1
xℓi
i
(A.30)
and “v.p.” again means that we take principle value integral (i.e. take half-sum of contours
|zv| = 1 ± ϵ). Such prescription corresponds to regularization by ω made in (A.16).
