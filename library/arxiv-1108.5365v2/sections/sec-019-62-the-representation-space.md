---
doc_id: arxiv-1108.5365v2
doc_title: "Representation of the Quantum Plane, its Quantum"
section_id: sec-019-62-the-representation-space
section_title: "The representation space"
section_number: 6.2
pages: 48-51
source_pdf: 1108.5365v2.pdf
source_sha256: 000961ede2234231
doc_brief: "Representation of the Quantum Plane, its Quantum — We give complete detail of the description of the GNS represe ntation of the quantum plane A and its dual ˆA as a von Neumann algebra."
---
We introduce the transformations such that A acts on H canonically, and ˆA acts
on ˆH canonically. We will use capital letter to denote the transformed fu nction.
All the new Hilbert spaces are L2(R× R).
Deﬁnition 6.2. We deﬁne T :H−→H rep by
T :f (s,t )↦→
∫
R
f (α,t−s + iQ
2 )e2πiαsdα, (6.12)
T −1 :F (s,t )↦→
∫
R
F (α,t +α− iQ
2 )e−2πiαsdα, (6.13)
or simply T = (t↦→t−s)◦F −1
s ◦ (t↦→t + iQ
2 ).
Similarly we deﬁne ˆT : ˆH−→ ˆHrep by
ˆT : ˆf (s,t )↦→
∫
ˆf (α,t−s + iQ
2 )e−2πiαteπQαdα, (6.14)
48
ˆT −1 : ˆF (s,t )↦→
∫
ˆF (α,t +α− iQ
2 )e2πis(α+t)dα, (6.15)
or simply ˆT = (t↦→t−s)◦F s◦ (t↦→t + iQ
2 )◦e−2πist.
Proposition 6.3. Under the transformations, both the spaces Hrep and ˆHrep carry
the usual inner product with respect to the standard Lebesgu e measure:
⟨F (s,t ),G (s,t )⟩ =
∫
R
∫
R
G(s,t )F (s,t )dsdt. (6.16)
Proposition 6.4. Under the transformations, the action of A onHrep is given by
A =e2πbs, B =e2πbps, (6.17)
and the action of ˆA on ˆHrep is given by
ˆA =e−2πbs, ˆB =e2πbps. (6.18)
Proof. Let us demonstrate the use of transformation rule for say, the o perator B.
The rest is similar. Recall that B acts on H as e2πbse−2πbpt. Hence under the
transformation it becomes
e2πbse−2πbpt ↦→t↦→t+ iQ
2
e2πbse−2πbpt
↦→F −1
s
e2πbpse−2πbpt
↦→t↦→t−s e2πbps.
As a corollary, we have
Corollary 6.5. As a representation of A we have
H≃H irr⊗L2(R), (6.19)
whereHirr is the canonical irreducible representation (1.2) ofA on L2(R).
Let us also note that
Proposition 6.6. The product of two elements in A induces a twisted product on
H by
F·G =T (T −1(F )·T −1(G)) =
∫
R
F (s,τ )G(τ,t )dτ. (6.20)
We can do the same analysis to the dual space:
49
Proposition 6.7. Under the transformations, the action of ˆA onHrep is given by
ˆA =e2πb(ps+pt), ˆB =Gb(Q
2 +is−it)◦e2πb(pt+s)◦Gb(Q
2 +is−it)−1, (6.21)
and the action of A on ˆHrep is given by
A =e2πb(ps+pt),B =Gb(Q
2−is +it)−1◦e2πb(pt−s)◦Gb(Q
2−is +it). (6.22)
Remark 6.8. Note that the action of A on ˆH is obtained by the ξ transformation.
Moreover, recall that Gb( Q
2 +is) is unitary, hence the action above is still positive.
Finally we will need to describe the action of the modular conjugation J and ˆJ
that are crucial in the construction of the multiplicative unitary for the quantum
double.
Proposition 6.9. The action of J and ˆJ onHrep is given by
J :F (s,t )↦→
F (t,s ), (6.23)
ˆJ :F (s,t )↦→F (−s,−t)eπis2−πit2
νi/8, (6.24)
whereν =e−2πQ2
.
Similarly, the action of ˆJ on ˆHrep is also given by
ˆJ : ˆF (s,t )↦→ˆF (t,s ), (6.25)
while the action of J on ˆHrep is given by
J : ˆF (s,t )↦→ˆF (−s,−t)eπit2−πis2
ν−i/8. (6.26)
Proposition 6.10. The action of AdJ onA is given by:
J(x)J = ˆR∗(x∗), (6.27)
where ˆR∗ is an anti-homomorphism given by
ˆR∗(A) = ˆA∗, ˆR∗(B) = ˆB∗, (6.28)
where
ˆA∗ =e2πbt, ˆB∗ =e−2πbpt. (6.29)
The action of Ad ˆJ on ˆA is given by:
ˆJ(y) ˆJ =R∗(y∗), (6.30)
whereR∗ is an anti-homomorphism given by
R∗( ˆA) = A∗, R ∗( ˆB) = B∗, (6.31)
where
A∗ =e−2πbt, B ∗ =e−2πbpt. (6.32)
50
Corollary 6.11. J◦A◦ J commutes withA as operators on Hrep, and similarly
ˆJ◦ ˆA◦ ˆJ commutes with ˆA as operators on ˆHrep, which veriﬁes Theorem 2.11.
