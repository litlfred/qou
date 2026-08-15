---
doc_id: arxiv-1810.11563v1
doc_title: "Three Lectures on Complexity and Black Holes Leonard Susskind"
section_id: sec-017-122-rindler-time-and-cv
section_title: "Rindler Time and CV"
section_number: 12.2
pages: 41-43
source_pdf: 1810.11563v1.pdf
source_sha256: 8e17ac8b91bc3cc9
doc_brief: "Three Lectures on Complexity and Black Holes Leonard Susskind — This is the written version of three lectures on complexity and black holes given at PiTP 2018 summer program entitled ”From Qubits to"
---
The standard architecture for quantum circuits (explained in Lecture I) is illustrated in
ﬁgure 21.
Figure 21
We assume that the circuit comes equipped with a clock, and in each time-step K/2
gates act. For sub-exponential time the number of gates in a circuit corresponds to the
40
complexity14C of the unitary operator prepared by the circuit satisﬁes,
dC
∂τ = K
2 (12.38)
or, assuming K∼S,
dC
∂τ ∼S. (12.39)
If black holes can be viewed as quantum circuits one may ask what the time-coordinate
τ corresponds to on the black hole side. One hint is that since complexity and entropy
are dimensionless, τ is also dimensionless. The ordinary Schwarzschild coordinate t of a
black hole has dimensions of time and therefore cannot be the same as τ. There is however
a universal dimensionless time for all non-extremal black holes, namely the Rindler time.
The near-horizon geometry has the universal form,
ds2 =−ρ2dτ 2 +dρ2 +r(ρ)2dΩ2 (12.40)
whereρ is proper distance from the horizon andτ is a hyperbolic boost angle. The natural
candidate for the circuit time for a black hole is the Rindler time. For now let’s accept
this identiﬁcation but later, in section 14.2 I will give a precise quantitative argument for
identifying circuit time with Rindler time.
Thus I will therefore use the same symbol τ for circuit time, and for Rindler time. We
may therefore assume that in the context of black hole evolution the complexity grows
according to 12.39 with τ being Rindler time.
An asymptotic observer at inﬁnity sees rate of computation red-shifted. It is a universal
fact for all non-extremal black holes, that the asymptotic time t is related to Rindler time
by
τ = 2πt
β = 2πTt. (12.41)
It follows that the rate of computation as seen from inﬁnity, is
dC
dt =ST. (12.42)
14This is the no-collisions assumption discussed at length in Lecture I. It is expected to be correct for
sub-exponential time.
41
Compare this with 12.37 and one sees that the quantity C is in fact the complexity C.
Accordingly 12.35 may be written in the form,
C = V
Glads
. (12.43)
This formula connecting complexity and the volume of the the wormhole is the called CV
correspondence. It is one of two versions of the complexity-geometry correspondence, the
other being complexity-action formulation. Time will not permit me to go over the CA
correspondence, but there are many papers that you can consult.
Let me summarize and emphasize two points:
1. Circuit time, measured in steps, corresponds to the Rindler time of a black hole.
Now repeat and memorize:
Circuit time, measured in steps, corresponds to the Rindler time of a black hole.
2. Complexity is proportional to the wormhole volume through 12.43
Of course this latter point is a conjecture; it was not derived from ﬁrst-principles. The
argument is due to Sherlock Holmes; I quote the great detective: “When you have excluded
the impossible whatever remains, however improbable, must be the truth.” We can and
will subject item 2 to rigorous testing.
