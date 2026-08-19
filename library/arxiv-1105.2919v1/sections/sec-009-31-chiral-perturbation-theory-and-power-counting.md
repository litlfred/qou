---
doc_id: arxiv-1105.2919v1
doc_title: "Chiral effective field theory and nuclear forces"
section_id: sec-009-31-chiral-perturbation-theory-and-power-counting
section_title: "Chiral perturbation theory and power counting"
section_number: 3.1
pages: 16-18
source_pdf: 1105.2919v1.pdf
source_sha256: 6d94496f2093ddd0
doc_brief: "Chiral effective field theory and nuclear forces — We review how nuclear forces emerge from low-energy QCD via chiral eﬀective ﬁeld theory. The presentation is accessible to the non-specialist."
---
Eﬀective Lagrangians have inﬁnitely many terms, and an unlimited number of Feynman graphs can be
calculated from them. Therefore, we need a scheme that makes the theory manageable and calculable. This
scheme which tells us how to distinguish between large (important) and small (unimportant) contributions
is chiral perturbation theory (ChPT).
In ChPT, graphs are analyzed in terms of powers of small external momenta over the large scale:
(Q/Λχ)ν, where Q is generic for a momentum (nucleon three-momentum or pion four-momentum) or a
16
pion mass and Λχ∼ 1 GeV is the chiral symmetry breaking scale (hadronic scale, hard scale). Determining
the power ν has become known as power counting.
For the moment, we will consider only so-called irreducible graphs; the problem of reducible or iterative
diagrams and their relevance for the NN system will be discussed later (cf. Section 4.5). By deﬁnition, an
irreducible graph is a diagram that cannot be separated into two by cutting only nucleon lines. Following
the Feynman rules of covariant perturbation theory, a nucleon propagator is Q−1, a pion propagator Q−2,
each derivative in any interaction is Q, and each four-momentum integration Q4. This is also known as
naive dimensional analysis. Applying then some topological identities, Weinberg obtained for the power of
an irreducible diagram involving A nucleons [50–52]
νW = 4−A− 2C + 2L +
∑
i
∆i (3.1)
with
∆i≡di + ni
2 − 2, (3.2)
whereC denotes the number of separately connected pieces and L the number of loops in the diagram; di is
the number of derivatives or pion-mass insertions andni the number of nucleon ﬁelds (nucleon legs) involved
in vertexi; the sum runs over all vertices i contained in the diagram under consideration. Note that ∆ i≥ 0
for all interactions allowed by chiral symmetry. Purely pionic interactions have at least two derivatives
(di≥ 2,ni = 0); interactions of pions with a nucleon have at least one derivative ( di≥ 1,ni = 2); and
nucleon-nucleon contact terms (ni = 4) have di≥ 0. This demonstrates how chiral symmetry guarantees a
low-energy expansion.
The Weinberg formula Eq. (3.1) works well for connected diagrams withA≤ 2 nucleons and any number
of pions, but there are problems when applied in systems with A≥ 3.
To illustrate the problem, consider one-pion exchange (L = 0, ∆i = 0) between two nucleons in anA = 2
system (C = 1) which yields νW = 0. Now, when the same interaction occurs in an A = 3 environment,
then C = 2, since one nucleon is not interacting, and Eq. (3.1) produces νW =−3. The reason for this
result is that, by widespread convention [115], particle states are normalized to Dirac δ-functions,
⟨p′|p⟩ =δ3(⃗ p−⃗ p′), (3.3)
which carry dimension Q−3. A nucleon line passing through a diagram without interaction is represented
by such a three-momentum-conserving δ-function.
The above-illustrated A-dependence of the power νW is undesirable. As indicated, the reason for the
problem is the dimension (−3) introduced for each nucleon through the normalization Eq. (3.3). Therefore,
to ﬁx the problem, we add (+3 A) to Eq. (3.1) and subtract 6 to have the A = 2 case unaltered. Thus, we
introduce the new power ν =νW + 3A− 6, which reads explicitly,
ν =−2 + 2A− 2C + 2L +
∑
i
∆i. (3.4)
This deﬁnition of the power ν will be applied throughout this report. It is also what is used in other
works [107]. Another way to get the formula Eq. (3.4) is to deﬁne ν as the diﬀerence between νW and the
smallest possible power, νmin: ν =νW−νmin. The minimal power νmin is obtained from Eq. (3.1) for the
case of no loops ( L = 0), ∆i = 0 for all vertices, and the maximal number of separately connected pieces,
which is C =A− 1 if at least two nucleons interact; thus, νmin = 6− 3A.
Notice that, even though A still appears in Eq. (3.4), the formula is essentially A independent: when
a non-interacting nucleon is added, A and C go up by one, which cancels. From the above derivation, it
should also be clear that Eq. (3.4) is suitable only for systems with A≥ 2 nucleons while Eq. (3.1) may be
used for connected graphs with A≤ 2.
An alternative method for developing a reasonable power formula has been presented by Friar [126],
who considers the expectation value of an m-nucleon operator (m≤ A) in A-nucleon space. Working in
conﬁguration space generates additional phase-space factors of power 3( A− 1) to be added to Eq. (3.1).
17
Thus, Friar’s power isνF =νW + 3A− 3 =ν + 3. The additional power of three by which Friar diﬀers from
Eq. (3.4) is due to an additional momentum-space integration that converts the units of a momentum-space
potential into units of energy, which is reasonable. Finally, we note that normalizing the nucleon states in
a box to a Kronecker-δ (instead of using the Dirac δ-function normalization of the continuum) should lead
to Eq. (3.4) in a straightforward fashion.
In any case, the most important observation from power counting is that the powers are bounded from
below and, speciﬁcally, ν≥ 0. This fact is crucial for the convergence of the low-momentum expansion.
Moreover, the power formula Eq. (3.4) allows to predict the leading orders of connected multi-nucleon
forces. Consider a m-nucleon irreducibly connected diagram ( m-nucleon force) in an A-nucleon system
(m≤ A). The number of separately connected pieces is C = A−m + 1. Inserting this into Eq. (3.4)
together with L = 0 and ∑
i ∆i = 0 yields ν = 2m− 4. Thus, two-nucleon forces ( m = 2) start at ν = 0,
three-nucleon forces (m = 3) at ν = 2 (but they happen to cancel at that order), and four-nucleon forces at
ν = 4 (they don’t cancel). More about this in the next sub-section and Section 5.
For later purposes, we note that for an irreducible NN diagram (A = 2, C = 1), the power formula
collapses to the very simple expression
ν = 2L +
∑
i
∆i. (3.5)
In summary, the chief point of the ChPT expansion is that, at a given order ν, there exists only a ﬁnite
number of graphs. This is what makes the theory calculable. The expression ( Q/Λχ)ν+1 provides a rough
estimate of the relative size of the contributions left out and, thus, of the accuracy at order ν. In this sense,
the theory can be calculated to any desired accuracy and has predictive power.
