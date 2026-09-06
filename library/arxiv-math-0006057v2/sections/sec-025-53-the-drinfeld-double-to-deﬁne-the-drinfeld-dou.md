---
doc_id: arxiv-math-0006057v2
doc_title: "FINITE QUANTUM GROUPOIDS AND THEIR APPLICA TIONS"
section_id: sec-025-53-the-drinfeld-double-to-deﬁne-the-drinfeld-dou
section_title: "The Drinfeld double. To deﬁne the Drinfeld double D(H) of a quantum"
section_number: 5.3
pages: 19-20
source_pdf: 0006057v2.pdf
source_sha256: c881434fe9f4b04f
doc_brief: "FINITE QUANTUM GROUPOIDS AND THEIR APPLICA TIONS — W e give a survey of the theory of ﬁnite quantum groupoids (wea k Hopf algebras), including foundations of the theory and app lications to ﬁnite"
---
groupoid H, consider on the vector space ˆH op ⊗kH an associative multiplication
(φ ⊗h)(ψ ⊗g) = ψ(2)φ ⊗h(2)g⟨S(h(1)), ψ(1) ⟩⟨h(3), ψ(3) ⟩,(34)
where φ,ψ ∈ ˆH op and h,g ∈H. Then one can verify that the linear span J of the
elements
φ ⊗zh − (ε↼z )φ ⊗h, z ∈Ht,(35)
φ ⊗yh − (y ⇀ε)φ ⊗h, y ∈Hs,(36)
is a two-sided ideal in ˆH op ⊗kH. Let D(H) be the factor-algebra ( ˆH op ⊗kH)/J
and let [φ ⊗h] denote the class of φ ⊗h in D(H).
Proposition 5.3.1. D(H) is a quantum groupoid with the unit [ε ⊗ 1], and comul-
tiplication, counit, and antipode given by
∆([ φ ⊗h]) = [ φ(1) ⊗h(1)] ⊗ [φ(2) ⊗h(2)],(37)
ε([φ ⊗h]) = ⟨εt(a), φ⟩,(38)
S([φ ⊗a]) = [ S−1(φ(2)) ⊗S(h(2))]⟨h(1), φ(1) ⟩⟨S(h(3)), φ(3) ⟩.(39)
Proof. The proof is a straightforward veriﬁcation that all the structure maps are
well-deﬁned and satisfy the axioms of a quantum groupoid, which is ca rried out in
full detail in ([NTV], 6.1).
Proposition 5.3.2. The Drinfeld double D(H) has a canonical quasitriangular
structure given by
R =
∑
i
[ξi ⊗ 1] ⊗ [ε ⊗fi], ¯R =
∑
j
[S−1(ξj ) ⊗ 1] ⊗ [ε ⊗fj](40)
where {fi} and {ξi} are bases in H and ˆH such that ⟨fi, ξj ⟩ =δij.
Proof. The identities (id ⊗ ∆) R = R13R12 and (∆ ⊗ id)R = R13R23 can be written
as (identifying [( ˆH)op ⊗ 1] with ( ˆH)op and [ε ⊗H] with H) :
∑
i
ξi
(1) ⊗ξi
(1) ⊗fi =
∑
ij
ξi ⊗ξj ⊗fifj,
∑
i
ξi ⊗fi(1) ⊗fi(2) =
∑
ij
ξjξi ⊗fj ⊗fi.
The above equalities can be veriﬁed, e.g., by evaluating both sides aga inst an el-
ement a ∈ H in the third factor (resp., against φ ∈ ( ˆH)op in the ﬁrst factor), see
([Ma], 7.1.1). It is also straightforward to check that R is an intertwiner between
∆ and ∆ op and check that ¯RR = ∆(1) and R ¯R = ∆ op(1), see ([NTV], 6.2).
Remark 5.3.3. The dual quantum groupoid ˆD(H) consists of all ∑
k hk ⊗φk in
H ⊗k ˆH op such that ∑
k
(hk ⊗φk)|J = 0.
