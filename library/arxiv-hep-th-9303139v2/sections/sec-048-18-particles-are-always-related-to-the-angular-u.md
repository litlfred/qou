---
doc_id: arxiv-hep-th-9303139v2
doc_title: "ITFA 93-10 March 1993 A.Morozov"
section_id: sec-048-18-particles-are-always-related-to-the-angular-u
section_title: "Particles are always related to the ”angular (unitary-) matrix” integrals (as everybody"
section_number: 18
pages: 46-60
source_pdf: 9303139v2.pdf
source_sha256: 79b9a45fd4c5b4aa
doc_brief: "ITFA 93-10 March 1993 A.Morozov — The theory of matrix models is reviewed from the point of view of its relation to integrable hierarchies."
---
knows from example of the Wilson lattice QCD) which are highly less trivial to deal with,
though these are also integrable in some broader sense of the word - within the (yet non-
existing) generalization of integrable hierarchies from the ﬁelds in the Cartan subalgebra
to the entire WZNW model.
43
Vαβ −→U†
αVαβUβ.
In other words, eigenvalue models are gauge theories
without gauge ﬁelds, i.e. are pure topological. Thus it is not a surprise that
they usually live in the space time of dimension d < 2, 19 since for d > 2 there
should be particles, associated with the gauge ﬁelds. At the ”boundary” lies
the model of ”d = 2 (c = 1) string”, which has one particle-like degree of
freedom (dilaton, which becomes tachyon in the d > 2 models). This very
interesting model is much worse understood than the d < 2 models, at least
its properties are already somewhat diﬀerent from other eigenvalue models
(especially in the most interesting ”compactiﬁed” case), and it will not be
discussed in these notes. Later we”ll return to the subject of non-eigenvalue
(d > 2) theories, though not too much is yet known about them, but now we
are going to concentrate on the eigenvalue models.
3.2
1-matrix model
Hermitean matrix integrals are usually transformed to the eigenvalue form
by separation of angular and eigenvalue variables. As usually, the simplest
is the case of the 1-matrix model
ZN{t} ≡cN
Z
N×N dHe
P∞
k=0 tkTrHk,
(3.1)
where this separations does not involve any information about unitary-matrix
integrals. Take
H = U†DU,
(3.2)
where U is a unitary matrix and diagonal matrix D = diag(h1...hN) has
eigenvalues of H as its entries. Then integration measure
dH =
N
Y
i,j=1
dHij =
[dU]
[dUCartan]
N
Y
i−1
dhi∆2(h),
(3.3)
19Let us remind that in the Polyakov formulation which is the least counterintuitive
for interpretation of what happens in the space-time (target space), string models usually
involve Liouville ﬁeld, identiﬁed as a time-variable in the target-space formalism. (Note
that for this reason there is usually (at least one) time in the string theory, while space
can be of any dimension (at least between 0 and 25), not obligatory integer.) Because of
this extra Liouville ﬁeld the space-time dimension d usually diﬀers by 1 from the central
charge of the CFT model, which is coupled to 2d-gravity to from a string model: d = c+1
and d < 2 is the same as c < 1.
44
where ”Van-der-Monde determinant” ∆(h) ≡det(ij)hj−1
i
= QN
i>j(hi −hj) and
[dU] is Haar measure of integration over unitary matrices.
The way to derive eq.(3.3) is to consider the norm of inﬁnitesimal variation
|| δH ||2 ≡PN
i,j=1 | δHij |2= PN
i,j=1 δHijδHji = Tr(δH)2 =
= Tr

−U†δUU†DU + U†DδU + U†δDU
2 =
= Tr(δD)2 + 2iTrδu[δD, D] + 2Tr (−δuDδuD + (δu)2D2) ,
where δu ≡
1
i δUU† = δu† and δD = diag(δh1 . . . δhN). The second term
at the r.h.s. vanishes because both D and δD are diagonal and commute.
Therefore
|| δH ||2=
N
X
i=1
(δhi)2 +
N
X
i,j=1
(δu)ij(δu)ji(hi −hj)2.
Now it remains to recall the basic relation between the inﬁnitesimal norm
and the measure: if
|| δl ||2= Gabδlaδlb then [dl] = √detabGab
Q
a dla, to
obtain eq.(3.3) with Haar measure [dU] = QN
ij duij being associated with the
inﬁnitesimal norm
|| δu ||2= Tr(δu)2 =
N
X
i,j=1
δuijδuji =
N
X
i,j=1
| δuij |2
and [dUCartan] ≡
QN
i=1 duii.
Coming back to the 1-matrix model it remains to note that the ”action”
TrU(H) ≡
P∞
k=0 tkTrHk with H substituted in the form (3.2) is independent
of U:
TrU(H) =
N
X
i=1
U(hi).
Thus
ZN{t} = 1
N!
N
Y
i=1
Z
dhieU(hi)
N
Y
i>j
(hi −hj)2 =
= 1
N!
N
Y
i=1
Z
dhieU(hi)∆2(h),
(3.4)
45
provided cN is chosen to be
c−1
N = N! VolU(N)
(VolU(1))N ,
(3.5)
where the volume of unitary group in Haar measure is equal to
VolU(N) = (2π)N(N+1)/2
QN
k=1 k!
.
(3.6)
A simple way to derive eq.(3.6) will be described at the end of this section,
as an example of application of orthogonal polinomials technique.
3.3
Itzykson-Zuber and Kontsevich integrals
Let us proceed now to Kontsevich integral,
FV,n{L} =
Z
n×n dXe−trV (X)+trLX.
(3.7)
We shall see shortly that it in fact depends only on the eigenvalues of the
matrix L (this fact was already used in the previous section), however, this
time somewhat more sophisticated unitary matrix integrals will be involved.
Substitute X = U†
XDXUX; L = U†
LDLUL in (3.7) and denote U ≡UXU†
L.
Then
FV,n{L} =
= Qn
i=1
R dxie−V (xi)∆2(x)
R
n×n
[dU]
[dUCartan] exp
Pn
γ,δ=1 xγlδ | Uγδ |2
. (3.8)
In order to proceed further we need to evaluate the integral over unitary
matrices, which appeared at the r.h.s.
This integral can actually be represented in two diﬀerent ways:
In{X, L} ≡
Z
n×n
[dU]
[dUCartan]etrXULU† =
(3.9)
=
Z
n×n
[dU]
[dUCartan]e
Pn
γ,δ=1 xγlδ|Uγδ|2
(3.10)
46
(the U’s in the two integrals are related by the transformation U −→UXUU†
L
and Haar measure is both left and right invariant). Formula (3.9) implies
that In{X, L} satisﬁes a set of simple equations [59]:

tr
 
∂
∂Xtr
!k
−trLk

In{X, L} = 0,
k ≥0,

tr
 ∂
∂Ltr
!k
−trXk

In{X, L} = 0,
k ≥0,
(3.11)
which by themselves are not very restrictive.
However, another formula,
(3.10), implies that In{X, L} in fact depends only on the eigenvalues of X
and L, and for such In{X, L} = ˆI{xγ, lδ} eqs.(3.11) become very restrictive
20 and allow to determine ˆI{xγ, lδ} unambigously (at least if ˆI{xγ, lδ} is
expandable in a formal power seria in xγ and lδ). The ﬁnal solution is
In{X, L} = (2π)
n(n−1)
2
n!
detγδexγlδ
∆(x)∆(l).
(3.12)
Normalization constant can be deﬁned by taking L = 0, when
In{X, L = 0} =
VolU(n)
(VolU(1))n = (2π)
n(n−1)
2
Qn
k=1 k! ,
and using the fact that
detγδfγ(lδ)
∆(l)

{lδ=0}
=
 n−1
Y
k=0
1
k!
!
detγδ∂δ−1fγ(0).
Eq.(3.12) is usually refered to as the Itzykson-Zuber formula [60].
In
mathematical literature it was earlier derived by Kharish-Chandra [61], and
20When acting on ˆI, which depends only on eigenvalues, matrix derivatives turn into:
tr
∂
∂Xtr
ˆI = P
γ
∂
∂xγ ˆI;
tr ∂2
∂X2
tr
ˆI = P
γ
∂2
∂x2γ ˆI + P
γ̸=δ
1
xγ−xδ

∂
∂xγ −
∂
∂xδ

ˆI;
etc.
47
in fact the integral (3.9 is the basic example of the coadjoint orbit integrals
[62]-[5], which can be exactly evaluated with the help of the Duistermaat-
Heckmann theorem [64], [65],[43],[44]. This calculation is the simplest exam-
ple of the very important technique of exact evaluation of non −Gaussian
unitary-matrix integrals, which is now doing its ﬁrst steps (see [66]-[68]) and
will be discussed at the end of these notes.
Now we turn back to the eigenvalue formulation of the GKM. Substitution
of (3.12) into (3.8) gives:
FV,n{L} = (2π)
n(n−1)
2
∆(l)
n
Y
δ=1
Z
dxδe−V (xδ)∆(x) 1
n!detγδexγlδ =
= (2π)
n(n−1)
2
∆(l)
n
Y
δ=1
Z
dxδe−V (xδ)+xδlδ∆(x),
(3.13)
where we used antisymmetry of ∆(x) under permutations of xγ’s in order to
change
1
n!detγδexγlδ for e
P
δ xδlδ under the sign of the xδ integration.
We can now use the fact that ∆(x) = detγδxγ−1
δ
in order to rewrite the
r.h.s. of (3.13):
FV,n{L} = (2π)
n(n−1)
2
detγδ ˆϕγ(lδ)
∆(l)
,
(3.14)
where
ˆϕγ(l) ≡
Z
dxxγ−1e−V (x)+lx,
γ ≥1.
(3.15)
These functions ˆϕ(l) satisfy a simple recurrent relation:
ˆϕγ = ∂ˆϕγ−1
∂l
=
 ∂
∂l
!γ−1
ˆΦ
(3.16)
with
ˆΦ(l) ≡ˆϕ1(l) =
Z
dxe−V (x)+lx.
(3.17)
Note also that if the ”zero-time” N is introduced (see subsection 2.6 above
and [36]), then
FV,n{N | L} ≡FV (X)−N log X,n{L} = (2π)
n(n−1)
2
detγδ ˆϕγ+N(lδ)
∆(l)
(3.18)
48
with just the same ˆϕγ(l) and γ, δ = 1 . . .n. If we divide by the quasiclassical
factor CV {Λ}(detΛ)N, L = V ′(Λ), in order to transform Kontsevich integral
into Kontsevich model (see section 2.5), we get:
ZV {N, T} =
1
(detΛ)N · detγδϕγ+N(λδ)
∆(λ)
.
(3.19)
The role of CV {Λ} is to convert ˆϕ(l) into the properly normalized expansions
in the negative iteger powers of λ:
ϕγ(λ) =
e−λV ′(λ)+V (λ)q
V ′′(λ)
√
2π
ˆϕγ(V ′(λ)) = λγ−1(1 + O(λ−1)),
(3.20)
and to change ∆(l) = ∆(V ′(λ)) in the denominator of (3.18) for ∆(λ) in
(3.19). Instead of the simple recurrent relations (3.16) for ˆϕ the normalized
functions ϕ satisfy:
ϕγ(λ) = Aϕγ−1(λ) = Aγ−1Φ(λ),
(3.21)
where Φ(λ) = ϕ1(λ) and operator
A =
1
V ′′(λ) · ∂
∂λ −1
2
V ′′′(λ)
(V ′′(λ))2 + λ
(3.22)
now depends on the potential V (x).
3.4
Conventional Multimatrix models
The multimatrix integrals of the form
ZN{t(α)} ≡
≡cp−1
N
Z
N×N dH(1)...dH(p−1)
p−1
Y
α=1
e
P∞
k=0 t(α)
k
TrHk
(α)
p−2
Y
α=1
eTrH(α)H(α+1)
(3.23)
can be rewritten in the eigenvalue form using the same Itzykson-Zuber for-
mula (3.12). Indeed, substituting H(α) = U(α) † D(α)Uα) and then defyining
49
U(α) U(α+1) † ≡˜U(α), we obtain:
ZN{t(α)} =
= 1
N!
p−1
Y
α=1
N
Y
i=1
Z
dh(α)
i
e−V (h(α)
i
)∆2(h(α))
p−2
Y
α=1
IN{H(α), H(α+1)} =
= 1
N!
p−1
Y
α=1
N
Y
i=1
Z
dh(α)
i
e−V (h(α)
i
)
p−2
Y
α=1
eh(α)
i
h(α+1)
i
∆(h(1))∆(h(2)),
(3.24)
where the same trick is done with the substitution of
1
N!detijeh(α)
i
h(α+1)
j
for
e
PN
i=1 h(α)
i
h(α+1)
i
under the sign of the h(α)
i
-integration (step by step: ﬁrst -
for α = 1, then for α = 2 and so on). Note that all the Van-der-Monde
determinants disappeared from the ﬁnal formula at the r.h.s. of eq.(3.24),
except for those at the ends of the matrix chain (at α = 1 and α = p −1).
If the chain was closed rather than open, i.e. there was an additional
factor of eTrH(p−1)H(1) under the integral in (3.23), then the trick with separa-
tion of all angular-variable (unitary-matrix) integrations would not work so
simply: in addition to the Itzykson-Zuber integral the much more involved
quantities would be required, like
In{X1, X2; L} ≡
≡cn
Z
n×n
[dU1]
[dU1,Cartan]
[dU2]
[dU2,Cartan]
· exp

trX1U1LU†
1 + trX2U2LU†
2 + trX1(U1U†
2)X2(U2U†
1)

(3.25)
This (so far unresolved) closed chain model (lattice Potts model) is an exam-
ple of non-eigenvalue models, in the p = ∞case it turns into ”compactiﬁed”
c = 1 model. This theory is more complicated then the so far simplest class
of non-eigenvalue models of ”induces Yang-Mills theory”, known as Kazakov-
Migdal models.
3.5
Determinant formulas for eigenvalue models
We are now prepared to make the crucial step towards understanding of
mathematical structure behind eigenvalue models, which distinguishes their
partition functions in the entire variety of arbitrary N-fold integrals. This
50
structure expresses itself in the form of determinantal formulas, which we are
now going to discuss. In the next section 4 these formulas will be identiﬁed
as examples of τ-functions of KP and Toda hierarchies.
Looking at the relevant integrals (3.4), (3.24) one can notice that inte-
grals over diﬀerent eigenvalues with non-trivial measures which depend on
the shape of potentials U or V , are almost separated, the only ”interac-
tion” between diﬀerent eigenvalues being deﬁned by universal (potential-
independent) quantities, made from the Van-der-Monde determinants. This
feature is intimately related both to its origin (decoupling of angular variables
in original matrix integral) and to its most important implication (integra-
bility). The main property of the Van-der-Monde determinant is that it is
at the same time a Pfaffian (and it is in this quality that it arises from
matrix integrals) and a determinant (and this is the feature that implies
integrability):
Y
i>j
(hi −hj) = ∆(h) = detijhj−1
i
.
(3.26)
We already used this property above, when going from eq.(3.13) to eq.(3.14),
which as we shall see later is the crucial step in the proof of integrability of
Kontsevich model. In that case determinantal formula (3.14) for partition
function was trivial to derive, because the integrand was linear in Van-der-
Monde determinants. Now we turn to slightly more complicated situations,
involving products of Van-der-Monde determinants.
Consider an eigenvalue model of the form:
ZN = 1
N!
N
Y
k=1
Z
dµhk,¯hk∆(h)∆(¯h),
(3.27)
to be refered to as ”scalar-product” model. All conventional multimatrix
models (3.23) belong to this class. In the case of the 1-matrix model (3.4)
dµh,¯h = dhd¯heU(h)δ(h −¯h),
(3.28)
while for conventional multimatrix models (3.24)
dµh(1),h(p−1) = dh(1)dh(p−1)
p−2
Y
α=2
Z
dh(α)
p−1
Y
α=1
eUα(h(α))
p−2
Y
α=1
eh(α)h(α+1)
(3.29)
51
If dµh,¯h = δ(h −¯h)d¯hdµh we call this measure local. The main feature of
local measure is that operator of multiplication by H (or any function of h)
is Hermitean. Thus measure is local in the 1-matrix model, but is non-local
for all p −1 > 1. In the latter case the measure is deﬁned to depend only on
h = h(1) and ¯h = h(p−1), all other h(α), α = 2 . . .p −2 being integrated out,
what makes the ”interaction” between h and ¯h more complicated than just
δ(h −¯h) in the one-matrix (p = 2) and eh¯h in the two-matrix (p = 3) cases.
In no sense the set of particular formulas (3.29) for p > 3 is distinguished
among other scalar-product models, and from now on we shall not consider
conventional multimatrix models with p−1 > 2 as a separate class of theories.
Eqs.(3.27) and (3.26) imply together that
ZN = 1
N!
N
Y
k=1
Z
dµhk,¯hkDetikhi−1
k
Detjk¯hj−1
k
=
= Detij
Z
dµh,¯hhi−1¯hj−1 = Detij⟨hi−1 | ¯hj−1⟩,
(3.30)
where an obvious notation is introduced for the scalar product
⟨f(h) | g(¯h)⟩≡
Z
dµh,¯hf(h)g(¯h).
We can now be a little more speciﬁc and introduce time-variables tk and
¯tk so, that
dµh,¯h = eU(h)+ ¯U(¯h)dˆµh,¯h,
U(h) =
∞
X
k=−∞
tkhk,
¯U(¯h) =
∞
X
k=−∞
¯tk¯hk,
(3.31)
and ˆdµh,¯h is already independent of h and ¯h. If we now denote Hf(t, ¯t) ≡
⟨1 | 1⟩, then
Hf
ij ≡⟨hi | ¯hj⟩=
∂2
∂ti∂¯tj
Hf(t, ¯t) =
if i,j≥0
=
 ∂
∂t1
!i ∂
∂¯t1
!j
Hf(t, ¯t),
(3.32)
and
ZN = DetNHf
ij,
(3.33)
52
where DetN stands for determinant of the N × N matrix Hi−1,j−1 (which
is deﬁned itself for any integers i, j) with i, j = 0, . . ., N −1. Characteristic
property of Hf
ij is its peculiar time-dependence:
Hf
ij
∂tk
= Hf
i+k,j;
Hf
ij
∂¯tk
= Hf
i,j+k.
(3.34)
Eq.(3.33) provides the determinantal formula for all scalar-product mod-
els.
The case of the local measure - for 1-matrix model - is a little spe-
cial. In this case U(h) contains the whole information about the measure:
dµh,¯h = δ(h −¯h)dµh, dµh = eU(h)dh, and there is no ¯U(¯h) (or ¯t simply
coincide with t). Then (3.33) is still valid, but
Hf
ij = ⟨hi | ¯hj⟩

dµh,¯h = ⟨hi+j⟩

dµh =
∂
∂ti+j
Hf(t) =
if i,j≥0
=
 ∂
∂t1
!i+j
Hf(t).
(3.35)
The same formula (3.35) can be also derived as a limit of eq.(3.14) for Kont-
sevich integral. Indeed,
ZN{t} = cN
Z
N×N dHeTrU(H) = lim
L→0 FU,N{L} =
= lim
{lj}→0
Detij ˆϕ{U}
i
(lj)
∆(l)
= Detij
∂j−1 ˆϕ{U}
i
(lj)
∂lj−1
(0) = DetijHf
i−1,j−1,
(3.36)
where this time
Hf
i−1,j−1
i,j>0
=
∂j−1 ˆϕ{U}
i
(lj)
∂lj−1
(l = 0)
(3.14)
=
 ∂
∂l
!i+j−2
ˆΦ{U} |l=0 .
(3.37)
Now we note, that the action of ∂
∂l on ˆΦ{U}(l) =
R dxeU(x)+lx is equivalent to
that of

∂
∂t1

, since this is no longer a matrix integral, and thus
Hf
ij =
 ∂
∂t1
!i+j
ˆΦ{U}(0),
(3.38)
i.e. Hf(t) = ˆΦ{U}(0).
53
Conformal multimatrix models were introduced in section 2.3 above just
as eigenvalue models. For the Ap−1 series partition functions are deﬁned to
be
ZAp−1
N1...Np−1{t(1) . . . t(p−1)} =
=
p−1
Y
α=1
cNα
Z
Nα×Nα dH(α)eTrUα(H(α))·
·
p−2
Y
α=1
Det

H(α) ⊗I −I ⊗H(α+1)
=
=
p−1
Y
α=1
1
Nα!
Nα
Y
i=1
Z
dh(α)
i
eUα(h(α)
i
)∆2(h(α))
p−2
Y
α=1
Y
i,k
(h(α)
i
−h(α+1)
k
).
(3.39)
This expression does not have a form of eq.(3.27), thus conformal matrix
models for p−1 > 1 are not of the ”scalar-product” type. We shall sometimes
call them (p −1)-component models, because they are related to the multi-
component integrable hierarchies. The simplest way to proceed with their
investigation is to use the same trick with Kontsevich integral, which was
just applied in the 1-matrix case.
Let us start from a very general (p −1)-component model:
Z =
p−1
Y
α=1
Z
Nα×Nα dH(α)eTrUα(H(α))K(H(1) . . . H(p−1)).
(3.40)
It can be also represented in terms of Kontsevich integrals:
Z = K
 
∂
∂L(1)
tr
, . . .,
∂
∂L(p−1)
tr
! p−1
Y
α=1
FUα,Nα{L(α)}

L(α)=0
.
(3.41)
This representation is not very usefull, since the limit L →0 is not easy
to take, unless K is a polinomial in the eigenvalues of all its arguments.
However, this is exactly the case for our confromal models (3.39). Indeed,
KAp−1 =
p−2
Y
α=1
Det
 
∂
∂L(α)
tr
⊗I −I ⊗
∂
∂L(α+1)
tr
!
.
(3.42)
54
Still this is not very convenient, because representation (3.14) for F contain
∆(L) in denominator, which are not very pleasant to diﬀerentiate. Simpli-
ﬁcation can be achieved if instead we rewrite the original expression at the
r.h.s. of (3.39) as follows:
ZAp−1
N1...Np−1{t(1) . . . t(p−1)} =
= ∆

∂
∂l(1)
 Qp−2
α=1 ∆

∂
∂l(α),
∂
∂l(α+1)

∆

∂
∂l(p−1)

×
× Qp−1
α=1

1
Nα!
QNα
i=1
R dh(α)
i
eUα(h(α)
i
)+l(α)
i
h(α)
i


l(α)=0
(3.43)
where ∆(h, h′) ≡
QN
i>j(hi−hj)
QN′
k>l(h′
k−h′
l)
QN
i=1
QN′
k=1(h′
k−hi). This formula
already takes the speciﬁc form of K into account. The product of integrals
in brackets at the r.h.s. of (3.43) is equal (for every ﬁxed α) to
1
Nα!
Nα
Y
j=1
ˆΦ{Uα}(l(α)
j )
(3.44)
(compare with eq.(3.38)).
In order to simplify the notation we shall further denote ˆΦ{Uα}(l) ≡
R dxeUα(x)+lx through ˆΦα(l), and

∂
∂t(α)
1
k ˆΦ{Uα}(l(α)) =

∂
∂l(α)
k ˆΦ{Uα}(l(α))
- through ∂k ˆΦα(l). Thus
ZAp−1
N1...Np−1{t(1) . . . t(p−1)} =
= ∆

∂
∂l(1)
 Qp−2
α=1 ∆

∂
∂l(α),
∂
∂l(α+1)

∆

∂
∂l(p−1)

×
× Qp−1
α=1

1
Nα!
QNα
j=1 ˆΦα(l(α)
j )


l(α)=0 .
(3.45)
If p −1 = 1, diﬀerential operator is just a square of determinant ∆(∂/∂l)
and we can use the relation
∆2(h) =
P
P Detijhi+j−2
P (j)
=
= P
P Det


1
hP (2)
h2
P (3) . . .
hN1−1
P (N1)
hP (1)
h2
P (2)
h3
P (3) . . .
hN1
P (N1)
h2
P (1)
h3
P (2)
h4
P (3) . . .
hN1+1
P (N1)
. . .
hN1−1
P (1)
hN1
P (2)
hN1+1
P (3) . . .
h2N1−2
P (N1)


(3.46)
55
where the sum is over all the N! permutations P of N elements 1 . . .N,
in order to conclude that (3.45) reproduces our old formula (3.33), (3.38):
ZN = Detij∂i+j−2 ˆΦ.
For p −1 = 2 we need to use a more complicated analogue of (3.46):
∆(h)∆(h, h′)∆(h′) =
(3.47)
= P
P
P
P ′ Det


1
hP (2) . . .
hN1−1
P (N1)
1
¯h ¯P (2) . . .
¯hN2−1
¯P (N2)
hP (1)
h2
P (2) . . .
hN1
P (N1)
¯h ¯P (1)
¯h2¯P (2) . . .
¯hN2
¯P (N2)
h2
P (1)
h3
P (2) . . .
hN1+1
P (N1)
¯h2¯P (1)
¯h3¯P (2) . . .
¯hN2+1
¯P (N2)
. . .
hN1−1
P (1)
hN1
P (2) . . .
hN +N1−2
P (N1)
¯hN2−1
¯P (1)
¯hN2
¯P (2) . . .
¯hN +N2−2
P (N2)


where N = Pp−1
α=1 Nα. Making use of this formula, we conclude that the r.h.s.
of (3.45) for p −1 = 2 is also representable in the form of determinant:
Det


ˆΦ
∂ˆΦ . . .
∂N1−1ˆΦ
ˆ¯Φ
∂ˆ¯Φ . . .
∂N2−1ˆ¯Φ
∂ˆΦ
∂2 ˆΦ . . .
∂N1 ˆΦ
∂ˆ¯Φ
∂2 ˆ¯Φ . . .
∂N2 ˆ¯Φ
. . .
∂N −1 ˆΦ
∂N ˆΦ . . .
∂N +N1−2ˆΦ
∂N −1ˆ¯Φ
∂N ˆ¯Φ . . .
∂N +N2−2 ˆ¯Φ


here ˆΦ = ˆΦ1, ˆ¯Φ = ˆΦ2 and all arguments l(α) = 0. It is especially easy to
check formula (3.47) in the simplest case of N1 = N2 = 1. Then it just
says that ¯h −h = Det
"
1
1
h
¯h
#
. Analogues expressions for p −1 > 2 are
more involved, they are no longer just determinants: this is obvious already
from consideration of the simplest case of N1 = . . . = Np−1 = 1, the product
Qp−2
α=1(h(α) −h(α+1)) is no longer determinant of any nice matrix.
3.6
Orthogonal polinomials
Formalism of orthogonal polinomials was intensively used at the early days
of the theory of matrix models. It is applicable to scalar-product eigenvalue
models and allows to further transform (diagonalize) the remaining determi-
nants into products. In variance with both reduction from original N2-fold
matrix integrals to the eigenvalue problem, which (when possible) reﬂects
a physical phenomenon - decoupling of angular (unitary-matrix) degrees of
56
freedom (associated with d-dimensional gauge bosons), - and with occurence
of determinant formulas which reﬂects integrability of the model, orthogonal
polinomials appear more as a technical device. Essentially orthogonal poli-
nomials are necessary if wants to explicitly separate dependence on the the
size N of the matrix in the matrix integral (”zero-time”) from dependencies
on all other time-variables and to explicitly construct variables, which satisfy
Toda-like equations. However, modern description of integrable hierarchies
in terms of τ-functions does not require explicit separation of the zero-time
and treats it more or less on the equal fooring with all other variables, thus
making the use of orthogonal polinomials unnecessary. Still this technique
remains in the arsenal of the matrix model theory21 and we now brieﬂy ex-
plain what it is about. At the end of this section two simple applications
will be also described: one to evaluation of the volume of the unitary group,
another - to direct proof of equivalence of the ordinary 1-matrix model and
the Gaussian Kontsevich model. Both these examples make use of explicitly
known orthogonal Hermite polinomials and in this sense are not quite rep-
resentative: usually orthogonal polinomials are not known explicitly. Some
applications of such ”abstract” theory of orthogonal polinomials to the study
of matrix models will be mentioned in the following sections.
In the context of the theory of scalar-product matrix models orthogonal
polinomials naturally arise when one notes that after partition functions
appears in a simple determinantal form of eq.(3.30), any linear change of
basises hi →Qi(h) = P
k Aikhk, ¯hj →¯Qj(¯h) = P
l Bjl¯hl can be easily
performed and Z −→Z ·detA·detB. In particular, if A and B are triangular
with units at diagonals, their determinants are just unities and Z does not
change at all. This freedom is, however, enough, to diagonalize the scalar
product and choose polinomials Qi and ¯Qj so that
⟨Qi(h) | ¯Qj(¯h)⟩= eφiδij.
(3.48)
Qi and ¯Qj deﬁned in this way up to normalization are called orthogonal
polinomials. (Note that ¯Q does not need to be a complex conjugate of Q:
”bar” does not mean complex conjugation.) Because of above restriction on
