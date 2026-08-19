---
doc_id: arxiv-1511.00400v2
doc_title: "Reidemeister torsion, hyperbolic three-manifolds, and character varieties Joan Porti ∗"
section_id: sec-018-431-generic-cohomology-on-the-distinguished-comp
section_title: "Generic cohomology on the distinguished component"
section_number: 4.3.1
pages: 29-30
source_pdf: 1511.00400v2.pdf
source_sha256: 6cb493049394ce3a
doc_brief: "Reidemeister torsion, hyperbolic three-manifolds, and character varieties Joan Porti ∗ — This is a survey on Reidemeister torsion for hyperbolic thre e-manifolds of ﬁnite volume."
---
Some cohomology preliminaries are required before deﬁning the tors ion of Symk1,k2
as function on X0(M 3). To simplify, use the notation
ρk1,k2 ∶= Symk1,k2 ○ρ
for any representation ρ∶ π1M 3 → SL2(C).
Deﬁnition 4.8. A character χ ∈X0(M 3) is called (k1, k2)-exceptional if there
exists a representation ρ ∈hom(π1M 3, SL2(C)) with character χρ = χ such that
H 0(M 3; ρk1,k2) ≠0.
The set of (k1, k2)-exceptional characters is denoted by E k1,k2.
If a character is irreducible, then the set of representations with this char-
acter is precisely a conjugation orbit, but for reducible character s there may be
representations with the same characters that are not conjuga te.
Notice that in Proposition 3.16 we have shown that E 1,0 consist of the trivial
character, when it belongs to X0(M 3) (hence E 1,0 = ∅ when b1(M 3) = 1).
Lemma 4.9. If k1 ≠k2, then a (k1, k2)-exceptional character is reducible. In
particular the (k1, k2)-exceptional set Ek1,k2 is a ﬁnite subset of X0(M 3).
The proof of this lemma is provided in Appendix B (Lemma B.9).
For further results, the following deﬁnition is convenient.
Deﬁnition 4.10. A subset of X0(M 3) is generic if it is non empty and Zariski
open. Here the ground ﬁeld is assumed to be C when working with an holomor-
phic representation Sym k, and R for Sym k1,k2 when k2 ≠0.
For the generic behavior of other cohomology groups, one must dis tinguish
the case where k1 or k2 is odd from the case they are both even. All proofs are
postponed to Appendix B.
Proposition 4.11. Let M 3 be orientable, hyperbolic and with one cusp. As-
sume k1 ≠k2.
(a) If k1 or k2 is odd, then
/brac⟩l⟩ft.alt1χρ ∈X0(M 3) /divid⟩s.alt0 ρk1,k2 is acyclic /brac⟩right.alt1
is generic.
(b) If both k1 and k2 are even, then
/brac⟩l⟩ft.alt1χρ ∈X0(M 3) /divid⟩s.alt0 dim Hi(M 3; ρk1,k2) = 1 for i = 1, 2 and 0 otherwise /brac⟩right.alt1
is generic.
29
When k1 and k2 are even, we need to discuss the choice of basis in homology
and perhaps we still need to remove a Zarsiki closed subset. We sha ll consider,
for k1 and k2 even,
Fk1,k2 = /brac⟩l⟩ft.alt1χρ ∈X0(M 3) /divid⟩s.alt0 dim H 0(T 2; ρk1,k2) ≠1/brac⟩right.alt1 ∪ Ek1,k2 , (30)
which is Zarsiki closed subset of X0(M 3) (over C for k2 = 0, over R otherwise).
In particular it is ﬁnite when k2 = 0 or k1 = 0.
Lemma 4.12. Let T 2 denote the peripheral torus. If both k1 and k2 are even,
then Fk1,k2 is a Zarsiki closed subset of X0(M 3) (over C for k2 = 0 or k1 = 0,
over R otherwise). In particular it is ﬁnite when k2 = 0 or k1 = 0.
Consider the cap product
∩∶ H 0(T 2; ρk1,k2) × Hi(T 2; C) → Hi(T 2; ρk1,k2).
It can be described as follows. Choose a ∈H 0(T 2; ρk1,k2 ), a ≠0, and view it
as an element of C(n1+1)(n2+1) invariant by the action of ρk1,k2(π1T 2). Any
element in Hi(T 2; C) is represented by a simplicial cycle: z ∈C∗(K; C) with
∂z = 0 (here K is a triangulation of T 2). Choose a lift of z to the universal
covering, ˜z ∈C∗( ̃K; C), then a ⊗ ˜z ∈Ci(K; ρk1,k2 ) is a cocycle and
a ∩ [z] = [a ⊗ ˜z], (31)
where the brackets denote the class in homology.
In the next proposition [T 2] ∈H2(T 2; Z) denotes a fundamental class, ⟨⋅⟩
the linear span, and i∶ T 2 → M 3 the inclusion.
Proposition 4.13. Let k1 ≠k2 be even integers. For 0 ≠a ∈H 0(T 2; ρk1,k2 ) and
0 ≠γ ∈H1(T 2; C), the set
/brac⟩l⟩ft.alt1χρ ∈X0(M 3) /divid⟩s.alt0 ⟨i∗(a ∩ γ)⟩ = H1(M 3; ρk1,k2) and
⟨i∗(a ∩ [T 2])⟩ = H2(M 3; ρk1,k2 )/brac⟩right.alt1
is generic.
