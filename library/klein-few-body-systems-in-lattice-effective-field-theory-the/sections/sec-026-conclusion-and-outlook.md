---
doc_id: klein-few-body-systems-in-lattice-effective-field-theory-the
doc_title: "Bonn, November 2018"
section_id: sec-026-conclusion-and-outlook
section_title: "Conclusion and Outlook"
section_number: null
pages: 53-55
source_pdf: klein-few-body-systems-in-lattice-effective-field-theory-thesis.pdf
source_sha256: 7ecafdd08255d5c6
doc_brief: "Few-Body Systems in Lattice Effective Field Theory Dissertation Erlangung des Doktorgrades (Dr. rer. nat.) Mathematisch-Naturwissenschaftlichen Fakultät Rheinischen Friedrich-Wilhelms-Universität Bonn"
---
5
6
7
8
9
-500 -400 -300 -200 -100 0
-36
-33
-30
-27
0 500 1000 1500
-2.50
-2.45
-2.40
-2.35
-2.30
-2.25
-2.20
34 36 38
pcot(δ) [MeV]
p2[MeV2]
a=1.97 fma=0.82 fma=0.66 fma=0.56 fma=0.49 fm
pcot(δ) [MeV]
p2[MeV2]
Eb[MeV]
L
Figure 4.2: Lattice space dependence of various parameters. Upper panel: The ﬁnite-volume deuteron bound
state energy. Central panel: The eﬀective range expansion for the 1S 0-channel. Lower panel: The eﬀective range
expansion for the 3S 1-channel.
keep the physical lattice size. The respective values are shown in Tab. 4.3 as well and there is a plateau
starting from a = 0.39 fm. The predictions for the eﬀective range expansion parameters are also quite
good as a 3S 1
≈ 5.470(1)... 5.649(1) fm and r 3S 1
≈ 1.818(1)... 1.899(1) fm depending on the lattice
spacing. Repeating the calculation for the binding energy according to Eq. (4.20) up-to-and-including
terms ofO(r2
e/a2
s) yields for the binding energy EB≈ 2.026(1)... 2.033(1) MeV for the various lattice
spacings in the range between 0.5 fm and 2.0 fm. This is again close to the physical binding energy
and the respective relation is fulﬁlled. For the remaining ones, it yields EB≈ 2.034(1)... 1.899(1) MeV
indicating that larger volumes become necessary particularly for the smallest lattice spacing. Finally, the
theory is well regularized and the diﬀerences between the lattice predictions and the experimental values
of a 3S 1
and r 3S 1
, respectively, can be compensated by higher order terms.
4.5 Conclusion and Outlook
In this chapter, we have studied the lattice spacing a dependence of the neutron-proton system at leading
order in the pionless and the pionful theory. We have used the scattering length and the eﬀective range
47
Chapter 4 Regularization Methods for Nuclear Lattice E ﬀective Field Theory
a−1 [MeV] a [fm] C3S 1
[MeV] C1S 0
[MeV] b [MeV−2] a 3S 1
[fm] r 3S 1
[fm]
100 1.97 −54.07 −36.11 2.59· 10−5 5.470(1) 1.818(1)
130 1.52 −67.11 −45.47 2.40· 10−5 5.513(1) 1.878(1)
160 1.23 −69.31 −46.52 2.41· 10−5 5.527(1) 1.899(1)
200 0.99 −63.83 −41.39 2.65· 10−5 5.523(1) 1.893(1)
240 0.82 −61.55 −39.23 2.83· 10−5 5.511(1) 1.876(1)
300 0.66 −62.20 −39.44 2.92· 10−5 5.498(1) 1.858(1)
350 0.56 −63.30 −40.19 2.92· 10−5 5.491(1) 1.842(1)
400 0.49 −64.31 −40.97 2.91· 10−5 5.491(1) 1.842(1)
500 0.39 −65.47 −41.90 2.89· 10−5 5.500(1) 1.836(1)
600 0.33 −66.14 −42.71 2.82· 10−5 5.553(1) 1.835(1)
700 0.28 −65.61 −42.64 2.86· 10−5 5.649(1) 1.845(1)
Table 4.3: Fit results in EFT with Gaussian-smeared contact interaction and position space regularization for the
pion-nucleon interaction with N = 3.5. The lattice size is L = 34, 36, 38 for a = 0.49... 1.97 fm and L = 38, 40, 42
for a = 0.39... 0.28 fm. The values for a 3S 1
and r 3S 1
are predictions (modulo the consistency condition Eq. (4.20)).
in the 1S 0 partial wave together with the deuteron binding energy to ﬁx the two LECs related to the
LO four-nucleon contact interaction and the smearing parameter b. To focus on the lattice spacing
dependence, we have worked at suﬃciently large lattice volumes so that ﬁnite volume eﬀects do not play
any role here. In the pionless case, it is suﬃcient to smear the contact interactions with a Gaussian-type
function, cf. Eq. (4.11), to achieve a-independence in the range 0.5 ≲ a ≲ 2.0 fm. We have explicitly
shown this for the scattering length and the eﬀective range in the 3S 1-channel, being aware of the strong
correlation between EB and a 3S 1
. In the pionful theory, the contribution from the one-pion-exchange is
best to be regularized in position space, as discussed in detail in Ref. [22]. Again, we can demonstrate
lattice spacing independence for the same range of a. Therefore, it should be possible to calculate the
phase shifts with the transfer matrix method and the spherical wall method. Smaller lattice spacings
should minimize the lattice errors such as the broken rotational invariance and make it possible to increase
the accuracy especially for higher momenta in the partial wave decomposition. Clearly, when decreasing
the lattice spacing, one has to be aware that the perturbative treatment of the NLO and higher order
corrections becomes doubtful and requires a separate investigation but it does not invalidate the results
found here. Furthermore, one should implement this regularization in Monte Carlo simulations in order
to minimize the lattice spacing and artifacts in the simulation. This, however, is a separate issue.
48
CHAPTER 5
