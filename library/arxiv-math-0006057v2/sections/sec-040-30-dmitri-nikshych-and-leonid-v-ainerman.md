---
doc_id: arxiv-math-0006057v2
doc_title: "FINITE QUANTUM GROUPOIDS AND THEIR APPLICA TIONS"
section_id: sec-040-30-dmitri-nikshych-and-leonid-v-ainerman
section_title: "DMITRI NIKSHYCH AND LEONID V AINERMAN"
section_number: 30
pages: 30-31
source_pdf: 0006057v2.pdf
source_sha256: c881434fe9f4b04f
doc_brief: "FINITE QUANTUM GROUPOIDS AND THEIR APPLICA TIONS — W e give a survey of the theory of ﬁnite quantum groupoids (wea k Hopf algebras), including foundations of the theory and app lications to ﬁnite"
---
We will denote by ˆh the Haar measure of ˆH.
Remark 7.3.2. ε is a positive functional, i.e., ε(x∗x) ≥ 0 for all x ∈H. Indeed, for
all x ∈H we have
ε(x∗x) = ε(x∗1(1))ε(1(2)1′
(2))ε(1′
(1)x) = ε(εt(x)∗εt(x)) = ⟨ˆh,ε t(x)∗εt(x) ⟩ ≥ 0,
where ˆh|Ht =ε|Ht , since ⟨ˆh,z ⟩ = ⟨ ˆεt(ˆh),z ⟩ = ⟨ˆ1,z ⟩ for all z ∈Ht.
The Haar measure provides target and source Haar conditional expectations (all
properties are easy to verify):
Et : H →Ht :Et(x) = (id ⊗ ˆh)∆( x),
Es : H →Hs :Es(x) = ( ˆh ⊗id)∆( x).
Let us introduce an element gt =Et(h)1/2 ∈Ht.
Remark 7.3.3. ([BNSz], 4.12). gt is positive and invertible, and the canonical group-
like element of H can be written as g =gtS(g−1
t ).
One can check that for a quasitriangular ∗-quantum groupoid ¯R = R∗.
Proposition 7.3.4 ([NTV], 9.3) . If H is a C∗-quantum groupoid, then D(H) is a
quasitriangular C∗-quantum groupoid.
Proof. The result follows from the fact that ˆD(H) is a C∗-quantum groupoid, which
is easy to verify using the explicit formulas from Remark 5.3.3.
Proposition 7.3.5. A quasitriangular C∗-quantum groupoid H is automatically
ribbon with the ribbon element ν =u−1g =gu−1, where u is the Drinfeld element
from Deﬁnition 5.2.7 and g is the canonical group-like element.
Proof. Since u also implements S2 (Proposition 5.2.6), ν =u−1g is central, there-
fore S(ν) is also central. Clearly, u must commute with g. The same Proposition
gives ∆( u−1) = R21R(u−1 ⊗u−1), which allows us to compute
∆( ν) = ∆( u−1)(g ⊗g) = R21R(u−1g ⊗u−1g) = R21R(ν ⊗ν).
Propositions 5.2.5 and 5.2.6 and the trace property imply that
tr(πα(u−1)) = tr( πα(R(2)S2(R(1))))
= tr( πα(S3(R(1))S(R(2))) = tr(πα(S(u−1))).
Since u−1 =νg −1 and ν is central, the above relation means that
tr(πα(ν))tr(πα(g−1)) = tr(πα(S(ν)))tr(πα(g)),
and, therefore, tr( πα(ν)) = tr( πα(S(ν))) for any irreducible representation πα,
which shows that that ν =S(ν) (cf. [EG]).
Remark 7.3.6. For a connected ribbon C∗-quantum groupoid we have:
trq(f ) = (dimHt)−1Tr V (g ◦f ), dimq(V ) = (dimHt)−1Tr V (g).
for any f ∈ End(V ), V is an H-module.
FINITE QUANTUM GROUPOIDS AND THEIR APPLICA TIONS 31
