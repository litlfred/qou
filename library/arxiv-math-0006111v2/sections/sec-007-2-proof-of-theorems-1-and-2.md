---
doc_id: arxiv-math-0006111v2
doc_title: "Approximate factorization and concentration for characters of symmetric groups"
section_id: sec-007-2-proof-of-theorems-1-and-2
section_title: "Proof of Theorems 1 and 2"
section_number: 2
pages: 5-6
source_pdf: 0006111v2.pdf
source_sha256: cd99f45d686eb6e2
doc_brief: "Approximate factorization and concentration for characters of symmetric groups — We prove a factorization-concentration result for characters of s ymmet- ric groups."
---
We shall rely heavily on results of [B], especially Section 4 . Let ψ be a normalized
positive deﬁnite function, then mn(ψ ) =∑
λ ∈Yq
pλmn(λ) is the mean value for Π ψ
of the random variable λ ↦→mn(λ) on Yq. The proof of Theorem 1 consists in
giving an estimate for the variance of this random variable a nd using Markov’s
inequality. The key result is the following whose proof is an alogous to the proof of
Lemma 5.1.1 or 6.1 in [B].
Lemma 2.1. Letn1,n 2,...n k be positive integers, then for every sequence (cl)l≥1
andδ> 0 there exists a constant K such that for all ψ ∈ Fn
c,δ withn =n1 +... +nk,
one has
|τψ (⟨Γ(ψ )n1⟩⟨Γ(ψ )n2⟩... ⟨Γ(ψ )nk ⟩) −τψ (⟨Γ(ψ )n1⟩)τψ (⟨Γ(ψ )n2⟩)...τ ψ (⟨Γ(ψ )nk ⟩)|
≤K(δ +q−1)qn/ 2
Proof. We shall only need the case k = 2 of this Lemma which is what we prove
here. The argument can be easily extended to yield the genera l case, which can be
used to give estimates on higher moments of ⟨Γ(ψ )n⟩ −τψ (⟨Γ(ψ )n⟩).
One has
⟨Γ(ψ )n⟩ = 1
q + 1
∑
0≤i1,i 2,...,i n≤q
rψ ((i1i2)... (in−1in)(ini1))
and analogously
(2.1.1)
⟨Γ(ψ )n1⟩⟨Γ(ψ )n2⟩ =
1
(q + 1)2
∑
0≤i1,i 2,... ,i n1 ≤q
0≤j1 ,j 2 ,... ,j n2 ≤q
rψ
(
(i1i2)... (in1i1)(j1j2)... (jn2j1)
)
where by convention ( ii) is zero and ( ij) = 1 if either i or j (but not both) is 0.
Applying the state τψ one gets
(2.1.2)
τψ (⟨Γ(ψ )n1⟩⟨Γ(ψ )n2⟩) =
1
(q + 1)2
∑
0≤i1,i 2 ,... ,i n1 ≤q
0≤j1 ,j 2 ,... ,j n2 ≤q
ψ
(
(i1i2)... (in1i1)(j1j2)... (jn2j1)
)
We shall compare (2.1.2) to
(2.1.3)
τψ (⟨Γ(ψ )n1⟩)τψ (⟨Γ(ψ )n2⟩) =
1
(q + 1)2
∑
0≤i1,i 2,... ,i n1 ≤q
0≤j1 ,j 2 ,... ,j n2 ≤q
ψ
(
(i1i2)... (in1i1)
)
ψ
(
(j1j2)... (jn2j1)
)
In (2.1.2), since ψ is a central function, the value of
ψ
(
(i1i2)... (in1i1)(j1j2)... (jn2j1)
)
