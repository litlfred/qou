---
doc_id: arxiv-1611.03697v5
doc_title: "RIEMANN-HILBERT PROBLEMS FROM DONALDSON-THOMAS THEORY TOM BRIDGELAND"
section_id: sec-026-45-null-vectors-and-uniqueness
section_title: "Null vectors and uniqueness"
section_number: 4.5
pages: 20-22
source_pdf: 1611.03697v5.pdf
source_sha256: 3d7e5a14a079c8c5
doc_brief: "RIEMANN-HILBERT PROBLEMS FROM DONALDSON-THOMAS THEORY TOM BRIDGELAND — We study a class of Riemann-Hilbert problems arising naturally in Donald son-Thomas theory."
---
corresponding twisted torus.
Deﬁnition 4.7. An element γ∈ Γ will be called null if it satisﬁes ⟨α, γ⟩ = 0 for all active classes
α∈ Γ. A twisted character xγ : T→ C∗ corresonding to a null element γ∈ Γ will be called a
coeﬃcient.
Note that the deﬁnition of the wall-crossing automorphisms S(ℓ) shows that they ﬁx all coeﬃ-
cients: S(ℓ)∗(xγ) = xγ. This leads to the following partial uniqueness result.
Lemma 4.8. Let (Z, Γ , Ω) be a convergent BPS structure and γ∈ Γ a null element. Then for any
solution to the Riemann-Hilbert problem, and any non-activ e ray r⊂ C∗, one has Yr,γ(t) = 1 for
all t∈ Hr.
Proof. Since coeﬃcients are unchanged by wall-crossing, condition (RH1) s hows that the functions
Yr,γ(t) for diﬀerent rays r⊂ C∗ piece together to give a single holomorphic function Yγ : C∗→ C∗.
RIEMANN-HILBERT PROBLEMS FROM DONALDSON-THOMAS THEORY 21
Since we can cover C∗ by the half-planes Hri deﬁned by ﬁnitely many non-active rays ri⊂ C∗,
condition (RH2) shows that this function has a removable singularity at 0∈ C with value Yγ(0) = 1,
and condition (RH3) shows that it has at worst polynomial growth at ∞. It follows that Yγ extends
to a meromorphic function CP1→ CP1 which has neither zeroes nor poles on C. This implies that
Yγ(t) is constant, which proves the result. □
Recall the deﬁnition of an uncoupled BPS structure from Section 2.6.
Lemma 4.9. Let (Z, Γ , Ω) be a ﬁnite, uncoupled, integral BPS structure. Then the asso ciated
Riemann-Hilbert problem has at most one solution.
Proof. Note that uncoupled BPS structures are in particular generic, so R emark 4.4 applies. Fix
an arbitrary class β∈ Γ. The uncoupled condition implies that all classes γ∈ Γ appearing in
the product on the right-hand side of ( 21) are null. Lemma 4.8 shows that for these classes the
corresponding functions
Xr,γ(t) = exp(−Z(γ)/t)· ξ(γ)
are uniquely determined. It follows that if we have two systems of so lutions
X (i)
r,β(t) : Hr→ C∗, i = 1, 2,
to the Riemann-Hilbert problem, then the ratios
qr,β(t) = X (2)
r,β (t)· (X (1)
r,β (t))−1 : Hr→ C∗
piece together to give a single holomorphic function qβ : C∗→ C∗. Arguing exactly as in Lemma
4.8, we can use conditions (RH2) and (RH3) to conclude that qβ(t) = 1 for all t∈ C∗, which proves
the claim. □
Remark 4.10. Let (Γ , Z, Ω) be a convergent BPS structure, and consider the doubled BPS s truc-
ture (Γ⊕ Γ ∨, Z, Ω) of Section 2.8. For each class γ∈ Γ the corresponding element
γD = (γ,⟨−, γ⟩)∈ Γ⊕ Γ ∨
is null, because, by the formula ( 11), it is orthogonal to any class of the form ( α, 0)∈ Γ⊕ Γ ∨.
Lemma 4.8 therefore implies that any solution to the Riemann-Hilbert problem fo r the double
satisﬁes YγD,r(t) = 1. This implies that
Yr,(0,⟨γ,−⟩)(t) = Yr,(γ,0)(t),
for all non-active rays r⊂ C∗, and all t∈ Hr.
22 TOM BRIDGELAND
In this way one sees that if a BPS structure has a non-degenerate form⟨−,−⟩, then solving
the Riemann-Hilbert problem for the doubled BPS structure is precis ely equivalent to solving the
problem for the original BPS structure. However, when the form ⟨−,−⟩ is degenerate, a solution
to the Riemann-Hilbert problem for the doubled BPS structure cont ains strictly more information
than a solution to the original problem. We will see an example of this in S ection 5.1 below.
