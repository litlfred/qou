---
doc_id: arxiv-1611.03697v5
doc_title: "RIEMANN-HILBERT PROBLEMS FROM DONALDSON-THOMAS THEORY"
section_id: sec-023-42-statement-of-the-problem
section_title: "Statement of the problem"
section_number: 4.2
pages: 17-18
source_pdf: 1611.03697v5.pdf
source_sha256: 3d7e5a14a079c8c5
doc_brief: "RIEMANN-HILBERT PROBLEMS FROM DONALDSON-THOMAS THEORY — We study a class of Riemann-Hilbert problems arising naturally in Donald son-Thomas theory."
---
the associated twisted torus. Given a ray r⊂ C∗ we consider the corresponding half-plane
Hr ={t∈ C∗ : t = z· v with z∈ r and Re( v) > 0}⊂ C∗
centered on it. We shall be dealing with functions of the form
Xr : Hr→ T.
Composing with the twisted characters of T we can equivalently consider functions
Xr,γ : Hr→ C∗, X r,γ(t) = xγ(Xr(t)).
The Riemann-Hilbert problem associated to the BPS structure (Γ , Z, Ω) depends on a choice of
element ξ∈ T which we call the constant term. It reads as follows:
Problem 4.3. Fix an element ξ∈ T. For each non-active ray r⊂ C∗, we seek a holomorphic
function Xr : Hr→ T such that the following three conditions are satisﬁed:
(RH1) Jumping. Suppose that two non-active rays r−, r+⊂ C∗ form the boundary rays of a convex
sector ∆ ⊂ C∗, taken in clockwise order. Then
Xr+(t) = S(∆)( Xr−(t)),
for all t∈ Hr−∩ Hr+ with 0 <|t|≪ 1.
(RH2) Finite limit at 0. For each non-active ray r⊂ C∗, and each class γ∈ Γ , we have
exp(Z(γ)/t)· Xr,γ(t)→ ξ(γ)
as t→ 0 in the half-plane Hr.
(RH3) Polynomial growth at ∞. For any class γ∈ Γ , and any non-active ray r⊂ C∗, there exists
k > 0 such that
|t|−k <|Xr,γ(t)| <|t|k,
for t∈ Hr with|t|≫ 0.
To make sense of the condition (RH1) note that by Proposition 4.2 we can ﬁnd R > 0 such that
the partially-deﬁned automorphism S(∆) is well-deﬁned on the open subset U∆ (R)⊂ T. Observe
that if an active class γ∈ Γ satisﬁes Z(γ)∈ ∆, and we take t∈ Hr1∩Hr2, then the quantity Z(γ)/t
has strictly positive real part. Using the support property it follow s (see the proof of Lemma B.2)
that for 0 <|t|≪ 1
exp(−Z/t)· ξ∈ U∆ (R).
18 TOM BRIDGELAND
Condition (RH2) then implies that Xri(t)∈ U∆ (R) whenever t∈ Hr1∩ Hr2 with 0 <|t|≪ 1, so
that the relation (RH1) is indeed well-deﬁned.
Remark 4.4. When the BPS structure (Γ , Z, Ω) is ﬁnite, integral and generic, we can rewrite
the condition (RH1) using Proposition
4.2. Given an active ray ℓ, consider a small anticlockwise
perturbation r−, and a small clockwise perturbation r+, both rays being non-active. Then (RH1)
is the condition that
Xr+,β(t) = Xr−,β(t)·
∏
Z(γ)∈ℓ
(1− Xr±,γ (t))Ω( γ)⟨γ,β ⟩. (21)
Note that the generic assumption ensures there is no need to distin guish the functions Xr±(t) inside
the product, since for classes γ∈ Γ satisfying Z(γ)∈ ℓ they are equal.
It will be useful to consider the maps Yr : Hr→ T+ deﬁned by
exp(Z/t)· Xr(t) = Yr(t)· ξ.
Composing with the characters of T+ we can also encode the solution in the system of maps
Yr,γ(t) = yγ(Yr(t)) = exp( Z(γ)/t)· Xr,γ(t)· ξ(γ)−1.
Of course the maps Xr and Yr are equivalent data: we use whichever is most convenient.
Remark 4.5. It follows from the condition (RH1) that if two non-active rays r1, r2 bound a convex
sector containing no active rays, then the two functions Xri : Hri → T required in Problem 4.3
glue together to give a holomorphic function on Hr1∪ Hr2. It follows that if a non-active ray
r⊂ C∗ is not a limit of active rays, then the corresponding function Xr extends analytically to a
neighbourhood of the closure of Hr⊂ C∗.
