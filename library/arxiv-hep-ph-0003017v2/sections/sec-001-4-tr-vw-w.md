---
doc_id: arxiv-hep-ph-0003017v2
doc_title: "Random Matrix Theory and Chiral Symmetry in QCD J.J.M. Verbaarschot"
section_id: sec-001-4-tr-vw-w
section_title: "Tr v(W †W ) ,"
section_number: 4
pages: 15-27
source_pdf: 0003017v2.pdf
source_sha256: 1660907865346bdf
doc_brief: "Random Matrix Theory and Chiral Symmetry in QCD J.J.M. Verbaarschot — Random matrix theory is a powerful way to describe universal correlations of eigenvalues of complex systems."
---
(28)
where β is the Dyson index,
D =

0
iW
iW †
0

,
(29)
and W is an n × m matrix with ν = m −n and N = n + m. The interpretation
of this model is that N low-lying modes interact via a random interaction. A
natural representation of this model is in the form of gauge ﬁeld conﬁgurations
given by a liquid of instantons. Then the low-lying modes are the zero modes
of each instanton. We assume that ν does not exceed
√
N so that, to a good
approximation, n = N/2 for large N. The parameter N is identiﬁed as the di-
mensionless volume of spacetime. For the formulation of this model with explicit
factors of N/V included, see Ref. [31]. The potential v is deﬁned by
v(φ) =
X
k≥1
akφk .
(30)
16
J.J.M. Verbaarschot and T. Wettig
The simplest case is the Gaussian case, where v(φ) = Σ2φ. It can be shown (see
Sec. 3.5) that the microscopic spectral density does not depend on the higher-
order terms in this potential provided that the average spectral density near zero
remains nonzero. The matrix elements of W are either real [β = 1, chiral Gaus-
sian Orthogonal Ensemble (chGOE)], complex [β = 2, chiral Gaussian Unitary
Ensemble (chGUE)], or quaternion real [β = 4, chiral Gaussian Symplectic En-
semble (chGSE)]. In the latter case, the eigenvalues of D are doubly degenerate,
and the use of Majorana fermions is implemented by replacing the determinant
by its square root. For a non-Gaussian potential v(φ), we will omit the G in the
abbreviations and use chOE, chUE, and chSE, respectively. Two earlier attempts
to describe QCD Dirac eigenvalues used the Wigner-Dyson ensembles instead of
the above chiral ensembles [32].
This model reproduces the following symmetries of the QCD partition function:
• The UA(1) symmetry. All eigenvalues of the random matrix Dirac operator
occur in pairs ±iλn or are zero.
• The topological structure of the QCD partition function. The Dirac matrix
has exactly |ν| = |n −m| zero eigenvalues. This identiﬁes ν as the topological
sector of the model.
• The ﬂavor symmetry, which is the same as in QCD. For β = 2 it is SU(Nf) ×
SU(Nf), for β = 1 it is SU(2Nf), and for β = 4 it is SU(Nf) (each Majorana
ﬂavor counts as 1/2 Dirac ﬂavor).
• The chiral symmetry, which is broken spontaneously with a chiral condensate
given by
Σ = lim
N→∞πρ(0)/N .
(31)
(N is interpreted as the dimensionless volume of spacetime.) The symmetry-
breaking pattern is [25] SU(Nf) × SU(Nf) →SU(Nf), SU(2Nf) →Sp(2Nf),
and SU(Nf) →O(Nf) for β = 2, 1, and 4, respectively — the same as in QCD
[22].
• The anti-unitary symmetries. These are implemented by choosing the matrix
elements of W to be real, complex, or quaternion real for β = 1, β = 2, and
β = 4, respectively.
Along with the invariant random matrix ensembles, the chiral ensembles are part
of a larger classiﬁcation scheme that also includes ensembles for the description of
disordered superconductors [33]. In total, 10 diﬀerent families of random matrix
ensembles have been identiﬁed.
They correspond one-to-one with the Cartan
classiﬁcation of symmetric spaces [34].
The uniform distribution of the eigenfunctions over the unitary unit sphere is
expressed as the invariance
W →U†WV ,
(32)
where the n × n matrix U and the m × m matrix V are orthogonal matrices
for β = 1, unitary matrices for β = 2, and symplectic matrices for β = 4.
This invariance makes it possible to express the partition function in terms of
eigenvalues of W deﬁned by
W = U†ΛV .
(33)
Random Matrix Theory and Chiral Symmetry in QCD
17
Here, Λ is a diagonal matrix with real diagonal matrix elements λk ≥0. In terms
of the eigenvalues, the partition function (28) is given by
Zβ
Nf ,ν(m1, . . . , mNf ) =
Z
dλ|∆(λ2)|β Y
k
λβ|ν|+β−1
k
e−Nβ
4 v(λ2
k) Y
f
m|ν|
f (λ2
k + m2
f) ,
(34)
where the Vandermonde determinant is deﬁned by
∆(λ2) =
Y
k<l
(λ2
k −λ2
l ) .
(35)
In Eq. (34) and elsewhere in this review, we have omitted the normalization
constant of the partition function. From the joint eigenvalue distribution (which
is the integrand of Eq. (34)), we see that a nonzero topological charge ν can be
introduced by adding β|ν|/2 massless ﬂavors to the theory with ν = 0. Therefore,
this duality between ﬂavor and topology is a general feature of all correlation
functions. For a discussion of this duality in terms of ﬁnite volume partition
functions, see Refs. [35, 36].
3.2
Sigma Model Representation of Chiral Random Matrix Models
The chiral random matrix partition function can be evaluated using standard
random matrix methods. For simplicity, let us consider the case β = 2. The
fermion determinant can be written as a Grassmann integral, and averaging over
the Gaussian distribution function results in a four-fermion interaction. Because
of the underlying unitary invariance (32) of the chRMT, the fermionic variables
only appear in invariant combinations of the form σfg ∼¯ψf
i ψg
i , and the partition
function can be rewritten identically in terms of these variables as [20, 37]
Zν(m) =
Z
Dσ e−nΣ2Tr σσ†detν(σ + m1)detn[(σ + m1)(σ† + m1)] ,
(36)
where the quark masses have been taken real and degenerate for simplicity. The
integration is over the real and imaginary parts of the Nf ×Nf arbitrary complex
matrix σ. For m = 0 this integral is invariant under σ →UσV −1 with U and
V ∈SU(Nf). Let us calculate the integrals by a saddle-point approximation.
The saddle-point equation reads (notice that ν ≪n)
Σ2(σ† + m)σ = 1 .
(37)
The condensate at the saddle point is given by
|⟨¯ψψ⟩| =
1
2nNf
∂m log Z = Σ2
2Nf
⟨Tr(σ + σ†)⟩,
(38)
where the expectation value is with respect to the partition function (36). The
solution of the saddle-point equation, ¯σ, is proportional to the identity matrix.
In the chiral limit, we then ﬁnd ¯σ = 1/Σ, and we can identify Σ as the chiral
condensate.
The ﬂuctuations about the saddle point can be separated into massive modes
with a curvature of order n and Goldstone modes with a curvature of order mn.
In the limit n →∞, the partition function (36) can be simpliﬁed by keeping the
18
J.J.M. Verbaarschot and T. Wettig
integrals over the Goldstone manifold and performing the remaining integrals by
a saddle-point integration. This results in the partition function
Zν(m) =
Z
U∈U(Nf )
DU detνU enΣTr (MU+M†U−1) ,
(39)
which is the familiar ﬁnite volume partition function to be discussed in Sec. 4.1.
3.3
θ-Dependence of the Partition Function
The θ-dependence of the partition function is obtained by summing over all topo-
logical sectors of the partition function according to Eq. (11), which applies to
full QCD where the partition function is obtained by integrating over the gauge
ﬁelds. The terms Zν in this equation reﬂect the probability of encountering gauge
ﬁelds with topological charge ν.
For the eﬀective theory, the partition function in the topological sector ν is
given in Eq. (39). However, this ν-dependence is only due to the fermion deter-
minant. In the sum over ν, we should therefore add weight factors P(ν) that take
into account the distribution of topological charge of the quenched gauge ﬁelds
(i.e. gauge ﬁelds generated without the fermion determinant). This yields
Zeﬀ(θ, m) =
X
ν
P(ν)eiνθZeﬀ
ν (m) .
(40)
Below, we argue that the weight factors can be ignored for light quarks but that
they are necessary when one considers the quenched theory (which corresponds
to Nf = 0 or, equivalently, to the limit of very heavy quarks).
Our starting point is that the topological susceptibility of the quenched gauge
ﬁelds is nonvanishing, i.e.
⟨ν2⟩q
V̸
= 0 .
(41)
Invoking the central limit theorem, we assume that P(ν) is Gaussian,
P(ν) =
1
q
2π⟨ν2⟩q
e
−
ν2
2⟨ν2⟩q ,
(42)
which has been veriﬁed by quenched lattice QCD simulations.
We analyze the partition function (40) for Zeﬀ
ν (m) given by the ﬁnite-volume
partition function in Eq. (39). Replacing the sum over ν by an integral, we obtain
after integration
Zeﬀ(θ, m) =
Z
U∈U(Nf )
DUe−
⟨ν2⟩q
2
(θ−iTr log U)2+ 1
2 ΣV Tr (MU+M†U−1) .
(43)
The exponent in the integrand corresponds to the eﬀective static potential of QCD
with a large number of colors [38], and therefore the chRMT partition function
reproduces all identities that have been derived from this eﬀective potential [20,
39].
For example, the topological charge is screened by light quarks.
For a
careful analysis of the periodicity requirements of the θ-dependence of the eﬀective
partition function (43), see Ref. [40].
Let us illustrate the screening of topological charge for Nf = 1 and real m, for
which
Zeﬀ(θ, m) =
Z
dφ e−
⟨ν2⟩q
2
(θ−φ)2+ΣV m cos φ .
(44)
Random Matrix Theory and Chiral Symmetry in QCD
19
The integral over φ can be performed by a saddle-point approximation resulting
in [23]
Zeﬀ(θ, m) = emV Σ cos θ.
(45)
The topological susceptibility is given by
⟨ν2⟩= −∂2
∂θ2 log Z = mV Σ
(for θ = 0)
(46)
so that the topological charge is completely screened in the chiral limit. This also
shows that the results are insensitive to our choice of the distribution function
P(ν). For example, in an instanton liquid interpretation of the chiral random
matrix model, the natural choice for P(ν) is the binomial distribution B(N−ν, ν),
resulting in the same eﬀective potential [20].
In fact, it can be concluded from Eq. (46) that for light quarks the distribution
P(ν) can be ignored altogether. Let us again illustrate this for Nf = 1, for which
the integral in Eq. (39) results in the ﬁnite volume partition function
Zeﬀ
ν (m) = Iν(mV Σ) ,
(47)
where Iν is a modiﬁed Bessel function. Summing over ν according to Eq. (11),
i.e. without the weight factors P(ν), we obtain [41]
Zeﬀ(θ, m) =
X
ν
eiνθIν(mV Σ) = emV Σ cos θ ,
(48)
where we have used a summation formula for modiﬁed Bessel functions. This is
exactly the same result as in Eq. (45). For an extension of these results to more
than one ﬂavor, see Ref. [41].
3.4
Spectral Correlation Functions
In this section, we discuss the spectral correlation functions and the microscopic
spectral density corresponding to the chRMT partition function.
The global
spectral density is a semicircle. It is not universal and we do not expect to ﬁnd
it in realistic physical systems. The universal quantities are local or microscopic
spectral correlation functions. In general, a k-point spectral correlation function
is deﬁned by [27]
Rk(λ1, . . . , λk) =
*
N
X
j1 · · · jk = 1
jp̸ = jq
δ(λ1 −Ej1) · · · δ(λk −Ejk)
+
,
(49)
where the Ejp are eigenvalues. The quantity Rk represents the probability density
to ﬁnd k eigenvalues, regardless of labeling, at λ1, . . . , λk. In particular, R1(λ) =
ρ(λ). By “local” we mean that the energy diﬀerences |λp −λq| are of the order
of a few mean level spacings.
Because of the UA(1) symmetry of QCD, all nonzero eigenvalues come in pairs
±iλn (see Sec. 2.2.1).
This implies that the origin, λ = 0, is a special point
of the spectrum and that we have to consider the Rk separately in the bulk of
the spectrum and near λ = 0. The latter is called the microscopic region or the
20
J.J.M. Verbaarschot and T. Wettig
“hard edge” of the spectrum.2 In addition, there is the tail or “soft edge” of
the spectrum, which we do not discuss. The bulk of the spectrum is the middle
region, far from either edge.
Because the random matrix partition function is known in terms of an integral
over the eigenvalues of the Dirac operator, see Eq. (34), it is possible to obtain
the spectral density and all spectral k-point correlation functions by integration
over N −k eigenvalues. In the present case, the integrals can be performed most
conveniently by the orthogonal polynomial method. We mention only the most
important results in the sections below.
3.4.1
BULK CORRELATIONS
Our conventions are such that if we have N eigenvalues, the global spectral
density is normalized to N so that the mean level spacing is of order 1/N. Local
spectral correlation functions Rk(λ1, . . . , λk) in the bulk of the spectrum are thus
characterized by λp ∼O(1) and |λp −λq| ∼O(1/N).
Universal correlation
functions are obtained by rescaling the eigenvalues according to the average local
level spacing. This procedure, known as unfolding, is discussed in more detail in
Sec. 5.1. The rescaled eigenvalues with average level spacing equal to unity are
denoted by xk.
In the bulk of the spectrum, the RMT results for the Rk are identical for
the chiral ensembles and the corresponding nonchiral ensembles [42, 43].
For
simplicity, let us consider the simplest ensemble, the chUE. On the unfolded
scale, we obtain in the limit N →∞
Rk(x1, . . . , xk) = det[K(xp, xq)]p,q=1,...,k
(50)
with the sine kernel
K(x, y) = sin π(x −y)
π(x −y)
.
(51)
The fact that K(x, y) depends only on |x−y| reﬂects the translational invariance
of the spectral properties after unfolding. The results for the chOE and the chSE
are somewhat more complicated than those for the chUE [17].
Other quantities can be derived from the Rk. As a measure of short-range
correlations between the eigenvalues, one considers the nearest-neighbor spacing
distribution P(s), which is the probability density to have a spacing of s be-
tween adjacent levels. In random matrix theories, one ﬁnds that P(s) ∼sβ for
small values of s and has a Gaussian tail for large spacings. Long-range spectral
correlations are characterized by the level-number variance Σ2(L) given by
Σ2(L) =
D
(n(L) −L)2E
,
(52)
where n(L) is the number of levels in an interval of length L, or by the spectral
rigidity ∆3(L) [44], which is deﬁned as an integral transform of Σ2(L),
∆3(L) = 2
L4
Z L
0
du (L −u)(L2 −Lu −u2)Σ2(u) .
(53)
2The reason for this nomenclature is that in a Fermi-gas formulation of RMT, where the
eigenvalues are interpreted as the positions of particles, this symmetry corresponds to choosing
a potential that is inﬁnite for negative values of the eigenvalues. In this picture, the soft edge
corresponds to a potential with a ﬁnite slope.
Random Matrix Theory and Chiral Symmetry in QCD
21
The advantage of using the ∆3-statistic is that its statistical ﬂuctuations are
much smaller than those of the Σ2-statistic. The quantities Σ2 and ∆3 can be
derived from the two-point function R2. To compute P(s), one needs all k-point
functions. These quantities are very diﬀerent for systems with correlated eigen-
values (described by RMT) and systems with uncorrelated eigenvalues (described
by the Poisson ensemble). For example, the large-L behavior of the chUE results
is given by Σ2(L) ∼(ln L)/π2 and ∆3(L) ∼(ln L)/2π2, whereas for uncorrelated
eigenvalues one ﬁnds Σ2(L) = L and ∆3(L) = L/15.
3.4.2
MICROSCOPIC CORRELATIONS
In the context of QCD, the small eigenvalues are more interesting than those in
the bulk because of their relation to spontaneous chiral symmetry breaking via
the Banks-Casher relation. The local spectral correlation functions at the hard
edge of the spectrum are characterized by λp ∼O(1/N) and |λp −λq| ∼O(1/N).
Unfolding in the microscopic region is easy; the eigenvalues are simply rescaled
by the mean level spacing at λ = 0, which is given by Eq. (23). By convention,
we deﬁne the unfolded variables by xp = λpV Σ, i.e. the factor of π is omitted.
Note that V ∝N.
Thus, in the unfolded variables we have xp ∼O(1) and
|xp −xq| ∼O(1). As advertised above, the functional form of the Rk is diﬀerent
in the microscopic region. The Rk are still given by the determinant of a kernel
according to Eq. (50), but the sine kernel is now replaced by the Bessel kernel
[45],
K(x, y) = √xy xJα+1(x)Jα(y) −yJα(x)Jα+1(y)
x2 −y2
,
(54)
where Jα denotes Bessel functions and α = Nf + |ν|, with Nf the number of
massless ﬂavors and ν the topological charge. A mathematical discussion of the
Bessel kernel can be found in Ref. [46].
The RMT results for the chOE and the chSE are more complicated [47, 48,
49, 33].
Note that, in contrast to the situation in the bulk, the microscopic
correlations depend on Nf and ν.
The one-point function is universal in the microscopic region. For the chUE,
the microscopic spectral density, deﬁned above in Eq. (25), is related to the kernel
by ρs(z) = K(z, z) and can be expressed as [45, 50]
ρs(z) = z
2
h
J2
Nf +|ν|(z) −JNf +|ν|+1(z)JNf +|ν|−1(z)
i
.
(55)
It is also the generating function for the Leutwyler-Smilga sum rules, which are
essentially inverse moments of ρs (or of higher-order spectral correlation func-
tions). They are discussed below. The results (54) and (55) were ﬁrst derived
using chiral RMT. In the meantime, Eq. (55) has been conﬁrmed by an explicit
calculation starting from a partially quenched chiral Lagrangian [51, 52], which is
discussed in the next section. The microscopic spectral density and the two-point
correlation function for the case Nf + |ν| = 0 have also been derived by means of
the supersymmetric method of RMT [53].
There is a very interesting connection between the Bessel kernel and the ef-
fective partition function.
In addition to the partition function Z(Nf ) for Nf
massless sea quarks, one can also compute the partition function Z(Nf +2) for Nf
massless quarks and two additional ﬂavors with imaginary masses.
One then
22
J.J.M. Verbaarschot and T. Wettig
ﬁnds the relation [54]
K(x, y) = 1
2(xy)Nf +1/2 Z(Nf+2)(ix, iy)
Z(Nf)
,
(56)
which can also be generalized to massive sea quarks. Thus, to obtain the Rk
for Nf ﬂavors, one needs to know the partition function for two additional ﬂa-
vors with imaginary masses. This result has a natural interpretation in terms
of the eﬀective spectral partition function (discussed below in Sec. 4). The two
additional ﬂavors are the spectral quark and its bosonic superpartner [51]. The
relation (56) once again demonstrates the equivalence of the random matrix for-
mulation and the eﬀective ﬁeld theory in the zero mode domain.
Additional
consistency conditions for the ﬁnite volume partition function are discussed in
Ref. [55].
3.5
Universality Proofs
In most random matrix calculations, the probability distribution of the random
matrix elements is assumed to be Gaussian to simplify the calculation. Nonuni-
versal features such as the global spectral density depend on the choice of the
probability distribution. On the other hand, universal results of RMT do not
depend on this choice, nor on other deformations of the random matrix model.
In addition to numerous empirical veriﬁcations of universal behavior in RMT,
analytical proofs of universality have recently been constructed for two diﬀerent
types of deformations.
First, consider deformations that do not break the invariance of the theory
under unitary transformations of the random matrix. In this case, the Gaus-
sian distribution P(W) ∝exp(−Na1 Tr WW †) is replaced by the more general
distribution P(W) ∝exp(−N P∞
k=1 ak Tr (WW †)k), i.e. the quadratic term in
the exponent is replaced by an arbitrary polynomial. The advantage of the uni-
tary invariance is that the probability distribution depends only on the eigen-
values of WW †.
For the chiral ensembles, it has been shown that both the
bulk and the microscopic spectral correlations remain unchanged on the un-
folded scale [49, 56, 57, 58, 59, 60].
The weight function of QCD also con-
tains the fermion determinant, and it has been shown that the universal results
are unchanged if the random Dirac matrix in the determinant is replaced by
a polynomial of that matrix [61]. Universal microscopic correlations have also
been found for the so-called Ginsparg-Wilson Dirac operator [62]. Along with
work on universality for the much more widely studied Wigner-Dyson ensem-
bles [63, 64, 65, 66, 67, 68, 69, 57, 70, 71, 72, 73], these ﬁndings make it clear
that spectral correlations on the scale of the average level spacing are strongly
universal, i.e. they do not change despite substantial variations of the average
spectral density. There have also been several interesting results on the validity
of universality for wide correlators, i.e. on macroscopic scales [64, 65, 66, 74].
Second, consider deformations that do break the unitary invariance by adding
an arbitrary deterministic matrix Y to the random matrix W in the Dirac oper-
ator. As we discuss in Sec. 6, such a model can provide a schematic description
of QCD at nonzero temperature. In particular, the matrix Y can be chosen in
such a way that ρ(0)/V vanishes so that chiral symmetry is restored. It has been
proven that the bulk correlations on the unfolded scale are unaﬀected by the
Random Matrix Theory and Chiral Symmetry in QCD
23
matrix Y , and that the same is true for the microscopic spectral correlations as
long as ρ(0)/V remains nonzero [75, 76, 77, 78, 79, 80].
Most universality proofs have been performed for random matrix ensembles
with β = 2.
However, it is possible to establish relations between the β =
2 kernel and the kernels of the other two ensembles with β = 1 and β = 4
[47, 81, 82, 83, 84]. From these relations and the universality of the β = 2 results,
one can then infer the universality of the β = 1 and β = 4 results. Recently,
interesting connections between massive correlators and the massless correlators
for β = 1 and β = 4 have been made [85], and the transition between these
ensembles and the β = 2 ensemble has been studied [86].
The microscopic spectral correlations are universally given by RMT only if
ρ(0)/V > 0. An interesting question [87] is what happens to the Rk if there is
some phase transition so that ρ(0)/V vanishes. This transition could be triggered
by, for example, nonzero temperature or a large number of ﬂavors. Beyond the
transition point, there will be a gap in the spectrum, and the smallest eigenvalues
beyond this gap are presumably described by the soft-edge results of RMT. What
is more interesting, however, is the transition point at which ρ(0)/V becomes
zero so that there is no gap. This situation has been investigated in two diﬀerent
ways. First, keeping the unitary invariance, one can ﬁne-tune the polynomial in
the exponent of P(W) to make ρ(0)/V just vanish [87]. Second, breaking the
unitary invariance, one can choose a “critical” deterministic matrix Y so that
ρ(0)/V = 0 without a gap [88, 89]. In both cases, one obtains new functional
forms for the microscopic spectral correlations and a diﬀerent scaling with the
volume (or matrix dimension). However, the results are not unique; they depend
on the way one chooses to approach the ρ(0)/V = 0 limit. It is, therefore, an open
question as to whether the microscopic spectral correlations of the QCD Dirac
operator at the chiral phase transition agree with one of the results obtained in
a random matrix model.
4
EFFECTIVE THEORIES AT LOW ENERGIES
4.1
Finite-Volume Partition Function
As we have seen before, chiral symmetry is spontaneously broken by the QCD
vacuum.
According to Goldstone’s theorem, this leads to the appearance of
massless modes. The Lagrangian describing the dynamics of these modes can be
obtained solely from the symmetries of the QCD partition function. Goldstone
modes corresponding to the symmetry-breaking pattern SUR(Nf) × SUL(Nf) →
SUV (Nf) can be parameterized as
U = URU−1
L
(57)
with UR ∈SUR(Nf) and UL ∈SUL(Nf). The chiral Lagrangian is constructed
by the requirement that it should have the same invariance properties as the
QCD Lagrangian.
In particular, for m = 0 the Lagrangian should be both
Lorentz invariant and invariant under SUR(Nf) × SUL(Nf).
To lowest order
in the momenta (or derivatives), the kinetic term in the eﬀective Lagrangian is
uniquely given by [6, 7]
Lkin = F 2
4 Tr ∂µU∂µU−1 .
(58)
24
J.J.M. Verbaarschot and T. Wettig
The parameter F is the pion decay constant. The mass term in the QCD La-
grangian breaks the full ﬂavor symmetry. However, the full symmetry can be
restored if the mass matrix is transformed as well,
M →ULMU−1
R .
(59)
We require that the mass term in the eﬀective Lagrangian satisﬁes this extended
symmetry. To lowest order in M, it is therefore uniquely given by
Lm = −1
2Σ Tr (MU + M†U−1) .
(60)
For a diagonal mass matrix, the action is therefore minimized by U = 1. The
normalization of the mass term is such that the mass derivative of the partition
function according to Eq. (21) is equal to the chiral condensate Σ. The chiral
Lagrangian is valid in the domain
m ≪Λ
and
p ≪Λ ,
(61)
where p is the momentum and Λ is a typical hadronic mass scale.
We will study the eﬀective Lagrangian at ﬁnite volume in a box of volume L4.
Then the smallest nonzero-momentum modes are of the order
p ∼1/L .
(62)
The ﬂuctuations of the zero-momentum modes, the constant ﬁelds, are not af-
fected by the kinetic term and are limited only by the mass term. Comparing
Eqs. (58) and (60), we see that in a domain where
mΣ
F 2 ≪1
L2 ,
(63)
the ﬂuctuations of the zero-momentum modes completely dominate the ﬂuctu-
ations of the nonzero-momentum modes. The mass-dependence of the eﬀective
partition function is then given by [19, 23]
Z(m, θ) =
Z
U∈SU(Nf )
DU eV Σ Re Tr Umeiθ/Nf ,
(64)
where we have set M = m1 and have introduced the θ-dependence by the sub-
stitution m →m exp(iθ/Nf) just as for the QCD partition function. Combining
the conditions (61) and (63), we ﬁnd that the ﬁnite volume partition function is
valid in the domain [19, 23]
m ≪
1
ΛL2 ≪Λ .
(65)
The partition function for a given topological charge can be extracted from its
θ-dependence. Since
Z(m, θ) =
X
ν
eiνθZν(m) ,
(66)
we obtain Zν by Fourier inversion. Thus, the ﬁnite volume partition function in
the sector of topological charge ν is
Zν(m) = 1
2π
Z
dθ e−iνθZ(m, θ) =
Z
U∈U(Nf )
DU detνU eV Σ Re Tr mU ,
(67)
which coincides with Eq. (39).
The partition function (67) can be evaluated
for arbitrary masses. The integrals were ﬁrst calculated in the context of one-
plaquette lattice QCD models [90] but later rederived by means of Itzykson-Zuber
integrals [91, 92, 93].
Random Matrix Theory and Chiral Symmetry in QCD
25
4.2
Leutwyler-Smilga Sum Rules
For masses in the domain of Eq. (65), we can equate the mass dependence of the
QCD partition function and the mass dependence of the eﬀective partition func-
tion. Equating the coeﬃcients of the expansion in powers of the mass then gives
us the so-called Leutwyler-Smilga sum rules [23]. The QCD partition function
can be expanded as
ZQCD
ν
(m) = ⟨m|ν| Q′
k(m + iλk)⟩
⟨Q′
k iλk⟩
= m|ν|
1 + m2D X
λk>0
1
λ2
k
E
+ . . .

,
(68)
where the prime indicates that the product is over nonzero eigenvalues only. The
eﬀective partition function can be expanded in a power series in m as well. From
the U(1) part of the group integral, it is clear that Zeﬀ
ν (m) ∝m|ν|. Thus,
Zeﬀ
ν
= m|ν|(a0 + a1m2 + . . .) ,
(69)
where the coeﬃcients ai are obtained by calculating the group integrals. Let us
consider two examples. The simplest example is Nf = 1, for which
Zeﬀ
ν
= 1
2π
Z
dθ e−iνθemV Σ cos θ = Iν(mV Σ) .
(70)
The series expansion of the modiﬁed Bessel function is given by
Iν(x) = 1
ν!
x
2
ν
+
1
(ν + 1)!
x
2
ν+2
+ . . .
(71)
for ν ≥0. We also have I−ν(x) = Iν(x). Matching the normalizations of Eqs. (68)
and (69) and equating the coeﬃcients of the O(m2) terms, we ﬁnd
*
1
V 2
X
λk>0
1
λ2
k
+
=
Σ2
4(|ν| + 1) .
(72)
A second example is the case of ν = 0 and arbitrary Nf. In this case, we use the
group integral
Z
DU UijU†
kl = 1
Nf
δjkδil
(73)
to derive the result
*
1
V 2
X
λk>0
1
λ2
k
+
= Σ2
4Nf
.
(74)
Since asymptotically for large λ the spectral density is proportional to V λ3, the
sum over the eigenvalues has to be regularized. As discussed above in Sec. 2.3, a
ﬁnite result is obtained by taking the thermodynamic limit before removing the
cutoﬀ.
What do we learn from these sum rules? Since the total number of eigenvalues
is of order V , the obvious interpretation is that the smallest eigenvalues are of
order 1/V . Indeed, this is in agreement with the Banks-Casher formula. What
is more important, however, is that in the derivation of the sum rules we have
relied only on the chiral symmetry of the partition function and its spontaneous
breaking by the formation of a chiral condensate.
Therefore any theory with
26
J.J.M. Verbaarschot and T. Wettig
the same pattern of chiral symmetry breaking as QCD should obey the same
spectral sum rules. In particular, the eigenvalues distributed according to the
chRMT introduced in the previous section should obey the same sum rules. In
fact, all Leutwyler-Smilga sum rules can be derived systematically from the joint
eigenvalue chRMT probability distribution in Eq. (34) using the known Selberg
integrals [94]. In addition to these sum rules, it is possible to derive massive sum
rules [95]. A relation between sum rules and partially quenched eﬀective theories
was considered in Ref. [96].
Spectral sum rules for Ginsparg-Wilson fermions
on the lattice were considered in Ref. [97]. Inverse moments of the small Dirac
eigenvalues in generalized chiral perturbation theory were derived in Ref. [98].
We have seen that chRMT allows us to calculate the correlations of the smallest
eigenvalues of the Dirac operator on the scale of the average level spacing. This
raises the question of whether it is possible to derive the microscopic properties
of the eigenvalues from the low-energy eﬀective partition function. The answer
is no. The spectral density cannot be derived from the mass dependence of the
chiral condensate,
Σ(m) =
*
1
V
X
k
1
iλk + m
+
,
(75)
because the average contains the fermion determinant with the same mass. As we
show in the next section, this problem can be circumvented by the introduction
of a spectral mass.
4.3
Spectral Mass and Partially Quenched Partition Function
The Dirac spectrum can be obtained from the resolvent
Σ(z) =

 1
V Tr
1
D + z

,
(76)
were the spectral mass z is an independent complex variable that does not occur
in the average. With purely imaginary eigenvalues the spectral density is given
by the discontinuity of the resolvent across the imaginary axis,
ρ(λ)
V
= lim
ǫ→0
1
2π[Σ(iλ + ǫ) −Σ(iλ −ǫ)] .
(77)
This follows immediately upon writing the trace as a sum over the eigenvalues of
D. The generating function for the resolvent can be written down easily [99],
Zsp =
*
detNf (D + m) det(D + z)
det(D + z′)
+
YM
,
(78)
where we have explicitly displayed the fermion determinant in the measure. The
resolvent is then given by
Σ(z) = 1
V ∂zZsp(z, z′)

z′=z
.
(79)
In QCD, this method was ﬁrst introduced in order to derive the quenched strong
coupling expansion [100]. In nuclear physics and condensed matter physics, this
method is known as the supersymmetric method or Efetov method for quenched
disorder [101, 102, 103].
Random Matrix Theory and Chiral Symmetry in QCD
27
The determinants in the numerator can be written as fermionic integrals where-
as the determinant in the denominator can be written as a bosonic integral.
The partition function (78) is thus invariant under ﬂavor symmetries that mix
commuting and anticommuting degrees of freedom. More precisely, for m = z =
z′ = 0 the partition function is invariant under the supergroup GlR(Nf + 1|1) ×
GlL(Nf + 1|1). In order to obtain a consistent eﬀective theory, it is essential to
extend the unitary symmetry to the general linear group Gl. We expect, as for
the QCD vacuum, that chiral symmetry is spontaneously broken to the diagonal
subgroup GlV(Nf + 1|1). The mass term explicitly breaks the full symmetry to
this subgroup as well.
The eﬀective partition function can be derived in the same way as the regular
chiral Lagrangian with one complication. To obtain ﬁnite integrals, we must make
sure that the integration manifold is Riemannian. This is why we have extended
the ﬂavor symmetry to the full general linear group. The integration manifold is
then given by the maximum Riemannian submanifold of GlA(Nf + 1|1). In plain
language, this means that we compensate the extra minus sign in the supertrace
by complexifying the group parameters. The generating function is thus given
by [51]
Zpq =
Z
U∈ˆ
Gl(Nf +1|1)
DUe
R
d4x

−F 2
