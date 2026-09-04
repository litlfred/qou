---
doc_id: arxiv-0911.3569v1
doc_title: "MULTIVARIATE STABLE POLYNOMIALS: THEORY AND APPLICATIONS"
section_id: sec-016-71-negative-correlation-and-negative-association
section_title: "Negative correlation and negative association."
section_number: 7.1
pages: 19-20
source_pdf: 0911.3569v1.pdf
source_sha256: 4e7c15c9724fb453
doc_brief: "MULTIVARIATE STABLE POLYNOMIALS: THEORY AND APPLICATIONS — Univariate polynomials with only real roots – while special – do occur often enough that their properties can lead to interesting"
---
distribution ϕ on Ω. An event E is any subset of Ω. The probability of the event
E is Pr[ E] = ∑
S∈Eϕ(S). An event E is increasing if whenever S≤ S′ in Ω and
S∈ E, then S′∈ E. For example, if K is any subset of Λ and EK is the event that
all sites in K are occupied, then EK is an increasing event. Notice that this event
has the form EK = E′×{ 0, 1}ΛrK for some event E′⊆{ 0, 1}K. Two events E
and F are disjointly supported when one can partition Λ = A∪B with A∩B = ∅
and E = E′×{ 0, 1}B and F ={0, 1}A× F′ for some events E′ ⊆ {0, 1}A and
F′⊆{ 0, 1}B.
A probability distribution on Ω is negatively associated (NA) when Pr[ E∩ F]≤
Pr[E]· Pr[F] for any two increasing events that are disjointly supported. It is
negatively correlated (NC) when Pr[E{i,j}]≤ Pr[E{i}]· Pr[E{j}] for any two distinct
sites{i,j}⊆ Λ. Clearly NA implies NC.
It is useful to ﬁnd conditions under which NC implies NA, since NC is so much
easier to check. The following originates with Feder and Mihail, but many others
have contributed their insights – see Section 4.2 of [7]. The partition function of
20 DAVID G. WAGNER
anyϕ : Ω→ R is the real multiaﬃne polynomial
Z(ϕ) =Z(ϕ; x) =
∑
S∈Ω
ϕ(S)xS
in R[x]MA. If ϕ is nonzero and nonnegative, then for anya∈ RΛ with a> 0, this de-
ﬁnes a probability distribution ϕa : Ω→ [0, 1] by setting ϕa(S) = ϕ(S)aS/Z(ϕ; a)
for all S∈ Ω.
Feder-Mihail Theorem (Theorem 4.8 of [7]) . Let S be a class of nonzero non-
negative functions satisfying the following conditions.
(i) Each ϕ∈ S has domain{0, 1}Λ for some ﬁnite set Λ = Λ(ϕ).
(ii) For each ϕ∈ S, Z(ϕ) is a homogeneous polynomial.
(iii) For eachϕ∈ S and i∈ Λ(ϕ), Z(ϕ)|xi=0 and ∂iZ(ϕ) are partition functions of
members of S.
(iv) For each ϕ∈ S and a∈ RΛ(ϕ) with a> 0, ϕa is NC.
Then for every ϕ∈ S and a∈ RΛ(ϕ) with a> 0, ϕa is NA.
