---
doc_id: arxiv-hep-lat-9912004v2
doc_title: "Microscopic Universality and the Chiral Phase Transition in two Flavor QCD F. Farchioni"
section_id: sec-003-ii-expectations-from-chrmt
section_title: "EXPECTATIONS FROM CHRMT"
section_number: II
pages: 2-3
source_pdf: 9912004v2.pdf
source_sha256: 7033719ec7a8a0bc
doc_brief: "Microscopic Universality and the Chiral Phase Transition in two Flavor QCD F. Farchioni — 9 sections: Hip; B. Lang; INTRODUCTION"
---
According to the nature of the elements in the random
matrix, chRMT appears in three universality classes.
In this paper we consider the SU(3) gauge theory with
quarks in the fundamental representation, which belongs
to the universality class of the chiral unitary ensemble
(chUE). The partition function under study is [2,16,17]
Z(Nf)({m}) =
Z
dM e−NTrU(M2)
×
Nf
Y
f=1
det(M + T + imf) ,
(2.1)
where M is a 2N × 2N block hermitian matrix (the ele-
ments of W being random complex numbers), and T is a
deterministic, i.e. not-random, oﬀ-diagonal block matrix
M =

0
W
W †
0

,
T =

0 t
t 0

.
(2.2)
Here dM denotes the Haar measure, U(x) is an analytic
function.
The predictions from chRMT concern the correlations
between the eigenvalues λ of D ≡M + T on the scale
of individual eigenvalues in the thermodynamic limit
N →∞. The matrix D is the analogue of the mass-
less Dirac operator in QCD. The chiral phase transition
within chRMT is identiﬁed through the value of the spec-
tral density of the eigenvalues of D near zero, i.e. using
the Banks-Casher relation.
Modeling
the
chiral phase
transition
in
chRMT
amounts to driving a depletion of eigenvalues of D near
the origin by means of some temperature parameter.
Two separate approaches have been examined in the lit-
erature. First, the unitary invariant chRMT [2,3], corre-
sponding to (2.1) with T = 0, in which the chiral phase
transition is driven by tuning U(M 2). Second, the non-
unitary invariant chRMT [16–18], corresponding to (2.1)
with U(M 2) = M 2, where the deterministic block matrix
T mimics the eﬀect of the temperature. In this paper we
do not need to distinguish between the two approaches
as they are consistent for the quantities measured here.
Below Tc, i.e. when ρ(0)̸ = 0, chRMT predicts [19] the
probability distribution for the smallest eigenvalue (for
the trivial topological sector)
P(z, {µ}) = z
2 e−z2/4 det1≤i,j≤Nf Cij({
p
µ2 + z2})
det1≤i,j≤Nf Aij({µ})
,
(2.3)
with
Aij({µ}) ≡µj−1
i
Ij−1(µi) ,
Cij({µ}) ≡µj−1
i
Ij+1(µi) ,
z = 2 π λ ρ(0) N , and µf = 2 π mf ρ(0) N . (2.4)
2
where ρ(0) is the spectral density at the origin for the
massless situation (i.e. when mf = 0 in (2.1)). Ij de-
notes the j’th modiﬁed Bessel function. This result is
universal in the chRMT context, that is, the analytic
form of P(z, {µ}) does not change under deformations of
U(M 2) provided that ρ(0)̸ = 0. After the identiﬁcation
V ≡2 N (V is the physical volume in lattice units), (2.3)
allows to extract Σ = π ρ(0) (the fermion condensate in
the chiral limit) from ﬁnite-volume Dirac spectra.
Of
course, in this the mild condition (1.1) must be satisﬁed.
Above Tc, when there is a ﬁnite gap in the spectral
density, the repulsion between the eigenvalue pair ±λmin
becomes negligible; chRMT hence predicts a soft inner
edge, known as the Airy-solution [20,21].
At Tc — signaled in chRMT by a power-like behavior
of the spectral density at small λ — ρ(λ) ∝λ
1
δ , the pre-
diction from chRMT is not unique. It turns out that the
spectral correlators depend on the value of δ [22].
The distribution of the smallest eigenvalue is a spec-
tral one-point correlation function and is quite sensitive
to statistical ﬂuctuations (see below). As an additional
measure we also study a two-point correlator: the level
spacing distribution P(s). Note that the level spacings,
s = si+1 −si, are determined in the unfolded spectrum
{si}2N
i=1. Unfolding separates the ﬂuctuation properties of
the spectrum from the supposedly smooth background
behavior. The unfolded variable is deﬁned in terms of
the eigenvalue spectrum and the local average spectral
density by
si =
Z λi
0
⟨ρ(λ)⟩dλ .
(2.5)
The RMT prediction for the level spacing distribution is
well approximated by the unitary Wigner surmise
P(s) = 32
π2 s2 e−4 s2
π
.
(2.6)
The level spacing distribution is not expected to be af-
fected by temperature and masses in chRMT, see e.g.
[23].
chRMT makes predictions for average spectral corre-
lators in sectors with deﬁnite topological charge ν, i.e.
derived assuming exact zero modes (these are not in-
cluded in the predicted distributions; cf. [24] for the re-
sult of the weighted summation of all topological sec-
tors). For Ginsparg-Wilson fermions [25], which realize
chiral symmetry on the lattice, one may identify exact
zero modes as resulting from topological excitations ac-
cording to the Atiyah-Singer index theorem (for Wilson
fermions one can hypothesize that zero modes are re-
placed by real modes). This is not the case for staggered
fermions, where exact zero modes are absent away from
the continuum limit [26] and even gauge conﬁgurations
with non-vanishing topological charge do not give zero
eigenvalues. Exact zero modes are here replaced by “al-
most” zero modes which accumulate to the origin in the
continuum limit. In the strong coupling region the mi-
croscopic staggered Dirac spectra summed over all topo-
logical sectors show [27,28] good agreement with the an-
alytical prediction for the topologically neutral, ν = 0,
sector from chRMT. However, approaching weaker cou-
pling observations contradicting this scenario have been
found in a two-dimensional context [29].
Before turning to the numerical studies, let us com-
ment on the validity of the chRMT predictions.
The
condition for application of chRMT in lattice analyses is
well established when T ∼0: The range in the unfolded
spectrum over which the chRMT correlations dominate is
|λ| ≤
f 2
π
⟨¯ψψ⟩L2x [30,31], where fπ is the pion decay constant.
An equivalent statement for T ≥Tc is not known and no
stringent tests of the low-lying eigenvalue statistics have
been carried out so far.
Let us emphasize that even though the larger part of
the studies of chRMT have been focused on the situa-
tion where ρ(0)̸ = 0, there is nothing wrong from ﬁrst
principles in using chRMT when ρ(0) = 0.
