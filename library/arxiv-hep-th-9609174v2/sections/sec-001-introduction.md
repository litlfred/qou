---
doc_id: arxiv-hep-th-9609174v2
doc_title: "Universality of random matrices in the microscopic limit and the Dirac operator spectrum"
section_id: sec-001-introduction
section_title: "Introduction"
section_number: null
pages: 2-8
source_pdf: 9609174v2.pdf
source_sha256: 87885f4d03661f26
doc_brief: "Universality of random matrices in the microscopic limit and the Dirac operator spectrum — We prove the universality of correlation functions of chiral unitary and unitary ensembles of ran- dom"
---
Consider a four-dimensional gauge theory coupled to fermions in given representations of the
gauge group, and with given global (and possibly spontaneously broken) ﬂavor symmetries. In
the chiral limit, the associated Dirac operator iD/ anticommutes with γ5,
{iD/, γ5} = 0 .
(1.1)
This means that the associated eigenvalues of iD/, deﬁned by iD/ φn = λnφn appear symmetrically
around zero: ±λn. The corresponding eigenfunctions are, for λn̸ = 0, φn and γ5φn. The accu-
mulation of eigenvalues near λ = 0 determines whether or not chiral symmetry is spontaneously
broken through the formation of a chiral condensate [1]. The study of the Dirac operator spec-
trum near λ = 0 is thus of fundamental importance for our understanding of chiral symmetry
breaking in gauge theories. For example, for QCD with Nf ﬂavors it is expected to lead to the
conventional SU(Nf)L × SU(Nf)R →SU(Nf)V scenario, with all its implications in terms of
low-energy eﬀective Lagrangians.
In a series of papers [2, 3, 4], Verbaarschot and collaborators have added substantial new insight
to this issue. Their central assertion is that the spectral density of the Dirac operator very close
to the origin λ = 0 should be universal, depending only on the symmetries in question. One
startling consequence of this conjecture is that the spectral density of the Dirac operator near the
origin need not be computed in the gauge theory at all, but can be extracted from much simpler
random matrix theories.
The pertinent random matrix ensemble is determined by symmetry
arguments alone. To ﬁnd universal features of the Dirac spectrum near the origin, it is essential
to ﬁrst consider the problem in a ﬁnite volume V4, corresponding in matrix-model terms to ﬁnite-
size matrices, and then magnify the spectrum near the origin at a scale of order 1/V4. The usual
spectral density ρ(λ) is deﬁned by the following average over gauge ﬁeld conﬁgurations:
ρ(λ) =
X
n
⟨δ(λ −λn)⟩.
(1.2)
By the Banks-Casher relation∗[1] (taking here the limit V4 →∞),
⟨¯ψψ⟩= 1
V4
lim
m→0 2m
Z ∞
0
dλ
ρ(λ)
λ2 + m2 = πρ(0)
V4
,
(1.3)
this spectral density, evaluated at the origin, is directly related to the appearance of a chiral
condensate. It follows that the average spacing between eigenvalues becomes roughly constant
near λ = 0 [5],
∆λ ∼
π
V4⟨¯ψψ⟩.
(1.4)
Magnifying ρ(λ) near λ = 0 according to the prescription given above thus entails the introduction
of an associated microscopic spectral density ρS(λ), which is deﬁned by [2]
ρS(λ) =
lim
V4→∞
1
V4
ρ
 λ
V4

.
(1.5)
∗Applied na¨ıvely here, ignoring the subtlety of regularization.
1
The precise statement is that this microscopic spectral density should be a universal function.
The most compelling evidence comes from the fact that the microscopic spectral density deﬁned
as above, and evaluated in a particular random matrix theory, exactly reproduces the Leutwyler-
Smilga spectral sum rules [5] and appropriate generalizations [6].
To understand the signiﬁcance of this universality conjecture, let us for convenience ﬁrst focus
on one example, that of QCD with Nf massless fermions in the fundamental representation. As
explained in refs. [2], the relevant matrix model partition function is given by a chiral unitary
ensemble of the form
ZχUE =
Z
dW detNf
 
0
W †
W
0
!
e−Ntr V (W †W ) .
(1.6)
Here only symmetry arguments alone have selected the integration to be over complex N × N
matrices, and the Dirac operator structure is encoded in the determinant. But such symmetry
arguments alone place no restrictions on the form of V (λ), which appears in the exponent. If
indeed symmetry arguments alone should determine the microscopic spectral density of QCD from
this matrix ensemble, then any reasonable choice of V (λ) should give the same result for ρS(λ).
This universality argument, if correct, allows us to evaluate the integral with a function V (λ)
of our own choice. Some hints supporting this universality had been found in refs. [7]. Clearly,
the most convenient choice in to make the matrix integral Gaussian except for the determinant
factor in front. This is the choice made in refs. [2].
It is important to separate the question of universality of the spectral density of the Dirac opera-
tor close to the origin into two parts. The ﬁrst concerns the crucial jump from the d-dimensional
gauge ﬁeld integrations to the framework of zero-dimensional matrix models with similar symme-
tries. The second step concerns the conjecture about the universality of the microscopic spectral
density within the framework of matrix models. The purpose of this paper is to prove the latter
of these universality conjectures. The question of whether the universality extends all the way
from zero-dimensional large-N matrix models to full-ﬂedged quantum ﬁeld theories such as QCD
will of course remain unproven. But we shall show, within the context of large-N matrix models,
under what conditions the microscopic spectral density and higher correlation functions are uni-
versal. This is a major step towards understanding the original issue, which concerns the possible
universality of also the Dirac operator spectrum near λ = 0.
This paper is organized as follows. In section 2 we prove a theorem for the asymptotic behavior
of generic orthogonal polynomials over a semi-inﬁnite range. By making use of this theorem, we
compute the associated universal form of the microscopic spectral density as well as all higher
order correlation functions in the same limit.
This universality class is of relevance for four-
dimensional SU(Nc ≥3) gauge theories with fermions in the fundamental representation.
In
section 3 we repeat the analysis for a class of orthogonal polynomials over an inﬁnite range. This
case is considered to be relevant for three-dimensional SU(Nc ≥3) gauge theories with an even
number of fermions in the fundamental representation. We conclude in section 4 with a discussion
about the possible relation between the chiral-ﬂavor (or parity-ﬂavor) symmetry breaking in gauge
2
theories and the now established universality of random matrices in the microscopic limit.
2
Chiral unitary ensembles
In this section we consider the chiral unitary ensemble:
Z =
Z
dM detNf M exp

−N
2 tr V (M2)

,
V (M2) =
X
k≥1
gk
k M2k,
Nf = 0, 1, · · ·
(2.1)
where M stands for an (N + N ′) × (N + N ′) block hermitian matrix whose non-zero components
are N × N ′ complex matrices on the oﬀ-diagonals,
M =
 
0
W †
W
0
!
(2.2)
and dM the Haar measure of W. We take N ≤N ′ without loss of generality. An ensemble is
called chiral unitary because of the invariance under the transformation
W 7→V † W U ,
U ∈U(N) ,
V ∈U(N ′).
(2.3)
This model has the same global symmetries as a Euclidean four-dimensional SU(Nc ≥3) gauge
theory coupled to Nf massless fermions in the fundamental representation. The topological charge
ν of the vacuum is identiﬁed with |ν| = N ′−N (which is kept ﬁxed) and the volume of space-time
is V4 = N + N ′ (which is sent to inﬁnity afterwards). Speciﬁcally, due to the “U(1)A symmetry”
{M, γ5} = 0,
γ5 =
 
1N
0
0
−1N′
!
,
(2.4)
all (2N) non-zero eigenvalues M occurs in pairs with opposite signs.
The partition function (2.1) is expressible in terms of the component matrices as well as of the
eigenvalues after integration over the angular coordinates (U, V ) ∈U(N) × U(N ′)/U(1)N [8],
Z
=
Z
dW detNf

W †W

e−NtrV (W †W )
∝
Z ∞
−∞
N
Y
i=1

dz2
i z2α
i
e−NV (z2
i ) 

det
ij z2(i−1)
j

2
=
Z ∞
0
N
Y
i=1

dλi λα
i e−NV (λi) 

det
ij λi−1
j

2
,
(2.5)
where we have set α = Nf + |ν| and suppressed an irrelevant constant of the angular integration.
The above expression can be interpreted as a positive deﬁnite N × N hermitian matrix model in
H = W †W whose eigenvalues are λ1, · · · , λN ≥0. Therefore the problem is reduced to ﬁnding a
3
set of orthogonal polynomials P (α)
n
(λ) over the semi-inﬁnite interval [0, ∞) with the shown weight
function,
Z ∞
0
dλ λα e−NV (λ)P (α)
n
(λ) P (α)
m (λ) = h(α)
n
δnm.
(2.6)
The deﬁnition of the orthogonality relation (2.6) shows that the problem is well-deﬁned for
arbitrary real α > −1. Here we shall only deal with α to be a nonnegative integer, which is
motivated physically from the above.
In the orthogonal polynomial method, the polynomials P (α)
n
(λ) are usually normalized to be
monic,
P (α)
n
(λ) = λn + · · · ,
(2.7)
so that the Vandermonde determinant detij λi−1
j
can be substituted by detij P (α)
i−1(λj) in the inte-
grand. However, for the present purposes we will employ a diﬀerent normalization by demanding
P (α)
n
(0) = 1:
P (α)
n
(λ) = 1 + · · · + p(α)
n λn.
(2.8)
This is because we shall seek a smooth limiting behavior near λ = 0 as n gets as large as N
(which is taken to inﬁnity), and N 2λ is kept ﬁxed at the same time (the microscopic limit). We
thus start by the assumption that P (α)
n
(0)̸ = 0, and normalize the polynomials accordingly.† As
we shall see shortly, this assumption is equivalent to having the origin included in the support of
the spectral density.
2.1
Asymptotics of orthogonal polynomials
We shall prove the following theorem on the asymptotic behavior of these orthogonal polynomials:
Theorem 1: Let {P (α)
n
(λ)}n=0,1,··· be the set of polynomials orthogonal with respect
to the measure
dλ λα e−N V (λ),
V (λ) =
X
k≥1
gk
k λk,
α = 0, 1, · · ·
over the range [0, ∞), whose moments are all ﬁnite. If the polynomials can be nor-
malized according to P (α)
n
(0) = 1, then, for ﬁxed x = N 2λ and t = n/N, the following
limiting relation holds:
lim
N→∞P (α)
n
( x
N 2 )

n=Nt
= α! Jα (u(t)√x)
(u(t)√x/2)α ,
(2.9)
where u(t) is determined by
u(t) =
Z t
0
dt′
p
r(t′),
t =
X
k
gk
2
2k
k

r(t)k.
† We avoid a proliferation of new symbols by employing the same P (α)
n
(λ) and h(α)
n
in both conventions.
4
The proof of this theorem for α = 0 was recently given by one of the authors [9], and is reproduced
here for completeness. The central idea of how to prove it for arbitrary α = 1, 2, . . . is to use
induction, starting with the case α = 0. Tracing it back, this means that the Bessel-type behavior
of the polynomials is a consequence of the three-term recursion relation for the orthogonal poly-
nomials. As n, N →∞with t = n/N ﬁxed, this yields a certain “continuum limit” reminiscent
of the derivation of string equations in the double-scaling limit. The recursion relations thus
become the deﬁning second order diﬀerential equations for Bessel (and Neumann) functions. It is
the boundary conditions that ﬁnally uniquely specify the Bessel solutions. However, for simplicity
we shall here show the proof by induction.
We start with the case α = 0. The recursion relation for Pn(λ) ≡P (0)
n (λ) takes the form (with
hn ≡h(0)
n
and pn ≡p(0)
n ):
λ Pn(λ)
=
−rn

Pn+1(λ) −Pn(λ) −hn
rn
rn−1
hn−1
(Pn(λ) −Pn−1(λ))


rn ≡−pn
pn+1

≡
X
m
ˆλnm Pm(λ).
(2.10)
This is the well-known three-term recursion relation rewritten in our nonmonic normalization.
The structure of the coeﬃcients is dictated by a comparison of O(λ0) and O(λn+1) terms on both
sides. The sets of unknowns {hn}, {rn} can be determined iteratively by
1 = −
Z ∞
0
dλ d
dλ
n
e−N V (λ)Pn(λ) Pn(λ)
o
= N V ′(ˆλ)nn hn,
(2.11)
0 = −
Z ∞
0
dλ d
dλ
n
e−N V (λ)λ Pn(λ) Pn(λ)
o
=

N(ˆλV ′(ˆλ))nn −2n −1

hn.
(2.12)
In the following we need to know the asymptotic behavior of rn and hn for
n, N →∞
while
n
N = t
is kept ﬁxed.
(2.13)
Eqs. (2.10), (2.11) and (2.12) tell us that they should behave as
rn = r
 n
N

+
higher orders in
1
N ,
hn = 1
N h
 n
N

+
higher orders in
1
N .
(2.14)
Then the leading behavior of the matrix ˆλ and its powers is
ˆλnm = r( n
N ) (−δn m−1 + 2δnm −δn m+1) ,
(ˆλk)nm = r( n
N )k
k
X
ℓ=−k
(−)ℓ
 2k
k + ℓ

δn m+ℓ
(2.15)
5
so that eqs. (2.11) and (2.12) read
X
k
gk
2k −2
k −1

r(t)k−1
=
1
h(t),
(2.16)
1
2
X
k
gk
2k
k

r(t)k
=
t.
(2.17)
Note that eqs. (2.16) and (2.17) imply a universal relationship among total derivatives,
dt = 2r d
1
h

+ 1
hdr = √r d
 
2√r
h
!
.
(2.18)
Next we expand the right hand side of the recursion relation (2.10) in terms of 1/N in the limit
(2.13) to get
N 2λ P(n, N, λ) = −r(t)
(
d2 P
dt2 + h(t)
r(t)
 d
dt
r(t)
h(t)
 dP
dt
)
= −h(t) d
dt
r(t)
h(t)
d
dtP(n, N, λ),
(2.19)
where the argument N in P(n, N, λ) ≡Pn(λ) is to indicate explicitly the dependency via the
coeﬃcient in front of the potential. Only the leading terms up to O(1/N) have been kept here.
Eq. (2.19) tells us that that the arguments of the polynomial appear only in the combinations
t = n/N and x = N 2λ in the large-N limit.
The rescaled eigenvalue coordinate x is to be
ﬁxed ﬁnite hereafter, and is regarded as a parameter in the ordinary diﬀerential equation in t.
Performing the change of variable
t 7→u(t) ≡2
p
r(t)
h(t)
=
Z t
0
dt′
p
r(t′),
(2.20)
using the relationship (2.18), and neglecting higher order terms in 1/N, eq. (2.19) reduces to
Bessel equation of zeroth order:
 1
u
d
duu d
du + x

P(u, x) = 0.
(2.21)
The unique solution to this equation which satisﬁes the following boundary condition at t =
n/N = 0 (u(0) = 0),
P(0, x) = P0(λ) = 1,
(2.22)
is
P(u, x) = J0
 u√x
 .
(2.23)
We now proceed for a generic integer α by induction.
Given a set of polynomials {P (α)
n
(λ)}
which are orthogonal with respect to the measure dλ λα e−NV (λ) on [0, ∞), and are normalized
by P (α)
n
(0) = 1 as in eq. (2.8), we note that
˜P (α+1)
n
(λ) ≡P (α)
n+1(λ) −P (α)
n
(λ)
λ
(2.24)
6
are polynomials of order n. They are orthogonal to λk, k = 0, · · · , n −1 with respect to the
measure dλ λα+1 e−NV (λ) [10]:
Z ∞
0
dλ λα+1 e−NV (λ) ˜P (α+1)
n
(λ) λk
=
Z ∞
0
dλ λα e−NV (λ) 
P (α)
n+1(λ) −P (α)
n
(λ)

λk = 0.
(2.25)
Under the assumption that ˜P (α+1)
n
(0)̸ = 0, the orthogonal polynomial normalized to P (α+1)
n
(0) = 1
is thus given by
P (α+1)
n
(λ) =
˜P (α+1)
n
(λ)
˜P (α+1)
n
(0)
.
(2.26)
The microscopic limit of the contiguous relation (2.24) reads
˜P (α+1)
Nt
( x
N 2 ) = N
x
∂
∂tP (α)
Nt ( x
N 2 ) +
higher orders in
1
N .
(2.27)
If we substitute eq. (2.9) for a given α into the above, we conﬁrm that
˜P (α+1)
Nt
( x
N 2 )
=
−N
α!
p
r(t)
Jα+1 (u(t)√x)
(u(t)/2)α (√x)α+1 ,
(2.28)
˜P (α+1)
Nt
(0)
=
−N
u(t)/2
(α + 1)
p
r(t).
(2.29)
Thus eq. (2.9) holds also for α+1 after normalizing according to (2.26). Together with the result
(2.23) for α = 0, this completes the proof.
We have worked out an alternative proof of the same theorem, which does not rely on induction.
Rather, it is possible to convert the recursion relation for P (α)
n
(λ) directly into Bessel equation of
order α,

1
u2α+1 d
duu2α+1 d
du + x

P (α)(u, x) = 0. Since it is lengthy, we do not reproduce it here.
2.2
Universal correlations
Theorem 1 can be used to establish a remarkable universal form of spectral correlators of the
model (2.5). We shall consider the spectral density ρ(λ), and higher order correlators, in the
same microscopic limit as above.
To begin, we recall the expression for the integration kernel KN(λ, µ) associated with the eigen-
value problem for the positive-deﬁnite hermitian matrix H = W †W,
KN(λ, µ) = (λ µ)α/2 e−N
