---
doc_id: arxiv-1301.6953v1
doc_title: "LU TP 13-03 Januray 2013"
section_id: sec-002-3-determining-low-energy-constants-in-the-contin
section_title: "Determining low-energy-constants in the continuum"
section_number: 3
pages: 5-7
source_pdf: 1301.6953v1.pdf
source_sha256: 8c9231d0832df3b6
doc_brief: "LU TP 13-03 Januray 2013 — 12 sections: Chiral Perturbation Theory; Introduction; Determining low-energy-constants i"
---
Lattice QCD has now reached the stage where they can start det ermining the ChPT LECs. A
review is the FLAG collaboration [21] and talks at this confe rence that had results on LECS are
[10, 22 – 24].
For the two-ﬂavour constants the status has not really changed much since the previous chiral
dynamics. The constants ¯l1 to ¯l4 are determined from ChPT at order p6 and the Roy equation
analysis in ππ and FS [25]. A related talk is [26]. ¯l5 and ¯l6 come from FV and π → ℓνγ [27, 28]
and from Π V − Π A [29]. Some related work using similar sum rules is [30]. In conclusion:
¯l1 = −0.4 ± 0.6 , ¯l2 = 4.3 ± 0.1 , ¯l3 = 2.9 ± 2.4 ,
¯l4 = 4.4 ± 0.2 , ¯l5 = 12.24 ± 0.21, ¯l6 − ¯l5 = 3.0 ± 0.3 ,
¯l6 = 16.0 ± 0.5 ± 0.7 .
and l7 ∼ 5 · 10−3 from π0-η mixing [14]. In the two-ﬂavour case the contribution from th e order
p6 LECs was small so the uncertainty on estimating those is not very important.
The uncertainty on estimates of the order p6 LECs, the Cr
i , in the three ﬂavour case is much
more important because m2
K,m2
η ≫ m2
π. The larger Cr
i dependent contributions make their estimates
much more relevant. Typically, if the term multiplying a particular Cr
i leads to a kinematical depen-
dence it can be measured and the estimates tested. But if it leads only to a higher order quark-mass
dependence they lead to experiment in a 100% correlated way w ith the order p4 LECs, the Lr
i .
Here we really need the lattice, typically the latter type of Cr
i need scalars to estimate their values
5
Chiral Perturbation Theory and Mesons Johan Bijnens
-1
-0.8
-0.6
-0.4
-0.2
 0
 0.2
 0.4
 0.6
 0.8
 1
 0  2  4  6  8  10  12  14
disp/exp
NLO+NNLO
NLO
Figure 3: The quality of the relations found in [31]. Shown are the NLO a nd NNLO predictions for
combinations of observables with vanishes NNLO LEC contributions as well as the experimental/dispersive
results for the same combinations.
from resonance exchance and are thus intrinsically less well estimated. In addition, often the large
Nc suppressed terms in the order p6 lagrangian contribute with large coefﬁcients as well and al l
estimates so far of the LECs rely on largeNc to a large extent. One big question is thus whether we
are really testing ChPT or simply doing a phenomenological ﬁ t. In order to answer this question
a systematic search for relations that are independent of th e Cr
i was done [31]. We found there 35
relations between 76 observables and of these 13 had sufﬁcie nt data to study their success. There
were 7 relations in
ππ scattering which worked about the same for two and three ﬂavo ur ChPT.
The two relations involving a−
3 did not work well in either case. Of the 5 extra relations invo lving
ππ and πK scattering three worked well, one of the bad ones involveda−
3 and the last one had very
large NNLO corrections. The ﬁnal relation involves Kℓ4 and did not work well probably because
ChPT fails to describe the quadratic slope in theF form-factor [32, 33]. The quality of the relations
is shown in Fig. 3. The conclusion is that three ﬂavour ChPT “s ort of” works taking into account
that the relations involve very large correlations and that thus the experimental or dispersive input
errors might be underestimated.
The previous major ﬁt to determine the Lr
i using NNLO formulas dates back to 2001 [34].
Given that many more calculations in three ﬂavour ChPT at NNL O have been performed since
and that the experimental input used then has also changed, an update has become necessary. This
was done in [35] and the main results are summarized in Tab. 2. The old programs in the isospin
conserving versions were rewritten in C++ for this purpose. The ﬁrst column uses the old input
values and reproduces the old ﬁt [34] which was done isospin violation included. The next columns
6
Chiral Perturbation Theory and Mesons Johan Bijnens
ﬁt 10 iso NA48/2 FK/Fπ All ⋆ All
old data ππ, πK, ⟨r2
S⟩ ms/ ˆm
103Lr
1
0.39 ± 0.12 0.88 0.87 0 .89 0.88 ± 0.09
103Lr
2
0.73 ± 0.12 0 .79 0 .80 0 .63 0.61 ± 0.20
103Lr
3
−2.34 ± 0.37 −3.11 −3.09 −3.06 −3.04 ± 0.43
103Lr
4
≡ 0 ≡ 0 ≡ 0 0.60 0.75 ± 0.75
103Lr
5
0.97 ± 0.11 0 .91 0.73 0.58 0.58 ± 0.13
103Lr
6
≡ 0 ≡ 0 ≡ 0 0 .08 0.29 ± 0.85
103Lr
7
−0.30 ± 0.15 −0.30 −0.26 −0.22 −0.11 ± 0.15
103Lr
8
0.60 ± 0.20 0 .59 0 .49 0 .40 0.18 ± 0.18
χ2 0.26 0 .01 0 .01 1 .20 1.28
dof 1 1 1 4 4
Table 2: The main new ﬁt of the Lr
i of [35]. The various columns show the changes w.r.t. the old ﬁt of [34].
give the results from including the NA48/2 data on the form factors [36], the new value of FK/F
π,
the inclusion of ππ, πK scattering and the scalar radius and ﬁnally the new value of ms/ ˆm. The
LEC that changed most at each step is put in a box. In the ﬁnal re sult one note signiﬁcant values
for the Nc-suppressed constants Lr
4,Lr
6, albeit with large errors and the fact the the largeNc-relation
2Lr
1 = Lr
2 no longer holds well.
A large number of variations on the ﬁt were tried in [35] by letting
μ free and varying the input
used for the Cr
i . All of these gave similar values for the Lr
i . However, a problem occurred when
including the relation between the 2 and 3-ﬂavour LECs of [37 ]. In order for getting this relation
to work well we needed nonzero values for at least some Nc-suppressed Cr
i . In [35] a large effort
was done to ﬁnd reasonable looking Cr
i that allowed to get good ﬁts to all of the inputs. Many were
found but there is no good ground to prefer any of these. More work especially in trying to include
lattice results is deﬁnitely needed. For now, ﬁt All of Tab. 2 and [35] should be regarded as the
standard values for the Lr
i .
