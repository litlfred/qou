---
doc_id: arxiv-1611.03697v5
doc_title: "RIEMANN-HILBERT PROBLEMS FROM DONALDSON-THOMAS THEORY"
section_id: sec-032-53-the-finite-uncoupled-case
section_title: "The finite uncoupled case"
section_number: 5.3
pages: 26-27
source_pdf: 1611.03697v5.pdf
source_sha256: 3d7e5a14a079c8c5
toc_source: outline
doc_brief: "RIEMANN-HILBERT PROBLEMS FROM DONALDSON-THOMAS THEORY — We study a class of Riemann-Hilbert problems arising naturally in Donaldson-Thomas theory."
---
can construct a unique solution to the Riemann-Hilbert problem by superposing the solutions from
the previous section.
Theorem 5.3. Let (Z, Γ, Ω) be a ﬁnite, uncoupled, integral BPS structure. Suppose that ξ ∈T
satisﬁes ξ(γ) = 1 for all active classes γ ∈Γ. Then the corresponding Riemann-Hilbert problem
has a unique solution, which associates to a non-active ray r the function
Yr,β(t) =
Y
Z(γ)∈iHr
Λ
Z(γ)
2πit
Ω(γ)⟨β,γ⟩
(29)
where the product is taken over the ﬁnitely many active classes γ ∈Γ for which Z(γ) ∈iHr.
Proof. Note ﬁrst that the expression (29) is holomorphic and non-zero on Hr because in each factor
both Z(γ)/i and t lie in Hr, so the argument of Λ does not lie in R<0. The properties (RH2) and
(RH3) then follow immediately as in the proof of Proposition 5.2. Consider two non-active rays
r−and r+ obtained by small perturbations, anti-clockwise and clockwise respectively, of an active
ray ℓ. Then ℓ⊂iHr+ whereas −ℓ⊂iHr−. Assume that t ∈Hr−∩Hr+. Then t ∈Hℓand hence
−Z(γ)/2πit lies in the upper half-plane whenever Z(γ) ∈ℓ. Using (28) we therefore obtain
Xr+,β(t)
Xr−,β(t) =
Y
Z(γ)∈ℓ

Λ
Z(γ)
2πit

· Λ
−Z(γ)
2πit
Ω(γ)⟨β,γ⟩
=
Y
Z(γ)∈ℓ
(1 −e−Z(γ)/t)Ω(γ)⟨γ,β⟩
This is precisely the condition (21) since Lemma 4.8 and the assumption on ξ implies that Xγ(t) =
exp(−Z(γ)/t) whenever Ω(γ)̸ = 0.
□
Using the Stirling expansion we obtain an asymptotic expansion
log Xr,β(t) ∼Z(β)
t
−2πiθ(β) +
X
g≥1
X
γ∈Γ
Ω(γ)⟨β, γ⟩B2g
4g (2g −1)
 2πit
Z(γ)
2g−1
,
(30)
valid as t →0 in the half-plane Hr. We have set ξ(β) = exp(2πiθ(β)). The extra factor of 2 in
the denominator arises because in (29) we take a product over half the classes in Γ. Note that this
expansion is independent of the choice of ray r ⊂C∗.
