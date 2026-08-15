---
doc_id: arxiv-1611.03697v5
doc_title: "RIEMANN-HILBERT PROBLEMS FROM DONALDSON-THOMAS THEORY TOM BRIDGELAND"
section_id: sec-047-b5-birational-transformations
section_title: "B.5. Birational transformations"
section_number: null
pages: 48-50
source_pdf: 1611.03697v5.pdf
source_sha256: 3d7e5a14a079c8c5
doc_brief: "RIEMANN-HILBERT PROBLEMS FROM DONALDSON-THOMAS THEORY TOM BRIDGELAND — We study a class of Riemann-Hilbert problems arising naturally in Donald son-Thomas theory."
---
Soibelman [23, Section 2.5]. Suppose that a ray ℓ contains a single active class γ, and that moreover
RIEMANN-HILBERT PROBLEMS FROM DONALDSON-THOMAS THEORY 49
Ω( γ) = 1. The series DT( ℓ) is then the dilogarithm
DT(ℓ) =−
∑
n≥1
xnγ
n2 =−
∑
n≥1
xn
γ
n2 .
This converges absolutely for|xγ| < 1 and hence deﬁnes a holomorphic function on the open subset
U(R) ={f∈ T :|f (γ)| < e −R}⊂ T,
for any R > 0. The argument of Proposition B.3 shows that the associated time 1 Hamiltonian
ﬂow S(ℓ) is well-deﬁned on U(R), and indeed we can directly compute
S(ℓ)∗(xβ) = exp
{
−
∑
n≥1
xn
γ
n2 ,−
}
(xβ) = xβ· exp
(
−
∑
n≥1
xn
γ
n2·⟨ nγ, β⟩
)
= xβ· exp
(
⟨γ, β⟩log(1− xγ)
)
= xβ· (1− xγ)⟨γ,β ⟩.
Thus the map S(ℓ) extends holomorphically to the Zariski open subset of T which is the complement
of the divisor xγ = 1. It therefore deﬁnes a birational automorphism of T.
Proposition B.6. Suppose that (Γ , Z, Ω) is a generic, integral and ray-ﬁnite BPS structure. Then
for any ray ℓ⊂ C∗ the BPS automorphism S(ℓ) extends to a birational automorphism of T, whose
action on twisted characters is given by
S(ℓ)∗(xβ) = xβ·
∏
Z(γ)∈ℓ
(1− xγ) Ω( γ)·⟨γ,β ⟩. (64)
Proof. The argument of Proposition B.3 shows that the automorphism S(ℓ) is well-deﬁned on a
suitable open subset of T. Under the generic assumption the Hamiltonian ﬂows of the charact ers
appearing in the function DT( ℓ) commute, so we can compute as before
S(ℓ)∗(xβ) = exp
{
−
∑
Z(γ)∈ℓ
∑
n≥1
Ω( γ)· xn
γ
n2 ,−
}
(xβ) = xβ· exp
(
−
∑
n≥1
∑
Z(γ)∈ℓ
Ω( γ)· xn
γ
n2·⟨ nγ, β⟩
)
= xβ· exp
( ∑
Z(γ)∈ℓ
⟨γ, β⟩Ω( γ) log(1− xγ)
)
= xβ·
∏
Z(γ)∈ℓ
(1− xγ) Ω( γ)·⟨γ,β ⟩.
When the invariants Ω( γ) are integers this is clearly a birational automorphism of T. □
50 TOM BRIDGELAND
