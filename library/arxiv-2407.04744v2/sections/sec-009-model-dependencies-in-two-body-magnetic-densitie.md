---
doc_id: arxiv-2407.04744v2
doc_title: "Magnetic structure of A≤ 10 nuclei using the Norfolk nuclear models with quantum Monte Carlo methods G. Chambers-Wall 1,∗ A. Gnech 2,3,† G. B. King 1,‡ S"
section_id: sec-009-model-dependencies-in-two-body-magnetic-densitie
section_title: "Model dependencies in two-body magnetic densities"
section_number: null
pages: 12-16
source_pdf: 2407.04744v2.pdf
source_sha256: fc6fda3138296fb1
doc_brief: "Magnetic structure of A≤ 10 nuclei using the Norfolk nuclear models with quantum Monte Carlo methods G. Chambers-Wall 1,∗ A. Gnech 2,3,† G. B. King 1,‡ S — 21 sections: Front matter; Theory; Introduct"
---
Up to this point, we have analyzed the densities only
for one model; however, it is important to assess the cut-
off dependence, which is evidently important in the inte-
grated two-body contributions. To that end, we compare
the dominant IV contributions to the 3H magnetic mo-
ment in Fig. 9. The effect of the softer cutoff in the Ia ⋆
regulator on the NLO(OPE) and N2LO(∆) currents is,
unsurprisingly, to reduce the two-body magnetic density
at short distances; however, the tail of the density is un-
affected by the cutoff function. Thus, taking a softer
cutoff quenches the overall magnitude of the matrix el-
ement. This particularly impacts the N2LO(∆) current
which is of shorter-range than the NLO contribution due
to the presence of the intermediate ∆-isobar. The soft
cutoff removes strength from the N2LO(∆) magnetic mo-
ment around its peak, resulting in a large quenching of
the contribution in model Ia⋆ relative to model IIb⋆. The
N3LO(NM) contribution, however, is enhanced when us-
ing the softer cutoff of model Ia ⋆. The contact density
is broadened for the softer cutoff while preserving the
overall magnitude. This effect is likely due to a combina-
tion of having a broader Gaussian representation of the
δ-function and a larger density of short-range IV pairs.
A similar broadening of the contact densities is ob-
served in Fig. 10 which shows the IS densities plotted
for 6Li. For the long-range N3LO(OPE) IS contribution,
the correlation functions I1(x) andI2(x) are particularly
sensitive to the choice of regulator, as was previously ob-
served in Ref. [6]. This can move the node in the density
and change the overall sign of the contribution to the
magnetic moment from this current, as shown in the fig-
ure.
From the model comparison, it is clear that altering
the short-range dynamics with different cutoffs signifi-
cantly impacts two-body magnetic moments. Clearly,
if one takes a cutoff that is too small, it will spoil the
convergence behavior of the higher-order contributions
due to significant quenching of the NLO and N2LO(∆)
terms. This quenching is compensated for by a larger
N3LO(NM) IV fit contribution and thus is not seen if
one looks only at the total magnetic moment; however,
if one were to perform the calculation up to NLO in the
current, evidently the model dependence would induce an
error much larger than the naive expectation from power
counting. Given this significant model dependence of the
two-body contributions and the particular importance of
the IV piece in predicting magnetic structure, it is crucial
to investigate this cutoff dependence more rigorously in
the future.
13
0.00
0.25
0.50
0.75
1.00
r2
ij
2b
M /|r2
ij
2b
M |max
NLO OPE
 N2LO 
 N3LO MIN IV
3H
3He
7Li
7Be
8Li
8B
9Be
9Li
0.0
0.5
1.0
r2
ij
2b
M /|r2
ij
2b
M |max
N3LO NM IV
 N3LO OPE IV d′8
 N3LO OPE IV d′21
0.0 0.5 1.0 1.5 2.0 2.5 3.0 3.5 4.0
rij (fm)
0.00
0.25
0.50
0.75
1.00
r2
ij
2b
M /|r2
ij
2b
M |max
N3LO LOOP M1
0.0 0.5 1.0 1.5 2.0 2.5 3.0 3.5 4.0
rij (fm)
T otal IV
FIG. 8: Scaled two-body VMC IV magnetic densities for different nuclei computed with model IIb ⋆ as a function of
interparticle spacing rij. Different colors represent different nuclei.
0 1 2 3 4
rij (fm)
0.05
0.00
0.05
0.10
0.15
4 r2
ij
2b
M
3H NLO OPE
N2LO 
N3LO NM IV
FIG. 9: Two-body VMC magnetic densities arising from
the NLO (blue circles), N2LO-∆ (orange squares), and
the N3LO(NM) IV (green triangles) contributions for
3H computed with model Ia⋆ (filled symbols) and IIb⋆
(open symbols) as a function of interparticle spacing rij.
0 1 2 3
rij (fm)
0.050
0.025
0.000
0.025
0.050
4 r2
ij
2b
M
6Li
N3LO MIN IS
N3LO OPE IS
FIG. 10: Two-body VMC magnetic densities arising
from the N3LO(MIN) IS (blue circles), and the
N3LO(OPE) IS (orange squares) contributions for 6Li
computed with model Ia⋆ (filled symbols) and IIb⋆
(open symbols) as a function of interparticle spacing rij.
14
0.0 0.5 1.0 1.5 2.0 2.5 3.0
q [fm−1]
10−7
10−6
10−5
10−4
10−3
10−2
|FM (q)|2
Sick 2001
(a) 3H
0.0 0.5 1.0 1.5 2.0 2.5 3.0
q [fm−1]
10−7
10−6
10−5
10−4
10−3
10−2
|FM (q)|2
Sick 2001 (b) 3He
0.0 0.5 1.0 1.5 2.0 2.5 3.0
q [fm−1]
10−7
10−6
10−5
10−4
|FM (q)|2
Bergstrom 1982
Lapikas 1978
Rand 1966
Goldemberg 1963
Peterson 1962 (c) 6Li
0.0 0.5 1.0 1.5 2.0 2.5 3.0
q [fm−1]
10−5
10−4
10−3
|FM (q)|2
Lichtenstadt 1983
Van Niftrik 1971
Goldemberg 1963
Peterson 1962
(d) 7Li
0.0 0.5 1.0 1.5 2.0 2.5 3.0
q [fm−1]
10−5
10−4
|FM (q)|2 (e) 7Be
0.0 0.5 1.0 1.5 2.0 2.5 3.0
q [fm−1]
10−6
10−5
10−4
10−3
|FM (q)|2 (f) 8Li
0.0 0.5 1.0 1.5 2.0 2.5 3.0
q [fm−1]
10−6
10−5
10−4
|FM (q)|2
(g) 8B
0.0 0.5 1.0 1.5 2.0 2.5 3.0
q [fm−1]
10−5
10−4
10−3
|FM (q)|2 (h) 9Li
0.0 0.5 1.0 1.5 2.0 2.5 3.0
q [fm−1]
10−5
10−4
|FM (q)|2
Lapikas 1975
Rand 1966
V anpraet 1965
Goldemberg 1963 (i) 9Be
0.0 0.5 1.0 1.5 2.0 2.5 3.0
q [fm−1]
10−5
10−4
10−3
|FM (q)|2
(j) 9B
0.0 0.5 1.0 1.5 2.0 2.5 3.0
q [fm−1]
10−5
10−4
10−3
|FM (q)|2 (k) 9C
0.0 0.5 1.0 1.5 2.0 2.5 3.0
q [fm−1]
10−7
10−6
10−5
10−4
10−3
|FM (q)|2
LO
NLO
N2LO
N3LO
Lapikas 1978
Rand 1966
V anpraet 1965 (l) 10B
FIG. 11: Magnetic form factors computed with the NV2+3-IIb ⋆ interaction and consistent electromagnetic current.
In the figure we show the contribution of the currents up to LO (dotted blue), NLO (dashed yellow), N2LO (dot
dashed green) and N3LO (full red) in the chiral expansion. We compare our calculations with the available world
experimental data. See the text for more details.
15
0.0 0.5 1.0 1.5 2.0 2.5 3.0
q [fm−1]
10−5
10−4
10−3
|FM (q)|2
Lichtenstadt 1983
Van Niftrik 1971
Goldemberg 1963
Peterson 1962
(a) 7Li
0.0 0.5 1.0 1.5 2.0 2.5 3.0
q [fm−1]
10−5
10−4
|FM (q)|2 (b) 7Be
0.0 0.5 1.0 1.5 2.0 2.5 3.0
q [fm−1]
10−6
10−5
10−4
10−3
|FM (q)|2 (c) 8Li
0.0 0.5 1.0 1.5 2.0 2.5 3.0
q [fm−1]
10−6
10−5
10−4
|FM (q)|2
(d) 8B
0.0 0.5 1.0 1.5 2.0 2.5 3.0
q [fm−1]
10−5
10−4
10−3
|FM (q)|2 (e) 9Li
0.0 0.5 1.0 1.5 2.0 2.5 3.0
q [fm−1]
10−5
10−4
|FM (q)|2
Lapikas 1975
Rand 1966
V anpraet 1965
Goldemberg 1963 (f) 9Be
0.0 0.5 1.0 1.5 2.0 2.5 3.0
q [fm−1]
10−5
10−4
10−3
|FM (q)|2
(g) 9B
0.0 0.5 1.0 1.5 2.0 2.5 3.0
q [fm−1]
10−5
10−4
10−3
|FM (q)|2 (h) 9C
0.0 0.5 1.0 1.5 2.0 2.5 3.0
q [fm−1]
10−7
10−6
10−5
10−4
10−3
|FM (q)|2
M1
M3
M5
F ull
Lapikas 1978
Rand 1966
V anpraet 1965 (i) 10B
FIG. 12: Multipole contribution to the form factors computed with the NV2+3-IIb ∗ interaction and consistent
electromagnetic current at N3LO for nuclei with J >1. In the figure we show the contribution of the multipoles M1
(dashed blue line), M3 (dotted green), and M5 (dashed dot purple). The red line represents the full result.
16
B. Magnetic form factors and high-momentum
structure
The magnetic form factor has been computed using
the same interactions and currents used for the mag-
netic moments. In Fig. 11, we present the results for
all the nuclei showing the contributions of the currents
order-by-order for the NV2+3-IIb⋆ interaction compared
to data where available. We also include predicted mag-
netic form factors of radioactive isotopes, because while
there are presently no data for comparison, novel tech-
niques have recently made it possible to study electron
scattering from radioactive nuclei [86].
In Fig. 12 we present the multipole contributions to
the magnetic form factors for the nuclei with J >1 com-
puted with the full currents at N3LO and the NV2+3-
IIb⋆. Similar results are obtained for the other interac-
tion and current models considered.
Finally, we estimated the truncation error, limiting our
analysis to the error associated with the chiral expan-
sion of the electromagnetic currents, assuming the power
counting adopted in Refs. [6, 7, 11–14]. The calculation
of the full chiral truncation error would require an anal-
ysis of the chiral expansion in both the interaction and
currents, together; however, for the nuclear interactions
considered in this work, this is not presently possible.
In order to estimate the truncation error we use the
prescription of Ref. [87, 88] applied to
˜FM(q) =
p
2π(2J + 1)2mN
q ⟨JJ,J −J|10⟩FM(q). (22)
For this analysis, we select a value of Λb = 700 MeV and,
for the characteristic scale of momentum Q, we follow
Ref. [89] by setting it to the typical momentum trans-
fer (A− 1)/Aq , for the nucleus of mass number A. In
Fig. 13, we plot the error bands at LO (orange), NLO
(green), N2LO (blue) and N3LO(red). Note that we do
not renormalize the results to a specific value of the mag-
netic moment.
Below we discuss in detail the results obtained for each
nucleus studied.
