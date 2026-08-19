---
doc_id: arxiv-1504.07260v3
doc_title: "Prepared for submission to JHEP Fricke S-duality in CHL models Daniel Persson 1 Roberto Volpato 2,3 1Fundamental Physics, Chalmers University of Technology, 412 96, Gothenburg, Swe"
section_id: sec-018-51-the-type-ii-helicity-supertrace
section_title: "The type II helicity supertrace"
section_number: 5.1
pages: 31-32
source_pdf: 1504.07260v3.pdf
source_sha256: 707cb014400a3f05
doc_brief: "Fricke S-duality in CHL models Daniel Persson 1 Roberto Volpato 2,3 1Fundamental Physics, Chalmers University of Technology, 412 96, Gothenburg, Sweden 2Theory Group, SLAC National Accelerator Laborat"
---
It is convenient to introduce a generating function, called thehelicity string partition func-
tion in [31]:
Z(υ, ¯υ) = Tr(−1)Fe2πiυJR
3 e2πi¯υJL
3qL0 ¯q
¯L0, (5.2)
where (υ, ¯υ) are chemical potentials for the left- and right-moving spacetime helicities
(JR
3 ,J L
3 ). From the generating functionZ(υ, ¯υ) one can compute the associated helicity
supertraces Bn can then be computed by taking derivatives of the partition function:
Bn =
( 1
2πi
∂
∂υ + 1
2πi
∂
∂¯υ
)n
Z(υ, ¯υ)
⏐⏐⏐
υ=¯υ=0
. (5.3)
The Bn’s should then be viewed as generating functions of the BPS-indicesΩn. For type
IIA compactiﬁed on K3×T 2, we have
ZIIA(υ, ¯υ) = ϑ1(υ/2)2 ¯ϑ1(¯υ/2)2
η2¯η2
ξ(υ)¯ξ(¯υ)
τ2η2¯η2 C(υ/2, ¯υ/2)ΘΓ2,2
η2¯η2 , (5.4)
where we deﬁned
ξ(υ) =
∞∏
n=1
(1−qn)2
(1−e2πiυqn)(1−e−2πiυqn) , (5.5)
and ΘΓ2,2 is the usual Narain theta function of the lattice. The contributions toZIIA are
as follows:
• ξ(υ)¯ξ(¯υ)
τ2η2¯η2 comes from the scalar ﬁelds along the two uncompactiﬁed transverse direc-
tions.
• C(υ/2, ¯υ/2) comes from the internalN = (4, 4) SCFT with central charge(c, ¯c) =
(6, 6) (non-linear sigma model on K3). For¯υ = 0, this is just the elliptic genus of K3.
• ΘΓ2,2
η2¯η2 comes from the oscillators and winding-momenta alongT 2.
• ϑ1(υ/2)2
η2 and its complex conjugate come from left- and right-moving fermions along
the two uncompactiﬁed transverse directions and along the torusT 2.
Since ϑ1(0) = 0, the only non-vanishing contributions to the fourth helicity traceB4 come
from terms where all four derivatives act on the theta functions. Using
ϑ′
1(0) = 2πη3 , ξ (0) = 1 , C (0, 0) = 24 (5.6)
we obtain the following expression for the fourth helicity supertrace:
B4 =
( 1
2πi
∂
∂υ + 1
2πi
∂
∂¯υ
)4
ZIIA(υ, ¯υ)
⏐⏐⏐
υ=0
= 6
( 1
2πi
∂
∂υ
)2( 1
2πi
∂
∂¯υ
)2
ZIIA(υ, ¯υ)
⏐⏐⏐
υ=0
= 3
2C(0, 0)ΘΓ2,2
τ2
= 36ΘΓ2,2
τ2
.
– 30 –
