---
doc_id: arxiv-hep-lat-0003021v3
doc_title: "Low-lying Eigenvalues of the QCD Dirac Operator at Finite Temperature"
section_id: sec-001-introduction
section_title: "Introduction"
section_number: null
pages: 2-19
source_pdf: 0003021v3.pdf
source_sha256: b35dfd9ab88b71d8
doc_brief: "Low-lying Eigenvalues of the QCD Dirac Operator at Finite Temperature — We compute the low-lying spectrum of the staggered Dirac operator above and below the ﬁnite temperature phase transition in"
---
The correlations of Dirac operator eigenvalues in QCD and related theories have been shown to have a
fascinating relation to Random Matrix Theory. There are two very diﬀerent domains of interest here.
One is the so-called “bulk” of the eigenvalue spectrum of the Dirac operator, far from both the infrared
and the ultraviolet ends. The other is the so-called “hard edge” at λ ∼0, i.e. the infrared end of the
spectrum in theories with spontaneous breaking of chiral symmetry. The relevance of Random Matrix
Theory in describing eigenvalue correlations of the Dirac operator in the bulk of the spectrum was ﬁrst
demonstrated by Halasz and Verbaarschot [1], and it has since been conﬁrmed by numerous lattice
gauge theory studies [2]. From a theoretical point of view, these results in the bulk of the spectrum
remain to be better understood. In the other case, near λ ∼0, the connection between universal
Random Matrix Theory results and the QCD Dirac operator spectrum [3, 4, 5] is by now ﬁrmly
established, and has also been extensively checked in lattice gauge theory simulations [6]. Already
in the original work of Shuryak and Verbaarschot [3] it was shown that the pertinent chiral Random
Matrix Theory partition function coincides exactly with the eﬀective ﬁeld theory partition function in
the relevant microscopic limit. More recently an explicit relationship between the universal Random
Matrix Theory eigenvalue distributions and those of the QCD Dirac operator has been established
[7, 8], the precise link being the partially quenched chiral condensate [8, 9]. In this domain Random
Matrix Theory is an intriguing alternative description of exactly the same phenomena that can be
derived from the eﬀective QCD partition function in the large-volume limit where V ≪1/m4
π [10].
There exists also an interesting physical situation that forces us to reconsider the two diﬀerent do-
mains of the Dirac operator spectrum simultaneously. This is near the ﬁnite-temperature chiral phase
transition, where the analytical connection between the eﬀective QCD partition function and Ran-
dom Matrix Theory breaks down even for the part of the spectrum that is close to λ = 0. This
situation is readily confronted in lattice gauge theory. Indeed, it is for staggered fermions even rig-
orously proven [11], that chiral symmetry is restored at high temperature. The low-lying spectrum
of the Dirac operator must therefore be quite diﬀerent in the high temperature phase as compared
with zero temperature. In particular, the absence of chiral symmetry breaking implies, through the
Banks-Casher relation,
⟨¯ψψ⟩= πρ(0) ,
(1)
that the density of eigenvalues at zero vanishes. This could happen either just at that point of λ = 0
(as, for example, in the free theory where ρ(λ) ∼λ3), or the spectrum could develop a gap. The chiral
phase transition occurs at the temperature Tc where the density of Dirac operator eigenvalues just
reaches zero at λ = 0. If the transition is continuous, this will happen smoothly as the temperature
T is increased towards Tc. In such a case, an important question to settle is the precise power-law
behavior of the spectral density of the Dirac operator right at T = Tc, because this can be related to
the critical exponents of the phase transition [12]. The same chiral Random Matrix Theory that yields
universal microscopic spectral correlators which exactly coincide with those of the Dirac operator at
T = 0 can be tuned in such a way as to just reach (multi-critical) points where [13]
ρ(λ) ∼λ2k
(2)
near λ = 0. Here k is an integer labeling the multi-criticality. At such points universality of microscopic
spectral correlators still holds in the Random Matrix Theory context, but there is no justiﬁcation for
assuming that these results are relevant for the Dirac operator spectrum at T = Tc.1 There is also a
1In particular, this behavior is only compatible with a continuous phase transition.
But at a more fundamental
level, there is simply no longer any relation between the chiral Random Matrix Theory ensemble and the eﬀective QCD
partition function for temperatures T that do not satisfy T ≪ΛQCD.
1
schematic Random Matrix model for the ﬁnite-temperature behavior of the Dirac operator spectrum
[14]. It gives a diﬀerent behavior at T = Tc: ρ(λ) ∼λ1/3. Also here there is no physical justiﬁcation for
using it in connection with the Dirac operator spectrum at ﬁnite temperature, but it is an interesting
model that depends on just one deterministic external parameter, and we shall therefore return to it
below.
Suppose, for a moment, that the Dirac spectrum actually develops a gap around λ = 0 above Tc.
In Random Matrix Theory the end of a spectrum around such a gap is referred to as a “soft edge”.
Generally, the (macroscopic) density of eigenvalues near a soft edge behaves as (for λ > λ0) [15]:
ρ(λ) ∝(λ −λ0)2m+1/2
(3)
with λ0 being the location of the edge. Here m is an integer that labels universality classes classiﬁed
by their Random Matrix Theory potentials (m parameters in the potentials must be tuned in order to
reach each class). Thus the generic behavior, without any ﬁne tuning, corresponds to m = 0, which
gives a square root approach to the soft edge:
ρ(λ) ∝(λ −λ0)1/2
(4)
Random Matrix Theory actually gives a more detailed, microscopic, description. This arises from a
blowing-up of the eigenvalue density function around the soft edge λ0 with a rescaling according to the
macroscopic behavior (3). For example, for the generic m = 0 universality class, the corresponding
microscopic eigenvalue density is [16]
ρ(λ) ∝X[Ai(−X)]2 + [Ai′(−X)]2 ,
(5)
where X ∝(λ −λ0)N 2/3 and Ai(x) is the standard Airy function.
Here N denotes the size of
the matrix, and the rescaling by N 2/3 is required in order to spread out the increasing number of
eigenvalues to obtain one well-deﬁned limiting function. From the known asymptotic behavior of the
Airy functions one ﬁnds:
ρ(λ) ∼
( √
X
π + O

1
X

for X →∞
17
96π|X|−1/2 exp(−4|X|3/2/3)
for X →−∞
(6)
Thus, at the microscopic level the spectrum is not cut oﬀsharply at λ0, but has an exponentially
suppressed tail beyond. Further, the square root behavior of the eigenvalue density is modulated by
wiggles corresponding to the distribution of particular eigenvalues (smallest, second, third, etc.). (See,
for example, Fig. 9.)
Until a few months ago, there existed only one low-statistics investigation of the low-lying Dirac
eigenvalue spectrum for staggered fermions in the high temperature phase [17]. It did not unequivocally
establish the existence of a gap. For example, some low eigenvalues were found. However, they could
possibly be attributed to “would-be zero modes” from global gauge ﬁeld topology, shifted away from
zero by the explicit chiral symmetry breaking of staggered fermions at ﬁnite lattice spacing [18]. This
is a general problem with staggered fermions that also we must face here: at ﬁnite lattice spacing,
the index theorem is not valid for staggered fermions, and gauge ﬁeld topology (whichever way one
deﬁnes it on a discrete lattice) does not give rise to exact zero modes of the staggered Dirac operator.
At T = 0 no trace of non-trivial gauge ﬁeld topology on the lowest-lying spectrum of staggered
eigenvalues has been found [19], except in the 2-d Schwinger model at fairly small lattice spacing [20].
Finite temperature, which causes a depletion of genuine non-zero eigenvalues near λ ∼0, further
complicates this issue of a mix-up with would-be zero modes.
2
Very recently a study of just the low-lying Dirac operator eigenvalues near Tc has actually indicated
the presence of a gap at large lattice volumes [21]. Again the statistics was rather limited, and only
a small number of the lowest-lying eigenvalues could be included (varying between 8 and 10). The
present study will in many ways follow the same lines of thought as Ref. [21], but we shall have much
larger statistics, and we shall also probe some diﬀerent aspects. In particular, we are also interested
in seeing whether quenching causes a diﬀerent behavior of the smallest eigenvalues near Tc compared
with dynamical fermions.
Last year a study of low-lying eigenvalues of the overlap Dirac operator in quenched ﬁnite temperature
gauge theories appeared [22]. Overlap fermions are well suited for such an investigation since they do
not suﬀer from explicit chiral symmetry breaking even at ﬁnite lattice spacing and since they have exact
zero modes in topologically non-trivial gauge ﬁelds. Ref. [22] found that eﬀects of topology persisted
in the high temperature phase, although strongly suppressed compared to the low temperature phase.
More interestingly, an accumulation of low eigenvalues with an apparently ﬁnite density in the inﬁnite-
volume limit was found very near λ ∼0 even above the (quenched) phase transition temperature Tc.
The statistical properties of the smallest group of eigenvalues were consistent with them being due
to a dilute gas of instantons and anti-instantons [22]. These results have led to the speculation that
chiral symmetry might remain broken even in the high temperature phase of quenched QCD with
overlap fermions.
In this paper we describe high statistics investigations of the low-lying eigenvalue spectrum of the
staggered Dirac operator for SU(3) gauge group at ﬁnite temperature. We do this for both quenched
(section 2) and dynamical QCD with four ﬂavors of staggered fermions (section 3). The interest in
the quenched case lies primarily in checking whether also staggered fermions, although insensitive to
topology at the gauge couplings we can investigate here, show signs of unusual behavior of the smallest
Dirac eigenvalues above Tc (as was the case for overlap fermions [22]). Both quenched and unquenched
simulations give rise to Dirac operator spectra that can be compared with Random Matrix Theory. In
particular, if the Dirac operator spectrum exhibits a gap, is it of the soft-edge kind of Random Matrix
Theory? Are there indications that Random Matrix Theory provides a more accurate description of
the Dirac operator spectrum as the three-volume is increased? We shall try to answer these questions
in what follows.
2
Quenched QCD at high temperature
For our quenched ﬁnite temperature Monte Carlo simulations we have used lattices with temporal
extent Nt = 4 and up to three spatial volumes: 83, 123 and 163. For Nt = 4 the deconﬁnement phase
transition for SU(3) pure gauge theory with Wilson action has been very accurately determined,
occurring at lattice gauge coupling βc = 5.6925(2) [23]. It has for long been assumed that the chiral
phase transition of the quenched theory occurs at exactly this deconﬁnement phase transition point
of the pure gauge theory, but this has recently been challenged [22].
We now give some technical details of our simulations. The gauge ﬁeld conﬁgurations were generated
with a mixture of overrelaxation and heat bath updates, and were analyzed after every 20-th heat
bath sweep. On each conﬁguration we computed the 50 lowest-lying eigenvalues, and in some cases
even more, using the variational Ritz functional method [24]. Many ensembles consisted of several
thousand conﬁgurations. Gauge coupling, lattice size and statistics of our ensembles is summarized
in Table 1.
3
V
β
#conﬁgurations
83 × 4
5.5
5931
83 × 4
5.66
5544
83 × 4
5.695
1769
83 × 4
5.71
1145
83 × 4
5.72
1426
83 × 4
5.73
2021
83 × 4
5.75
7029
123 × 4
5.75
1933
163 × 4
5.75
692
83 × 4
5.8
5335
83 × 4
5.85
6149
83 × 4
5.9
4263
123 × 4
5.9
1755
163 × 4
5.9
824
Table 1: Details of our quenched ensembles.
As is well-known, the staggered Dirac operator
/
Dx,y
=
1
2
X
µ
ηµ(x)

Uµ(x)δx+µ,y −U †
µ(y)δx,y+µ

≡
/
De,o + /
Do,e
(7)
is anti-hermitian, with purely imaginary eigenvalues iλ that come in pairs of opposite sign. In eq. (7)
ηµ(x) = (−1)
P
ν<µ xν
(8)
are the usual phase factors for staggered fermions. Denoting
ǫ(x) = (−1)
P
ν xν ,
(9)
we have also explicitly shown how /
D connects even sites, i.e. those with ǫ(x) = +1, with odd sites, those
with ǫ(x) = −1, and vice versa. This means that the operator −/
D2 is hermitian and positive semi-
deﬁnite. The sign function ǫ(x) deﬁned above plays the role of γ5 in the continuum: it anticommutes
with /
D : { /
D, ǫ} = 0. As −/
D2 does not mix between even and odd lattice sites, we need only compute
the eigenvalues, on, say, the even sublattice. One easily sees that if ψe is a normalized eigenvector of
−/
D2 with eigenvalue λ2, then ψo ≡1
λ /
Do,eψe is a normalized eigenvector of −/
D2 with eigenvalue λ2,
and non-zero only on odd sites. Moreover, as we will never encounter exact zero modes on genuine
quantum conﬁgurations, there is no diﬃculty with the above deﬁnition of ψo. We of course make use
of these properties, and hence compute only the (positive) eigenvalues of −/
D2 restricted to the even
sublattice, and then take the (positive) square root. All eigenvalues to be shown in the following thus
have an equal number of negative companions, of the exact same magnitude.
The spectral density of the Dirac operator is given by
ρ(λ) ≡
1
V ⟨
X
n
δ(λ −λn)⟩,
(10)
4
0.0
0.1
0.2
0.3
λ
0.0
0.1
0.2
0.3
ρ(λ)
β=5.5
β=5.66
β=5.71
β=5.75
β=5.9
Figure 1: The measured distribution of the 50 lowest eigenvalues in quenched QCD at ﬁnite tempera-
ture for several β’s on 83 ×4 lattices. One sees a clear suppression of the spectral density at the origin
ρ(0) as the temperature (coupling) is increased, indicating a diminishing chiral condensate according
to the Banks-Casher formula. For large temperatures the spectrum is heavily suppressed near the
origin, although in this quenched case a small tail always seems to extend towards λ = 0 (see below).
5
0.0
0.1
0.2
0.3
λ
0.0
0.1
0.2
ρ(λ)
0.05
0.1
2e−03
4e−03
16  x4
3
12  x4
8  x4
3
3
Figure 2: The density of the smallest eigenvalues in the high temperature phase of quenched QCD, at
β = 5.9, for spatial volumes 83, 123 and 163. In the two large volumes we measured 100 eigenvalues
and only 50 in the small volume. Since the eigenvalue density increases with increasing volume, the
distributions are correspondingly cut oﬀat smaller λ. There is no observable change in the eigenvalue
density as the three-volume is increased. This holds even at the very small tail extending towards
λ = 0, as shown in the magniﬁed plot inserted.
and it is readily computed numerically from our Monte Carlo simulations by a binning of the measured
eigenvalues per conﬁguration at convenient small intervals.
In Fig. 1 we show the density of low lying eigenvalues on 83 × 4 lattices for several β values between
5.5 (in the conﬁned phase) to 5.9 (in the deconﬁned phase). In each case we computed the 50 lowest
positive eigenvalues iλ of the staggered Dirac operator. The plots are normalized by the following
condition,
R ∞
0 ρ(λ)dλ = #eigenvalues/V . In the conﬁned phase it is quite evident that the density at
zero would be non-zero in the thermodynamic limit. As the temperature is increased, the density at
zero decreases. There is a qualitative change of the eigenvalue density once the temperature is increased
above Tc. Beyond the ﬁrst few eigenvalues the eigenvalue density assumes a shape compatible with
a square root behavior (4). However, a sizable tail, decreasing with increasing temperature, of small
eigenvalues persists, which seems to extend all the way down to zero.
In Fig. 2 we compare the eigenvalue density in the high temperature phase, at β = 5.9, for several
spatial volumes. As can be seen the eigenvalue density is volume independent to a surprising degree.
In particular, the tail of small eigenvalues is seen to be volume independent and appears to persist in
the thermodynamic limit. We note that the tail is much larger than would be compatible with the
exponential tail from the Airy function behavior of random matrix theory at a soft edge eq. (6) (see
Fig. 9 in section 3 below for an example).
It is tempting to speculate that the tail seen here in the quenched case with staggered fermions is a
6
0
1
2
3
0
0.2
0.4
0.6
0.8
1
P(s)
0
1
2
3
0
0.2
0.4
0.6
0.8
1
0
1
2
3
s
0
1
2
3
0
1
2
3
4
0
1
2
3
4
s1
s2
s3
s4
s5
s6
Figure 3: Distributions of the unfolded level spacings between the ﬁrst few eigenvalues for β = 5.75
on an 83 × 4 lattice, compared to the Wigner surmise. The agreement with Random Matrix Theory
is clear once we go beyond the ﬁrst few eigenvalues. However, there is not very good agreement for
the ﬁrst 2-3 eigenvalues at this volume.
reﬂection of the accumulation of small eigenvalues seen with overlap fermions in [22] and attributed
there to a dilute gas of instantons and anti-instantons.
In the staggered case, the explicit chiral
symmetry breaking at ﬁnite lattice spacing shifts the small modes, presumably resulting in the observed
tail.
We also looked at the unfolded level spacing between individual eigenvalues i and i + 1
si =
λi+1 −λi
⟨λi+1 −λi⟩.
(11)
In Fig. 3 the distribution of the si between eigenvalue i and i + 1, i = 1..6 is shown and compared to
the expected distribution, the Wigner surmise
P(s) = 32
π2 s2e−4
π s2 .
(12)
Evidently, the level spacings between the ﬁrst eigenvalues are not very accurately given by Random
Matrix Theory correlations. But as we move into the bulk, say for i > 5 in the case of the 83 × 4
lattice, the agreement with Random Matrix Theory becomes almost perfect. It should be stressed
here that this is a volume-dependent statement. For larger volumes one needs to go beyond more
eigenvalues starting at the soft edge before one ﬁnds good agreement. This is consistent with the fact
that there is a deﬁnite scale around the soft edge, where eigenvalue correlations are poorly described
by Random Matrix Theory. Going to larger volumes simply forces more eigenvalues into that region.
7
4.96
4.98
5.00
5.02
5.04
5.06
β
0.00
0.02
0.04
0.06
1. eigenvalue
Figure 4: The lowest eigenvalue, averaged over 5 conﬁgurations, on an 83 ×4 lattice with amq = 0.025
as a function of β. One sees a clear change in behavior around β ∼5.02, indicating the restoration of
chiral symmetry around this temperature. Just this ﬁrst Dirac operator eigenvalue can thus serve as
an excellent indicator of the chiral phase transition point.
3
QCD with four dynamical fermions at high temperature
For our dynamical simulations we chose to work with nf = 4 ﬂavors. Four is the “natural” number
of ﬂavors for staggered fermions in the continuum limit, and an eﬃcient exact simulation algorithm
can be used, the Hybrid Monte Carlo algorithm. In addition, the four ﬂavor theory is known to have
a rather strong ﬁrst order ﬁnite temperature phase transition [25]. Therefore, tunnelings into the low
temperature phase are strongly suppressed already on rather small systems and at temperatures quite
close to Tc.
We made dynamical simulations with quark masses amq = 0.1, 0.05, 0.025, 0.01 and 0.002, and for
couplings β in the high temperature phase (here a is the lattice spacing). Interestingly, the lowest
eigenvalue provides a sensitive method for determining the critical coupling βc(amq): in Fig 4 the
lowest eigenvalue on a 83 × 4 lattice with amq = 0.025 is plotted against β. β ranges from 4.96 to
5.07 in intervals of 0.002. Each point is an average over 5 conﬁgurations at that β-value. A rise is
observed between β = 5.012 and β = 5.022, which can be clearly interpreted as the chiral symmetry
restoring ﬁnite temperature phase transition. (For published values of the critical couplings βc(amq))
see Ref. [25].) The possibility of using the magnitude of the smallest Dirac operator eigenvalues as
probes for chiral symmetry restoration was suggested by Jackson and Verbaarschot [14] on the basis
of a similarly observed behavior in a Random Matrix Theory context that we will also discuss below.
Most of our analysis with dynamical fermions was performed at β = 5.2, which is above βc for all
values of mq we used. Typically, we analyzed ∼3000 conﬁgurations for each volume and mq, extracting
the 50 smallest eigenvalues. Ensemble details are summarized in Table 2. Note the large statistics
8
V
β
amq
#conﬁgurations
83 × 4
5.1
0.1
8897
83 × 4
5.1
0.025
2909
83 × 4
5.1
0.01
4050
83 × 4
5.2
0.1
4348
83 × 4
5.2
0.05
2149
83 × 4
5.2
0.025
29632
123 × 4
5.2
0.025
13929
83 × 4
5.2
0.01
4050
123 × 4
5.2
0.01
2882
83 × 4
5.2
0.008
4200
83 × 4
5.2
0.005
7948
83 × 4
5.2
0.002
6950
83 × 4
5.3
0.025
4549
83 × 4
5.4
0.025
3746
Table 2: Details of our ensembles with dynamical fermions.
gathered for β = 5.2 and amq = 0.025.
As in the quenched case we ﬁnd a small tail at the lower end of the eigenvalue distribution, reaching
towards λ = 0 from the main bulk of the distribution. This tail also appears to be volume independent
(see Fig. 6). However, in this case it is somewhat more suppressed than in the quenched case, and for
small values of the quark mass it does not extend all the way to λ = 0, see Fig. 5.
In Fig. 7 we show eigenvalue distributions measured at β = 5.2 and various amq. Note that for
larger amq, βc is also larger, which causes a shift of the whole spectrum as amq is varied. Therefore, a
direct quantitative comparison of the distributions in Fig. 7 is not straightforward. However, we note
that the distributions at amq = 0.025 and amq = 0.002 are almost on top of each other, indicating
that these distributions are very close to the amq = 0 distribution.
Furthermore, as in the quenched case described in the previous section, we ﬁnd the “macroscopic”
behavior of the eigenvalue density seemingly compatible with a square root form. By ﬁtting eq. (3) to
the bulk of the spectrum (leaving out the tail), we obtain diﬀerent powers, depending on how much
of the tail we choose to cut oﬀ. This ﬁtting has been done for V = 83 × 4 at β = 5.2 and amq = 0.025
and the resulting values can be seen in Table 3. There is a clear tendency towards a slightly higher
power (= 2m + 1/2) than the square root which would be expected from Random Matrix Theory. In
Fig. 8 we show the ﬁt with the cut at 0.1. For comparison, we include the distribution of the ﬁrst
eigenvalue in the ﬁgure. Clearly, the tail at small λ is caused by the excessive width of the distribution
of the smallest eigenvalue.
In Fig. 9 we compare the spectral density for quark mass amq = 0.025 with the prediction (5) of the
Random Matrix Theory for the density near a soft edge. In order to make the comparison possible,
we rescale the spectral density as
ρ(λ) →λ0
2

2
πλ0KV
 2
3 ρ
 
2
λ0
(λ −λ0)

2
πλ0KV
−2
3
!
(13)
where we determine λ0 and K from a ﬁt to a square root:
q
λ0
2 K
p
(λ −λ0). Here V is the lattice vol-
9
0.0
0.1
0.2
0.3
λ
0.0
0.1
0.2
0.3
ρ(λ)
0.05
0.1
2e−03
4e−03
Figure 5: Quenched spectrum of β = 5.9 and a dynamical spectrum at β = 5.4 with amq = 0.025,
both on an 83 × 4 lattice. A blowup of the y-axis near the end of the tail is also shown. There is
a much stronger suppression of small eigenvalues in the case of dynamical fermions, perhaps due to
fewer would-be zero modes in topological non-trivial gauge ﬁeld conﬁgurations.
Cut at
m
2m + 1/2
0.09
0.055 ±0.003
0.609 ±0.006
0.095
0.049 ±0.004
0.598 ±0.007
0.1
0.040 ±0.005
0.580 ±0.010
0.105
0.036 ±0.006
0.572 ±0.011
0.11
0.041 ±0.008
0.582 ±0.016
0.115
0.035 ±0.010
0.570 ±0.019
0.12
0.043 ±0.013
0.585 ±0.027
0.125
0.040 ±0.016
0.581 ±0.032
0.13
0.033 ±0.021
0.567 ±0.041
0.14
0.027 ±0.034
0.554 ±0.068
Table 3: The dependence of the ﬁtted power on the λ where the small-λ tail is cut oﬀ. The data are
from 83 × 4, β = 5.2 and amq = 0.025 lattices, using the 50 smallest eigenvalues. The ﬁts are almost
compatible with a square-root behavior of the spectrum at this soft edge, but there is a consistent
small upward shift in the exponent.
10
0.0
0.1
0.2
λ
0.0
0.1
0.2
0.3
ρ(λ)
12  x4
8  x4
3
3
Figure 6: The density of the 50 smallest eigenvalues in the high temperature phase, β = 5.2 and
amq = 0.025 for spatial volumes 83 and 123. The normalization of the distributions is as in Fig. 2. As
in the quenched simulations, we observe no signiﬁcant change in the eigenvalue spectrum at all as the
three-volume is increased.
11
0.0
0.1
0.2
λ
0.0
0.1
0.2
0.3
ρ(λ)
am=0.1
am=0.05
am=0.025
am=0.002
Figure 7:
The density of the 50 smallest eigenvalues at β
= 5.2 for quark masses amq
=
0.1, 0.05, 0.025, 0.002 on 83 × 4 lattices.
While there is some shift with decreasing quark mass for
the larger values of amq, the spectral density seems to approach a limiting function, which we can
identify as the chiral limit of the spectrum. Note that the large-mass behavior of the spectrum is al-
most identical to the quenched spectrum in this region, in agreement with the notion that on this scale
of eigenvalues the large-mass fermion has completely decoupled, and eﬀectively become quenched.
12
0.0
0.1
0.2
λ
0.0
0.1
0.2
0.3
ρ(λ)
Figure 8: Power ﬁt to the spectral density for β = 5.2 with amq = 0.025 on an 83 × 4 lattice with cut
at 0.1 (see Table 3). Also included is the distribution of the ﬁrst eigenvalue. The distribution of this
smallest eigenvalue is very diﬀerent from that demanded by the Airy-function behavior (see below).
ume. We see that the tail predicted by the Random Matrix Theory is much more strongly suppressed
than the measured distribution. Moreover, we can also observe that the density of the eigenvalues
themselves does not match: the measured distribution includes 50 eigenvalues, whereas the function
(5) has only 40 ‘wiggles’ in the λ-range of the distribution. However, if we attempt to perform the
comparison by matching the number of eigenvalues/wiggles, the overall ﬁt becomes worse. In itself,
this mismatch is not surprising, when we remember that the overall shape is not well described by a
square root behavior in the ﬁrst place (see Table 3).
In the quenched simulations we saw that correlations between the ﬁrst 5 or 6 eigenvalues were not
very accurately given by Random Matrix Theory. In Fig. 10 the distribution of si, deﬁned in eq. (11),
is shown for a dynamical simulation with β = 5.2 , amq = 0.025 on a 83 × 4 lattice. Here we see,
on the same lattice volume, a clear deviation from the Wigner surmise only for the ﬁrst two or three
spacings, s1, s2 and s3. Again, comparisons can only be made at equal volumes, as larger volumes
imply more eigenvalues in the region around the soft edge where correlations are poorly described by
Random Matrix Theory.
There is an interesting physical consequence of a genuine gap in the Dirac eigenvalue spectrum.
Consider the diﬀerence between the (π) susceptibility χP and the susceptibility of its scalar partner
(a0), which we denote by χS [26, 27]. In a manner similar to the Banks-Casher formula for the chiral
condensate one ﬁnds that this diﬀerence can be written
ω = 4m2
Z ∞
0
dλ
ρ(λ; m)
(λ2 + m2)2 ,
(14)
13
−20
0
20
40
λ
0.0
0.5
1.0
1.5
2.0
ρ(λ)
Figure 9: Comparison of the spectral density for β = 5.2, amq = 0.025 on a 83 × 4 lattice, with the
Random Matrix Theory prediction for a soft edge, as in eq. (5).
0
1
2
3
0
0.2
0.4
0.6
0.8
1
P(s)
0
1
2
3
0
0.2
0.4
0.6
0.8
1
0
1
2
3
s
0
1
2
3
0
1
2
3
4
0
1
2
3
4
s1
s2
s3
s4
s5
s6
Figure 10: Distributions of the unfolded level spacings between the ﬁrst few eigenvalues in the dynam-
ical case, compared to the Wigner surmise. As in the quenched case, we ﬁnd a small disagreement for
the ﬁrst eigenvalues. But in contrast to the quenched case the agreement sets in after almost just the
2nd eigenvalue, at the same volume.
14
where the spectral density ρ(λ; m) includes the zero modes due to topology as well. In the inﬁnite-
volume limit this contribution from exact zero modes should vanish, and we should be left with the
integral over non-zero modes. If the spectral density has a gap around the origin this means that ω
vanishes in the chiral limit. Because axial U(1) rotates χP into χS and vice versa, this would imply
a restoration of axial U(1) at these high temperatures [26, 27]. Conversely, if one believes that this
axial U(1) symmetry is not restored at high temperature, one gets constraints on the behavior of
the spectral density of the Dirac operator near the origin. For a power-law behavior near λ ∼0 a
non-vanishing ω in the inﬁnite-volume chiral limit can only be supported for ρ(λ, 0) ∼λα with α ≤1,
and in fact ω would only remain ﬁnite in that limit if α = 1.
Of course, the fact that we appear to see a gap in the eigenvalue spectrum with staggered fermions at
this particular coupling does not imply that this gap persists in physical units as we take the continuum
limit. If not, we are here studying a pure lattice artifact. The only way to test this is to study the shift
in the apparent cut-oﬀeigenvalue λ0 as we change the lattice spacing (this is, however, far beyond
what we can do at present). A very diﬀerent uncertainty comes from the fact that we are working
with fermions that are almost insensitive to topology at the couplings and volumes available to us.
This means that there are some would-be zero modes mixed up with our regular eigenvalues near the
origin. At zero temperature we found that these would-be zero modes somewhat surprisingly behaved
as the non-zero eigenvalues at realistic couplings and volumes [19]. But there is no guarantee that this
is the case at ﬁnite temperature. This means that the small tail extending to zero in our quenched
simulations, and some of the smallest eigenvalues in the simulations with dynamical fermions may be
due to these would-be zero modes. In particular, the disagreement with Airy-function behavior very
close to the soft edge may be partly due to these would-be zero modes.
4
Random Matrix Theory
We have just shown our lattice gauge theory data for the spectrum of the Dirac operator below, around,
and above Tc, and compared it with some of the analytical formulas of Random Matrix Theory in the
limit where the size of these matrices N goes to inﬁnity. It is of interest to see how a simple model of
a chiral phase transition in Random Matrix Theory behaves at ﬁnite N, as some external parameter
(mimicking temperature T) is changed. The model we shall focus on here was proposed by Jackson
and Verbaarschot in the ﬁrst of Ref. [14] and has also been studied in Ref. [28]. It is based on a
modiﬁed chiral ensemble of N × N complex matrices W, with partition function
Z =
Z
dW
Nf
Y
f=1
det(M −imf) exp
h
−NTr(WW †)
i
(15)
in a sector of topological charge zero. Here
M =
 
0
W † + T
W + T
0
!
(16)
is a 2N × 2N block hermitian matrix, and the external deterministic parameter T is playing a rˆole
reminiscent of temperature. In the normalization chosen here, a continuous “phase transition” occurs
at Tc = 1, where the spectral density ρ(λ) of the eigenvalues of the random matrices just reaches zero
[14]. For T > Tc the spectrum becomes two-banded, with a gap surrounding zero. The global shape of
ρ(λ) in this model will be very diﬀerent from the actual (macroscopic) Dirac operator spectral density.
But the interesting feature lies in having here a simple model which qualitatively seems to describe
15
0
1
2
3
0
0.1
0.2
0.3
ρ(λ)
0
0.1
0.2
0.3
0.4
0
1
2
3
λ
0
1
2
3
4
T=0
T=0.5
T=0.75
T=1
T=1.2
T=2
Figure 11: Full spectra of 200 × 200 matrices at T = 0, 0.5, 0.75, 1.0, 1.2, 2.0. In this simple model a
gap indeed develops around λ = 0 at T = 1.
some of the observed behavior of the staggered Dirac operator with Nf = 4, in particular the apparent
gap in the density for T > Tc.2
It is very simple to do quenched (i.e, Nf = 0) numerical simulations of the above Random Matrix
model, as it just corresponds to generating an ensemble of complex matrices with Gaussian weight.
Such matrices are “maximally random” in that their matrix elements are independently of Gaussian
distribution. This allows us to choose very large random matrices numerically, and then ﬁnding the
eigenvalues of the hermitian matrix M. In this way we have studied the detailed behavior of the
ﬁnite-N Random Matrix model (15) just below Tc, at Tc, and just above Tc (where the two bands
separate as the gap develops).3
We show some of our numerical results in Figs. 11 and 12.
First, in Fig. 11 we display a se-
quence of the macroscopic spectral density with increasing magnitude of the parameter T: T =
0, 0.5, 0.75, 1.0, 1.2, 2.0. The plots were made by diagonalizing 10000 200 × 200 matrices. At T = 0
this macroscopic Random Matrix Theory spectrum is just the Wigner semi-circle law (we display only
the λ > 0 part):
ρ(λ, T = 0) = 1
2π
p
4 −λ2 .
(17)
As T increases, a dip in the spectral density around λ = 0 slowly develops, and it subsequently
turns into a gap. Of course, this macroscopic Random Matrix Theory spectrum is totally unlike the
macroscopic Dirac operator spectrum. But it is interesting to zoom in on the microscopic behavior
2Many other details do not match at all. For instance the “phase transition” in the model (15) is continuous, in
contrast to the ﬁnite-temperature phase transition in the massless Nf = 4 theory, which is believed to be of ﬁrst order.
3Similar numerical studies have been performed by K. Splittorﬀ, M.Sc. thesis, The Niels Bohr Institute 1999 (unpub-
lished). Simulations of the macroscopic spectral density in this model can also be found in the original paper by Jackson
and Verbaarschot [14].
16
0
5
10
15
0
0.1
0.2
0.3
ρ(λ)
0
2
4
6
8
0
0.1
0.2
0.3
0.4
0.5
0
5
10
15
 λ
0
2
4
6
8
40
50
60
70
0
2
4
6
8
10
T=0
T=0.5
T=0.75
T=1
T=1.2
T=2
Figure 12: A blowup of the graphs in Fig. 11. The microscopic spectrum changes smoothly from
Bessel-type behavior to Airy-type behavior, going through an intermediate “critical” distribution at
T = 1 corresponding to a macroscopic power-law behavior of type ρ(λ) ∼λ1/3. The exact analytical
curve for the microscopic spectral density at T = 1 has been computed in Ref. [12].
of the Random Matrix spectral density at the soft edge of the gap. In this way, by blowing up the
scale of the smallest eigenvalues, we obtain the plots in Fig. 12 for the same parameter values of T as
above. One sees clearly how the universal Bessel-kernel behavior below Tc turns into the also universal
Airy-kernel above Tc. We note that it is has been shown in Ref. [14] that the massless microscopic
spectral density of the above Random Matrix model has precisely the usual zero-temperature form,
ρs(ζ(T)) = ζ(T)
2
h
JNf (ζ(T))2 −JNf −1(ζ(T))JNf +1(ζ(T))
i
,
(18)
where ζ(T) is simply the eigenvalues rescaled by the (T-dependent) inﬁnite-volume spectral density
at the origin ρ(0, T):
ζ(T) = λ2πNρ(0, T) .
(19)
In this model ρ(0) approaches zero with a mean-ﬁeld type of behavior [14]:
ρ(0, T) = ρ(0, 0)
p
1 −T 2 .
(20)
For T bigger than Tc, but still close to it, we ﬁnd, as expected, a deformation of the Airy-kernel.
In fact, the microscopic behavior there smoothly interpolates between the Bessel-form and the Airy-
form. The peaks corresponding to individual eigenvalues from the Bessel-function behavior below
Tc gradually smoothen out to become the inﬂection points in the spectral density of the Airy-kind
as the soft edge moves away from the origin. To illustrate how accurately one reproduces the Airy-
behavior in this kind of simulations, we show in Fig. 13 the soft edge prediction appropriately scaled
to ﬁt simulation data at T=3. The Airy-behavior is perfectly reproduced close to the edge, but with
deviations after the ﬁrst few eigenvalues(wiggles). The deviation is presumably caused by the limited
number of eigenvalues at N = 300, and when N is increased we expect the ﬁt to improve.
17
500
600
λ
0.0
0.1
0.2
ρ(λ)
Figure 13: A blowup of a T = 3 spectrum compared with the Airy-prediction. There is nice agreement
near the edge.
5
