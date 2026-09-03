---
doc_id: arxiv-2201.05665v1
doc_title: "HAROLD WIDOM’S WORK IN RANDOM MATRIX THEORY"
section_id: sec-004-41-general-invariant-ensembles-and-the-wigner-en
section_title: "General invariant ensembles and the Wigner ensembles"
section_number: 4.1
pages: 7-9
source_pdf: 2201.05665v1.pdf
source_sha256: bad7bde03d199a73
doc_brief: "HAROLD WIDOM’S WORK IN RANDOM MATRIX THEORY — This is a survey of Harold Widom’s work in random matrices."
---
GSE ensembles are respectively particular examples of unitary (UE), orthogonal (OE) and
symplectic (SE) ensembles of random matrix theory. The joint probability density of the
eigenvalues for these ensembles are given by (cf. (3.1))
PNβ(λ1, ..., λN) = Z−1
Nβ e−ηβ
PN
j=1 V (λj) Y
j<k
|λj −λk|β,
(4.1)
where η1 = 1, η2 = 1, η4 = 2 (this reﬂects the fact that the eigenvalues of self-dual Hermitian
matrices come in pairs), and the potential V (λ) is a polynomial with even leading term,
V (λ) =
2m
X
k=1
tkλk,
t2m > 0.
(4.2)
(More general potential functions are also allowed.) GUE, GOE and GSE correspond to
the choice V (λ) = λ2. Consider again the upper edge ﬂuctuations of the spectrum. Edge-
universality states that for a given polynomial potential V (λ) there exist scalars z(β)
N
and s(β)
N
such that
lim
N→∞Prob
 
λmax −z(β)
N
s(N)
N
≤t
!
= Fβ(t),
(4.3)
where Fβ(t), β = 1, 2, 4 are exactly the same Tracy-Widom distribution functions as in
(3.2).
For β = 2 this result was obtained in [DKMVZ1, DKMVZ2] and for β = 1, 4 in
[DeGi1, DeGi2]. It should be noted that the authors of [DeGi1, DeGi2] based their analysis
on Widom’s papers [11, 12] where important relations between symplectic, orthogonal and
unitary ensembles were established for ﬁnite N.
These relations allowed the authors of
[DeGi1, DeGi2] to use, in the symplectic and orthogonal cases, the asymptotic estimates
8
IVAN Z. CORWIN, PERCY A. DEIFT, AND ALEXANDER R. ITS
previously obtained in [DKMVZ2] for the unitary ensembles. There are also a variety of
universality results for eigenvalues in the bulk of the spectrum (see e.g. [Dei3] and references
therein ) for UE, OE, and SE.
Complementary to the invariant ensembles (UE, OE, and SE) are the so-called Wigner
matrix ensembles, i.e., random matrices with independent identically distributed entries.
Tracy-Widom edge universality for these ensembles is also valid and this important fact
was proved by Soshnikov [Sos]. In addition, universality in the bulk of the spectrum for the
Wigner ensembles is now established—see e.g. [Erd] for a comprehensive survey of the results
and a historical review.
The Tracy-Widom distribution appears also in Hermitian matrix models with varying
weights. These are unitary ensembles with the potential V (λ) in (4.1) replaced by NV (λ).
Universality results of the form (4.3) are also true for such scaled potentials (see e.g. [DKMVZ1],
[Dei3] and the references therein). For potentials NV (λ) a key issue is the large N asymp-
totics of the partition functions
ZN =
Z ∞
−∞
...
Z ∞
−∞
e−N PN
j=1 V (λj) Y
j<k
(λj −λk)2dλ1...dλN.
(4.4)
Under certain regularity conditions, the leading large N behavior of the partition function is
described by the relation [Joh1]
ZN ∼e−N2F0,
N →∞,
(4.5)
where F0 is the free energy of the model, and is given explicitly in terms of the equilib-
rium measure corresponding to the potential V (λ). The equilibrium measure is the unique
probability measure νeq which minimizes the energy functional
IV (ν) = −
Z Z
R2 ln |λ −λ′|dν(λ)dν(λ′) +
Z
R
V (λ)dλ.
The formula for the free energy reads
F0 = IV (νeq).
As shown in [DKM], in the case that V (λ) is real analytic and V (λ)
ln |λ| →+∞as |λ| →∞, the
equilibrium measure is absolutely continuous and is supported on a ﬁnite number of intervals.
The derivative of νeq coincides with the mean limiting density of eigenvalues of the associated
UE. If the support of the equilibrium measure consists of one interval, then one can prove
(see [EM] and also [BI]) the existence of a full asymptotic expansion,
ln
ZN
ZGauss
N
∼−N2e0 +
∞
X
g=1
eg
N2g−2 ,
N →∞,
(4.6)
where ZGauss
N
stands for the partition function of GUE ( V (λ) = λ2). Since 1980, the expan-
sion (4.6) has played a prominent role in the application of random matrices to enumerative
topology.
This role was ﬁrst recognized in [BIZ] together with the discovery of its deep
connections to the counting of graphs on Riemann surfaces (see [EM] for more details).
The number of intervals in the support of the equilibrium measure depends on the values
of the parameters t1, ..., t2m in (4.2). It is of great interest to study the transition regimes,
i.e. regimes involving values of tj near critical values when the number of the intervals in
the support of the equilibrium measure changes. The ﬁrst example where one can observe
HAROLD WIDOM’S WORK IN RANDOM MATRIX THEORY
9
this important critical phenomenon is the even quartic potential V (λ) = t4λ4 + t2λ2. Up to
a trivial renormalization, the potential V can be chosen in the form
V (λ) = 1
4t2 λ4 +

1 −2
t

λ2.
(4.7)
For t > 1 the support of the equilibrium measure corresponding to this potential consists of
one interval. Moreover, as shown in [BI], all the coeﬃcients eg(t) of the asymptotic series
(4.6), as functions of t, are real analytic on [1, ∞). If t < 1, the support becomes two intervals.
At the critical value, t = 1, the support consists of one interval but the density function has
a double zero inside the support at λ = 0. The relevant double scaling limit near the critical
point t = 1 is prescribed by the scaling condition

(t −1)N2/3

 < C.
(4.8)
As N →∞and t →1 satisfying (4.8), the partition function admits the following asymptotic
representation [BI]:
ZN(t)
ZGauss = F2

(t −1)22/3N2/3
Zreg
N (t)

1 + O(N−1/3+ϵ)

,
ϵ > 0
(4.9)
where ln Zreg
N
is the sum of the ﬁrst two terms of the series (4.6), i.e.,
Zreg
N (t) = e−N2e0(t)+e1(t),
and F2(x) denotes, as before, the second Tracy-Widom distribution. Thus we see that in this
context F2 appears not as a distribution function but rather as a special factor describing
the transition between the one interval and two interval asymptotic regime in the large N
limit of these partition functions. This gives F2 added meaning in the realm of enumerative
topology, not just probability. Although not yet proven, it is expected that equation (4.9) is
universal.
