---
doc_id: s10052-020-08615-2
doc_title: "Sum rule for the Compton amplitude and implications for the proton–neutron mass difference"
section_id: sec-017-16-input-used-for-the-structure-functions
section_title: "Input used for the structure functions"
section_number: 16
pages: 11-13
source_pdf: s10052-020-08615-2.pdf
source_sha256: 23becb0b1a2e7f1b
toc_source: outline
doc_brief: "Sum rule for the Compton amplitude and implications for the proton–neutron mass difference — The Cottingham formula expresses the leading contribution of the electromagnetic interaction to the"
---
Forthenumericalevaluationoftheinelasticcontributions,we
need a representation for the difference between the structure
functions of proton and neutron, and not only for the rela-
tively well explored quantity F2, but also for the longitudinal
component FL, which is known less well. At low values of
Q2, we closely follow the analysis of [11] and distinguish
123
three different regions in the centre of mass energy W = √s
(numerical values for W and Q2 are given in GeV units):
(i) For the range W < 1.3, we rely on the parametrizations
of the structure functions of MAID and DMT [54–56]
– we refer to these as MD. Both of them are accessible
on the MAID home page [57]. We identify the central
values of the structure functions in this region with the
mean of the two parametrizations and use the difference
as an error estimate (half of the difference would sufﬁce
to cover the two). The green error band in Fig. 1, shows
the corresponding representation of the structure function
¯F for Q2 = 1.
(ii) In the interval 1.3 < W < 3, we make use of the rep-
resentation due to Bosted and Christy (BC) [58,59]. It
contains a wealth of information, but suffers from sev-
eral shortcomings that are discussed in detail in section
5.1 of [11]. Part of the problem originates in the fact that
the longitudinal cross section is more difﬁcult to mea-
sure than the transverse one. In [58,59] it is assumed that
the ratio R = σL/σT of the neutron cross sections is the
same as for the proton. In the region where the Pomeron
dominates, this holds to good accuracy, but we need the
difference between the two, where Pomeron exchange
drops out. The assumption amounts to using an approxi-
mation and introduces a systematic error that is not easy
to estimate.
In our opinion, the procedure used in [11] to cope with
the uncertainties in the region 1.3 < W < 3 is on the
conservative side and we adopt it in the present work:
we treat the transverse and longitudinal cross sections as
independent and assign an uncertainty in σ p−n
T
and σ p−n
L
of 8% of σ p
T and 8% of σ p
L , respectively. In part of phase
space, this may well overestimate the uncertainties con-
siderably – a reanalysis of the data in the resonance region
would be most welcome. The structure of the brown error
band reﬂects the resonances occurring in this region.
(iii) For W > 3, Q2 < 1, we rely on the parametrization of
the proton structure functions due to Alwall and Ingel-
man (AI) [60]. It represents the amplitude as a sum of
a contribution from the Pomeron and one from the a2.
In the difference between the proton and neutron ampli-
tudes, the Pomeron drops out. We assume that the cou-
plings of the a2 to proton and neutron are approximately
SU(3)-symmetric and attach an uncertainty of 30% to
the representation for the difference between proton and
neutron obtained on this basis. The blue band in Fig. 1
shows the corresponding uncertainty range at Q2 = 1.
For details, we refer to section 5.1 in [11].
(iv) In the region W > 3, Q2 > 1, we use the solution of
the DGLAP equations constructed by Alekhin, Blümlein
and Moch, who obained numerical values for the struc-
ture functions over a wide range: 1 ≤Q2 ≤2 × 105
and 10−7 ≤x ≤0.99. The values of F2(x, Q2) and
FL(x, Q2) are listed for the proton as well as for the
neutron on a grid of 60 × 98 points. We thank Johannes
Blümlein for providing us with this table, which we refer
to with the acronym ABM. The underlying analysis is
described in [61–63]. In the region where we make use
of these results (see below), we estimate the uncertainty
in the values obtained from ABM for ¯F p−n and F p−n
2
at
30%.
In the deep inelastic region, asymptotic freedom leads
to very strong constraints, particularly for the structure
function FL. The strength of these constraints is clearly
visible at leading order of the perturbative expansion,
where FL is given by an integral over F2. The DGLAP
equations extend this relationship to higher orders, by
means of the renormalization group. In our framework,
the properties of FL play a crucial role in the evaluation of
the sum rule for the subtraction function. The theoretical
constraints on this quantity are very important for our
analysis, particularly also because the raw experimental
information for FL is much weaker than the one for F2.
The black dots in Fig. 1 show the numbers obtained for
W and ¯F from the entries for x, F2 and FL, at the lowest
value of Q2 listed in the ABM table, Q2 = 1, and W > 3.
While the result agrees very well with AI for W > 5, the
two representations do differ at lower values of W. Since the
DGLAP equations rely on perturbation theory, we should
not be surprised to ﬁnd deviations at low momenta, i.e. in the
region where Q2 as well as W are small.
17 Polarizabilities, ¯S(0)
Two low energy theorems relate the values of T1 and T2 at
q = 0 to the polarizabilities of proton and neutron:3
T1 = T el
1 −κ2
4m2 −m
αem
βM + O(ν2, q2).
T2 = T el
2 + m
αem
(αE + βM) + O(ν2, q2),
(79)
where κ is the anomalous magnetic moment of the particle
(these relations hold separately for proton and neutron). The
dispersion relation for T2 converts the second one into the
Baldin sum rule [64], which expresses the sum αE + βM as
an integral over the cross section for photoproduction. For
the combination ¯T = T1 + 1
2T2 we are working with, the low
energy theorem involves the difference between the electric
3 For a derivation see e.g. appendix B.8 in [11]).
123
and magnetic polarizabilities:
¯T = ¯T el −κ2
4m2 +
m
2αem
(αE −βM) + O(ν2, q2).
(80)
It ﬁxes the value of the subtraction function ¯S(q2) at q2 = 0
in terms of the polarizabilities:
¯S(0) = −1
4m2 κ2 +
m
2αem
(αE −βM),
(81)
For q2 = 0, our sum rule for the subtraction function thus
represents an analog of the Baldin sum rule: it determines
the value of the difference between the electric and magnetic
polarizabilities rather than their sum, in terms of the structure
functions. While the Baldin sum rule directly follows from
the unsubtracted dispersion relation for T2, the one for αE −
βM relies on Reggeon dominance.
The integrals over the structure functions relevant for the
evaluation of the subtraction function in the dispersion rela-
tion for T1 at small values of Q2 were analyzed in detail
in section 5 of [11]. As shown there, the prediction for the
electric polarizability comes with comparatively small uncer-
tainties:4
α p−n
E
= −1.7(4) [12].
(82)
The averages for proton and neutron quoted by the Particle
Data Group yield α p−n
E
= −0.6(1.2) [65]. The fact that
experiment agrees with the prediction within errors provides
a test of Reggeon dominance.
For a review of the currently available information about
the polarizabilities, in particular also of the analysis based on
chiral effective theories, we refer to [66–68]. In the frame-
work of χPT, the representation of the virtual Compton scat-
tering amplitude has been worked out to ﬁrst nonleading
order [69]. In this reference, the low energy singularity gen-
erated by the Δ(1232) resonance is explicitly accounted for.
It will be of considerable interest to compare the result of this
analysis for the slope of the subtraction function at Q2 = 0
with the solution of the sum rule that follows from Reggeon
dominance constructed in the present paper.
The Baldin sum rule and the data on photoproduction
imply that the sum αE + βM is known more accurately
than the individual terms. For this reason, it is useful to
treat αE ± βM as the two independent quantities. The results
quotedfor protonandneutroninthecompilationof Melendez
et al. lead to
(αE + βM)p−n = −1.20(45) [69],
(83)
(αE −βM)p−n = −0.4(3.1) [69].
(84)
Combining the prediction (82), which is based on Reggeon
dominance, with the result (83) obtained from photoproduc-
tion, we obtain a prediction for the magnetic polarizability,
4 As usual, the polarizabilities are given in units of 10−4 fm3.
which is slightly more accurate than the one given in [11]:
β p−n
M
= 0.5(6).
(85)
There were early attempts at calculating the electric polar-
izabilities on the lattice [71–73], based on turning on a con-
stant external electric ﬁeld, but they did not reach a level
where the results could be compared with the experimental
determinations in a meaningful way. The very recent lat-
tice determination of the magnetic polarizabilities, however,
which makes use of a constant external magnetic ﬁeld, does
yield a remarkably precise value for β p−n
M
,
β p−n
M
= 0.80(28)(4) [73],
(86)
in good agreement with our predicton in equation (85).
In connection with the proton–neutron mass difference,
the polarizabilities are of interest because they determine the
value of the subtraction function ¯S(q2) at q2 = 0, according
to (81). The prediction (82) for α p−n
E
and the experimental
value (83) of (αE + βM)p−n imply
¯S(0) = −1.71(77) GeV−2.
(87)
The uncertainty is signiﬁcantly smaller than the one obtained
from the experimental value of (αE −βM)p−n:
¯S(0) = −0.2(2.6) GeV−2[69].
(88)
On the other hand, combining the lattice result (86) for the
magnetic polarizability with the experimental value (83) of
(αE + βM)p−n, we obtain a result for the subtraction func-
tion at the origin that is even slightly more precise than the
prediction:
¯S(0) = −2.22(60) GeV−2.
(89)
The fact that, within errors, this result agrees with the pre-
diction (87) amounts to a more stringent test of the Reggeon
dominance hypothesis than the one discussed above. It is
important to pursue the determination of the polarizabilities;
in particular, the pioneering lattice result which provides such
a test calls for conﬁrmation.
