---
doc_id: arxiv-2006.02042v1
doc_title: "THE STRONG AJ CONJECTURE FOR THE FIGURE EIGHT KNOT"
section_id: sec-008-28-double-checking-the-recurrence-relation
section_title: "Double-checking the recurrence relation"
section_number: 2.8
pages: 9-10
source_pdf: 2006.02042v1.pdf
source_sha256: 9de75ced3a3360bb
doc_brief: "THE STRONG AJ CONJECTURE FOR THE FIGURE EIGHT KNOT — Motivated by the theory of quantum A-ideals of Frohman-Gelca-Lo Faro, the theory of q-holonomicity of quantum invariants of Garoufalidis-Le and"
---
we deﬁne ⟨Q⟩ : Z → R = C[t±1] by
⟨Q⟩(n) := [ n]
n−1∑
k=0
P (t, t2n, t4k)
k∏
l=1
(t4n + t−4n − t4l − t−4l)
for n ≥ 1, and ⟨Q⟩(−n) = − ⟨Q⟩(n) for n ≤ 0. It is known that the colored Jones
polynomial of the ﬁgure eight knot is JE = ⟨1⟩.
For Q, R ∈ C[t, M, x], we write Q ≡ R if Q − R ∈ C[t, M]. Then we have the following.
10 HOANG-AN NGUYEN AND ANH T. TRAN
Lemma 2.2.
L ⟨1⟩ ≡
(
t−2M −4 − t−2M −2 − t2)
⟨1⟩ +
(
t6M 2 − t2M −2)
⟨x⟩,
L2 ⟨1⟩ ≡
{
t−12M −8 −
(
t−12 + t−8)
M −6 − t12M 4 − (t−4 + 1)M −4
+
(
t−4 + 1
)
M −2 + t8 + t4 + 1
}
⟨1⟩
+
{
t16M 6 − t−8M −6 − t12M 4 + t−4M −4 −
(
t12 + t8 + t4)
M 2
+
(
t4 + t−4 + 1
)
M −2}
⟨x⟩,
L−1 ⟨1⟩ ≡
(
t−2M 4 − t−2M 2 − t2)
⟨1⟩ +
(
t6M −2 − t2M 2)
⟨x⟩,
L−2 ⟨1⟩ ≡
{
t−12M 8 −
(
t−12 + t−8)
M 6 − t12M −4 −
(
t−4 + 1
)
M 4
+ (t−4 + 1)M 2 + t8 + t4 + 1
}
⟨1⟩
+
{
t16M −6 − t−8M 6 − t12M −4 + t−4M 4 −
(
t12 + t8 + t4)
M −2
+
(
t4 + t−4 + 1
)
M 2}
⟨x⟩.
Proof. From [CM, Proposition 4.5] we have
L ⟨1⟩ ≡
(
t−2M −4 − t−2M −2 − t2)
⟨1⟩ +
(
t6M 2 − t2M −2)
⟨x⟩,
L⟨x⟩ ≡ (t−2M −2 − t2M 2)⟨1⟩ + (t6M 4 − t2M 2 − t2)⟨x⟩.
By a direct calculation, using the fact that L2⟨1⟩ = L(L⟨1⟩) and the above formulas, we
obtain the formula for L2⟨1⟩. The proofs for L−1 ⟨1⟩ and L−2 ⟨1⟩ are similar. □
Using Lemma 2.2 and a direct calculation we see that
(L2 + L−2 + p1(t, M)L + p−1(t, M)L−1 + p0(t, M))⟨1⟩ ≡ 0.
This means that P JE ∈ R[M ±1].
