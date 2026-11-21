---
doc_id: generalised-markov-traces-and-jucys-murphy-element
doc_title: "Glasgow Mathematical Journal (2026), 1–10"
section_id: sec-008-markov-traces-via-jucys-murphy-elements
section_title: "Markov traces via Jucys-Murphy elements"
section_number: null
pages: 5-6
source_pdf: Generalised_Markov_traces_and_Jucys-Murphy_element.pdf
source_sha256: 9246e10a44d0b4aa
toc_source: outline
doc_brief: "Glasgow Mathematical Journal (2026), 1–10 — We give a simple construction of Markov traces for Iwahori–Hecke algebras associated with the crystallographic Coxeter groups of types An, Bn and Dn."
---
Deﬁnition 3.1.1. Let R be a commutative A-algebra. A family (φn) of A-linear functionals φn : H(Xn) →
R, where X is A−1, B or D and n ∈Z≥1 (n ∈Z≥2 in type D) is called a Markov trace if there are elements
μ, ρ ∈R such that the following conditions are satisﬁed:
(M1) φn is a trace function, that is, φn(hh′) = φn(h′h). This property is a generalisation of the ﬁrst
Markov move from the theory of link invariants.
Recall the embedding ι = ιn−1 : H(Xn−1) →H(Xn) deﬁned in Section 2.4. The functionals φn−1
and φn, n ≥2 must satisfy
(U1) φn(ι(h)) = ρφn−1(h). This property is a generalisation of a rule for removing an unlinked circle
in the theory of link invariants.
(M2) φn(ι(h)tn−1) = μφn−1(h). This property is a generalisation of the second Markov move from the
theory of link invariants.
Note that if (φn) is a Markov trace with constants ρ, μ, then, for arbitrary λ1, λ2 ∈R, (λ1λn
2φn) is
again a Markov trace with constants λ2ρ, λ2μ.
Remark 3.1.2. We exclude small n in our deﬁnition of the Markov trace because some special treatment
is needed for the embeddings B0 →B1, D0 →D1 →D2. For the geometric traces, these properties are
extended to small n, see Section 3.3.
Deﬁnition 3.1.3. Assume that the involution v 
→v−1 is extended to R. We say that an element z ∈
H(W, S) ⊗A R represents a functional φ : H(W, S) →R if φ(h) = ⟨z, h⟩for any h ∈H(W, S). It is easy
to see that φ satisﬁes the property (M1) if and only if z is in the centre of H(W, S). In this case, we write
φ = trz.
Let R = A(a) and let a = a−1. Deﬁne
ζn =
n
i=1
(1 + a−1JX
i ), ζ0 = 1,
an element in H(Xn) when X = A−1, B or D. By Corollary 2.5.3, elements ζn are central in the
corresponding Iwahori–Hecke algebras. We prove
6
Kostiantyn Tolmachov and Heorhii Zhylinskyi
Theorem 3.1.4. The family of functionals (trζn) is a Markov trace with constants ρ = 1 + a, μ = v −v−1.
Proof. We ﬁrst check the property (U1). We have
⟨ζn, ι(h)⟩= ⟨ζn−1(1 + a−1JX
n ), ι(h)⟩= ⟨ζn−1, ι(h)⟩+ a⟨ζn−1JX
n , ι(h)⟩.
Applying Proposition 2.4.2 twice – recall that JX
n = S(Xn)−1S(Xn−1) – we get the equality ⟨ζn−1JX
n , ι(h)⟩=
⟨ζn−1, ι(h)⟩and (U1) follows.
We now check the property (M2). We have
⟨ζn, ι(h)tn−1⟩= ⟨ζn−1(1 + a−1JX
n ), ι(h)tn−1⟩= ⟨ζn−1, ι(h)tn−1⟩+ a⟨ζn−1JX
n , ι(h)tn−1⟩
(2)
= ⟨ζn−1, ι(h)t−1
n−1⟩+ (v −v−1)⟨ζn−1, ι(h)⟩+ a⟨ζn−1JX
n , ι(h)tn−1⟩.
From Corollary 2.3.2, we get that ⟨ζn−1, ι(h)t−1
n−1⟩= 0.
For the third summand in the last expression in (2), applying Proposition 2.4.2, we have
⟨ζn−1JX
n , ι(h)tn−1⟩= ⟨ι(h)tn−1, ζn−1S(Xn−1)⟩= 0,
with the last equality again following from Corollary 2.3.2. We obtain (M2).
Remark 3.1.5. Note that in type A the properties (M1), (U1) and (M2) deﬁne the Markov trace uniquely,
and thus the preceding theorem recovers, up to a change of variable, the classical result: a-coeﬃcients of
the Markov trace in type A are represented by the elementary symmetric polynomials in Jucys–Murphy
elements.
Remark 3.1.6. We will show below that, in types A and B (but not in type D), the traces trζn coincide
with the traces coming from geometry. See Section 3.3.
