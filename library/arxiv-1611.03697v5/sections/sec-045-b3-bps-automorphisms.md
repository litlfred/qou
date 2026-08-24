---
doc_id: arxiv-1611.03697v5
doc_title: "RIEMANN-HILBERT PROBLEMS FROM DONALDSON-THOMAS THEORY"
section_id: sec-045-b3-bps-automorphisms
section_title: "B.3. BPS automorphisms"
section_number: null
pages: 45-47
source_pdf: 1611.03697v5.pdf
source_sha256: 3d7e5a14a079c8c5
doc_brief: "RIEMANN-HILBERT PROBLEMS FROM DONALDSON-THOMAS THEORY — We study a class of Riemann-Hilbert problems arising naturally in Donald son-Thomas theory."
---
∆ ⊂ C∗. Recall the deﬁnition of the formal series DT( ℓ) associated to a ray ℓ⊂ C∗ from Section
2.5. In this section we show that this series is absolutely convergent on suitable open subsets of
T and that the Hamiltonian ﬂow of the resulting holomorphic function giv es a partially-deﬁned
automorphism of T in the precise sense described in the last subsection.
Proposition B.3. For all suﬃciently large R > 0 the following statements hold. For each ray
ℓ⊂ ∆ , the power series DT(ℓ) is absolutely convergent on U∆ (R), and hence deﬁnes a holomorphic
function
DT(ℓ) : U∆ (R)→ C.
Moreover the time 1 Hamiltonian ﬂow of this function gives a h olomorphic map
S(ℓ) : U∆ (R)→ T
which deﬁnes an invertible, bounded ∆ -map germ.
46 TOM BRIDGELAND
Proof. Take assumptions as in the statement and choose ǫ > 0. For convenience we choose the
norm‖·‖ on Γ Z⊗ R so that for all β, γ∈ Γ there is an inequality
|⟨β, γ⟩| <‖β‖·‖ γ‖. (56)
Take R > 0 satisfying the conclusion of Lemma B.1. Thus for each ray ℓ⊂ ∆ we can choose
M(ℓ) > 0 such that
∑
Z(γ)∈ℓ
‖γ‖p·| DT(γ)|· e−R‖γ‖ < M (ℓ), (57)
for each p∈{ 0, 1, 2}, and such that
∑
ℓ⊂∆
M(ℓ) < ǫ. (58)
Since the‖γ‖ are bounded below, the p = 0 case of ( 57) immediately implies that for each point
ξ∈ U∆ (R)
∑
Z(γ)∈ℓ
| DT(γ)|·| xγ(ξ)| <
∑
Z(γ)∈ℓ
| DT(γ)|· e−R‖γ‖ <∞, (59)
which proves that DT( ℓ) is absolutely convergent.
The Hamiltonian ﬂow of DT( ℓ) is deﬁned by the diﬀerential equation
dxβ
dt ={DT(ℓ), xβ} = xβ·
∑
Z(γ)∈ℓ
DT(γ)·⟨ γ, β⟩· xγ. (60)
Using ( 56) it follows that providing the ﬂow stays in U∆ (R) it satisﬁes
⏐
⏐
⏐ d
dt log xβ
⏐
⏐
⏐≤
∑
Z(γ)∈ℓ
| DT(γ)|·‖ β‖·‖ γ‖· e−R‖γ‖ < M (ℓ)·‖ β‖. (61)
Let us consider an integral curve φ(t) for this ﬂow which starts at some point φ(0)∈ U∆ (R + ǫ).
We claim that this curve extends to all times t∈ [0, 1] and remains in U∆ (R). It follows from this
that the time 1 Hamiltonian ﬂow S(ℓ) exists, and deﬁnes a holomorphic map
S(ℓ) : U∆ (R + ǫ)→ U∆ (R).
Since we can make ǫ > 0 arbitrarily small by increasing R > 0, the resulting ∆-map germ is
bounded. Considering the opposite ﬂow then shows that the map is in vertible, which completes
the proof of Proposition
B.3.
RIEMANN-HILBERT PROBLEMS FROM DONALDSON-THOMAS THEORY 47
To prove the claim, let us deﬁne t0 ∈ [0, 1] to be the supremum of s∈ [0, 1] such that the
integral curve φ(t) can be extended to a map φ : [0 , s]→ U∆ (R). We obtain an integral curve
φ : [0 , t0)→ U∆ (R). Equation ( 61) implies that
e−M (ℓ)·‖β‖·| xβ(φ(0))|≤| xβ(φ(t))|≤ eM (ℓ)·‖β‖·| xβ(φ(0))| (62)
for 0≤ t < t 0. Thus the ﬂow stays in the compact subset of T deﬁned by these inequalities, and
hence extends to a ﬂow φ : [0 , t0]→ T. Applying ( 62) to the active classes β∈ Γ then shows that
φ(t0)∈ U∆ (R). But now local existence of solutions to ( 60) shows that we can extend the ﬂow a
little further, which contradicts the deﬁnition of t0 unless t0 = 1. This proves the claim. □
