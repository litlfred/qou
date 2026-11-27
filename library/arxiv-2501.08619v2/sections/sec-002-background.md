---
doc_id: arxiv-2501.08619v2
doc_title: "Lattice QCD calculation of the Compton amplitude subtraction function"
section_id: sec-002-background
section_title: "Background"
section_number: null
pages: 2-3
source_pdf: 2501.08619v2.pdf
source_sha256: 29ce7af1791830fb
toc_source: outline
doc_brief: "Lattice QCD calculation of the Compton amplitude subtraction function — 16 sections: Front matter; Lattice QCD calculation of the Com; Introduction"
---
In this context, a first-principles lattice QCD evalu-
ation of the Compton amplitude subtraction function
is crucial.
Recently a lattice calculation of the sub-
traction function was performed using four-point cor-
relation functions [24], following on from earlier work
[25, 26]. This calculation was performed over the range
Q2 ∈[0, 2] GeV2 at the physical pion mass and at an
alternative subtraction point [27]. The resultant sub-
traction function was determined from a combination
of lattice results and experimental data.
In this paper, we determine the Compton amplitude
subtraction function over the range 1 ≲Q2 ≲16 GeV2
at the standard subtraction point using the Feynman-
Hellmann technique, which has previously been used to
determine the structure function moments for the for-
ward [28–30] and off-forward [31, 32] Compton ampli-
tudes. Preliminary results of our work on the Feynman-
Hellmann subtraction function were first published in
Ref. [33]. Unlike Ref. [24], we do not incorporate exper-
imental data into our subtraction function calculation,
but rather present pure lattice results.
The structure of this paper is as follows: In Section
II we discuss in further detail the definition of the sub-
traction function and its parameterisation in the high-
energy region. In Section III we discuss the Feynman-
Hellmann method used to determine the Compton am-
plitude, highlighting aspects of this implementation
most relevant to the subtraction function, and initial
results. Then, in Section IV, we discuss our method for
correcting leading discretisation artefacts in our calcu-
lation. This is done using a lattice operator product
expansion (LOPE). Finally, in Section V we remove the
leading order discretisation artefacts and, in doing so,
present the Compton amplitude subtraction function,
and compare it with the continuum OPE expectation.
II.
BACKGROUND
Our starting point is the forward virtual Compton
amplitude for a proton, as shown in Eq. (2). This am-
plitude describes the process of photon-proton scatter-
ing, γ∗(q)p(p) →γ∗(q)p(p)—see Fig. 1. By performing
the standard tensor decomposition, the Compton am-
q
q
p
p
Figure 1. The diagram for proton forward Compton scat-
tering, γ∗(q)p(p) →γ∗(q)p(p).
plitude can be written in the form [29]
Tµν =

−gµν + qµqν
q2

T1(ω, Q2)
+
1
p · q

pµ −p · q
q2 qµ
 
pν −p · q
q2 qν

T2(ω, Q2),
(3)
where ω = 2p · q/Q2 and Q2 = −q2. The alternative
decomposition put forward in Ref. [22] could provide an
opportunity for future work.
The two Compton amplitude structure functions,
T1,2, satisfy the following dispersion relations [34, 35]:
T1(ω, Q2) = T1(0, Q2) + 2ω2
π
Z ∞
1
dω′
ImT1(ω′, Q2)
ω′(ω′2 −ω2 −iϵ),
T2(ω, Q2) = 2ω
π
Z ∞
1
dω′ ImT2(ω′, Q2)
ω′2 −ω2 −iϵ.
(4)
Crucially, the imaginary parts of T1,2 can be determined
from deep-inelastic scattering.
On the other hand,
T1(0, Q2) can not be experimentally accessed from in-
clusive processes. This is the subtraction function:
S1(Q2) ≡T1(0, Q2).
(5)
Although the subtraction function is not experimentally
accessible, it can be estimated in both the low Q2 and
high Q2 regions.
For Q2 ≪m2
p the subtraction function has been com-
puted in a variety of formalisms, including effective field
theory calculations [2–6, 17–19, 23, 36–39]. These cal-
culations have sizeable errors and are not always con-
sistent with one another [22].
In the region Q2 ≫Λ2
QCD the subtraction function
can be evaluated model-independently using the opera-
tor product expansion (OPE). Such an expansion is per-
formed in powers of m2
p/Q2, with the predicted asymp-
totic behaviour
S1(Q2) ∼m2
p
Q2 ,
for
Q2 ≫Λ2
QCD.
(6)
Collins [20] originally determined the leading-order
m2
p/Q2 contribution from the OPE. Hill and Paz later
3
corrected this calculation, again only evaluating the
leading m2
p/Q2 term. Up to gluon contributions which
are suppressed by αs, the OPE result can be written
[21]
SOPE
1
(Q2) = 4m2
p
Q2
X
q
Q2
q

⟨x⟩q −mq
mp
gq
S

,
(7)
where ⟨x⟩q is the second parton distribution function
moment (i.e. the momentum fraction), mq is the quark
mass and gq
S is the scalar charge—all for a quark of
flavour q and charge Qq.
Note that the expression in Eq. (7) is only the leading-
order in m2
p/Q2 contribution to the OPE prediction.
There are higher order terms in m2
p/Q2 that may con-
tribute significantly, especially for Q2 on the threshold
of the perturbative region.
At low energies, in addition to the OPE contribution,
there is also an elastic contribution to the subtraction
function [3, 5, 9, 40]
