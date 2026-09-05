---
doc_id: arxiv-math-0006057v2
doc_title: "FINITE QUANTUM GROUPOIDS AND THEIR APPLICA TIONS"
section_id: sec-015-12-dmitri-nikshych-and-leonid-v-ainerman
section_title: "DMITRI NIKSHYCH AND LEONID V AINERMAN"
section_number: 12
pages: 12-12
source_pdf: 0006057v2.pdf
source_sha256: c881434fe9f4b04f
doc_brief: "FINITE QUANTUM GROUPOIDS AND THEIR APPLICA TIONS — W e give a survey of the theory of ﬁnite quantum groupoids (wea k Hopf algebras), including foundations of the theory and app lications to ﬁnite"
---
Proof. Proposition 2.2.1(iii) implies that the H-Hopf module structure on M is well
deﬁned, and it is easy to check that α is a well deﬁned homomorphism of H-Hopf
modules. We will show that
β :M →N ⊗HtH :m ↦→(m(0) ·S(m(1))) ⊗m(2)(23)
is an inverse of α. First, we observe that m(0) ·S(m(1)) ∈N for all m ∈M , since
ρ(m(0) ·S(m(1))) = ( m(0) ·S(m(3))) ⊗m(1)S(m(2))
= ( m(0) ·S(1(2)m(1)) ⊗S(1(1))
= ( m(0) ·S(m(1))1(1)) ⊗ 1(2),
soβ maps to N ⊗HtH. Next, we check that it is both module and comodule map :
β(m ·h) = m(0) ·h(1)S(m(1)h(2)) ⊗m(2)h(3)
= m(0) ·εt(h(1))S(m(1)) ⊗m(2)h(2)
= m(0) ·S(m(1)1(1)) ⊗m(2)1(2)h =β(m) ·h,
β(m(0)) ⊗m(1) = m(0) ·S(m(1)) ⊗m(2) ⊗m(3)
= β(m)(0) ⊗β(m)(1),
Finally, we verify that α ◦β = id and β ◦α = id :
α ◦β(m) = m(0) ·S(m(1))m(2) =m(0) ·εs(m(1))
= m(0) · 1(1)ε(m(1)1(2)) = m(0)ε(m(1)) = m,
β ◦α(n ⊗h) = β(n ·h) = β(n) ·h
= n · 1(1)S(1(2)) ⊗ 1(3)h =n ⊗h,
which completes the proof.
Remark 3.2.6.
∫ l
ˆ H = Coinv ˆH where ˆH is an H-Hopf module as in Example 3.2.4.
Indeed, the condition
λ(1) ⊗λ(2) =λ · 1(1) ⊗ 1(2)
is equivalent to φλ = (S(1(1))⇀λ )⟨φ, 1(2) ⟩ =εt(φ)λ.
Corollary 3.2.7. ˆH ∼=
∫ l
ˆ H ⊗HtH as right H-Hopf modules. In particular,
∫ l
ˆ H is a
non-zero subspace of ˆH.
Proof. TakeM = ˆH in Theorem 3.2.5 and use Remark 3.2.6.
