---
doc_id: arxiv-2501.08619v2
doc_title: "Lattice QCD calculation of the Compton amplitude subtraction function"
section_id: sec-007-free-fermion
section_title: "Free fermion"
section_number: null
pages: 7-7
source_pdf: 2501.08619v2.pdf
source_sha256: 29ce7af1791830fb
toc_source: outline
doc_brief: "Lattice QCD calculation of the Compton amplitude subtraction function — 16 sections: Front matter; Lattice QCD calculation of the Com; Introduction"
---
a range of q values.
Free fermion
To investigate the effectiveness of the LOPE correc-
tion ∆S1, we briefly consider the simple case of the
free fermion. Applying simple QED, we can derive an
analytic form of the forward Compton amplitude Tµν
which, under the conditions µ = ν = 3 and p3 = q3 = 0,
reduces to T33 = 2ω2/(1−ω2). At the subtraction point,
ω = 0, the amplitude for a free fermion (ff) therefore
vanishes. Setting Simp
1
= 0, Eq. (18) then reduces to:
SL (ff)
1
(Q2) = −∆S(ff)
1
,
(19)
where SL (ff)
1
(Q2) is the free fermion lattice calculation
of the subtraction function, which can be determined
from Feynman-Hellmann using a single perturbed prop-
agator as in Eq. (9) (i.e. we do not form multiple Wick
contractions as in a hadron), and using unit gauge fields,
Uµ = I, in the fermion matrix. We perform this calcu-
lation with a lattice size N 3
L × NT = 323 × 64, and
for values of the hopping parameter, κ, in the range
κ = 0.0956−0.1248, which correspond to dimensionless
bare masses in the range am = 0.0064−0.5. The results
of this calculation are shown as the hollow data points
in Fig. 4. As for ∆S(ff)
1
, up to higher order corrections
in a, it takes the form
∆S(ff)
1
= CW (q, m0)2(am0)gbare
S
(20)
where m0 is the free fermion mass and we have taken
gbare
S
= (1 + am0)−1 and r = 1.
In Fig. 4 we plot the FH results, the discretisation
artefact in Eq. (20) (solid curve) and our 2006 result
(broken curve). We observe that, as a function of am0,
the LOPE agrees well with the numerical Feynman-
Hellmann results up to am0 ≈0.5.
Comparing this
0
5
10
15
Q2 [GeV2]
0.90
0.95
1.00
CW(q, m0)
a = 0.074 fm
a = 0.068 fm
a = 0.058 fm
0.00
0.02
0.04
0.06
0.08
a [fm]
1
2
3
2amp · Z2
V gS
u
d
Figure 6. The two components of the leading lattice artefact
to our calculation as in Eq. (16). The upper panel shows
CW (q, m0) for each kinematic point reported in Table II,
while the lower panel depicts Z2
V ⟨p| ¯ψψ|p⟩. The total lattice
artefact is given by ∆S1 = CW (q, m0)2(amp)Z2
V gS.
LOPE with our 2006 LOPE result (which did not in-
clude the bare mass contribution) also suggests an im-
provement in the correction. Similarly, in Fig. 5 we see
a strong agreement between SL (ff)
1
(Q2) and ∆S(ff)
1
as
a function of q2. For the smallest am0 (κ = 0.1248)
in particular, the agreement is excellent, and also holds
to large q2. It’s also interesting to note that, despite
minor fluctuations in ∆S(ff)
1
, the discretisation artefacts
for the greater am0 results are largely q2-independent.
For the free fermion we expect a strong agreement
between the LOPE and numerical Feynman-Hellmann
results, as SL (ff)
1
(Q2) vanishes in the continuum. There-
fore, the agreement of these results suggest that the
LOPE is a good parameterisation of our dominant dis-
cretisation artefacts, both in terms of the larger O(am0)
artefacts as well as the smaller O(aq) effects.
