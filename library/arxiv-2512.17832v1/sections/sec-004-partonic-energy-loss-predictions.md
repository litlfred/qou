---
doc_id: arxiv-2512.17832v1
doc_title: "From Lead to Helium: Discovery Potential for Jet Quenching in the Smallest Collision Systems"
section_id: sec-004-partonic-energy-loss-predictions
section_title: "Partonic energy loss predictions"
section_number: null
pages: 3-4
source_pdf: 2512.17832v1.pdf
source_sha256: 7cad0d880361a6c3
toc_source: outline
doc_brief: "From Lead to Helium: Discovery Potential for Jet Quenching in the Smallest Collision Systems — 9 sections: From Lead to Helium: Discovery Pot; Introduction; Nuclear modification factor"
---
There is a large
literature of partonic energy loss calculations in various
frameworks that make different assumptions [59–65] as
well as many phenomenological implementations of these
energy loss calculations that have been applied to small
systems [31, 33, 34, 66–70]. We use our pQCD-based en-
ergy loss model that is described in detail in our previous
work [44], briefly recapping the main features here.
Partons propagate through a fluctuating collision ge-
ometry [71] that is generated with IP-Glasma initial con-
ditions [72, 73] and evolved according to longitudinal
Bjorken expansion [74]. Initial nucleon locations are sam-
pled event-by-event using Woods-Saxon distributions for
Pb, Au, and Xe with standard parameters [71]; Projected
Generator Coordinate Method (PGCM) [75, 76] sampling
for Ne and O [77]; and a variational Monte Carlo (VMC)
for 3He [78] and 4He [79, 80]. While both 6Li and 10B
are small nuclei, and so should in principle be modeled
similarly to He or Ne / O, in this first work we model
them with a Woods-Saxon distribution as only the one-
and two-nucleon distributions from these more sophisti-
cated nucleon configurations are available. The Woods-
Saxon parameters are found to be R = 1.355 fm and
a = 0.584 fm for 6Li, and R = 2.367 fm and a = 0.349 fm
for 10B by fitting to single nucleon densities computed
in the same VMC framework as 3He and 4He [81]. A
minimum nucleon separation of 0.9 fm is enforced for all
Woods-Saxon implementations [71]. Since 4He is small
and tightly bound, our results (see Fig. 1) suggest the
Woods-Saxon geometry is conservative:
6Li has 50%
more nucleons than 4He and is less tightly bound, so
we expect the medium produced in 6Li collisions to be
significantly larger than for 4He. Thus, our prediction
R6Li6Li ≃R4He4He likely represents a conservative esti-
mate for the amount of suppression. We expect that a
more careful treatment of the initial-state geometry—a
significant theoretical task—would produce predictions
of greater suppression.
Parton production is assumed to be the same in p + p
as in A + A.
Including nPDF effects would likely be
largely absorbed in a rigorous statistical recalibration to
large system data.
As one moves to smaller systems,
where nPDF effects constitute a larger fractional contri-
bution, the predicted suppression from our energy loss
model would presumably increase. Our conclusions are
therefore conservative with respect to the magnitude of
suppression due to energy loss in small systems.
We compute both collisional and radiative energy loss
using pQCD-based calculations.
Radiative energy loss
is computed in the DGLV framework [82] including cor-
rections that are exponentially suppressed by pathlength
[83] and neglected by all other models [84], making
our calculation particularly well-suited to small systems.
Collisional energy loss is computed using two limiting
cases: hard thermal loops (HTL)-only [85] and Braaten-
Thoma (BT) [86]. Collisional energy loss is essential for
reliable small system predictions, as it dominates radia-
tive loss (L vs L2 scaling) for very short paths [49].
We treat the effective strong coupling αeff.
s
as our single
free parameter, neglecting running coupling effects. We
previously estimated the uncertainty from this approxi-
mation by allowing the coupling to run over commonly
used phenomenological scales and found the uncertainty
to be small when extrapolating our results to small sys-
tems [87]. The effective strong coupling is fit to all avail-
able high-pT RAA data from charged hadrons, pions, and
D mesons with 8 GeV ≤pT ≤50 GeV in 0–50% central-
ity Pb + Pb collisions [44]. Theoretical uncertainties are
estimated from two sources: varying the collinear radi-
ation cone by factors of two up and down [44, 48], and
the choice between the two collisional kernels, HTL-only
and BT, which treat the HTL-vacuum propagator transi-
tion in limiting ways. The fit is performed separately for
each model variation, and the envelope of results defines
our theoretical uncertainty band. We find the best fit
0-10% energy loss
0-100% energy loss
nPDF only
10
0.6
0.7
0.8
0.9
1
1.1
1.2
pT (GeV)
RAA
3He
10
pT (GeV)
4He
10
102
pT (GeV)
6Li
FIG. 2. Plot of RAA as a function of pT for π0 hadrons produced in 3He + 3He (left), 4He + 4He (central), and 6Li + 6Li (right)
collisions. Predictions from our partonic energy loss model are shown for 0–100% centrality (red) as well as 0–10% centrality
(green), where the band represents the envelope of all energy loss results computed with different variations in the theoretical
uncertainty. The nPDF-only predictions are also shown (blue), where the lighter, outer band represents the nPDF and PDF
uncertainties and the darker, inner band represents the scale uncertainties.
extracted is αeff.
s
= 0.37+0.11
−0.08 at LHC [44]. While it is dif-
ficult to translate our extracted αeff.
s
to the jet transport
coefficient, our best translation gives a jet transport coef-
ficient normalized to temperature cubed of ˆq/T 3 = 11±3
[44].
