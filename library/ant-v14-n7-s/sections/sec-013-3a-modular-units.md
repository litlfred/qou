---
doc_id: ant-v14-n7-s
doc_title: "Algebra & Number Theory Volume 14 No. 7 msp"
section_id: sec-013-3a-modular-units
section_title: "3A. Modular units"
section_number: null
pages: 16-17
source_pdf: ant-v14-n7-s.pdf
source_sha256: ab695eddd565addf
---
YQ(U). In this section, we work exclusively overQ, so we shall drop the subscriptQ from the notation. As
is well known, the manifolds Y(U) are naturally the complex points of algebraic varieties deﬁned over Q.
Deﬁnition 3.1. A modular unit on Y(U) is an element of O(Y(U))×, that is, a regular function on Y(U)
with no zeros or poles. (This corresponds to a rational function on the compactiﬁcation X(U) whose
divisor is supported on the cusps).
Modular units are motivic in the sense that there arerealisations of modular units in various cohomology
theories. In particular, to a modular unit φ∈ O(Y1(N))× one can attach:
• its de Rham realisation CdR(φ)∈ H1
dR(Y1(N), Q), which is the class of the differential form
d logφ= dφ
φ ;
• its Betti realisation C(φ)∈ H1(Y1(N), Z), which is the pullback along φ: Y1(N)(C)→ C× of the
generator C of H1(C×, Z)∼= Z that pairs to 1 with the homology class of a positively oriented loop
around 0.
p-adic Asai L-functions of Bianchi modular forms 1683
These are closely related:
Proposition 3.2. The canonical comparison isomorphism
H1(Y1(N), Z)⊗Z C ∼=−→H1
dR(Y1(N), Q)⊗Q C
maps C(φ) to 1/(2πi)CdR(φ).
Proof. The comparison isomorphism identiﬁes the de Rham cohomology class of an n-formω with the
Betti cohomology class mapping an n-simplexδ to
∫
δω. By construction, this isomorphism is compatible
with the pullback maps in the two cohomology theories attached to a smooth map of manifolds.
In our case, the modular unitφ gives a map Y1(N)(C)→ C×. By deﬁnition, C(φ) is the pullback byφ
of the generator C of H1(C×, Z); and CdR(φ) is the pullback of the class of the differential dT
T , where T
is the coordinate on C. If δ denotes a positively oriented loop around 0, then
∫
δ
dT
T = 2πi. Since C pairs
to 1 withδ (by deﬁnition), the result follows. □
Remark. It is conventional to “normalise away” the factor of 2πi by deﬁning C(φ) as an element
of H1(Y1(N), Z(1)), where Z(1)= 2πi· Z⊂ C. However, this formalism does not work well when
considering the cohomology of nonalgebraic manifolds, so we shall not use it here.
