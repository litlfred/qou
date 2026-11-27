---
doc_id: physrevd111094513
doc_title: "Lattice QCD calculation of the Compton amplitude subtraction function"
section_id: sec-001-i-introduction
section_title: "I. INTRODUCTION"
section_number: null
pages: 1-2
source_pdf: PhysRevD.111.094513.pdf
source_sha256: c05dfaef1f1c2f98
toc_source: outline
doc_brief: "Lattice QCD calculation of the Compton amplitude subtraction function — 16 sections: Lattice QCD calculation of the Com; I. INTRODUCTION; II. BACKGROUND"
---
The Compton amplitude subtraction function, S1ðQ2Þ, is
a critical component in the theoretical determination of the
proton-neutron mass difference, and a necessary quantity
for the calculation of the proton charge radius. However,
the subtraction function is not directly measurable from
experiment, and as such contributes significant theoretical
and statistical uncertainties to these quantities. In this
context, a first-principles determination of the subtraction
function could play a vital role in clarifying our under-
standing of hadron structure.
The leading electromagnetic contribution to the proton-
neutron mass difference is given by the Cottingham sum
rule [1],
δmγ
N ¼ −
i
2mp
α
ð2πÞ3
Z
d4q gμνTμν
N ðp; qÞ
Q2 −iϵ
;
ð1Þ
where TNμν is the spin-averaged forward Compton scattering
amplitude for a nucleon NðpÞ,
TNμνðp; qÞ ¼ i
Z
d4z eiq·zhNðpÞjT fVμðzÞVνð0ÞgjNðpÞi;
ð2Þ
with Vμ denoting the electromagnetic vector current and q
denoting the virtual photon 4-momentum with Q2 ¼ −q2.
The subtraction function S1ðQ2Þ, defined below, encapsu-
lates critical information about TNμν at the p · q ¼ 0 point.
An early evaluation of the Cottingham sum rule by
Gasser and Leutwyler [2] found the electromagnetic
contribution
to
the
mass
difference
to
be
δmγ
N ¼
0.76ð30Þ MeV. By contrast, a more recent evaluation [3]
proposed a significantly greater value, largely due to a
different consideration of the Compton subtraction func-
tion. As a consequence of these developments, renewed
interest was taken in the proton-neutron mass difference
[4–8]. In light of further clarification [9], focusing parti-
cularly on the treatment of the subtraction function, the
exact value of δmγ
N remains somewhat unclear. Thus a
first-principles evaluation of S1ðQ2Þ would be rather
beneficial.
Published by the American Physical Society under the terms of
the Creative Commons Attribution 4.0 International license.
Further distribution of this work must maintain attribution to
the author(s) and the published article’s title, journal citation,
and DOI. Funded by SCOAP3.
PHYSICAL REVIEW D 111, 094513 (2025)
Editors' Suggestion
2470-0010=2025=111(9)=094513(14)
Published by the American Physical Society
Similarly, the Compton amplitude is an input for
measurements of the proton charge radius from the
muonic-hydrogen Lamb shift, for which recent determi-
nations have a 7σ tension with results obtained via electron-
proton scattering [10,11]—the so-called “proton radius
puzzle” [12,13]. This has led to renewed interest in possible
systematic corrections to the muonic-hydrogen measure-
ments, including the hadronic corrections from the two-
photon exchange (TPE) [14–16], which are dependent on
the forward Compton amplitude and, consequently, the
subtraction function. Unfortunately, the Compton ampli-
tude contributes the dominant uncertainty to the hadronic
background, in large part due to S1ðQ2Þ [17–19]. Therefore
a more precise determination of the subtraction function
could also help clarify the proton radius puzzle.
In both the context of the proton-neutron mass differ-
ence, and the muonic-hydrogen Lamb shift, knowledge of
the Compton amplitude over the entire range of virtual
photon momenta is essential. The subtraction function can
be evaluated in a model independent way in the low-energy
region (Q2 ≪m2p) from effective field theory [18], and in
the high-energy region (Q2 ≫Λ2
QCD) using the operator
product expansion (OPE) [20–22]. In the intermediate Q2
region various different methods have been applied includ-
ing physically-motivated functional interpolations between
the low and high Q2 [3,5,21], and Regge model evaluations
[2,22,23]. The different methods of evaluating the unknown
behavior of the subtraction function lead to significant
differences in both the proton-neutron mass difference and
the two-photon exchange hadronic background.
In this context, a first-principles lattice QCD evaluation
of the Compton amplitude subtraction function is crucial.
Recently a lattice calculation of the subtraction function
was performed using four-point correlation functions [24],
following on from earlier work [25,26]. This calculation
was performed over the range Q2 ∈½0; 2 GeV2 at the
physical pion mass and at an alternative subtraction point
[27]. The resultant subtraction function was determined
from a combination of lattice results and experimental data.
In this paper, we determine the Compton amplitude
subtraction function over the range 1 ≲Q2 ≲16 GeV2 at
the
standard
subtraction
point
using
the
Feynman-
Hellmann technique, which has previously been used to
determine the structure function moments for the forward
[28–30] and off-forward [31,32] Compton amplitudes.
Preliminary
results
of
our
work
on
the
Feynman-
Hellmann subtraction function were first published in
Ref. [33]. Unlike Ref. [24], we do not incorporate exper-
imental data into our subtraction function calculation, but
rather present pure lattice results.
The structure of this paper is as follows: In Sec. II we
discuss in further detail the definition of the subtraction
function and its parametrization in the high-energy region.
In Sec. III we discuss the Feynman-Hellmann method used
to determine the Compton amplitude, highlighting aspects
of this implementation most relevant to the subtraction
function, and initial results. Then, in Sec. IV, we discuss our
method for correcting leading discretization artifacts in our
calculation. This is done using a lattice operator product
expansion (LOPE). Finally, in Sec. V we remove the
leading order discretization artifacts and, in doing so,
present the Compton amplitude subtraction function, and
compare it with the continuum OPE expectation.
