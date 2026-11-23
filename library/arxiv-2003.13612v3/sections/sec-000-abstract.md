---
doc_id: arxiv-2003.13612v3
doc_title: "On the mass difference between proton and neutron"
section_id: sec-000-abstract
section_title: "Abstract"
section_number: null
pages: 1-10
source_pdf: 2003.13612v3.pdf
source_sha256: 98a3287428a46e57
toc_source: inferred
doc_brief: "On the mass difference between proton and neutron — The Cottingham formula expresses the electromagnetic part of the mass of a particle in terms of the virtual Compton scattering amplitude."
---
The Cottingham formula expresses the electromagnetic part of the mass of a particle in terms of
the virtual Compton scattering amplitude. At large photon momenta, this amplitude is dominated
by short distance singularities associated with operators of spin 0 and spin 2. In the diﬀerence
between proton and neutron, chiral symmetry suppresses the spin 0 term. Although the angular
integration removes the spin 2 singularities altogether, the various pieces occurring in the standard
decomposition of the Cottingham formula do pick up such contributions. These approach asymp-
totics extremely slowly because the relevant Wilson coeﬃcients only fall oﬀlogarithmically. We
rewrite the formula in such a way that the leading spin 2 contributions are avoided ab initio. Using
a sum rule that follows from Reggeon dominance, the numerical evaluation of the e.m. part of the
mass diﬀerence between proton and neutron yields mQED = 0.58 ± 0.16 MeV. The result indicates
that the inelastic contributions are small compared to the elastic ones.
Keywords: Electromagnetic mass diﬀerences; Dispersion relations; Regge behaviour; Structure
functions; Protons and neutrons; Cottingham formula
The fact that proton and neutron nearly have the same mass is understood since the 1930s, as
consequence of an approximate symmetry: isospin [1]. For a long time, it was taken for granted
that the symmetry is broken only by the e.m. interaction – the Cottingham formula [2] did explain
the size of the observed mass diﬀerences with ∆I = 2, mπ+ −mπ0 for instance. For ∆I = 1, however,
in particular for mp −mn, the fact that the charged particle is lighter than the neutral one remained
mysterious [3–5].
In 1975, Gasser and Leutwyler [6] pointed out that the mystery disappears if the popular con-
viction, according to which the strong interaction conserves isospin, is dismissed. They showed
that a coherent picture of isospin breaking can be reached within the Quark Model, provided the
Email addresses: gasser@itp.unibe.ch (J. Gasser), leutwyler@itp.unibe.ch (H. Leutwyler),
rusetsky@hiskp.uni-bonn.de (A. Rusetsky)
masses of the two lightest quarks are not only very small but also very diﬀerent. At that time, the
experimental results on deep inelastic scattering were consistent with the scaling laws of Bjorken
[7]. Evaluating the Cottingham formula with the scarce experimental information available then,
they concluded that the elastic contributions dominate over the inelastic ones and arrived at the
estimate mQED = 0.7 ± 0.3 MeV [6].
Walker-Loud, Carlson and Miller [8] claimed that the analysis in [6] is incorrect and instead
arrived at mQED = 1.30(03)(47). This paper triggered renewed interest and several authors investi-
gated the matter [9–12]. We will brieﬂy discuss the results obtained in these works below. Some
of the claims made in [8] are rectiﬁed in Appendix E of [13] and in [14, 15].
A thorough account of our recent work on the subject with the technical details of the calcu-
lation is given in [16]. The aim of the present paper is to describe the basic ideas underlying our
analysis and the conclusions drawn from it.
Cottingham formula. We denote the e.m. self-energy of the particle by mγ. As shown by
Cottingham [2], it is determined by the spin averaged forward Compton scattering amplitude,
T µν(p, q) = i
2
Z
d4x eiq·x⟨p|T jµ(x)jν(0)|p⟩.
(1)
Current conservation, Lorentz invariance and symmetry under space reﬂection imply that T µν can
be expressed in terms of two functions T1(ν, q2), T2(ν, q2) that only depend on ν = p · q/m and q2
(m is the mass of the particle). We use the notation of [13]:
T µν(p, q) = (qµqν −gµνq2)T1(ν, q2)
(2)
+ 1
m2{(pµqν + pνqµ)p · q −gµν(p · q)2 −pµpνq2}T2(ν, q2) .
The Cottingham formula represents mγ as an integral over the four components of the photon
momentum q. In the rest frame of the particle, the analytic properties of the time-ordered product
allow one to perform a Wick rotation that turns the path of integration in the variable q0 from
the real axis into the imaginary axis, q0 = iQ4 [2, 13]. The variable ν coincides with q0 and
thus becomes purely imaginary. Identifying Q1, Q2, Q3 with the space components of the physical
momentum, we have q2 = −Q2, where Q is the length of the euclidean four-vector Qµ. The
Cottingham formula then takes the form of an integral over euclidean space:
mγ =
e2
2m(2π)4
Z d4Q
Q2 φ ,
φ = 3Q2T1 + (2Q2
4 + Q2)T2 ,
(3)
where T1, T2 are to be evaluated at ν = iQ4, q2 = −Q2.
Operator product expansion. The asymptotic behaviour of the integrand in formula (3) is
controlled by the operator product expansion [17–22]. The leading contributions are determined
by the Wilson coeﬃcients of the operators of lowest dimension, which carry either spin 0 or spin
2. The explicit expressions [21–23] show that the contributions from T1 and T2 both diverge –
the formula (3) must be regularized, e.g. by cutting the integral oﬀwith Q2 ≤Λ2. We denote the
regularized version of mγ by mΛ
γ .
2
Since the operators of spin 2 are of anomalous dimension, their contributions to the asymptotic
behaviour of T1 and T2 involve a negative fractional power of ln Q2, so that asymptotics sets in
only very slowly. The key observation in our evaluation of the Cottingham formula is that the spin
2 contributions to T1 and T2 are the same – apart from the sign and a factor of 2. In the amplitude
¯T(ν, q2) = T1(ν, q2) + 1
2T2(ν, q2) ,
(4)
the leading short distance singularities of spin 2 drop out. Accordingly, this amplitude approaches
asymptotics much more rapidly than the individual terms. The advantage of replacing T1 with ¯T
also shows up in the asymptotic behaviour of the integrand in (3): the divergence stems from the
ﬁrst term in the decomposition φ = 3Q2 ¯T −1
2(Q2 −4Q2
4)T2. The angular integration suppresses
the second when Q2 →∞.
Dispersion relations. The amplitudes ¯T(ν, −Q2) and T2(ν, −Q2) obey ﬁxed-Q2 dispersion rela-
tions in the variable ν. The imaginary parts are determined by the structure functions:
Im ¯T = π ¯F/2xQ2 ,
ImT2 = π2m2xF2/Q4 ,
¯F = FL + 2m2x2F2/Q2 ,
(5)
with x = Q2/2mν and FL ≡F2 −2xF1. Regge asymptotics implies that T2 obeys an unsubtracted
dispersion relation, while ¯T requires a subtraction:
¯T(ν, −Q2) = ¯T el(ν, −Q2) + ¯S (−Q2) + (Q2 + 4ν2)
Z xth
0
dx
m2 ¯F(x, Q2)
(Q2 + m2x2)(Q4 −4m2x2ν2 −iǫ) ,
T2(ν, −Q2) = T el
2 (ν, −Q2) +
Z xth
0
dx
4m2F2(x, Q2)
Q4 −4m2x2ν2 −iǫ .
(6)
The elastic parts, ¯T el and T el
2 , are unambiguously determined by the nucleon form factors [6, 13,
15]. In the dispersion integrals, we have replaced the variable of integration with ν′ = Q2/(2mx).
The upper limit represents the boundary of the inelastic region, xth = Q2/(Q2 + 2mMπ + M2
π).
Note that we are not subtracting the dispersion integral for ¯T at ν = 0, but at ν =
i
2Q. This
simpliﬁes the analysis further, as it implies that, for ν = iQ4, the subtracted integral picks up the
factor (Q2 −4Q2
4), so that the angular average suppresses that part as well.
Renormalization. In the framework of QCD+QED, the mass of a particle is determined by
the bare parameters that occur in the Lagrangian and the cutoﬀused to regularize the theory. If
the electromagnetic interaction is turned oﬀ, only the QCD coupling constant, the quark masses
and the cutoﬀare relevant. To order e2, the e.m. interaction changes the mass not only by the
regularized version of equation (3), but in addition by the contribution ∆mΛ, which arises from the
change in the bare parameters needed for the mass of the particle to stay ﬁnite when the cutoﬀis
removed: the bare quantities depend on the cutoﬀas well as on e. The e.m. contribution to the
mass is given by
mQED = lim
Λ→∞
{mΛ
γ + ∆mΛ} .
(7)
Decomposition of the Cottingham formula. With our decomposition of the Compton ampli-
tude, the renormalized Cottingham formula consists of four parts [16]:
mQED = mel + m ¯F + mF2 + m ¯S .
(8)
3
While the ﬁrst term collects the elastic contributions, the second and third ones represent the
contributions from the integrals occurring in the dispersion relations for ¯T and T2. In the ﬁrst three
parts, the limit Λ →∞can be taken – the explicit expressions involve integrals over the elastic
form factors and structure functions of the nucleon [16]. The divergence resides in the fourth term,
which contains the contributions from subtraction function and renormalization,
m ¯S = lim
Λ→∞
N
Z Λ2
0
dQ2Q2 ¯S (−Q2) + ∆mΛ
,
(9)
where the constant N stands for 3αem/8πm.
Asymptotic behaviour of the subtraction function. The operator product expansion implies that
¯S falls oﬀin proportion to 1/Q4 when Q2 becomes large , while ∆mΛ grows logarithmically with
Λ. For m ¯S to stay ﬁnite, the leading contributions must match:
¯S (−Q2) →C
Q4 ,
∆mΛ →−NC ln Λ2
µ2 .
(10)
The constant C is related to the matrix elements of the lowest dimensional operators of spin 0.
In the following, we consider the diﬀerence between proton and neutron, without explicitly
indicating this in the notation: we write ¯T for ¯T p−n and likewise for ¯S , C, ¯F, T2, . . . In the proton-
neutron mass diﬀerence, we work to ﬁrst order in the isospin breaking parameters mu −md and e2
and neglect contributions of O[e2(mu −md)]. The constant C can then be expressed in terms of the
proton matrix elements of ¯uu −¯dd:
C = 4mu −md
9
⟨p|¯uu −¯dd|p⟩.
(11)
The same matrix element also determines the leading contribution to the QCD part of the mass
diﬀerence [24]:
mQCD = mu −md
2m
⟨p|¯uu −¯dd|p⟩{1 + O(mu −md)} .
(12)
The crude estimate mQCD ≈−2 MeV and the known quark mass ratios imply that C is tiny: with the
lattice result ms/mud = 27.23(10) [25] and the value of the ratio Q ≡
q
(m2s −m2
ud)/(m2
d −m2u) =
22.1(7) extracted from η-decay [26], we obtain C ≈6 · 10−4 GeV2. The approximate chiral sym-
metry of the Standard Model very strongly suppresses the asymptotic behaviour of ¯S .
The expression (11) for the constant C receives corrections from higher orders of the perturba-
tion series. These imply that the Cottingham formula contains subleading divergences proportional
to ln ln Λ – for details, we refer to [16]. Since chiral symmetry suppresses the entire contribution
from the region where perturbation theory applies, the corresponding eﬀects in the renormalized
mass diﬀerence are tiny and can be neglected. Setting ¯µ ≡exp(−1
2)µ, the expression for ∆mΛ in
(10) diﬀers from −NC
R Λ2
0
dQ2Q2/(¯µ2 + Q2)2 only by terms of order µ2/Λ2. The contribution to
mQED that arises from the subtraction function can thus be written in the form [16]
m ¯S = N
Z ∞
0
dQ2Q2
(
¯S (−Q2) −
C
(¯µ2 + Q2)2
)
.
(13)
4
This distinguishes our evaluation of the Cottingham formula from those in the literature [8–12],
where the integral as well as the counter term are evaluated at a ﬁnite value of the cutoﬀaround
Λ2 ≈2 GeV2. This would be legitimate if asymptotics were reached at such a low scale, but for
the subtraction function used in these references, that is not the case.
Role of spin 2 operators: ¯S versus S1. Traditionally, the subtraction function is identiﬁed
with a multiple of S1(q2) ≡T1(0, q2). Asymptotically, Q4S1 approaches the same constant C as
Q4 ¯S , but this happens much more slowly: in contrast to ¯S , the function S1 does pick up spin 2
contributions [21] and these are not proportional to the lightest quark masses. This implies that,
in the pre-asymptotic region, the two subtraction functions behave quite diﬀerently. In S1, it takes
extremely large values of Q2 for the spin 0 term to ﬁnally win over those of spin 2. When working
with a low cutoﬀ, this aﬀects the result for the mass diﬀerence quite substantially – see below.
In contrast to the mass itself, mQED depends on the renormalization scale µ: the splitting into
a contribution from QCD and one from QED is a matter of convention. In the decomposition
(8), the parameter µ resides in m ¯S and enters through the term ∆mΛ in (10). The above estimate
for the size of the constant C shows, however, that the sensitivity of m ¯S to µ is extremely weak:
increasing the scale by a factor of 2 increases the value of mQED by about 1 keV. For deﬁniteness,
we set µ = 2 GeV.
Reggeon dominance. The behaviour of the Compton amplitude in the limit q = λ ¯q, λ →∞is
controlled by the operator product expansion, which implies that both ¯T and T2 tend to zero in this
limit. The gluons as well as the quarks reggeize, however [27–32]: in the limit where ν becomes
large while q2 is kept ﬁxed, only T2 disappears, ¯T diverges.
In the Compton amplitudes of proton and neutron, the leading terms stem from singlet con-
tributions due to Pomeron exchange, but in the diﬀerence between the two, these drop out: the
dominating contributions to ¯T stem from the exchange of the leading Reggeon with IC = 1+,
which we refer to as the a2. It generates a Regge pole in the angular momentum plane which
moves along the trajectory α(t). In the forward direction, only the value at t = 0 matters: at ﬁxed
q2, the contribution from the a2 grows with the power να:
¯T R(ν, q2) = −π β(q2)
sin πα {(−s)α + (−u)α} ,
(14)
where α stands for α(0) and the variables s = m2 + 2mν + q2, u = m2 −2mν + q2 represent
the square of the centre of mass energy in the s- and u-channels, respectively. The value of α is
experimentally well determined from the high energy behaviour of hadronic cross sections and is
in the vicinity of α ≈0.55 – the uncertainties in α are too small to aﬀect our results.
Reggeization implies that the dispersion relation for ¯T requires a subtraction. We assume that
the Reggeons fully determine the asymptotic behaviour [4, 6, 13],
lim
ν→∞( ¯T −¯T
R) = 0 ,
(15)
and that the remainder disappears suﬃciently fast for the diﬀerence ¯T −¯T R to obey an unsubtracted
dispersion relation. We refer to this assumption as Reggeon dominance.
A nonzero limiting value in (15) would represent a ﬁxed pole in ¯T at α = 0. We do not know of
a physical phenomenon that could produce such a term – neither causality, nor the short-distance
5
singularities, nor the Reggeons generate terms of this sort. The presence of a ﬁxed pole would
mean that the high energy behaviour of the Compton amplitude is not understood.
For T2, the contribution from the Reggeons tends to zero in proportion to να−2. The generally
accepted assumption that this amplitude obeys an unsubtracted dispersion relation immediately
implies that it also obeys the Reggeon dominance condition (15). Note, however, that the expan-
sion of the dispersion integral for T2 in inverse powers of ν contains a term proportional to 1/ν2.
As pointed out by Damashek and Gilman [33] and, independently by Dominguez et al. [34], this
term corresponds to a ﬁxed pole in T2, at α = 0 (there is an analogous term also in ¯T, but it
represents a ﬁxed pole with α = −2 and is at most of academic interest).
Sum rule. Elitzur and Harari [4] pointed out that if the exchange of Reggeons correctly de-
scribes the asymptotic behaviour in the limit ν →∞at ﬁxed q2, then the subtraction function
obeys a sum rule which fully determines it through the cross section of lepton-nucleon scattering.
The sum rule relevant for our decomposition of the Compton amplitude exclusively involves the
structure function ¯F. At small values of x, this quantity is dominated by Reggeon exchange:
¯FR = b(Q2)x1−α ,
b(Q2) = 2Q2(α+1)β(−Q2) .
(16)
In the diﬀerence ¯F −¯FR, the leading term cancels out. As demonstrated in [16], the sum rule for
¯S can be brought to the form:
Q2 ¯S (−Q2) =
Z xth
0
dx
¯F(x, Q2) −¯FR(x, Q2)
x2
−b(Q2)
α xα
th
−
Z xth
0
dx m2 ¯F(x, Q2)
Q2 + m2x2 .
(17)
In [6], the violations of Bjorken scaling were ignored: it was assumed that for Q2 →∞, the
structure function ¯F tends to (2xH1 + F2)x2m2/Q2, where H1 and F2 only depend on x. One
readily checks that the sum rule (17) then indeed reduces to the relation between the operator
matrix element C and the structure functions given in (5.2), (5.3), (13.14) of [6]. Scaling would
imply that the last term on the r.h.s. of (17) tends to zero ∝1/Q4. The scaling violations merely
make it disappear less rapidly, in proportion to 1/Q2/(ln Q2)1+d2 with d2 > 0 [16].
Elastic contributions.
In recent years, the precision to which the elastic form factors are known has increased signif-
icantly [35–38]. The results obtained with the three parametrizations of [35–37] are in the range
mel = 0.75 ± 0.02 MeV .
(18)
Note that the amplitudes used in the literature often have kinematic zeros – this can make
it diﬃcult not only to sort out the asymptotic behaviour, but also to identify the elastic part of
the dispersive representation (“Born term”) with the contribution generated by the one-particle
intermediate state [13, 15]. In [12], for instance, it is assumed that the amplitude ˆT = q2T1 + ν2T2
satisﬁes the asymptotic condition (15). That assumption, however, requires q2T1 to contain a ﬁxed
pole which compensates the one in ν2T2 and hence violates Reggeon dominance.
Structure functions, parton distributions. For the numerical evaluation of the dispersion inte-
grals and of the sum rule for the subtraction function, we need a representation for the diﬀerence
6
between the structure functions of proton and neutron, and not only for the relatively well explored
quantity F2, but also for the longitudinal component FL, which is known less well. In the reso-
nance region (W < 3), we make use of the parametrizations of the structure functions in [39–43].
For W > 3 and low photon virtualities (Q2 < 1), we invoke the Regge representation of Alwall
and Ingelman (AI) [44].
At higher values of Q2, the DGLAP equations [45–47] for the parton distribution functions
(PDFs) provide a strong constraint for the analysis of the data: at leading order in αs, these equa-
tions imply that FL is given by an integral over F2. A vast amount of PDFs is available [48, 49] and
APFEL Web [50, 51] provides a ﬂexible, user-friendly tool for the evaluation of the corresponding
structure functions. Since the quark masses mu and md are tiny, the u- and d-distributions in the
neutron must be very close to the d- and u-distributions in the proton, respectively. As empha-
sized e.g.in [52], this ensures that the u- and d-distributions can separately be determined by using
neutral and charged current data on the proton – scattering on deuterons or heavier nuclei is not
needed to sort out the diﬀerence between the u- and d-distributions of the proton.
As mentioned above, the behaviour in the Regge region (x small) is dominated by the singlet
part of the distributions. This implies that the u- and d-distributions must approach one another
when x →0. While the available data strongly constrain the singlet part at small x, the non-singlet
PDFs are much less well determined. The same applies to the non-singlet structure function ¯F
which plays a central role in our work.
Since reggeization involves sums to all orders of perturbation theory, it is not a simple matter
to analyze the behaviour at small x in the framework of the DGLAP equations (for a review of
the problems encountered in this endeavour, we refer to [53]). In particular, the requirement that
the u- and d-distributions must approach one another in the Regge limit and that their diﬀerence
yields a contribution to ¯F that falls oﬀwith b(Q2)x1−α, α ≈0.55 imposes nontrivial theoretical
constraints. A coherent parametrization of the PDFs that is consistent not only with the data, but
also with these constraints, yet needs to be found.
In our calculation, we rely on the solutions of the DGLAP equations constructed by Alekhin,
Bl¨umlein and Moch (ABM) [52, 54, 55] in the region x > 0.01. At smaller values of x, we assume
that ¯F is dominated by the Reggeon a2, not only at small photon virtualities, but also at higher
values of Q2. We determine the residue b(Q2) by smoothly matching the two parametrizations
around x = 0.01. In the region W > 3, Q2 > 1, we estimate the uncertainty in our representation
for the structure functions ¯F p−n and F p−n
2
at 30%. For details, we refer to [16].
Inelastic contributions. The most striking aspect of our numerical result is that the two terms
m ¯F and mF2 turn out to be tiny: m ¯F + mF2 = −0.004(1) MeV. As discussed above, the angular
integration suppresses the integrands of these quantities at large values of Q2, but the numerical
result shows that the suppression is very eﬃcient also in the low energy region. We conclude
that – in our decomposition of the Compton amplitude – only the elastic contribution mel and
the term m ¯S from the subtraction function play a signiﬁcant role. Note that this statement holds
independently of the assumptions used to determine the subtraction function. Since the various
attempts at evaluating the Cottingham formula arrive at very similar values for the elastic part, the
discrepancies in the results for the mass diﬀerence mainly come from the term m ¯S, i.e. from the
fact that the parametrizations used for the Compton amplitude yield diﬀerent representations for
7
the subtraction function ¯S .
Contribution from the subtraction function. It is straightforward to evaluate the sum rule for ¯S
with the two representations of ¯F(x, Q2) and b(Q2) we are using below and above Q2 = 1 GeV2,
respectively and to calculate the corresponding contribution to m ¯S with (13). Isospin conservation
prevents the most prominent feature in the low energy region, the ∆(1232), to make a signiﬁcant
contribution. Moreover, the regions below and above a centre of mass energy of 3 GeV contribute
with opposite sign – within errors, they cancel: m ¯S(Q2 < 1 GeV2) = −0.034(68) MeV. Note that
the error is twice as large as the central value. It is dominated by the uncertainties in the resonance
region and is of systematic nature, as it stems from the simpliﬁcation used in the data analysis
of Bosted and Christy [42, 43]: the ratio R = σL/σT is assumed to be the same for proton and
neutron. In the region where the Pomeron dominates, this holds to good accuracy, but we need the
diﬀerence between the two, where Pomeron exchange drops out.
At Q2 = 1 GeV2, where the representations AI and ABM meet, the results for the contributions
to ¯S from W > 3 GeV agree within errors: the two entirely diﬀerent sources match, both in sign
and in size. In order to interpolate between the values of Q2 where the ABM results provide
signiﬁcant information and the region where asymptotics sets in, we make use of the Generalized
Vector Dominance Model of Sakurai and Schildknecht [56], parametrizing the subtraction function
in terms of the contributions from ρ, ω and φ. In the diﬀerence between proton and neutron, only
the oﬀ-diagonal terms survive:
¯S VMD(−Q2) =
1
m2ρ + Q2

cω
m2ω + Q2 +
cφ
m2
φ + Q2
.
(19)
The asymptotic condition (10) requires the two terms in the bracket to nearly cancel: cω + cφ = C.
This leaves a single parameter free, say cω. Fitting the parametrization in the range between 2 and
3.5 GeV2, we obtain cω = −0.74(49) GeV2. We have checked that the outcome for m ¯S is neither
sensitive to the speciﬁc form of the interpolation nor to the range used in the ﬁt. Numerically, this
yields m ¯S(Q2 > 1 GeV2) = −0.13(9) MeV. Together with the contributions from low virtualities,
this yields
m ¯S = −0.17(16) MeV .
(20)
Because asymptotic freedom ﬁxes the asymptotic behaviour of the subtraction function, the
parametrization obtained within Generalized Vector Meson Dominance contains a single free pa-
rameter. Instead of ﬁxing it to the results obtained with the ABM solution of the DGLAP equa-
tions, we can dismiss the experimental information available for W > 3, Q2 > 1 altogether
and determine the free parameter with a ﬁt to the results obtained for Q2 < 1.
This yields
m ¯S = −0.12(21) MeV: the central value stays well within the estimated uncertainty and the er-
ror only increases by about 30%. This indicates that our result is not sensitive to the input used in
the region where the non-singlet contributions to the structure functions are not yet known well.
Numerical result. Collecting the various contributions and using the experimental value of the
proton-neutron mass diﬀerence, the parts due to the e.m. interaction and to the diﬀerence between
mu and md become
mQED = 0.58 ± 0.16 MeV , mQCD = −1.87 ∓0.16 MeV .
(21)
8
The result for mQCD yields a more precise estimate for the leading Wilson coeﬃcient: C = 5.7(1.1)·
10−4 GeV2, but the corresponding shift in our results is negligibly small.
The conclusions reached in [6] are thus conﬁrmed: mQED is dominated by the elastic contri-
bution. The uncertainty in the old result, mQED = 0.7(3) MeV, is reduced by about a factor of
two.
It is not diﬃcult to understand why the inelastic contributions are so small: (a) the angular inte-
gration suppresses the contributions from the dispersion integrals, (b) if Q2 is large, the subtraction
functions of proton and neutron are nearly the same – in the chiral limit, there is no diﬀerence, (c)
in the region where Reggeon exchange dominates, the leading term, the Pomeron, is the same, (d)
isospin symmetry ensures that the most important resonance, the ∆(1232), contributes equally to
proton and neutron and (e) the elastic contributions also dominate the chiral perturbation series of
the Compton amplitude: the leading terms exclusively contribute to the elastic part - inelastic pro-
cesses merely generate higher order corrections (for a recent analysis of the subtraction function
in χPT, we refer to [57]).
Comparison with lattice results. The determination of mQED on a lattice is a very demanding
goal. While the numbers in [58] cluster around mQED ≈0.7 MeV, in agreement with our result,
the values 1.00(7)(14) MeV [59], 1.03(17) [60] and 1.53(25)(50) MeV [61] are higher than ours.
Adding statistical and systematic errors in quadrature, the various lattice results diﬀer from the
outcome of our calculation by less than two standard deviations. In the framework we are relying
on, values like mQED = 1 MeV or even higher require sizeable positive contributions from m ¯S – this
is not compatible with Reggeon dominance.
Comparison with other dispersive calculations. The main diﬀerence between our analysis
and the work reported in [8–11] is that, there, the subtraction function is not calculated, but
parametrized with an ansatz in terms of its value at Q2 = 0 (taken from experiment) and a scale
m0 that speciﬁes the momentum dependence. Moreover, in these models, the parametrization is
applied to S1 rather than to ¯S . As discussed above, the asymptotic behaviour of S1 picks up con-
tributions from operators with spin 2, which fall oﬀonly extremely slowly. Since chiral symmetry
suppresses the coeﬃcient C of the leading asymptotic term, it starts dominating S1 only if Q2
becomes very large. This implies that the parametrization used in these models does not behave
properly in the pre-asymptotic region, which does make a signiﬁcant contribution to m ¯S.
The mismatch with the asymptotics disappears if the ansatz in [9] is assumed to be valid for
¯S rather than S1. The central value obtained for mQED then drops to about 0.7 MeV, in agreement
with what we ﬁnd. The uncertainties in the result for mQED, however, are much larger than ours,
not only because the experimental values of the magnetic polarizabilities of proton and neutron,
which play a key role in those models, are subject to large errors, but also because the result is
quite sensitive to the shape of the parametrization used for low values of Q2.
Summary. We have applied the Reggeon dominance hypothesis to the electromagnetic part of
the proton-neutron mass diﬀerence. The uncertainty in our ﬁnal result, mQED = 0.58 ± 0.16 MeV,
stems from a careful estimate of the errors coming from the diﬀerent experimental data sets used in
the calculations. While this conﬁrms the old result [6], which also relies on Reggeon dominance,
recent evaluations of the Cottingham formula [8–12] yield central values around 1 MeV or even
higher. The diﬀerence stems from the short distance singularities associated with operators of spin
9
