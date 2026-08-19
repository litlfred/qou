---
doc_id: arxiv-1611.03697v5
doc_title: "RIEMANN-HILBERT PROBLEMS FROM DONALDSON-THOMAS THEORY TOM BRIDGELAND"
section_id: sec-022-41-analytic-bps-automorphisms
section_title: "Analytic BPS automorphisms"
section_number: 4.1
pages: 15-17
source_pdf: 1611.03697v5.pdf
source_sha256: 3d7e5a14a079c8c5
doc_brief: "RIEMANN-HILBERT PROBLEMS FROM DONALDSON-THOMAS THEORY TOM BRIDGELAND — We study a class of Riemann-Hilbert problems arising naturally in Donald son-Thomas theory."
---
are proved in Appendix B. Let (Γ , Z, Ω) be a BPS structure, let T be the associated twisted torus,
and ﬁx an acute sector ∆ ⊂ C∗. For each real number R > 0 deﬁne the open subset U∆ (R)⊂ T
to be the interior of the subset
{
g∈ T : Z(γ)∈ ∆ and Ω( γ)⁄= 0 =⇒ |g(γ)| < exp(−R‖γ‖)
}
⊂ T.
It follows from the support property that the subset U∆ (R)⊂ T is non-empty (see Lemma B.2).
Recall the deﬁnition of the height of a ray ℓ⊂ C∗ from Section 2.5.
Proposition 4.1. Let (Γ , Z, Ω) be a convergent BPS structure, and ∆ ⊂ C∗ a convex sector. For
suﬃciently large R > 0 the following statements hold:
16 TOM BRIDGELAND
(i) For each ray ℓ⊂ ∆ , the series (8) deﬁning DT(ℓ) is absolutely convergent on U∆ (R), and
hence deﬁnes a holomorphic function
DT(ℓ) : U∆ (R)→ C.
(ii) The time 1 Hamiltonian ﬂow of the function DT(ℓ) with respect to the Poisson structure
{−,−} on T deﬁnes a holomorphic embedding
S(ℓ) : U∆ (R)→ T.
(iii) For each H > 0, the composition in anti-clockwise order
S<H (∆) = Sℓ1◦ Sℓ2◦···◦ Sℓk ,
corresponding to the ﬁnitely many rays ℓi⊂ ∆ of height < H exists, and the pointwise limit
S(∆) = lim
H→∞
S<H(∆) : U∆ (R)→ T
is a well-deﬁned holomorphic embedding.
Proof. See Appendix B, Proposition B.3. □
We think of the maps S(ℓ) of Proposition 4.1 as being partially-deﬁned automorphisms of the
twisted torus T. We will usually restrict attention to BPS structures which, in the te rminology of
Section 2.6, are ray-ﬁnite, generic and integral. The maps S(ℓ) can then be computed using the
following result.
Proposition 4.2. Suppose that (Γ , Z, Ω) is ray-ﬁnite, generic and integral. Then for any ray
ℓ⊂ C∗ the embedding S(ℓ) of Proposition
4.1 extends to a birational automorphism of T, whose
action on twisted characters is given by
S(ℓ)∗(xβ) = xβ·
∏
Z(γ)∈ℓ
(1− xγ) Ω( γ)⟨γ,β ⟩. (20)
Proof. See Appendix B, Proposition B.6. □
Note that if the BPS structure (Γ , Z, Ω) satisﬁes the stronger condition of being ﬁnite, then there
are only ﬁnitely many active rays, so for any acute sector ∆ ⊂ C∗ the map S(∆) of Proposition
4.1 also extends to a birational automorphism of T.
RIEMANN-HILBERT PROBLEMS FROM DONALDSON-THOMAS THEORY 17
