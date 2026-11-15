---
doc_id: arxiv-hep-th-9803007v2
doc_title: "arXiv:hep-th/9803007v2 17 Jun 1998"
section_id: sec-000-smallest-dirac-eigenvalue-distribution-from-rand
section_title: "Smallest Dirac Eigenvalue Distribution from Random Matrix Theory"
section_number: null
pages: 1-4
source_pdf: 9803007v2.pdf
source_sha256: 75f6484941ecbca0
toc_source: inferred
doc_brief: "arXiv:hep-th/9803007v2 17 Jun 1998 — 2 sections: Front matter; Smallest Dirac Eigenvalue Distribu"
---
Shinsuke M. Nishigaki1,∗, Poul H. Damgaard2,†, and Tilo Wettig3,‡
1Institute for Theoretical Physics, University of California, Santa Barbara, CA 93106-4030, USA
2The Niels Bohr Institute, Blegdamsvej 17, DK-2100 Copenhagen Ø, Denmark
3Institut f¨ur Theoretische Physik, Technische Universit¨at M¨unchen, D-85747 Garching, Germany
(March 2, 1998)
We derive the hole probability and the distribution of the smallest eigenvalue of chiral hermitian
random matrices corresponding to Dirac operators coupled to massive quarks in QCD. They are
expressed in terms of the QCD partition function in the mesoscopic regime. Their universality is
explicitly related to that of the microscopic massive Bessel kernel.
PACS number(s): 05.45.+b, 12.38.Aw, 12.38.Lg
There has long been an attractive idea that the low-
energy physics of a complex system can be described by
a simple eﬀective theory which respects the global sym-
metries of the original system. As an example, the quan-
tum spectral statistics of a classically chaotic system is
believed to be described by a random matrix theory be-
longing to the same universality class as the former [1].
One new manifestation of essentially the same idea is the
recent observation that QCD Dirac operator spectra on
the scale λ = O(1/V4) (where V4 is the space-time vol-
ume) measured in lattice Monte Carlo simulations [2] are
in excellent agreement with the predictions from those
large-N random matrix theories [3,4] that share the same
global symmetries as QCD. The suitably rescaled (micro-
scopic) spectral correlation functions thus seem to pro-
vide exact ﬁnite-size scaling functions for QCD in a ﬁnite
volume.
Very recently, the microscopic spectral corre-
lators have been calculated from random matrix theo-
ries that include the eﬀect of fermion determinants with
masses m ≃O(1/V4) [5–7] (see also [8]). When λ and
m are measured in units of the mean level spacing at
zero virtuality, all the random matrix predictions turn
out to be universal, i.e., insensitive to the details of the
random matrix potential [4–6]. Although the question of
whether or not QCD is included in the same universality
class cannot be answered by demonstrating the existence
of the wide range of universality within random matrix
theories, it provides strong support for the former.
From the ﬁeld-theoretic point of view [9] it would be
most surprising if these observables would not also be
computable solely within the framework of ﬁnite-volume
generating functionals (partition functions) for the order
parameter ⟨¯ψψ⟩. If not, large-N random matrix theory,
which in principle is foreign to the pertinent ﬁeld theory
language, would seem to be a new ingredient required
to describe the observed spectral correlators. It has re-
cently been shown that a description entirely in terms of
ﬁnite-volume partition functions is indeed also possible
[10].
In order to conﬁrm by numerical simulations that the
low-lying spectra of QCD Dirac operators can be de-
scribed alternatively by large-N random matrix theories,
it is in practice most convenient to measure the distribu-
tion of the smallest eigenvalue [2] and compare that to
the random matrix prediction [11,7]. Since the smallest
eigenvalue distribution largely consists of the ﬁrst peak
of the microscopic spectral density (see Fig. 1, ζ ≡Nλ),
we expect it to be universal.
FIG. 1.
Microscopic spectral density (solid line, normal-
ized as ρs(ζ →∞)=1/π) and smallest eigenvalue distribution
(dotted line) for the quenched chiral unitary ensemble.
In fact, the proven universality of the massive kernels
[5,6] of (chiral) unitary ensembles of random matrices
guarantees the universality of the hole probability E(s),
i.e., the probability that the interval [−s, s] is free of
eigenvalues, and of the smallest eigenvalue distribution
P(s) = −E′(s) because it is related to the kernel via the
Fredholm determinant formula [12],
E(s) = det(1 −ˆK).
(1)
Here, ˆK is an integral operator whose kernel is the mi-
croscopic massive Bessel kernel (Eq. (17) below or its
non-chiral counterpart) over the interval [−s, s]. While
other universal statistical quantities such as the num-
ber variance Σ2(s) and the spectral rigidity ∆3(s) of the
eigenvalues in the interval [−s, s] are directly related to
the kernel by integral transforms, the techniques required
to compute (1) from the kernel are rather involved. In
the case of the universal (massless) sine kernel describ-
ing the bulk of unitary ensembles, its eigenmodes are
1
given by the prolate spheroidal functions whose eigenval-
ues are known. However, the massive generalization of
these eigenmodes is diﬃcult to construct. The alternative
technique of determining E(s) as a τ-function of a sys-
tem of integrable partial diﬀerential equations [13] does
not simplify the situation either. Consequently, the ex-
plicit calculation for the massive case has been done so far
solely for the chiral Gaussian unitary ensemble [7]. The
result contains an explicit factor of exp(−ζ2/4) which at
ﬁrst sight is due to the Gaussian potential. Since these
results should be universal, the identical factor should
also arise from a generic random matrix potential. How
this happens is not immediately obvious and will be ad-
dressed in the sequel. We shall provide a concise method
to circumvent the diﬃculty in explicitly evaluating (1)
and to eﬃciently calculate E(s) for the massive chiral
unitary ensembles with generic potentials.
We deﬁne the partition function of the chiral unitary
ensemble
Z(α)({m}) =
Z
dM e−Ntr v(M)
α
Y
f=1
det (M + imf) ,
(2)
where M is a 2N × 2N block hermitian matrix
M =

0
W
W †
0

,
(3)
dM is the Haar measure of W, and v(M) is an even
analytic function. The matrix M models the Dirac op-
erator for SU(Nc ≥3) QCD4 in the Weyl basis, and N
can be identiﬁed with the spacetime volume V4.
The
integer α corresponds to the number of ﬂavors.
The
case of nonzero topological charge ν can be treated
by introducing |ν| massless ﬂavors [3].
One then has
α = Nf +|ν|, where Nf is the number of (massive) ﬂavors
and mNf+1, . . . , mNf+|ν| = 0.
The (unnormalized) probability of having no eigenval-
ues in the interval [−s, s] is given by
E(α)(s; {m}) =
Z
|eigenvalues|≥s
dM
e−Ntr v(M)
α
Y
f=1
det (M + imf) .
(4)
It is convenient to change the picture from M to an N×N
positive deﬁnite hermitian matrix H = W †W,
E(α)(s; {m}) =
Z
eigenvalues≥s2
dH
e−Ntr V (H) Y
f
det(H + m2
f)
=
Z
eigenvalues≥0
dH
e−Ntr V (H+s2) Y
f
det(H + s2 + m2
f),
(5)
where V (z2) ≡2v(z). Hereafter we write
m′ =
p
m2 + s2.
(6)
We can express (5) in terms of an expectation value
⟨· · ·⟩m′
with
respect
to
the
measure
e−Ntr V (H) ×
Q
f det(H + m′
f
2),
E(α)(s; {m}) =
R ∞
0
dH e−Ntr V (H+s2) Q
f det(H + m′
f
2)
R ∞
0
dH e−Ntr V (H) Q
f det(H + m′
f
2)
Z ∞
0
dH e−Ntr V (H) Y
f
det(H + m′
f
2)
=
D
e−Ntr (V (H+s2)−V (H))E
m′ Z(α)({m′}).
(7)
In the following we shall show that the two factors in
Eq. (7) are piecewise universal in the limit N →∞with
ζ = Ns and µ = Nm ﬁxed ﬁnite.
Due to the large-N factorization of macroscopic corre-
lation functions of U(N)-invariant operators O, O′ [14],
⟨OO′⟩= ⟨O⟩⟨O′⟩+ O
 1
N 2

,
(8)
the ﬁrst factor of (7) is, in the large-N limit, approxi-
mated by
∼e−N 2⟨1
N tr (V (H+s2)−V (H))⟩m′
∼e−N 2(s2⟨1
N tr V ′(H)⟩+O(s4)).
(9)
Since the fermion determinant does not contribute to
the macroscopic correlator in the large-N limit, we have
dropped the suﬃx m′.
Now we change the picture back to M, whose macro-
scopic spectral density is ρ(z) ≡⟨(1/2N)tr δ(z −M)⟩=
R(z2)
√
a2 −z2, where [−a, a] is the support of the spec-
trum of M and R(z2) is an analytic function which de-
pends on the details of v(M) [4]. We obtain
Q ≡

 1
N tr V ′(H)

=

 1
2N tr v′(M)
M

=
Z a
−a
dz ρ(z)v′(z)
z
.
(10)
In terms of ρ(z), the leading (of order O(N 2)) part of the
action in (2) is written as
S =
Z a
−a
dz ρ(z)2v(z) −
Z a
−a
dzdw ρ(z)ρ(w)2P ln |z −w|.
(11)
The second term is the exponentiated Vandermonde de-
terminant.
By substituting the large-N saddle-point
equation [15] δS/δρ(z) = 0, i.e.,
2
v′(z) −2
Z a
−a
dw ρ(w)P
1
z −w = 0,
(12)
into (10), we have
Q = 2
Z a
−a
dz dw ρ(z)ρ(w)P 1
z P
1
z −w .
(13)
Using the identity 1/(z ± iǫ) = P(1/z) ∓iπδ(z) and tak-
ing into account that ρ(z) is even, we ﬁnally obtain
Q =
Z a
−a
dz dw ρ(z)ρ(w)πδ(z)πδ(z −w) = (πρ(0))2.
(14)
That is,
D
e−Ntr (V (H+s2)−V (H))E
s,m′

s= ζ
N
N→∞
−→e−(πρ(0)ζ)2 (15)
which, after the rescaling ζ →ζ/(2πρ(0)), universally
reads exp(−ζ2/4). This answers the question raised in
the introduction how the Gaussian factor arises from a
generic potential.
We denote the microscopic limit of the partition func-
tion Z(α)({m} = { µ
N }) by Z(α)({µ}). It is related to the
microscopic kernel by the master formula [10]
K(α)(ζ1, ζ2; µ1, . . . , µα) = C
p
|ζ1ζ2|
Y
f
q
(ζ2
1 + µ2
f)(ζ2
2 + µ2
f)Z(α+2)(iζ1, iζ2, µ1, . . . , µα)
Z(α)(µ1, . . . , µα)
,
(16)
where C is a normalization constant. This formula is reminiscent of the very deﬁnition of the partition function and
the kernel [16] and is valid in the large-N limit, regardless of whether microscopic or macroscopic eigenvalue and mass
variables are kept ﬁnite.
Using the technique of orthogonal polynomials and rescaling ζ →ζ/(2πρ(0)), µ →µ/(2πρ(0)), the left-hand side is
shown to be universally given by [5]
K(α)(ζ1, ζ2; {µ}) = C
p
|ζ1 ζ2|
ζ2
1 −ζ2
2
det
1≤i,j≤α+2 Bij(ζ1, ζ2; {µ})
Q
f
p
(ζ2
1 + µf 2) (ζ2
2 + µf 2)
det
1≤i,j≤α Aij({µ})
,
(17)
Aij = µj−1
i
Ij−1(µi),
Bij =

Aij
(i = 1, . . . , α)
(−ζ1,2)j−1Jj−1(ζ1,2)
(i = α + 1, α + 2) ,
where J and I denote the Bessel function of real and
imaginary argument, respectively. Therefore, after con-
tinuing ζ →−iµ, we can derive Z(2n)({µ}) iteratively
using (16), starting from Z(0) = 1. Z(2n−1)({µ}) can be
obtained by decoupling one of the masses in Z(2n)({µ})
by sending it to inﬁnity. In this way, one obtains univer-
sally
Z(α)({µ}) =
det
1≤i,j≤α Aij({µ})
det
1≤i,j≤α µ2(j−1)
i
,
(18)
which is identical to the ﬁnite-volume QCD partition
function as calculated from the chiral Lagrangian in the
“mesoscopic” scaling limit [9,17].
Both factors in (7) being universal, the normalized hole
probability
E(α)(ζ; {µ}) = e−ζ2/4 Z(α)({
p
µ2 + ζ2})
Z(α)({µ})
(19)
as well as the smallest eigenvalue distribution [7]
P (α)(ζ; {µ}) = −∂
∂ζ E(α)(ζ; {µ})
= ζ
2e−ζ2/4
det
1≤i,j≤α Cij({
p
µ2 + ζ2})
det
1≤i,j≤α Aij({µ})
(20)
with Cij({µ}) = µj−1
i
Ij+1(µi) are universal.
As ex-
plained above, the general case of nonzero topological
charge ν is obtained by introducing |ν| massless ﬂavors
(α = Nf + |ν|).
Except for the Gaussian prefactor the expressions (19)
and (20) are explicitly given in terms of a ﬁnite-volume
ﬁeld theory partition function in the mesoscopic scaling
regime. This indicates that also these quantities can be
derived directly from ﬁeld theory in the mesoscopic scal-
ing regime, without the bypass through random matrix
theory [10].
The hole probabilities for the orthogonal (β = 1) and
symplectic (β = 4) ensembles are also related to the uni-
tary kernel K by formulae analogous to Eq. (1) (det±
represents the determinant projected to even or odd or-
ders of eigenvalues) [12]:
E1(s) = det+(1 −ˆK),
(21a)
E4(s) = 1
2

det+(1 −ˆK) + (det−(1 −ˆK)

,
(21b)
which hold regardless of the fermion determinant. Hence,
the smallest eigenvalue distributions for these ensembles
are also guaranteed to be universal. This is consistent
3
with the recently proven universality [18] of the micro-
scopic kernels for the massless chiral orthogonal and sym-
plectic ensembles [19] via universal relationships between
them and the massless chiral unitary kernel. Explicit ex-
pressions for E1(s) and E4(s) are however not known ex-
cept for the massless chiral Gaussian/Laguerre case [20].
To obtain these quantities for the corresponding massive
ensembles, our method presented here needs modiﬁca-
tion because the mapping M 7→H involves a nontrivial
Jacobian, (det H)β/2−1. This point will be discussed else-
where.
TW would like to thank T. Guhr and T. Wilke for
useful discussions.
∗
Supported in part by the Nishina Memorial Foundation
and by NSF Grant no. PHY94-07194.
†
Supported in part by European Community TMR grant
no. ERBFMRXCT97-0122.
‡
Supported in part by DFG grant We 655/11-2.
[1] O. Bohigas, M.-J. Giannoni, and C. Schmit, Phys. Rev.
Lett. 52 (1984) 1.
[2] M.E. Berbenni-Bitsch, S. Meyer, A. Sch¨afer, J.J.M. Ver-
baarschot, and T. Wettig, Phys. Rev. Lett. 80 (1998)
1146.
[3] E.V. Shuryak and J.J.M. Verbaarschot, Nucl. Phys.
A560 (1993) 306; J.J.M. Verbaarschot and I. Zahed,
Phys. Rev. Lett. 70 (1993) 3852; J.J.M. Verbaarschot,
Phys. Rev. Lett. 72 (1994) 2531; Phys. Lett. B329
(1994) 351; Nucl. Phys. B426 (1994) 559.
[4] S. Nishigaki, Phys. Lett. B387 (1996) 139; hep-th/
9712051; G. Akemann, P.H. Damgaard, U. Magnea, and
S. Nishigaki, Nucl. Phys. B487 (1997) 721.
[5] P.H. Damgaard and S.M. Nishigaki, Nucl. Phys. B518
(1998) 495.
[6] P.H. Damgaard and S.M. Nishigaki, Phys. Rev. D57
(1998) 5299.
[7] T. Wilke, T. Guhr, and T. Wettig, Phys. Rev. D57
(1998) 6486.
[8] J. Jurkiewicz, M.A. Nowak, and I. Zahed, Nucl. Phys.
B513 (1998) 759.
[9] H. Leutwyler and A. Smilga, Phys. Rev. D46 (1992)
5607.
[10] P.H. Damgaard,
Phys. Lett. B424 (1998) 322;
G.
Akemann and P.H. Damgaard, hep-th/9801133; hep-
th/9802174.
[11] P.J. Forrester, Nucl. Phys. B402 (1993) 709.
[12] M.L. Mehta, “Random Matrices”, 2nd Ed. (Academic
Press, New York, 1991).
[13] C.A. Tracy and H. Widom, Comm. Math. Phys. 163
(1994) 33.
[14] G. ’t Hooft, Nucl. Phys. B72 (1974) 461.
[15] E. Br´ezin, C. Itzykson, G. Parisi, and J.-B. Zuber,
Comm. Math. Phys. 59 (1978) 35.
[16] P. Zinn-Justin, Nucl. Phys. B497 (1997) 725.
[17] A.D. Jackson, M.K. S¸ener, and J.J.M. Verbaarschot,
Phys. Lett. B387 (1996) 355; J.J.M. Verbaarschot, hep-
th/9709032.
[18] M.K. S¸ener and J.J.M. Verbaarschot, hep-th/9801042.
[19] T. Nagao and P.J. Forrester, Nucl. Phys. B435 (1995)
401.
[20] T. Nagao and P.J. Forrester, Nucl. Phys. B509 (1998)
561.
4
