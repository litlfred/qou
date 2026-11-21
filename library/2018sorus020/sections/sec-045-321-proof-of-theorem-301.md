---
doc_id: 2018sorus020
doc_title: "Reidemeister torsion on character varieties"
section_id: sec-045-321-proof-of-theorem-301
section_title: "Proof of Theorem 3.0.1"
section_number: 3.2.1
pages: 87-88
source_pdf: 2018SORUS020.pdf
source_sha256: c3f929e5195983ce
toc_source: inferred
doc_brief: "Reidemeister torsion on character varieties — 52 sections: Front matter; Introduction; Character varieties and Reidemeist"
---
Proof of Theorem 3.0.1
In this section we give a proof of the following theorem :
Theorem (Theorem 3.0.1). Let X be a one dimensional component of the character
variety X(M) and ρ : π1(M) →SL2(k(X)) the tautological representation. Assume
86
that the complex C∗(M, ρ) is acyclic. Then tor(M, ρ) is a regular function on X.
Moreover its vanishing order at a point χ ∈X is given by the length of the torsion
module H2(M, ρ)v, where v is the valuation associated to x on the function ﬁeld
k(X). In particular it vanishes if and only if H1(M, ¯ρ) is non trivial, where ¯ρ is the
residual representation ¯ρ : π1(M)
ρ−→SL2(Ov)
mod t
−−−→SL2(k).
The main tool of the proof is the following theorem already used in Section 2.3.
Recall that a complex of Ov-modules C∗such that C∗⊗k(X) is an exact complex is
said rationally exact, and that the length of a torsion Ov-module ⊕kOv/(tnk) equals
P nk.
Theorem 3.2.1. [GKZ94, Theorem 30] Let χ ∈X a character, and v a valuation
on k(X) associated to χ. If C∗is a rationally exact based complex of Ov-modules
with basis {ci}, then
v(tor(C∗⊗k(X), {ci})) =
X
k
(−1)k length(Hk(C∗))
Proof of Theorem 3.0.1. Since the complex C∗(M, ρ) is acyclic, the theorem above
applies. Now notice that the Hi(M, ρ)v are torsion modules. As a submodule of a free
module, H0(M, ρ)v is trivial. Then Proposition 1.4.2 implies that no character χ ∈X
is central, in particular H0(M, ¯ρ) is trivial. But the Universal Coeﬃcients Theorem
provide the isomorphisms H0(M, ¯ρ) ≃H0(M, ¯ρ)∗, and H0(M, ¯ρ) ≃H0(M, ρ)v ⊗
k, thus we have proved that H0(M, ρ)v is trivial. Again by the U.C. Theorem we
have Ext(H1(M, ρ)v, Ov) ≃H0(M, ρ)v = {0}, and we conclude that H1(M, ρ)v ≃
Ext(H1(M, ρ)v, Ov) = {0} because its a torsion module. In conclusion we have
proved the ﬁrst part of the theorem
v(tor(M, ρ)) = length(H2(M, ρ)v)
Now H2(M, ρ)v being trivial is equivalent to H2(M, ¯ρ) being trivial which is the
same that H1(M, ¯ρ) being trivial, and the theorem is proved.
