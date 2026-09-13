---
doc_id: arxiv-2608.25107v1
doc_title: "ADoNIS: A Differentiable generatOr of Neutrino Interaction Samples César Jesús-Valls1,∗ 1European Organization for Nuclear Research (CERN), 1211 Geneva 23, Switzerland"
section_id: sec-010-validation
section_title: "Validation"
section_number: null
pages: 7-8
source_pdf: 2608.25107v1.pdf
source_sha256: 6dca8b99a1f32db4
doc_brief: "ADoNIS: A Differentiable generatOr of Neutrino Interaction Samples César Jesús-Valls1,∗ 1European Organization for Nuclear Research (CERN), 1211 Geneva 23, Switzerland — 17 sections: ADoNIS: A Differe"
---
ADoNISimplements the same underlying physics
choices as ACHILLES, enabling a direct validation
against its predictions. Ref. [90] compares ACHILLES
with a broad set of measurements; here we reproduce rep-
resentative comparisons withADoNISand ACHILLES
overlaid, spanning different probes, interaction channels,
target nuclei and beam energies.
Figure 1 shows the MINERvA CC0πsample on 12C
at⟨E ν⟩ ≈3 GeV, generated for the signal definition
of Ref. [138]. The observables span lepton kinematics,
hadron kinematics and the transverse kinematic imbal-
ance (TKI) variables that correlate the two. At MIN-
ERvA energies both quasi-elastic and resonant interac-
tions contribute substantially, with excellent agreement
observed in both. Agreement holds equally for other
beams, binnings and signal definitions. For instance,
we showcase the T2K CC0πand CC1π + samples of
Refs. [139] and [140] in Figs. 13 and 14 of Appendix A.
Figure 2 showcases the double-differential cross sec-
tion for NC 1π 0Xp production measured by Micro-
BooNE [141], and demonstrates that equivalent predic-
tions are also achieved for the two generators for neutral-
current observables on Ar. Analogous agreement in
charged-current MicroBooNE TKI observables [142] is
also presented in Fig. 15 in Appendix A.
The last two comparisons isolate single ingredients.
Figure 3 shows inclusive (e,e′) cross sections on 12C and
40Ar at 2.222 GeV, in the configuration of the Jefferson
Lab E12-14-012 measurements [15, 131, 143]: an elec-
tromagnetic probe of known kinematics, on both target
nuclei, separated into quasi-elastic and resonant contri-
butions. Exclusive electron-scattering observables from
e4ν[144], which confront the neutrino-energy estimators
against a beam of known energy, are given in Fig. 16
of Appendix A. Lastly, Fig. 4 showsπ +–nucleus absorp-
tion and reaction cross sections in the configuration of
Refs. [145–147], where the pions come from a tagged
hadron beam rather than an interaction vertex, so that
the cascade is exercised on its own.
8
Taken together, these comparisons show that the
differentiable reformulation preserves the underlying
physics predictions.
0.0 0.5 1.0 1.5 2.0 2.5 3.0
δαT [rad]
0.0
0.2
0.4
0.6
0.8
1.0dσ/dx [nb]
1e−5
/ Total
/ QE
/ RES
0 500 1000 1500 2000
pn [MeV/c]
0
2
4
6
8
1e−8
0 500 1000 1500 2000
δpT [MeV/c]
0
2
4
6
8
1e−8
0.0 0.5 1.0 1.5 2.0 2.5 3.0
δϕT [rad]
0
2
4
6
1e−5
600 800 1000 1200
pp [MeV/c]
0
1
2
3
4
1e−8
0 10 20 30 40 50 60 70
θp [deg]
0
2
4
6
8
1e−7
2000 4000 6000 8000 10000
pμ [MeV/c]
0.0
0.2
0.4
0.6
0.8
1.0
1e−8
0 5 10 15 20
θμ [deg]
0.0
0.5
1.0
1.5
1e−6
FIG. 1. ADoNIS (solid) vs. ACHILLES (dashed). MINERvA
CC0πon 12C at⟨E ν⟩≈3 GeV, with the signal definition of
Ref. [138]: the TKI variablesδα T ,p n,δp T andδϕ T , and the
proton and muon kinematics.
0 200 400 600 800 1000 1200
pπ0 [MeV/c],  −1 < cos θπ0 < 0
0
1
2
3dσ/dx [nb]
1e−8
/ Total
/ QE
/ RES
0 200 400 600 800 1000 1200
pπ0 [MeV/c],  0 < cos θπ0 < 0.5
0.0
0.5
1.0
1.5
1e−8
0 200 400 600 800 1000 1200
pπ0 [MeV/c],  0.5 < cos θπ0 < 0.85
0.0
0.2
0.4
0.6
0.8
1.0
1e−8
0 200 400 600 800 1000 1200
pπ0 [MeV/c],  0.85 < cos θπ0 < 1
0
1
2
3
4
5
1e−9
FIG. 2. ADoNIS (solid) vs. ACHILLES (dashed). Micro-
BooNE NC 1π0Xp on 40Ar [141]: the double-differential cross
sectiond 2σ/dcosθ π0dpπ0, in slices of cosθ π0.
0.2 0.4 0.6 0.8
ω [GeV]
0
2500
5000
7500
10000
12500dσ/dω [nb/GeV]
40Ar/ Total
/ QE
/ RES
0.2 0.4 0.6 0.8
ω [GeV]
0
1000
2000
3000
4000
5000 12C
FIG. 3. ADoNIS (solid) vs. ACHILLES (dashed). Inclusive
(e,e′) cross sectiondσ/dωon 12C and 40Ar at a beam energy
of 2.222 GeV andθ e′ ≈15.5 ◦ [15, 131, 143], separated into
quasi-elastic and resonant contributions.
0.1 0.2 0.3 0.4
0
50
100
150
200σ [mb]
π +  12C
absorption
0.2 0.4 0.6 0.8 1.0
0
200
400
600
800σ [mb]
π +  12C
reaction
0.1 0.2 0.3 0.4
beam |p| [GeV/c]
0
100
200
300
400
500σ [mb]
π +  40Ar
0.2 0.4 0.6 0.8 1.0
beam |p| [GeV/c]
0
250
500
750
1000
1250
1500σ [mb]
π +  40Ar
FIG. 4. ADoNIS (solid) vs. ACHILLES (dashed).π +–nucleus
absorption and reaction cross sections on carbon and argon as
a function of pion momentum [145–147], testing the intranu-
clear cascade in isolation.
